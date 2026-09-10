import abc
from abc import ABCMeta, abstractmethod
from pyspark import SparkContext as SparkContext
from pyspark.pandas._typing import FrameLike as FrameLike
from pyspark.pandas.groupby import DataFrameGroupBy as DataFrameGroupBy, GroupBy as GroupBy
from pyspark.pandas.internal import NATURAL_ORDER_COLUMN_NAME as NATURAL_ORDER_COLUMN_NAME, SPARK_INDEX_NAME_FORMAT as SPARK_INDEX_NAME_FORMAT
from pyspark.pandas.missing.window import MissingPandasLikeExpanding as MissingPandasLikeExpanding, MissingPandasLikeExpandingGroupby as MissingPandasLikeExpandingGroupby, MissingPandasLikeExponentialMoving as MissingPandasLikeExponentialMoving, MissingPandasLikeExponentialMovingGroupby as MissingPandasLikeExponentialMovingGroupby, MissingPandasLikeRolling as MissingPandasLikeRolling, MissingPandasLikeRollingGroupby as MissingPandasLikeRollingGroupby
from pyspark.pandas.utils import scol_for as scol_for
from pyspark.sql import Window as Window
from pyspark.sql.column import Column as Column
from pyspark.sql.types import DoubleType as DoubleType
from pyspark.sql.window import WindowSpec as WindowSpec
from typing import Any, Generic

class RollingAndExpanding(Generic[FrameLike], metaclass=ABCMeta):
    def __init__(self, window: WindowSpec, min_periods: int) -> None: ...
    @abstractmethod
    def count(self) -> FrameLike: ...
    def sum(self) -> FrameLike: ...
    def min(self) -> FrameLike: ...
    def max(self) -> FrameLike: ...
    def mean(self) -> FrameLike: ...
    def quantile(self, q: float, accuracy: int = 10000) -> FrameLike: ...
    def std(self) -> FrameLike: ...
    def var(self) -> FrameLike: ...
    def skew(self) -> FrameLike: ...
    def kurt(self) -> FrameLike: ...

class RollingLike(RollingAndExpanding[FrameLike], metaclass=abc.ABCMeta):
    def __init__(self, window: int, min_periods: int | None = None) -> None: ...
    def count(self) -> FrameLike: ...

