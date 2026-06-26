from _typeshed import Incomplete
from pandas import DataFrame as DataFrame, Index as Index, Series as Series
from pandas._libs import lib as lib
from pandas._libs.tslibs import BaseOffset as BaseOffset, IncompatibleFrequency as IncompatibleFrequency, NaT as NaT, Period as Period, Timedelta as Timedelta, Timestamp as Timestamp, to_offset as to_offset
from pandas._typing import AnyArrayLike as AnyArrayLike, Axis as Axis, AxisInt as AxisInt, Frequency as Frequency, IndexLabel as IndexLabel, NDFrameT as NDFrameT, QuantileInterpolation as QuantileInterpolation, T as T, TimeGrouperOrigin as TimeGrouperOrigin, TimedeltaConvertibleTypes as TimedeltaConvertibleTypes, TimestampConvertibleTypes as TimestampConvertibleTypes, npt as npt
from pandas.core.apply import ResamplerWindowApply as ResamplerWindowApply
from pandas.core.base import PandasObject as PandasObject
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.groupby.generic import SeriesGroupBy as SeriesGroupBy
from pandas.core.groupby.groupby import BaseGroupBy as BaseGroupBy, GroupBy as GroupBy, get_groupby as get_groupby
from pandas.core.groupby.grouper import Grouper as Grouper
from pandas.core.groupby.ops import BinGrouper as BinGrouper
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex, date_range as date_range
from pandas.core.indexes.period import PeriodIndex as PeriodIndex, period_range as period_range
from pandas.core.indexes.timedeltas import TimedeltaIndex as TimedeltaIndex, timedelta_range as timedelta_range
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.tseries.frequencies import is_subperiod as is_subperiod, is_superperiod as is_superperiod
from pandas.tseries.offsets import Day as Day, Tick as Tick
from pandas.util._decorators import Appender as Appender, Substitution as Substitution, doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Callable, Hashable, Literal

