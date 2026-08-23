import numpy as np
from _typeshed import Incomplete
from datetime import timedelta
from pandas._libs import lib as lib
from pandas._libs.arrays import NDArrayBacked as NDArrayBacked
from pandas._libs.tslibs import BaseOffset as BaseOffset, NaT as NaT, NaTType as NaTType, Timedelta as Timedelta, astype_overflowsafe as astype_overflowsafe, get_unit_from_dtype as get_unit_from_dtype, iNaT as iNaT, parsing as parsing, period as libperiod, to_offset as to_offset
from pandas._libs.tslibs.dtypes import FreqGroup as FreqGroup
from pandas._libs.tslibs.fields import isleapyear_arr as isleapyear_arr
from pandas._libs.tslibs.offsets import Tick as Tick, delta_to_tick as delta_to_tick
from pandas._libs.tslibs.period import DIFFERENT_FREQ as DIFFERENT_FREQ, IncompatibleFrequency as IncompatibleFrequency, Period as Period, get_period_field_arr as get_period_field_arr, period_asfreq_arr as period_asfreq_arr
from pandas._typing import AnyArrayLike as AnyArrayLike, Dtype as Dtype, NpDtype as NpDtype, NumpySorter as NumpySorter, NumpyValueArrayLike as NumpyValueArrayLike, npt as npt
from pandas.core.arrays import DatetimeArray as DatetimeArray, TimedeltaArray as TimedeltaArray, datetimelike as dtl
from pandas.core.arrays.base import ExtensionArray as ExtensionArray
from pandas.core.dtypes.common import ensure_object as ensure_object, is_datetime64_any_dtype as is_datetime64_any_dtype, is_datetime64_dtype as is_datetime64_dtype, is_dtype_equal as is_dtype_equal, is_float_dtype as is_float_dtype, is_integer_dtype as is_integer_dtype, is_period_dtype as is_period_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import PeriodDtype as PeriodDtype
from pandas.core.dtypes.generic import ABCIndex as ABCIndex, ABCPeriodIndex as ABCPeriodIndex, ABCSeries as ABCSeries, ABCTimedeltaArray as ABCTimedeltaArray
from pandas.core.dtypes.missing import isna as isna
from pandas.util._decorators import cache_readonly as cache_readonly, doc as doc
from typing import Literal, Sequence, TypeVar, overload

BaseOffsetT = TypeVar('BaseOffsetT', bound=BaseOffset)

class PeriodArray(dtl.DatelikeOps, libperiod.PeriodMixin):
    '''
    Pandas ExtensionArray for storing Period data.

    Users should use :func:`~pandas.period_array` to create new instances.
    Alternatively, :func:`~pandas.array` can be used to create new instances
    from a sequence of Period scalars.

    Parameters
    ----------
    values : Union[PeriodArray, Series[period], ndarray[int], PeriodIndex]
        The data to store. These should be arrays that can be directly
        converted to ordinals without inference or copy (PeriodArray,
        ndarray[int64]), or a box around such an array (Series[period],
        PeriodIndex).
    dtype : PeriodDtype, optional
        A PeriodDtype instance from which to extract a `freq`. If both
        `freq` and `dtype` are specified, then the frequencies must match.
    freq : str or DateOffset
        The `freq` to use for the array. Mostly applicable when `values`
        is an ndarray of integers, when `freq` is required. When `values`
        is a PeriodArray (or box around), it\'s checked that ``values.freq``
        matches `freq`.
    copy : bool, default False
        Whether to copy the ordinals before storing.

    Attributes
    ----------
    None

    Methods
    -------
    None

    See Also
    --------
    Period: Represents a period of time.
    PeriodIndex : Immutable Index for period data.
    period_range: Create a fixed-frequency PeriodArray.
    array: Construct a pandas array.

    Notes
    -----
    There are two components to a PeriodArray

    - ordinals : integer ndarray
    - freq : pd.tseries.offsets.Offset

    The values are physically stored as a 1-D ndarray of integers. These are
    called "ordinals" and represent some kind of offset from a base.

    The `freq` indicates the span covered by each element of the array.
    All elements in the PeriodArray have the same `freq`.
    '''
    __array_priority__: int
    def __init__(self, values, dtype: Dtype | None = None, freq: Incomplete | None = None, copy: bool = False) -> None: ...
    def dtype(self) -> PeriodDtype: ...
    @property
    def freq(self) -> BaseOffset:
        """
        Return the frequency object for this PeriodArray.
        """
    def __array__(self, dtype: NpDtype | None = None) -> np.ndarray: ...
    def __arrow_array__(self, type: Incomplete | None = None):
        """
        Convert myself into a pyarrow Array.
        """
    year: Incomplete
    month: Incomplete
    day: Incomplete
    hour: Incomplete
    minute: Incomplete
    second: Incomplete
    weekofyear: Incomplete
    week = weekofyear
    day_of_week: Incomplete
    dayofweek = day_of_week
    weekday = dayofweek
    dayofyear: Incomplete
    day_of_year: Incomplete
    quarter: Incomplete
    qyear: Incomplete
    days_in_month: Incomplete
    daysinmonth = days_in_month
    @property
    def is_leap_year(self) -> np.ndarray:
        """
        Logical indicating if the date belongs to a leap year.
        """
    def to_timestamp(self, freq: Incomplete | None = None, how: str = 'start') -> DatetimeArray:
        """
        Cast to DatetimeArray/Index.

        Parameters
        ----------
        freq : str or DateOffset, optional
            Target frequency. The default is 'D' for week or longer,
            'S' otherwise.
        how : {'s', 'e', 'start', 'end'}
            Whether to use the start or end of the time period being converted.

        Returns
        -------
        DatetimeArray/Index
        """
    def asfreq(self, freq: Incomplete | None = None, how: str = 'E') -> PeriodArray:
        """
        Convert the {klass} to the specified frequency `freq`.

        Equivalent to applying :meth:`pandas.Period.asfreq` with the given arguments
        to each :class:`~pandas.Period` in this {klass}.

        Parameters
        ----------
        freq : str
            A frequency.
        how : str {{'E', 'S'}}, default 'E'
            Whether the elements should be aligned to the end
            or start within pa period.

            * 'E', 'END', or 'FINISH' for end,
            * 'S', 'START', or 'BEGIN' for start.

            January 31st ('END') vs. January 1st ('START') for example.

        Returns
        -------
        {klass}
            The transformed {klass} with the new frequency.

        See Also
        --------
        {other}.asfreq: Convert each Period in a {other_name} to the given frequency.
        Period.asfreq : Convert a :class:`~pandas.Period` object to the given frequency.

        Examples
        --------
        >>> pidx = pd.period_range('2010-01-01', '2015-01-01', freq='A')
        >>> pidx
        PeriodIndex(['2010', '2011', '2012', '2013', '2014', '2015'],
        dtype='period[A-DEC]')

        >>> pidx.asfreq('M')
        PeriodIndex(['2010-12', '2011-12', '2012-12', '2013-12', '2014-12',
        '2015-12'], dtype='period[M]')

        >>> pidx.asfreq('M', how='S')
        PeriodIndex(['2010-01', '2011-01', '2012-01', '2013-01', '2014-01',
        '2015-01'], dtype='period[M]')
        """
    def astype(self, dtype, copy: bool = True): ...
    def searchsorted(self, value: NumpyValueArrayLike | ExtensionArray, side: Literal['left', 'right'] = 'left', sorter: NumpySorter = None) -> npt.NDArray[np.intp] | np.intp: ...
    def fillna(self, value: Incomplete | None = None, method: Incomplete | None = None, limit: Incomplete | None = None) -> PeriodArray: ...

