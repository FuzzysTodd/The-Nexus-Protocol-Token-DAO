import numpy as np
from _typeshed import Incomplete
from pandas import Index as Index, Series as Series
from pandas._config import get_option as get_option
from pandas._libs import lib as lib
from pandas._libs.interval import Interval as Interval, IntervalMixin as IntervalMixin, VALID_CLOSED as VALID_CLOSED, intervals_to_interval_bounds as intervals_to_interval_bounds
from pandas._libs.missing import NA as NA
from pandas._typing import ArrayLike as ArrayLike, AxisInt as AxisInt, Dtype as Dtype, IntervalClosedType as IntervalClosedType, NpDtype as NpDtype, PositionalIndexer as PositionalIndexer, ScalarIndexer as ScalarIndexer, SequenceIndexer as SequenceIndexer, SortKind as SortKind, TimeArrayLike as TimeArrayLike, npt as npt
from pandas.core.algorithms import isin as isin, take as take, unique as unique, value_counts as value_counts
from pandas.core.arrays.base import ExtensionArray as ExtensionArray
from pandas.core.arrays.datetimes import DatetimeArray as DatetimeArray
from pandas.core.arrays.timedeltas import TimedeltaArray as TimedeltaArray
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike, extract_array as extract_array
from pandas.core.dtypes.cast import LossySetitemError as LossySetitemError, maybe_upcast_numeric_to_64bit as maybe_upcast_numeric_to_64bit
from pandas.core.dtypes.common import is_categorical_dtype as is_categorical_dtype, is_dtype_equal as is_dtype_equal, is_float_dtype as is_float_dtype, is_integer_dtype as is_integer_dtype, is_interval_dtype as is_interval_dtype, is_list_like as is_list_like, is_object_dtype as is_object_dtype, is_scalar as is_scalar, is_string_dtype as is_string_dtype, needs_i8_conversion as needs_i8_conversion, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import IntervalDtype as IntervalDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCDatetimeIndex as ABCDatetimeIndex, ABCIntervalIndex as ABCIntervalIndex, ABCPeriodIndex as ABCPeriodIndex
from pandas.core.dtypes.missing import is_valid_na_for_dtype as is_valid_na_for_dtype, isna as isna, notna as notna
from pandas.core.indexers import check_array_indexer as check_array_indexer
from pandas.core.ops import invalid_comparison as invalid_comparison, unpack_zerodim_and_defer as unpack_zerodim_and_defer
from pandas.errors import IntCastingNaNError as IntCastingNaNError
from pandas.util._decorators import Appender as Appender
from typing import Iterator, Literal, Sequence, TypeVar, overload

IntervalArrayT = TypeVar('IntervalArrayT', bound='IntervalArray')
IntervalSideT = TimeArrayLike | np.ndarray
IntervalOrNA = Interval | float