class Resampler(BaseGroupBy, PandasObject):
    """
    Class for resampling datetimelike data, a groupby-like operation.
    See aggregate, transform, and apply functions on this object.

    It's easiest to use obj.resample(...) to use Resampler.

    Parameters
    ----------
    obj : Series or DataFrame
    groupby : TimeGrouper
    axis : int, default 0
    kind : str or None
        'period', 'timestamp' to override default index treatment

    Returns
    -------
    a Resampler of the appropriate type

    Notes
    -----
    After resampling, see aggregate, apply, and transform functions.
    """
    grouper: BinGrouper
    binner: DatetimeIndex | TimedeltaIndex | PeriodIndex
    exclusions: frozenset[Hashable]
    keys: Incomplete
    sort: bool
    axis: Incomplete
    kind: Incomplete
    group_keys: Incomplete
    as_index: bool
    def __init__(self, obj: NDFrame, timegrouper: TimeGrouper, axis: Axis = 0, kind: Incomplete | None = None, *, gpr_index: Index, group_keys: bool = False, selection: Incomplete | None = None) -> None: ...
    def __getattr__(self, attr: str): ...
    def pipe(self, func: Callable[..., T] | tuple[Callable[..., T], str], *args, **kwargs) -> T: ...
    def aggregate(self, func: Incomplete | None = None, *args, **kwargs): ...
    agg = aggregate
    apply = aggregate
    def transform(self, arg, *args, **kwargs):
        """
        Call function producing a like-indexed Series on each group.

        Return a Series with the transformed values.

        Parameters
        ----------
        arg : function
            To apply to each group. Should return a Series with the same index.

        Returns
        -------
        Series

        Examples
        --------
        >>> s = pd.Series([1, 2],
        ...               index=pd.date_range('20180101',
        ...                                   periods=2,
        ...                                   freq='1h'))
        >>> s
        2018-01-01 00:00:00    1
        2018-01-01 01:00:00    2
        Freq: H, dtype: int64

        >>> resampled = s.resample('15min')
        >>> resampled.transform(lambda x: (x - x.mean()) / x.std())
        2018-01-01 00:00:00   NaN
        2018-01-01 01:00:00   NaN
        Freq: H, dtype: float64
        """
    def ffill(self, limit: Incomplete | None = None):
        """
        Forward fill the values.

        Parameters
        ----------
        limit : int, optional
            Limit of how many values to fill.

        Returns
        -------
        An upsampled Series.

        See Also
        --------
        Series.fillna: Fill NA/NaN values using the specified method.
        DataFrame.fillna: Fill NA/NaN values using the specified method.
        """
    def nearest(self, limit: Incomplete | None = None):
        """
        Resample by using the nearest value.

        When resampling data, missing values may appear (e.g., when the
        resampling frequency is higher than the original frequency).
        The `nearest` method will replace ``NaN`` values that appeared in
        the resampled data with the value from the nearest member of the
        sequence, based on the index value.
        Missing values that existed in the original data will not be modified.
        If `limit` is given, fill only this many values in each direction for
        each of the original values.

        Parameters
        ----------
        limit : int, optional
            Limit of how many values to fill.

        Returns
        -------
        Series or DataFrame
            An upsampled Series or DataFrame with ``NaN`` values filled with
            their nearest value.

        See Also
        --------
        backfill : Backward fill the new missing values in the resampled data.
        pad : Forward fill ``NaN`` values.

        Examples
        --------
        >>> s = pd.Series([1, 2],
        ...               index=pd.date_range('20180101',
        ...                                   periods=2,
        ...                                   freq='1h'))
        >>> s
        2018-01-01 00:00:00    1
        2018-01-01 01:00:00    2
        Freq: H, dtype: int64

        >>> s.resample('15min').nearest()
        2018-01-01 00:00:00    1
        2018-01-01 00:15:00    1
        2018-01-01 00:30:00    2
        2018-01-01 00:45:00    2
        2018-01-01 01:00:00    2
        Freq: 15T, dtype: int64

        Limit the number of upsampled values imputed by the nearest:

        >>> s.resample('15min').nearest(limit=1)
        2018-01-01 00:00:00    1.0
        2018-01-01 00:15:00    1.0
        2018-01-01 00:30:00    NaN
        2018-01-01 00:45:00    2.0
        2018-01-01 01:00:00    2.0
        Freq: 15T, dtype: float64
        """
    def bfill(self, limit: Incomplete | None = None):
        """
        Backward fill the new missing values in the resampled data.

        In statistics, imputation is the process of replacing missing data with
        substituted values [1]_. When resampling data, missing values may
        appear (e.g., when the resampling frequency is higher than the original
        frequency). The backward fill will replace NaN values that appeared in
        the resampled data with the next value in the original sequence.
        Missing values that existed in the original data will not be modified.

        Parameters
        ----------
        limit : int, optional
            Limit of how many values to fill.

        Returns
        -------
        Series, DataFrame
            An upsampled Series or DataFrame with backward filled NaN values.

        See Also
        --------
        bfill : Alias of backfill.
        fillna : Fill NaN values using the specified method, which can be
            'backfill'.
        nearest : Fill NaN values with nearest neighbor starting from center.
        ffill : Forward fill NaN values.
        Series.fillna : Fill NaN values in the Series using the
            specified method, which can be 'backfill'.
        DataFrame.fillna : Fill NaN values in the DataFrame using the
            specified method, which can be 'backfill'.

        References
        ----------
        .. [1] https://en.wikipedia.org/wiki/Imputation_(statistics)

        Examples
        --------
        Resampling a Series:

        >>> s = pd.Series([1, 2, 3],
        ...               index=pd.date_range('20180101', periods=3, freq='h'))
        >>> s
        2018-01-01 00:00:00    1
        2018-01-01 01:00:00    2
        2018-01-01 02:00:00    3
        Freq: H, dtype: int64

        >>> s.resample('30min').bfill()
        2018-01-01 00:00:00    1
        2018-01-01 00:30:00    2
        2018-01-01 01:00:00    2
        2018-01-01 01:30:00    3
        2018-01-01 02:00:00    3
        Freq: 30T, dtype: int64

        >>> s.resample('15min').bfill(limit=2)
        2018-01-01 00:00:00    1.0
        2018-01-01 00:15:00    NaN
        2018-01-01 00:30:00    2.0
        2018-01-01 00:45:00    2.0
        2018-01-01 01:00:00    2.0
        2018-01-01 01:15:00    NaN
        2018-01-01 01:30:00    3.0
        2018-01-01 01:45:00    3.0
        2018-01-01 02:00:00    3.0
        Freq: 15T, dtype: float64

        Resampling a DataFrame that has missing values:

        >>> df = pd.DataFrame({'a': [2, np.nan, 6], 'b': [1, 3, 5]},
        ...                   index=pd.date_range('20180101', periods=3,
        ...                                       freq='h'))
        >>> df
                               a  b
        2018-01-01 00:00:00  2.0  1
        2018-01-01 01:00:00  NaN  3
        2018-01-01 02:00:00  6.0  5

        >>> df.resample('30min').bfill()
                               a  b
        2018-01-01 00:00:00  2.0  1
        2018-01-01 00:30:00  NaN  3
        2018-01-01 01:00:00  NaN  3
        2018-01-01 01:30:00  6.0  5
        2018-01-01 02:00:00  6.0  5

        >>> df.resample('15min').bfill(limit=2)
                               a    b
        2018-01-01 00:00:00  2.0  1.0
        2018-01-01 00:15:00  NaN  NaN
        2018-01-01 00:30:00  NaN  3.0
        2018-01-01 00:45:00  NaN  3.0
        2018-01-01 01:00:00  NaN  3.0
        2018-01-01 01:15:00  NaN  NaN
        2018-01-01 01:30:00  6.0  5.0
        2018-01-01 01:45:00  6.0  5.0
        2018-01-01 02:00:00  6.0  5.0
        """
    def fillna(self, method, limit: Incomplete | None = None):
        '''
        Fill missing values introduced by upsampling.

        In statistics, imputation is the process of replacing missing data with
        substituted values [1]_. When resampling data, missing values may
        appear (e.g., when the resampling frequency is higher than the original
        frequency).

        Missing values that existed in the original data will
        not be modified.

        Parameters
        ----------
        method : {\'pad\', \'backfill\', \'ffill\', \'bfill\', \'nearest\'}
            Method to use for filling holes in resampled data

            * \'pad\' or \'ffill\': use previous valid observation to fill gap
              (forward fill).
            * \'backfill\' or \'bfill\': use next valid observation to fill gap.
            * \'nearest\': use nearest valid observation to fill gap.

        limit : int, optional
            Limit of how many consecutive missing values to fill.

        Returns
        -------
        Series or DataFrame
            An upsampled Series or DataFrame with missing values filled.

        See Also
        --------
        bfill : Backward fill NaN values in the resampled data.
        ffill : Forward fill NaN values in the resampled data.
        nearest : Fill NaN values in the resampled data
            with nearest neighbor starting from center.
        interpolate : Fill NaN values using interpolation.
        Series.fillna : Fill NaN values in the Series using the
            specified method, which can be \'bfill\' and \'ffill\'.
        DataFrame.fillna : Fill NaN values in the DataFrame using the
            specified method, which can be \'bfill\' and \'ffill\'.

        References
        ----------
        .. [1] https://en.wikipedia.org/wiki/Imputation_(statistics)

        Examples
        --------
        Resampling a Series:

        >>> s = pd.Series([1, 2, 3],
        ...               index=pd.date_range(\'20180101\', periods=3, freq=\'h\'))
        >>> s
        2018-01-01 00:00:00    1
        2018-01-01 01:00:00    2
        2018-01-01 02:00:00    3
        Freq: H, dtype: int64

        Without filling the missing values you get:

        >>> s.resample("30min").asfreq()
        2018-01-01 00:00:00    1.0
        2018-01-01 00:30:00    NaN
        2018-01-01 01:00:00    2.0
        2018-01-01 01:30:00    NaN
        2018-01-01 02:00:00    3.0
        Freq: 30T, dtype: float64

        >>> s.resample(\'30min\').fillna("backfill")
        2018-01-01 00:00:00    1
        2018-01-01 00:30:00    2
        2018-01-01 01:00:00    2
        2018-01-01 01:30:00    3
        2018-01-01 02:00:00    3
        Freq: 30T, dtype: int64

        >>> s.resample(\'15min\').fillna("backfill", limit=2)
        2018-01-01 00:00:00    1.0
        2018-01-01 00:15:00    NaN
        2018-01-01 00:30:00    2.0
        2018-01-01 00:45:00    2.0
        2018-01-01 01:00:00    2.0
        2018-01-01 01:15:00    NaN
        2018-01-01 01:30:00    3.0
        2018-01-01 01:45:00    3.0
        2018-01-01 02:00:00    3.0
        Freq: 15T, dtype: float64

        >>> s.resample(\'30min\').fillna("pad")
        2018-01-01 00:00:00    1
        2018-01-01 00:30:00    1
        2018-01-01 01:00:00    2
        2018-01-01 01:30:00    2
        2018-01-01 02:00:00    3
        Freq: 30T, dtype: int64

        >>> s.resample(\'30min\').fillna("nearest")
        2018-01-01 00:00:00    1
        2018-01-01 00:30:00    2
        2018-01-01 01:00:00    2
        2018-01-01 01:30:00    3
        2018-01-01 02:00:00    3
        Freq: 30T, dtype: int64

        Missing values present before the upsampling are not affected.

        >>> sm = pd.Series([1, None, 3],
        ...               index=pd.date_range(\'20180101\', periods=3, freq=\'h\'))
        >>> sm
        2018-01-01 00:00:00    1.0
        2018-01-01 01:00:00    NaN
        2018-01-01 02:00:00    3.0
        Freq: H, dtype: float64

        >>> sm.resample(\'30min\').fillna(\'backfill\')
        2018-01-01 00:00:00    1.0
        2018-01-01 00:30:00    NaN
        2018-01-01 01:00:00    NaN
        2018-01-01 01:30:00    3.0
        2018-01-01 02:00:00    3.0
        Freq: 30T, dtype: float64

        >>> sm.resample(\'30min\').fillna(\'pad\')
        2018-01-01 00:00:00    1.0
        2018-01-01 00:30:00    1.0
        2018-01-01 01:00:00    NaN
        2018-01-01 01:30:00    NaN
        2018-01-01 02:00:00    3.0
        Freq: 30T, dtype: float64

        >>> sm.resample(\'30min\').fillna(\'nearest\')
        2018-01-01 00:00:00    1.0
        2018-01-01 00:30:00    NaN
        2018-01-01 01:00:00    NaN
        2018-01-01 01:30:00    3.0
        2018-01-01 02:00:00    3.0
        Freq: 30T, dtype: float64

        DataFrame resampling is done column-wise. All the same options are
        available.

        >>> df = pd.DataFrame({\'a\': [2, np.nan, 6], \'b\': [1, 3, 5]},
        ...                   index=pd.date_range(\'20180101\', periods=3,
        ...                                       freq=\'h\'))
        >>> df
                               a  b
        2018-01-01 00:00:00  2.0  1
        2018-01-01 01:00:00  NaN  3
        2018-01-01 02:00:00  6.0  5

        >>> df.resample(\'30min\').fillna("bfill")
                               a  b
        2018-01-01 00:00:00  2.0  1
        2018-01-01 00:30:00  NaN  3
        2018-01-01 01:00:00  NaN  3
        2018-01-01 01:30:00  6.0  5
        2018-01-01 02:00:00  6.0  5
        '''
    def interpolate(self, method: QuantileInterpolation = 'linear', *, axis: Axis = 0, limit: Incomplete | None = None, inplace: bool = False, limit_direction: Literal['forward', 'backward', 'both'] = 'forward', limit_area: Incomplete | None = None, downcast: Incomplete | None = None, **kwargs):
        """
        Interpolate values according to different methods.
        """
    def asfreq(self, fill_value: Incomplete | None = None):
        """
        Return the values at the new freq, essentially a reindex.

        Parameters
        ----------
        fill_value : scalar, optional
            Value to use for missing values, applied during upsampling (note
            this does not fill NaNs that already were present).

        Returns
        -------
        DataFrame or Series
            Values at the specified freq.

        See Also
        --------
        Series.asfreq: Convert TimeSeries to specified frequency.
        DataFrame.asfreq: Convert TimeSeries to specified frequency.
        """
    def sum(self, numeric_only: bool = False, min_count: int = 0, *args, **kwargs): ...
    def prod(self, numeric_only: bool = False, min_count: int = 0, *args, **kwargs): ...
    def min(self, numeric_only: bool = False, min_count: int = 0, *args, **kwargs): ...
    def max(self, numeric_only: bool = False, min_count: int = 0, *args, **kwargs): ...
    def first(self, numeric_only: bool = False, min_count: int = 0, *args, **kwargs): ...
    def last(self, numeric_only: bool = False, min_count: int = 0, *args, **kwargs): ...
    def median(self, numeric_only: bool = False, *args, **kwargs): ...
    def mean(self, numeric_only: bool = False, *args, **kwargs):
        """
        Compute mean of groups, excluding missing values.

        Parameters
        ----------
        numeric_only : bool, default False
            Include only `float`, `int` or `boolean` data.

            .. versionchanged:: 2.0.0

                numeric_only now defaults to ``False``.

        Returns
        -------
        DataFrame or Series
            Mean of values within each group.
        """
    def std(self, ddof: int = 1, numeric_only: bool = False, *args, **kwargs):
        """
        Compute standard deviation of groups, excluding missing values.

        Parameters
        ----------
        ddof : int, default 1
            Degrees of freedom.
        numeric_only : bool, default False
            Include only `float`, `int` or `boolean` data.

            .. versionadded:: 1.5.0

            .. versionchanged:: 2.0.0

                numeric_only now defaults to ``False``.

        Returns
        -------
        DataFrame or Series
            Standard deviation of values within each group.
        """
    def var(self, ddof: int = 1, numeric_only: bool = False, *args, **kwargs):
        """
        Compute variance of groups, excluding missing values.

        Parameters
        ----------
        ddof : int, default 1
            Degrees of freedom.

        numeric_only : bool, default False
            Include only `float`, `int` or `boolean` data.

            .. versionadded:: 1.5.0

            .. versionchanged:: 2.0.0

                numeric_only now defaults to ``False``.

        Returns
        -------
        DataFrame or Series
            Variance of values within each group.
        """
    def sem(self, ddof: int = 1, numeric_only: bool = False, *args, **kwargs): ...
    def ohlc(self, *args, **kwargs): ...
    def nunique(self, *args, **kwargs): ...
    def size(self): ...
    def count(self): ...
    def quantile(self, q: float | AnyArrayLike = 0.5, **kwargs):
        """
        Return value at the given quantile.

        Parameters
        ----------
        q : float or array-like, default 0.5 (50% quantile)

        Returns
        -------
        DataFrame or Series
            Quantile of values within each group.

        See Also
        --------
        Series.quantile
            Return a series, where the index is q and the values are the quantiles.
        DataFrame.quantile
            Return a DataFrame, where the columns are the columns of self,
            and the values are the quantiles.
        DataFrameGroupBy.quantile
            Return a DataFrame, where the columns are groupby columns,
            and the values are its quantiles.
        """

