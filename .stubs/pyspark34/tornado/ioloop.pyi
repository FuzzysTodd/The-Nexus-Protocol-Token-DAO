import concurrent.futures
import datetime
import typing
from _typeshed import Incomplete
from tornado.concurrent import Future as Future, chain_future as chain_future, future_add_done_callback as future_add_done_callback, future_set_exc_info as future_set_exc_info, is_future as is_future
from tornado.log import app_log as app_log
from tornado.util import Configurable as Configurable, TimeoutError as TimeoutError, import_object as import_object
from typing import Any, Awaitable, Callable, Tuple, Type
from typing_extensions import Protocol

class _Selectable(Protocol):
    def fileno(self) -> int: ...
    def close(self) -> None: ...

class IOLoop(Configurable):
    '''An I/O event loop.

    As of Tornado 6.0, `IOLoop` is a wrapper around the `asyncio` event loop.

    Example usage for a simple TCP server:

    .. testcode::

        import asyncio
        import errno
        import functools
        import socket

        import tornado
        from tornado.iostream import IOStream

        async def handle_connection(connection, address):
            stream = IOStream(connection)
            message = await stream.read_until_close()
            print("message from client:", message.decode().strip())

        def connection_ready(sock, fd, events):
            while True:
                try:
                    connection, address = sock.accept()
                except BlockingIOError:
                    return
                connection.setblocking(0)
                io_loop = tornado.ioloop.IOLoop.current()
                io_loop.spawn_callback(handle_connection, connection, address)

        async def main():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.setblocking(0)
            sock.bind(("", 8888))
            sock.listen(128)

            io_loop = tornado.ioloop.IOLoop.current()
            callback = functools.partial(connection_ready, sock)
            io_loop.add_handler(sock.fileno(), callback, io_loop.READ)
            await asyncio.Event().wait()

        if __name__ == "__main__":
            asyncio.run(main())

    .. testoutput::
       :hide:

    Most applications should not attempt to construct an `IOLoop` directly,
    and instead initialize the `asyncio` event loop and use `IOLoop.current()`.
    In some cases, such as in test frameworks when initializing an `IOLoop`
    to be run in a secondary thread, it may be appropriate to construct
    an `IOLoop` with ``IOLoop(make_current=False)``.

    In general, an `IOLoop` cannot survive a fork or be shared across processes
    in any way. When multiple processes are being used, each process should
    create its own `IOLoop`, which also implies that any objects which depend on
    the `IOLoop` (such as `.AsyncHTTPClient`) must also be created in the child
    processes. As a guideline, anything that starts processes (including the
    `tornado.process` and `multiprocessing` modules) should do so as early as
    possible, ideally the first thing the application does after loading its
    configuration, and *before* any calls to `.IOLoop.start` or `asyncio.run`.

    .. versionchanged:: 4.2
       Added the ``make_current`` keyword argument to the `IOLoop`
       constructor.

    .. versionchanged:: 5.0

       Uses the `asyncio` event loop by default. The ``IOLoop.configure`` method
       cannot be used on Python 3 except to redundantly specify the `asyncio`
       event loop.

    .. versionchanged:: 6.3
       ``make_current=True`` is now the default when creating an IOLoop -
       previously the default was to make the event loop current if there wasn\'t
       already a current one.
    '''
    NONE: int
    READ: int
    WRITE: int
    ERROR: int
    @classmethod
    def configure(cls, impl: None | str | Type[Configurable], **kwargs: Any) -> None: ...
    @staticmethod
    def instance() -> IOLoop:
        """Deprecated alias for `IOLoop.current()`.

        .. versionchanged:: 5.0

           Previously, this method returned a global singleton
           `IOLoop`, in contrast with the per-thread `IOLoop` returned
           by `current()`. In nearly all cases the two were the same
           (when they differed, it was generally used from non-Tornado
           threads to communicate back to the main thread's `IOLoop`).
           This distinction is not present in `asyncio`, so in order
           to facilitate integration with that package `instance()`
           was changed to be an alias to `current()`. Applications
           using the cross-thread communications aspect of
           `instance()` should instead set their own global variable
           to point to the `IOLoop` they want to use.

        .. deprecated:: 5.0
        """
    def install(self) -> None:
        """Deprecated alias for `make_current()`.

        .. versionchanged:: 5.0

           Previously, this method would set this `IOLoop` as the
           global singleton used by `IOLoop.instance()`. Now that
           `instance()` is an alias for `current()`, `install()`
           is an alias for `make_current()`.

        .. deprecated:: 5.0
        """
    @staticmethod
    def clear_instance() -> None:
        """Deprecated alias for `clear_current()`.

        .. versionchanged:: 5.0

           Previously, this method would clear the `IOLoop` used as
           the global singleton by `IOLoop.instance()`. Now that
           `instance()` is an alias for `current()`,
           `clear_instance()` is an alias for `clear_current()`.

        .. deprecated:: 5.0

        """
    @typing.overload
    @staticmethod
    def current() -> IOLoop: ...
    @typing.overload
    @staticmethod
    def current(instance: bool = True) -> IOLoop | None: ...
    def make_current(self) -> None:
        """Makes this the `IOLoop` for the current thread.

        An `IOLoop` automatically becomes current for its thread
        when it is started, but it is sometimes useful to call
        `make_current` explicitly before starting the `IOLoop`,
        so that code run at startup time can find the right
        instance.

        .. versionchanged:: 4.1
           An `IOLoop` created while there is no current `IOLoop`
           will automatically become current.

        .. versionchanged:: 5.0
           This method also sets the current `asyncio` event loop.

        .. deprecated:: 6.2
           Setting and clearing the current event loop through Tornado is
           deprecated. Use ``asyncio.set_event_loop`` instead if you need this.
        """
    @staticmethod
    def clear_current() -> None:
        """Clears the `IOLoop` for the current thread.

        Intended primarily for use by test frameworks in between tests.

        .. versionchanged:: 5.0
           This method also clears the current `asyncio` event loop.
        .. deprecated:: 6.2
        """
    @classmethod
    def configurable_base(cls) -> Type[Configurable]: ...
    @classmethod
    def configurable_default(cls) -> Type[Configurable]: ...
    def initialize(self, make_current: bool = True) -> None: ...
    def close(self, all_fds: bool = False) -> None:
        '''Closes the `IOLoop`, freeing any resources used.

        If ``all_fds`` is true, all file descriptors registered on the
        IOLoop will be closed (not just the ones created by the
        `IOLoop` itself).

        Many applications will only use a single `IOLoop` that runs for the
        entire lifetime of the process.  In that case closing the `IOLoop`
        is not necessary since everything will be cleaned up when the
        process exits.  `IOLoop.close` is provided mainly for scenarios
        such as unit tests, which create and destroy a large number of
        ``IOLoops``.

        An `IOLoop` must be completely stopped before it can be closed.  This
        means that `IOLoop.stop()` must be called *and* `IOLoop.start()` must
        be allowed to return before attempting to call `IOLoop.close()`.
        Therefore the call to `close` will usually appear just after
        the call to `start` rather than near the call to `stop`.

        .. versionchanged:: 3.1
           If the `IOLoop` implementation supports non-integer objects
           for "file descriptors", those objects will have their
           ``close`` method when ``all_fds`` is true.
        '''
    @typing.overload
    def add_handler(self, fd: int, handler: Callable[[int, int], None], events: int) -> None: ...
    @typing.overload
    def add_handler(self, fd: _S, handler: Callable[[_S, int], None], events: int) -> None: ...
    def update_handler(self, fd: int | _Selectable, events: int) -> None:
        """Changes the events we listen for ``fd``.

        .. versionchanged:: 4.0
           Added the ability to pass file-like objects in addition to
           raw file descriptors.
        """
    def remove_handler(self, fd: int | _Selectable) -> None:
        """Stop listening for events on ``fd``.

        .. versionchanged:: 4.0
           Added the ability to pass file-like objects in addition to
           raw file descriptors.
        """
    def start(self) -> None:
        """Starts the I/O loop.

        The loop will run until one of the callbacks calls `stop()`, which
        will make the loop stop after the current event iteration completes.
        """
    def stop(self) -> None:
        """Stop the I/O loop.

        If the event loop is not currently running, the next call to `start()`
        will return immediately.

        Note that even after `stop` has been called, the `IOLoop` is not
        completely stopped until `IOLoop.start` has also returned.
        Some work that was scheduled before the call to `stop` may still
        be run before the `IOLoop` shuts down.
        """
    def run_sync(self, func: Callable, timeout: float | None = None) -> Any:
        """Starts the `IOLoop`, runs the given function, and stops the loop.

        The function must return either an awaitable object or
        ``None``. If the function returns an awaitable object, the
        `IOLoop` will run until the awaitable is resolved (and
        `run_sync()` will return the awaitable's result). If it raises
        an exception, the `IOLoop` will stop and the exception will be
        re-raised to the caller.

        The keyword-only argument ``timeout`` may be used to set
        a maximum duration for the function.  If the timeout expires,
        a `asyncio.TimeoutError` is raised.

        This method is useful to allow asynchronous calls in a
        ``main()`` function::

            async def main():
                # do stuff...

            if __name__ == '__main__':
                IOLoop.current().run_sync(main)

        .. versionchanged:: 4.3
           Returning a non-``None``, non-awaitable value is now an error.

        .. versionchanged:: 5.0
           If a timeout occurs, the ``func`` coroutine will be cancelled.

        .. versionchanged:: 6.2
           ``tornado.util.TimeoutError`` is now an alias to ``asyncio.TimeoutError``.
        """
    def time(self) -> float:
        """Returns the current time according to the `IOLoop`'s clock.

        The return value is a floating-point number relative to an
        unspecified time in the past.

        Historically, the IOLoop could be customized to use e.g.
        `time.monotonic` instead of `time.time`, but this is not
        currently supported and so this method is equivalent to
        `time.time`.

        """
    def add_timeout(self, deadline: float | datetime.timedelta, callback: Callable, *args: Any, **kwargs: Any) -> object:
        """Runs the ``callback`` at the time ``deadline`` from the I/O loop.

        Returns an opaque handle that may be passed to
        `remove_timeout` to cancel.

        ``deadline`` may be a number denoting a time (on the same
        scale as `IOLoop.time`, normally `time.time`), or a
        `datetime.timedelta` object for a deadline relative to the
        current time.  Since Tornado 4.0, `call_later` is a more
        convenient alternative for the relative case since it does not
        require a timedelta object.

        Note that it is not safe to call `add_timeout` from other threads.
        Instead, you must use `add_callback` to transfer control to the
        `IOLoop`'s thread, and then call `add_timeout` from there.

        Subclasses of IOLoop must implement either `add_timeout` or
        `call_at`; the default implementations of each will call
        the other.  `call_at` is usually easier to implement, but
        subclasses that wish to maintain compatibility with Tornado
        versions prior to 4.0 must use `add_timeout` instead.

        .. versionchanged:: 4.0
           Now passes through ``*args`` and ``**kwargs`` to the callback.
        """
    def call_later(self, delay: float, callback: Callable, *args: Any, **kwargs: Any) -> object:
        """Runs the ``callback`` after ``delay`` seconds have passed.

        Returns an opaque handle that may be passed to `remove_timeout`
        to cancel.  Note that unlike the `asyncio` method of the same
        name, the returned object does not have a ``cancel()`` method.

        See `add_timeout` for comments on thread-safety and subclassing.

        .. versionadded:: 4.0
        """
    def call_at(self, when: float, callback: Callable, *args: Any, **kwargs: Any) -> object:
        """Runs the ``callback`` at the absolute time designated by ``when``.

        ``when`` must be a number using the same reference point as
        `IOLoop.time`.

        Returns an opaque handle that may be passed to `remove_timeout`
        to cancel.  Note that unlike the `asyncio` method of the same
        name, the returned object does not have a ``cancel()`` method.

        See `add_timeout` for comments on thread-safety and subclassing.

        .. versionadded:: 4.0
        """
    def remove_timeout(self, timeout: object) -> None:
        """Cancels a pending timeout.

        The argument is a handle as returned by `add_timeout`.  It is
        safe to call `remove_timeout` even if the callback has already
        been run.
        """
    def add_callback(self, callback: Callable, *args: Any, **kwargs: Any) -> None:
        """Calls the given callback on the next I/O loop iteration.

        It is safe to call this method from any thread at any time,
        except from a signal handler.  Note that this is the **only**
        method in `IOLoop` that makes this thread-safety guarantee; all
        other interaction with the `IOLoop` must be done from that
        `IOLoop`'s thread.  `add_callback()` may be used to transfer
        control from other threads to the `IOLoop`'s thread.

        To add a callback from a signal handler, see
        `add_callback_from_signal`.
        """
    def add_callback_from_signal(self, callback: Callable, *args: Any, **kwargs: Any) -> None:
        """Calls the given callback on the next I/O loop iteration.

        Safe for use from a Python signal handler; should not be used
        otherwise.
        """
    def spawn_callback(self, callback: Callable, *args: Any, **kwargs: Any) -> None:
        """Calls the given callback on the next IOLoop iteration.

        As of Tornado 6.0, this method is equivalent to `add_callback`.

        .. versionadded:: 4.0
        """
    def add_future(self, future: Future[_T] | concurrent.futures.Future[_T], callback: Callable[[Future[_T]], None]) -> None:
        """Schedules a callback on the ``IOLoop`` when the given
        `.Future` is finished.

        The callback is invoked with one argument, the
        `.Future`.

        This method only accepts `.Future` objects and not other
        awaitables (unlike most of Tornado where the two are
        interchangeable).
        """
    def run_in_executor(self, executor: concurrent.futures.Executor | None, func: Callable[..., _T], *args: Any) -> Awaitable[_T]:
        """Runs a function in a ``concurrent.futures.Executor``. If
        ``executor`` is ``None``, the IO loop's default executor will be used.

        Use `functools.partial` to pass keyword arguments to ``func``.

        .. versionadded:: 5.0
        """
    def set_default_executor(self, executor: concurrent.futures.Executor) -> None:
        """Sets the default executor to use with :meth:`run_in_executor`.

        .. versionadded:: 5.0
        """
    def split_fd(self, fd: int | _Selectable) -> Tuple[int, int | _Selectable]: ...
    def close_fd(self, fd: int | _Selectable) -> None: ...

