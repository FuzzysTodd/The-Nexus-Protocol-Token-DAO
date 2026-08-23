from pandas._libs import NaT as NaT
from pandas._typing import Axis
from pandas.core.indexes.base import Index as Index, _new_Index as _new_Index, ensure_index as ensure_index, ensure_index_from_sequences as ensure_index_from_sequences, get_unanimous_names as get_unanimous_names
from pandas.core.indexes.category import CategoricalIndex as CategoricalIndex
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex
from pandas.core.indexes.interval import IntervalIndex as IntervalIndex
from pandas.core.indexes.multi import MultiIndex as MultiIndex
from pandas.core.indexes.period import PeriodIndex as PeriodIndex
from pandas.core.indexes.range import RangeIndex as RangeIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex as TimedeltaIndex
from pandas.errors import InvalidIndexError as InvalidIndexError

__all__ = ['Index', 'MultiIndex', 'CategoricalIndex', 'IntervalIndex', 'RangeIndex', 'InvalidIndexError', 'TimedeltaIndex', 'PeriodIndex', 'DatetimeIndex', '_new_Index', 'NaT', 'ensure_index', 'ensure_index_from_sequences', 'get_objs_combined_axis', 'union_indexes', 'get_unanimous_names', 'all_indexes_same', 'default_index', 'safe_sort_index']

def get_objs_combined_axis(objs, intersect: bool = False, axis: Axis = 0, sort: bool = True, copy: bool = False) -> Index:
    '''
    Extract combined index: return intersection or union (depending on the
    value of "intersect") of indexes on given axis, or None if all objects
    lack indexes (e.g. they are numpy arrays).

    Parameters
    ----------
    objs : list
        Series or DataFrame objects, may be mix of the two.
    intersect : bool, default False
        If True, calculate the intersection between indexes. Otherwise,
        calculate the union.
    axis : {0 or \'index\', 1 or \'outer\'}, default 0
        The axis to extract indexes from.
    sort : bool, default True
        Whether the result index should come out sorted or not.
    copy : bool, default False
        If True, return a copy of the combined index.

    Returns
    -------
    Index
    '''
def safe_sort_index(index: Index) -> Index:
    """
    Returns the sorted index

    We keep the dtypes and the name attributes.

    Parameters
    ----------
    index : an Index

    Returns
    -------
    Index
    """
def union_indexes(indexes, sort: bool | None = True) -> Index:
    """
    Return the union of indexes.

    The behavior of sort and names is not consistent.

    Parameters
    ----------
    indexes : list of Index or list objects
    sort : bool, default True
        Whether the result index should come out sorted or not.

    Returns
    -------
    Index
    """
def all_indexes_same(indexes) -> bool:
    """
    Determine if all indexes contain the same elements.

    Parameters
    ----------
    indexes : iterable of Index objects

    Returns
    -------
    bool
        True if all indexes contain the same elements, False otherwise.
    """
def default_index(n: int) -> RangeIndex: ...
