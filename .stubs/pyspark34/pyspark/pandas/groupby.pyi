import pandas as pd
from _typeshed import Incomplete
from abc import ABCMeta
from pyspark.pandas._typing import Axis as Axis, FrameLike as FrameLike, Label as Label, Name as Name
from pyspark.pandas.config import get_option as get_option
from pyspark.pandas.exceptions import DataError as DataError
from pyspark.pandas.frame import DataFrame as DataFrame
from pyspark.pandas.internal import HIDDEN_COLUMNS as HIDDEN_COLUMNS, InternalField as InternalField, InternalFrame as InternalFrame, NATURAL_ORDER_COLUMN_NAME as NATURAL_ORDER_COLUMN_NAME, SPARK_DEFAULT_SERIES_NAME as SPARK_DEFAULT_SERIES_NAME, SPARK_INDEX_NAME_FORMAT as SPARK_INDEX_NAME_FORMAT, SPARK_INDEX_NAME_PATTERN as SPARK_INDEX_NAME_PATTERN
from pyspark.pandas.missing.groupby import MissingPandasLikeDataFrameGroupBy as MissingPandasLikeDataFrameGroupBy, MissingPandasLikeSeriesGroupBy as MissingPandasLikeSeriesGroupBy
from pyspark.pandas.series import Series as Series, first_series as first_series
from pyspark.pandas.spark.utils import as_nullable_spark_type as as_nullable_spark_type, force_decimal_precision_scale as force_decimal_precision_scale
from pyspark.pandas.typedef import DataFrameType as DataFrameType, ScalarType as ScalarType, SeriesType as SeriesType, infer_return_type as infer_return_type
from pyspark.pandas.utils import align_diff_frames as align_diff_frames, is_name_like_tuple as is_name_like_tuple, is_name_like_value as is_name_like_value, log_advice as log_advice, name_like_string as name_like_string, same_anchor as same_anchor, scol_for as scol_for, verify_temp_column_name as verify_temp_column_name
from pyspark.pandas.window import ExpandingGroupby as ExpandingGroupby, ExponentialMovingGroupby as ExponentialMovingGroupby, RollingGroupby as RollingGroupby
from pyspark.sql import Column as Column, Window as Window
from pyspark.sql.types import BooleanType as BooleanType, DataType as DataType, DoubleType as DoubleType, NumericType as NumericType, StringType as StringType, StructField as StructField, StructType as StructType
from typing import Any, Callable, Dict, Generic, List, NamedTuple, Set, Tuple

class NamedAgg(NamedTuple):
    column: Incomplete
    aggfunc: Incomplete