class _GroupByMixin(PandasObject):
    """
    Provide the groupby facilities.
    """
    binner: Incomplete
    key: Incomplete
    ax: Incomplete
    obj: Incomplete
    def __init__(self, *, parent: Resampler, groupby: GroupBy, key: Incomplete | None = None, selection: IndexLabel | None = None) -> None: ...

class DatetimeIndexResampler(Resampler): ...
class DatetimeIndexResamplerGroupby(_GroupByMixin, DatetimeIndexResampler):
    """
    Provides a resample of a groupby implementation
    """
class PeriodIndexResampler(DatetimeIndexResampler): ...
class PeriodIndexResamplerGroupby(_GroupByMixin, PeriodIndexResampler):
    """
    Provides a resample of a groupby implementation.
    """
class TimedeltaIndexResampler(DatetimeIndexResampler): ...
class TimedeltaIndexResamplerGroupby(_GroupByMixin, TimedeltaIndexResampler):
    """
    Provides a resample of a groupby implementation.
    """

def get_resampler(obj: Series | DataFrame, kind: Incomplete | None = None, **kwds) -> Resampler:
    """
    Create a TimeGrouper and return our resampler.
    """
def get_resampler_for_grouping(groupby: GroupBy, rule, how: Incomplete | None = None, fill_method: Incomplete | None = None, limit: Incomplete | None = None, kind: Incomplete | None = None, on: Incomplete | None = None, **kwargs) -> Resampler:
    """
    Return our appropriate resampler when grouping as well.
    """

