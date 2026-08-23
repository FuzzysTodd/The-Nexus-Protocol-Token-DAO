from _typeshed import Incomplete
from typing import Any, Awaitable, Deque, Generic

__all__ = ['Empty', 'Full', 'Queue']

class Empty(Exception):
    """Exception raised by Queue.get(block=0)/get_nowait()."""
class Full(Exception):
    """Exception raised by Queue.put(block=0)/put_nowait()."""

class QueueCommon(Generic[_T]):
    maxsize: int
    use_lifo: bool
    def __init__(self, maxsize: int = 0, use_lifo: bool = False) -> None: ...
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
    def qsize(self) -> int: ...
    def put_nowait(self, item: _T) -> None: ...
    def put(self, item: _T, block: bool = True, timeout: float | None = None) -> None: ...
    def get_nowait(self) -> _T: ...
    def get(self, block: bool = True, timeout: float | None = None) -> _T: ...

class Queue(QueueCommon[_T]):
    queue: Deque[_T]
    mutex: Incomplete
    not_empty: Incomplete
    not_full: Incomplete
    use_lifo: Incomplete
    def __init__(self, maxsize: int = 0, use_lifo: bool = False) -> None:
        """Initialize a queue object with a given maximum size.

        If `maxsize` is <= 0, the queue size is infinite.

        If `use_lifo` is True, this Queue acts like a Stack (LIFO).
        """
    def qsize(self) -> int:
        """Return the approximate size of the queue (not reliable!)."""
    def empty(self) -> bool:
        """Return True if the queue is empty, False otherwise (not
        reliable!)."""
    def full(self) -> bool:
        """Return True if the queue is full, False otherwise (not
        reliable!)."""
    def put(self, item: _T, block: bool = True, timeout: float | None = None) -> None:
        """Put an item into the queue.

        If optional args `block` is True and `timeout` is None (the
        default), block if necessary until a free slot is
        available. If `timeout` is a positive number, it blocks at
        most `timeout` seconds and raises the ``Full`` exception if no
        free slot was available within that time.  Otherwise (`block`
        is false), put an item on the queue if a free slot is
        immediately available, else raise the ``Full`` exception
        (`timeout` is ignored in that case).
        """
    def put_nowait(self, item: _T) -> None:
        """Put an item into the queue without blocking.

        Only enqueue the item if a free slot is immediately available.
        Otherwise raise the ``Full`` exception.
        """
    def get(self, block: bool = True, timeout: float | None = None) -> _T:
        """Remove and return an item from the queue.

        If optional args `block` is True and `timeout` is None (the
        default), block if necessary until an item is available. If
        `timeout` is a positive number, it blocks at most `timeout`
        seconds and raises the ``Empty`` exception if no item was
        available within that time.  Otherwise (`block` is false),
        return an item if one is immediately available, else raise the
        ``Empty`` exception (`timeout` is ignored in that case).

        """
    def get_nowait(self) -> _T:
        """Remove and return an item from the queue without blocking.

        Only get an item if one is immediately available. Otherwise
        raise the ``Empty`` exception.
        """

class AsyncAdaptedQueue(QueueCommon[_T]):
    @staticmethod
    def await_(coroutine: Awaitable[Any]) -> _T: ...
    use_lifo: Incomplete
    maxsize: Incomplete
    def __init__(self, maxsize: int = 0, use_lifo: bool = False) -> None: ...
    def empty(self) -> bool: ...
    def full(self): ...
    def qsize(self): ...
    def put_nowait(self, item: _T) -> None: ...
    def put(self, item: _T, block: bool = True, timeout: float | None = None) -> None: ...
    def get_nowait(self) -> _T: ...
    def get(self, block: bool = True, timeout: float | None = None) -> _T: ...

class FallbackAsyncAdaptedQueue(AsyncAdaptedQueue[_T]): ...
