import datetime
from _typeshed import Incomplete
from tornado.concurrent import Future
from typing import Awaitable, Generic

__all__ = ['Queue', 'PriorityQueue', 'LifoQueue', 'QueueFull', 'QueueEmpty']

class QueueEmpty(Exception):
    """Raised by `.Queue.get_nowait` when the queue has no items."""
class QueueFull(Exception):
    """Raised by `.Queue.put_nowait` when a queue is at its maximum size."""

class _QueueIterator(Generic[_T]):
    q: Incomplete
    def __init__(self, q: Queue[_T]) -> None: ...
    def __anext__(self) -> Awaitable[_T]: ...

class Queue(Generic[_T]):
    """Coordinate producer and consumer coroutines.

    If maxsize is 0 (the default) the queue size is unbounded.

    .. testcode::

        import asyncio
        from tornado.ioloop import IOLoop
        from tornado.queues import Queue

        q = Queue(maxsize=2)

        async def consumer():
            async for item in q:
                try:
                    print('Doing work on %s' % item)
                    await asyncio.sleep(0.01)
                finally:
                    q.task_done()

        async def producer():
            for item in range(5):
                await q.put(item)
                print('Put %s' % item)

        async def main():
            # Start consumer without waiting (since it never finishes).
            IOLoop.current().spawn_callback(consumer)
            await producer()     # Wait for producer to put all tasks.
            await q.join()       # Wait for consumer to finish all tasks.
            print('Done')

        asyncio.run(main())

    .. testoutput::

        Put 0
        Put 1
        Doing work on 0
        Put 2
        Doing work on 1
        Put 3
        Doing work on 2
        Put 4
        Doing work on 3
        Doing work on 4
        Done


    In versions of Python without native coroutines (before 3.5),
    ``consumer()`` could be written as::

        @gen.coroutine
        def consumer():
            while True:
                item = yield q.get()
                try:
                    print('Doing work on %s' % item)
                    yield gen.sleep(0.01)
                finally:
                    q.task_done()

    .. versionchanged:: 4.3
       Added ``async for`` support in Python 3.5.

    """
    def __init__(self, maxsize: int = 0) -> None: ...
    @property
    def maxsize(self) -> int:
        """Number of items allowed in the queue."""
    def qsize(self) -> int:
        """Number of items in the queue."""
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
    def put(self, item: _T, timeout: float | datetime.timedelta | None = None) -> Future[None]:
        """Put an item into the queue, perhaps waiting until there is room.

        Returns a Future, which raises `tornado.util.TimeoutError` after a
        timeout.

        ``timeout`` may be a number denoting a time (on the same
        scale as `tornado.ioloop.IOLoop.time`, normally `time.time`), or a
        `datetime.timedelta` object for a deadline relative to the
        current time.
        """
    def put_nowait(self, item: _T) -> None:
        """Put an item into the queue without blocking.

        If no free slot is immediately available, raise `QueueFull`.
        """
    def get(self, timeout: float | datetime.timedelta | None = None) -> Awaitable[_T]:
        """Remove and return an item from the queue.

        Returns an awaitable which resolves once an item is available, or raises
        `tornado.util.TimeoutError` after a timeout.

        ``timeout`` may be a number denoting a time (on the same
        scale as `tornado.ioloop.IOLoop.time`, normally `time.time`), or a
        `datetime.timedelta` object for a deadline relative to the
        current time.

        .. note::

           The ``timeout`` argument of this method differs from that
           of the standard library's `queue.Queue.get`. That method
           interprets numeric values as relative timeouts; this one
           interprets them as absolute deadlines and requires
           ``timedelta`` objects for relative timeouts (consistent
           with other timeouts in Tornado).

        """
    def get_nowait(self) -> _T:
        """Remove and return an item from the queue without blocking.

        Return an item if one is immediately available, else raise
        `QueueEmpty`.
        """
    def task_done(self) -> None:
        """Indicate that a formerly enqueued task is complete.

        Used by queue consumers. For each `.get` used to fetch a task, a
        subsequent call to `.task_done` tells the queue that the processing
        on the task is complete.

        If a `.join` is blocking, it resumes when all items have been
        processed; that is, when every `.put` is matched by a `.task_done`.

        Raises `ValueError` if called more times than `.put`.
        """
    def join(self, timeout: float | datetime.timedelta | None = None) -> Awaitable[None]:
        """Block until all items in the queue are processed.

        Returns an awaitable, which raises `tornado.util.TimeoutError` after a
        timeout.
        """
    def __aiter__(self) -> _QueueIterator[_T]: ...

class PriorityQueue(Queue):
    """A `.Queue` that retrieves entries in priority order, lowest first.

    Entries are typically tuples like ``(priority number, data)``.

    .. testcode::

        import asyncio
        from tornado.queues import PriorityQueue

        async def main():
            q = PriorityQueue()
            q.put((1, 'medium-priority item'))
            q.put((0, 'high-priority item'))
            q.put((10, 'low-priority item'))

            print(await q.get())
            print(await q.get())
            print(await q.get())

        asyncio.run(main())

    .. testoutput::

        (0, 'high-priority item')
        (1, 'medium-priority item')
        (10, 'low-priority item')
    """
class LifoQueue(Queue):
    """A `.Queue` that retrieves the most recently put items first.

    .. testcode::

        import asyncio
        from tornado.queues import LifoQueue

        async def main():
            q = LifoQueue()
            q.put(3)
            q.put(2)
            q.put(1)

            print(await q.get())
            print(await q.get())
            print(await q.get())

        asyncio.run(main())

    .. testoutput::

        1
        2
        3
    """