class Rolling(RollingLike[FrameLike]):
    def __init__(self, psdf_or_psser: FrameLike, window: int, min_periods: int | None = None) -> None: ...
    def __getattr__(self, item: str) -> Any: ...
    def count(self) -> FrameLike:
        '''
        The rolling count of any non-NaN observations inside the window.

        .. note:: the current implementation of this API uses Spark\'s Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Return type is the same as the original object with `np.float64` dtype.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.count : Count of the full Series.
        pyspark.pandas.DataFrame.count : Count of the full DataFrame.

        Examples
        --------
        >>> s = ps.Series([2, 3, float("nan"), 10])
        >>> s.rolling(1).count()
        0    1.0
        1    1.0
        2    0.0
        3    1.0
        dtype: float64

        >>> s.rolling(3).count()
        0    1.0
        1    2.0
        2    2.0
        3    2.0
        dtype: float64

        >>> s.to_frame().rolling(1).count()
             0
        0  1.0
        1  1.0
        2  0.0
        3  1.0

        >>> s.to_frame().rolling(3).count()
             0
        0  1.0
        1  2.0
        2  2.0
        3  2.0
        '''
    def sum(self) -> FrameLike:
        '''
        Calculate rolling summation of given DataFrame or Series.

        .. note:: the current implementation of this API uses Spark\'s Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Same type as the input, with the same index, containing the
            rolling summation.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.sum : Reducing sum for Series.
        pyspark.pandas.DataFrame.sum : Reducing sum for DataFrame.

        Examples
        --------
        >>> s = ps.Series([4, 3, 5, 2, 6])
        >>> s
        0    4
        1    3
        2    5
        3    2
        4    6
        dtype: int64

        >>> s.rolling(2).sum()
        0    NaN
        1    7.0
        2    8.0
        3    7.0
        4    8.0
        dtype: float64

        >>> s.rolling(3).sum()
        0     NaN
        1     NaN
        2    12.0
        3    10.0
        4    13.0
        dtype: float64

        For DataFrame, each rolling summation is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df
           A   B
        0  4  16
        1  3   9
        2  5  25
        3  2   4
        4  6  36

        >>> df.rolling(2).sum()
             A     B
        0  NaN   NaN
        1  7.0  25.0
        2  8.0  34.0
        3  7.0  29.0
        4  8.0  40.0

        >>> df.rolling(3).sum()
              A     B
        0   NaN   NaN
        1   NaN   NaN
        2  12.0  50.0
        3  10.0  38.0
        4  13.0  65.0
        '''
    def min(self) -> FrameLike:
        '''
        Calculate the rolling minimum.

        .. note:: the current implementation of this API uses Spark\'s Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the rolling
            calculation.

        See Also
        --------
        pyspark.pandas.Series.rolling : Calling object with a Series.
        pyspark.pandas.DataFrame.rolling : Calling object with a DataFrame.
        pyspark.pandas.Series.min : Similar method for Series.
        pyspark.pandas.DataFrame.min : Similar method for DataFrame.

        Examples
        --------
        >>> s = ps.Series([4, 3, 5, 2, 6])
        >>> s
        0    4
        1    3
        2    5
        3    2
        4    6
        dtype: int64

        >>> s.rolling(2).min()
        0    NaN
        1    3.0
        2    3.0
        3    2.0
        4    2.0
        dtype: float64

        >>> s.rolling(3).min()
        0    NaN
        1    NaN
        2    3.0
        3    2.0
        4    2.0
        dtype: float64

        For DataFrame, each rolling minimum is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df
           A   B
        0  4  16
        1  3   9
        2  5  25
        3  2   4
        4  6  36

        >>> df.rolling(2).min()
             A    B
        0  NaN  NaN
        1  3.0  9.0
        2  3.0  9.0
        3  2.0  4.0
        4  2.0  4.0

        >>> df.rolling(3).min()
             A    B
        0  NaN  NaN
        1  NaN  NaN
        2  3.0  9.0
        3  2.0  4.0
        4  2.0  4.0
        '''
    def max(self) -> FrameLike:
        '''
        Calculate the rolling maximum.

        .. note:: the current implementation of this API uses Spark\'s Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Return type is determined by the caller.

        See Also
        --------
        pyspark.pandas.Series.rolling : Series rolling.
        pyspark.pandas.DataFrame.rolling : DataFrame rolling.
        pyspark.pandas.Series.max : Similar method for Series.
        pyspark.pandas.DataFrame.max : Similar method for DataFrame.

        Examples
        --------
        >>> s = ps.Series([4, 3, 5, 2, 6])
        >>> s
        0    4
        1    3
        2    5
        3    2
        4    6
        dtype: int64

        >>> s.rolling(2).max()
        0    NaN
        1    4.0
        2    5.0
        3    5.0
        4    6.0
        dtype: float64

        >>> s.rolling(3).max()
        0    NaN
        1    NaN
        2    5.0
        3    5.0
        4    6.0
        dtype: float64

        For DataFrame, each rolling maximum is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df
           A   B
        0  4  16
        1  3   9
        2  5  25
        3  2   4
        4  6  36

        >>> df.rolling(2).max()
             A     B
        0  NaN   NaN
        1  4.0  16.0
        2  5.0  25.0
        3  5.0  25.0
        4  6.0  36.0

        >>> df.rolling(3).max()
             A     B
        0  NaN   NaN
        1  NaN   NaN
        2  5.0  25.0
        3  5.0  25.0
        4  6.0  36.0
        '''
    def mean(self) -> FrameLike:
        '''
        Calculate the rolling mean of the values.

        .. note:: the current implementation of this API uses Spark\'s Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the rolling
            calculation.

        See Also
        --------
        pyspark.pandas.Series.rolling : Calling object with Series data.
        pyspark.pandas.DataFrame.rolling : Calling object with DataFrames.
        pyspark.pandas.Series.mean : Equivalent method for Series.
        pyspark.pandas.DataFrame.mean : Equivalent method for DataFrame.

        Examples
        --------
        >>> s = ps.Series([4, 3, 5, 2, 6])
        >>> s
        0    4
        1    3
        2    5
        3    2
        4    6
        dtype: int64

        >>> s.rolling(2).mean()
        0    NaN
        1    3.5
        2    4.0
        3    3.5
        4    4.0
        dtype: float64

        >>> s.rolling(3).mean()
        0         NaN
        1         NaN
        2    4.000000
        3    3.333333
        4    4.333333
        dtype: float64

        For DataFrame, each rolling mean is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df
           A   B
        0  4  16
        1  3   9
        2  5  25
        3  2   4
        4  6  36

        >>> df.rolling(2).mean()
             A     B
        0  NaN   NaN
        1  3.5  12.5
        2  4.0  17.0
        3  3.5  14.5
        4  4.0  20.0

        >>> df.rolling(3).mean()
                  A          B
        0       NaN        NaN
        1       NaN        NaN
        2  4.000000  16.666667
        3  3.333333  12.666667
        4  4.333333  21.666667
        '''
    def quantile(self, quantile: float, accuracy: int = 10000) -> FrameLike:
        '''
        Calculate the rolling quantile of the values.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        quantile : float
            Value between 0 and 1 providing the quantile to compute.
        accuracy : int, optional
            Default accuracy of approximation. Larger value means better accuracy.
            The relative error can be deduced by 1.0 / accuracy.
            This is a panda-on-Spark specific parameter.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the rolling
            calculation.

        Notes
        -----
        `quantile` in pandas-on-Spark are using distributed percentile approximation
        algorithm unlike pandas, the result might be different with pandas, also `interpolation`
        parameter is not supported yet.

        the current implementation of this API uses Spark\'s Window without
        specifying partition specification. This leads to move all data into
        single partition in single machine and could cause serious
        performance degradation. Avoid this method against very large dataset.

        See Also
        --------
        pyspark.pandas.Series.rolling : Calling rolling with Series data.
        pyspark.pandas.DataFrame.rolling : Calling rolling with DataFrames.
        pyspark.pandas.Series.quantile : Aggregating quantile for Series.
        pyspark.pandas.DataFrame.quantile : Aggregating quantile for DataFrame.

        Examples
        --------
        >>> s = ps.Series([4, 3, 5, 2, 6])
        >>> s
        0    4
        1    3
        2    5
        3    2
        4    6
        dtype: int64

        >>> s.rolling(2).quantile(0.5)
        0    NaN
        1    3.0
        2    3.0
        3    2.0
        4    2.0
        dtype: float64

        >>> s.rolling(3).quantile(0.5)
        0    NaN
        1    NaN
        2    4.0
        3    3.0
        4    5.0
        dtype: float64

        For DataFrame, each rolling quantile is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df
           A   B
        0  4  16
        1  3   9
        2  5  25
        3  2   4
        4  6  36

        >>> df.rolling(2).quantile(0.5)
             A    B
        0  NaN  NaN
        1  3.0  9.0
        2  3.0  9.0
        3  2.0  4.0
        4  2.0  4.0

        >>> df.rolling(3).quantile(0.5)
             A     B
        0  NaN   NaN
        1  NaN   NaN
        2  4.0  16.0
        3  3.0   9.0
        4  5.0  25.0
        '''
    def std(self) -> FrameLike:
        '''
        Calculate rolling standard deviation.

        .. note:: the current implementation of this API uses Spark\'s Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Returns the same object type as the caller of the rolling calculation.

        See Also
        --------
        pyspark.pandas.Series.rolling : Calling object with Series data.
        pyspark.pandas.DataFrame.rolling : Calling object with DataFrames.
        pyspark.pandas.Series.std : Equivalent method for Series.
        pyspark.pandas.DataFrame.std : Equivalent method for DataFrame.
        numpy.std : Equivalent method for Numpy array.

        Examples
        --------
        >>> s = ps.Series([5, 5, 6, 7, 5, 5, 5])
        >>> s.rolling(3).std()
        0         NaN
        1         NaN
        2    0.577350
        3    1.000000
        4    1.000000
        5    1.154701
        6    0.000000
        dtype: float64

        For DataFrame, each rolling standard deviation is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.rolling(2).std()
                  A          B
        0       NaN        NaN
        1  0.000000   0.000000
        2  0.707107   7.778175
        3  0.707107   9.192388
        4  1.414214  16.970563
        5  0.000000   0.000000
        6  0.000000   0.000000
        '''
    def var(self) -> FrameLike:
        '''
        Calculate unbiased rolling variance.

        .. note:: the current implementation of this API uses Spark\'s Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Returns the same object type as the caller of the rolling calculation.

        See Also
        --------
        Series.rolling : Calling object with Series data.
        DataFrame.rolling : Calling object with DataFrames.
        Series.var : Equivalent method for Series.
        DataFrame.var : Equivalent method for DataFrame.
        numpy.var : Equivalent method for Numpy array.

        Examples
        --------
        >>> s = ps.Series([5, 5, 6, 7, 5, 5, 5])
        >>> s.rolling(3).var()
        0         NaN
        1         NaN
        2    0.333333
        3    1.000000
        4    1.000000
        5    1.333333
        6    0.000000
        dtype: float64

        For DataFrame, each unbiased rolling variance is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.rolling(2).var()
             A      B
        0  NaN    NaN
        1  0.0    0.0
        2  0.5   60.5
        3  0.5   84.5
        4  2.0  288.0
        5  0.0    0.0
        6  0.0    0.0
        '''
    def skew(self) -> FrameLike:
        '''
        Calculate unbiased rolling skew.

        .. note:: the current implementation of this API uses Spark\'s Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Returns the same object type as the caller of the rolling calculation.

        See Also
        --------
        pyspark.pandas.Series.rolling : Calling object with Series data.
        pyspark.pandas.DataFrame.rolling : Calling object with DataFrames.
        pyspark.pandas.Series.std : Equivalent method for Series.
        pyspark.pandas.DataFrame.std : Equivalent method for DataFrame.
        numpy.std : Equivalent method for Numpy array.

        Examples
        --------
        >>> s = ps.Series([5, 5, 6, 7, 5, 1, 5, 9])
        >>> s.rolling(3).skew()
        0         NaN
        1         NaN
        2    1.732051
        3    0.000000
        4    0.000000
        5   -0.935220
        6   -1.732051
        7    0.000000
        dtype: float64

        For DataFrame, each rolling standard deviation is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.rolling(5).skew()
                  A         B
        0       NaN       NaN
        1       NaN       NaN
        2       NaN       NaN
        3       NaN       NaN
        4  1.257788  1.369456
        5 -1.492685 -0.526039
        6 -1.492685 -0.526039
        7 -0.551618  0.686072
        '''
    def kurt(self) -> FrameLike:
        '''
        Calculate unbiased rolling kurtosis.

        .. note:: the current implementation of this API uses Spark\'s Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Returns the same object type as the caller of the rolling calculation.

        See Also
        --------
        pyspark.pandas.Series.rolling : Calling object with Series data.
        pyspark.pandas.DataFrame.rolling : Calling object with DataFrames.
        pyspark.pandas.Series.var : Equivalent method for Series.
        pyspark.pandas.DataFrame.var : Equivalent method for DataFrame.
        numpy.var : Equivalent method for Numpy array.

        Examples
        --------
        >>> s = ps.Series([5, 5, 6, 7, 5, 1, 5, 9])
        >>> s.rolling(4).kurt()
        0         NaN
        1         NaN
        2         NaN
        3   -1.289256
        4   -1.289256
        5    2.234867
        6    2.227147
        7    1.500000
        dtype: float64

        For DataFrame, each unbiased rolling variance is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.rolling(5).kurt()
                  A         B
        0       NaN       NaN
        1       NaN       NaN
        2       NaN       NaN
        3       NaN       NaN
        4  0.312500  0.906336
        5  2.818047  1.016942
        6  2.818047  1.016942
        7  0.867769  0.389750
        '''

