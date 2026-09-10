import datetime as dt
import numpy as np
from _typeshed import Incomplete
from pandas._libs import NaT as NaT, Period as Period, Timestamp as Timestamp, lib as lib
from pandas._libs.tslibs import Resolution as Resolution, periods_per_day as periods_per_day, timezones as timezones, to_offset as to_offset
from pandas._libs.tslibs.offsets import prefix_mapping as prefix_mapping
from pandas._typing import Dtype as Dtype, DtypeObj as DtypeObj, Frequency as Frequency, IntervalClosedType as IntervalClosedType, TimeAmbiguous as TimeAmbiguous, TimeNonexistent as TimeNonexistent, npt as npt
from pandas.core.api import DataFrame as DataFrame, PeriodIndex as PeriodIndex
from pandas.core.arrays.datetimes import DatetimeArray as DatetimeArray, tz_to_dtype as tz_to_dtype
from pandas.core.dtypes.common import is_datetime64_dtype as is_datetime64_dtype, is_datetime64tz_dtype as is_datetime64tz_dtype, is_scalar as is_scalar
from pandas.core.dtypes.generic import ABCSeries as ABCSeries
from pandas.core.dtypes.missing import is_valid_na_for_dtype as is_valid_na_for_dtype
from pandas.core.indexes.base import Index as Index, maybe_extract_name as maybe_extract_name
from pandas.core.indexes.datetimelike import DatetimeTimedeltaMixin as DatetimeTimedeltaMixin
from pandas.core.indexes.extension import inherit_names as inherit_names
from pandas.core.tools.times import to_time as to_time
from pandas.util._decorators import cache_readonly as cache_readonly, doc as doc
from typing import Hashable

