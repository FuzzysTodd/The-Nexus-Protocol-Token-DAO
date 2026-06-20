import numpy as np
from _typeshed import Incomplete
from pandas._libs import algos as algos, lib as lib
from pandas._libs.arrays import NDArrayBacked as NDArrayBacked
from pandas._libs.tslibs import BaseOffset as BaseOffset, IncompatibleFrequency as IncompatibleFrequency, NaT as NaT, NaTType as NaTType, Period as Period, Resolution as Resolution, Tick as Tick, Timedelta as Timedelta, Timestamp as Timestamp, astype_overflowsafe as astype_overflowsafe, delta_to_nanoseconds as delta_to_nanoseconds, get_unit_from_dtype as get_unit_from_dtype, iNaT as iNaT, ints_to_pydatetime as ints_to_pydatetime, ints_to_pytimedelta as ints_to_pytimedelta, to_offset as to_offset
from pandas._libs.tslibs.fields import RoundTo as RoundTo, round_nsint64 as round_nsint64
from pandas._libs.tslibs.np_datetime import compare_mismatched_resolutions as compare_mismatched_resolutions
from pandas._libs.tslibs.timestamps import integer_op_not_supported as integer_op_not_supported
from pandas._typing import ArrayLike as ArrayLike, AxisInt as AxisInt, DatetimeLikeScalar as DatetimeLikeScalar, Dtype as Dtype, DtypeObj as DtypeObj, F as F, NpDtype as NpDtype, PositionalIndexer2D as PositionalIndexer2D, PositionalIndexerTuple as PositionalIndexerTuple, ScalarIndexer as ScalarIndexer, SequenceIndexer as SequenceIndexer, TimeAmbiguous as TimeAmbiguous, TimeNonexistent as TimeNonexistent, npt as npt
from pandas.core import algorithms as algorithms, nanops as nanops, ops as ops
from pandas.core.algorithms import checked_add_with_arr as checked_add_with_arr, isin as isin, unique1d as unique1d
from pandas.core.array_algos import datetimelike_accumulations as datetimelike_accumulations
from pandas.core.arraylike import OpsMixin as OpsMixin
from pandas.core.arrays import DatetimeArray as DatetimeArray, PeriodArray as PeriodArray, TimedeltaArray as TimedeltaArray
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray as NDArrayBackedExtensionArray, ravel_compat as ravel_compat
from pandas.core.arrays.arrow.array import ArrowExtensionArray as ArrowExtensionArray
from pandas.core.arrays.base import ExtensionArray as ExtensionArray
from pandas.core.arrays.integer import IntegerArray as IntegerArray
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike, extract_array as extract_array
from pandas.core.dtypes.common import is_all_strings as is_all_strings, is_categorical_dtype as is_categorical_dtype, is_datetime64_any_dtype as is_datetime64_any_dtype, is_datetime64_dtype as is_datetime64_dtype, is_datetime64tz_dtype as is_datetime64tz_dtype, is_datetime_or_timedelta_dtype as is_datetime_or_timedelta_dtype, is_dtype_equal as is_dtype_equal, is_float_dtype as is_float_dtype, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_object_dtype as is_object_dtype, is_period_dtype as is_period_dtype, is_string_dtype as is_string_dtype, is_timedelta64_dtype as is_timedelta64_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype as DatetimeTZDtype, ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.generic import ABCCategorical as ABCCategorical, ABCMultiIndex as ABCMultiIndex
from pandas.core.dtypes.missing import is_valid_na_for_dtype as is_valid_na_for_dtype, isna as isna
from pandas.core.indexers import check_array_indexer as check_array_indexer, check_setitem_lengths as check_setitem_lengths
from pandas.core.ops.common import unpack_zerodim_and_defer as unpack_zerodim_and_defer
from pandas.core.ops.invalid import invalid_comparison as invalid_comparison, make_invalid_op as make_invalid_op
from pandas.errors import AbstractMethodError as AbstractMethodError, InvalidComparison as InvalidComparison, PerformanceWarning as PerformanceWarning
from pandas.tseries import frequencies as frequencies
from pandas.util._decorators import Appender as Appender, Substitution as Substitution, cache_readonly as cache_readonly
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Any, Iterator, Literal, Sequence, TypeVar, overload

DTScalarOrNaT = DatetimeLikeScalar | NaTType
DatetimeLikeArrayT = TypeVar('DatetimeLikeArrayT', bound='DatetimeLikeArrayMixin')

