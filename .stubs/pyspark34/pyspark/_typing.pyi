from _typeshed import Incomplete
from numpy import float32, float64, int32, int64, ndarray
from typing import Callable, Iterable, Sized, TypeVar
from typing_extensions import Protocol

F = TypeVar('F', bound=Callable)
T_co = TypeVar('T_co', covariant=True)
PrimitiveType = bool | float | int | str
NonUDFType: Incomplete

class SupportsIAdd(Protocol):
    def __iadd__(self, other: SupportsIAdd) -> SupportsIAdd: ...

class SupportsOrdering(Protocol):
    def __lt__(self, other: SupportsOrdering) -> bool: ...

class SizedIterable(Sized, Iterable[T_co], Protocol): ...
S = TypeVar('S', bound=SupportsOrdering)
NumberOrArray = TypeVar('NumberOrArray', float, int, complex, int32, int64, float32, float64, ndarray)