class RollingGroupby(RollingLike[FrameLike]):
    def __init__(self, groupby: GroupBy[FrameLike], window: int, min_periods: int | None = None) -> None: ...
    def __getattr__(self, item: str) -> Any: ...
    def count(self) -> FrameLike:
        '''
        The rolling count of any non-NaN observations inside the window.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the expanding
            calculation.

        See Also
        --------
        pyspark.pandas.Series.rolling : Calling object with Series data.
        pyspark.pandas.DataFrame.rolling : Calling object with DataFrames.
        pyspark.pandas.Series.count : Count of the full Series.
        pyspark.pandas.DataFrame.count : Count of the full DataFrame.

        Examples
        --------
        >>> s = ps.Series([2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5])
        >>> s.groupby(s).rolling(3).count().sort_index()
        2  0     1.0
           1     2.0
        3  2     1.0
           3     2.0
           4     3.0
        4  5     1.0
           6     2.0
           7     3.0
           8     3.0
        5  9     1.0
           10    2.0
        dtype: float64

        For DataFrame, each rolling count is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.groupby(df.A).rolling(2).count().sort_index()  # doctest: +NORMALIZE_WHITESPACE
                B
        A
        2 0   1.0
          1   2.0
        3 2   1.0
          3   2.0
          4   2.0
        4 5   1.0
          6   2.0
          7   2.0
          8   2.0
        5 9   1.0
          10  2.0
        '''
    def sum(self) -> FrameLike:
        '''
        The rolling summation of any non-NaN observations inside the window.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the rolling
            calculation.

        See Also
        --------
        pyspark.pandas.Series.rolling : Calling object with Series data.
        pyspark.pandas.DataFrame.rolling : Calling object with DataFrames.
        pyspark.pandas.Series.sum : Sum of the full Series.
        pyspark.pandas.DataFrame.sum : Sum of the full DataFrame.

        Examples
        --------
        >>> s = ps.Series([2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5])
        >>> s.groupby(s).rolling(3).sum().sort_index()
        2  0      NaN
           1      NaN
        3  2      NaN
           3      NaN
           4      9.0
        4  5      NaN
           6      NaN
           7     12.0
           8     12.0
        5  9      NaN
           10     NaN
        dtype: float64

        For DataFrame, each rolling summation is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.groupby(df.A).rolling(2).sum().sort_index()  # doctest: +NORMALIZE_WHITESPACE
                 B
        A
        2 0    NaN
          1    8.0
        3 2    NaN
          3   18.0
          4   18.0
        4 5    NaN
          6   32.0
          7   32.0
          8   32.0
        5 9    NaN
          10  50.0
        '''
    def min(self) -> FrameLike:
        '''
        The rolling minimum of any non-NaN observations inside the window.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the rolling
            calculation.

        See Also
        --------
        pyspark.pandas.Series.rolling : Calling object with Series data.
        pyspark.pandas.DataFrame.rolling : Calling object with DataFrames.
        pyspark.pandas.Series.min : Min of the full Series.
        pyspark.pandas.DataFrame.min : Min of the full DataFrame.

        Examples
        --------
        >>> s = ps.Series([2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5])
        >>> s.groupby(s).rolling(3).min().sort_index()
        2  0     NaN
           1     NaN
        3  2     NaN
           3     NaN
           4     3.0
        4  5     NaN
           6     NaN
           7     4.0
           8     4.0
        5  9     NaN
           10    NaN
        dtype: float64

        For DataFrame, each rolling minimum is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.groupby(df.A).rolling(2).min().sort_index()  # doctest: +NORMALIZE_WHITESPACE
                 B
        A
        2 0    NaN
          1    4.0
        3 2    NaN
          3    9.0
          4    9.0
        4 5    NaN
          6   16.0
          7   16.0
          8   16.0
        5 9    NaN
          10  25.0
        '''
    def max(self) -> FrameLike:
        '''
        The rolling maximum of any non-NaN observations inside the window.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the rolling
            calculation.

        See Also
        --------
        pyspark.pandas.Series.rolling : Calling object with Series data.
        pyspark.pandas.DataFrame.rolling : Calling object with DataFrames.
        pyspark.pandas.Series.max : Max of the full Series.
        pyspark.pandas.DataFrame.max : Max of the full DataFrame.

        Examples
        --------
        >>> s = ps.Series([2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5])
        >>> s.groupby(s).rolling(3).max().sort_index()
        2  0     NaN
           1     NaN
        3  2     NaN
           3     NaN
           4     3.0
        4  5     NaN
           6     NaN
           7     4.0
           8     4.0
        5  9     NaN
           10    NaN
        dtype: float64

        For DataFrame, each rolling maximum is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.groupby(df.A).rolling(2).max().sort_index()  # doctest: +NORMALIZE_WHITESPACE
                 B
        A
        2 0    NaN
          1    4.0
        3 2    NaN
          3    9.0
          4    9.0
        4 5    NaN
          6   16.0
          7   16.0
          8   16.0
        5 9    NaN
          10  25.0
        '''
    def mean(self) -> FrameLike:
        '''
        The rolling mean of any non-NaN observations inside the window.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the rolling
            calculation.

        See Also
        --------
        pyspark.pandas.Series.rolling : Calling object with Series data.
        pyspark.pandas.DataFrame.rolling : Calling object with DataFrames.
        pyspark.pandas.Series.mean : Mean of the full Series.
        pyspark.pandas.DataFrame.mean : Mean of the full DataFrame.

        Examples
        --------
        >>> s = ps.Series([2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5])
        >>> s.groupby(s).rolling(3).mean().sort_index()
        2  0     NaN
           1     NaN
        3  2     NaN
           3     NaN
           4     3.0
        4  5     NaN
           6     NaN
           7     4.0
           8     4.0
        5  9     NaN
           10    NaN
        dtype: float64

        For DataFrame, each rolling mean is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.groupby(df.A).rolling(2).mean().sort_index()  # doctest: +NORMALIZE_WHITESPACE
                 B
        A
        2 0    NaN
          1    4.0
        3 2    NaN
          3    9.0
          4    9.0
        4 5    NaN
          6   16.0
          7   16.0
          8   16.0
        5 9    NaN
          10  25.0
        '''
    def quantile(self, quantile: float, accuracy: int = 10000) -> FrameLike:
        '''
        Calculate rolling quantile.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        quantile : float
            Value between 0 and 1 providing the quantile to compute.
        accuracy : int, optional
            Default accuracy of approximation. Larger value means better accuracy.
            The relative error can be deduced by 1.0 / accuracy.
            This is a panda-on-Spark specific parameter.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the rolling
            calculation.

        Notes
        -----
        `quantile` in pandas-on-Spark are using distributed percentile approximation
        algorithm unlike pandas, the result might be different with pandas, also `interpolation`
        parameter is not supported yet.

        See Also
        --------
        pyspark.pandas.Series.rolling : Calling rolling with Series data.
        pyspark.pandas.DataFrame.rolling : Calling rolling with DataFrames.
        pyspark.pandas.Series.quantile : Aggregating quantile for Series.
        pyspark.pandas.DataFrame.quantile : Aggregating quantile for DataFrame.

        Examples
        --------
        >>> s = ps.Series([2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5])
        >>> s.groupby(s).rolling(3).quantile(0.5).sort_index()
        2  0     NaN
           1     NaN
        3  2     NaN
           3     NaN
           4     3.0
        4  5     NaN
           6     NaN
           7     4.0
           8     4.0
        5  9     NaN
           10    NaN
        dtype: float64

        For DataFrame, each rolling quantile is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.groupby(df.A).rolling(2).quantile(0.5).sort_index()
                 B
        A
        2 0    NaN
          1    4.0
        3 2    NaN
          3    9.0
          4    9.0
        4 5    NaN
          6   16.0
          7   16.0
          8   16.0
        5 9    NaN
          10  25.0
        '''
    def std(self) -> FrameLike:
        """
        Calculate rolling standard deviation.

        Returns
        -------
        Series or DataFrame
            Returns the same object type as the caller of the rolling calculation.

        See Also
        --------
        pyspark.pandas.Series.rolling : Calling object with Series data.
        pyspark.pandas.DataFrame.rolling : Calling object with DataFrames.
        pyspark.pandas.Series.std : Equivalent method for Series.
        pyspark.pandas.DataFrame.std : Equivalent method for DataFrame.
        numpy.std : Equivalent method for Numpy array.
        """
    def var(self) -> FrameLike:
        """
        Calculate unbiased rolling variance.

        Returns
        -------
        Series or DataFrame
            Returns the same object type as the caller of the rolling calculation.

        See Also
        --------
        pyspark.pandas.Series.rolling : Calling object with Series data.
        pyspark.pandas.DataFrame.rolling : Calling object with DataFrames.
        pyspark.pandas.Series.var : Equivalent method for Series.
        pyspark.pandas.DataFrame.var : Equivalent method for DataFrame.
        numpy.var : Equivalent method for Numpy array.
        """
    def skew(self) -> FrameLike:
        """
        Calculate unbiased rolling skew.

        Returns
        -------
        Series or DataFrame
            Returns the same object type as the caller of the rolling calculation.

        See Also
        --------
        pyspark.pandas.Series.rolling : Calling object with Series data.
        pyspark.pandas.DataFrame.rolling : Calling object with DataFrames.
        pyspark.pandas.Series.std : Equivalent method for Series.
        pyspark.pandas.DataFrame.std : Equivalent method for DataFrame.
        numpy.std : Equivalent method for Numpy array.
        """
    def kurt(self) -> FrameLike:
        """
        Calculate unbiased rolling kurtosis.

        Returns
        -------
        Series or DataFrame
            Returns the same object type as the caller of the rolling calculation.

        See Also
        --------
        pyspark.pandas.Series.rolling : Calling object with Series data.
        pyspark.pandas.DataFrame.rolling : Calling object with DataFrames.
        pyspark.pandas.Series.var : Equivalent method for Series.
        pyspark.pandas.DataFrame.var : Equivalent method for DataFrame.
        numpy.var : Equivalent method for Numpy array.
        """