class GroupBy(Generic[FrameLike], metaclass=ABCMeta):
    """
    :ivar _psdf: The parent dataframe that is used to perform the groupby
    :type _psdf: DataFrame
    :ivar _groupkeys: The list of keys that will be used to perform the grouping
    :type _groupkeys: List[Series]
    """
    def __init__(self, psdf: DataFrame, groupkeys: List[Series], as_index: bool, dropna: bool, column_labels_to_exclude: Set[Label], agg_columns_selected: bool, agg_columns: List[Series]) -> None: ...
    def aggregate(self, func_or_funcs: str | List[str] | Dict[Name, str | List[str]] | None = None, *args: Any, **kwargs: Any) -> DataFrame:
        """Aggregate using one or more operations over the specified axis.

        Parameters
        ----------
        func_or_funcs : dict, str or list
             a dict mapping from column name (string) to
             aggregate functions (string or list of strings).

        Returns
        -------
        Series or DataFrame

            The return can be:

            * Series : when DataFrame.agg is called with a single function
            * DataFrame : when DataFrame.agg is called with several functions

            Return Series or DataFrame.

        Notes
        -----
        `agg` is an alias for `aggregate`. Use the alias.

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> df = ps.DataFrame({'A': [1, 1, 2, 2],
        ...                    'B': [1, 2, 3, 4],
        ...                    'C': [0.362, 0.227, 1.267, -0.562]},
        ...                   columns=['A', 'B', 'C'])

        >>> df
           A  B      C
        0  1  1  0.362
        1  1  2  0.227
        2  2  3  1.267
        3  2  4 -0.562

        Different aggregations per column

        >>> aggregated = df.groupby('A').agg({'B': 'min', 'C': 'sum'})
        >>> aggregated[['B', 'C']].sort_index()  # doctest: +NORMALIZE_WHITESPACE
           B      C
        A
        1  1  0.589
        2  3  0.705

        >>> aggregated = df.groupby('A').agg({'B': ['min', 'max']})
        >>> aggregated.sort_index()  # doctest: +NORMALIZE_WHITESPACE
             B
           min  max
        A
        1    1    2
        2    3    4

        >>> aggregated = df.groupby('A').agg('min')
        >>> aggregated.sort_index()  # doctest: +NORMALIZE_WHITESPACE
             B      C
        A
        1    1  0.227
        2    3 -0.562

        >>> aggregated = df.groupby('A').agg(['min', 'max'])
        >>> aggregated.sort_index()  # doctest: +NORMALIZE_WHITESPACE
             B           C
           min  max    min    max
        A
        1    1    2  0.227  0.362
        2    3    4 -0.562  1.267

        To control the output names with different aggregations per column, pandas-on-Spark
        also supports 'named aggregation' or nested renaming in .agg. It can also be
        used when applying multiple aggregation functions to specific columns.

        >>> aggregated = df.groupby('A').agg(b_max=ps.NamedAgg(column='B', aggfunc='max'))
        >>> aggregated.sort_index()  # doctest: +NORMALIZE_WHITESPACE
             b_max
        A
        1        2
        2        4

        >>> aggregated = df.groupby('A').agg(b_max=('B', 'max'), b_min=('B', 'min'))
        >>> aggregated.sort_index()  # doctest: +NORMALIZE_WHITESPACE
             b_max   b_min
        A
        1        2       1
        2        4       3

        >>> aggregated = df.groupby('A').agg(b_max=('B', 'max'), c_min=('C', 'min'))
        >>> aggregated.sort_index()  # doctest: +NORMALIZE_WHITESPACE
             b_max   c_min
        A
        1        2   0.227
        2        4  -0.562
        """
    agg = aggregate
    def count(self) -> FrameLike:
        """
        Compute count of group, excluding missing values.

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> df = ps.DataFrame({'A': [1, 1, 2, 1, 2],
        ...                    'B': [np.nan, 2, 3, 4, 5],
        ...                    'C': [1, 2, 1, 1, 2]}, columns=['A', 'B', 'C'])
        >>> df.groupby('A').count().sort_index()  # doctest: +NORMALIZE_WHITESPACE
            B  C
        A
        1  2  3
        2  2  2
        """
    def first(self, numeric_only: bool | None = False, min_count: int = -1) -> FrameLike:
        '''
        Compute first of group values.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        numeric_only : bool, default False
            Include only float, int, boolean columns. If None, will attempt to use
            everything, then use only numeric data.

            .. versionadded:: 3.4.0
        min_count : int, default -1
            The required number of valid values to perform the operation. If fewer
            than ``min_count`` non-NA values are present the result will be NA.

            .. versionadded:: 3.4.0

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> df = ps.DataFrame({"A": [1, 2, 1, 2], "B": [True, False, False, True],
        ...                    "C": [3, 3, 4, 4], "D": ["a", "b", "a", "a"]})
        >>> df
           A      B  C  D
        0  1   True  3  a
        1  2  False  3  b
        2  1  False  4  a
        3  2   True  4  a

        >>> df.groupby("A").first().sort_index()
               B  C  D
        A
        1   True  3  a
        2  False  3  b

        Include only float, int, boolean columns when set numeric_only True.

        >>> df.groupby("A").first(numeric_only=True).sort_index()
               B  C
        A
        1   True  3
        2  False  3

        >>> df.groupby("D").first().sort_index()
           A      B  C
        D
        a  1   True  3
        b  2  False  3

        >>> df.groupby("D").first(min_count=3).sort_index()
             A     B    C
        D
        a  1.0  True  3.0
        b  NaN  None  NaN
        '''
    def last(self, numeric_only: bool | None = False, min_count: int = -1) -> FrameLike:
        '''
        Compute last of group values.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        numeric_only : bool, default False
            Include only float, int, boolean columns. If None, will attempt to use
            everything, then use only numeric data.

            .. versionadded:: 3.4.0
        min_count : int, default -1
            The required number of valid values to perform the operation. If fewer
            than ``min_count`` non-NA values are present the result will be NA.

            .. versionadded:: 3.4.0

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> df = ps.DataFrame({"A": [1, 2, 1, 2], "B": [True, False, False, True],
        ...                    "C": [3, 3, 4, 4], "D": ["a", "a", "b", "a"]})
        >>> df
           A      B  C  D
        0  1   True  3  a
        1  2  False  3  a
        2  1  False  4  b
        3  2   True  4  a

        >>> df.groupby("A").last().sort_index()
               B  C  D
        A
        1  False  4  b
        2   True  4  a

        Include only float, int, boolean columns when set numeric_only True.

        >>> df.groupby("A").last(numeric_only=True).sort_index()
               B  C
        A
        1  False  4
        2   True  4

        >>> df.groupby("D").last().sort_index()
           A      B  C
        D
        a  2   True  4
        b  1  False  4

        >>> df.groupby("D").last(min_count=3).sort_index()
             A     B    C
        D
        a  2.0  True  4.0
        b  NaN  None  NaN
        '''
    def max(self, numeric_only: bool | None = False, min_count: int = -1) -> FrameLike:
        '''
        Compute max of group values.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        numeric_only : bool, default False
            Include only float, int, boolean columns. If None, will attempt to use
            everything, then use only numeric data.

            .. versionadded:: 3.4.0
        min_count : bool, default -1
            The required number of valid values to perform the operation. If fewer
            than min_count non-NA values are present the result will be NA.

            .. versionadded:: 3.4.0

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> df = ps.DataFrame({"A": [1, 2, 1, 2], "B": [True, False, False, True],
        ...                    "C": [3, 4, 3, 4], "D": ["a", "a", "b", "a"]})

        >>> df.groupby("A").max().sort_index()
              B  C  D
        A
        1  True  3  b
        2  True  4  a

        Include only float, int, boolean columns when set numeric_only True.

        >>> df.groupby("A").max(numeric_only=True).sort_index()
              B  C
        A
        1  True  3
        2  True  4

        >>> df.groupby("D").max().sort_index()
           A      B  C
        D
        a  2   True  4
        b  1  False  3

        >>> df.groupby("D").max(min_count=3).sort_index()
             A     B    C
        D
        a  2.0  True  4.0
        b  NaN  None  NaN
        '''
    def mean(self, numeric_only: bool | None = True) -> FrameLike:
        """
        Compute mean of groups, excluding missing values.

        Parameters
        ----------
        numeric_only : bool, default False
            Include only float, int, boolean columns. If None, will attempt to use
            everything, then use only numeric data.

            .. versionadded:: 3.4.0

        Returns
        -------
        pyspark.pandas.Series or pyspark.pandas.DataFrame

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> df = ps.DataFrame({'A': [1, 1, 2, 1, 2],
        ...                    'B': [np.nan, 2, 3, 4, 5],
        ...                    'C': [1, 2, 1, 1, 2],
        ...                    'D': [True, False, True, False, True]})

        Groupby one column and return the mean of the remaining columns in
        each group.

        >>> df.groupby('A').mean().sort_index()  # doctest: +NORMALIZE_WHITESPACE
             B         C         D
        A
        1  3.0  1.333333  0.333333
        2  4.0  1.500000  1.000000
        """
    def quantile(self, q: float = 0.5, accuracy: int = 10000) -> FrameLike:
        """
        Return group values at the given quantile.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        q : float, default 0.5 (50% quantile)
            Value between 0 and 1 providing the quantile to compute.
        accuracy : int, optional
            Default accuracy of approximation. Larger value means better accuracy.
            The relative error can be deduced by 1.0 / accuracy.
            This is a panda-on-Spark specific parameter.

        Returns
        -------
        pyspark.pandas.Series or pyspark.pandas.DataFrame
            Return type determined by caller of GroupBy object.

        Notes
        -----
        `quantile` in pandas-on-Spark are using distributed percentile approximation
        algorithm unlike pandas, the result might be different with pandas, also
        `interpolation` parameter is not supported yet.

        See Also
        --------
        pyspark.pandas.Series.quantile
        pyspark.pandas.DataFrame.quantile
        pyspark.sql.functions.percentile_approx

        Examples
        --------
        >>> df = ps.DataFrame([
        ...     ['a', 1], ['a', 2], ['a', 3],
        ...     ['b', 1], ['b', 3], ['b', 5]
        ... ], columns=['key', 'val'])

        Groupby one column and return the quantile of the remaining columns in
        each group.

        >>> df.groupby('key').quantile()
             val
        key
        a    2.0
        b    3.0
        """
    def min(self, numeric_only: bool | None = False, min_count: int = -1) -> FrameLike:
        '''
        Compute min of group values.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        numeric_only : bool, default False
            Include only float, int, boolean columns. If None, will attempt to use
            everything, then use only numeric data.

            .. versionadded:: 3.4.0
        min_count : bool, default -1
            The required number of valid values to perform the operation. If fewer
            than min_count non-NA values are present the result will be NA.

            .. versionadded:: 3.4.0

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> df = ps.DataFrame({"A": [1, 2, 1, 2], "B": [True, False, False, True],
        ...                    "C": [3, 4, 3, 4], "D": ["a", "a", "b", "a"]})
        >>> df.groupby("A").min().sort_index()
               B  C  D
        A
        1  False  3  a
        2  False  4  a

        Include only float, int, boolean columns when set numeric_only True.

        >>> df.groupby("A").min(numeric_only=True).sort_index()
               B  C
        A
        1  False  3
        2  False  4

        >>> df.groupby("D").min().sort_index()
           A      B  C
        D
        a  1  False  3
        b  1  False  3


        >>> df.groupby("D").min(min_count=3).sort_index()
             A      B    C
        D
        a  1.0  False  3.0
        b  NaN   None  NaN
        '''
    def std(self, ddof: int = 1) -> FrameLike:
        '''
        Compute standard deviation of groups, excluding missing values.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        ddof : int, default 1
            Delta Degrees of Freedom. The divisor used in calculations is N - ddof,
            where N represents the number of elements.

            .. versionchanged:: 3.4.0
               Supported including arbitary integers.

        Examples
        --------
        >>> df = ps.DataFrame({"A": [1, 2, 1, 2], "B": [True, False, False, True],
        ...                    "C": [3, 4, 3, 4], "D": ["a", "b", "b", "a"]})

        >>> df.groupby("A").std()
                  B    C
        A
        1  0.707107  0.0
        2  0.707107  0.0

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby
        '''
    def sum(self, numeric_only: bool | None = True, min_count: int = 0) -> FrameLike:
        '''
        Compute sum of group values

        .. versionadded:: 3.3.0

        Parameters
        ----------
        numeric_only : bool, default False
            Include only float, int, boolean columns. If None, will attempt to use
            everything, then use only numeric data.
            It takes no effect since only numeric columns can be support here.

            .. versionadded:: 3.4.0
        min_count : int, default 0
            The required number of valid values to perform the operation.
            If fewer than min_count non-NA values are present the result will be NA.

            .. versionadded:: 3.4.0

        Examples
        --------
        >>> df = ps.DataFrame({"A": [1, 2, 1, 2], "B": [True, False, False, True],
        ...                    "C": [3, 4, 3, 4], "D": ["a", "a", "b", "a"]})

        >>> df.groupby("A").sum().sort_index()
           B  C
        A
        1  1  6
        2  1  8

        >>> df.groupby("D").sum().sort_index()
           A  B   C
        D
        a  5  2  11
        b  1  0   3

        >>> df.groupby("D").sum(min_count=3).sort_index()
             A    B     C
        D
        a  5.0  2.0  11.0
        b  NaN  NaN   NaN

        Notes
        -----
        There is a behavior difference between pandas-on-Spark and pandas:

        * when there is a non-numeric aggregation column, it will be ignored
            even if `numeric_only` is False.

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby
        '''
    def var(self, ddof: int = 1) -> FrameLike:
        '''
        Compute variance of groups, excluding missing values.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        ddof : int, default 1
            Delta Degrees of Freedom. The divisor used in calculations is N - ddof,
            where N represents the number of elements.

            .. versionchanged:: 3.4.0
               Supported including arbitary integers.

        Examples
        --------
        >>> df = ps.DataFrame({"A": [1, 2, 1, 2], "B": [True, False, False, True],
        ...                    "C": [3, 4, 3, 4], "D": ["a", "b", "b", "a"]})

        >>> df.groupby("A").var()
             B    C
        A
        1  0.5  0.0
        2  0.5  0.0

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby
        '''
    def skew(self) -> FrameLike:
        '''
        Compute skewness of groups, excluding missing values.

        .. versionadded:: 3.4.0

        Examples
        --------
        >>> df = ps.DataFrame({"A": [1, 2, 1, 1], "B": [True, False, False, True],
        ...                    "C": [3, 4, 3, 4], "D": ["a", "b", "b", "a"]})

        >>> df.groupby("A").skew()
                  B         C
        A
        1 -1.732051  1.732051
        2       NaN       NaN

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby
        '''
    def mad(self) -> FrameLike:
        '''
        Compute mean absolute deviation of groups, excluding missing values.

        .. versionadded:: 3.4.0

        .. deprecated:: 3.4.0

        Examples
        --------
        >>> df = ps.DataFrame({"A": [1, 2, 1, 1], "B": [True, False, False, True],
        ...                    "C": [3, 4, 3, 4], "D": ["a", "b", "b", "a"]})

        >>> df.groupby("A").mad()
                  B         C
        A
        1  0.444444  0.444444
        2  0.000000  0.000000

        >>> df.B.groupby(df.A).mad()
        A
        1    0.444444
        2    0.000000
        Name: B, dtype: float64

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby
        '''
    def sem(self, ddof: int = 1) -> FrameLike:
        '''
        Compute standard error of the mean of groups, excluding missing values.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        ddof : int, default 1
            Delta Degrees of Freedom. The divisor used in calculations is N - ddof,
            where N represents the number of elements.

        Examples
        --------
        >>> df = ps.DataFrame({"A": [1, 2, 1, 1], "B": [True, False, False, True],
        ...                    "C": [3, None, 3, 4], "D": ["a", "b", "b", "a"]})

        >>> df.groupby("A").sem()
                  B         C
        A
        1  0.333333  0.333333
        2       NaN       NaN

        >>> df.groupby("D").sem(ddof=1)
             A    B    C
        D
        a  0.0  0.0  0.5
        b  0.5  0.0  NaN

        >>> df.B.groupby(df.A).sem()
        A
        1    0.333333
        2         NaN
        Name: B, dtype: float64

        See Also
        --------
        pyspark.pandas.Series.sem
        pyspark.pandas.DataFrame.sem
        '''
    def nth(self, n: int) -> FrameLike:
        """
        Take the nth row from each group.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        n : int
            A single nth value for the row

        Returns
        -------
        Series or DataFrame

        Notes
        -----
        There is a behavior difference between pandas-on-Spark and pandas:

        * when there is no aggregation column, and `n` not equal to 0 or -1,
            the returned empty dataframe may have an index with different lenght `__len__`.

        Examples
        --------
        >>> df = ps.DataFrame({'A': [1, 1, 2, 1, 2],
        ...                    'B': [np.nan, 2, 3, 4, 5]}, columns=['A', 'B'])
        >>> g = df.groupby('A')
        >>> g.nth(0)
             B
        A
        1  NaN
        2  3.0
        >>> g.nth(1)
             B
        A
        1  2.0
        2  5.0
        >>> g.nth(-1)
             B
        A
        1  4.0
        2  5.0

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby
        """
    def prod(self, numeric_only: bool | None = True, min_count: int = 0) -> FrameLike:
        '''
        Compute prod of groups.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        numeric_only : bool, default False
            Include only float, int, boolean columns. If None, will attempt to use
            everything, then use only numeric data.

        min_count : int, default 0
            The required number of valid values to perform the operation.
            If fewer than min_count non-NA values are present the result will be NA.

        Returns
        -------
        Series or DataFrame
            Computed prod of values within each group.

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> import numpy as np
        >>> df = ps.DataFrame(
        ...     {
        ...         "A": [1, 1, 2, 1, 2],
        ...         "B": [np.nan, 2, 3, 4, 5],
        ...         "C": [1, 2, 1, 1, 2],
        ...         "D": [True, False, True, False, True],
        ...     }
        ... )

        Groupby one column and return the prod of the remaining columns in
        each group.

        >>> df.groupby(\'A\').prod().sort_index()
             B  C  D
        A
        1  8.0  2  0
        2  15.0 2  1

        >>> df.groupby(\'A\').prod(min_count=3).sort_index()
             B  C   D
        A
        1  NaN  2.0  0.0
        2  NaN NaN  NaN
        '''
    def all(self, skipna: bool = True) -> FrameLike:
        """
        Returns True if all values in the group are truthful, else False.

        Parameters
        ----------
        skipna : bool, default True
            Flag to ignore NA(nan/null) values during truth testing.

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> df = ps.DataFrame({'A': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
        ...                    'B': [True, True, True, False, False,
        ...                          False, None, True, None, False]},
        ...                   columns=['A', 'B'])
        >>> df
           A      B
        0  1   True
        1  1   True
        2  2   True
        3  2  False
        4  3  False
        5  3  False
        6  4   None
        7  4   True
        8  5   None
        9  5  False

        >>> df.groupby('A').all().sort_index()  # doctest: +NORMALIZE_WHITESPACE
               B
        A
        1   True
        2  False
        3  False
        4   True
        5  False

        >>> df.groupby('A').all(skipna=False).sort_index()  # doctest: +NORMALIZE_WHITESPACE
               B
        A
        1   True
        2  False
        3  False
        4  False
        5  False
        """
    def any(self) -> FrameLike:
        """
        Returns True if any value in the group is truthful, else False.

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> df = ps.DataFrame({'A': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
        ...                    'B': [True, True, True, False, False,
        ...                          False, None, True, None, False]},
        ...                   columns=['A', 'B'])
        >>> df
           A      B
        0  1   True
        1  1   True
        2  2   True
        3  2  False
        4  3  False
        5  3  False
        6  4   None
        7  4   True
        8  5   None
        9  5  False

        >>> df.groupby('A').any().sort_index()  # doctest: +NORMALIZE_WHITESPACE
               B
        A
        1   True
        2   True
        3  False
        4   True
        5  False
        """
    def size(self) -> Series:
        """
        Compute group sizes.

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> df = ps.DataFrame({'A': [1, 2, 2, 3, 3, 3],
        ...                    'B': [1, 1, 2, 3, 3, 3]},
        ...                   columns=['A', 'B'])
        >>> df
           A  B
        0  1  1
        1  2  1
        2  2  2
        3  3  3
        4  3  3
        5  3  3

        >>> df.groupby('A').size().sort_index()
        A
        1    1
        2    2
        3    3
        dtype: int64

        >>> df.groupby(['A', 'B']).size().sort_index()
        A  B
        1  1    1
        2  1    1
           2    1
        3  3    3
        dtype: int64

        For Series,

        >>> df.B.groupby(df.A).size().sort_index()
        A
        1    1
        2    2
        3    3
        Name: B, dtype: int64

        >>> df.groupby(df.A).B.size().sort_index()
        A
        1    1
        2    2
        3    3
        Name: B, dtype: int64
        """
    def diff(self, periods: int = 1) -> FrameLike:
        """
        First discrete difference of element.

        Calculates the difference of a DataFrame element compared with another element in the
        DataFrame group (default is the element in the same column of the previous row).

        Parameters
        ----------
        periods : int, default 1
            Periods to shift for calculating difference, accepts negative values.

        Returns
        -------
        diffed : DataFrame or Series

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> df = ps.DataFrame({'a': [1, 2, 3, 4, 5, 6],
        ...                    'b': [1, 1, 2, 3, 5, 8],
        ...                    'c': [1, 4, 9, 16, 25, 36]}, columns=['a', 'b', 'c'])
        >>> df
           a  b   c
        0  1  1   1
        1  2  1   4
        2  3  2   9
        3  4  3  16
        4  5  5  25
        5  6  8  36

        >>> df.groupby(['b']).diff().sort_index()
             a    c
        0  NaN  NaN
        1  1.0  3.0
        2  NaN  NaN
        3  NaN  NaN
        4  NaN  NaN
        5  NaN  NaN

        Difference with previous column in a group.

        >>> df.groupby(['b'])['a'].diff().sort_index()
        0    NaN
        1    1.0
        2    NaN
        3    NaN
        4    NaN
        5    NaN
        Name: a, dtype: float64
        """
    def cumcount(self, ascending: bool = True) -> Series:
        """
        Number each item in each group from 0 to the length of that group - 1.

        Essentially this is equivalent to

        .. code-block:: python

            self.apply(lambda x: pd.Series(np.arange(len(x)), x.index))

        Parameters
        ----------
        ascending : bool, default True
            If False, number in reverse, from length of group - 1 to 0.

        Returns
        -------
        Series
            Sequence number of each element within each group.

        Examples
        --------

        >>> df = ps.DataFrame([['a'], ['a'], ['a'], ['b'], ['b'], ['a']],
        ...                   columns=['A'])
        >>> df
           A
        0  a
        1  a
        2  a
        3  b
        4  b
        5  a
        >>> df.groupby('A').cumcount().sort_index()
        0    0
        1    1
        2    2
        3    0
        4    1
        5    3
        dtype: int64
        >>> df.groupby('A').cumcount(ascending=False).sort_index()
        0    3
        1    2
        2    1
        3    1
        4    0
        5    0
        dtype: int64
        """
    def cummax(self) -> FrameLike:
        '''
        Cumulative max for each group.

        Returns
        -------
        Series or DataFrame

        See Also
        --------
        Series.cummax
        DataFrame.cummax

        Examples
        --------
        >>> df = ps.DataFrame(
        ...     [[1, None, 4], [1, 0.1, 3], [1, 20.0, 2], [4, 10.0, 1]],
        ...     columns=list(\'ABC\'))
        >>> df
           A     B  C
        0  1   NaN  4
        1  1   0.1  3
        2  1  20.0  2
        3  4  10.0  1

        By default, iterates over rows and finds the sum in each column.

        >>> df.groupby("A").cummax().sort_index()
              B  C
        0   NaN  4
        1   0.1  4
        2  20.0  4
        3  10.0  1

        It works as below in Series.

        >>> df.C.groupby(df.A).cummax().sort_index()
        0    4
        1    4
        2    4
        3    1
        Name: C, dtype: int64
        '''
    def cummin(self) -> FrameLike:
        '''
        Cumulative min for each group.

        Returns
        -------
        Series or DataFrame

        See Also
        --------
        Series.cummin
        DataFrame.cummin

        Examples
        --------
        >>> df = ps.DataFrame(
        ...     [[1, None, 4], [1, 0.1, 3], [1, 20.0, 2], [4, 10.0, 1]],
        ...     columns=list(\'ABC\'))
        >>> df
           A     B  C
        0  1   NaN  4
        1  1   0.1  3
        2  1  20.0  2
        3  4  10.0  1

        By default, iterates over rows and finds the sum in each column.

        >>> df.groupby("A").cummin().sort_index()
              B  C
        0   NaN  4
        1   0.1  3
        2   0.1  2
        3  10.0  1

        It works as below in Series.

        >>> df.B.groupby(df.A).cummin().sort_index()
        0     NaN
        1     0.1
        2     0.1
        3    10.0
        Name: B, dtype: float64
        '''
    def cumprod(self) -> FrameLike:
        '''
        Cumulative product for each group.

        Returns
        -------
        Series or DataFrame

        See Also
        --------
        Series.cumprod
        DataFrame.cumprod

        Examples
        --------
        >>> df = ps.DataFrame(
        ...     [[1, None, 4], [1, 0.1, 3], [1, 20.0, 2], [4, 10.0, 1]],
        ...     columns=list(\'ABC\'))
        >>> df
           A     B  C
        0  1   NaN  4
        1  1   0.1  3
        2  1  20.0  2
        3  4  10.0  1

        By default, iterates over rows and finds the sum in each column.

        >>> df.groupby("A").cumprod().sort_index()
              B   C
        0   NaN   4
        1   0.1  12
        2   2.0  24
        3  10.0   1

        It works as below in Series.

        >>> df.B.groupby(df.A).cumprod().sort_index()
        0     NaN
        1     0.1
        2     2.0
        3    10.0
        Name: B, dtype: float64
        '''
    def cumsum(self) -> FrameLike:
        '''
        Cumulative sum for each group.

        Returns
        -------
        Series or DataFrame

        See Also
        --------
        Series.cumsum
        DataFrame.cumsum

        Examples
        --------
        >>> df = ps.DataFrame(
        ...     [[1, None, 4], [1, 0.1, 3], [1, 20.0, 2], [4, 10.0, 1]],
        ...     columns=list(\'ABC\'))
        >>> df
           A     B  C
        0  1   NaN  4
        1  1   0.1  3
        2  1  20.0  2
        3  4  10.0  1

        By default, iterates over rows and finds the sum in each column.

        >>> df.groupby("A").cumsum().sort_index()
              B  C
        0   NaN  4
        1   0.1  7
        2  20.1  9
        3  10.0  1

        It works as below in Series.

        >>> df.B.groupby(df.A).cumsum().sort_index()
        0     NaN
        1     0.1
        2    20.1
        3    10.0
        Name: B, dtype: float64
        '''
    def apply(self, func: Callable, *args: Any, **kwargs: Any) -> DataFrame | Series:
        '''
        Apply function `func` group-wise and combine the results together.

        The function passed to `apply` must take a DataFrame as its first
        argument and return a DataFrame. `apply` will
        then take care of combining the results back together into a single
        dataframe. `apply` is therefore a highly flexible
        grouping method.

        While `apply` is a very flexible method, its downside is that
        using it can be quite a bit slower than using more specific methods
        like `agg` or `transform`. pandas-on-Spark offers a wide range of method that will
        be much faster than using `apply` for their specific purposes, so try to
        use them before reaching for `apply`.

        .. note:: this API executes the function once to infer the type which is
            potentially expensive, for instance, when the dataset is created after
            aggregations or sorting.

            To avoid this, specify return type in ``func``, for instance, as below:

            >>> def pandas_div(x) -> ps.DataFrame[int, [float, float]]:
            ...     return x[[\'B\', \'C\']] / x[[\'B\', \'C\']]

            If the return type is specified, the output column names become
            `c0, c1, c2 ... cn`. These names are positionally mapped to the returned
            DataFrame in ``func``.

            To specify the column names, you can assign them in a NumPy compound type style
            as below:

            >>> def pandas_div(x) -> ps.DataFrame[("index", int), [("a", float), ("b", float)]]:
            ...     return x[[\'B\', \'C\']] / x[[\'B\', \'C\']]

            >>> pdf = pd.DataFrame({\'B\': [1.], \'C\': [3.]})
            >>> def plus_one(x) -> ps.DataFrame[
            ...         (pdf.index.name, pdf.index.dtype), zip(pdf.columns, pdf.dtypes)]:
            ...     return x[[\'B\', \'C\']] / x[[\'B\', \'C\']]

        .. note:: the dataframe within ``func`` is actually a pandas dataframe. Therefore,
            any pandas API within this function is allowed.

        Parameters
        ----------
        func : callable
            A callable that takes a DataFrame as its first argument, and
            returns a dataframe.
        *args
            Positional arguments to pass to func.
        **kwargs
            Keyword arguments to pass to func.

        Returns
        -------
        applied : DataFrame or Series

        See Also
        --------
        aggregate : Apply aggregate function to the GroupBy object.
        DataFrame.apply : Apply a function to a DataFrame.
        Series.apply : Apply a function to a Series.

        Examples
        --------
        >>> df = ps.DataFrame({\'A\': \'a a b\'.split(),
        ...                    \'B\': [1, 2, 3],
        ...                    \'C\': [4, 6, 5]}, columns=[\'A\', \'B\', \'C\'])
        >>> g = df.groupby(\'A\')

        Notice that ``g`` has two groups, ``a`` and ``b``.
        Calling `apply` in various ways, we can get different grouping results:

        Below the functions passed to `apply` takes a DataFrame as
        its argument and returns a DataFrame. `apply` combines the result for
        each group together into a new DataFrame:

        >>> def plus_min(x):
        ...     return x + x.min()
        >>> g.apply(plus_min).sort_index()  # doctest: +NORMALIZE_WHITESPACE
            A  B   C
        0  aa  2   8
        1  aa  3  10
        2  bb  6  10

        >>> g.apply(sum).sort_index()  # doctest: +NORMALIZE_WHITESPACE
            A  B   C
        A
        a  aa  3  10
        b   b  3   5

        >>> g.apply(len).sort_index()  # doctest: +NORMALIZE_WHITESPACE
        A
        a    2
        b    1
        dtype: int64

        You can specify the type hint and prevent schema inference for better performance.

        >>> def pandas_div(x) -> ps.DataFrame[int, [float, float]]:
        ...     return x[[\'B\', \'C\']] / x[[\'B\', \'C\']]
        >>> g.apply(pandas_div).sort_index()  # doctest: +NORMALIZE_WHITESPACE
            c0   c1
        0  1.0  1.0
        1  1.0  1.0
        2  1.0  1.0

        >>> def pandas_div(x) -> ps.DataFrame[("index", int), [("f1", float), ("f2", float)]]:
        ...     return x[[\'B\', \'C\']] / x[[\'B\', \'C\']]
        >>> g.apply(pandas_div).sort_index()  # doctest: +NORMALIZE_WHITESPACE
                f1   f2
        index
        0      1.0  1.0
        1      1.0  1.0
        2      1.0  1.0

        In case of Series, it works as below.

        >>> def plus_max(x) -> ps.Series[int]:
        ...     return x + x.max()
        >>> df.B.groupby(df.A).apply(plus_max).sort_index()  # doctest: +SKIP
        0    6
        1    3
        2    4
        Name: B, dtype: int64

        >>> def plus_min(x):
        ...     return x + x.min()
        >>> df.B.groupby(df.A).apply(plus_min).sort_index()
        0    2
        1    3
        2    6
        Name: B, dtype: int64

        You can also return a scalar value as an aggregated value of the group:

        >>> def plus_length(x) -> int:
        ...     return len(x)
        >>> df.B.groupby(df.A).apply(plus_length).sort_index()  # doctest: +SKIP
        0    1
        1    2
        Name: B, dtype: int64

        The extra arguments to the function can be passed as below.

        >>> def calculation(x, y, z) -> int:
        ...     return len(x) + y * z
        >>> df.B.groupby(df.A).apply(calculation, 5, z=10).sort_index()  # doctest: +SKIP
        0    51
        1    52
        Name: B, dtype: int64
        '''
    def filter(self, func: Callable[[FrameLike], FrameLike]) -> FrameLike:
        """
        Return a copy of a DataFrame excluding elements from groups that
        do not satisfy the boolean criterion specified by func.

        Parameters
        ----------
        f : function
            Function to apply to each subframe. Should return True or False.
        dropna : Drop groups that do not pass the filter. True by default;
            if False, groups that evaluate False are filled with NaNs.

        Returns
        -------
        filtered : DataFrame or Series

        Notes
        -----
        Each subframe is endowed the attribute 'name' in case you need to know
        which group you are working on.

        Examples
        --------
        >>> df = ps.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
        ...                           'foo', 'bar'],
        ...                    'B' : [1, 2, 3, 4, 5, 6],
        ...                    'C' : [2.0, 5., 8., 1., 2., 9.]}, columns=['A', 'B', 'C'])
        >>> grouped = df.groupby('A')
        >>> grouped.filter(lambda x: x['B'].mean() > 3.)
             A  B    C
        1  bar  2  5.0
        3  bar  4  1.0
        5  bar  6  9.0

        >>> df.B.groupby(df.A).filter(lambda x: x.mean() > 3.)
        1    2
        3    4
        5    6
        Name: B, dtype: int64
        """
    def rank(self, method: str = 'average', ascending: bool = True) -> FrameLike:
        '''
        Provide the rank of values within each group.

        Parameters
        ----------
        method : {\'average\', \'min\', \'max\', \'first\', \'dense\'}, default \'average\'
            * average: average rank of group
            * min: lowest rank in group
            * max: highest rank in group
            * first: ranks assigned in order they appear in the array
            * dense: like \'min\', but rank always increases by 1 between groups
        ascending : boolean, default True
            False for ranks by high (1) to low (N)

        Returns
        -------
        DataFrame with ranking of values within each group

        Examples
        --------

        >>> df = ps.DataFrame({
        ...     \'a\': [1, 1, 1, 2, 2, 2, 3, 3, 3],
        ...     \'b\': [1, 2, 2, 2, 3, 3, 3, 4, 4]}, columns=[\'a\', \'b\'])
        >>> df
           a  b
        0  1  1
        1  1  2
        2  1  2
        3  2  2
        4  2  3
        5  2  3
        6  3  3
        7  3  4
        8  3  4

        >>> df.groupby("a").rank().sort_index()
             b
        0  1.0
        1  2.5
        2  2.5
        3  1.0
        4  2.5
        5  2.5
        6  1.0
        7  2.5
        8  2.5

        >>> df.b.groupby(df.a).rank(method=\'max\').sort_index()
        0    1.0
        1    3.0
        2    3.0
        3    1.0
        4    3.0
        5    3.0
        6    1.0
        7    3.0
        8    3.0
        Name: b, dtype: float64

        '''
    def idxmax(self, skipna: bool = True) -> FrameLike:
        """
        Return index of first occurrence of maximum over requested axis in group.
        NA/null values are excluded.

        Parameters
        ----------
        skipna : boolean, default True
            Exclude NA/null values. If an entire row/column is NA, the result will be NA.

        See Also
        --------
        Series.idxmax
        DataFrame.idxmax
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> df = ps.DataFrame({'a': [1, 1, 2, 2, 3],
        ...                    'b': [1, 2, 3, 4, 5],
        ...                    'c': [5, 4, 3, 2, 1]}, columns=['a', 'b', 'c'])

        >>> df.groupby(['a'])['b'].idxmax().sort_index() # doctest: +NORMALIZE_WHITESPACE
        a
        1  1
        2  3
        3  4
        Name: b, dtype: int64

        >>> df.groupby(['a']).idxmax().sort_index() # doctest: +NORMALIZE_WHITESPACE
           b  c
        a
        1  1  0
        2  3  2
        3  4  4
        """
    def idxmin(self, skipna: bool = True) -> FrameLike:
        """
        Return index of first occurrence of minimum over requested axis in group.
        NA/null values are excluded.

        Parameters
        ----------
        skipna : boolean, default True
            Exclude NA/null values. If an entire row/column is NA, the result will be NA.

        See Also
        --------
        Series.idxmin
        DataFrame.idxmin
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> df = ps.DataFrame({'a': [1, 1, 2, 2, 3],
        ...                    'b': [1, 2, 3, 4, 5],
        ...                    'c': [5, 4, 3, 2, 1]}, columns=['a', 'b', 'c'])

        >>> df.groupby(['a'])['b'].idxmin().sort_index() # doctest: +NORMALIZE_WHITESPACE
        a
        1    0
        2    2
        3    4
        Name: b, dtype: int64

        >>> df.groupby(['a']).idxmin().sort_index() # doctest: +NORMALIZE_WHITESPACE
           b  c
        a
        1  0  1
        2  2  3
        3  4  4
        """
    def fillna(self, value: Any | None = None, method: str | None = None, axis: Axis | None = None, inplace: bool = False, limit: int | None = None) -> FrameLike:
        """Fill NA/NaN values in group.

        Parameters
        ----------
        value : scalar, dict, Series
            Value to use to fill holes. alternately a dict/Series of values
            specifying which value to use for each column.
            DataFrame is not supported.
        method : {'backfill', 'bfill', 'pad', 'ffill', None}, default None
            Method to use for filling holes in reindexed Series pad / ffill: propagate last valid
            observation forward to next valid backfill / bfill:
            use NEXT valid observation to fill gap
        axis : {0 or `index`}
            1 and `columns` are not supported.
        inplace : boolean, default False
            Fill in place (do not create a new object)
        limit : int, default None
            If method is specified, this is the maximum number of consecutive NaN values to
            forward/backward fill. In other words, if there is a gap with more than this number of
            consecutive NaNs, it will only be partially filled. If method is not specified,
            this is the maximum number of entries along the entire axis where NaNs will be filled.
            Must be greater than 0 if not None

        Returns
        -------
        DataFrame
            DataFrame with NA entries filled.

        Examples
        --------
        >>> df = ps.DataFrame({
        ...     'A': [1, 1, 2, 2],
        ...     'B': [2, 4, None, 3],
        ...     'C': [None, None, None, 1],
        ...     'D': [0, 1, 5, 4]
        ...     },
        ...     columns=['A', 'B', 'C', 'D'])
        >>> df
           A    B    C  D
        0  1  2.0  NaN  0
        1  1  4.0  NaN  1
        2  2  NaN  NaN  5
        3  2  3.0  1.0  4

        We can also propagate non-null values forward or backward in group.

        >>> df.groupby(['A'])['B'].fillna(method='ffill').sort_index()
        0    2.0
        1    4.0
        2    NaN
        3    3.0
        Name: B, dtype: float64

        >>> df.groupby(['A']).fillna(method='bfill').sort_index()
             B    C  D
        0  2.0  NaN  0
        1  4.0  NaN  1
        2  3.0  1.0  5
        3  3.0  1.0  4
        """
    def bfill(self, limit: int | None = None) -> FrameLike:
        """
        Synonym for `DataFrame.fillna()` with ``method=`bfill```.

        Parameters
        ----------
        axis : {0 or `index`}
            1 and `columns` are not supported.
        inplace : boolean, default False
            Fill in place (do not create a new object)
        limit : int, default None
            If method is specified, this is the maximum number of consecutive NaN values to
            forward/backward fill. In other words, if there is a gap with more than this number of
            consecutive NaNs, it will only be partially filled. If method is not specified,
            this is the maximum number of entries along the entire axis where NaNs will be filled.
            Must be greater than 0 if not None

        Returns
        -------
        DataFrame
            DataFrame with NA entries filled.

        Examples
        --------
        >>> df = ps.DataFrame({
        ...     'A': [1, 1, 2, 2],
        ...     'B': [2, 4, None, 3],
        ...     'C': [None, None, None, 1],
        ...     'D': [0, 1, 5, 4]
        ...     },
        ...     columns=['A', 'B', 'C', 'D'])
        >>> df
           A    B    C  D
        0  1  2.0  NaN  0
        1  1  4.0  NaN  1
        2  2  NaN  NaN  5
        3  2  3.0  1.0  4

        Propagate non-null values backward.

        >>> df.groupby(['A']).bfill().sort_index()
             B    C  D
        0  2.0  NaN  0
        1  4.0  NaN  1
        2  3.0  1.0  5
        3  3.0  1.0  4
        """
    def backfill(self, limit: int | None = None) -> FrameLike:
        """
        Alias for bfill.

        .. deprecated:: 3.4.0
        """
    def ffill(self, limit: int | None = None) -> FrameLike:
        """
        Synonym for `DataFrame.fillna()` with ``method=`ffill```.

        Parameters
        ----------
        axis : {0 or `index`}
            1 and `columns` are not supported.
        inplace : boolean, default False
            Fill in place (do not create a new object)
        limit : int, default None
            If method is specified, this is the maximum number of consecutive NaN values to
            forward/backward fill. In other words, if there is a gap with more than this number of
            consecutive NaNs, it will only be partially filled. If method is not specified,
            this is the maximum number of entries along the entire axis where NaNs will be filled.
            Must be greater than 0 if not None

        Returns
        -------
        DataFrame
            DataFrame with NA entries filled.

        Examples
        --------
        >>> df = ps.DataFrame({
        ...     'A': [1, 1, 2, 2],
        ...     'B': [2, 4, None, 3],
        ...     'C': [None, None, None, 1],
        ...     'D': [0, 1, 5, 4]
        ...     },
        ...     columns=['A', 'B', 'C', 'D'])
        >>> df
           A    B    C  D
        0  1  2.0  NaN  0
        1  1  4.0  NaN  1
        2  2  NaN  NaN  5
        3  2  3.0  1.0  4

        Propagate non-null values forward.

        >>> df.groupby(['A']).ffill().sort_index()
             B    C  D
        0  2.0  NaN  0
        1  4.0  NaN  1
        2  NaN  NaN  5
        3  3.0  1.0  4
        """
    def pad(self, limit: int | None = None) -> FrameLike:
        """
        Alias for ffill.

        .. deprecated:: 3.4.0
        """
    def head(self, n: int = 5) -> FrameLike:
        '''
        Return first n rows of each group.

        Returns
        -------
        DataFrame or Series

        Examples
        --------
        >>> df = ps.DataFrame({\'a\': [1, 1, 1, 1, 2, 2, 2, 3, 3, 3],
        ...                    \'b\': [2, 3, 1, 4, 6, 9, 8, 10, 7, 5],
        ...                    \'c\': [3, 5, 2, 5, 1, 2, 6, 4, 3, 6]},
        ...                   columns=[\'a\', \'b\', \'c\'],
        ...                   index=[7, 2, 4, 1, 3, 4, 9, 10, 5, 6])
        >>> df
            a   b  c
        7   1   2  3
        2   1   3  5
        4   1   1  2
        1   1   4  5
        3   2   6  1
        4   2   9  2
        9   2   8  6
        10  3  10  4
        5   3   7  3
        6   3   5  6

        >>> df.groupby(\'a\').head(2).sort_index()
            a   b  c
        2   1   3  5
        3   2   6  1
        4   2   9  2
        5   3   7  3
        7   1   2  3
        10  3  10  4

        >>> df.groupby(\'a\')[\'b\'].head(2).sort_index()
        2      3
        3      6
        4      9
        5      7
        7      2
        10    10
        Name: b, dtype: int64

        Supports Groupby positional indexing Since pandas on Spark 3.4 (with pandas 1.4+):

        >>> df = ps.DataFrame([["g", "g0"],
        ...                   ["g", "g1"],
        ...                   ["g", "g2"],
        ...                   ["g", "g3"],
        ...                   ["h", "h0"],
        ...                   ["h", "h1"]], columns=["A", "B"])
        >>> df.groupby("A").head(-1) # doctest: +SKIP
           A   B
        0  g  g0
        1  g  g1
        2  g  g2
        4  h  h0
        '''
    def tail(self, n: int = 5) -> FrameLike:
        '''
        Return last n rows of each group.

        Similar to `.apply(lambda x: x.tail(n))`, but it returns a subset of rows from
        the original DataFrame with original index and order preserved (`as_index` flag is ignored).

        Does not work for negative values of n.

        Returns
        -------
        DataFrame or Series

        Examples
        --------
        >>> df = ps.DataFrame({\'a\': [1, 1, 1, 1, 2, 2, 2, 3, 3, 3],
        ...                    \'b\': [2, 3, 1, 4, 6, 9, 8, 10, 7, 5],
        ...                    \'c\': [3, 5, 2, 5, 1, 2, 6, 4, 3, 6]},
        ...                   columns=[\'a\', \'b\', \'c\'],
        ...                   index=[7, 2, 3, 1, 3, 4, 9, 10, 5, 6])
        >>> df
            a   b  c
        7   1   2  3
        2   1   3  5
        3   1   1  2
        1   1   4  5
        3   2   6  1
        4   2   9  2
        9   2   8  6
        10  3  10  4
        5   3   7  3
        6   3   5  6

        >>> df.groupby(\'a\').tail(2).sort_index()
           a  b  c
        1  1  4  5
        3  1  1  2
        4  2  9  2
        5  3  7  3
        6  3  5  6
        9  2  8  6

        >>> df.groupby(\'a\')[\'b\'].tail(2).sort_index()
        1    4
        3    1
        4    9
        5    7
        6    5
        9    8
        Name: b, dtype: int64

        Supports Groupby positional indexing Since pandas on Spark 3.4 (with pandas 1.4+):

        >>> df = ps.DataFrame([["g", "g0"],
        ...                   ["g", "g1"],
        ...                   ["g", "g2"],
        ...                   ["g", "g3"],
        ...                   ["h", "h0"],
        ...                   ["h", "h1"]], columns=["A", "B"])
        >>> df.groupby("A").tail(-1) # doctest: +SKIP
           A   B
        3  g  g3
        2  g  g2
        1  g  g1
        5  h  h1
        '''
    def shift(self, periods: int = 1, fill_value: Any | None = None) -> FrameLike:
        """
        Shift each group by periods observations.

        Parameters
        ----------
        periods : integer, default 1
            number of periods to shift
        fill_value : optional

        Returns
        -------
        Series or DataFrame
            Object shifted within each group.

        Examples
        --------

        >>> df = ps.DataFrame({
        ...     'a': [1, 1, 1, 2, 2, 2, 3, 3, 3],
        ...     'b': [1, 2, 2, 2, 3, 3, 3, 4, 4]}, columns=['a', 'b'])
        >>> df
           a  b
        0  1  1
        1  1  2
        2  1  2
        3  2  2
        4  2  3
        5  2  3
        6  3  3
        7  3  4
        8  3  4

        >>> df.groupby('a').shift().sort_index()  # doctest: +SKIP
             b
        0  NaN
        1  1.0
        2  2.0
        3  NaN
        4  2.0
        5  3.0
        6  NaN
        7  3.0
        8  4.0

        >>> df.groupby('a').shift(periods=-1, fill_value=0).sort_index()  # doctest: +SKIP
           b
        0  2
        1  2
        2  0
        3  3
        4  3
        5  0
        6  4
        7  4
        8  0
        """
    def transform(self, func: Callable[..., pd.Series], *args: Any, **kwargs: Any) -> FrameLike:
        '''
        Apply function column-by-column to the GroupBy object.

        The function passed to `transform` must take a Series as its first
        argument and return a Series. The given function is executed for
        each series in each grouped data.

        While `transform` is a very flexible method, its downside is that
        using it can be quite a bit slower than using more specific methods
        like `agg` or `transform`. pandas-on-Spark offers a wide range of method that will
        be much faster than using `transform` for their specific purposes, so try to
        use them before reaching for `transform`.

        .. note:: this API executes the function once to infer the type which is
             potentially expensive, for instance, when the dataset is created after
             aggregations or sorting.

             To avoid this, specify return type in ``func``, for instance, as below:

             >>> def convert_to_string(x) -> ps.Series[str]:
             ...     return x.apply("a string {}".format)

            When the given function has the return type annotated, the original index of the
            GroupBy object will be lost, and a default index will be attached to the result.
            Please be careful about configuring the default index. See also `Default Index Type
            <https://spark.apache.org/docs/latest/api/python/user_guide/pandas_on_spark/options.html#default-index-type>`_.

        .. note:: the series within ``func`` is actually a pandas series. Therefore,
            any pandas API within this function is allowed.


        Parameters
        ----------
        func : callable
            A callable that takes a Series as its first argument, and
            returns a Series.
        *args
            Positional arguments to pass to func.
        **kwargs
            Keyword arguments to pass to func.

        Returns
        -------
        applied : DataFrame

        See Also
        --------
        aggregate : Apply aggregate function to the GroupBy object.
        Series.apply : Apply a function to a Series.

        Examples
        --------

        >>> df = ps.DataFrame({\'A\': [0, 0, 1],
        ...                    \'B\': [1, 2, 3],
        ...                    \'C\': [4, 6, 5]}, columns=[\'A\', \'B\', \'C\'])

        >>> g = df.groupby(\'A\')

        Notice that ``g`` has two groups, ``0`` and ``1``.
        Calling `transform` in various ways, we can get different grouping results:
        Below the functions passed to `transform` takes a Series as
        its argument and returns a Series. `transform` applies the function on each series
        in each grouped data, and combine them into a new DataFrame:

        >>> def convert_to_string(x) -> ps.Series[str]:
        ...     return x.apply("a string {}".format)
        >>> g.transform(convert_to_string)  # doctest: +NORMALIZE_WHITESPACE
                    B           C
        0  a string 1  a string 4
        1  a string 2  a string 6
        2  a string 3  a string 5

        >>> def plus_max(x) -> ps.Series[int]:
        ...     return x + x.max()
        >>> g.transform(plus_max)  # doctest: +NORMALIZE_WHITESPACE
           B   C
        0  3  10
        1  4  12
        2  6  10

        You can omit the type hint and let pandas-on-Spark infer its type.

        >>> def plus_min(x):
        ...     return x + x.min()
        >>> g.transform(plus_min)  # doctest: +NORMALIZE_WHITESPACE
           B   C
        0  2   8
        1  3  10
        2  6  10

        In case of Series, it works as below.

        >>> df.B.groupby(df.A).transform(plus_max)
        0    3
        1    4
        2    6
        Name: B, dtype: int64

        >>> (df * -1).B.groupby(df.A).transform(abs)
        0    1
        1    2
        2    3
        Name: B, dtype: int64

        You can also specify extra arguments to pass to the function.

        >>> def calculation(x, y, z) -> ps.Series[int]:
        ...     return x + x.min() + y + z
        >>> g.transform(calculation, 5, z=20)  # doctest: +NORMALIZE_WHITESPACE
            B   C
        0  27  33
        1  28  35
        2  31  35
        '''
    def nunique(self, dropna: bool = True) -> FrameLike:
        """
        Return DataFrame with number of distinct observations per group for each column.

        Parameters
        ----------
        dropna : boolean, default True
            Don’t include NaN in the counts.

        Returns
        -------
        nunique : DataFrame or Series

        Examples
        --------

        >>> df = ps.DataFrame({'id': ['spam', 'egg', 'egg', 'spam',
        ...                           'ham', 'ham'],
        ...                    'value1': [1, 5, 5, 2, 5, 5],
        ...                    'value2': list('abbaxy')}, columns=['id', 'value1', 'value2'])
        >>> df
             id  value1 value2
        0  spam       1      a
        1   egg       5      b
        2   egg       5      b
        3  spam       2      a
        4   ham       5      x
        5   ham       5      y

        >>> df.groupby('id').nunique().sort_index() # doctest: +SKIP
              value1  value2
        id
        egg        1       1
        ham        1       2
        spam       2       1

        >>> df.groupby('id')['value1'].nunique().sort_index() # doctest: +NORMALIZE_WHITESPACE
        id
        egg     1
        ham     1
        spam    2
        Name: value1, dtype: int64
        """
    def rolling(self, window: int, min_periods: int | None = None) -> RollingGroupby[FrameLike]:
        """
        Return an rolling grouper, providing rolling
        functionality per group.

        .. note:: 'min_periods' in pandas-on-Spark works as a fixed window size unlike pandas.
        Unlike pandas, NA is also counted as the period. This might be changed
        soon.

        Parameters
        ----------
        window : int, or offset
            Size of the moving window.
            This is the number of observations used for calculating the statistic.
            Each window will be a fixed size.

        min_periods : int, default 1
            Minimum number of observations in window required to have a value
            (otherwise result is NA).

        See Also
        --------
        Series.groupby
        DataFrame.groupby
        """
    def expanding(self, min_periods: int = 1) -> ExpandingGroupby[FrameLike]:
        """
        Return an expanding grouper, providing expanding
        functionality per group.

        .. note:: 'min_periods' in pandas-on-Spark works as a fixed window size unlike pandas.
        Unlike pandas, NA is also counted as the period. This might be changed
        soon.

        Parameters
        ----------
        min_periods : int, default 1
            Minimum number of observations in window required to have a value
            (otherwise result is NA).

        See Also
        --------
        Series.groupby
        DataFrame.groupby
        """
    def ewm(self, com: float | None = None, span: float | None = None, halflife: float | None = None, alpha: float | None = None, min_periods: int | None = None, ignore_na: bool = False) -> ExponentialMovingGroupby[FrameLike]:
        """
        Return an ewm grouper, providing ewm functionality per group.

        .. note:: 'min_periods' in pandas-on-Spark works as a fixed window size unlike pandas.
            Unlike pandas, NA is also counted as the period. This might be changed
            soon.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        com : float, optional
            Specify decay in terms of center of mass.
            alpha = 1 / (1 + com), for com >= 0.

        span : float, optional
            Specify decay in terms of span.
            alpha = 2 / (span + 1), for span >= 1.

        halflife : float, optional
            Specify decay in terms of half-life.
            alpha = 1 - exp(-ln(2) / halflife), for halflife > 0.

        alpha : float, optional
            Specify smoothing factor alpha directly.
            0 < alpha <= 1.

        min_periods : int, default None
            Minimum number of observations in window required to have a value
            (otherwise result is NA).

        ignore_na : bool, default False
            Ignore missing values when calculating weights.

            - When ``ignore_na=False`` (default), weights are based on absolute positions.
              For example, the weights of :math:`x_0` and :math:`x_2` used in calculating
              the final weighted average of [:math:`x_0`, None, :math:`x_2`] are
              :math:`(1-\x07lpha)^2` and :math:`1` if ``adjust=True``, and
              :math:`(1-\x07lpha)^2` and :math:`\x07lpha` if ``adjust=False``.

            - When ``ignore_na=True``, weights are based
              on relative positions. For example, the weights of :math:`x_0` and :math:`x_2`
              used in calculating the final weighted average of
              [:math:`x_0`, None, :math:`x_2`] are :math:`1-\x07lpha` and :math:`1` if
              ``adjust=True``, and :math:`1-\x07lpha` and :math:`\x07lpha` if ``adjust=False``.
        """
    def get_group(self, name: Name | List[Name]) -> FrameLike:
        '''
        Construct DataFrame from group with provided name.

        Parameters
        ----------
        name : object
            The name of the group to get as a DataFrame.

        Returns
        -------
        group : same type as obj

        Examples
        --------
        >>> psdf = ps.DataFrame([(\'falcon\', \'bird\', 389.0),
        ...                     (\'parrot\', \'bird\', 24.0),
        ...                     (\'lion\', \'mammal\', 80.5),
        ...                     (\'monkey\', \'mammal\', np.nan)],
        ...                    columns=[\'name\', \'class\', \'max_speed\'],
        ...                    index=[0, 2, 3, 1])
        >>> psdf
             name   class  max_speed
        0  falcon    bird      389.0
        2  parrot    bird       24.0
        3    lion  mammal       80.5
        1  monkey  mammal        NaN

        >>> psdf.groupby("class").get_group("bird").sort_index()
             name class  max_speed
        0  falcon  bird      389.0
        2  parrot  bird       24.0

        >>> psdf.groupby("class").get_group("mammal").sort_index()
             name   class  max_speed
        1  monkey  mammal        NaN
        3    lion  mammal       80.5
        '''
    def median(self, numeric_only: bool | None = True, accuracy: int = 10000) -> FrameLike:
        """
        Compute median of groups, excluding missing values.

        For multiple groupings, the result index will be a MultiIndex

        .. note:: Unlike pandas', the median in pandas-on-Spark is an approximated median based upon
            approximate percentile computation because computing median across a large dataset
            is extremely expensive.

        Parameters
        ----------
        numeric_only : bool, default False
            Include only float, int, boolean columns. If None, will attempt to use
            everything, then use only numeric data.

            .. versionadded:: 3.4.0

        Returns
        -------
        Series or DataFrame
            Median of values within each group.

        Examples
        --------
        >>> psdf = ps.DataFrame({'a': [1., 1., 1., 1., 2., 2., 2., 3., 3., 3.],
        ...                     'b': [2., 3., 1., 4., 6., 9., 8., 10., 7., 5.],
        ...                     'c': [3., 5., 2., 5., 1., 2., 6., 4., 3., 6.]},
        ...                    columns=['a', 'b', 'c'],
        ...                    index=[7, 2, 4, 1, 3, 4, 9, 10, 5, 6])
        >>> psdf
              a     b    c
        7   1.0   2.0  3.0
        2   1.0   3.0  5.0
        4   1.0   1.0  2.0
        1   1.0   4.0  5.0
        3   2.0   6.0  1.0
        4   2.0   9.0  2.0
        9   2.0   8.0  6.0
        10  3.0  10.0  4.0
        5   3.0   7.0  3.0
        6   3.0   5.0  6.0

        DataFrameGroupBy

        >>> psdf.groupby('a').median().sort_index()  # doctest: +NORMALIZE_WHITESPACE
               b    c
        a
        1.0  2.0  3.0
        2.0  8.0  2.0
        3.0  7.0  4.0

        SeriesGroupBy

        >>> psdf.groupby('a')['b'].median().sort_index()
        a
        1.0    2.0
        2.0    8.0
        3.0    7.0
        Name: b, dtype: float64
        """

