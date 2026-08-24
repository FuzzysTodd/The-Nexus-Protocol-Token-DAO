from typing import Any, Callable, Iterable, Tuple, Type, TypeVar, overload

T = TypeVar('T')
Result = Iterable[Any | Tuple[Any] | Tuple[str, Any] | Tuple[str, Any, Any]]
RichReprResult = Result

class ReprError(Exception):
    """An error occurred when attempting to build a repr."""

@overload
def auto(cls) -> Type[T]: ...
@overload
def auto(*, angular: bool = False) -> Callable[[Type[T]], Type[T]]: ...
@overload
def rich_repr(cls) -> Type[T]: ...
@overload
def rich_repr(*, angular: bool = False) -> Callable[[Type[T]], Type[T]]: ...