class DatetimeIndex(DatetimeTimedeltaMixin):
    """
    Immutable ndarray-like of datetime64 data.

    Represented internally as int64, and which can be boxed to Timestamp objects
    that are subclasses of datetime and carry metadata.

    .. versionchanged:: 2.0.0
        The various numeric date/time attributes (:attr:`~DatetimeIndex.day`,
        :attr:`~DatetimeIndex.month`, :attr:`~DatetimeIndex.year` etc.) now have dtype
        ``int32``. Previously they had dtype ``int64``.

    Parameters
    ----------
    data : array-like (1-dimensional)
        Datetime-like data to construct index with.
    freq : str or pandas offset object, optional
        One of pandas date offset strings or corresponding objects. The string
        'infer' can be passed in order to set the frequency of the index as the
        inferred frequency upon creation.
    tz : pytz.timezone or dateutil.tz.tzfile or datetime.tzinfo or str
        Set the Timezone of the data.
    normalize : bool, default False
        Normalize start/end dates to midnight before generating date range.
    closed : {'left', 'right'}, optional
        Set whether to include `start` and `end` that are on the
        boundary. The default includes boundary points on either end.
    ambiguous : 'infer', bool-ndarray, 'NaT', default 'raise'
        When clocks moved backward due to DST, ambiguous times may arise.
        For example in Central European Time (UTC+01), when going from 03:00
        DST to 02:00 non-DST, 02:30:00 local time occurs both at 00:30:00 UTC
        and at 01:30:00 UTC. In such a situation, the `ambiguous` parameter
        dictates how ambiguous times should be handled.

        - 'infer' will attempt to infer fall dst-transition hours based on
          order
        - bool-ndarray where True signifies a DST time, False signifies a
          non-DST time (note that this flag is only applicable for ambiguous
          times)
        - 'NaT' will return NaT where there are ambiguous times
        - 'raise' will raise an AmbiguousTimeError if there are ambiguous times.
    dayfirst : bool, default False
        If True, parse dates in `data` with the day first order.
    yearfirst : bool, default False
        If True parse dates in `data` with the year first order.
    dtype : numpy.dtype or DatetimeTZDtype or str, default None
        Note that the only NumPy dtype allowed is ‘datetime64[ns]’.
    copy : bool, default False
        Make a copy of input ndarray.
    name : label, default None
        Name to be stored in the index.

    Attributes
    ----------
    year
    month
    day
    hour
    minute
    second
    microsecond
    nanosecond
    date
    time
    timetz
    dayofyear
    day_of_year
    weekofyear
    week
    dayofweek
    day_of_week
    weekday
    quarter
    tz
    freq
    freqstr
    is_month_start
    is_month_end
    is_quarter_start
    is_quarter_end
    is_year_start
    is_year_end
    is_leap_year
    inferred_freq

    Methods
    -------
    normalize
    strftime
    snap
    tz_convert
    tz_localize
    round
    floor
    ceil
    to_period
    to_pydatetime
    to_series
    to_frame
    month_name
    day_name
    mean
    std

    See Also
    --------
    Index : The base pandas Index type.
    TimedeltaIndex : Index of timedelta64 data.
    PeriodIndex : Index of Period data.
    to_datetime : Convert argument to datetime.
    date_range : Create a fixed-frequency DatetimeIndex.

    Notes
    -----
    To learn more about the frequency strings, please see `this link
    <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases>`__.
    """
    tz: dt.tzinfo | None
    def strftime(self, date_format) -> Index: ...
    def tz_convert(self, tz) -> DatetimeIndex: ...
    def tz_localize(self, tz, ambiguous: TimeAmbiguous = 'raise', nonexistent: TimeNonexistent = 'raise') -> DatetimeIndex: ...
    def to_period(self, freq: Incomplete | None = None) -> PeriodIndex: ...
    def to_julian_date(self) -> Index: ...
    def isocalendar(self) -> DataFrame: ...
    def __new__(cls, data: Incomplete | None = None, freq: Frequency | lib.NoDefault = ..., tz=..., normalize: bool = False, closed: Incomplete | None = None, ambiguous: TimeAmbiguous = 'raise', dayfirst: bool = False, yearfirst: bool = False, dtype: Dtype | None = None, copy: bool = False, name: Hashable = None) -> DatetimeIndex: ...
    def __reduce__(self): ...
    def snap(self, freq: Frequency = 'S') -> DatetimeIndex:
        """
        Snap time stamps to nearest occurring frequency.

        Returns
        -------
        DatetimeIndex
        """
    def get_loc(self, key):
        """
        Get integer location for requested label

        Returns
        -------
        loc : int
        """
    def slice_indexer(self, start: Incomplete | None = None, end: Incomplete | None = None, step: Incomplete | None = None):
        """
        Return indexer for specified label slice.
        Index.slice_indexer, customized to handle time slicing.

        In addition to functionality provided by Index.slice_indexer, does the
        following:

        - if both `start` and `end` are instances of `datetime.time`, it
          invokes `indexer_between_time`
        - if `start` and `end` are both either string or None perform
          value-based selection in non-monotonic cases.

        """
    @property
    def inferred_type(self) -> str: ...
    def indexer_at_time(self, time, asof: bool = False) -> npt.NDArray[np.intp]:
        '''
        Return index locations of values at particular time of day.

        Parameters
        ----------
        time : datetime.time or str
            Time passed in either as object (datetime.time) or as string in
            appropriate format ("%H:%M", "%H%M", "%I:%M%p", "%I%M%p",
            "%H:%M:%S", "%H%M%S", "%I:%M:%S%p", "%I%M%S%p").

        Returns
        -------
        np.ndarray[np.intp]

        See Also
        --------
        indexer_between_time : Get index locations of values between particular
            times of day.
        DataFrame.at_time : Select values at particular time of day.
        '''
    def indexer_between_time(self, start_time, end_time, include_start: bool = True, include_end: bool = True) -> npt.NDArray[np.intp]:
        '''
        Return index locations of values between particular times of day.

        Parameters
        ----------
        start_time, end_time : datetime.time, str
            Time passed either as object (datetime.time) or as string in
            appropriate format ("%H:%M", "%H%M", "%I:%M%p", "%I%M%p",
            "%H:%M:%S", "%H%M%S", "%I:%M:%S%p","%I%M%S%p").
        include_start : bool, default True
        include_end : bool, default True

        Returns
        -------
        np.ndarray[np.intp]

        See Also
        --------
        indexer_at_time : Get index locations of values at particular time of day.
        DataFrame.between_time : Select values between particular times of day.
        '''

