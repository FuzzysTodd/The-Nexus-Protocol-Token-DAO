import abc
from ... import util as util
from ...util.typing import Literal as Literal, Self as Self
from typing import Any, AsyncGenerator, AsyncIterator, Awaitable, Callable, Dict, Generator, Generic, Tuple

class ReversibleProxy(Generic[_PT]): ...

class StartableContext(Awaitable[_T_co], abc.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def start(self, is_ctxmanager: bool = False) -> _T_co: ...
    def __await__(self) -> Generator[Any, Any, _T_co]: ...
    async def __aenter__(self) -> _T_co: ...
    @abc.abstractmethod
    async def __aexit__(self, type_: Any, value: Any, traceback: Any) -> bool | None: ...

class GeneratorStartableContext(StartableContext[_T_co]):
    gen: AsyncGenerator[_T_co, Any]
    def __init__(self, func: Callable[..., AsyncIterator[_T_co]], args: Tuple[Any, ...], kwds: Dict[str, Any]) -> None: ...
    async def start(self, is_ctxmanager: bool = False) -> _T_co: ...
    async def __aexit__(self, typ: Any, value: Any, traceback: Any) -> bool | None: ...

def asyncstartablecontext(func: Callable[..., AsyncIterator[_T_co]]) -> Callable[..., GeneratorStartableContext[_T_co]]:
    """@asyncstartablecontext decorator.

    the decorated function can be called either as ``async with fn()``, **or**
    ``await fn()``.   This is decidedly different from what
    ``@contextlib.asynccontextmanager`` supports, and the usage pattern
    is different as well.

    Typical usage::

        @asyncstartablecontext
        async def some_async_generator(<arguments>):
            <setup>
            try:
                yield <value>
            except GeneratorExit:
                # return value was awaited, no context manager is present
                # and caller will .close() the resource explicitly
                pass
            else:
                <context manager cleanup>


    Above, ``GeneratorExit`` is caught if the function were used as an
    ``await``.  In this case, it's essential that the cleanup does **not**
    occur, so there should not be a ``finally`` block.

    If ``GeneratorExit`` is not invoked, this means we're in ``__aexit__``
    and we were invoked as a context manager, and cleanup should proceed.


    """

class ProxyComparable(ReversibleProxy[_PT]):
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
