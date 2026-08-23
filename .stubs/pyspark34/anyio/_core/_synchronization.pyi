from ..lowlevel import cancel_shielded_checkpoint as cancel_shielded_checkpoint, checkpoint as checkpoint, checkpoint_if_cancelled as checkpoint_if_cancelled
from ._compat import DeprecatedAwaitable as DeprecatedAwaitable
from ._eventloop import get_asynclib as get_asynclib
from ._exceptions import BusyResourceError as BusyResourceError, WouldBlock as WouldBlock
from ._tasks import CancelScope as CancelScope
from ._testing import TaskInfo as TaskInfo, get_current_task as get_current_task
from _typeshed import Incomplete
from dataclasses import dataclass
from types import TracebackType

@dataclass(frozen=True)
class EventStatistics:
    """
    :ivar int tasks_waiting: number of tasks waiting on :meth:`~.Event.wait`
    """
    tasks_waiting: int
    def __init__(self, tasks_waiting) -> None: ...

@dataclass(frozen=True)
class CapacityLimiterStatistics:
    """
    :ivar int borrowed_tokens: number of tokens currently borrowed by tasks
    :ivar float total_tokens: total number of available tokens
    :ivar tuple borrowers: tasks or other objects currently holding tokens borrowed from this
        limiter
    :ivar int tasks_waiting: number of tasks waiting on :meth:`~.CapacityLimiter.acquire` or
        :meth:`~.CapacityLimiter.acquire_on_behalf_of`
    """
    borrowed_tokens: int
    total_tokens: float
    borrowers: tuple[object, ...]
    tasks_waiting: int
    def __init__(self, borrowed_tokens, total_tokens, borrowers, tasks_waiting) -> None: ...

@dataclass(frozen=True)
class LockStatistics:
    """
    :ivar bool locked: flag indicating if this lock is locked or not
    :ivar ~anyio.TaskInfo owner: task currently holding the lock (or ``None`` if the lock is not
        held by any task)
    :ivar int tasks_waiting: number of tasks waiting on :meth:`~.Lock.acquire`
    """
    locked: bool
    owner: TaskInfo | None
    tasks_waiting: int
    def __init__(self, locked, owner, tasks_waiting) -> None: ...

@dataclass(frozen=True)
class ConditionStatistics:
    """
    :ivar int tasks_waiting: number of tasks blocked on :meth:`~.Condition.wait`
    :ivar ~anyio.LockStatistics lock_statistics: statistics of the underlying :class:`~.Lock`
    """
    tasks_waiting: int
    lock_statistics: LockStatistics
    def __init__(self, tasks_waiting, lock_statistics) -> None: ...

@dataclass(frozen=True)
class SemaphoreStatistics:
    """
    :ivar int tasks_waiting: number of tasks waiting on :meth:`~.Semaphore.acquire`

    """
    tasks_waiting: int
    def __init__(self, tasks_waiting) -> None: ...

class Event:
    def __new__(cls) -> Event: ...
    def set(self) -> DeprecatedAwaitable:
        """Set the flag, notifying all listeners."""
    def is_set(self) -> bool:
        """Return ``True`` if the flag is set, ``False`` if not."""
    async def wait(self) -> None:
        """
        Wait until the flag has been set.

        If the flag has already been set when this method is called, it returns immediately.

        """
    def statistics(self) -> EventStatistics:
        """Return statistics about the current state of this event."""

class Lock:
    def __init__(self) -> None: ...
    async def __aenter__(self) -> None: ...
    async def __aexit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...
    async def acquire(self) -> None:
        """Acquire the lock."""
    def acquire_nowait(self) -> None:
        """
        Acquire the lock, without blocking.

        :raises ~anyio.WouldBlock: if the operation would block

        """
    def release(self) -> DeprecatedAwaitable:
        """Release the lock."""
    def locked(self) -> bool:
        """Return True if the lock is currently held."""
    def statistics(self) -> LockStatistics:
        """
        Return statistics about the current state of this lock.

        .. versionadded:: 3.0
        """

class Condition:
    def __init__(self, lock: Lock | None = None) -> None: ...
    async def __aenter__(self) -> None: ...
    async def __aexit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...
    async def acquire(self) -> None:
        """Acquire the underlying lock."""
    def acquire_nowait(self) -> None:
        """
        Acquire the underlying lock, without blocking.

        :raises ~anyio.WouldBlock: if the operation would block

        """
    def release(self) -> DeprecatedAwaitable:
        """Release the underlying lock."""
    def locked(self) -> bool:
        """Return True if the lock is set."""
    def notify(self, n: int = 1) -> None:
        """Notify exactly n listeners."""
    def notify_all(self) -> None:
        """Notify all the listeners."""
    async def wait(self) -> None:
        """Wait for a notification."""
    def statistics(self) -> ConditionStatistics:
        """
        Return statistics about the current state of this condition.

        .. versionadded:: 3.0
        """