def date_range(start: Incomplete | None = None, end: Incomplete | None = None, periods: Incomplete | None = None, freq: Incomplete | None = None, tz: Incomplete | None = None, normalize: bool = False, name: Hashable = None, inclusive: IntervalClosedType = 'both', *, unit: str | None = None, **kwargs) -> DatetimeIndex:
    '''
    Return a fixed frequency DatetimeIndex.

    Returns the range of equally spaced time points (where the difference between any
    two adjacent points is specified by the given frequency) such that they all
    satisfy `start <[=] x <[=] end`, where the first one and the last one are, resp.,
    the first and last time points in that range that fall on the boundary of ``freq``
    (if given as a frequency string) or that are valid for ``freq`` (if given as a
    :class:`pandas.tseries.offsets.DateOffset`). (If exactly one of ``start``,
    ``end``, or ``freq`` is *not* specified, this missing parameter can be computed
    given ``periods``, the number of timesteps in the range. See the note below.)

    Parameters
    ----------
    start : str or datetime-like, optional
        Left bound for generating dates.
    end : str or datetime-like, optional
        Right bound for generating dates.
    periods : int, optional
        Number of periods to generate.
    freq : str, datetime.timedelta, or DateOffset, default \'D\'
        Frequency strings can have multiples, e.g. \'5H\'. See
        :ref:`here <timeseries.offset_aliases>` for a list of
        frequency aliases.
    tz : str or tzinfo, optional
        Time zone name for returning localized DatetimeIndex, for example
        \'Asia/Hong_Kong\'. By default, the resulting DatetimeIndex is
        timezone-naive unless timezone-aware datetime-likes are passed.
    normalize : bool, default False
        Normalize start/end dates to midnight before generating date range.
    name : str, default None
        Name of the resulting DatetimeIndex.
    inclusive : {"both", "neither", "left", "right"}, default "both"
        Include boundaries; Whether to set each bound as closed or open.

        .. versionadded:: 1.4.0
    unit : str, default None
        Specify the desired resolution of the result.

        .. versionadded:: 2.0.0
    **kwargs
        For compatibility. Has no effect on the result.

    Returns
    -------
    DatetimeIndex

    See Also
    --------
    DatetimeIndex : An immutable container for datetimes.
    timedelta_range : Return a fixed frequency TimedeltaIndex.
    period_range : Return a fixed frequency PeriodIndex.
    interval_range : Return a fixed frequency IntervalIndex.

    Notes
    -----
    Of the four parameters ``start``, ``end``, ``periods``, and ``freq``,
    exactly three must be specified. If ``freq`` is omitted, the resulting
    ``DatetimeIndex`` will have ``periods`` linearly spaced elements between
    ``start`` and ``end`` (closed on both sides).

    To learn more about the frequency strings, please see `this link
    <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases>`__.

    Examples
    --------
    **Specifying the values**

    The next four examples generate the same `DatetimeIndex`, but vary
    the combination of `start`, `end` and `periods`.

    Specify `start` and `end`, with the default daily frequency.

    >>> pd.date_range(start=\'1/1/2018\', end=\'1/08/2018\')
    DatetimeIndex([\'2018-01-01\', \'2018-01-02\', \'2018-01-03\', \'2018-01-04\',
                   \'2018-01-05\', \'2018-01-06\', \'2018-01-07\', \'2018-01-08\'],
                  dtype=\'datetime64[ns]\', freq=\'D\')

    Specify timezone-aware `start` and `end`, with the default daily frequency.

    >>> pd.date_range(
    ...     start=pd.to_datetime("1/1/2018").tz_localize("Europe/Berlin"),
    ...     end=pd.to_datetime("1/08/2018").tz_localize("Europe/Berlin"),
    ... )
    DatetimeIndex([\'2018-01-01 00:00:00+01:00\', \'2018-01-02 00:00:00+01:00\',
                   \'2018-01-03 00:00:00+01:00\', \'2018-01-04 00:00:00+01:00\',
                   \'2018-01-05 00:00:00+01:00\', \'2018-01-06 00:00:00+01:00\',
                   \'2018-01-07 00:00:00+01:00\', \'2018-01-08 00:00:00+01:00\'],
                  dtype=\'datetime64[ns, Europe/Berlin]\', freq=\'D\')

    Specify `start` and `periods`, the number of periods (days).

    >>> pd.date_range(start=\'1/1/2018\', periods=8)
    DatetimeIndex([\'2018-01-01\', \'2018-01-02\', \'2018-01-03\', \'2018-01-04\',
                   \'2018-01-05\', \'2018-01-06\', \'2018-01-07\', \'2018-01-08\'],
                  dtype=\'datetime64[ns]\', freq=\'D\')

    Specify `end` and `periods`, the number of periods (days).

    >>> pd.date_range(end=\'1/1/2018\', periods=8)
    DatetimeIndex([\'2017-12-25\', \'2017-12-26\', \'2017-12-27\', \'2017-12-28\',
                   \'2017-12-29\', \'2017-12-30\', \'2017-12-31\', \'2018-01-01\'],
                  dtype=\'datetime64[ns]\', freq=\'D\')

    Specify `start`, `end`, and `periods`; the frequency is generated
    automatically (linearly spaced).

    >>> pd.date_range(start=\'2018-04-24\', end=\'2018-04-27\', periods=3)
    DatetimeIndex([\'2018-04-24 00:00:00\', \'2018-04-25 12:00:00\',
                   \'2018-04-27 00:00:00\'],
                  dtype=\'datetime64[ns]\', freq=None)

    **Other Parameters**

    Changed the `freq` (frequency) to ``\'M\'`` (month end frequency).

    >>> pd.date_range(start=\'1/1/2018\', periods=5, freq=\'M\')
    DatetimeIndex([\'2018-01-31\', \'2018-02-28\', \'2018-03-31\', \'2018-04-30\',
                   \'2018-05-31\'],
                  dtype=\'datetime64[ns]\', freq=\'M\')

    Multiples are allowed

    >>> pd.date_range(start=\'1/1/2018\', periods=5, freq=\'3M\')
    DatetimeIndex([\'2018-01-31\', \'2018-04-30\', \'2018-07-31\', \'2018-10-31\',
                   \'2019-01-31\'],
                  dtype=\'datetime64[ns]\', freq=\'3M\')

    `freq` can also be specified as an Offset object.

    >>> pd.date_range(start=\'1/1/2018\', periods=5, freq=pd.offsets.MonthEnd(3))
    DatetimeIndex([\'2018-01-31\', \'2018-04-30\', \'2018-07-31\', \'2018-10-31\',
                   \'2019-01-31\'],
                  dtype=\'datetime64[ns]\', freq=\'3M\')

    Specify `tz` to set the timezone.

    >>> pd.date_range(start=\'1/1/2018\', periods=5, tz=\'Asia/Tokyo\')
    DatetimeIndex([\'2018-01-01 00:00:00+09:00\', \'2018-01-02 00:00:00+09:00\',
                   \'2018-01-03 00:00:00+09:00\', \'2018-01-04 00:00:00+09:00\',
                   \'2018-01-05 00:00:00+09:00\'],
                  dtype=\'datetime64[ns, Asia/Tokyo]\', freq=\'D\')

    `inclusive` controls whether to include `start` and `end` that are on the
    boundary. The default, "both", includes boundary points on either end.

    >>> pd.date_range(start=\'2017-01-01\', end=\'2017-01-04\', inclusive="both")
    DatetimeIndex([\'2017-01-01\', \'2017-01-02\', \'2017-01-03\', \'2017-01-04\'],
                  dtype=\'datetime64[ns]\', freq=\'D\')

    Use ``inclusive=\'left\'`` to exclude `end` if it falls on the boundary.

    >>> pd.date_range(start=\'2017-01-01\', end=\'2017-01-04\', inclusive=\'left\')
    DatetimeIndex([\'2017-01-01\', \'2017-01-02\', \'2017-01-03\'],
                  dtype=\'datetime64[ns]\', freq=\'D\')

    Use ``inclusive=\'right\'`` to exclude `start` if it falls on the boundary, and
    similarly ``inclusive=\'neither\'`` will exclude both `start` and `end`.

    >>> pd.date_range(start=\'2017-01-01\', end=\'2017-01-04\', inclusive=\'right\')
    DatetimeIndex([\'2017-01-02\', \'2017-01-03\', \'2017-01-04\'],
                  dtype=\'datetime64[ns]\', freq=\'D\')

    **Specify a unit**

    >>> pd.date_range(start="2017-01-01", periods=10, freq="100AS", unit="s")
    DatetimeIndex([\'2017-01-01\', \'2117-01-01\', \'2217-01-01\', \'2317-01-01\',
                   \'2417-01-01\', \'2517-01-01\', \'2617-01-01\', \'2717-01-01\',
                   \'2817-01-01\', \'2917-01-01\'],
                  dtype=\'datetime64[s]\', freq=\'100AS-JAN\')
    '''
