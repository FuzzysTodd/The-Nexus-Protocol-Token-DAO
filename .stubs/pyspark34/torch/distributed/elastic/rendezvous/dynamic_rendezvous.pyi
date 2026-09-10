import abc
from .api import RendezvousHandler, RendezvousParameters
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from torch.distributed import Store
from typing import Any, Callable, Dict, Set, Tuple

__all__ = ['RendezvousBackend', 'RendezvousTimeout', 'RendezvousSettings', 'DynamicRendezvousHandler', 'create_handler']

Token = Any

class RendezvousBackend(ABC, metaclass=abc.ABCMeta):
    """Represents a backend that holds the rendezvous state."""
    @property
    @abstractmethod
    def name(self) -> str:
        """Gets the name of the backend."""
    @abstractmethod
    def get_state(self) -> Tuple[bytes, Token] | None:
        """Gets the rendezvous state.

        Returns:
            A tuple of the encoded rendezvous state and its fencing token or
            ``None`` if no state is found in the backend.

        Raises:
            RendezvousConnectionError:
                The connection to the backend has failed.
            RendezvousStateError:
                The rendezvous state is corrupt.
        """
    @abstractmethod
    def set_state(self, state: bytes, token: Token | None = None) -> Tuple[bytes, Token, bool] | None:
        """Sets the rendezvous state.

        The new rendezvous state is set conditionally:

          - If the specified ``token`` matches the fencing token stored in the
            backend, the state will be updated. The new state will be returned
            to the caller along with its fencing token.
          - If the specified ``token`` does not match the fencing token stored
            in the backend, the state won't be updated; instead the existing
            state along with its fencing token will be returned to the caller.
          - If the specified ``token`` is ``None``, the new state will be set
            only if there is no existing state in the backend. Either the new
            state or the existing state along with its fencing token will be
            returned to the caller.

        Args:
            state:
                The encoded rendezvous state.
            token:
                An optional fencing token that was retrieved by a previous call
                to :py:meth:`get_state` or ``set_state()``.

        Returns:
            A tuple of the serialized rendezvous state, its fencing token, and
            a boolean value indicating whether our set attempt succeeded.

        Raises:
            RendezvousConnectionError:
                The connection to the backend has failed.
            RendezvousStateError:
                The rendezvous state is corrupt.
        """

class RendezvousTimeout:
    """Holds the timeout configuration of a rendezvous.

    Args:
        join:
            The time within which the rendezvous is expected to complete.
        last_call:
            An additional wait amount before completing the rendezvous once the
            rendezvous has the minimum number of required participants.
        close:
            The time within which the rendezvous is expected to close after a
            call to :py:meth:`RendezvousHandler.set_closed` or
            :py:meth:`RendezvousHandler.shutdown`.
        keep_alive:
            The time within which a keep-alive heartbeat is expected to
            complete.
    """
    def __init__(self, join: timedelta | None = None, last_call: timedelta | None = None, close: timedelta | None = None, heartbeat: timedelta | None = None) -> None: ...
    @property
    def join(self) -> timedelta:
        """Gets the join timeout."""
    @property
    def last_call(self) -> timedelta:
        """Gets the last call timeout."""
    @property
    def close(self) -> timedelta:
        """Gets the close timeout."""
    @property
    def heartbeat(self) -> timedelta:
        """Gets the keep-alive heartbeat timeout."""

@dataclass(repr=False, eq=False, frozen=True)
class RendezvousSettings:
    """Holds the settings of the rendezvous.

    Attributes:
        run_id:
            The run id of the rendezvous.
        min_nodes:
            The minimum number of nodes to admit to the rendezvous.
        max_nodes:
            The maximum number of nodes to admit to the rendezvous.
        timeout:
            The timeout configuration of the rendezvous.
        keep_alive_interval:
            The amount of time a node waits before sending a heartbeat to keep
            it alive in the rendezvous.
        keep_alive_max_attempt:
            The maximum number of failed heartbeat attempts after which a node
            is considered dead.
    """
    run_id: str
    min_nodes: int
    max_nodes: int
    timeout: RendezvousTimeout
    keep_alive_interval: timedelta
    keep_alive_max_attempt: int
    def __init__(self, run_id, min_nodes, max_nodes, timeout, keep_alive_interval, keep_alive_max_attempt) -> None: ...

