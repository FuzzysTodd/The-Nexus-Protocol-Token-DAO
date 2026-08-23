import pyspark.pandas as ps
from pandas.tseries.offsets import DateOffset
from pyspark.sql.types import DateType as DateType, LongType as LongType, TimestampNTZType as TimestampNTZType, TimestampType as TimestampType
from typing import Any

class DatetimeMethods:
    """Date/Time methods for pandas-on-Spark Series"""
    def __init__(self, series: ps.Series) -> None: ...
    @property
    def date(self) -> ps.Series:
        """
        Returns a Series of python datetime.date objects (namely, the date
        part of Timestamps without timezone information).
        """
    @property
    def time(self) -> ps.Series: ...
    @property
    def timetz(self) -> ps.Series: ...
    @property
    def year(self) -> ps.Series:
        """
        The year of the datetime.
        """
    @property
    def month(self) -> ps.Series:
        """
        The month of the timestamp as January = 1 December = 12.
        """
    @property
    def day(self) -> ps.Series:
        """
        The days of the datetime.
        """
    @property
    def hour(self) -> ps.Series:
        """
        The hours of the datetime.
        """
    @property
    def minute(self) -> ps.Series:
        """
        The minutes of the datetime.
        """
    @property
    def second(self) -> ps.Series:
        """
        The seconds of the datetime.
        """
    @property
    def microsecond(self) -> ps.Series:
        """
        The microseconds of the datetime.
        """
    @property
    def nanosecond(self) -> ps.Series: ...
    @property
    def week(self) -> ps.Series:
        """
        The week ordinal of the year.

        .. deprecated:: 3.4.0
        """
    @property
    def weekofyear(self) -> ps.Series: ...
    @property
    def dayofweek(self) -> ps.Series:
        """
        The day of the week with Monday=0, Sunday=6.

        Return the day of the week. It is assumed the week starts on
        Monday, which is denoted by 0 and ends on Sunday which is denoted
        by 6. This method is available on both Series with datetime
        values (using the `dt` accessor).

        Returns
        -------
        Series
            Containing integers indicating the day number.

        See Also
        --------
        Series.dt.dayofweek : Alias.
        Series.dt.weekday : Alias.
        Series.dt.day_name : Returns the name of the day of the week.

        Examples
        --------
        >>> s = ps.from_pandas(pd.date_range('2016-12-31', '2017-01-08', freq='D').to_series())
        >>> s.dt.dayofweek
        2016-12-31    5
        2017-01-01    6
        2017-01-02    0
        2017-01-03    1
        2017-01-04    2
        2017-01-05    3
        2017-01-06    4
        2017-01-07    5
        2017-01-08    6
        dtype: int64
        """
    @property
    def weekday(self) -> ps.Series: ...
    @property
    def dayofyear(self) -> ps.Series:
        """
        The ordinal day of the year.
        """
    @property
    def quarter(self) -> ps.Series:
        """
        The quarter of the date.
        """
    @property
    def is_month_start(self) -> ps.Series:
        '''
        Indicates whether the date is the first day of the month.

        Returns
        -------
        Series
            For Series, returns a Series with boolean values.

        See Also
        --------
        is_month_end : Return a boolean indicating whether the date
            is the last day of the month.

        Examples
        --------
        This method is available on Series with datetime values under
        the ``.dt`` accessor.

        >>> s = ps.Series(pd.date_range("2018-02-27", periods=3))
        >>> s
        0   2018-02-27
        1   2018-02-28
        2   2018-03-01
        dtype: datetime64[ns]

        >>> s.dt.is_month_start
        0    False
        1    False
        2     True
        dtype: bool
        '''
    @property
    def is_month_end(self) -> ps.Series:
        '''
        Indicates whether the date is the last day of the month.

        Returns
        -------
        Series
            For Series, returns a Series with boolean values.

        See Also
        --------
        is_month_start : Return a boolean indicating whether the date
            is the first day of the month.

        Examples
        --------
        This method is available on Series with datetime values under
        the ``.dt`` accessor.

        >>> s = ps.Series(pd.date_range("2018-02-27", periods=3))
        >>> s
        0   2018-02-27
        1   2018-02-28
        2   2018-03-01
        dtype: datetime64[ns]

        >>> s.dt.is_month_end
        0    False
        1     True
        2    False
        dtype: bool
        '''
    @property
    def is_quarter_start(self) -> ps.Series:
        '''
        Indicator for whether the date is the first day of a quarter.

        Returns
        -------
        is_quarter_start : Series
            The same type as the original data with boolean values. Series will
            have the same name and index.

        See Also
        --------
        quarter : Return the quarter of the date.
        is_quarter_end : Similar property for indicating the quarter start.

        Examples
        --------
        This method is available on Series with datetime values under
        the ``.dt`` accessor.

        >>> df = ps.DataFrame({\'dates\': pd.date_range("2017-03-30",
        ...                   periods=4)})
        >>> df
               dates
        0 2017-03-30
        1 2017-03-31
        2 2017-04-01
        3 2017-04-02

        >>> df.dates.dt.quarter
        0    1
        1    1
        2    2
        3    2
        Name: dates, dtype: int64

        >>> df.dates.dt.is_quarter_start
        0    False
        1    False
        2     True
        3    False
        Name: dates, dtype: bool
        '''
    @property
    def is_quarter_end(self) -> ps.Series:
        '''
        Indicator for whether the date is the last day of a quarter.

        Returns
        -------
        is_quarter_end : Series
            The same type as the original data with boolean values. Series will
            have the same name and index.

        See Also
        --------
        quarter : Return the quarter of the date.
        is_quarter_start : Similar property indicating the quarter start.

        Examples
        --------
        This method is available on Series with datetime values under
        the ``.dt`` accessor.

        >>> df = ps.DataFrame({\'dates\': pd.date_range("2017-03-30",
        ...                   periods=4)})
        >>> df
               dates
        0 2017-03-30
        1 2017-03-31
        2 2017-04-01
        3 2017-04-02

        >>> df.dates.dt.quarter
        0    1
        1    1
        2    2
        3    2
        Name: dates, dtype: int64

        >>> df.dates.dt.is_quarter_start
        0    False
        1    False
        2     True
        3    False
        Name: dates, dtype: bool
        '''
    @property
    def is_year_start(self) -> ps.Series:
        '''
        Indicate whether the date is the first day of a year.

        Returns
        -------
        Series
            The same type as the original data with boolean values. Series will
            have the same name and index.

        See Also
        --------
        is_year_end : Similar property indicating the last day of the year.

        Examples
        --------
        This method is available on Series with datetime values under
        the ``.dt`` accessor.

        >>> dates = ps.Series(pd.date_range("2017-12-30", periods=3))
        >>> dates
        0   2017-12-30
        1   2017-12-31
        2   2018-01-01
        dtype: datetime64[ns]

        >>> dates.dt.is_year_start
        0    False
        1    False
        2     True
        dtype: bool
        '''
    @property
    def is_year_end(self) -> ps.Series:
        '''
        Indicate whether the date is the last day of the year.

        Returns
        -------
        Series
            The same type as the original data with boolean values. Series will
            have the same name and index.

        See Also
        --------
        is_year_start : Similar property indicating the start of the year.

        Examples
        --------
        This method is available on Series with datetime values under
        the ``.dt`` accessor.

        >>> dates = ps.Series(pd.date_range("2017-12-30", periods=3))
        >>> dates
        0   2017-12-30
        1   2017-12-31
        2   2018-01-01
        dtype: datetime64[ns]

        >>> dates.dt.is_year_end
        0    False
        1     True
        2    False
        dtype: bool
        '''
    @property
    def is_leap_year(self) -> ps.Series:
        '''
        Boolean indicator if the date belongs to a leap year.

        A leap year is a year, which has 366 days (instead of 365) including
        29th of February as an intercalary day.
        Leap years are years which are multiples of four with the exception
        of years divisible by 100 but not by 400.

        Returns
        -------
        Series
             Booleans indicating if dates belong to a leap year.

        Examples
        --------
        This method is available on Series with datetime values under
        the ``.dt`` accessor.

        >>> dates_series = ps.Series(pd.date_range("2012-01-01", "2015-01-01", freq="Y"))
        >>> dates_series
        0   2012-12-31
        1   2013-12-31
        2   2014-12-31
        dtype: datetime64[ns]

        >>> dates_series.dt.is_leap_year
        0     True
        1    False
        2    False
        dtype: bool
        '''
    @property
    def daysinmonth(self) -> ps.Series:
        """
        The number of days in the month.
        """
    @property
    def days_in_month(self) -> ps.Series: ...
    def tz_localize(self, tz) -> None:
        """
        Localize tz-naive Datetime column to tz-aware Datetime column.
        """
    def tz_convert(self, tz) -> None:
        """
        Convert tz-aware Datetime column from one time zone to another.
        """
    def normalize(self) -> ps.Series:
        """
        Convert times to midnight.

        The time component of the date-time is converted to midnight i.e.
        00:00:00. This is useful in cases, when the time does not matter.
        Length is unaltered. The time zones are unaffected.

        This method is available on Series with datetime values under
        the ``.dt`` accessor, and directly on Datetime Array.

        Returns
        -------
        Series
            The same type as the original data. Series will have the same
            name and index.

        See Also
        --------
        floor : Floor the series to the specified freq.
        ceil : Ceil the series to the specified freq.
        round : Round the series to the specified freq.

        Examples
        --------
        >>> series = ps.Series(pd.Series(pd.date_range('2012-1-1 12:45:31', periods=3, freq='M')))
        >>> series.dt.normalize()
        0   2012-01-31
        1   2012-02-29
        2   2012-03-31
        dtype: datetime64[ns]
        """
    def strftime(self, date_format: str) -> ps.Series:
        '''
        Convert to a string Series using specified date_format.

        Return an series of formatted strings specified by date_format, which
        supports the same string format as the python standard library. Details
        of the string format can be found in the python string format
        doc.

        Parameters
        ----------
        date_format : str
            Date format string (example: "%%Y-%%m-%%d").

        Returns
        -------
        Series
            Series of formatted strings.

        See Also
        --------
        to_datetime : Convert the given argument to datetime.
        normalize : Return series with times to midnight.
        round : Round the series to the specified freq.
        floor : Floor the series to the specified freq.

        Examples
        --------
        >>> series = ps.Series(pd.date_range(pd.Timestamp("2018-03-10 09:00"),
        ...                                  periods=3, freq=\'s\'))
        >>> series
        0   2018-03-10 09:00:00
        1   2018-03-10 09:00:01
        2   2018-03-10 09:00:02
        dtype: datetime64[ns]

        >>> series.dt.strftime(\'%B %d, %Y, %r\')
        0    March 10, 2018, 09:00:00 AM
        1    March 10, 2018, 09:00:01 AM
        2    March 10, 2018, 09:00:02 AM
        dtype: object
        '''
    def round(self, freq: str | DateOffset, *args: Any, **kwargs: Any) -> ps.Series:
        '''
        Perform round operation on the data to the specified freq.

        Parameters
        ----------
        freq : str or Offset
            The frequency level to round the index to. Must be a fixed
            frequency like \'S\' (second) not \'ME\' (month end).

        nonexistent : \'shift_forward\', \'shift_backward, \'NaT\', timedelta, default \'raise\'
            A nonexistent time does not exist in a particular timezone
            where clocks moved forward due to DST.

            - \'shift_forward\' will shift the nonexistent time forward to the
              closest existing time
            - \'shift_backward\' will shift the nonexistent time backward to the
              closest existing time
            - \'NaT\' will return NaT where there are nonexistent times
            - timedelta objects will shift nonexistent times by the timedelta
            - \'raise\' will raise an NonExistentTimeError if there are
              nonexistent times

            .. note:: this option only works with pandas 0.24.0+

        Returns
        -------
        Series
            a Series with the same index for a Series.

        Raises
        ------
        ValueError if the `freq` cannot be converted.

        Examples
        --------
        >>> series = ps.Series(pd.date_range(\'1/1/2018 11:59:00\', periods=3, freq=\'min\'))
        >>> series
        0   2018-01-01 11:59:00
        1   2018-01-01 12:00:00
        2   2018-01-01 12:01:00
        dtype: datetime64[ns]

        >>> series.dt.round("H")
        0   2018-01-01 12:00:00
        1   2018-01-01 12:00:00
        2   2018-01-01 12:00:00
        dtype: datetime64[ns]
        '''
    def floor(self, freq: str | DateOffset, *args: Any, **kwargs: Any) -> ps.Series:
        '''
        Perform floor operation on the data to the specified freq.

        Parameters
        ----------
        freq : str or Offset
            The frequency level to floor the index to. Must be a fixed
            frequency like \'S\' (second) not \'ME\' (month end).

        nonexistent : \'shift_forward\', \'shift_backward, \'NaT\', timedelta, default \'raise\'
            A nonexistent time does not exist in a particular timezone
            where clocks moved forward due to DST.

            - \'shift_forward\' will shift the nonexistent time forward to the
              closest existing time
            - \'shift_backward\' will shift the nonexistent time backward to the
              closest existing time
            - \'NaT\' will return NaT where there are nonexistent times
            - timedelta objects will shift nonexistent times by the timedelta
            - \'raise\' will raise an NonExistentTimeError if there are
              nonexistent times

            .. note:: this option only works with pandas 0.24.0+

        Returns
        -------
        Series
            a Series with the same index for a Series.

        Raises
        ------
        ValueError if the `freq` cannot be converted.

        Examples
        --------
        >>> series = ps.Series(pd.date_range(\'1/1/2018 11:59:00\', periods=3, freq=\'min\'))
        >>> series
        0   2018-01-01 11:59:00
        1   2018-01-01 12:00:00
        2   2018-01-01 12:01:00
        dtype: datetime64[ns]

        >>> series.dt.floor("H")
        0   2018-01-01 11:00:00
        1   2018-01-01 12:00:00
        2   2018-01-01 12:00:00
        dtype: datetime64[ns]
        '''
    def ceil(self, freq: str | DateOffset, *args: Any, **kwargs: Any) -> ps.Series:
        '''
        Perform ceil operation on the data to the specified freq.

        Parameters
        ----------
        freq : str or Offset
            The frequency level to round the index to. Must be a fixed
            frequency like \'S\' (second) not \'ME\' (month end).

        nonexistent : \'shift_forward\', \'shift_backward, \'NaT\', timedelta, default \'raise\'
            A nonexistent time does not exist in a particular timezone
            where clocks moved forward due to DST.

            - \'shift_forward\' will shift the nonexistent time forward to the
              closest existing time
            - \'shift_backward\' will shift the nonexistent time backward to the
              closest existing time
            - \'NaT\' will return NaT where there are nonexistent times
            - timedelta objects will shift nonexistent times by the timedelta
            - \'raise\' will raise an NonExistentTimeError if there are
              nonexistent times

            .. note:: this option only works with pandas 0.24.0+

        Returns
        -------
        Series
            a Series with the same index for a Series.

        Raises
        ------
        ValueError if the `freq` cannot be converted.

        Examples
        --------
        >>> series = ps.Series(pd.date_range(\'1/1/2018 11:59:00\', periods=3, freq=\'min\'))
        >>> series
        0   2018-01-01 11:59:00
        1   2018-01-01 12:00:00
        2   2018-01-01 12:01:00
        dtype: datetime64[ns]

        >>> series.dt.ceil("H")
        0   2018-01-01 12:00:00
        1   2018-01-01 12:00:00
        2   2018-01-01 13:00:00
        dtype: datetime64[ns]
        '''
    def month_name(self, locale: str | None = None) -> ps.Series:
        """
        Return the month names of the series with specified locale.

        Parameters
        ----------
        locale : str, optional
            Locale determining the language in which to return the month name.
            Default is English locale.

        Returns
        -------
        Series
            Series of month names.

        Examples
        --------
        >>> series = ps.Series(pd.date_range(start='2018-01', freq='M', periods=3))
        >>> series
        0   2018-01-31
        1   2018-02-28
        2   2018-03-31
        dtype: datetime64[ns]

        >>> series.dt.month_name()
        0     January
        1    February
        2       March
        dtype: object
        """
    def day_name(self, locale: str | None = None) -> ps.Series:
        """
        Return the day names of the series with specified locale.

        Parameters
        ----------
        locale : str, optional
            Locale determining the language in which to return the day name.
            Default is English locale.

        Returns
        -------
        Series
            Series of day names.

        Examples
        --------
        >>> series = ps.Series(pd.date_range(start='2018-01-01', freq='D', periods=3))
        >>> series
        0   2018-01-01
        1   2018-01-02
        2   2018-01-03
        dtype: datetime64[ns]

        >>> series.dt.day_name()
        0       Monday
        1      Tuesday
        2    Wednesday
        dtype: object
        """