class DatetimeLikeArrayMixin(OpsMixin, NDArrayBackedExtensionArray):
    """
    Shared Base/Mixin class for DatetimeArray, TimedeltaArray, PeriodArray

    Assumes that __new__/__init__ defines:
        _ndarray

    and that inheriting subclass implements:
        freq
    """
    freq: BaseOffset | None
    def __init__(self, data, dtype: Dtype | None = None, freq: Incomplete | None = None, copy: bool = False) -> None: ...
    def __iter__(self) -> Iterator: ...
    @property
    def asi8(self) -> npt.NDArray[np.int64]:
        """
        Integer representation of the values.

        Returns
        -------
        ndarray
            An ndarray with int64 dtype.
        """
    def __array__(self, dtype: NpDtype | None = None) -> np.ndarray: ...
    @overload
    def __getitem__(self, item: ScalarIndexer) -> DTScalarOrNaT: ...
    @overload
    def __getitem__(self, item: SequenceIndexer | PositionalIndexerTuple) -> DatetimeLikeArrayT: ...
    def __setitem__(self, key: int | Sequence[int] | Sequence[bool] | slice, value: NaTType | Any | Sequence[Any]) -> None: ...
    def astype(self, dtype, copy: bool = True): ...
    @overload
    def view(self) -> DatetimeLikeArrayT: ...
    @overload
    def view(self, dtype: Literal['M8[ns]']) -> DatetimeArray: ...
    @overload
    def view(self, dtype: Literal['m8[ns]']) -> TimedeltaArray: ...
    @overload
    def view(self, dtype: Dtype | None = ...) -> ArrayLike: ...
    def copy(self, order: str = 'C') -> DatetimeLikeArrayT: ...
    def map(self, mapper): ...
    def isin(self, values) -> npt.NDArray[np.bool_]:
        """
        Compute boolean array of whether each value is found in the
        passed set of values.

        Parameters
        ----------
        values : set or sequence of values

        Returns
        -------
        ndarray[bool]
        """
    def isna(self) -> npt.NDArray[np.bool_]: ...
    @property
    def freqstr(self) -> str | None:
        """
        Return the frequency object as a string if its set, otherwise None.
        """
    @property
    def inferred_freq(self) -> str | None:
        """
        Tries to return a string representing a frequency generated by infer_freq.

        Returns None if it can't autodetect the frequency.
        """
    @property
    def resolution(self) -> str:
        """
        Returns day, hour, minute, second, millisecond or microsecond
        """
    __pow__: Incomplete
    __rpow__: Incomplete
    __mul__: Incomplete
    __rmul__: Incomplete
    __truediv__: Incomplete
    __rtruediv__: Incomplete
    __floordiv__: Incomplete
    __rfloordiv__: Incomplete
    __mod__: Incomplete
    __rmod__: Incomplete
    __divmod__: Incomplete
    __rdivmod__: Incomplete
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __iadd__(self, other) -> DatetimeLikeArrayT: ...
    def __isub__(self, other) -> DatetimeLikeArrayT: ...
    def min(self, *, axis: AxisInt | None = None, skipna: bool = True, **kwargs):
        """
        Return the minimum value of the Array or minimum along
        an axis.

        See Also
        --------
        numpy.ndarray.min
        Index.min : Return the minimum value in an Index.
        Series.min : Return the minimum value in a Series.
        """
    def max(self, *, axis: AxisInt | None = None, skipna: bool = True, **kwargs):
        """
        Return the maximum value of the Array or maximum along
        an axis.

        See Also
        --------
        numpy.ndarray.max
        Index.max : Return the maximum value in an Index.
        Series.max : Return the maximum value in a Series.
        """
    def mean(self, *, skipna: bool = True, axis: AxisInt | None = 0):
        """
        Return the mean value of the Array.

        Parameters
        ----------
        skipna : bool, default True
            Whether to ignore any NaT elements.
        axis : int, optional, default 0

        Returns
        -------
        scalar
            Timestamp or Timedelta.

        See Also
        --------
        numpy.ndarray.mean : Returns the average of array elements along a given axis.
        Series.mean : Return the mean value in a Series.

        Notes
        -----
        mean is only defined for Datetime and Timedelta dtypes, not for Period.
        """
    def median(self, *, axis: AxisInt | None = None, skipna: bool = True, **kwargs): ...