class IntervalArray(IntervalMixin, ExtensionArray):
    can_hold_na: bool
    @property
    def ndim(self) -> Literal[1]: ...
    def __new__(cls, data, closed: Incomplete | None = None, dtype: Dtype | None = None, copy: bool = False, verify_integrity: bool = True): ...
    @classmethod
    def from_breaks(cls, breaks, closed: IntervalClosedType | None = 'right', copy: bool = False, dtype: Dtype | None = None) -> IntervalArrayT: ...
    @classmethod
    def from_arrays(cls, left, right, closed: IntervalClosedType | None = 'right', copy: bool = False, dtype: Dtype | None = None) -> IntervalArrayT: ...
    @classmethod
    def from_tuples(cls, data, closed: IntervalClosedType | None = 'right', copy: bool = False, dtype: Dtype | None = None) -> IntervalArrayT: ...
    @property
    def dtype(self) -> IntervalDtype: ...
    @property
    def nbytes(self) -> int: ...
    @property
    def size(self) -> int: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, key: ScalarIndexer) -> IntervalOrNA: ...
    @overload
    def __getitem__(self, key: SequenceIndexer) -> IntervalArrayT: ...
    def __setitem__(self, key, value) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def argsort(self, *, ascending: bool = True, kind: SortKind = 'quicksort', na_position: str = 'last', **kwargs) -> np.ndarray: ...
    def min(self, *, axis: AxisInt | None = None, skipna: bool = True) -> IntervalOrNA: ...
    def max(self, *, axis: AxisInt | None = None, skipna: bool = True) -> IntervalOrNA: ...
    def fillna(self, value: Incomplete | None = None, method: Incomplete | None = None, limit: Incomplete | None = None) -> IntervalArrayT:
        """
        Fill NA/NaN values using the specified method.

        Parameters
        ----------
        value : scalar, dict, Series
            If a scalar value is passed it is used to fill all missing values.
            Alternatively, a Series or dict can be used to fill in different
            values for each index. The value should not be a list. The
            value(s) passed should be either Interval objects or NA/NaN.
        method : {'backfill', 'bfill', 'pad', 'ffill', None}, default None
            (Not implemented yet for IntervalArray)
            Method to use for filling holes in reindexed Series
        limit : int, default None
            (Not implemented yet for IntervalArray)
            If method is specified, this is the maximum number of consecutive
            NaN values to forward/backward fill. In other words, if there is
            a gap with more than this number of consecutive NaNs, it will only
            be partially filled. If method is not specified, this is the
            maximum number of entries along the entire axis where NaNs will be
            filled.

        Returns
        -------
        filled : IntervalArray with NA/NaN filled
        """
    def astype(self, dtype, copy: bool = True):
        """
        Cast to an ExtensionArray or NumPy array with dtype 'dtype'.

        Parameters
        ----------
        dtype : str or dtype
            Typecode or data-type to which the array is cast.

        copy : bool, default True
            Whether to copy the data, even if not necessary. If False,
            a copy is made only if the old dtype does not match the
            new dtype.

        Returns
        -------
        array : ExtensionArray or ndarray
            ExtensionArray or NumPy ndarray with 'dtype' for its dtype.
        """
    def equals(self, other) -> bool: ...
    def copy(self) -> IntervalArrayT:
        """
        Return a copy of the array.

        Returns
        -------
        IntervalArray
        """
    def isna(self) -> np.ndarray: ...
    def shift(self, periods: int = 1, fill_value: object = None) -> IntervalArray: ...
    def take(self, indices, *, allow_fill: bool = False, fill_value: Incomplete | None = None, axis: Incomplete | None = None, **kwargs) -> IntervalArrayT:
        '''
        Take elements from the IntervalArray.

        Parameters
        ----------
        indices : sequence of integers
            Indices to be taken.

        allow_fill : bool, default False
            How to handle negative values in `indices`.

            * False: negative values in `indices` indicate positional indices
              from the right (the default). This is similar to
              :func:`numpy.take`.

            * True: negative values in `indices` indicate
              missing values. These values are set to `fill_value`. Any other
              other negative values raise a ``ValueError``.

        fill_value : Interval or NA, optional
            Fill value to use for NA-indices when `allow_fill` is True.
            This may be ``None``, in which case the default NA value for
            the type, ``self.dtype.na_value``, is used.

            For many ExtensionArrays, there will be two representations of
            `fill_value`: a user-facing "boxed" scalar, and a low-level
            physical NA value. `fill_value` should be the user-facing version,
            and the implementation should handle translating that to the
            physical version for processing the take if necessary.

        axis : any, default None
            Present for compat with IntervalIndex; does nothing.

        Returns
        -------
        IntervalArray

        Raises
        ------
        IndexError
            When the indices are out of bounds for the array.
        ValueError
            When `indices` contains negative values other than ``-1``
            and `allow_fill` is True.
        '''
    def value_counts(self, dropna: bool = True) -> Series:
        """
        Returns a Series containing counts of each interval.

        Parameters
        ----------
        dropna : bool, default True
            Don't include counts of NaN.

        Returns
        -------
        counts : Series

        See Also
        --------
        Series.value_counts
        """
    @property
    def left(self):
        """
        Return the left endpoints of each Interval in the IntervalArray as an Index.
        """
    @property
    def right(self):
        """
        Return the right endpoints of each Interval in the IntervalArray as an Index.
        """
    @property
    def length(self) -> Index:
        """
        Return an Index with entries denoting the length of each Interval.
        """
    @property
    def mid(self) -> Index:
        """
        Return the midpoint of each Interval in the IntervalArray as an Index.
        """
    def overlaps(self, other): ...
    @property
    def closed(self) -> IntervalClosedType:
        """
        String describing the inclusive side the intervals.

        Either ``left``, ``right``, ``both`` or ``neither``.
        """
    def set_closed(self, closed: IntervalClosedType) -> IntervalArrayT: ...
    @property
    def is_non_overlapping_monotonic(self) -> bool: ...
    def __array__(self, dtype: NpDtype | None = None) -> np.ndarray:
        """
        Return the IntervalArray's data as a numpy array of Interval
        objects (with dtype='object')
        """
    def __arrow_array__(self, type: Incomplete | None = None):
        """
        Convert myself into a pyarrow Array.
        """
    def to_tuples(self, na_tuple: bool = True) -> np.ndarray: ...
    def insert(self, loc: int, item: Interval) -> IntervalArrayT:
        """
        Return a new IntervalArray inserting new item at location. Follows
        Python numpy.insert semantics for negative values.  Only Interval
        objects and NA can be inserted into an IntervalIndex

        Parameters
        ----------
        loc : int
        item : Interval

        Returns
        -------
        IntervalArray
        """
    def delete(self, loc) -> IntervalArrayT: ...
    def repeat(self, repeats: int | Sequence[int], axis: AxisInt | None = None) -> IntervalArrayT: ...
    def contains(self, other): ...
    def isin(self, values) -> npt.NDArray[np.bool_]: ...
    def unique(self) -> IntervalArray: ...
