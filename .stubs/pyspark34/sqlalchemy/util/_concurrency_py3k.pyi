import asyncio
from .. import exc as exc
from ..util.typing import Protocol as Protocol, TypeGuard as TypeGuard
from .langhelpers import memoized_property as memoized_property
from _typeshed import Incomplete
from contextvars import Context
from typing import Any, Awaitable, Callable, Coroutine

class greenlet(Protocol):
    dead: bool
    gr_context: Context | None
    def __init__(self, fn: Callable[..., Any], driver: greenlet) -> None: ...
    def throw(self, *arg: Any) -> Any: ...
    def switch(self, value: Any) -> Any: ...

def getcurrent() -> greenlet: ...
def is_exit_exception(e: BaseException) -> bool: ...

class _AsyncIoGreenlet(greenlet):
    dead: bool
    driver: Incomplete
    gr_context: Incomplete
    def __init__(self, fn: Callable[..., Any], driver: greenlet) -> None: ...

def iscoroutine(awaitable: Awaitable[_T_co]) -> TypeGuard[Coroutine[Any, Any, _T_co]]: ...
def await_only(awaitable: Awaitable[_T]) -> _T:
    """Awaits an async function in a sync method.

    The sync method must be inside a :func:`greenlet_spawn` context.
    :func:`await_only` calls cannot be nested.

    :param awaitable: The coroutine to call.

    """
def await_fallback(awaitable: Awaitable[_T]) -> _T:
    """Awaits an async function in a sync method.

    The sync method must be inside a :func:`greenlet_spawn` context.
    :func:`await_fallback` calls cannot be nested.

    :param awaitable: The coroutine to call.

    """
async def greenlet_spawn(fn: Callable[..., _T], *args: Any, _require_await: bool = False, **kwargs: Any) -> _T:
    """Runs a sync function ``fn`` in a new greenlet.

    The sync function can then use :func:`await_only` to wait for async
    functions.

    :param fn: The sync callable to call.
    :param \\*args: Positional arguments to pass to the ``fn`` callable.
    :param \\*\\*kwargs: Keyword arguments to pass to the ``fn`` callable.
    """

class AsyncAdaptedLock:
    def mutex(self) -> asyncio.Lock: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, *arg: Any, **kw: Any) -> None: ...

def get_event_loop() -> asyncio.AbstractEventLoop:
    """vendor asyncio.get_event_loop() for python 3.7 and above.

    Python 3.10 deprecates get_event_loop() as a standalone.

    """