@dataclass(eq=True, order=True, frozen=True)
class _NodeDesc:
    """Describes a node in the rendezvous.

    Attributes:
        addr:
            The FQDN of the node or user specified local node address.
        pid:
            The id of the process in which the rendezvous handler runs.
        local_id:
            A process-wide unique id.
    """
    addr: str
    pid: int
    local_id: int
    def __init__(self, addr, pid, local_id) -> None: ...

class _NodeDescGenerator:
    """Generates node descriptors.

    A node descriptor is a combination of an FQDN, a process id, and an auto-
    incremented integer that uniquely identifies a node in the rendezvous.
    """
    def __init__(self) -> None: ...
    def generate(self, local_addr: str | None = None) -> _NodeDesc: ...

class _RendezvousState:
    """Holds the state of a rendezvous.

    Attributes:
        round:
            The current round of the rendezvous.
        complete:
            A boolean value indicating whether the current round of the
            rendezvous is complete.
        deadline:
            The time at which the current round of the rendezvous will be
            considered complete if it is still waiting for nodes to join.
        closed:
            A boolean value indicating whether the rendezvous is closed.
        participants:
            A dictionary of the participants and their corresponding ranks.
        wait_list:
            A set of nodes that are waiting to participate in the next round of
            the rendezvous.
        last_heartbeats:
            A dictionary containing each node's last heartbeat time.
    """
    round: int
    complete: bool
    deadline: datetime | None
    closed: bool
    participants: Dict[_NodeDesc, int]
    wait_list: Set[_NodeDesc]
    last_heartbeats: Dict[_NodeDesc, datetime]
    def __init__(self) -> None: ...

class _RendezvousStateHolder(ABC, metaclass=abc.ABCMeta):
    """Holds the shared rendezvous state synced with other nodes."""
    @property
    @abstractmethod
    def state(self) -> _RendezvousState:
        """Gets the local state."""
    @abstractmethod
    def sync(self) -> bool | None:
        """Reads or writes the latest state.

        Returns:
            A boolean value indicating whether the local state, in case marked
            as dirty, was successfully synced with other nodes.
        """
    @abstractmethod
    def mark_dirty(self) -> None:
        """Marks the local state as dirty."""

class _BackendRendezvousStateHolder(_RendezvousStateHolder):
    """Holds the rendezvous state synced with other nodes via a backend.

    Args:
        backend:
            The rendezvous backend to use.
        settings:
            The rendezvous settings.
        cache_duration:
            The amount of time, in seconds, to cache the last rendezvous state
            before requesting it from the backend again.
    """
    def __init__(self, backend: RendezvousBackend, settings: RendezvousSettings, cache_duration: int = 1) -> None: ...
    @property
    def state(self) -> _RendezvousState:
        """See base class."""
    def sync(self) -> bool | None:
        """See base class."""
    def mark_dirty(self) -> None:
        """See base class.

        If the local rendezvous state is dirty, the next sync call will try to
        write the changes back to the backend. However this attempt might fail
        if another node, which had the same state, also made changes and wrote
        them before us.
        """

class _Action(Enum):
    """Specifies the possible actions based on the state of the rendezvous."""
    KEEP_ALIVE: int
    ADD_TO_PARTICIPANTS: int
    ADD_TO_WAIT_LIST: int
    REMOVE_FROM_PARTICIPANTS: int
    REMOVE_FROM_WAIT_LIST: int
    MARK_RENDEZVOUS_COMPLETE: int
    MARK_RENDEZVOUS_CLOSED: int
    SYNC: int
    ERROR_CLOSED: int
    ERROR_TIMEOUT: int
    FINISH: int

class _RendezvousContext:
    """Holds the context of the rendezvous.

    Attributes:
        node:
            The node descriptor associated with the current rendezvous handler
            instance.
        state:
            The current state of the rendezvous.
        settings:
            The rendezvous settings.
    """
    node: _NodeDesc
    state: _RendezvousState
    settings: RendezvousSettings
    def __init__(self, node: _NodeDesc, state: _RendezvousState, settings: RendezvousSettings) -> None: ...

class _RendezvousOpExecutor(ABC, metaclass=abc.ABCMeta):
    """Executes rendezvous operations."""
    @abstractmethod
    def run(self, state_handler: Callable[[_RendezvousContext, float], _Action], deadline: float) -> None:
        """Executes a rendezvous operation.

        An operation is run inside a state machine and is expected to transition
        the rendezvous from one state to another.

        Args:
            state_handler:
                A callable that is expected to return the next state transition
                action based on the current state of the rendezvous.
            deadline:
                The time, in seconds, at which the operation will be considered
                timed-out.
        """