class ExpandingLike(RollingAndExpanding[FrameLike], metaclass=abc.ABCMeta):
    def __init__(self, min_periods: int = 1) -> None: ...
    def count(self) -> FrameLike: ...

class Expanding(ExpandingLike[FrameLike]):
    def __init__(self, psdf_or_psser: FrameLike, min_periods: int = 1) -> None: ...
    def __getattr__(self, item: str) -> Any: ...
    def count(self) -> FrameLike:
        '''
        The expanding count of any non-NaN observations inside the window.

        .. note:: the current implementation of this API uses Spark\'s Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the expanding
            calculation.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.count : Count of the full Series.
        pyspark.pandas.DataFrame.count : Count of the full DataFrame.

        Examples
        --------
        >>> s = ps.Series([2, 3, float("nan"), 10])
        >>> s.expanding().count()
        0    1.0
        1    2.0
        2    2.0
        3    3.0
        dtype: float64

        >>> s.to_frame().expanding().count()
             0
        0  1.0
        1  2.0
        2  2.0
        3  3.0
        '''
    def sum(self) -> FrameLike:
        '''
        Calculate expanding summation of given DataFrame or Series.

        .. note:: the current implementation of this API uses Spark\'s Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Same type as the input, with the same index, containing the
            expanding summation.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.sum : Reducing sum for Series.
        pyspark.pandas.DataFrame.sum : Reducing sum for DataFrame.

        Examples
        --------
        >>> s = ps.Series([1, 2, 3, 4, 5])
        >>> s
        0    1
        1    2
        2    3
        3    4
        4    5
        dtype: int64

        >>> s.expanding(3).sum()
        0     NaN
        1     NaN
        2     6.0
        3    10.0
        4    15.0
        dtype: float64

        For DataFrame, each expanding summation is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df
           A   B
        0  1   1
        1  2   4
        2  3   9
        3  4  16
        4  5  25

        >>> df.expanding(3).sum()
              A     B
        0   NaN   NaN
        1   NaN   NaN
        2   6.0  14.0
        3  10.0  30.0
        4  15.0  55.0
        '''
    def min(self) -> FrameLike:
        """
        Calculate the expanding minimum.

        .. note:: the current implementation of this API uses Spark's Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the expanding
            calculation.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with a Series.
        pyspark.pandas.DataFrame.expanding : Calling object with a DataFrame.
        pyspark.pandas.Series.min : Similar method for Series.
        pyspark.pandas.DataFrame.min : Similar method for DataFrame.

        Examples
        --------
        Performing a expanding minimum with a window size of 3.

        >>> s = ps.Series([4, 3, 5, 2, 6])
        >>> s.expanding(3).min()
        0    NaN
        1    NaN
        2    3.0
        3    2.0
        4    2.0
        dtype: float64
        """
    def max(self) -> FrameLike:
        """
        Calculate the expanding maximum.

        .. note:: the current implementation of this API uses Spark's Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Return type is determined by the caller.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.max : Similar method for Series.
        pyspark.pandas.DataFrame.max : Similar method for DataFrame.

        Examples
        --------
        Performing a expanding minimum with a window size of 3.

        >>> s = ps.Series([4, 3, 5, 2, 6])
        >>> s.expanding(3).max()
        0    NaN
        1    NaN
        2    5.0
        3    5.0
        4    6.0
        dtype: float64
        """
    def mean(self) -> FrameLike:
        """
        Calculate the expanding mean of the values.

        .. note:: the current implementation of this API uses Spark's Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the expanding
            calculation.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.mean : Equivalent method for Series.
        pyspark.pandas.DataFrame.mean : Equivalent method for DataFrame.

        Examples
        --------
        The below examples will show expanding mean calculations with window sizes of
        two and three, respectively.

        >>> s = ps.Series([1, 2, 3, 4])
        >>> s.expanding(2).mean()
        0    NaN
        1    1.5
        2    2.0
        3    2.5
        dtype: float64

        >>> s.expanding(3).mean()
        0    NaN
        1    NaN
        2    2.0
        3    2.5
        dtype: float64
        """
    def quantile(self, quantile: float, accuracy: int = 10000) -> FrameLike:
        """
        Calculate the expanding quantile of the values.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the expanding
            calculation.

        Parameters
        ----------
        quantile : float
            Value between 0 and 1 providing the quantile to compute.
        accuracy : int, optional
            Default accuracy of approximation. Larger value means better accuracy.
            The relative error can be deduced by 1.0 / accuracy.
            This is a panda-on-Spark specific parameter.

        Notes
        -----
        `quantile` in pandas-on-Spark are using distributed percentile approximation
        algorithm unlike pandas, the result might be different with pandas (the result is
        similar to the interpolation set to `lower`), also `interpolation` parameter is
        not supported yet.

        the current implementation of this API uses Spark's Window without
        specifying partition specification. This leads to move all data into
        single partition in single machine and could cause serious
        performance degradation. Avoid this method against very large dataset.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling expanding with Series data.
        pyspark.pandas.DataFrame.expanding : Calling expanding with DataFrames.
        pyspark.pandas.Series.quantile : Aggregating quantile for Series.
        pyspark.pandas.DataFrame.quantile : Aggregating quantile for DataFrame.

        Examples
        --------
        The below examples will show expanding quantile calculations with window sizes of
        two and three, respectively.

        >>> s = ps.Series([1, 2, 3, 4])
        >>> s.expanding(2).quantile(0.5)
        0    NaN
        1    1.0
        2    2.0
        3    2.0
        dtype: float64

        >>> s.expanding(3).quantile(0.5)
        0    NaN
        1    NaN
        2    2.0
        3    2.0
        dtype: float64
        """
    def std(self) -> FrameLike:
        '''
        Calculate expanding standard deviation.

        .. note:: the current implementation of this API uses Spark\'s Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Returns the same object type as the caller of the expanding calculation.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.std : Equivalent method for Series.
        pyspark.pandas.DataFrame.std : Equivalent method for DataFrame.
        numpy.std : Equivalent method for Numpy array.

        Examples
        --------
        >>> s = ps.Series([5, 5, 6, 7, 5, 5, 5])
        >>> s.expanding(3).std()
        0         NaN
        1         NaN
        2    0.577350
        3    0.957427
        4    0.894427
        5    0.836660
        6    0.786796
        dtype: float64

        For DataFrame, each expanding standard deviation variance is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.expanding(2).std()
                  A          B
        0       NaN        NaN
        1  0.000000   0.000000
        2  0.577350   6.350853
        3  0.957427  11.412712
        4  0.894427  10.630146
        5  0.836660   9.928075
        6  0.786796   9.327379
        '''
    def var(self) -> FrameLike:
        '''
        Calculate unbiased expanding variance.

        .. note:: the current implementation of this API uses Spark\'s Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Returns the same object type as the caller of the expanding calculation.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.var : Equivalent method for Series.
        pyspark.pandas.DataFrame.var : Equivalent method for DataFrame.
        numpy.var : Equivalent method for Numpy array.

        Examples
        --------
        >>> s = ps.Series([5, 5, 6, 7, 5, 5, 5])
        >>> s.expanding(3).var()
        0         NaN
        1         NaN
        2    0.333333
        3    0.916667
        4    0.800000
        5    0.700000
        6    0.619048
        dtype: float64

        For DataFrame, each unbiased expanding variance is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.expanding(2).var()
                  A           B
        0       NaN         NaN
        1  0.000000    0.000000
        2  0.333333   40.333333
        3  0.916667  130.250000
        4  0.800000  113.000000
        5  0.700000   98.566667
        6  0.619048   87.000000
        '''
    def skew(self) -> FrameLike:
        '''
        Calculate unbiased expanding skew.

        .. note:: the current implementation of this API uses Spark\'s Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Returns the same object type as the caller of the expanding calculation.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.std : Equivalent method for Series.
        pyspark.pandas.DataFrame.std : Equivalent method for DataFrame.
        numpy.std : Equivalent method for Numpy array.

        Examples
        --------
        >>> s = ps.Series([5, 5, 6, 7, 5, 1, 5, 9])
        >>> s.expanding(3).skew()
        0         NaN
        1         NaN
        2    1.732051
        3    0.854563
        4    1.257788
        5   -1.571593
        6   -1.657542
        7   -0.521760
        dtype: float64

        For DataFrame, each expanding standard deviation variance is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.expanding(5).skew()
                  A         B
        0       NaN       NaN
        1       NaN       NaN
        2       NaN       NaN
        3       NaN       NaN
        4  1.257788  1.369456
        5 -1.571593 -0.423309
        6 -1.657542 -0.355737
        7 -0.521760  1.116874
        '''
    def kurt(self) -> FrameLike:
        '''
        Calculate unbiased expanding kurtosis.

        .. note:: the current implementation of this API uses Spark\'s Window without
            specifying partition specification. This leads to move all data into
            single partition in single machine and could cause serious
            performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Returns the same object type as the caller of the expanding calculation.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.var : Equivalent method for Series.
        pyspark.pandas.DataFrame.var : Equivalent method for DataFrame.
        numpy.var : Equivalent method for Numpy array.

        Examples
        --------
        >>> s = ps.Series([5, 5, 6, 7, 5, 1, 5, 9])
        >>> s.expanding(4).kurt()
        0         NaN
        1         NaN
        2         NaN
        3   -1.289256
        4    0.312500
        5    3.419520
        6    4.028185
        7    2.230373
        dtype: float64

        For DataFrame, each unbiased expanding variance is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.expanding(5).kurt()
                  A         B
        0       NaN       NaN
        1       NaN       NaN
        2       NaN       NaN
        3       NaN       NaN
        4  0.312500  0.906336
        5  3.419520  1.486581
        6  4.028185  1.936169
        7  2.230373  2.273792
        '''

