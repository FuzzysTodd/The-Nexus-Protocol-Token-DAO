from typing import Iterable, List, overload
from typing_extensions import SupportsIndex

__all__ = ['explode_text_fragments']

class _ExplodedList(List[_T]):
    """
    Wrapper around a list, that marks it as 'exploded'.

    As soon as items are added or the list is extended, the new items are
    automatically exploded as well.
    """
    exploded: bool
    def append(self, item: _T) -> None: ...
    def extend(self, lst: Iterable[_T]) -> None: ...
    def insert(self, index: SupportsIndex, item: _T) -> None: ...
    @overload
    def __setitem__(self, index: SupportsIndex, value: _T) -> None: ...
    @overload
    def __setitem__(self, index: slice, value: Iterable[_T]) -> None: ...

def explode_text_fragments(fragments: Iterable[_T]) -> _ExplodedList[_T]:
    """
    Turn a list of (style_str, text) tuples into another list where each string is
    exactly one character.

    It should be fine to call this function several times. Calling this on a
    list that is already exploded, is a null operation.

    :param fragments: List of (style, text) tuples.
    """
