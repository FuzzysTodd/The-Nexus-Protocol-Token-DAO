from _typeshed import Incomplete
from pyspark._typing import SizedIterable
from typing import Iterable, Iterator, TypeVar

__all__ = ['ResultIterable']

T = TypeVar('T')

class ResultIterable(Iterable[T]):
    """
    A special result iterable. This is used because the standard
    iterator can not be pickled
    """
    data: Incomplete
    index: int
    maxindex: Incomplete
    def __init__(self, data: SizedIterable[T]) -> None: ...
    def __iter__(self) -> Iterator[T]: ...
    def __len__(self) -> int: ...
