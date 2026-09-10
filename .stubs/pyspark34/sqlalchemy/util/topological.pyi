from typing import Collection, Iterable, Iterator, Sequence, Set, Tuple

__all__ = ['sort', 'sort_as_subsets', 'find_cycles']

def sort_as_subsets(tuples: Collection[Tuple[_T, _T]], allitems: Collection[_T]) -> Iterator[Sequence[_T]]: ...
def sort(tuples: Collection[Tuple[_T, _T]], allitems: Collection[_T], deterministic_order: bool = True) -> Iterator[_T]:
    '''sort the given list of items by dependency.

    \'tuples\' is a list of tuples representing a partial ordering.

    deterministic_order is no longer used, the order is now always
    deterministic given the order of "allitems".    the flag is there
    for backwards compatibility with Alembic.

    '''
def find_cycles(tuples: Iterable[Tuple[_T, _T]], allitems: Iterable[_T]) -> Set[_T]: ...
