import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from torch.distributed import Store as Store
from typing import Any, Callable, Tuple

class RendezvousError(Exception):
    """Represents the base type for rendezvous errors."""
class RendezvousClosedError(RendezvousError):
    """Raised when a rendezvous is closed."""
class RendezvousTimeoutError(RendezvousError):
    """Raised when a rendezvous did not complete on time."""
class RendezvousConnectionError(RendezvousError):
    """Raised when the connection to a rendezvous backend has failed."""
class RendezvousStateError(RendezvousError):
    """Raised when the state of a rendezvous is corrupt."""

class RendezvousHandler(ABC, metaclass=abc.ABCMeta):
    """Main rendezvous interface.

    Note:
        Distributed Torch users normally **do not** need to implement their own
        ``RendezvousHandler``. An implementation based on C10d Store is already
        provided, and is recommended for most users.
    """
    @abstractmethod
    def get_backend(self) -> str:
        """Returns the name of the rendezvous backend."""
    @abstractmethod
    def next_rendezvous(self) -> Tuple[Store, int, int]:
        """Main entry-point into the rendezvous barrier.

        Blocks until the rendezvous is complete and the current process is
        included in the formed worker group, or a timeout occurs, or the
        rendezvous was marked closed.

        Returns:
            A tuple of :py:class:`torch.distributed.Store`, ``rank``, and
            ``world size``.

        Raises:
            RendezvousClosedError:
                The rendezvous is closed.
            RendezvousConnectionError:
                The connection to the rendezvous backend has failed.
            RendezvousStateError:
                The rendezvous state is corrupt.
            RendezvousTimeoutError:
                The rendezvous did not complete on time.
        """
    @abstractmethod
    def is_closed(self) -> bool:
        """Checks whether the rendezvous has been closed.

        A closed rendezvous means all future attempts to re-rendezvous within
        same job will fail.

        ``is_closed()`` and :py:meth:`set_closed` have semantics of eventual
        propagation and should not be used for synchronization. The intention is
        that if at least one node decides the job is finished, it will close the
        rendezvous, and other nodes will soon observe this and stop running as
        well.
        """
    @abstractmethod
    def set_closed(self):
        """Marks the rendezvous as closed."""
    @abstractmethod
    def num_nodes_waiting(self) -> int:
        """Returns the number of nodes who arrived late at the rendezvous
        barrier, hence were not included in the current worker group.

        Callers should periodically call this method to check whether new
        nodes are waiting to join the job and if so admit them by calling
        :py:meth:`next_rendezvous()` (re-rendezvous).
        """
    @abstractmethod
    def get_run_id(self) -> str:
        """Returns the run id of the rendezvous.

        The run id is a user-defined id that uniquely identifies an instance of
        a distributed application. It typically maps to a job id and is used to
        allow nodes to join the correct distributed application.
        """
    def shutdown(self) -> bool:
        """Closes all resources that were open for the rendezvous.

        Example::

            rdzv_handler = ...
            try:
                store, rank, world_size = rdzv_handler.next_rendezvous()
            finally:
                rdzv_handler.shutdown()
        """

class RendezvousParameters:
    """Holds the parameters to construct a :py:class:`RendezvousHandler`.

    Args:
        backend:
            The name of the backend to use to handle the rendezvous.
        endpoint:
            The endpoint of the rendezvous, usually in form <hostname>[:<port>].
        run_id:
            The id of the rendezvous.
        min_nodes:
            The minimum number of nodes to admit to the rendezvous.
        max_nodes:
            The maximum number of nodes to admit to the rendezvous.
        local_addr:
            The address of the local node.
        **kwargs:
            Additional parameters for the specified backend.
    """
    backend: Incomplete
    endpoint: Incomplete
    run_id: Incomplete
    min_nodes: Incomplete
    max_nodes: Incomplete
    config: Incomplete
    local_addr: Incomplete
    def __init__(self, backend: str, endpoint: str, run_id: str, min_nodes: int, max_nodes: int, local_addr: str | None = None, **kwargs) -> None: ...
    def get(self, key: str, default: Any = None) -> Any:
        """Returns the value for ``key`` if ``key`` exists, else ``default``."""
    def get_as_bool(self, key: str, default: bool | None = None) -> bool | None:
        """Returns the value for ``key`` as a ``bool``."""
    def get_as_int(self, key: str, default: int | None = None) -> int | None:
        """Returns the value for ``key`` as an ``int``."""
RendezvousHandlerCreator = Callable[[RendezvousParameters], RendezvousHandler]

class RendezvousHandlerRegistry:
    """Represents a registry of :py:class:`RendezvousHandler` backends."""
    def __init__(self) -> None: ...
    def register(self, backend: str, creator: RendezvousHandlerCreator) -> None:
        """Registers a new rendezvous backend.

        Args:
            backend:
                The name of the backend.
            creator:
                The callback to invoke to construct the
                :py:class:`RendezvousHandler`.
        """
    def create_handler(self, params: RendezvousParameters) -> RendezvousHandler:
        """Creates a new :py:class:`RendezvousHandler`."""

rendezvous_handler_registry: Incomplete