class Semaphore:
    def __init__(self, initial_value: int, *, max_value: int | None = None) -> None: ...
    async def __aenter__(self) -> Semaphore: ...
    async def __aexit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...
    async def acquire(self) -> None:
        """Decrement the semaphore value, blocking if necessary."""
    def acquire_nowait(self) -> None:
        """
        Acquire the underlying lock, without blocking.

        :raises ~anyio.WouldBlock: if the operation would block

        """
    def release(self) -> DeprecatedAwaitable:
        """Increment the semaphore value."""
    @property
    def value(self) -> int:
        """The current value of the semaphore."""
    @property
    def max_value(self) -> int | None:
        """The maximum value of the semaphore."""
    def statistics(self) -> SemaphoreStatistics:
        """
        Return statistics about the current state of this semaphore.

        .. versionadded:: 3.0
        """

class CapacityLimiter:
    def __new__(cls, total_tokens: float) -> CapacityLimiter: ...
    async def __aenter__(self) -> None: ...
    async def __aexit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> bool | None: ...
    @property
    def total_tokens(self) -> float:
        """
        The total number of tokens available for borrowing.

        This is a read-write property. If the total number of tokens is increased, the
        proportionate number of tasks waiting on this limiter will be granted their tokens.

        .. versionchanged:: 3.0
            The property is now writable.

        """
    @total_tokens.setter
    def total_tokens(self, value: float) -> None: ...
    async def set_total_tokens(self, value: float) -> None: ...
    @property
    def borrowed_tokens(self) -> int:
        """The number of tokens that have currently been borrowed."""
    @property
    def available_tokens(self) -> float:
        """The number of tokens currently available to be borrowed"""
    def acquire_nowait(self) -> DeprecatedAwaitable:
        """
        Acquire a token for the current task without waiting for one to become available.

        :raises ~anyio.WouldBlock: if there are no tokens available for borrowing

        """
    def acquire_on_behalf_of_nowait(self, borrower: object) -> DeprecatedAwaitable:
        """
        Acquire a token without waiting for one to become available.

        :param borrower: the entity borrowing a token
        :raises ~anyio.WouldBlock: if there are no tokens available for borrowing

        """
    async def acquire(self) -> None:
        """
        Acquire a token for the current task, waiting if necessary for one to become available.

        """
    async def acquire_on_behalf_of(self, borrower: object) -> None:
        """
        Acquire a token, waiting if necessary for one to become available.

        :param borrower: the entity borrowing a token

        """
    def release(self) -> None:
        """
        Release the token held by the current task.
        :raises RuntimeError: if the current task has not borrowed a token from this limiter.

        """
    def release_on_behalf_of(self, borrower: object) -> None:
        """
        Release the token held by the given borrower.

        :raises RuntimeError: if the borrower has not borrowed a token from this limiter.

        """
    def statistics(self) -> CapacityLimiterStatistics:
        """
        Return statistics about the current state of this limiter.

        .. versionadded:: 3.0

        """

def create_lock() -> Lock:
    """
    Create an asynchronous lock.

    :return: a lock object

    .. deprecated:: 3.0
       Use :class:`~Lock` directly.

    """
def create_condition(lock: Lock | None = None) -> Condition:
    """
    Create an asynchronous condition.

    :param lock: the lock to base the condition object on
    :return: a condition object

    .. deprecated:: 3.0
       Use :class:`~Condition` directly.

    """
def create_event() -> Event:
    """
    Create an asynchronous event object.

    :return: an event object

    .. deprecated:: 3.0
       Use :class:`~Event` directly.

    """
def create_semaphore(value: int, *, max_value: int | None = None) -> Semaphore:
    '''
    Create an asynchronous semaphore.

    :param value: the semaphore\'s initial value
    :param max_value: if set, makes this a "bounded" semaphore that raises :exc:`ValueError` if the
        semaphore\'s value would exceed this number
    :return: a semaphore object

    .. deprecated:: 3.0
       Use :class:`~Semaphore` directly.

    '''
def create_capacity_limiter(total_tokens: float) -> CapacityLimiter:
    """
    Create a capacity limiter.

    :param total_tokens: the total number of tokens available for borrowing (can be an integer or
        :data:`math.inf`)
    :return: a capacity limiter object

    .. deprecated:: 3.0
       Use :class:`~CapacityLimiter` directly.

    """

class ResourceGuard:
    action: Incomplete
    def __init__(self, action: str) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> bool | None: ...
