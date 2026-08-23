from _typeshed import Incomplete
from pandas.core.base import PandasObject as PandasObject
from pandas.io.formats.printing import pprint_thing as pprint_thing
from typing import Any

class FrozenList(PandasObject, list):
    """
    Container that doesn't allow setting item *but*
    because it's technically hashable, will be used
    for lookups, appropriately, etc.
    """
    def union(self, other) -> FrozenList:
        """
        Returns a FrozenList with other concatenated to the end of self.

        Parameters
        ----------
        other : array-like
            The array-like whose elements we are concatenating.

        Returns
        -------
        FrozenList
            The collection difference between self and other.
        """
    def difference(self, other) -> FrozenList:
        """
        Returns a FrozenList with elements from other removed from self.

        Parameters
        ----------
        other : array-like
            The array-like whose elements we are removing self.

        Returns
        -------
        FrozenList
            The collection difference between self and other.
        """
    __add__ = union
    __iadd__ = union
    def __getitem__(self, n): ...
    def __radd__(self, other): ...
    def __eq__(self, other: Any) -> bool: ...
    __req__ = __eq__
    def __mul__(self, other): ...
    __imul__ = __mul__
    def __reduce__(self): ...
    def __hash__(self) -> int: ...
    __setitem__: Incomplete
    __setslice__: Incomplete
    __delitem__: Incomplete
    __delslice__: Incomplete
    pop: Incomplete
    append: Incomplete
    extend: Incomplete
    remove: Incomplete
    sort: Incomplete
    insert: Incomplete
