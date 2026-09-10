import abc
import asyncio
import concurrent.futures
from _typeshed import Incomplete
from tornado.gen import convert_yielded as convert_yielded
from tornado.ioloop import IOLoop as IOLoop, _Selectable
from typing import Any, Awaitable, Callable
from typing_extensions import Protocol

class _HasFileno(Protocol):
    def fileno(self) -> int: ...

class BaseAsyncIOLoop(IOLoop):
    asyncio_loop: Incomplete
    selector_loop: Incomplete
    handlers: Incomplete
    readers: Incomplete
    writers: Incomplete
    closing: bool
    def initialize(self, asyncio_loop: asyncio.AbstractEventLoop, **kwargs: Any) -> None: ...
    def close(self, all_fds: bool = False) -> None: ...
    def add_handler(self, fd: int | _Selectable, handler: Callable[..., None], events: int) -> None: ...
    def update_handler(self, fd: int | _Selectable, events: int) -> None: ...
    def remove_handler(self, fd: int | _Selectable) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def call_at(self, when: float, callback: Callable, *args: Any, **kwargs: Any) -> object: ...
    def remove_timeout(self, timeout: object) -> None: ...
    def add_callback(self, callback: Callable, *args: Any, **kwargs: Any) -> None: ...
    def add_callback_from_signal(self, callback: Callable, *args: Any, **kwargs: Any) -> None: ...
    def run_in_executor(self, executor: concurrent.futures.Executor | None, func: Callable[..., _T], *args: Any) -> Awaitable[_T]: ...
    def set_default_executor(self, executor: concurrent.futures.Executor) -> None: ...

class AsyncIOMainLoop(BaseAsyncIOLoop):
    """``AsyncIOMainLoop`` creates an `.IOLoop` that corresponds to the
    current ``asyncio`` event loop (i.e. the one returned by
    ``asyncio.get_event_loop()``).

    .. deprecated:: 5.0

       Now used automatically when appropriate; it is no longer necessary
       to refer to this class directly.

    .. versionchanged:: 5.0

       Closing an `AsyncIOMainLoop` now closes the underlying asyncio loop.
    """
    def initialize(self, **kwargs: Any) -> None: ...

class AsyncIOLoop(BaseAsyncIOLoop):
    """``AsyncIOLoop`` is an `.IOLoop` that runs on an ``asyncio`` event loop.
    This class follows the usual Tornado semantics for creating new
    ``IOLoops``; these loops are not necessarily related to the
    ``asyncio`` default event loop.

    Each ``AsyncIOLoop`` creates a new ``asyncio.EventLoop``; this object
    can be accessed with the ``asyncio_loop`` attribute.

    .. versionchanged:: 6.2

       Support explicit ``asyncio_loop`` argument
       for specifying the asyncio loop to attach to,
       rather than always creating a new one with the default policy.

    .. versionchanged:: 5.0

       When an ``AsyncIOLoop`` becomes the current `.IOLoop`, it also sets
       the current `asyncio` event loop.

    .. deprecated:: 5.0

       Now used automatically when appropriate; it is no longer necessary
       to refer to this class directly.
    """
    is_current: bool
    def initialize(self, **kwargs: Any) -> None: ...
    def close(self, all_fds: bool = False) -> None: ...

def to_tornado_future(asyncio_future: asyncio.Future) -> asyncio.Future:
    """Convert an `asyncio.Future` to a `tornado.concurrent.Future`.

    .. versionadded:: 4.1

    .. deprecated:: 5.0
       Tornado ``Futures`` have been merged with `asyncio.Future`,
       so this method is now a no-op.
    """
def to_asyncio_future(tornado_future: asyncio.Future) -> asyncio.Future:
    """Convert a Tornado yieldable object to an `asyncio.Future`.

    .. versionadded:: 4.1

    .. versionchanged:: 4.3
       Now accepts any yieldable object, not just
       `tornado.concurrent.Future`.

    .. deprecated:: 5.0
       Tornado ``Futures`` have been merged with `asyncio.Future`,
       so this method is now equivalent to `tornado.gen.convert_yielded`.
    """

class AnyThreadEventLoopPolicy(_BasePolicy):
    """Event loop policy that allows loop creation on any thread.

    The default `asyncio` event loop policy only automatically creates
    event loops in the main threads. Other threads must create event
    loops explicitly or `asyncio.get_event_loop` (and therefore
    `.IOLoop.current`) will fail. Installing this policy allows event
    loops to be created automatically on any thread, matching the
    behavior of Tornado versions prior to 5.0 (or 5.0 on Python 2).

    Usage::

        asyncio.set_event_loop_policy(AnyThreadEventLoopPolicy())

    .. versionadded:: 5.0

    .. deprecated:: 6.2

        ``AnyThreadEventLoopPolicy`` affects the implicit creation
        of an event loop, which is deprecated in Python 3.10 and
        will be removed in a future version of Python. At that time
        ``AnyThreadEventLoopPolicy`` will no longer be useful.
        If you are relying on it, use `asyncio.new_event_loop`
        or `asyncio.run` explicitly in any non-main threads that
        need event loops.
    """
    def __init__(self) -> None: ...
    def get_event_loop(self) -> asyncio.AbstractEventLoop: ...

class AddThreadSelectorEventLoop(asyncio.AbstractEventLoop, metaclass=abc.ABCMeta):
    """Wrap an event loop to add implementations of the ``add_reader`` method family.

    Instances of this class start a second thread to run a selector.
    This thread is completely hidden from the user; all callbacks are
    run on the wrapped event loop's thread.

    This class is used automatically by Tornado; applications should not need
    to refer to it directly.

    It is safe to wrap any event loop with this class, although it only makes sense
    for event loops that do not implement the ``add_reader`` family of methods
    themselves (i.e. ``WindowsProactorEventLoop``)

    Closing the ``AddThreadSelectorEventLoop`` also closes the wrapped event loop.

    """
    MY_ATTRIBUTES: Incomplete
    def __getattribute__(self, name: str) -> Any: ...
    def __init__(self, real_loop: asyncio.AbstractEventLoop) -> None: ...
    def __del__(self) -> None: ...
    def close(self) -> None: ...
    def add_reader(self, fd: _FileDescriptorLike, callback: Callable[..., None], *args: Any) -> None: ...
    def add_writer(self, fd: _FileDescriptorLike, callback: Callable[..., None], *args: Any) -> None: ...
    def remove_reader(self, fd: _FileDescriptorLike) -> bool: ...
    def remove_writer(self, fd: _FileDescriptorLike) -> bool: ...
