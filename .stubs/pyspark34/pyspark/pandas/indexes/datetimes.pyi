import datetime
from _typeshed import Incomplete
from pandas.tseries.offsets import DateOffset
from pyspark.pandas.indexes.base import Index as Index
from pyspark.pandas.missing.indexes import MissingPandasLikeDatetimeIndex as MissingPandasLikeDatetimeIndex
from pyspark.pandas.series import Series as Series, first_series as first_series
from pyspark.pandas.utils import verify_temp_column_name as verify_temp_column_name
from typing import Any

class DatetimeIndex(Index):
    """
    Immutable ndarray-like of datetime64 data.

    Parameters
    ----------
    data : array-like (1-dimensional), optional
        Optional datetime-like data to construct index with.
    freq : str or pandas offset object, optional
        One of pandas date offset strings or corresponding objects. The string
        'infer' can be passed in order to set the frequency of the index as the
        inferred frequency upon creation.
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
    dtype : numpy.dtype or str, default None
        Note that the only NumPy dtype allowed is ‘datetime64[ns]’.
    copy : bool, default False
        Make a copy of input ndarray.
    name : label, default None
        Name to be stored in the index.

    See Also
    --------
    Index : The base pandas Index type.
    to_datetime : Convert argument to datetime.

    Examples
    --------
    >>> ps.DatetimeIndex(['1970-01-01', '1970-01-01', '1970-01-01'])
    DatetimeIndex(['1970-01-01', '1970-01-01', '1970-01-01'], dtype='datetime64[ns]', freq=None)

    From a Series:

    >>> from datetime import datetime
    >>> s = ps.Series([datetime(2021, 3, 1), datetime(2021, 3, 2)], index=[10, 20])
    >>> ps.DatetimeIndex(s)
    DatetimeIndex(['2021-03-01', '2021-03-02'], dtype='datetime64[ns]', freq=None)

    From an Index:

    >>> idx = ps.DatetimeIndex(['1970-01-01', '1970-01-01', '1970-01-01'])
    >>> ps.DatetimeIndex(idx)
    DatetimeIndex(['1970-01-01', '1970-01-01', '1970-01-01'], dtype='datetime64[ns]', freq=None)
    """
    def __new__(cls, data: Incomplete | None = None, freq=..., normalize: bool = False, closed: Incomplete | None = None, ambiguous: str = 'raise', dayfirst: bool = False, yearfirst: bool = False, dtype: Incomplete | None = None, copy: bool = False, name: Incomplete | None = None): ...
    def __getattr__(self, item: str) -> Any: ...
    @property
    def year(self) -> Index:
        """
        The year of the datetime.
        """
    @property
    def month(self) -> Index:
        """
        The month of the timestamp as January = 1 December = 12.
        """
    @property
    def day(self) -> Index:
        """
        The days of the datetime.
        """
    @property
    def hour(self) -> Index:
        """
        The hours of the datetime.
        """
    @property
    def minute(self) -> Index:
        """
        The minutes of the datetime.
        """
    @property
    def second(self) -> Index:
        """
        The seconds of the datetime.
        """
    @property
    def microsecond(self) -> Index:
        """
        The microseconds of the datetime.
        """
    @property
    def week(self) -> Index:
        """
        The week ordinal of the year.
        """
    @property
    def weekofyear(self) -> Index: ...
    @property
    def dayofweek(self) -> Index:
        """
        The day of the week with Monday=0, Sunday=6.
        Return the day of the week. It is assumed the week starts on
        Monday, which is denoted by 0 and ends on Sunday which is denoted
        by 6. This method is available on both Series with datetime
        values (using the `dt` accessor) or DatetimeIndex.

        Returns
        -------
        Series or Index
            Containing integers indicating the day number.

        See Also
        --------
        Series.dt.dayofweek : Alias.
        Series.dt.weekday : Alias.
        Series.dt.day_name : Returns the name of the day of the week.

        Examples
        --------
        >>> idx = ps.date_range('2016-12-31', '2017-01-08', freq='D')
        >>> idx.dayofweek
        Int64Index([5, 6, 0, 1, 2, 3, 4, 5, 6], dtype='int64')
        """
    @property
    def day_of_week(self) -> Index: ...
    @property
    def weekday(self) -> Index: ...
    @property
    def dayofyear(self) -> Index:
        """
        The ordinal day of the year.
        """
    @property
    def day_of_year(self) -> Index: ...
    @property
    def quarter(self) -> Index:
        """
        The quarter of the date.
        """
    @property
    def is_month_start(self) -> Index:
        '''
        Indicates whether the date is the first day of the month.

        Returns
        -------
        Index
            Returns a Index with boolean values

        See Also
        --------
        is_month_end : Return a boolean indicating whether the date
            is the last day of the month.

        Examples
        --------
        >>> idx = ps.date_range("2018-02-27", periods=3)
        >>> idx.is_month_start  # doctest: +SKIP
        Index([False, False, True], dtype=\'bool\')
        '''
    @property
    def is_month_end(self) -> Index:
        '''
        Indicates whether the date is the last day of the month.

        Returns
        -------
        Index
            Returns an Index with boolean values.

        See Also
        --------
        is_month_start : Return a boolean indicating whether the date
            is the first day of the month.

        Examples
        --------
        >>> idx = ps.date_range("2018-02-27", periods=3)
        >>> idx.is_month_end  # doctest: +SKIP
        Index([False, True, False], dtype=\'bool\')
        '''
    @property
    def is_quarter_start(self) -> Index:
        """
        Indicator for whether the date is the first day of a quarter.

        Returns
        -------
        is_quarter_start : Index
            Returns an Index with boolean values.

        See Also
        --------
        quarter : Return the quarter of the date.
        is_quarter_end : Similar property for indicating the quarter start.

        Examples
        --------
        >>> idx = ps.date_range('2017-03-30', periods=4)
        >>> idx.is_quarter_start  # doctest: +SKIP
        Index([False, False, True, False], dtype='bool')
        """
    @property
    def is_quarter_end(self) -> Index:
        """
        Indicator for whether the date is the last day of a quarter.

        Returns
        -------
        is_quarter_end : Index
            Returns an Index with boolean values.

        See Also
        --------
        quarter : Return the quarter of the date.
        is_quarter_start : Similar property indicating the quarter start.

        Examples
        --------
        >>> idx = ps.date_range('2017-03-30', periods=4)
        >>> idx.is_quarter_end  # doctest: +SKIP
        Index([False, True, False, False], dtype='bool')
        """
    @property
    def is_year_start(self) -> Index:
        '''
        Indicate whether the date is the first day of a year.

        Returns
        -------
        Index
            Returns an Index with boolean values.

        See Also
        --------
        is_year_end : Similar property indicating the last day of the year.

        Examples
        --------
        >>> idx = ps.date_range("2017-12-30", periods=3)
        >>> idx.is_year_start  # doctest: +SKIP
        Index([False, False, True], dtype=\'bool\')
        '''
    @property
    def is_year_end(self) -> Index:
        '''
        Indicate whether the date is the last day of the year.

        Returns
        -------
        Index
            Returns an Index with boolean values.

        See Also
        --------
        is_year_start : Similar property indicating the start of the year.

        Examples
        --------
        >>> idx = ps.date_range("2017-12-30", periods=3)
        >>> idx.is_year_end  # doctest: +SKIP
        Index([False, True, False], dtype=\'bool\')
        '''
    @property
    def is_leap_year(self) -> Index:
        '''
        Boolean indicator if the date belongs to a leap year.

        A leap year is a year, which has 366 days (instead of 365) including
        29th of February as an intercalary day.
        Leap years are years which are multiples of four with the exception
        of years divisible by 100 but not by 400.

        Returns
        -------
        Index
             Booleans indicating if dates belong to a leap year.

        Examples
        --------
        >>> idx = ps.date_range("2012-01-01", "2015-01-01", freq="Y")
        >>> idx.is_leap_year  # doctest: +SKIP
        Index([True, False, False], dtype=\'bool\')
        '''
    @property
    def daysinmonth(self) -> Index:
        """
        The number of days in the month.
        """
    @property
    def days_in_month(self) -> Index: ...
    def ceil(self, freq: str | DateOffset, *args: Any, **kwargs: Any) -> DatetimeIndex:
        """
        Perform ceil operation on the data to the specified freq.

        Parameters
        ----------
        freq : str or Offset
            The frequency level to ceil the index to. Must be a fixed
            frequency like 'S' (second) not 'ME' (month end).

        Returns
        -------
        DatetimeIndex

        Raises
        ------
        ValueError if the `freq` cannot be converted.

        Examples
        --------
        >>> rng = ps.date_range('1/1/2018 11:59:00', periods=3, freq='min')
        >>> rng.ceil('H')  # doctest: +NORMALIZE_WHITESPACE
        DatetimeIndex(['2018-01-01 12:00:00', '2018-01-01 12:00:00',
                       '2018-01-01 13:00:00'],
                      dtype='datetime64[ns]', freq=None)
        """
    def floor(self, freq: str | DateOffset, *args: Any, **kwargs: Any) -> DatetimeIndex:
        '''
        Perform floor operation on the data to the specified freq.

        Parameters
        ----------
        freq : str or Offset
            The frequency level to floor the index to. Must be a fixed
            frequency like \'S\' (second) not \'ME\' (month end).

        Returns
        -------
        DatetimeIndex

        Raises
        ------
        ValueError if the `freq` cannot be converted.

        Examples
        --------
        >>> rng = ps.date_range(\'1/1/2018 11:59:00\', periods=3, freq=\'min\')
        >>> rng.floor("H")  # doctest: +NORMALIZE_WHITESPACE
        DatetimeIndex([\'2018-01-01 11:00:00\', \'2018-01-01 12:00:00\',
                       \'2018-01-01 12:00:00\'],
                      dtype=\'datetime64[ns]\', freq=None)
        '''
    def round(self, freq: str | DateOffset, *args: Any, **kwargs: Any) -> DatetimeIndex:
        '''
        Perform round operation on the data to the specified freq.

        Parameters
        ----------
        freq : str or Offset
            The frequency level to round the index to. Must be a fixed
            frequency like \'S\' (second) not \'ME\' (month end).

        Returns
        -------
        DatetimeIndex

        Raises
        ------
        ValueError if the `freq` cannot be converted.

        Examples
        --------
        >>> rng = ps.date_range(\'1/1/2018 11:59:00\', periods=3, freq=\'min\')
        >>> rng.round("H")  # doctest: +NORMALIZE_WHITESPACE
        DatetimeIndex([\'2018-01-01 12:00:00\', \'2018-01-01 12:00:00\',
                       \'2018-01-01 12:00:00\'],
                      dtype=\'datetime64[ns]\', freq=None)
        '''
    def month_name(self, locale: str | None = None) -> Index:
        """
        Return the month names of the DatetimeIndex with specified locale.

        Parameters
        ----------
        locale : str, optional
            Locale determining the language in which to return the month name.
            Default is English locale.

        Returns
        -------
        Index
            Index of month names.

        Examples
        --------
        >>> idx = ps.date_range(start='2018-01', freq='M', periods=3)
        >>> idx.month_name()
        Index(['January', 'February', 'March'], dtype='object')
        """
    def day_name(self, locale: str | None = None) -> Index:
        """
        Return the day names of the series with specified locale.

        Parameters
        ----------
        locale : str, optional
            Locale determining the language in which to return the day name.
            Default is English locale.

        Returns
        -------
        Index
            Index of day names.

        Examples
        --------
        >>> idx = ps.date_range(start='2018-01-01', freq='D', periods=3)
        >>> idx.day_name()
        Index(['Monday', 'Tuesday', 'Wednesday'], dtype='object')
        """
    def normalize(self) -> DatetimeIndex:
        """
        Convert times to midnight.

        The time component of the date-time is converted to midnight i.e.
        00:00:00. This is useful in cases, when the time does not matter.
        Length is unaltered. The time zones are unaffected.

        This method is available on Series with datetime values under
        the ``.dt`` accessor.

        Returns
        -------
        DatetimeIndex
            The same type as the original data.

        See Also
        --------
        floor : Floor the series to the specified freq.
        ceil : Ceil the series to the specified freq.
        round : Round the series to the specified freq.

        Examples
        --------
        >>> idx = ps.date_range(start='2014-08-01 10:00', freq='H', periods=3)
        >>> idx.normalize()
        DatetimeIndex(['2014-08-01', '2014-08-01', '2014-08-01'], dtype='datetime64[ns]', freq=None)
        """
    def strftime(self, date_format: str) -> Index:
        '''
        Convert to a string Index using specified date_format.

        Return an Index of formatted strings specified by date_format, which
        supports the same string format as the python standard library. Details
        of the string format can be found in the python string format
        doc.

        Parameters
        ----------
        date_format : str
            Date format string (example: "%%Y-%%m-%%d").

        Returns
        -------
        Index
            Index of formatted strings.

        See Also
        --------
        normalize : Return series with times to midnight.
        round : Round the series to the specified freq.
        floor : Floor the series to the specified freq.

        Examples
        --------
        >>> idx = ps.date_range(pd.Timestamp("2018-03-10 09:00"), periods=3, freq=\'s\')
        >>> idx.strftime(\'%B %d, %Y, %r\')  # doctest: +NORMALIZE_WHITESPACE
        Index([\'March 10, 2018, 09:00:00 AM\', \'March 10, 2018, 09:00:01 AM\',
               \'March 10, 2018, 09:00:02 AM\'],
              dtype=\'object\')
        '''
    def indexer_between_time(self, start_time: datetime.time | str, end_time: datetime.time | str, include_start: bool = True, include_end: bool = True) -> Index:
        '''
        Return index locations of values between particular times of day
        (example: 9:00-9:30AM).

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
        values_between_time : Index of integers

        Examples
        --------
        >>> psidx = ps.date_range("2000-01-01", periods=3, freq="T")
        >>> psidx  # doctest: +NORMALIZE_WHITESPACE
        DatetimeIndex([\'2000-01-01 00:00:00\', \'2000-01-01 00:01:00\',
                       \'2000-01-01 00:02:00\'],
                      dtype=\'datetime64[ns]\', freq=None)

        >>> psidx.indexer_between_time("00:01", "00:02").sort_values()
        Int64Index([1, 2], dtype=\'int64\')

        >>> psidx.indexer_between_time("00:01", "00:02", include_end=False)
        Int64Index([1], dtype=\'int64\')

        >>> psidx.indexer_between_time("00:01", "00:02", include_start=False)
        Int64Index([2], dtype=\'int64\')
        '''
    def indexer_at_time(self, time: datetime.time | str, asof: bool = False) -> Index:
        '''
        Return index locations of values at particular time of day
        (example: 9:30AM).

        Parameters
        ----------
        time : datetime.time or str
            Time passed in either as object (datetime.time) or as string in
            appropriate format ("%H:%M", "%H%M", "%I:%M%p", "%I%M%p",
            "%H:%M:%S", "%H%M%S", "%I:%M:%S%p", "%I%M%S%p").

        Returns
        -------
        values_at_time : Index of integers

        Examples
        --------
        >>> psidx = ps.date_range("2000-01-01", periods=3, freq="T")
        >>> psidx  # doctest: +NORMALIZE_WHITESPACE
        DatetimeIndex([\'2000-01-01 00:00:00\', \'2000-01-01 00:01:00\',
                       \'2000-01-01 00:02:00\'],
                      dtype=\'datetime64[ns]\', freq=None)

        >>> psidx.indexer_at_time("00:00")
        Int64Index([0], dtype=\'int64\')

        >>> psidx.indexer_at_time("00:01")
        Int64Index([1], dtype=\'int64\')
        '''
    def all(self, *args, **kwargs) -> None: ...

def disallow_nanoseconds(freq: str | DateOffset) -> None: ...
