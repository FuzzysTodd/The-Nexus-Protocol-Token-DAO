import enum
from ._core._eventloop import get_asynclib as get_asynclib
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Generic, Literal, TypeVar, overload

T = TypeVar('T')
D = TypeVar('D')

async def checkpoint() -> None:
    """
    Check for cancellation and allow the scheduler to switch to another task.

    Equivalent to (but more efficient than)::

        await checkpoint_if_cancelled()
        await cancel_shielded_checkpoint()


    .. versionadded:: 3.0

    """
async def checkpoint_if_cancelled() -> None:
    """
    Enter a checkpoint if the enclosing cancel scope has been cancelled.

    This does not allow the scheduler to switch to a different task.

    .. versionadded:: 3.0

    """
async def cancel_shielded_checkpoint() -> None:
    """
    Allow the scheduler to switch to another task but without checking for cancellation.

    Equivalent to (but potentially more efficient than)::

        with CancelScope(shield=True):
            await checkpoint()


    .. versionadded:: 3.0

    """
def current_token() -> object:
    """Return a backend specific token object that can be used to get back to the event loop."""

@dataclass(frozen=True)
class _TokenWrapper:
    def __init__(self, _token) -> None: ...

class _NoValueSet(enum.Enum):
    NO_VALUE_SET: Incomplete

class RunvarToken(Generic[T]):
    def __init__(self, var: RunVar[T], value: T | Literal[_NoValueSet.NO_VALUE_SET]) -> None: ...

class RunVar(Generic[T]):
    """
    Like a :class:`~contextvars.ContextVar`, except scoped to the running event loop.
    """
    NO_VALUE_SET: Literal[_NoValueSet.NO_VALUE_SET]
    def __init__(self, name: str, default: T | Literal[_NoValueSet.NO_VALUE_SET] = ...) -> None: ...
    @overload
    def get(self, default: D) -> T | D: ...
    @overload
    def get(self) -> T: ...
    def set(self, value: T) -> RunvarToken[T]: ...
    def reset(self, token: RunvarToken[T]) -> None: ...
