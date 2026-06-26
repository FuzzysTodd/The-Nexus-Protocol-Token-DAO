import queue as __queue__
from _typeshed import Incomplete

__all__ = ['SimpleQueue']

Full = __queue__.Full
Empty = __queue__.Empty
SimpleQueue: Incomplete

class ItemWaiter(Waiter):
    item: Incomplete
    queue: Incomplete
    def __init__(self, item, queue) -> None: ...
    def put_and_switch(self): ...

class Queue:
    """
    Create a queue object with a given maximum size.

    If *maxsize* is less than or equal to zero or ``None``, the queue
    size is infinite.

    Queues have a ``len`` equal to the number of items in them (the :meth:`qsize`),
    but in a boolean context they are always True.

    .. versionchanged:: 1.1b3
       Queues now support :func:`len`; it behaves the same as :meth:`qsize`.
    .. versionchanged:: 1.1b3
       Multiple greenlets that block on a call to :meth:`put` for a full queue
       will now be awakened to put their items into the queue in the order in which
       they arrived. Likewise, multiple greenlets that block on a call to :meth:`get` for
       an empty queue will now receive items in the order in which they blocked. An
       implementation quirk under CPython *usually* ensured this was roughly the case
       previously anyway, but that wasn't the case for PyPy.
    """
    getters: Incomplete
    putters: Incomplete
    hub: Incomplete
    queue: Incomplete
    def __init__(self, maxsize: Incomplete | None = None, items=(), _warn_depth: int = 2) -> None: ...
    @property
    def maxsize(self): ...
    @maxsize.setter
    def maxsize(self, nv) -> None: ...
    def copy(self): ...
    def qsize(self):
        """Return the size of the queue."""
    def __len__(self) -> int:
        """
        Return the size of the queue. This is the same as :meth:`qsize`.

        .. versionadded: 1.1b3

            Previously, getting len() of a queue would raise a TypeError.
        """
    def __bool__(self) -> bool:
        """
        A queue object is always True.

        .. versionadded: 1.1b3

           Now that queues support len(), they need to implement ``__bool__``
           to return True for backwards compatibility.
        """
    def __nonzero__(self): ...
    def empty(self):
        """Return ``True`` if the queue is empty, ``False`` otherwise."""
    def full(self):
        """Return ``True`` if the queue is full, ``False`` otherwise.

        ``Queue(None)`` is never full.
        """
    def put(self, item, block: bool = True, timeout: Incomplete | None = None) -> None:
        """Put an item into the queue.

        If optional arg *block* is true and *timeout* is ``None`` (the default),
        block if necessary until a free slot is available. If *timeout* is
        a positive number, it blocks at most *timeout* seconds and raises
        the :class:`Full` exception if no free slot was available within that time.
        Otherwise (*block* is false), put an item on the queue if a free slot
        is immediately available, else raise the :class:`Full` exception (*timeout*
        is ignored in that case).
        """
    def put_nowait(self, item) -> None:
        """Put an item into the queue without blocking.

        Only enqueue the item if a free slot is immediately available.
        Otherwise raise the :class:`Full` exception.
        """
    def get(self, block: bool = True, timeout: Incomplete | None = None):
        """Remove and return an item from the queue.

        If optional args *block* is true and *timeout* is ``None`` (the default),
        block if necessary until an item is available. If *timeout* is a positive number,
        it blocks at most *timeout* seconds and raises the :class:`Empty` exception
        if no item was available within that time. Otherwise (*block* is false), return
        an item if one is immediately available, else raise the :class:`Empty` exception
        (*timeout* is ignored in that case).
        """
    def get_nowait(self):
        """Remove and return an item from the queue without blocking.

        Only get an item if one is immediately available. Otherwise
        raise the :class:`Empty` exception.
        """
    def peek(self, block: bool = True, timeout: Incomplete | None = None):
        """Return an item from the queue without removing it.

        If optional args *block* is true and *timeout* is ``None`` (the default),
        block if necessary until an item is available. If *timeout* is a positive number,
        it blocks at most *timeout* seconds and raises the :class:`Empty` exception
        if no item was available within that time. Otherwise (*block* is false), return
        an item if one is immediately available, else raise the :class:`Empty` exception
        (*timeout* is ignored in that case).
        """
    def peek_nowait(self):
        """Return an item from the queue without blocking.

        Only return an item if one is immediately available. Otherwise
        raise the :class:`Empty` exception.
        """
    def __iter__(self): ...
    def __next__(self): ...
    next = __next__

class UnboundQueue(Queue):
    putters: Incomplete
    def __init__(self, maxsize: Incomplete | None = None, items=()) -> None: ...
    def put(self, item, block: bool = True, timeout: Incomplete | None = None) -> None: ...

class PriorityQueue(Queue):
    """A subclass of :class:`Queue` that retrieves entries in priority order (lowest first).

    Entries are typically tuples of the form: ``(priority number, data)``.

    .. versionchanged:: 1.2a1
       Any *items* given to the constructor will now be passed through
       :func:`heapq.heapify` to ensure the invariants of this class hold.
       Previously it was just assumed that they were already a heap.
    """
class LifoQueue(Queue):
    """A subclass of :class:`Queue` that retrieves most recently added entries first."""

class JoinableQueue(Queue):
    """
    A subclass of :class:`Queue` that additionally has
    :meth:`task_done` and :meth:`join` methods.
    """
    unfinished_tasks: Incomplete
    def __init__(self, maxsize: Incomplete | None = None, items=(), unfinished_tasks: Incomplete | None = None) -> None:
        """

        .. versionchanged:: 1.1a1
           If *unfinished_tasks* is not given, then all the given *items*
           (if any) will be considered unfinished.

        """
    def copy(self): ...
    def task_done(self) -> None:
        """Indicate that a formerly enqueued task is complete. Used by queue consumer threads.
        For each :meth:`get <Queue.get>` used to fetch a task, a subsequent call to :meth:`task_done` tells the queue
        that the processing on the task is complete.

        If a :meth:`join` is currently blocking, it will resume when all items have been processed
        (meaning that a :meth:`task_done` call was received for every item that had been
        :meth:`put <Queue.put>` into the queue).

        Raises a :exc:`ValueError` if called more times than there were items placed in the queue.
        """
    def join(self, timeout: Incomplete | None = None):
        """
        Block until all items in the queue have been gotten and processed.

        The count of unfinished tasks goes up whenever an item is added to the queue.
        The count goes down whenever a consumer thread calls :meth:`task_done` to indicate
        that the item was retrieved and all work on it is complete. When the count of
        unfinished tasks drops to zero, :meth:`join` unblocks.

        :param float timeout: If not ``None``, then wait no more than this time in seconds
            for all tasks to finish.
        :return: ``True`` if all tasks have finished; if ``timeout`` was given and expired before
            all tasks finished, ``False``.

        .. versionchanged:: 1.1a1
           Add the *timeout* parameter.
        """

class Channel:
    getters: Incomplete
    putters: Incomplete
    hub: Incomplete
    def __init__(self, maxsize: int = 1) -> None: ...
    @property
    def balance(self): ...
    def qsize(self): ...
    def empty(self): ...
    def full(self): ...
    def put(self, item, block: bool = True, timeout: Incomplete | None = None) -> None: ...
    def put_nowait(self, item) -> None: ...
    def get(self, block: bool = True, timeout: Incomplete | None = None): ...
    def get_nowait(self): ...
    def __iter__(self): ...
    def __next__(self): ...
    next = __next__
