import numpy as np
from _typeshed import Incomplete
from pandas._libs import lib as lib
from pandas._libs.interval import Interval as Interval, IntervalMixin as IntervalMixin, IntervalTree as IntervalTree
from pandas._libs.tslibs import BaseOffset as BaseOffset, Timedelta as Timedelta, Timestamp as Timestamp, to_offset as to_offset
from pandas._typing import Dtype as Dtype, DtypeObj as DtypeObj, IntervalClosedType as IntervalClosedType, npt as npt
from pandas.core.algorithms import unique as unique
from pandas.core.arrays.interval import IntervalArray as IntervalArray
from pandas.core.dtypes.cast import find_common_type as find_common_type, infer_dtype_from_scalar as infer_dtype_from_scalar, maybe_box_datetimelike as maybe_box_datetimelike, maybe_downcast_numeric as maybe_downcast_numeric, maybe_upcast_numeric_to_64bit as maybe_upcast_numeric_to_64bit
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int, is_datetime64tz_dtype as is_datetime64tz_dtype, is_datetime_or_timedelta_dtype as is_datetime_or_timedelta_dtype, is_dtype_equal as is_dtype_equal, is_float as is_float, is_float_dtype as is_float_dtype, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_interval_dtype as is_interval_dtype, is_list_like as is_list_like, is_number as is_number, is_object_dtype as is_object_dtype, is_scalar as is_scalar
from pandas.core.dtypes.dtypes import IntervalDtype as IntervalDtype
from pandas.core.dtypes.missing import is_valid_na_for_dtype as is_valid_na_for_dtype
from pandas.core.indexers import is_valid_positional_slice as is_valid_positional_slice
from pandas.core.indexes.base import Index as Index, ensure_index as ensure_index, maybe_extract_name as maybe_extract_name
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex, date_range as date_range
from pandas.core.indexes.extension import ExtensionIndex as ExtensionIndex, inherit_names as inherit_names
from pandas.core.indexes.multi import MultiIndex as MultiIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex as TimedeltaIndex, timedelta_range as timedelta_range
from pandas.errors import InvalidIndexError as InvalidIndexError
from pandas.util._decorators import Appender as Appender, cache_readonly as cache_readonly
from pandas.util._exceptions import rewrite_exception as rewrite_exception
from typing import Any, Hashable

class IntervalIndex(ExtensionIndex):
    closed: IntervalClosedType
    is_non_overlapping_monotonic: bool
    closed_left: bool
    closed_right: bool
    open_left: bool
    open_right: bool
    def __new__(cls, data, closed: Incomplete | None = None, dtype: Dtype | None = None, copy: bool = False, name: Hashable = None, verify_integrity: bool = True) -> IntervalIndex: ...
    @classmethod
    def from_breaks(cls, breaks, closed: IntervalClosedType | None = 'right', name: Hashable = None, copy: bool = False, dtype: Dtype | None = None) -> IntervalIndex: ...
    @classmethod
    def from_arrays(cls, left, right, closed: IntervalClosedType = 'right', name: Hashable = None, copy: bool = False, dtype: Dtype | None = None) -> IntervalIndex: ...
    @classmethod
    def from_tuples(cls, data, closed: IntervalClosedType = 'right', name: Hashable = None, copy: bool = False, dtype: Dtype | None = None) -> IntervalIndex: ...
    def __contains__(self, key: Any) -> bool:
        """
        return a boolean if this key is IN the index
        We *only* accept an Interval

        Parameters
        ----------
        key : Interval

        Returns
        -------
        bool
        """
    def __reduce__(self): ...
    @property
    def inferred_type(self) -> str:
        """Return a string of the type inferred from the values"""
    def memory_usage(self, deep: bool = False) -> int: ...
    def is_monotonic_decreasing(self) -> bool:
        """
        Return True if the IntervalIndex is monotonic decreasing (only equal or
        decreasing values), else False
        """
    def is_unique(self) -> bool:
        """
        Return True if the IntervalIndex contains unique elements, else False.
        """
    @property
    def is_overlapping(self) -> bool:
        """
        Return True if the IntervalIndex has overlapping intervals, else False.

        Two intervals overlap if they share a common point, including closed
        endpoints. Intervals that only have an open endpoint in common do not
        overlap.

        Returns
        -------
        bool
            Boolean indicating if the IntervalIndex has overlapping intervals.

        See Also
        --------
        Interval.overlaps : Check whether two Interval objects overlap.
        IntervalIndex.overlaps : Check an IntervalIndex elementwise for
            overlaps.

        Examples
        --------
        >>> index = pd.IntervalIndex.from_tuples([(0, 2), (1, 3), (4, 5)])
        >>> index
        IntervalIndex([(0, 2], (1, 3], (4, 5]],
              dtype='interval[int64, right]')
        >>> index.is_overlapping
        True

        Intervals that share closed endpoints overlap:

        >>> index = pd.interval_range(0, 3, closed='both')
        >>> index
        IntervalIndex([[0, 1], [1, 2], [2, 3]],
              dtype='interval[int64, both]')
        >>> index.is_overlapping
        True

        Intervals that only have an open endpoint in common do not overlap:

        >>> index = pd.interval_range(0, 3, closed='left')
        >>> index
        IntervalIndex([[0, 1), [1, 2), [2, 3)],
              dtype='interval[int64, left]')
        >>> index.is_overlapping
        False
        """
    def get_loc(self, key) -> int | slice | np.ndarray:
        """
        Get integer location, slice or boolean mask for requested label.

        Parameters
        ----------
        key : label

        Returns
        -------
        int if unique index, slice if monotonic index, else mask

        Examples
        --------
        >>> i1, i2 = pd.Interval(0, 1), pd.Interval(1, 2)
        >>> index = pd.IntervalIndex([i1, i2])
        >>> index.get_loc(1)
        0

        You can also supply a point inside an interval.

        >>> index.get_loc(1.5)
        1

        If a label is in several intervals, you get the locations of all the
        relevant intervals.

        >>> i3 = pd.Interval(0, 2)
        >>> overlapping_index = pd.IntervalIndex([i1, i2, i3])
        >>> overlapping_index.get_loc(0.5)
        array([ True, False,  True])

        Only exact matches will be returned if an interval is provided.

        >>> index.get_loc(pd.Interval(0, 1))
        0
        """
    def get_indexer_non_unique(self, target: Index) -> tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]: ...
    def left(self) -> Index: ...
    def right(self) -> Index: ...
    def mid(self) -> Index: ...
    @property
    def length(self) -> Index: ...