class DataFrameGroupBy(GroupBy[DataFrame]):
    def __init__(self, psdf: DataFrame, by: List[Series], as_index: bool, dropna: bool, column_labels_to_exclude: Set[Label], agg_columns: List[Label] = None) -> None: ...
    def __getattr__(self, item: str) -> Any: ...
    def __getitem__(self, item: Any) -> GroupBy: ...
    def describe(self) -> DataFrame:
        """
        Generate descriptive statistics that summarize the central tendency,
        dispersion and shape of a dataset's distribution, excluding
        ``NaN`` values.

        Analyzes both numeric and object series, as well
        as ``DataFrame`` column sets of mixed data types. The output
        will vary depending on what is provided. Refer to the notes
        below for more detail.

        .. note:: Unlike pandas, the percentiles in pandas-on-Spark are based upon
            approximate percentile computation because computing percentiles
            across a large dataset is extremely expensive.

        Returns
        -------
        DataFrame
            Summary statistics of the DataFrame provided.

        See Also
        --------
        DataFrame.count
        DataFrame.max
        DataFrame.min
        DataFrame.mean
        DataFrame.std

        Examples
        --------
        >>> df = ps.DataFrame({'a': [1, 1, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
        >>> df
           a  b  c
        0  1  4  7
        1  1  5  8
        2  3  6  9

        Describing a ``DataFrame``. By default only numeric fields
        are returned.

        >>> described = df.groupby('a').describe()
        >>> described.sort_index()  # doctest: +NORMALIZE_WHITESPACE
              b                                        c
          count mean       std min 25% 50% 75% max count mean       std min 25% 50% 75% max
        a
        1   2.0  4.5  0.707107 4.0 4.0 4.0 5.0 5.0   2.0  7.5  0.707107 7.0 7.0 7.0 8.0 8.0
        3   1.0  6.0       NaN 6.0 6.0 6.0 6.0 6.0   1.0  9.0       NaN 9.0 9.0 9.0 9.0 9.0

        """