class ExpandingGroupby(ExpandingLike[FrameLike]):
    def __init__(self, groupby: GroupBy[FrameLike], min_periods: int = 1) -> None: ...
    def __getattr__(self, item: str) -> Any: ...
    def count(self) -> FrameLike:
        '''
        The expanding count of any non-NaN observations inside the window.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the expanding
            calculation.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.count : Count of the full Series.
        pyspark.pandas.DataFrame.count : Count of the full DataFrame.

        Examples
        --------
        >>> s = ps.Series([2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5])
        >>> s.groupby(s).expanding(3).count().sort_index()
        2  0     NaN
           1     NaN
        3  2     NaN
           3     NaN
           4     3.0
        4  5     NaN
           6     NaN
           7     3.0
           8     4.0
        5  9     NaN
           10    NaN
        dtype: float64

        For DataFrame, each expanding count is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.groupby(df.A).expanding(2).count().sort_index()  # doctest: +NORMALIZE_WHITESPACE
                B
        A
        2 0   NaN
          1   2.0
        3 2   NaN
          3   2.0
          4   3.0
        4 5   NaN
          6   2.0
          7   3.0
          8   4.0
        5 9   NaN
          10  2.0
        '''
    def sum(self) -> FrameLike:
        '''
        Calculate expanding summation of given DataFrame or Series.

        Returns
        -------
        Series or DataFrame
            Same type as the input, with the same index, containing the
            expanding summation.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.sum : Reducing sum for Series.
        pyspark.pandas.DataFrame.sum : Reducing sum for DataFrame.

        Examples
        --------
        >>> s = ps.Series([2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5])
        >>> s.groupby(s).expanding(3).sum().sort_index()
        2  0      NaN
           1      NaN
        3  2      NaN
           3      NaN
           4      9.0
        4  5      NaN
           6      NaN
           7     12.0
           8     16.0
        5  9      NaN
           10     NaN
        dtype: float64

        For DataFrame, each expanding summation is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.groupby(df.A).expanding(2).sum().sort_index()  # doctest: +NORMALIZE_WHITESPACE
                 B
        A
        2 0    NaN
          1    8.0
        3 2    NaN
          3   18.0
          4   27.0
        4 5    NaN
          6   32.0
          7   48.0
          8   64.0
        5 9    NaN
          10  50.0
        '''
    def min(self) -> FrameLike:
        '''
        Calculate the expanding minimum.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the expanding
            calculation.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with a Series.
        pyspark.pandas.DataFrame.expanding : Calling object with a DataFrame.
        pyspark.pandas.Series.min : Similar method for Series.
        pyspark.pandas.DataFrame.min : Similar method for DataFrame.

        Examples
        --------
        >>> s = ps.Series([2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5])
        >>> s.groupby(s).expanding(3).min().sort_index()
        2  0     NaN
           1     NaN
        3  2     NaN
           3     NaN
           4     3.0
        4  5     NaN
           6     NaN
           7     4.0
           8     4.0
        5  9     NaN
           10    NaN
        dtype: float64

        For DataFrame, each expanding minimum is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.groupby(df.A).expanding(2).min().sort_index()  # doctest: +NORMALIZE_WHITESPACE
                 B
        A
        2 0    NaN
          1    4.0
        3 2    NaN
          3    9.0
          4    9.0
        4 5    NaN
          6   16.0
          7   16.0
          8   16.0
        5 9    NaN
          10  25.0
        '''
    def max(self) -> FrameLike:
        '''
        Calculate the expanding maximum.

        Returns
        -------
        Series or DataFrame
            Return type is determined by the caller.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.max : Similar method for Series.
        pyspark.pandas.DataFrame.max : Similar method for DataFrame.

        Examples
        --------
        >>> s = ps.Series([2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5])
        >>> s.groupby(s).expanding(3).max().sort_index()
        2  0     NaN
           1     NaN
        3  2     NaN
           3     NaN
           4     3.0
        4  5     NaN
           6     NaN
           7     4.0
           8     4.0
        5  9     NaN
           10    NaN
        dtype: float64

        For DataFrame, each expanding maximum is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.groupby(df.A).expanding(2).max().sort_index()  # doctest: +NORMALIZE_WHITESPACE
                 B
        A
        2 0    NaN
          1    4.0
        3 2    NaN
          3    9.0
          4    9.0
        4 5    NaN
          6   16.0
          7   16.0
          8   16.0
        5 9    NaN
          10  25.0
        '''
    def mean(self) -> FrameLike:
        '''
        Calculate the expanding mean of the values.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the expanding
            calculation.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.mean : Equivalent method for Series.
        pyspark.pandas.DataFrame.mean : Equivalent method for DataFrame.

        Examples
        --------
        >>> s = ps.Series([2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5])
        >>> s.groupby(s).expanding(3).mean().sort_index()
        2  0     NaN
           1     NaN
        3  2     NaN
           3     NaN
           4     3.0
        4  5     NaN
           6     NaN
           7     4.0
           8     4.0
        5  9     NaN
           10    NaN
        dtype: float64

        For DataFrame, each expanding mean is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.groupby(df.A).expanding(2).mean().sort_index()  # doctest: +NORMALIZE_WHITESPACE
                 B
        A
        2 0    NaN
          1    4.0
        3 2    NaN
          3    9.0
          4    9.0
        4 5    NaN
          6   16.0
          7   16.0
          8   16.0
        5 9    NaN
          10  25.0
        '''
    def quantile(self, quantile: float, accuracy: int = 10000) -> FrameLike:
        '''
         Calculate the expanding quantile of the values.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        quantile : float
            Value between 0 and 1 providing the quantile to compute.
        accuracy : int, optional
            Default accuracy of approximation. Larger value means better accuracy.
            The relative error can be deduced by 1.0 / accuracy.
            This is a panda-on-Spark specific parameter.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the expanding
            calculation.

        Notes
        -----
        `quantile` in pandas-on-Spark are using distributed percentile approximation
        algorithm unlike pandas, the result might be different with pandas, also `interpolation`
        parameter is not supported yet.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling expanding with Series data.
        pyspark.pandas.DataFrame.expanding : Calling expanding with DataFrames.
        pyspark.pandas.Series.quantile : Aggregating quantile for Series.
        pyspark.pandas.DataFrame.quantile : Aggregating quantile for DataFrame.

        Examples
        --------
        >>> s = ps.Series([2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5])
        >>> s.groupby(s).expanding(3).quantile(0.5).sort_index()
        2  0     NaN
           1     NaN
        3  2     NaN
           3     NaN
           4     3.0
        4  5     NaN
           6     NaN
           7     4.0
           8     4.0
        5  9     NaN
           10    NaN
        dtype: float64

        For DataFrame, each expanding quantile is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.groupby(df.A).expanding(2).quantile(0.5).sort_index()
                 B
        A
        2 0    NaN
          1    4.0
        3 2    NaN
          3    9.0
          4    9.0
        4 5    NaN
          6   16.0
          7   16.0
          8   16.0
        5 9    NaN
          10  25.0
        '''
    def std(self) -> FrameLike:
        """
        Calculate expanding standard deviation.


        Returns
        -------
        Series or DataFrame
            Returns the same object type as the caller of the expanding calculation.

        See Also
        --------
        pyspark.pandas.Series.expanding: Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.std : Equivalent method for Series.
        pyspark.pandas.DataFrame.std : Equivalent method for DataFrame.
        numpy.std : Equivalent method for Numpy array.
        """
    def var(self) -> FrameLike:
        """
        Calculate unbiased expanding variance.

        Returns
        -------
        Series or DataFrame
            Returns the same object type as the caller of the expanding calculation.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.var : Equivalent method for Series.
        pyspark.pandas.DataFrame.var : Equivalent method for DataFrame.
        numpy.var : Equivalent method for Numpy array.
        """
    def skew(self) -> FrameLike:
        """
        Calculate expanding standard skew.


        Returns
        -------
        Series or DataFrame
            Returns the same object type as the caller of the expanding calculation.

        See Also
        --------
        pyspark.pandas.Series.expanding: Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.std : Equivalent method for Series.
        pyspark.pandas.DataFrame.std : Equivalent method for DataFrame.
        numpy.std : Equivalent method for Numpy array.
        """
    def kurt(self) -> FrameLike:
        """
        Calculate unbiased expanding kurtosis.

        Returns
        -------
        Series or DataFrame
            Returns the same object type as the caller of the expanding calculation.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.var : Equivalent method for Series.
        pyspark.pandas.DataFrame.var : Equivalent method for DataFrame.
        numpy.var : Equivalent method for Numpy array.
        """