class _Timeout:
    """An IOLoop timeout, a UNIX timestamp and a callback"""
    deadline: Incomplete
    callback: Incomplete
    tdeadline: Incomplete
    def __init__(self, deadline: float, callback: Callable[[], None], io_loop: IOLoop) -> None: ...
    def __lt__(self, other: _Timeout) -> bool: ...
    def __le__(self, other: _Timeout) -> bool: ...

class PeriodicCallback:
    '''Schedules the given callback to be called periodically.

    The callback is called every ``callback_time`` milliseconds when
    ``callback_time`` is a float. Note that the timeout is given in
    milliseconds, while most other time-related functions in Tornado use
    seconds. ``callback_time`` may alternatively be given as a
    `datetime.timedelta` object.

    If ``jitter`` is specified, each callback time will be randomly selected
    within a window of ``jitter * callback_time`` milliseconds.
    Jitter can be used to reduce alignment of events with similar periods.
    A jitter of 0.1 means allowing a 10% variation in callback time.
    The window is centered on ``callback_time`` so the total number of calls
    within a given interval should not be significantly affected by adding
    jitter.

    If the callback runs for longer than ``callback_time`` milliseconds,
    subsequent invocations will be skipped to get back on schedule.

    `start` must be called after the `PeriodicCallback` is created.

    .. versionchanged:: 5.0
       The ``io_loop`` argument (deprecated since version 4.1) has been removed.

    .. versionchanged:: 5.1
       The ``jitter`` argument is added.

    .. versionchanged:: 6.2
       If the ``callback`` argument is a coroutine, and a callback runs for
       longer than ``callback_time``, subsequent invocations will be skipped.
       Previously this was only true for regular functions, not coroutines,
       which were "fire-and-forget" for `PeriodicCallback`.

       The ``callback_time`` argument now accepts `datetime.timedelta` objects,
       in addition to the previous numeric milliseconds.
    '''
    callback: Incomplete
    callback_time: Incomplete
    jitter: Incomplete
    def __init__(self, callback: Callable[[], Awaitable | None], callback_time: datetime.timedelta | float, jitter: float = 0) -> None: ...
    io_loop: Incomplete
    def start(self) -> None:
        """Starts the timer."""
    def stop(self) -> None:
        """Stops the timer."""
    def is_running(self) -> bool:
        """Returns ``True`` if this `.PeriodicCallback` has been started.

        .. versionadded:: 4.1
        """