def bdate_range(start: Incomplete | None = None, end: Incomplete | None = None, periods: int | None = None, freq: Frequency = 'B', tz: Incomplete | None = None, normalize: bool = True, name: Hashable = None, weekmask: Incomplete | None = None, holidays: Incomplete | None = None, inclusive: IntervalClosedType = 'both', **kwargs) -> DatetimeIndex:
    '''
    Return a fixed frequency DatetimeIndex with business day as the default.

    Parameters
    ----------
    start : str or datetime-like, default None
        Left bound for generating dates.
    end : str or datetime-like, default None
        Right bound for generating dates.
    periods : int, default None
        Number of periods to generate.
    freq : str, Timedelta, datetime.timedelta, or DateOffset, default \'B\'
        Frequency strings can have multiples, e.g. \'5H\'. The default is
        business daily (\'B\').
    tz : str or None
        Time zone name for returning localized DatetimeIndex, for example
        Asia/Beijing.
    normalize : bool, default False
        Normalize start/end dates to midnight before generating date range.
    name : str, default None
        Name of the resulting DatetimeIndex.
    weekmask : str or None, default None
        Weekmask of valid business days, passed to ``numpy.busdaycalendar``,
        only used when custom frequency strings are passed.  The default
        value None is equivalent to \'Mon Tue Wed Thu Fri\'.
    holidays : list-like or None, default None
        Dates to exclude from the set of valid business days, passed to
        ``numpy.busdaycalendar``, only used when custom frequency strings
        are passed.
    inclusive : {"both", "neither", "left", "right"}, default "both"
        Include boundaries; Whether to set each bound as closed or open.

        .. versionadded:: 1.4.0
    **kwargs
        For compatibility. Has no effect on the result.

    Returns
    -------
    DatetimeIndex

    Notes
    -----
    Of the four parameters: ``start``, ``end``, ``periods``, and ``freq``,
    exactly three must be specified.  Specifying ``freq`` is a requirement
    for ``bdate_range``.  Use ``date_range`` if specifying ``freq`` is not
    desired.

    To learn more about the frequency strings, please see `this link
    <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases>`__.

    Examples
    --------
    Note how the two weekend days are skipped in the result.

    >>> pd.bdate_range(start=\'1/1/2018\', end=\'1/08/2018\')
    DatetimeIndex([\'2018-01-01\', \'2018-01-02\', \'2018-01-03\', \'2018-01-04\',
               \'2018-01-05\', \'2018-01-08\'],
              dtype=\'datetime64[ns]\', freq=\'B\')
    '''