class DatelikeOps(DatetimeLikeArrayMixin):
    """
    Common ops for DatetimeIndex/PeriodIndex, but not TimedeltaIndex.
    """
    def strftime(self, date_format: str) -> npt.NDArray[np.object_]:
        '''
        Convert to Index using specified date_format.

        Return an Index of formatted strings specified by date_format, which
        supports the same string format as the python standard library. Details
        of the string format can be found in `python string format
        doc <%(URL)s>`__.

        Formats supported by the C `strftime` API but not by the python string format
        doc (such as `"%%R"`, `"%%r"`) are not officially supported and should be
        preferably replaced with their supported equivalents (such as `"%%H:%%M"`,
        `"%%I:%%M:%%S %%p"`).

        Note that `PeriodIndex` support additional directives, detailed in
        `Period.strftime`.

        Parameters
        ----------
        date_format : str
            Date format string (e.g. "%%Y-%%m-%%d").

        Returns
        -------
        ndarray[object]
            NumPy ndarray of formatted strings.

        See Also
        --------
        to_datetime : Convert the given argument to datetime.
        DatetimeIndex.normalize : Return DatetimeIndex with times to midnight.
        DatetimeIndex.round : Round the DatetimeIndex to the specified freq.
        DatetimeIndex.floor : Floor the DatetimeIndex to the specified freq.
        Timestamp.strftime : Format a single Timestamp.
        Period.strftime : Format a single Period.

        Examples
        --------
        >>> rng = pd.date_range(pd.Timestamp("2018-03-10 09:00"),
        ...                     periods=3, freq=\'s\')
        >>> rng.strftime(\'%%B %%d, %%Y, %%r\')
        Index([\'March 10, 2018, 09:00:00 AM\', \'March 10, 2018, 09:00:01 AM\',
               \'March 10, 2018, 09:00:02 AM\'],
              dtype=\'object\')
        '''
TimelikeOpsT = TypeVar('TimelikeOpsT', bound='TimelikeOps')

class TimelikeOps(DatetimeLikeArrayMixin):
    """
    Common ops for TimedeltaIndex/DatetimeIndex, but not PeriodIndex.
    """
    def __init__(self, values, dtype: Incomplete | None = None, freq=..., copy: bool = False) -> None: ...
    @property
    def freq(self):
        """
        Return the frequency object if it is set, otherwise None.
        """
    @freq.setter
    def freq(self, value) -> None: ...
    def unit(self) -> str: ...
    def as_unit(self, unit: str) -> TimelikeOpsT: ...
    def __array_ufunc__(self, ufunc: np.ufunc, method: str, *inputs, **kwargs): ...
    def round(self, freq, ambiguous: TimeAmbiguous = 'raise', nonexistent: TimeNonexistent = 'raise'): ...
    def floor(self, freq, ambiguous: TimeAmbiguous = 'raise', nonexistent: TimeNonexistent = 'raise'): ...
    def ceil(self, freq, ambiguous: TimeAmbiguous = 'raise', nonexistent: TimeNonexistent = 'raise'): ...
    def any(self, *, axis: AxisInt | None = None, skipna: bool = True) -> bool: ...
    def all(self, *, axis: AxisInt | None = None, skipna: bool = True) -> bool: ...
    def factorize(self, use_na_sentinel: bool = True, sort: bool = False): ...

def ensure_arraylike_for_datetimelike(data, copy: bool, cls_name: str): ...
@overload
def validate_periods(periods: None) -> None: ...
@overload
def validate_periods(periods: int | float) -> int: ...
def validate_inferred_freq(freq, inferred_freq, freq_infer) -> tuple[BaseOffset | None, bool]:
    """
    If the user passes a freq and another freq is inferred from passed data,
    require that they match.

    Parameters
    ----------
    freq : DateOffset or None
    inferred_freq : DateOffset or None
    freq_infer : bool

    Returns
    -------
    freq : DateOffset or None
    freq_infer : bool

    Notes
    -----
    We assume at this point that `maybe_infer_freq` has been called, so
    `freq` is either a DateOffset object or None.
    """
def maybe_infer_freq(freq):
    '''
    Comparing a DateOffset to the string "infer" raises, so we need to
    be careful about comparisons.  Make a dummy variable `freq_infer` to
    signify the case where the given freq is "infer" and set freq to None
    to avoid comparison trouble later on.

    Parameters
    ----------
    freq : {DateOffset, None, str}

    Returns
    -------
    freq : {DateOffset, None}
    freq_infer : bool
        Whether we should inherit the freq of passed data.
    '''
def dtype_to_unit(dtype: DatetimeTZDtype | np.dtype) -> str:
    """
    Return the unit str corresponding to the dtype's resolution.

    Parameters
    ----------
    dtype : DatetimeTZDtype or np.dtype
        If np.dtype, we assume it is a datetime64 dtype.

    Returns
    -------
    str
    """
