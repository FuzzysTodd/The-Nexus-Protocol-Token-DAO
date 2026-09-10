from _typeshed import Incomplete
from pandas import DataFrame as DataFrame, Series as Series
from pandas._typing import PositionalIndexer as PositionalIndexer
from pandas.core.dtypes.common import is_integer as is_integer, is_list_like as is_list_like
from pandas.core.groupby import groupby as groupby
from pandas.util._decorators import cache_readonly as cache_readonly, doc as doc
from typing import Literal

class GroupByIndexingMixin:
    """
    Mixin for adding ._positional_selector to GroupBy.
    """

class GroupByPositionalSelector:
    groupby_object: Incomplete
    def __init__(self, groupby_object: groupby.GroupBy) -> None: ...
    def __getitem__(self, arg: PositionalIndexer | tuple) -> DataFrame | Series:
        """
        Select by positional index per group.

        Implements GroupBy._positional_selector

        Parameters
        ----------
        arg : PositionalIndexer | tuple
            Allowed values are:
            - int
            - int valued iterable such as list or range
            - slice with step either None or positive
            - tuple of integers and slices

        Returns
        -------
        Series
            The filtered subset of the original groupby Series.
        DataFrame
            The filtered subset of the original groupby DataFrame.

        See Also
        --------
        DataFrame.iloc : Integer-location based indexing for selection by position.
        GroupBy.head : Return first n rows of each group.
        GroupBy.tail : Return last n rows of each group.
        GroupBy._positional_selector : Return positional selection for each group.
        GroupBy.nth : Take the nth row from each group if n is an int, or a
            subset of rows, if n is a list of ints.
        """

class GroupByNthSelector:
    """
    Dynamically substituted for GroupBy.nth to enable both call and index
    """
    groupby_object: Incomplete
    def __init__(self, groupby_object: groupby.GroupBy) -> None: ...
    def __call__(self, n: PositionalIndexer | tuple, dropna: Literal['any', 'all', None] = None) -> DataFrame | Series: ...
    def __getitem__(self, n: PositionalIndexer | tuple) -> DataFrame | Series: ...