class SeriesGroupBy(GroupBy[Series]):
    def __init__(self, psser: Series, by: List[Series], as_index: bool = True, dropna: bool = True) -> None: ...
    def __getattr__(self, item: str) -> Any: ...
    def agg(self, *args: Any, **kwargs: Any) -> None: ...
    def aggregate(self, *args: Any, **kwargs: Any) -> None: ...
    def size(self) -> Series: ...
    def nsmallest(self, n: int = 5) -> Series:
        """
        Return the smallest `n` elements.

        Parameters
        ----------
        n : int
            Number of items to retrieve.

        See Also
        --------
        pyspark.pandas.Series.nsmallest
        pyspark.pandas.DataFrame.nsmallest

        Examples
        --------
        >>> df = ps.DataFrame({'a': [1, 1, 1, 2, 2, 2, 3, 3, 3],
        ...                    'b': [1, 2, 2, 2, 3, 3, 3, 4, 4]}, columns=['a', 'b'])

        >>> df.groupby(['a'])['b'].nsmallest(1).sort_index()  # doctest: +NORMALIZE_WHITESPACE
        a
        1  0    1
        2  3    2
        3  6    3
        Name: b, dtype: int64
        """
    def nlargest(self, n: int = 5) -> Series:
        """
        Return the first n rows ordered by columns in descending order in group.

        Return the first n rows with the smallest values in columns, in descending order.
        The columns that are not specified are returned as well, but not used for ordering.

        Parameters
        ----------
        n : int
            Number of items to retrieve.

        See Also
        --------
        pyspark.pandas.Series.nlargest
        pyspark.pandas.DataFrame.nlargest

        Examples
        --------
        >>> df = ps.DataFrame({'a': [1, 1, 1, 2, 2, 2, 3, 3, 3],
        ...                    'b': [1, 2, 2, 2, 3, 3, 3, 4, 4]}, columns=['a', 'b'])

        >>> df.groupby(['a'])['b'].nlargest(1).sort_index()  # doctest: +NORMALIZE_WHITESPACE
        a
        1  1    2
        2  4    3
        3  7    4
        Name: b, dtype: int64
        """
    def value_counts(self, sort: bool | None = None, ascending: bool | None = None, dropna: bool = True) -> Series:
        """
        Compute group sizes.

        Parameters
        ----------
        sort : boolean, default None
            Sort by frequencies.
        ascending : boolean, default False
            Sort in ascending order.
        dropna : boolean, default True
            Don't include counts of NaN.

        See Also
        --------
        pyspark.pandas.Series.groupby
        pyspark.pandas.DataFrame.groupby

        Examples
        --------
        >>> df = ps.DataFrame({'A': [1, 2, 2, 3, 3, 3],
        ...                    'B': [1, 1, 2, 3, 3, np.nan]},
        ...                   columns=['A', 'B'])
        >>> df
           A    B
        0  1  1.0
        1  2  1.0
        2  2  2.0
        3  3  3.0
        4  3  3.0
        5  3  NaN

        >>> df.groupby('A')['B'].value_counts().sort_index()  # doctest: +NORMALIZE_WHITESPACE
        A  B
        1  1.0    1
        2  1.0    1
           2.0    1
        3  3.0    2
        Name: B, dtype: int64

        Don't include counts of NaN when dropna is False.

        >>> df.groupby('A')['B'].value_counts(
        ...   dropna=False).sort_index()  # doctest: +NORMALIZE_WHITESPACE
        A  B
        1  1.0    1
        2  1.0    1
           2.0    1
        3  3.0    2
           NaN    1
        Name: B, dtype: int64
        """
    def unique(self) -> Series:
        """
        Return unique values in group.

        Unique is returned in order of unknown. It does NOT sort.

        See Also
        --------
        pyspark.pandas.Series.unique
        pyspark.pandas.Index.unique

        Examples
        --------
        >>> df = ps.DataFrame({'a': [1, 1, 1, 2, 2, 2, 3, 3, 3],
        ...                    'b': [1, 2, 2, 2, 3, 3, 3, 4, 4]}, columns=['a', 'b'])

        >>> df.groupby(['a'])['b'].unique().sort_index()  # doctest: +SKIP
        a
        1    [1, 2]
        2    [2, 3]
        3    [3, 4]
        Name: b, dtype: object
        """