class TimeGrouper(Grouper):
    """
    Custom groupby class for time-interval grouping.

    Parameters
    ----------
    freq : pandas date offset or offset alias for identifying bin edges
    closed : closed end of interval; 'left' or 'right'
    label : interval boundary to use for labeling; 'left' or 'right'
    convention : {'start', 'end', 'e', 's'}
        If axis is PeriodIndex
    """
    origin: TimeGrouperOrigin
    closed: Incomplete
    label: Incomplete
    kind: Incomplete
    convention: Incomplete
    how: Incomplete
    fill_method: Incomplete
    limit: Incomplete
    group_keys: Incomplete
    offset: Incomplete
    def __init__(self, freq: Frequency = 'Min', closed: Literal['left', 'right'] | None = None, label: Literal['left', 'right'] | None = None, how: str = 'mean', axis: Axis = 0, fill_method: Incomplete | None = None, limit: Incomplete | None = None, kind: str | None = None, convention: Literal['start', 'end', 'e', 's'] | None = None, origin: Literal['epoch', 'start', 'start_day', 'end', 'end_day'] | TimestampConvertibleTypes = 'start_day', offset: TimedeltaConvertibleTypes | None = None, group_keys: bool = False, **kwargs) -> None: ...

def asfreq(obj: NDFrameT, freq, method: Incomplete | None = None, how: Incomplete | None = None, normalize: bool = False, fill_value: Incomplete | None = None) -> NDFrameT:
    """
    Utility frequency conversion method for Series/DataFrame.

    See :meth:`pandas.NDFrame.asfreq` for full documentation.
    """
def maybe_warn_args_and_kwargs(cls, kernel: str, args, kwargs) -> None:
    """
    Warn for deprecation of args and kwargs in resample functions.

    Parameters
    ----------
    cls : type
        Class to warn about.
    kernel : str
        Operation name.
    args : tuple or None
        args passed by user. Will be None if and only if kernel does not have args.
    kwargs : dict or None
        kwargs passed by user. Will be None if and only if kernel does not have kwargs.
    """