class _DistributedRendezvousOpExecutor(_RendezvousOpExecutor):
    """Executes rendezvous operations using a shared state.

    Args:
        node:
            The node descriptor associated with the current rendezvous handler
            instance.
        state_holder:
            The ``RendezvousStateHolder`` to use to sync the rendezvous state
            with other nodes.
        settings:
            The rendezvous settings.
    """
    def __init__(self, node: _NodeDesc, state_holder: _RendezvousStateHolder, settings: RendezvousSettings) -> None: ...
    def run(self, state_handler: Callable[[_RendezvousContext, float], _Action], deadline: float) -> None:
        """See base class."""

class _RendezvousExitOp:
    """Represents a rendezvous exit operation."""
    def __call__(self, ctx: _RendezvousContext, deadline: float) -> _Action: ...

class _RendezvousJoinOp:
    """Represents a rendezvous join operation."""
    def __call__(self, ctx: _RendezvousContext, deadline: float) -> _Action: ...

class _RendezvousCloseOp:
    """Represents a rendezvous close operation."""
    def __call__(self, ctx: _RendezvousContext, deadline: float) -> _Action: ...

class _RendezvousKeepAliveOp:
    """Represents a rendezvous keep-alive update operation."""
    def __call__(self, ctx: _RendezvousContext, deadline: float) -> _Action: ...

class DynamicRendezvousHandler(RendezvousHandler):
    """Represents a handler that sets up a rendezvous among a set of nodes."""
    @classmethod
    def from_backend(cls, run_id: str, store: Store, backend: RendezvousBackend, min_nodes: int, max_nodes: int, local_addr: str | None = None, timeout: RendezvousTimeout | None = None):
        """Creates a new :py:class:`DynamicRendezvousHandler`.

        Args:
            run_id:
                The run id of the rendezvous.
            store:
                The C10d store to return as part of the rendezvous.
            backend:
                The backend to use to hold the rendezvous state.
            min_nodes:
                The minimum number of nodes to admit to the rendezvous.
            max_nodes:
                The maximum number of nodes to admit to the rendezvous.
            local_addr:
                The local node adress.
            timeout:
                The timeout configuration of the rendezvous.
        """
    def __init__(self, node: _NodeDesc, settings: RendezvousSettings, backend_name: str, store: Store, state_holder: _RendezvousStateHolder) -> None: ...
    @property
    def settings(self) -> RendezvousSettings:
        """Gets the settings of the rendezvous."""
    def get_backend(self) -> str:
        """See base class."""
    def next_rendezvous(self) -> Tuple[Store, int, int]:
        """See base class."""
    def is_closed(self) -> bool:
        """See base class."""
    def set_closed(self) -> None:
        """See base class."""
    def num_nodes_waiting(self) -> int:
        """See base class."""
    def get_run_id(self) -> str:
        """See base class."""
    def shutdown(self) -> bool:
        """See base class."""

def create_handler(store: Store, backend: RendezvousBackend, params: RendezvousParameters) -> DynamicRendezvousHandler:
    """Creates a new :py:class:`DynamicRendezvousHandler` from the specified
    parameters.

    Args:
        store:
            The C10d store to return as part of the rendezvous.
        backend:
            The backend to use to hold the rendezvous state.

    +-------------------+------------------------------------------------------+
    | Parameter         | Description                                          |
    +===================+======================================================+
    | join_timeout      | The total time, in seconds, within which the         |
    |                   | rendezvous is expected to complete. Defaults to 600  |
    |                   | seconds.                                             |
    +-------------------+------------------------------------------------------+
    | last_call_timeout | An additional wait amount, in seconds, before        |
    |                   | completing the rendezvous once the minimum number of |
    |                   | nodes has been reached. Defaults to 30 seconds.      |
    +-------------------+------------------------------------------------------+
    | close_timeout     | The time, in seconds, within which the rendezvous is |
    |                   | expected to close after a call to                    |
    |                   | :py:meth:`RendezvousHandler.set_closed` or           |
    |                   | :py:meth:`RendezvousHandler.shutdown`. Defaults to   |
    |                   | 30 seconds.                                          |
    +-------------------+------------------------------------------------------+
    """