def interval_range(start: Incomplete | None = None, end: Incomplete | None = None, periods: Incomplete | None = None, freq: Incomplete | None = None, name: Hashable = None, closed: IntervalClosedType = 'right') -> IntervalIndex:
    """
    Return a fixed frequency IntervalIndex.

    Parameters
    ----------
    start : numeric or datetime-like, default None
        Left bound for generating intervals.
    end : numeric or datetime-like, default None
        Right bound for generating intervals.
    periods : int, default None
        Number of periods to generate.
    freq : numeric, str, datetime.timedelta, or DateOffset, default None
        The length of each interval. Must be consistent with the type of start
        and end, e.g. 2 for numeric, or '5H' for datetime-like.  Default is 1
        for numeric and 'D' for datetime-like.
    name : str, default None
        Name of the resulting IntervalIndex.
    closed : {'left', 'right', 'both', 'neither'}, default 'right'
        Whether the intervals are closed on the left-side, right-side, both
        or neither.

    Returns
    -------
    IntervalIndex

    See Also
    --------
    IntervalIndex : An Index of intervals that are all closed on the same side.

    Notes
    -----
    Of the four parameters ``start``, ``end``, ``periods``, and ``freq``,
    exactly three must be specified. If ``freq`` is omitted, the resulting
    ``IntervalIndex`` will have ``periods`` linearly spaced elements between
    ``start`` and ``end``, inclusively.

    To learn more about datetime-like frequency strings, please see `this link
    <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases>`__.

    Examples
    --------
    Numeric ``start`` and  ``end`` is supported.

    >>> pd.interval_range(start=0, end=5)
    IntervalIndex([(0, 1], (1, 2], (2, 3], (3, 4], (4, 5]],
                  dtype='interval[int64, right]')

    Additionally, datetime-like input is also supported.

    >>> pd.interval_range(start=pd.Timestamp('2017-01-01'),
    ...                   end=pd.Timestamp('2017-01-04'))
    IntervalIndex([(2017-01-01, 2017-01-02], (2017-01-02, 2017-01-03],
                   (2017-01-03, 2017-01-04]],
                  dtype='interval[datetime64[ns], right]')

    The ``freq`` parameter specifies the frequency between the left and right.
    endpoints of the individual intervals within the ``IntervalIndex``.  For
    numeric ``start`` and ``end``, the frequency must also be numeric.

    >>> pd.interval_range(start=0, periods=4, freq=1.5)
    IntervalIndex([(0.0, 1.5], (1.5, 3.0], (3.0, 4.5], (4.5, 6.0]],
                  dtype='interval[float64, right]')

    Similarly, for datetime-like ``start`` and ``end``, the frequency must be
    convertible to a DateOffset.

    >>> pd.interval_range(start=pd.Timestamp('2017-01-01'),
    ...                   periods=3, freq='MS')
    IntervalIndex([(2017-01-01, 2017-02-01], (2017-02-01, 2017-03-01],
                   (2017-03-01, 2017-04-01]],
                  dtype='interval[datetime64[ns], right]')

    Specify ``start``, ``end``, and ``periods``; the frequency is generated
    automatically (linearly spaced).

    >>> pd.interval_range(start=0, end=6, periods=4)
    IntervalIndex([(0.0, 1.5], (1.5, 3.0], (3.0, 4.5], (4.5, 6.0]],
              dtype='interval[float64, right]')

    The ``closed`` parameter specifies which endpoints of the individual
    intervals within the ``IntervalIndex`` are closed.

    >>> pd.interval_range(end=5, periods=4, closed='both')
    IntervalIndex([[1, 2], [2, 3], [3, 4], [4, 5]],
                  dtype='interval[int64, both]')
    """