class ExponentialMovingLike(Generic[FrameLike], metaclass=ABCMeta):
    def __init__(self, window: WindowSpec, com: float | None = None, span: float | None = None, halflife: float | None = None, alpha: float | None = None, min_periods: int | None = None, ignore_na: bool = False) -> None: ...
    def mean(self) -> FrameLike: ...

class ExponentialMoving(ExponentialMovingLike[FrameLike]):
    def __init__(self, psdf_or_psser: FrameLike, com: float | None = None, span: float | None = None, halflife: float | None = None, alpha: float | None = None, min_periods: int | None = None, ignore_na: bool = False) -> None: ...
    def __getattr__(self, item: str) -> Any: ...
    def mean(self) -> FrameLike:
        """
        Calculate an online exponentially weighted mean.

        Notes
        -----
        There are behavior differences between pandas-on-Spark and pandas.

        * the current implementation of this API uses Spark's Window without
          specifying partition specification. This leads to move all data into
          single partition in single machine and could cause serious
          performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the exponentially
            calculation.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.mean : Equivalent method for Series.
        pyspark.pandas.DataFrame.mean : Equivalent method for DataFrame.

        Examples
        --------
        The below examples will show computing exponentially weighted moving average.

        >>> df = ps.DataFrame({'s1': [.2, .0, .6, .2, .4, .5, .6], 's2': [2, 1, 3, 1, 0, 0, 0]})
        >>> df.ewm(com=0.1).mean()
                 s1        s2
        0  0.200000  2.000000
        1  0.016667  1.083333
        2  0.547368  2.827068
        3  0.231557  1.165984
        4  0.384688  0.105992
        5  0.489517  0.009636
        6  0.589956  0.000876

        >>> df.s2.ewm(halflife=1.5, min_periods=3).mean()
        0         NaN
        1         NaN
        2    2.182572
        3    1.663174
        4    0.979949
        5    0.593155
        6    0.364668
        Name: s2, dtype: float64
        """