def raise_on_incompatible(left, right):
    """
    Helper function to render a consistent error message when raising
    IncompatibleFrequency.

    Parameters
    ----------
    left : PeriodArray
    right : None, DateOffset, Period, ndarray, or timedelta-like

    Returns
    -------
    IncompatibleFrequency
        Exception to be raised by the caller.
    """
def period_array(data: Sequence[Period | str | None] | AnyArrayLike, freq: str | Tick | None = None, copy: bool = False) -> PeriodArray:
    """
    Construct a new PeriodArray from a sequence of Period scalars.

    Parameters
    ----------
    data : Sequence of Period objects
        A sequence of Period objects. These are required to all have
        the same ``freq.`` Missing values can be indicated by ``None``
        or ``pandas.NaT``.
    freq : str, Tick, or Offset
        The frequency of every element of the array. This can be specified
        to avoid inferring the `freq` from `data`.
    copy : bool, default False
        Whether to ensure a copy of the data is made.

    Returns
    -------
    PeriodArray

    See Also
    --------
    PeriodArray
    pandas.PeriodIndex

    Examples
    --------
    >>> period_array([pd.Period('2017', freq='A'),
    ...               pd.Period('2018', freq='A')])
    <PeriodArray>
    ['2017', '2018']
    Length: 2, dtype: period[A-DEC]

    >>> period_array([pd.Period('2017', freq='A'),
    ...               pd.Period('2018', freq='A'),
    ...               pd.NaT])
    <PeriodArray>
    ['2017', '2018', 'NaT']
    Length: 3, dtype: period[A-DEC]

    Integers that look like years are handled

    >>> period_array([2000, 2001, 2002], freq='D')
    <PeriodArray>
    ['2000-01-01', '2001-01-01', '2002-01-01']
    Length: 3, dtype: period[D]

    Datetime-like strings may also be passed

    >>> period_array(['2000-Q1', '2000-Q2', '2000-Q3', '2000-Q4'], freq='Q')
    <PeriodArray>
    ['2000Q1', '2000Q2', '2000Q3', '2000Q4']
    Length: 4, dtype: period[Q-DEC]
    """
@overload
def validate_dtype_freq(dtype, freq: BaseOffsetT) -> BaseOffsetT: ...
@overload
def validate_dtype_freq(dtype, freq: timedelta | str | None) -> BaseOffset: ...
def dt64arr_to_periodarr(data, freq, tz: Incomplete | None = None) -> tuple[npt.NDArray[np.int64], BaseOffset]:
    """
    Convert an datetime-like array to values Period ordinals.

    Parameters
    ----------
    data : Union[Series[datetime64[ns]], DatetimeIndex, ndarray[datetime64ns]]
    freq : Optional[Union[str, Tick]]
        Must match the `freq` on the `data` if `data` is a DatetimeIndex
        or Series.
    tz : Optional[tzinfo]

    Returns
    -------
    ordinals : ndarray[int64]
    freq : Tick
        The frequency extracted from the Series or DatetimeIndex if that's
        used.

    """