def is_multi_agg_with_relabel(**kwargs: Any) -> bool:
    """
    Check whether the kwargs pass to .agg look like multi-agg with relabling.

    Parameters
    ----------
    **kwargs : dict

    Returns
    -------
    bool

    Examples
    --------
    >>> is_multi_agg_with_relabel(a='max')
    False
    >>> is_multi_agg_with_relabel(a_max=('a', 'max'),
    ...                            a_min=('a', 'min'))
    True
    >>> is_multi_agg_with_relabel()
    False
    """
def normalize_keyword_aggregation(kwargs: Dict[str, Tuple[Name, str]]) -> Tuple[Dict[Name, List[str]], List[str], List[Tuple]]:
    """
    Normalize user-provided kwargs.

    Transforms from the new ``Dict[str, NamedAgg]`` style kwargs
    to the old defaultdict[str, List[scalar]].

    Parameters
    ----------
    kwargs : dict

    Returns
    -------
    aggspec : dict
        The transformed kwargs.
    columns : List[str]
        The user-provided keys.
    order : List[Tuple[str, str]]
        Pairs of the input and output column names.

    Examples
    --------
    >>> normalize_keyword_aggregation({'output': ('input', 'sum')})
    (defaultdict(<class 'list'>, {'input': ['sum']}), ['output'], [('input', 'sum')])
    """