class ExponentialMovingGroupby(ExponentialMovingLike[FrameLike]):
    def __init__(self, groupby: GroupBy[FrameLike], com: float | None = None, span: float | None = None, halflife: float | None = None, alpha: float | None = None, min_periods: int | None = None, ignore_na: bool = False) -> None: ...
    def __getattr__(self, item: str) -> Any: ...
    def mean(self) -> FrameLike:
        '''
        Calculate an online exponentially weighted mean.

        Notes
        -----
        There are behavior differences between pandas-on-Spark and pandas.

        * the current implementation of this API uses Spark\'s Window without
          specifying partition specification. This leads to move all data into
          single partition in single machine and could cause serious
          performance degradation. Avoid this method against very large dataset.

        Returns
        -------
        Series or DataFrame
            Returned object type is determined by the caller of the exponentially
            calculation.

        See Also
        --------
        pyspark.pandas.Series.expanding : Calling object with Series data.
        pyspark.pandas.DataFrame.expanding : Calling object with DataFrames.
        pyspark.pandas.Series.mean : Equivalent method for Series.
        pyspark.pandas.DataFrame.mean : Equivalent method for DataFrame.

        Examples
        --------
        >>> s = ps.Series([2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5])
        >>> s.groupby(s).ewm(alpha=0.5).mean().sort_index()
        2  0     2.0
           1     2.0
        3  2     3.0
           3     3.0
           4     3.0
        4  5     4.0
           6     4.0
           7     4.0
           8     4.0
        5  9     5.0
           10    5.0
        dtype: float64

        For DataFrame, each ewm mean is computed column-wise.

        >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
        >>> df.groupby(df.A).ewm(alpha=0.5).mean().sort_index()  # doctest: +NORMALIZE_WHITESPACE
                 B
        A
        2 0    4.0
          1    4.0
        3 2    9.0
          3    9.0
          4    9.0
        4 5   16.0
          6   16.0
          7   16.0
          8   16.0
        5 9   25.0
          10  25.0
        '''
