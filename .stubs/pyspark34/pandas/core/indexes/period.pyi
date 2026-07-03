import numpy as np
from _typeshed import Incomplete
from pandas._libs.tslibs import BaseOffset as BaseOffset, NaT as NaT, Period as Period, Resolution as Resolution, Tick as Tick
from pandas._typing import Dtype as Dtype, DtypeObj as DtypeObj, npt as npt
from pandas.core.arrays.period import PeriodArray as PeriodArray, period_array as period_array, raise_on_incompatible as raise_on_incompatible, validate_dtype_freq as validate_dtype_freq
from pandas.core.dtypes.common import is_integer as is_integer
from pandas.core.dtypes.dtypes import PeriodDtype as PeriodDtype
from pandas.core.dtypes.generic import ABCSeries as ABCSeries
from pandas.core.dtypes.missing import is_valid_na_for_dtype as is_valid_na_for_dtype
from pandas.core.indexes.base import maybe_extract_name as maybe_extract_name
from pandas.core.indexes.datetimelike import DatetimeIndexOpsMixin as DatetimeIndexOpsMixin
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex, Index as Index
from pandas.core.indexes.extension import inherit_names as inherit_names
from pandas.util._decorators import cache_readonly as cache_readonly, doc as doc
from typing import Hashable

class PeriodIndex(DatetimeIndexOpsMixin):
    """
    Immutable ndarray holding ordinal values indicating regular periods in time.

    Index keys are boxed to Period objects which carries the metadata (eg,
    frequency information).

    Parameters
    ----------
    data : array-like (1d int np.ndarray or PeriodArray), optional
        Optional period-like data to construct index with.
    copy : bool
        Make a copy of input ndarray.
    freq : str or period object, optional
        One of pandas period strings or corresponding objects.
    year : int, array, or Series, default None
    month : int, array, or Series, default None
    quarter : int, array, or Series, default None
    day : int, array, or Series, default None
    hour : int, array, or Series, default None
    minute : int, array, or Series, default None
    second : int, array, or Series, default None
    dtype : str or PeriodDtype, default None

    Attributes
    ----------
    day
    dayofweek
    day_of_week
    dayofyear
    day_of_year
    days_in_month
    daysinmonth
    end_time
    freq
    freqstr
    hour
    is_leap_year
    minute
    month
    quarter
    qyear
    second
    start_time
    week
    weekday
    weekofyear
    year

    Methods
    -------
    asfreq
    strftime
    to_timestamp

    See Also
    --------
    Index : The base pandas Index type.
    Period : Represents a period of time.
    DatetimeIndex : Index with datetime64 data.
    TimedeltaIndex : Index of timedelta64 data.
    period_range : Create a fixed-frequency PeriodIndex.

    Examples
    --------
    >>> idx = pd.PeriodIndex(year=[2000, 2002], quarter=[1, 3])
    >>> idx
    PeriodIndex(['2000Q1', '2002Q3'], dtype='period[Q-DEC]')
    """
    freq: BaseOffset
    dtype: PeriodDtype
    def asfreq(self, freq: Incomplete | None = None, how: str = 'E') -> PeriodIndex: ...
    def to_timestamp(self, freq: Incomplete | None = None, how: str = 'start') -> DatetimeIndex: ...
    @property
    def hour(self) -> Index: ...
    @property
    def minute(self) -> Index: ...
    @property
    def second(self) -> Index: ...
    def __new__(cls, data: Incomplete | None = None, ordinal: Incomplete | None = None, freq: Incomplete | None = None, dtype: Dtype | None = None, copy: bool = False, name: Hashable = None, **fields) -> PeriodIndex: ...
    @property
    def values(self) -> np.ndarray: ...
    def asof_locs(self, where: Index, mask: npt.NDArray[np.bool_]) -> np.ndarray:
        """
        where : array of timestamps
        mask : np.ndarray[bool]
            Array of booleans where data is not NA.
        """
    @property
    def is_full(self) -> bool:
        """
        Returns True if this PeriodIndex is range-like in that all Periods
        between start and end are present, in order.
        """
    @property
    def inferred_type(self) -> str: ...
    def get_loc(self, key):
        """
        Get integer location for requested label.

        Parameters
        ----------
        key : Period, NaT, str, or datetime
            String or datetime key must be parsable as Period.

        Returns
        -------
        loc : int or ndarray[int64]

        Raises
        ------
        KeyError
            Key is not present in the index.
        TypeError
            If key is listlike or otherwise not hashable.
        """
    def shift(self, periods: int = 1, freq: Incomplete | None = None): ...

def period_range(start: Incomplete | None = None, end: Incomplete | None = None, periods: int | None = None, freq: Incomplete | None = None, name: Incomplete | None = None) -> PeriodIndex:
    '''
    Return a fixed frequency PeriodIndex.

    The day (calendar) is the default frequency.

    Parameters
    ----------
    start : str or period-like, default None
        Left bound for generating periods.
    end : str or period-like, default None
        Right bound for generating periods.
    periods : int, default None
        Number of periods to generate.
    freq : str or DateOffset, optional
        Frequency alias. By default the freq is taken from `start` or `end`
        if those are Period objects. Otherwise, the default is ``"D"`` for
        daily frequency.
    name : str, default None
        Name of the resulting PeriodIndex.

    Returns
    -------
    PeriodIndex

    Notes
    -----
    Of the three parameters: ``start``, ``end``, and ``periods``, exactly two
    must be specified.

    To learn more about the frequency strings, please see `this link
    <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases>`__.

    Examples
    --------
    >>> pd.period_range(start=\'2017-01-01\', end=\'2018-01-01\', freq=\'M\')
    PeriodIndex([\'2017-01\', \'2017-02\', \'2017-03\', \'2017-04\', \'2017-05\', \'2017-06\',
             \'2017-07\', \'2017-08\', \'2017-09\', \'2017-10\', \'2017-11\', \'2017-12\',
             \'2018-01\'],
            dtype=\'period[M]\')

    If ``start`` or ``end`` are ``Period`` objects, they will be used as anchor
    endpoints for a ``PeriodIndex`` with frequency matching that of the
    ``period_range`` constructor.

    >>> pd.period_range(start=pd.Period(\'2017Q1\', freq=\'Q\'),
    ...                 end=pd.Period(\'2017Q2\', freq=\'Q\'), freq=\'M\')
    PeriodIndex([\'2017-03\', \'2017-04\', \'2017-05\', \'2017-06\'],
                dtype=\'period[M]\')
    '''
