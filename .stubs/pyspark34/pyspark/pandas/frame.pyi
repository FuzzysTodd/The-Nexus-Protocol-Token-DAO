import datetime
import numpy as np
import pandas as pd
from _typeshed import Incomplete
from collections.abc import Mapping
from pandas.io.formats.style import Styler
from pandas.tseries.frequencies import DateOffset
from pyspark import StorageLevel as StorageLevel
from pyspark.pandas._typing import Axis as Axis, DataFrameOrSeries as DataFrameOrSeries, Dtype as Dtype, Label as Label, Name as Name, Scalar as Scalar, T as T
from pyspark.pandas.accessors import PandasOnSparkFrameMethods as PandasOnSparkFrameMethods
from pyspark.pandas.config import get_option as get_option, option_context as option_context
from pyspark.pandas.correlation import CORRELATION_CORR_OUTPUT_COLUMN as CORRELATION_CORR_OUTPUT_COLUMN, CORRELATION_COUNT_OUTPUT_COLUMN as CORRELATION_COUNT_OUTPUT_COLUMN, CORRELATION_VALUE_1_COLUMN as CORRELATION_VALUE_1_COLUMN, CORRELATION_VALUE_2_COLUMN as CORRELATION_VALUE_2_COLUMN, compute as compute
from pyspark.pandas.generic import Frame as Frame
from pyspark.pandas.groupby import DataFrameGroupBy as DataFrameGroupBy
from pyspark.pandas.indexes import Index as Index
from pyspark.pandas.internal import HIDDEN_COLUMNS as HIDDEN_COLUMNS, InternalField as InternalField, InternalFrame as InternalFrame, NATURAL_ORDER_COLUMN_NAME as NATURAL_ORDER_COLUMN_NAME, SPARK_DEFAULT_INDEX_NAME as SPARK_DEFAULT_INDEX_NAME, SPARK_DEFAULT_SERIES_NAME as SPARK_DEFAULT_SERIES_NAME, SPARK_INDEX_NAME_FORMAT as SPARK_INDEX_NAME_FORMAT, SPARK_INDEX_NAME_PATTERN as SPARK_INDEX_NAME_PATTERN
from pyspark.pandas.missing.frame import MissingPandasLikeDataFrame as MissingPandasLikeDataFrame
from pyspark.pandas.plot import PandasOnSparkPlotAccessor as PandasOnSparkPlotAccessor
from pyspark.pandas.resample import DataFrameResampler as DataFrameResampler
from pyspark.pandas.series import Series as Series
from pyspark.pandas.spark.accessors import CachedSparkFrameMethods as CachedSparkFrameMethods, SparkFrameMethods as SparkFrameMethods
from pyspark.pandas.typedef.typehints import DataFrameType as DataFrameType, ScalarType as ScalarType, SeriesType as SeriesType, as_spark_type as as_spark_type, create_tuple_for_frame_type as create_tuple_for_frame_type, infer_return_type as infer_return_type, pandas_on_spark_type as pandas_on_spark_type, spark_type_to_pandas_dtype as spark_type_to_pandas_dtype
from pyspark.pandas.utils import align_diff_frames as align_diff_frames, column_labels_level as column_labels_level, combine_frames as combine_frames, default_session as default_session, is_name_like_tuple as is_name_like_tuple, is_name_like_value as is_name_like_value, is_testing as is_testing, log_advice as log_advice, name_like_string as name_like_string, same_anchor as same_anchor, scol_for as scol_for, validate_arguments_and_invoke_function as validate_arguments_and_invoke_function, validate_axis as validate_axis, validate_bool_kwarg as validate_bool_kwarg, validate_how as validate_how, validate_mode as validate_mode, verify_temp_column_name as verify_temp_column_name
from pyspark.sql import Column as Column, DataFrame as SparkDataFrame
from pyspark.sql._typing import OptionalPrimitiveType as OptionalPrimitiveType
from pyspark.sql.functions import pandas_udf as pandas_udf
from pyspark.sql.types import ArrayType as ArrayType, BooleanType as BooleanType, DataType as DataType, DecimalType as DecimalType, DoubleType as DoubleType, NumericType as NumericType, Row as Row, StringType as StringType, StructField as StructField, StructType as StructType, TimestampNTZType as TimestampNTZType, TimestampType as TimestampType
from pyspark.sql.window import Window as Window
from types import TracebackType
from typing import Any, Callable, Dict, Generic, IO, Iterable, Iterator, List, Sequence, Tuple, Type

REPR_PATTERN: Incomplete
REPR_HTML_PATTERN: Incomplete

class DataFrame(Frame, Generic[T]):
    '''
    pandas-on-Spark DataFrame that corresponds to pandas DataFrame logically. This holds Spark
    DataFrame internally.

    :ivar _internal: an internal immutable Frame to manage metadata.
    :type _internal: InternalFrame

    Parameters
    ----------
    data : numpy ndarray (structured or homogeneous), dict, pandas DataFrame,
        Spark DataFrame, pandas-on-Spark DataFrame or pandas-on-Spark Series.
        Dict can contain Series, arrays, constants, or list-like objects
    index : Index or array-like
        Index to use for the resulting frame. Will default to RangeIndex if
        no indexing information part of input data and no index provided
    columns : Index or array-like
        Column labels to use for the resulting frame. Will default to
        RangeIndex (0, 1, 2, ..., n) if no column labels are provided
    dtype : dtype, default None
        Data type to force. Only a single dtype is allowed. If None, infer
    copy : boolean, default False
        Copy data from inputs. Only affects DataFrame / 2d ndarray input

    .. versionchanged:: 3.4.0
        Since 3.4.0, it deals with `data` and `index` in this approach:
        1, when `data` is a distributed dataset (Internal DataFrame/Spark DataFrame/
        pandas-on-Spark DataFrame/pandas-on-Spark Series), it will first parallelize
        the `index` if necessary, and then try to combine the `data` and `index`;
        Note that if `data` and `index` doesn\'t have the same anchor, then
        `compute.ops_on_diff_frames` should be turned on;
        2, when `data` is a local dataset (Pandas DataFrame/numpy ndarray/list/etc),
        it will first collect the `index` to driver if necessary, and then apply
        the `Pandas.DataFrame(...)` creation internally;

    Examples
    --------
    Constructing DataFrame from a dictionary.

    >>> d = {\'col1\': [1, 2], \'col2\': [3, 4]}
    >>> df = ps.DataFrame(data=d, columns=[\'col1\', \'col2\'])
    >>> df
       col1  col2
    0     1     3
    1     2     4

    Constructing DataFrame from pandas DataFrame

    >>> df = ps.DataFrame(pd.DataFrame(data=d, columns=[\'col1\', \'col2\']))
    >>> df
       col1  col2
    0     1     3
    1     2     4

    Notice that the inferred dtype is int64.

    >>> df.dtypes
    col1    int64
    col2    int64
    dtype: object

    To enforce a single dtype:

    >>> df = ps.DataFrame(data=d, dtype=np.int8)
    >>> df.dtypes
    col1    int8
    col2    int8
    dtype: object

    Constructing DataFrame from numpy ndarray:

    >>> import numpy as np
    >>> ps.DataFrame(data=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]),
    ...     columns=[\'a\', \'b\', \'c\', \'d\', \'e\'])
       a  b  c  d  e
    0  1  2  3  4  5
    1  6  7  8  9  0

    Constructing DataFrame from numpy ndarray with Pandas index:

    >>> import numpy as np
    >>> import pandas as pd

    >>> ps.DataFrame(data=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]),
    ...     index=pd.Index([1, 4]), columns=[\'a\', \'b\', \'c\', \'d\', \'e\'])
       a  b  c  d  e
    1  1  2  3  4  5
    4  6  7  8  9  0

    Constructing DataFrame from numpy ndarray with pandas-on-Spark index:

    >>> import numpy as np
    >>> import pandas as pd
    >>> ps.DataFrame(data=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]),
    ...     index=ps.Index([1, 4]), columns=[\'a\', \'b\', \'c\', \'d\', \'e\'])
       a  b  c  d  e
    1  1  2  3  4  5
    4  6  7  8  9  0

    Constructing DataFrame from Pandas DataFrame with Pandas index:

    >>> import numpy as np
    >>> import pandas as pd
    >>> pdf = pd.DataFrame(data=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]),
    ...     columns=[\'a\', \'b\', \'c\', \'d\', \'e\'])
    >>> ps.DataFrame(data=pdf, index=pd.Index([1, 4]))
         a    b    c    d    e
    1  6.0  7.0  8.0  9.0  0.0
    4  NaN  NaN  NaN  NaN  NaN

    Constructing DataFrame from Pandas DataFrame with pandas-on-Spark index:

    >>> import numpy as np
    >>> import pandas as pd
    >>> pdf = pd.DataFrame(data=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]),
    ...     columns=[\'a\', \'b\', \'c\', \'d\', \'e\'])
    >>> ps.DataFrame(data=pdf, index=ps.Index([1, 4]))
         a    b    c    d    e
    1  6.0  7.0  8.0  9.0  0.0
    4  NaN  NaN  NaN  NaN  NaN

    Constructing DataFrame from Spark DataFrame with Pandas index:

    >>> import pandas as pd
    >>> sdf = spark.createDataFrame([("Data", 1), ("Bricks", 2)], ["x", "y"])
    >>> ps.DataFrame(data=sdf, index=pd.Index([0, 1, 2]))
    Traceback (most recent call last):
      ...
    ValueError: Cannot combine the series or dataframe...\'compute.ops_on_diff_frames\' option.

    Enable \'compute.ops_on_diff_frames\' to combine SparkDataFrame and Pandas index

    >>> with ps.option_context("compute.ops_on_diff_frames", True):
    ...     ps.DataFrame(data=sdf, index=pd.Index([0, 1, 2]))
            x    y
    0    Data  1.0
    1  Bricks  2.0
    2    None  NaN

    Constructing DataFrame from Spark DataFrame with pandas-on-Spark index:

    >>> import pandas as pd
    >>> sdf = spark.createDataFrame([("Data", 1), ("Bricks", 2)], ["x", "y"])
    >>> ps.DataFrame(data=sdf, index=ps.Index([0, 1, 2]))
    Traceback (most recent call last):
      ...
    ValueError: Cannot combine the series or dataframe...\'compute.ops_on_diff_frames\' option.

    Enable \'compute.ops_on_diff_frames\' to combine Spark DataFrame and pandas-on-Spark index

    >>> with ps.option_context("compute.ops_on_diff_frames", True):
    ...     ps.DataFrame(data=sdf, index=ps.Index([0, 1, 2]))
            x    y
    0    Data  1.0
    1  Bricks  2.0
    2    None  NaN
    '''
    def __init__(self, data: Incomplete | None = None, index: Incomplete | None = None, columns: Incomplete | None = None, dtype: Incomplete | None = None, copy: bool = False) -> None: ...
    @property
    def ndim(self) -> int:
        """
        Return an int representing the number of array dimensions.

        return 2 for DataFrame.

        Examples
        --------

        >>> df = ps.DataFrame([[1, 2], [4, 5], [7, 8]],
        ...                   index=['cobra', 'viper', None],
        ...                   columns=['max_speed', 'shield'])
        >>> df  # doctest: +SKIP
               max_speed  shield
        cobra          1       2
        viper          4       5
        None           7       8
        >>> df.ndim
        2
        """
    @property
    def axes(self) -> List:
        """
        Return a list representing the axes of the DataFrame.

        It has the row axis labels and column axis labels as the only members.
        They are returned in that order.

        Examples
        --------

        >>> df = ps.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.axes
        [Int64Index([0, 1], dtype='int64'), Index(['col1', 'col2'], dtype='object')]
        """
    def __add__(self, other: Any) -> DataFrame: ...
    def __radd__(self, other: Any) -> DataFrame: ...
    def __truediv__(self, other: Any) -> DataFrame: ...
    def __rtruediv__(self, other: Any) -> DataFrame: ...
    def __mul__(self, other: Any) -> DataFrame: ...
    def __rmul__(self, other: Any) -> DataFrame: ...
    def __sub__(self, other: Any) -> DataFrame: ...
    def __rsub__(self, other: Any) -> DataFrame: ...
    def __pow__(self, other: Any) -> DataFrame: ...
    def __rpow__(self, other: Any) -> DataFrame: ...
    def __mod__(self, other: Any) -> DataFrame: ...
    def __rmod__(self, other: Any) -> DataFrame: ...
    def __floordiv__(self, other: Any) -> DataFrame: ...
    def __rfloordiv__(self, other: Any) -> DataFrame: ...
    def __abs__(self) -> DataFrame: ...
    def __neg__(self) -> DataFrame: ...
    def add(self, other: Any) -> DataFrame: ...
    plot: Incomplete
    spark: Incomplete
    pandas_on_spark: Incomplete
    koalas: Incomplete
    def hist(self, bins: int = 10, **kwds): ...
    def boxplot(self, **kwds): ...
    def kde(self, bw_method: Incomplete | None = None, ind: Incomplete | None = None, **kwds): ...
    def radd(self, other: Any) -> DataFrame: ...
    def div(self, other: Any) -> DataFrame: ...
    divide = div
    def rdiv(self, other: Any) -> DataFrame: ...
    def truediv(self, other: Any) -> DataFrame: ...
    def rtruediv(self, other: Any) -> DataFrame: ...
    def mul(self, other: Any) -> DataFrame: ...
    multiply = mul
    def rmul(self, other: Any) -> DataFrame: ...
    def sub(self, other: Any) -> DataFrame: ...
    subtract = sub
    def rsub(self, other: Any) -> DataFrame: ...
    def mod(self, other: Any) -> DataFrame: ...
    def rmod(self, other: Any) -> DataFrame: ...
    def pow(self, other: Any) -> DataFrame: ...
    def rpow(self, other: Any) -> DataFrame: ...
    def floordiv(self, other: Any) -> DataFrame: ...
    def rfloordiv(self, other: Any) -> DataFrame: ...
    def __eq__(self, other: Any) -> DataFrame: ...
    def __ne__(self, other: Any) -> DataFrame: ...
    def __lt__(self, other: Any) -> DataFrame: ...
    def __le__(self, other: Any) -> DataFrame: ...
    def __ge__(self, other: Any) -> DataFrame: ...
    def __gt__(self, other: Any) -> DataFrame: ...
    def eq(self, other: Any) -> DataFrame:
        """
        Compare if the current value is equal to the other.

        >>> df = ps.DataFrame({'a': [1, 2, 3, 4],
        ...                    'b': [1, np.nan, 1, np.nan]},
        ...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

        >>> df.eq(1)
               a      b
        a   True   True
        b  False  False
        c  False   True
        d  False  False
        """
    equals = eq
    def gt(self, other: Any) -> DataFrame:
        """
        Compare if the current value is greater than the other.

        >>> df = ps.DataFrame({'a': [1, 2, 3, 4],
        ...                    'b': [1, np.nan, 1, np.nan]},
        ...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

        >>> df.gt(2)
               a      b
        a  False  False
        b  False  False
        c   True  False
        d   True  False
        """
    def ge(self, other: Any) -> DataFrame:
        """
        Compare if the current value is greater than or equal to the other.

        >>> df = ps.DataFrame({'a': [1, 2, 3, 4],
        ...                    'b': [1, np.nan, 1, np.nan]},
        ...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

        >>> df.ge(1)
              a      b
        a  True   True
        b  True  False
        c  True   True
        d  True  False
        """
    def lt(self, other: Any) -> DataFrame:
        """
        Compare if the current value is less than the other.

        >>> df = ps.DataFrame({'a': [1, 2, 3, 4],
        ...                    'b': [1, np.nan, 1, np.nan]},
        ...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

        >>> df.lt(1)
               a      b
        a  False  False
        b  False  False
        c  False  False
        d  False  False
        """
    def le(self, other: Any) -> DataFrame:
        """
        Compare if the current value is less than or equal to the other.

        >>> df = ps.DataFrame({'a': [1, 2, 3, 4],
        ...                    'b': [1, np.nan, 1, np.nan]},
        ...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

        >>> df.le(2)
               a      b
        a   True   True
        b   True  False
        c  False   True
        d  False  False
        """
    def ne(self, other: Any) -> DataFrame:
        """
        Compare if the current value is not equal to the other.

        >>> df = ps.DataFrame({'a': [1, 2, 3, 4],
        ...                    'b': [1, np.nan, 1, np.nan]},
        ...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

        >>> df.ne(1)
               a      b
        a  False  False
        b   True   True
        c   True  False
        d   True   True
        """
    def applymap(self, func: Callable[[Any], Any]) -> DataFrame:
        """
        Apply a function to a Dataframe elementwise.

        This method applies a function that accepts and returns a scalar
        to every element of a DataFrame.

        .. note:: this API executes the function once to infer the type which is
             potentially expensive, for instance, when the dataset is created after
             aggregations or sorting.

             To avoid this, specify return type in ``func``, for instance, as below:

             >>> def square(x) -> np.int32:
             ...     return x ** 2

             pandas-on-Spark uses return type hints and does not try to infer the type.

        Parameters
        ----------
        func : callable
            Python function returns a single value from a single value.

        Returns
        -------
        DataFrame
            Transformed DataFrame.

        Examples
        --------
        >>> df = ps.DataFrame([[1, 2.12], [3.356, 4.567]])
        >>> df
               0      1
        0  1.000  2.120
        1  3.356  4.567

        >>> def str_len(x) -> int:
        ...     return len(str(x))
        >>> df.applymap(str_len)
           0  1
        0  3  4
        1  5  5

        >>> def power(x) -> float:
        ...     return x ** 2
        >>> df.applymap(power)
                   0          1
        0   1.000000   4.494400
        1  11.262736  20.857489

        You can omit type hints and let pandas-on-Spark infer its type.

        >>> df.applymap(lambda x: x ** 2)
                   0          1
        0   1.000000   4.494400
        1  11.262736  20.857489
        """
    def aggregate(self, func: List[str] | Dict[Name, List[str]]) -> DataFrame:
        '''Aggregate using one or more operations over the specified axis.

        Parameters
        ----------
        func : dict or a list
             a dict mapping from column name (string) to
             aggregate functions (list of strings).
             If a list is given, the aggregation is performed against
             all columns.

        Returns
        -------
        DataFrame

        Notes
        -----
        `agg` is an alias for `aggregate`. Use the alias.

        See Also
        --------
        DataFrame.apply : Invoke function on DataFrame.
        DataFrame.transform : Only perform transforming type operations.
        DataFrame.groupby : Perform operations over groups.
        Series.aggregate : The equivalent function for Series.

        Examples
        --------
        >>> df = ps.DataFrame([[1, 2, 3],
        ...                    [4, 5, 6],
        ...                    [7, 8, 9],
        ...                    [np.nan, np.nan, np.nan]],
        ...                   columns=[\'A\', \'B\', \'C\'])

        >>> df
             A    B    C
        0  1.0  2.0  3.0
        1  4.0  5.0  6.0
        2  7.0  8.0  9.0
        3  NaN  NaN  NaN

        Aggregate these functions over the rows.

        >>> df.agg([\'sum\', \'min\'])[[\'A\', \'B\', \'C\']].sort_index()
                A     B     C
        min   1.0   2.0   3.0
        sum  12.0  15.0  18.0

        Different aggregations per column.

        >>> df.agg({\'A\' : [\'sum\', \'min\'], \'B\' : [\'min\', \'max\']})[[\'A\', \'B\']].sort_index()
                A    B
        max   NaN  8.0
        min   1.0  2.0
        sum  12.0  NaN

        For multi-index columns:

        >>> df.columns = pd.MultiIndex.from_tuples([("X", "A"), ("X", "B"), ("Y", "C")])
        >>> df.agg([\'sum\', \'min\'])[[("X", "A"), ("X", "B"), ("Y", "C")]].sort_index()
                X           Y
                A     B     C
        min   1.0   2.0   3.0
        sum  12.0  15.0  18.0

        >>> aggregated = df.agg({("X", "A") : [\'sum\', \'min\'], ("X", "B") : [\'min\', \'max\']})
        >>> aggregated[[("X", "A"), ("X", "B")]].sort_index()  # doctest: +NORMALIZE_WHITESPACE
                X
                A    B
        max   NaN  8.0
        min   1.0  2.0
        sum  12.0  NaN
        '''
    agg = aggregate
    def corr(self, method: str = 'pearson', min_periods: int | None = None) -> DataFrame:
        """
        Compute pairwise correlation of columns, excluding NA/null values.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        method : {'pearson', 'spearman', 'kendall'}
            * pearson : standard correlation coefficient
            * spearman : Spearman rank correlation
            * kendall : Kendall Tau correlation coefficient

            .. versionchanged:: 3.4.0
               support 'kendall' for method parameter
        min_periods : int, optional
            Minimum number of observations required per pair of columns
            to have a valid result.

            .. versionadded:: 3.4.0

        Returns
        -------
        DataFrame

        See Also
        --------
        DataFrame.corrwith
        Series.corr

        Notes
        -----
        1. Pearson, Kendall and Spearman correlation are currently computed using pairwise
           complete observations.

        2. The complexity of Kendall correlation is O(#row * #row), if the dataset is too
           large, sampling ahead of correlation computation is recommended.

        Examples
        --------
        >>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
        ...                   columns=['dogs', 'cats'])
        >>> df.corr('pearson')
                  dogs      cats
        dogs  1.000000 -0.851064
        cats -0.851064  1.000000

        >>> df.corr('spearman')
                  dogs      cats
        dogs  1.000000 -0.948683
        cats -0.948683  1.000000

        >>> df.corr('kendall')
                  dogs      cats
        dogs  1.000000 -0.912871
        cats -0.912871  1.000000
        """
    def corrwith(self, other: DataFrameOrSeries, axis: Axis = 0, drop: bool = False, method: str = 'pearson') -> Series:
        '''
        Compute pairwise correlation.

        Pairwise correlation is computed between rows or columns of
        DataFrame with rows or columns of Series or DataFrame. DataFrames
        are first aligned along both axes before computing the
        correlations.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        other : DataFrame, Series
            Object with which to compute correlations.
        axis : int, default 0 or \'index\'
            Can only be set to 0 now.
        drop : bool, default False
            Drop missing indices from result.
        method : {\'pearson\', \'spearman\', \'kendall\'}
            * pearson : standard correlation coefficient
            * spearman : Spearman rank correlation
            * kendall : Kendall Tau correlation coefficient

        Returns
        -------
        Series
            Pairwise correlations.

        See Also
        --------
        DataFrame.corr : Compute pairwise correlation of columns.

        Examples
        --------
        >>> df1 = ps.DataFrame({
        ...         "A":[1, 5, 7, 8],
        ...         "X":[5, 8, 4, 3],
        ...         "C":[10, 4, 9, 3]})
        >>> df1.corrwith(df1[["X", "C"]]).sort_index()
        A    NaN
        C    1.0
        X    1.0
        dtype: float64

        >>> df2 = ps.DataFrame({
        ...         "A":[5, 3, 6, 4],
        ...         "B":[11, 2, 4, 3],
        ...         "C":[4, 3, 8, 5]})

        >>> with ps.option_context("compute.ops_on_diff_frames", True):
        ...     df1.corrwith(df2).sort_index()
        A   -0.041703
        B         NaN
        C    0.395437
        X         NaN
        dtype: float64

        >>> with ps.option_context("compute.ops_on_diff_frames", True):
        ...     df1.corrwith(df2, method="kendall").sort_index()
        A    0.0
        B    NaN
        C    0.0
        X    NaN
        dtype: float64

        >>> with ps.option_context("compute.ops_on_diff_frames", True):
        ...     df1.corrwith(df2.B, method="spearman").sort_index()
        A   -0.4
        C    0.8
        X   -0.2
        dtype: float64

        >>> with ps.option_context("compute.ops_on_diff_frames", True):
        ...     df2.corrwith(df1.X).sort_index()
        A   -0.597614
        B   -0.151186
        C   -0.642857
        dtype: float64
        '''
    def items(self) -> Iterator[Tuple[Name, 'Series']]:
        """
        Iterator over (column name, Series) pairs.

        Iterates over the DataFrame columns, returning a tuple with
        the column name and the content as a Series.

        Returns
        -------
        label : object
            The column names for the DataFrame being iterated over.
        content : Series
            The column entries belonging to each label, as a Series.

        Examples
        --------
        >>> df = ps.DataFrame({'species': ['bear', 'bear', 'marsupial'],
        ...                    'population': [1864, 22000, 80000]},
        ...                   index=['panda', 'polar', 'koala'],
        ...                   columns=['species', 'population'])
        >>> df
                 species  population
        panda       bear        1864
        polar       bear       22000
        koala  marsupial       80000

        >>> for label, content in df.iteritems():
        ...    print('label:', label)
        ...    print('content:', content.to_string())
        ...
        label: species
        content: panda         bear
        polar         bear
        koala    marsupial
        label: population
        content: panda     1864
        polar    22000
        koala    80000
        """
    def iterrows(self) -> Iterator[Tuple[Name, pd.Series]]:
        """
        Iterate over DataFrame rows as (index, Series) pairs.

        Yields
        ------
        index : label or tuple of label
            The index of the row. A tuple for a `MultiIndex`.
        data : pandas.Series
            The data of the row as a Series.

        it : generator
            A generator that iterates over the rows of the frame.

        Notes
        -----

        1. Because ``iterrows`` returns a Series for each row,
           it does **not** preserve dtypes across the rows (dtypes are
           preserved across columns for DataFrames). For example,

           >>> df = ps.DataFrame([[1, 1.5]], columns=['int', 'float'])
           >>> row = next(df.iterrows())[1]
           >>> row
           int      1.0
           float    1.5
           Name: 0, dtype: float64
           >>> print(row['int'].dtype)
           float64
           >>> print(df['int'].dtype)
           int64

           To preserve dtypes while iterating over the rows, it is better
           to use :meth:`itertuples` which returns namedtuples of the values
           and which is generally faster than ``iterrows``.

        2. You should **never modify** something you are iterating over.
           This is not guaranteed to work in all cases. Depending on the
           data types, the iterator returns a copy and not a view, and writing
           to it will have no effect.
        """
    def itertuples(self, index: bool = True, name: str | None = 'PandasOnSpark') -> Iterator[Tuple]:
        '''
        Iterate over DataFrame rows as namedtuples.

        Parameters
        ----------
        index : bool, default True
            If True, return the index as the first element of the tuple.
        name : str or None, default "PandasOnSpark"
            The name of the returned namedtuples or None to return regular
            tuples.

        Returns
        -------
        iterator
            An object to iterate over namedtuples for each row in the
            DataFrame with the first field possibly being the index and
            following fields being the column values.

        See Also
        --------
        DataFrame.iterrows : Iterate over DataFrame rows as (index, Series)
            pairs.
        DataFrame.items : Iterate over (column name, Series) pairs.

        Notes
        -----
        The column names will be renamed to positional names if they are
        invalid Python identifiers, repeated, or start with an underscore.
        On python versions < 3.7 regular tuples are returned for DataFrames
        with many columns (>254).

        Examples
        --------
        >>> df = ps.DataFrame({\'num_legs\': [4, 2], \'num_wings\': [0, 2]},
        ...                   index=[\'dog\', \'hawk\'])
        >>> df
              num_legs  num_wings
        dog          4          0
        hawk         2          2

        >>> for row in df.itertuples():
        ...     print(row)
        ...
        PandasOnSpark(Index=\'dog\', num_legs=4, num_wings=0)
        PandasOnSpark(Index=\'hawk\', num_legs=2, num_wings=2)

        By setting the `index` parameter to False we can remove the index
        as the first element of the tuple:

        >>> for row in df.itertuples(index=False):
        ...     print(row)
        ...
        PandasOnSpark(num_legs=4, num_wings=0)
        PandasOnSpark(num_legs=2, num_wings=2)

        With the `name` parameter set we set a custom name for the yielded
        namedtuples:

        >>> for row in df.itertuples(name=\'Animal\'):
        ...     print(row)
        ...
        Animal(Index=\'dog\', num_legs=4, num_wings=0)
        Animal(Index=\'hawk\', num_legs=2, num_wings=2)
        '''
    def iteritems(self) -> Iterator[Tuple[Name, 'Series']]:
        """
        This is an alias of ``items``.

        .. deprecated:: 3.4.0
            iteritems is deprecated and will be removed in a future version.
            Use .items instead.
        """
    def to_clipboard(self, excel: bool = True, sep: str | None = None, **kwargs: Any) -> None:
        """
        Copy object to the system clipboard.

        Write a text representation of object to the system clipboard.
        This can be pasted into Excel, for example.

        .. note:: This method should only be used if the resulting DataFrame is expected
            to be small, as all the data is loaded into the driver's memory.

        Parameters
        ----------
        excel : bool, default True
            - True, use the provided separator, writing in a csv format for
              allowing easy pasting into excel.
            - False, write a string representation of the object to the
              clipboard.

        sep : str, default ``'\\t'``
            Field delimiter.
        **kwargs
            These parameters will be passed to DataFrame.to_csv.

        Notes
        -----
        Requirements for your platform.

          - Linux : `xclip`, or `xsel` (with `gtk` or `PyQt4` modules)
          - Windows : none
          - OS X : none

        See Also
        --------
        read_clipboard : Read text from clipboard.

        Examples
        --------
        Copy the contents of a DataFrame to the clipboard.

        >>> df = ps.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])  # doctest: +SKIP
        >>> df.to_clipboard(sep=',')  # doctest: +SKIP
        ... # Wrote the following to the system clipboard:
        ... # ,A,B,C
        ... # 0,1,2,3
        ... # 1,4,5,6

        We can omit the index by passing the keyword `index` and setting
        it to false.

        >>> df.to_clipboard(sep=',', index=False)  # doctest: +SKIP
        ... # Wrote the following to the system clipboard:
        ... # A,B,C
        ... # 1,2,3
        ... # 4,5,6

        This function also works for Series:

        >>> df = ps.Series([1, 2, 3, 4, 5, 6, 7], name='x')  # doctest: +SKIP
        >>> df.to_clipboard(sep=',')  # doctest: +SKIP
        ... # Wrote the following to the system clipboard:
        ... # 0, 1
        ... # 1, 2
        ... # 2, 3
        ... # 3, 4
        ... # 4, 5
        ... # 5, 6
        ... # 6, 7
        """
    def to_html(self, buf: IO[str] | None = None, columns: Sequence[Name] | None = None, col_space: str | int | Dict[Name, str | int] | None = None, header: bool = True, index: bool = True, na_rep: str = 'NaN', formatters: List[Callable[[Any], str]] | Dict[Name, Callable[[Any], str]] | None = None, float_format: Callable[[float], str] | None = None, sparsify: bool | None = None, index_names: bool = True, justify: str | None = None, max_rows: int | None = None, max_cols: int | None = None, show_dimensions: bool = False, decimal: str = '.', bold_rows: bool = True, classes: str | list | tuple | None = None, escape: bool = True, notebook: bool = False, border: int | None = None, table_id: str | None = None, render_links: bool = False) -> str | None:
        """
        Render a DataFrame as an HTML table.

        .. note:: This method should only be used if the resulting pandas object is expected
                  to be small, as all the data is loaded into the driver's memory. If the input
                  is large, set max_rows parameter.

        Parameters
        ----------
        buf : StringIO-like, optional
            Buffer to write to.
        columns : sequence, optional, default None
            The subset of columns to write. Writes all columns by default.
        col_space : int, optional
            The minimum width of each column.
        header : bool, optional
            Write out the column names. If a list of strings is given, it
            is assumed to be aliases for the column names
        index : bool, optional, default True
            Whether to print index (row) labels.
        na_rep : str, optional, default 'NaN'
            String representation of NAN to use.
        formatters : list or dict of one-param. functions, optional
            Formatter functions to apply to columns' elements by position or
            name.
            The result of each function must be a Unicode string.
            List must be of length equal to the number of columns.
        float_format : one-parameter function, optional, default None
            Formatter function to apply to columns' elements if they are
            floats. The result of this function must be a Unicode string.
        sparsify : bool, optional, default True
            Set to False for a DataFrame with a hierarchical index to print
            every multiindex key at each row.
        index_names : bool, optional, default True
            Prints the names of the indexes.
        justify : str, default None
            How to justify the column labels. If None uses the option from
            the print configuration (controlled by set_option), 'right' out
            of the box. Valid values are

            * left
            * right
            * center
            * justify
            * justify-all
            * start
            * end
            * inherit
            * match-parent
            * initial
            * unset.
        max_rows : int, optional
            Maximum number of rows to display in the console.
        max_cols : int, optional
            Maximum number of columns to display in the console.
        show_dimensions : bool, default False
            Display DataFrame dimensions (number of rows by number of columns).
        decimal : str, default '.'
            Character recognized as decimal separator, e.g. ',' in Europe.
        bold_rows : bool, default True
            Make the row labels bold in the output.
        classes : str or list or tuple, default None
            CSS class(es) to apply to the resulting html table.
        escape : bool, default True
            Convert the characters <, >, and & to HTML-safe sequences.
        notebook : {True, False}, default False
            Whether the generated HTML is for IPython Notebook.
        border : int
            A ``border=border`` attribute is included in the opening
            `<table>` tag. By default ``pd.options.html.border``.
        table_id : str, optional
            A css id is included in the opening `<table>` tag if specified.
        render_links : bool, default False
            Convert URLs to HTML links (only works with pandas 0.24+).

        Returns
        -------
        str (or Unicode, depending on data and options)
            String representation of the dataframe.

        See Also
        --------
        to_string : Convert DataFrame to a string.
        """
    def to_string(self, buf: IO[str] | None = None, columns: Sequence[Name] | None = None, col_space: str | int | Dict[Name, str | int] | None = None, header: bool = True, index: bool = True, na_rep: str = 'NaN', formatters: List[Callable[[Any], str]] | Dict[Name, Callable[[Any], str]] | None = None, float_format: Callable[[float], str] | None = None, sparsify: bool | None = None, index_names: bool = True, justify: str | None = None, max_rows: int | None = None, max_cols: int | None = None, show_dimensions: bool = False, decimal: str = '.', line_width: int | None = None) -> str | None:
        """
        Render a DataFrame to a console-friendly tabular output.

        .. note:: This method should only be used if the resulting pandas object is expected
                  to be small, as all the data is loaded into the driver's memory. If the input
                  is large, set max_rows parameter.

        Parameters
        ----------
        buf : StringIO-like, optional
            Buffer to write to.
        columns : sequence, optional, default None
            The subset of columns to write. Writes all columns by default.
        col_space : int, optional
            The minimum width of each column.
        header : bool, optional
            Write out the column names. If a list of strings is given, it
            is assumed to be aliases for the column names
        index : bool, optional, default True
            Whether to print index (row) labels.
        na_rep : str, optional, default 'NaN'
            String representation of NAN to use.
        formatters : list or dict of one-param. functions, optional
            Formatter functions to apply to columns' elements by position or
            name.
            The result of each function must be a Unicode string.
            List must be of length equal to the number of columns.
        float_format : one-parameter function, optional, default None
            Formatter function to apply to columns' elements if they are
            floats. The result of this function must be a Unicode string.
        sparsify : bool, optional, default True
            Set to False for a DataFrame with a hierarchical index to print
            every multiindex key at each row.
        index_names : bool, optional, default True
            Prints the names of the indexes.
        justify : str, default None
            How to justify the column labels. If None uses the option from
            the print configuration (controlled by set_option), 'right' out
            of the box. Valid values are

            * left
            * right
            * center
            * justify
            * justify-all
            * start
            * end
            * inherit
            * match-parent
            * initial
            * unset.
        max_rows : int, optional
            Maximum number of rows to display in the console.
        max_cols : int, optional
            Maximum number of columns to display in the console.
        show_dimensions : bool, default False
            Display DataFrame dimensions (number of rows by number of columns).
        decimal : str, default '.'
            Character recognized as decimal separator, e.g. ',' in Europe.
        line_width : int, optional
            Width to wrap a line in characters.

        Returns
        -------
        str (or Unicode, depending on data and options)
            String representation of the dataframe.

        See Also
        --------
        to_html : Convert DataFrame to HTML.

        Examples
        --------
        >>> df = ps.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]}, columns=['col1', 'col2'])
        >>> print(df.to_string())
           col1  col2
        0     1     4
        1     2     5
        2     3     6

        >>> print(df.to_string(max_rows=2))
           col1  col2
        0     1     4
        1     2     5
        """
    def to_dict(self, orient: str = 'dict', into: Type = ...) -> List | Mapping:
        """
        Convert the DataFrame to a dictionary.

        The type of the key-value pairs can be customized with the parameters
        (see below).

        .. note:: This method should only be used if the resulting pandas DataFrame is expected
            to be small, as all the data is loaded into the driver's memory.

        Parameters
        ----------
        orient : str {'dict', 'list', 'series', 'split', 'records', 'index'}
            Determines the type of the values of the dictionary.

            - 'dict' (default) : dict like {column -> {index -> value}}
            - 'list' : dict like {column -> [values]}
            - 'series' : dict like {column -> Series(values)}
            - 'split' : dict like
              {'index' -> [index], 'columns' -> [columns], 'data' -> [values]}
            - 'records' : list like
              [{column -> value}, ... , {column -> value}]
            - 'index' : dict like {index -> {column -> value}}

            Abbreviations are allowed. `s` indicates `series` and `sp`
            indicates `split`.

        into : class, default dict
            The collections.abc.Mapping subclass used for all Mappings
            in the return value.  Can be the actual class or an empty
            instance of the mapping type you want.  If you want a
            collections.defaultdict, you must pass it initialized.

        Returns
        -------
        dict, list or collections.abc.Mapping
            Return a collections.abc.Mapping object representing the DataFrame.
            The resulting transformation depends on the `orient` parameter.

        Examples
        --------
        >>> df = ps.DataFrame({'col1': [1, 2],
        ...                    'col2': [0.5, 0.75]},
        ...                   index=['row1', 'row2'],
        ...                   columns=['col1', 'col2'])
        >>> df
              col1  col2
        row1     1  0.50
        row2     2  0.75

        >>> df_dict = df.to_dict()
        >>> sorted([(key, sorted(values.items())) for key, values in df_dict.items()])
        [('col1', [('row1', 1), ('row2', 2)]), ('col2', [('row1', 0.5), ('row2', 0.75)])]

        You can specify the return orientation.

        >>> df_dict = df.to_dict('series')
        >>> sorted(df_dict.items())
        [('col1', row1    1
        row2    2
        Name: col1, dtype: int64), ('col2', row1    0.50
        row2    0.75
        Name: col2, dtype: float64)]

        >>> df_dict = df.to_dict('split')
        >>> sorted(df_dict.items())  # doctest: +ELLIPSIS
        [('columns', ['col1', 'col2']), ('data', [[1..., 0.75]]), ('index', ['row1', 'row2'])]

        >>> df_dict = df.to_dict('records')
        >>> [sorted(values.items()) for values in df_dict]  # doctest: +ELLIPSIS
        [[('col1', 1...), ('col2', 0.5)], [('col1', 2...), ('col2', 0.75)]]

        >>> df_dict = df.to_dict('index')
        >>> sorted([(key, sorted(values.items())) for key, values in df_dict.items()])
        [('row1', [('col1', 1), ('col2', 0.5)]), ('row2', [('col1', 2), ('col2', 0.75)])]

        You can also specify the mapping type.

        >>> from collections import OrderedDict, defaultdict
        >>> df.to_dict(into=OrderedDict)
        OrderedDict([('col1', OrderedDict([('row1', 1), ('row2', 2)])), ('col2', OrderedDict([('row1', 0.5), ('row2', 0.75)]))])

        If you want a `defaultdict`, you need to initialize it:

        >>> dd = defaultdict(list)
        >>> df.to_dict('records', into=dd)  # doctest: +ELLIPSIS
        [defaultdict(<class 'list'>, {'col..., 'col...}), defaultdict(<class 'list'>, {'col..., 'col...})]
        """
    def to_latex(self, buf: IO[str] | None = None, columns: List[Name] | None = None, col_space: int | None = None, header: bool = True, index: bool = True, na_rep: str = 'NaN', formatters: List[Callable[[Any], str]] | Dict[Name, Callable[[Any], str]] | None = None, float_format: Callable[[float], str] | None = None, sparsify: bool | None = None, index_names: bool = True, bold_rows: bool = False, column_format: str | None = None, longtable: bool | None = None, escape: bool | None = None, encoding: str | None = None, decimal: str = '.', multicolumn: bool | None = None, multicolumn_format: str | None = None, multirow: bool | None = None) -> str | None:
        """
        Render an object to a LaTeX tabular environment table.

        Render an object to a tabular environment table. You can splice this into a LaTeX
        document. Requires usepackage{booktabs}.

        .. note:: This method should only be used if the resulting pandas object is expected
                  to be small, as all the data is loaded into the driver's memory. If the input
                  is large, consider alternative formats.

        Parameters
        ----------
        buf : file descriptor or None
            Buffer to write to. If None, the output is returned as a string.
        columns : list of label, optional
            The subset of columns to write. Writes all columns by default.
        col_space : int, optional
            The minimum width of each column.

            .. deprecated:: 3.4.0

        header : bool or list of str, default True
            Write out the column names. If a list of strings is given, it is assumed to be aliases
            for the column names.
        index : bool, default True
            Write row names (index).
        na_rep : str, default ‘NaN’
            Missing data representation.
        formatters : list of functions or dict of {str: function}, optional
            Formatter functions to apply to columns’ elements by position or name. The result of
            each function must be a Unicode string. List must be of length equal to the number of
            columns.
        float_format : str, optional
            Format string for floating point numbers.
        sparsify : bool, optional
            Set to False for a DataFrame with a hierarchical index to print every multiindex key at
            each row. By default the value will be read from the config module.
        index_names : bool, default True
            Prints the names of the indexes.
        bold_rows : bool, default False
            Make the row labels bold in the output.
        column_format : str, optional
            The columns format as specified in LaTeX table format e.g. ‘rcl’ for 3 columns. By
            default, ‘l’ will be used for all columns except columns of numbers, which default
            to ‘r’.
        longtable : bool, optional
            By default the value will be read from the pandas config module. Use a longtable
            environment instead of tabular. Requires adding a usepackage{longtable} to your LaTeX
            preamble.
        escape : bool, optional
            By default the value will be read from the pandas config module. When set to False
            prevents from escaping latex special characters in column names.
        encoding : str, optional
            A string representing the encoding to use in the output file, defaults to ‘ascii’ on
            Python 2 and ‘utf-8’ on Python 3.
        decimal : str, default ‘.’
            Character recognized as decimal separator, e.g. ‘,’ in Europe.
        multicolumn : bool, default True
            Use multicolumn to enhance MultiIndex columns. The default will be read from the config
            module.
        multicolumn_format : str, default ‘l’
            The alignment for multicolumns, similar to column_format The default will be read from
            the config module.
        multirow : bool, default False
            Use multirow to enhance MultiIndex rows. Requires adding a usepackage{multirow} to your
            LaTeX preamble. Will print centered labels (instead of top-aligned) across the contained
            rows, separating groups via clines. The default will be read from the pandas config
            module.

        Returns
        -------
        str or None
            If buf is None, returns the resulting LateX format as a string. Otherwise returns None.

        See Also
        --------
        DataFrame.to_string : Render a DataFrame to a console-friendly
            tabular output.
        DataFrame.to_html : Render a DataFrame as an HTML table.


        Examples
        --------
        >>> df = ps.DataFrame({'name': ['Raphael', 'Donatello'],
        ...                    'mask': ['red', 'purple'],
        ...                    'weapon': ['sai', 'bo staff']},
        ...                   columns=['name', 'mask', 'weapon'])
        >>> print(df.to_latex(index=False)) # doctest: +NORMALIZE_WHITESPACE
        \\begin{tabular}{lll}
        \\toprule
              name &    mask &    weapon \\\\\n        \\midrule
           Raphael &     red &       sai \\\\\n         Donatello &  purple &  bo staff \\\\\n        \\bottomrule
        \\end{tabular}
        """
    def transpose(self) -> DataFrame:
        """
        Transpose index and columns.

        Reflect the DataFrame over its main diagonal by writing rows as columns
        and vice-versa. The property :attr:`.T` is an accessor to the method
        :meth:`transpose`.

        .. note:: This method is based on an expensive operation due to the nature
            of big data. Internally it needs to generate each row for each value, and
            then group twice - it is a huge operation. To prevent misuse, this method
            has the 'compute.max_rows' default limit of input length and raises a ValueError.

                >>> from pyspark.pandas.config import option_context
                >>> with option_context('compute.max_rows', 1000):  # doctest: +NORMALIZE_WHITESPACE
                ...     ps.DataFrame({'a': range(1001)}).transpose()
                Traceback (most recent call last):
                  ...
                ValueError: Current DataFrame's length exceeds the given limit of 1000 rows.
                Please set 'compute.max_rows' by using 'pyspark.pandas.config.set_option'
                to retrieve more than 1000 rows. Note that, before changing the
                'compute.max_rows', this operation is considerably expensive.

        Returns
        -------
        DataFrame
            The transposed DataFrame.

        Notes
        -----
        Transposing a DataFrame with mixed dtypes will result in a homogeneous
        DataFrame with the coerced dtype. For instance, if int and float have
        to be placed in same column, it becomes float. If type coercion is not
        possible, it fails.

        Also, note that the values in index should be unique because they become
        unique column names.

        In addition, if Spark 2.3 is used, the types should always be exactly same.

        Examples
        --------
        **Square DataFrame with homogeneous dtype**

        >>> d1 = {'col1': [1, 2], 'col2': [3, 4]}
        >>> df1 = ps.DataFrame(data=d1, columns=['col1', 'col2'])
        >>> df1
           col1  col2
        0     1     3
        1     2     4

        >>> df1_transposed = df1.T.sort_index()  # doctest: +SKIP
        >>> df1_transposed  # doctest: +SKIP
              0  1
        col1  1  2
        col2  3  4

        When the dtype is homogeneous in the original DataFrame, we get a
        transposed DataFrame with the same dtype:

        >>> df1.dtypes
        col1    int64
        col2    int64
        dtype: object
        >>> df1_transposed.dtypes  # doctest: +SKIP
        0    int64
        1    int64
        dtype: object

        **Non-square DataFrame with mixed dtypes**

        >>> d2 = {'score': [9.5, 8],
        ...       'kids': [0, 0],
        ...       'age': [12, 22]}
        >>> df2 = ps.DataFrame(data=d2, columns=['score', 'kids', 'age'])
        >>> df2
           score  kids  age
        0    9.5     0   12
        1    8.0     0   22

        >>> df2_transposed = df2.T.sort_index()  # doctest: +SKIP
        >>> df2_transposed  # doctest: +SKIP
                  0     1
        age    12.0  22.0
        kids    0.0   0.0
        score   9.5   8.0

        When the DataFrame has mixed dtypes, we get a transposed DataFrame with
        the coerced dtype:

        >>> df2.dtypes
        score    float64
        kids       int64
        age        int64
        dtype: object

        >>> df2_transposed.dtypes  # doctest: +SKIP
        0    float64
        1    float64
        dtype: object
        """
    T: Incomplete
    def apply(self, func: Callable, axis: Axis = 0, args: Sequence[Any] = (), **kwds: Any) -> Series | DataFrame | Index:
        '''
        Apply a function along an axis of the DataFrame.

        Objects passed to the function are Series objects whose index is
        either the DataFrame\'s index (``axis=0``) or the DataFrame\'s columns
        (``axis=1``).

        See also `Transform and apply a function
        <https://spark.apache.org/docs/latest/api/python/user_guide/pandas_on_spark/transform_apply.html>`_.

        .. note:: when `axis` is 0 or \'index\', the `func` is unable to access
            to the whole input series. pandas-on-Spark internally splits the input series into
            multiple batches and calls `func` with each batch multiple times. Therefore, operations
            such as global aggregations are impossible. See the example below.

            >>> # This case does not return the length of whole series but of the batch internally
            ... # used.
            ... def length(s) -> int:
            ...     return len(s)
            ...
            >>> df = ps.DataFrame({\'A\': range(1000)})
            >>> df.apply(length, axis=0)  # doctest: +SKIP
            0     83
            1     83
            2     83
            ...
            10    83
            11    83
            dtype: int32

        .. note:: this API executes the function once to infer the type which is
            potentially expensive, for instance, when the dataset is created after
            aggregations or sorting.

            To avoid this, specify the return type as `Series` or scalar value in ``func``,
            for instance, as below:

            >>> def square(s) -> ps.Series[np.int32]:
            ...     return s ** 2

            pandas-on-Spark uses return type hints and does not try to infer the type.

            In case when axis is 1, it requires to specify `DataFrame` or scalar value
            with type hints as below:

            >>> def plus_one(x) -> ps.DataFrame[int, [float, float]]:
            ...     return x + 1

            If the return type is specified as `DataFrame`, the output column names become
            `c0, c1, c2 ... cn`. These names are positionally mapped to the returned
            DataFrame in ``func``.

            To specify the column names, you can assign them in a pandas style as below:

            >>> def plus_one(x) -> ps.DataFrame[("index", int), [("a", float), ("b", float)]]:
            ...     return x + 1

            >>> pdf = pd.DataFrame({\'a\': [1, 2, 3], \'b\': [3, 4, 5]})
            >>> def plus_one(x) -> ps.DataFrame[
            ...         (pdf.index.name, pdf.index.dtype), zip(pdf.dtypes, pdf.columns)]:
            ...     return x + 1

        Parameters
        ----------
        func : function
            Function to apply to each column or row.
        axis : {0 or \'index\', 1 or \'columns\'}, default 0
            Axis along which the function is applied:

            * 0 or \'index\': apply function to each column.
            * 1 or \'columns\': apply function to each row.
        args : tuple
            Positional arguments to pass to `func` in addition to the
            array/series.
        **kwds
            Additional keyword arguments to pass as keywords arguments to
            `func`.

        Returns
        -------
        Series or DataFrame
            Result of applying ``func`` along the given axis of the
            DataFrame.

        See Also
        --------
        DataFrame.applymap : For elementwise operations.
        DataFrame.aggregate : Only perform aggregating type operations.
        DataFrame.transform : Only perform transforming type operations.
        Series.apply : The equivalent function for Series.

        Examples
        --------
        >>> df = ps.DataFrame([[4, 9]] * 3, columns=[\'A\', \'B\'])
        >>> df
           A  B
        0  4  9
        1  4  9
        2  4  9

        Using a numpy universal function (in this case the same as
        ``np.sqrt(df)``):

        >>> def sqrt(x) -> ps.Series[float]:
        ...     return np.sqrt(x)
        ...
        >>> df.apply(sqrt, axis=0)
             A    B
        0  2.0  3.0
        1  2.0  3.0
        2  2.0  3.0

        You can omit type hints and let pandas-on-Spark infer its type.

        >>> df.apply(np.sqrt, axis=0)
             A    B
        0  2.0  3.0
        1  2.0  3.0
        2  2.0  3.0

        When `axis` is 1 or \'columns\', it applies the function for each row.

        >>> def summation(x) -> np.int64:
        ...     return np.sum(x)
        ...
        >>> df.apply(summation, axis=1)
        0    13
        1    13
        2    13
        dtype: int64

        You can omit type hints and let pandas-on-Spark infer its type.

        >>> df.apply(np.sum, axis=1)
        0    13
        1    13
        2    13
        dtype: int64

        >>> df.apply(max, axis=1)
        0    9
        1    9
        2    9
        dtype: int64

        Returning a list-like will result in a Series

        >>> df.apply(lambda x: [1, 2], axis=1)
        0    [1, 2]
        1    [1, 2]
        2    [1, 2]
        dtype: object

        To specify the types when `axis` is \'1\', it should use DataFrame[...]
        annotation. In this case, the column names are automatically generated.

        >>> def identify(x) -> ps.DataFrame[(\'index\', int), [(\'A\', np.int64), (\'B\', np.int64)]]:
        ...     return x
        ...
        >>> df.apply(identify, axis=1)  # doctest: +NORMALIZE_WHITESPACE
               A  B
        index
        0      4  9
        1      4  9
        2      4  9

        You can also specify extra arguments.

        >>> def plus_two(a, b, c) -> ps.DataFrame[np.int64, [np.int64, np.int64]]:
        ...     return a + b + c
        ...
        >>> df.apply(plus_two, axis=1, args=(1,), c=3)
           c0  c1
        0   8  13
        1   8  13
        2   8  13
        '''
    def transform(self, func: Callable[..., 'Series'], axis: Axis = 0, *args: Any, **kwargs: Any) -> DataFrame:
        """
        Call ``func`` on self producing a Series with transformed values
        and that has the same length as its input.

        See also `Transform and apply a function
        <https://spark.apache.org/docs/latest/api/python/user_guide/pandas_on_spark/transform_apply.html>`_.

        .. note:: this API executes the function once to infer the type which is
             potentially expensive, for instance, when the dataset is created after
             aggregations or sorting.

             To avoid this, specify return type in ``func``, for instance, as below:

             >>> def square(x) -> ps.Series[np.int32]:
             ...     return x ** 2

             pandas-on-Spark uses return type hints and does not try to infer the type.

        .. note:: the series within ``func`` is actually multiple pandas series as the
            segments of the whole pandas-on-Spark series; therefore, the length of each series
            is not guaranteed. As an example, an aggregation against each series
            does work as a global aggregation but an aggregation of each segment. See
            below:

            >>> def func(x) -> ps.Series[np.int32]:
            ...     return x + sum(x)

        Parameters
        ----------
        func : function
            Function to use for transforming the data. It must work when pandas Series
            is passed.
        axis : int, default 0 or 'index'
            Can only be set to 0 now.
        *args
            Positional arguments to pass to func.
        **kwargs
            Keyword arguments to pass to func.

        Returns
        -------
        DataFrame
            A DataFrame that must have the same length as self.

        Raises
        ------
        Exception : If the returned DataFrame has a different length than self.

        See Also
        --------
        DataFrame.aggregate : Only perform aggregating type operations.
        DataFrame.apply : Invoke function on DataFrame.
        Series.transform : The equivalent function for Series.

        Examples
        --------
        >>> df = ps.DataFrame({'A': range(3), 'B': range(1, 4)}, columns=['A', 'B'])
        >>> df
           A  B
        0  0  1
        1  1  2
        2  2  3

        >>> def square(x) -> ps.Series[np.int32]:
        ...     return x ** 2
        >>> df.transform(square)
           A  B
        0  0  1
        1  1  4
        2  4  9

        You can omit type hints and let pandas-on-Spark infer its type.

        >>> df.transform(lambda x: x ** 2)
           A  B
        0  0  1
        1  1  4
        2  4  9

        For multi-index columns:

        >>> df.columns = [('X', 'A'), ('X', 'B')]
        >>> df.transform(square)  # doctest: +NORMALIZE_WHITESPACE
           X
           A  B
        0  0  1
        1  1  4
        2  4  9

        >>> (df * -1).transform(abs)  # doctest: +NORMALIZE_WHITESPACE
           X
           A  B
        0  0  1
        1  1  2
        2  2  3

        You can also specify extra arguments.

        >>> def calculation(x, y, z) -> ps.Series[int]:
        ...     return x ** y + z
        >>> df.transform(calculation, y=10, z=20)  # doctest: +NORMALIZE_WHITESPACE
              X
              A      B
        0    20     21
        1    21   1044
        2  1044  59069
        """
    def pop(self, item: Name) -> DataFrame:
        """
        Return item and drop from frame. Raise KeyError if not found.

        Parameters
        ----------
        item : str
            Label of column to be popped.

        Returns
        -------
        Series

        Examples
        --------
        >>> df = ps.DataFrame([('falcon', 'bird', 389.0),
        ...                    ('parrot', 'bird', 24.0),
        ...                    ('lion', 'mammal', 80.5),
        ...                    ('monkey','mammal', np.nan)],
        ...                   columns=('name', 'class', 'max_speed'))

        >>> df
             name   class  max_speed
        0  falcon    bird      389.0
        1  parrot    bird       24.0
        2    lion  mammal       80.5
        3  monkey  mammal        NaN

        >>> df.pop('class')
        0      bird
        1      bird
        2    mammal
        3    mammal
        Name: class, dtype: object

        >>> df
             name  max_speed
        0  falcon      389.0
        1  parrot       24.0
        2    lion       80.5
        3  monkey        NaN

        Also support for MultiIndex

        >>> df = ps.DataFrame([('falcon', 'bird', 389.0),
        ...                    ('parrot', 'bird', 24.0),
        ...                    ('lion', 'mammal', 80.5),
        ...                    ('monkey','mammal', np.nan)],
        ...                   columns=('name', 'class', 'max_speed'))
        >>> columns = [('a', 'name'), ('a', 'class'), ('b', 'max_speed')]
        >>> df.columns = pd.MultiIndex.from_tuples(columns)
        >>> df
                a                 b
             name   class max_speed
        0  falcon    bird     389.0
        1  parrot    bird      24.0
        2    lion  mammal      80.5
        3  monkey  mammal       NaN

        >>> df.pop('a')
             name   class
        0  falcon    bird
        1  parrot    bird
        2    lion  mammal
        3  monkey  mammal

        >>> df
                  b
          max_speed
        0     389.0
        1      24.0
        2      80.5
        3       NaN
        """
    def xs(self, key: Name, axis: Axis = 0, level: int | None = None) -> DataFrameOrSeries:
        """
        Return cross-section from the DataFrame.

        This method takes a `key` argument to select data at a particular
        level of a MultiIndex.

        Parameters
        ----------
        key : label or tuple of label
            Label contained in the index, or partially in a MultiIndex.
        axis : 0 or 'index', default 0
            Axis to retrieve cross-section on.
            currently only support 0 or 'index'
        level : object, defaults to first n levels (n=1 or len(key))
            In case of a key partially contained in a MultiIndex, indicate
            which levels are used. Levels can be referred by label or position.

        Returns
        -------
        DataFrame or Series
            Cross-section from the original DataFrame
            corresponding to the selected index levels.

        See Also
        --------
        DataFrame.loc : Access a group of rows and columns
            by label(s) or a boolean array.
        DataFrame.iloc : Purely integer-location based indexing
            for selection by position.

        Examples
        --------
        >>> d = {'num_legs': [4, 4, 2, 2],
        ...      'num_wings': [0, 0, 2, 2],
        ...      'class': ['mammal', 'mammal', 'mammal', 'bird'],
        ...      'animal': ['cat', 'dog', 'bat', 'penguin'],
        ...      'locomotion': ['walks', 'walks', 'flies', 'walks']}
        >>> df = ps.DataFrame(data=d)
        >>> df = df.set_index(['class', 'animal', 'locomotion'])
        >>> df  # doctest: +NORMALIZE_WHITESPACE
                                   num_legs  num_wings
        class  animal  locomotion
        mammal cat     walks              4          0
               dog     walks              4          0
               bat     flies              2          2
        bird   penguin walks              2          2

        Get values at specified index

        >>> df.xs('mammal')  # doctest: +NORMALIZE_WHITESPACE
                           num_legs  num_wings
        animal locomotion
        cat    walks              4          0
        dog    walks              4          0
        bat    flies              2          2

        Get values at several indexes

        >>> df.xs(('mammal', 'dog'))  # doctest: +NORMALIZE_WHITESPACE
                    num_legs  num_wings
        locomotion
        walks              4          0

        >>> df.xs(('mammal', 'dog', 'walks'))  # doctest: +NORMALIZE_WHITESPACE
        num_legs     4
        num_wings    0
        Name: (mammal, dog, walks), dtype: int64

        Get values at specified index and level

        >>> df.xs('cat', level=1)  # doctest: +NORMALIZE_WHITESPACE
                           num_legs  num_wings
        class  locomotion
        mammal walks              4          0
        """
    def between_time(self, start_time: datetime.time | str, end_time: datetime.time | str, include_start: bool = True, include_end: bool = True, axis: Axis = 0) -> DataFrame:
        """
        Select values between particular times of the day (example: 9:00-9:30 AM).

        By setting ``start_time`` to be later than ``end_time``,
        you can get the times that are *not* between the two times.

        Parameters
        ----------
        start_time : datetime.time or str
            Initial time as a time filter limit.
        end_time : datetime.time or str
            End time as a time filter limit.
        include_start : bool, default True
            Whether the start time needs to be included in the result.

            .. deprecated:: 3.4.0

        include_end : bool, default True
            Whether the end time needs to be included in the result.

            .. deprecated:: 3.4.0

        axis : {0 or 'index', 1 or 'columns'}, default 0
            Determine range time on index or columns value.

        Returns
        -------
        DataFrame
            Data from the original object filtered to the specified dates range.

        Raises
        ------
        TypeError
            If the index is not  a :class:`DatetimeIndex`

        See Also
        --------
        at_time : Select values at a particular time of the day.
        first : Select initial periods of time series based on a date offset.
        last : Select final periods of time series based on a date offset.
        DatetimeIndex.indexer_between_time : Get just the index locations for
            values between particular times of the day.

        Examples
        --------
        >>> idx = pd.date_range('2018-04-09', periods=4, freq='1D20min')
        >>> psdf = ps.DataFrame({'A': [1, 2, 3, 4]}, index=idx)
        >>> psdf
                             A
        2018-04-09 00:00:00  1
        2018-04-10 00:20:00  2
        2018-04-11 00:40:00  3
        2018-04-12 01:00:00  4

        >>> psdf.between_time('0:15', '0:45')
                             A
        2018-04-10 00:20:00  2
        2018-04-11 00:40:00  3

        You get the times that are *not* between two times by setting
        ``start_time`` later than ``end_time``:

        >>> psdf.between_time('0:45', '0:15')
                             A
        2018-04-09 00:00:00  1
        2018-04-12 01:00:00  4
        """
    def at_time(self, time: datetime.time | str, asof: bool = False, axis: Axis = 0) -> DataFrame:
        """
        Select values at particular time of day (example: 9:30AM).

        Parameters
        ----------
        time : datetime.time or str
        axis : {0 or 'index', 1 or 'columns'}, default 0

        Returns
        -------
        DataFrame

        Raises
        ------
        TypeError
            If the index is not  a :class:`DatetimeIndex`

        See Also
        --------
        between_time : Select values between particular times of the day.
        DatetimeIndex.indexer_at_time : Get just the index locations for
            values at particular time of the day.

        Examples
        --------
        >>> idx = pd.date_range('2018-04-09', periods=4, freq='12H')
        >>> psdf = ps.DataFrame({'A': [1, 2, 3, 4]}, index=idx)
        >>> psdf
                             A
        2018-04-09 00:00:00  1
        2018-04-09 12:00:00  2
        2018-04-10 00:00:00  3
        2018-04-10 12:00:00  4

        >>> psdf.at_time('12:00')
                             A
        2018-04-09 12:00:00  2
        2018-04-10 12:00:00  4
        """
    def where(self, cond: DataFrameOrSeries, other: DataFrameOrSeries | Any = ..., axis: Axis = None) -> DataFrame:
        '''
        Replace values where the condition is False.

        Parameters
        ----------
        cond : boolean DataFrame
            Where cond is True, keep the original value. Where False,
            replace with corresponding value from other.
        other : scalar, DataFrame
            Entries where cond is False are replaced with corresponding value from other.
        axis : int, default None
            Can only be set to 0 now for compatibility with pandas.

        Returns
        -------
        DataFrame

        Examples
        --------

        >>> from pyspark.pandas.config import set_option, reset_option
        >>> set_option("compute.ops_on_diff_frames", True)
        >>> df1 = ps.DataFrame({\'A\': [0, 1, 2, 3, 4], \'B\':[100, 200, 300, 400, 500]})
        >>> df2 = ps.DataFrame({\'A\': [0, -1, -2, -3, -4], \'B\':[-100, -200, -300, -400, -500]})
        >>> df1
           A    B
        0  0  100
        1  1  200
        2  2  300
        3  3  400
        4  4  500
        >>> df2
           A    B
        0  0 -100
        1 -1 -200
        2 -2 -300
        3 -3 -400
        4 -4 -500

        >>> df1.where(df1 > 0).sort_index()
             A      B
        0  NaN  100.0
        1  1.0  200.0
        2  2.0  300.0
        3  3.0  400.0
        4  4.0  500.0

        >>> df1.where(df1 > 1, 10).sort_index()
            A    B
        0  10  100
        1  10  200
        2   2  300
        3   3  400
        4   4  500

        >>> df1.where(df1 > 1, df1 + 100).sort_index()
             A    B
        0  100  100
        1  101  200
        2    2  300
        3    3  400
        4    4  500

        >>> df1.where(df1 > 1, df2).sort_index()
           A    B
        0  0  100
        1 -1  200
        2  2  300
        3  3  400
        4  4  500

        When the column name of cond is different from self, it treats all values are False

        >>> cond = ps.DataFrame({\'C\': [0, -1, -2, -3, -4], \'D\':[4, 3, 2, 1, 0]}) % 3 == 0
        >>> cond
               C      D
        0   True  False
        1  False   True
        2  False  False
        3   True  False
        4  False   True

        >>> df1.where(cond).sort_index()
            A   B
        0 NaN NaN
        1 NaN NaN
        2 NaN NaN
        3 NaN NaN
        4 NaN NaN

        When the type of cond is Series, it just check boolean regardless of column name

        >>> cond = ps.Series([1, 2]) > 1
        >>> cond
        0    False
        1     True
        dtype: bool

        >>> df1.where(cond).sort_index()
             A      B
        0  NaN    NaN
        1  1.0  200.0
        2  NaN    NaN
        3  NaN    NaN
        4  NaN    NaN

        >>> reset_option("compute.ops_on_diff_frames")
        '''
    def mask(self, cond: DataFrameOrSeries, other: DataFrameOrSeries | Any = ...) -> DataFrame:
        '''
        Replace values where the condition is True.

        Parameters
        ----------
        cond : boolean DataFrame
            Where cond is False, keep the original value. Where True,
            replace with corresponding value from other.
        other : scalar, DataFrame
            Entries where cond is True are replaced with corresponding value from other.

        Returns
        -------
        DataFrame

        Examples
        --------

        >>> from pyspark.pandas.config import set_option, reset_option
        >>> set_option("compute.ops_on_diff_frames", True)
        >>> df1 = ps.DataFrame({\'A\': [0, 1, 2, 3, 4], \'B\':[100, 200, 300, 400, 500]})
        >>> df2 = ps.DataFrame({\'A\': [0, -1, -2, -3, -4], \'B\':[-100, -200, -300, -400, -500]})
        >>> df1
           A    B
        0  0  100
        1  1  200
        2  2  300
        3  3  400
        4  4  500
        >>> df2
           A    B
        0  0 -100
        1 -1 -200
        2 -2 -300
        3 -3 -400
        4 -4 -500

        >>> df1.mask(df1 > 0).sort_index()
             A   B
        0  0.0 NaN
        1  NaN NaN
        2  NaN NaN
        3  NaN NaN
        4  NaN NaN

        >>> df1.mask(df1 > 1, 10).sort_index()
            A   B
        0   0  10
        1   1  10
        2  10  10
        3  10  10
        4  10  10

        >>> df1.mask(df1 > 1, df1 + 100).sort_index()
             A    B
        0    0  200
        1    1  300
        2  102  400
        3  103  500
        4  104  600

        >>> df1.mask(df1 > 1, df2).sort_index()
           A    B
        0  0 -100
        1  1 -200
        2 -2 -300
        3 -3 -400
        4 -4 -500

        >>> reset_option("compute.ops_on_diff_frames")
        '''
    @property
    def index(self) -> Index:
        """The index (row labels) Column of the DataFrame.

        Currently not supported when the DataFrame has no index.

        See Also
        --------
        Index
        """
    @property
    def empty(self) -> bool:
        """
        Returns true if the current DataFrame is empty. Otherwise, returns false.

        Examples
        --------
        >>> ps.range(10).empty
        False

        >>> ps.range(0).empty
        True

        >>> ps.DataFrame({}, index=list('abc')).empty
        True
        """
    @property
    def style(self) -> Styler:
        """
        Property returning a Styler object containing methods for
        building a styled HTML representation for the DataFrame.

        Examples
        --------
        >>> ps.range(1001).style  # doctest: +SKIP
        <pandas.io.formats.style.Styler object at ...>
        """
    def set_index(self, keys: Name | List[Name], drop: bool = True, append: bool = False, inplace: bool = False) -> DataFrame | None:
        '''Set the DataFrame index (row labels) using one or more existing columns.

        Set the DataFrame index (row labels) using one or more existing
        columns or arrays (of the correct length). The index can replace the
        existing index or expand on it.

        Parameters
        ----------
        keys : label or array-like or list of labels/arrays
            This parameter can be either a single column key, a single array of
            the same length as the calling DataFrame, or a list containing an
            arbitrary combination of column keys and arrays. Here, "array"
            encompasses :class:`Series`, :class:`Index` and ``np.ndarray``.
        drop : bool, default True
            Delete columns to be used as the new index.
        append : bool, default False
            Whether to append columns to existing index.
        inplace : bool, default False
            Modify the DataFrame in place (do not create a new object).

        Returns
        -------
        DataFrame
            Changed row labels.

        See Also
        --------
        DataFrame.reset_index : Opposite of set_index.

        Examples
        --------
        >>> df = ps.DataFrame({\'month\': [1, 4, 7, 10],
        ...                    \'year\': [2012, 2014, 2013, 2014],
        ...                    \'sale\': [55, 40, 84, 31]},
        ...                   columns=[\'month\', \'year\', \'sale\'])
        >>> df
           month  year  sale
        0      1  2012    55
        1      4  2014    40
        2      7  2013    84
        3     10  2014    31

        Set the index to become the \'month\' column:

        >>> df.set_index(\'month\')  # doctest: +NORMALIZE_WHITESPACE
               year  sale
        month
        1      2012    55
        4      2014    40
        7      2013    84
        10     2014    31

        Create a MultiIndex using columns \'year\' and \'month\':

        >>> df.set_index([\'year\', \'month\'])  # doctest: +NORMALIZE_WHITESPACE
                    sale
        year  month
        2012  1     55
        2014  4     40
        2013  7     84
        2014  10    31
        '''
    def reset_index(self, level: int | Name | Sequence[int | Name] | None = None, drop: bool = False, inplace: bool = False, col_level: int = 0, col_fill: str = '') -> DataFrame | None:
        """Reset the index, or a level of it.

        For DataFrame with multi-level index, return new DataFrame with labeling information in
        the columns under the index names, defaulting to 'level_0', 'level_1', etc. if any are None.
        For a standard index, the index name will be used (if set), otherwise a default 'index' or
        'level_0' (if 'index' is already taken) will be used.

        Parameters
        ----------
        level : int, str, tuple, or list, default None
            Only remove the given levels from the index. Removes all levels by
            default.
        drop : bool, default False
            Do not try to insert index into dataframe columns. This reset
            the index to the default integer index.
        inplace : bool, default False
            Modify the DataFrame in place (do not create a new object).
        col_level : int or str, default 0
            If the columns have multiple levels, determines which level the
            labels are inserted into. By default it is inserted into the first
            level.
        col_fill : object, default ''
            If the columns have multiple levels, determines how the other
            levels are named. If None then the index name is repeated.

        Returns
        -------
        DataFrame
            DataFrame with the new index.

        See Also
        --------
        DataFrame.set_index : Opposite of reset_index.

        Examples
        --------
        >>> df = ps.DataFrame([('bird', 389.0),
        ...                    ('bird', 24.0),
        ...                    ('mammal', 80.5),
        ...                    ('mammal', np.nan)],
        ...                   index=['falcon', 'parrot', 'lion', 'monkey'],
        ...                   columns=('class', 'max_speed'))
        >>> df
                 class  max_speed
        falcon    bird      389.0
        parrot    bird       24.0
        lion    mammal       80.5
        monkey  mammal        NaN

        When we reset the index, the old index is added as a column. Unlike pandas, pandas-on-Spark
        does not automatically add a sequential index. The following 0, 1, 2, 3 are only
        there when we display the DataFrame.

        >>> df.reset_index()
            index   class  max_speed
        0  falcon    bird      389.0
        1  parrot    bird       24.0
        2    lion  mammal       80.5
        3  monkey  mammal        NaN

        We can use the `drop` parameter to avoid the old index being added as
        a column:

        >>> df.reset_index(drop=True)
            class  max_speed
        0    bird      389.0
        1    bird       24.0
        2  mammal       80.5
        3  mammal        NaN

        You can also use `reset_index` with `MultiIndex`.

        >>> index = pd.MultiIndex.from_tuples([('bird', 'falcon'),
        ...                                    ('bird', 'parrot'),
        ...                                    ('mammal', 'lion'),
        ...                                    ('mammal', 'monkey')],
        ...                                   names=['class', 'name'])
        >>> columns = pd.MultiIndex.from_tuples([('speed', 'max'),
        ...                                      ('species', 'type')])
        >>> df = ps.DataFrame([(389.0, 'fly'),
        ...                    ( 24.0, 'fly'),
        ...                    ( 80.5, 'run'),
        ...                    (np.nan, 'jump')],
        ...                   index=index,
        ...                   columns=columns)
        >>> df  # doctest: +NORMALIZE_WHITESPACE
                       speed species
                         max    type
        class  name
        bird   falcon  389.0     fly
               parrot   24.0     fly
        mammal lion     80.5     run
               monkey    NaN    jump

        If the index has multiple levels, we can reset a subset of them:

        >>> df.reset_index(level='class')  # doctest: +NORMALIZE_WHITESPACE
                 class  speed species
                          max    type
        name
        falcon    bird  389.0     fly
        parrot    bird   24.0     fly
        lion    mammal   80.5     run
        monkey  mammal    NaN    jump

        If we are not dropping the index, by default, it is placed in the top
        level. We can place it in another level:

        >>> df.reset_index(level='class', col_level=1)  # doctest: +NORMALIZE_WHITESPACE
                        speed species
                 class    max    type
        name
        falcon    bird  389.0     fly
        parrot    bird   24.0     fly
        lion    mammal   80.5     run
        monkey  mammal    NaN    jump

        When the index is inserted under another level, we can specify under
        which one with the parameter `col_fill`:

        >>> df.reset_index(level='class', col_level=1,
        ...                col_fill='species')  # doctest: +NORMALIZE_WHITESPACE
                      species  speed species
                        class    max    type
        name
        falcon           bird  389.0     fly
        parrot           bird   24.0     fly
        lion           mammal   80.5     run
        monkey         mammal    NaN    jump

        If we specify a nonexistent level for `col_fill`, it is created:

        >>> df.reset_index(level='class', col_level=1,
        ...                col_fill='genus')  # doctest: +NORMALIZE_WHITESPACE
                        genus  speed species
                        class    max    type
        name
        falcon           bird  389.0     fly
        parrot           bird   24.0     fly
        lion           mammal   80.5     run
        monkey         mammal    NaN    jump
        """
    def isnull(self) -> DataFrame:
        """
        Detects missing values for items in the current Dataframe.

        Return a boolean same-sized Dataframe indicating if the values are NA.
        NA values, such as None or numpy.NaN, gets mapped to True values.
        Everything else gets mapped to False values.

        See Also
        --------
        DataFrame.notnull

        Examples
        --------
        >>> df = ps.DataFrame([(.2, .3), (.0, None), (.6, None), (.2, .1)])
        >>> df.isnull()
               0      1
        0  False  False
        1  False   True
        2  False   True
        3  False  False

        >>> df = ps.DataFrame([[None, 'bee', None], ['dog', None, 'fly']])
        >>> df.isnull()
               0      1      2
        0   True  False   True
        1  False   True  False
        """
    isna = isnull
    def notnull(self) -> DataFrame:
        """
        Detects non-missing values for items in the current Dataframe.

        This function takes a dataframe and indicates whether it's
        values are valid (not missing, which is ``NaN`` in numeric
        datatypes, ``None`` or ``NaN`` in objects and ``NaT`` in datetimelike).

        See Also
        --------
        DataFrame.isnull

        Examples
        --------
        >>> df = ps.DataFrame([(.2, .3), (.0, None), (.6, None), (.2, .1)])
        >>> df.notnull()
              0      1
        0  True   True
        1  True  False
        2  True  False
        3  True   True

        >>> df = ps.DataFrame([['ant', 'bee', 'cat'], ['dog', None, 'fly']])
        >>> df.notnull()
              0      1     2
        0  True   True  True
        1  True  False  True
        """
    notna = notnull
    def insert(self, loc: int, column: Name, value: Scalar | Series | Iterable, allow_duplicates: bool = False) -> None:
        '''
        Insert column into DataFrame at specified location.

        Raises a ValueError if `column` is already contained in the DataFrame,
        unless `allow_duplicates` is set to True.

        Parameters
        ----------
        loc : int
            Insertion index. Must verify 0 <= loc <= len(columns).
        column : str, number, or hashable object
            Label of the inserted column.
        value : int, Series, or array-like
        allow_duplicates : bool, optional

        Examples
        --------
        >>> psdf = ps.DataFrame([1, 2, 3])
        >>> psdf.sort_index()
           0
        0  1
        1  2
        2  3
        >>> psdf.insert(0, \'x\', 4)
        >>> psdf.sort_index()
           x  0
        0  4  1
        1  4  2
        2  4  3

        >>> from pyspark.pandas.config import set_option, reset_option
        >>> set_option("compute.ops_on_diff_frames", True)

        >>> psdf.insert(1, \'y\', [5, 6, 7])
        >>> psdf.sort_index()
           x  y  0
        0  4  5  1
        1  4  6  2
        2  4  7  3

        >>> psdf.insert(2, \'z\', ps.Series([8, 9, 10]))
        >>> psdf.sort_index()
           x  y   z  0
        0  4  5   8  1
        1  4  6   9  2
        2  4  7  10  3

        >>> reset_option("compute.ops_on_diff_frames")
        '''
    def shift(self, periods: int = 1, fill_value: Any | None = None) -> DataFrame:
        """
        Shift DataFrame by desired number of periods.

        .. note:: the current implementation of shift uses Spark's Window without
            specifying partition specification. This leads to moving all data into
            a single partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

        Parameters
        ----------
        periods : int
            Number of periods to shift. Can be positive or negative.
        fill_value : object, optional
            The scalar value to use for newly introduced missing values.
            The default depends on the dtype of self. For numeric data, np.nan is used.

        Returns
        -------
        Copy of input DataFrame, shifted.

        Examples
        --------
        >>> df = ps.DataFrame({'Col1': [10, 20, 15, 30, 45],
        ...                    'Col2': [13, 23, 18, 33, 48],
        ...                    'Col3': [17, 27, 22, 37, 52]},
        ...                   columns=['Col1', 'Col2', 'Col3'])

        >>> df.shift(periods=3)
           Col1  Col2  Col3
        0   NaN   NaN   NaN
        1   NaN   NaN   NaN
        2   NaN   NaN   NaN
        3  10.0  13.0  17.0
        4  20.0  23.0  27.0

        >>> df.shift(periods=3, fill_value=0)
           Col1  Col2  Col3
        0     0     0     0
        1     0     0     0
        2     0     0     0
        3    10    13    17
        4    20    23    27

        """
    def diff(self, periods: int = 1, axis: Axis = 0) -> DataFrame:
        """
        First discrete difference of element.

        Calculates the difference of a DataFrame element compared with another element in the
        DataFrame (default is the element in the same column of the previous row).

        .. note:: the current implementation of diff uses Spark's Window without
            specifying partition specification. This leads to moving all data into
            a single partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

        Parameters
        ----------
        periods : int, default 1
            Periods to shift for calculating difference, accepts negative values.
        axis : int, default 0 or 'index'
            Can only be set to 0 now.

        Returns
        -------
        diffed : DataFrame

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

        >>> df.diff()
             a    b     c
        0  NaN  NaN   NaN
        1  1.0  0.0   3.0
        2  1.0  1.0   5.0
        3  1.0  1.0   7.0
        4  1.0  2.0   9.0
        5  1.0  3.0  11.0

        Difference with previous column

        >>> df.diff(periods=3)
             a    b     c
        0  NaN  NaN   NaN
        1  NaN  NaN   NaN
        2  NaN  NaN   NaN
        3  3.0  2.0  15.0
        4  3.0  4.0  21.0
        5  3.0  6.0  27.0

        Difference with following row

        >>> df.diff(periods=-1)
             a    b     c
        0 -1.0  0.0  -3.0
        1 -1.0 -1.0  -5.0
        2 -1.0 -1.0  -7.0
        3 -1.0 -2.0  -9.0
        4 -1.0 -3.0 -11.0
        5  NaN  NaN   NaN
        """
    def nunique(self, axis: Axis = 0, dropna: bool = True, approx: bool = False, rsd: float = 0.05) -> Series:
        """
        Return number of unique elements in the object.

        Excludes NA values by default.

        Parameters
        ----------
        axis : int, default 0 or 'index'
            Can only be set to 0 now.
        dropna : bool, default True
            Don’t include NaN in the count.
        approx: bool, default False
            If False, will use the exact algorithm and return the exact number of unique.
            If True, it uses the HyperLogLog approximate algorithm, which is significantly faster
            for large amounts of data.
            Note: This parameter is specific to pandas-on-Spark and is not found in pandas.
        rsd: float, default 0.05
            Maximum estimation error allowed in the HyperLogLog algorithm.
            Note: Just like ``approx`` this parameter is specific to pandas-on-Spark.

        Returns
        -------
        The number of unique values per column as a pandas-on-Spark Series.

        Examples
        --------
        >>> df = ps.DataFrame({'A': [1, 2, 3], 'B': [np.nan, 3, np.nan]})
        >>> df.nunique()
        A    3
        B    1
        dtype: int64

        >>> df.nunique(dropna=False)
        A    3
        B    2
        dtype: int64

        On big data, we recommend using the approximate algorithm to speed up this function.
        The result will be very close to the exact unique count.

        >>> df.nunique(approx=True)
        A    3
        B    1
        dtype: int64
        """
    def round(self, decimals: int | Dict[Name, int] | Series = 0) -> DataFrame:
        """
        Round a DataFrame to a variable number of decimal places.

        Parameters
        ----------
        decimals : int, dict, Series
            Number of decimal places to round each column to. If an int is
            given, round each column to the same number of places.
            Otherwise dict and Series round to variable numbers of places.
            Column names should be in the keys if `decimals` is a
            dict-like, or in the index if `decimals` is a Series. Any
            columns not included in `decimals` will be left as is. Elements
            of `decimals` which are not columns of the input will be
            ignored.

            .. note:: If `decimals` is a Series, it is expected to be small,
                as all the data is loaded into the driver's memory.

        Returns
        -------
        DataFrame

        See Also
        --------
        Series.round

        Examples
        --------
        >>> df = ps.DataFrame({'A':[0.028208, 0.038683, 0.877076],
        ...                    'B':[0.992815, 0.645646, 0.149370],
        ...                    'C':[0.173891, 0.577595, 0.491027]},
        ...                    columns=['A', 'B', 'C'],
        ...                    index=['first', 'second', 'third'])
        >>> df
                       A         B         C
        first   0.028208  0.992815  0.173891
        second  0.038683  0.645646  0.577595
        third   0.877076  0.149370  0.491027

        >>> df.round(2)
                   A     B     C
        first   0.03  0.99  0.17
        second  0.04  0.65  0.58
        third   0.88  0.15  0.49

        >>> df.round({'A': 1, 'C': 2})
                  A         B     C
        first   0.0  0.992815  0.17
        second  0.0  0.645646  0.58
        third   0.9  0.149370  0.49

        >>> decimals = ps.Series([1, 0, 2], index=['A', 'B', 'C'])
        >>> df.round(decimals)
                  A    B     C
        first   0.0  1.0  0.17
        second  0.0  1.0  0.58
        third   0.9  0.0  0.49
        """
    def duplicated(self, subset: Name | List[Name] | None = None, keep: bool | str = 'first') -> Series:
        """
        Return boolean Series denoting duplicate rows, optionally only considering certain columns.

        Parameters
        ----------
        subset : column label or sequence of labels, optional
            Only consider certain columns for identifying duplicates,
            default use all of the columns
        keep : {'first', 'last', False}, default 'first'
           - ``first`` : Mark duplicates as ``True`` except for the first occurrence.
           - ``last`` : Mark duplicates as ``True`` except for the last occurrence.
           - False : Mark all duplicates as ``True``.

        Returns
        -------
        duplicated : Series

        Examples
        --------
        >>> df = ps.DataFrame({'a': [1, 1, 1, 3], 'b': [1, 1, 1, 4], 'c': [1, 1, 1, 5]},
        ...                   columns = ['a', 'b', 'c'])
        >>> df
           a  b  c
        0  1  1  1
        1  1  1  1
        2  1  1  1
        3  3  4  5

        >>> df.duplicated().sort_index()
        0    False
        1     True
        2     True
        3    False
        dtype: bool

        Mark duplicates as ``True`` except for the last occurrence.

        >>> df.duplicated(keep='last').sort_index()
        0     True
        1     True
        2    False
        3    False
        dtype: bool

        Mark all duplicates as ``True``.

        >>> df.duplicated(keep=False).sort_index()
        0     True
        1     True
        2     True
        3    False
        dtype: bool
        """
    def dot(self, other: Series) -> Series:
        '''
        Compute the matrix multiplication between the DataFrame and others.

        This method computes the matrix product between the DataFrame and the
        values of an other Series

        It can also be called using ``self @ other`` in Python >= 3.5.

        .. note:: This method is based on an expensive operation due to the nature
            of big data. Internally it needs to generate each row for each value, and
            then group twice - it is a huge operation. To prevent misuse, this method
            has the \'compute.max_rows\' default limit of input length and raises a ValueError.

                >>> from pyspark.pandas.config import option_context
                >>> with option_context(
                ...     \'compute.max_rows\', 1000, "compute.ops_on_diff_frames", True
                ... ):  # doctest: +NORMALIZE_WHITESPACE
                ...     psdf = ps.DataFrame({\'a\': range(1001)})
                ...     psser = ps.Series([2], index=[\'a\'])
                ...     psdf.dot(psser)
                Traceback (most recent call last):
                  ...
                ValueError: Current DataFrame\'s length exceeds the given limit of 1000 rows.
                Please set \'compute.max_rows\' by using \'pyspark.pandas.config.set_option\'
                to retrieve more than 1000 rows. Note that, before changing the
                \'compute.max_rows\', this operation is considerably expensive.

        Parameters
        ----------
        other : Series
            The other object to compute the matrix product with.

        Returns
        -------
        Series
            Return the matrix product between self and other as a Series.

        See Also
        --------
        Series.dot: Similar method for Series.

        Notes
        -----
        The dimensions of DataFrame and other must be compatible to
        compute the matrix multiplication. In addition, the column names of
        DataFrame and the index of other must contain the same values, as they
        will be aligned prior to the multiplication.

        The dot method for Series computes the inner product, instead of the
        matrix product here.

        Examples
        --------
        >>> from pyspark.pandas.config import set_option, reset_option
        >>> set_option("compute.ops_on_diff_frames", True)
        >>> psdf = ps.DataFrame([[0, 1, -2, -1], [1, 1, 1, 1]])
        >>> psser = ps.Series([1, 1, 2, 1])
        >>> psdf.dot(psser)
        0   -4
        1    5
        dtype: int64

        Note how shuffling of the objects does not change the result.

        >>> psser2 = psser.reindex([1, 0, 2, 3])
        >>> psdf.dot(psser2)
        0   -4
        1    5
        dtype: int64
        >>> psdf @ psser2
        0   -4
        1    5
        dtype: int64
        >>> reset_option("compute.ops_on_diff_frames")
        '''
    def __matmul__(self, other: Series) -> Series:
        """
        Matrix multiplication using binary `@` operator in Python>=3.5.
        """
    def to_table(self, name: str, format: str | None = None, mode: str = 'w', partition_cols: str | List[str] | None = None, index_col: str | List[str] | None = None, **options: Any) -> None: ...
    def to_delta(self, path: str, mode: str = 'w', partition_cols: str | List[str] | None = None, index_col: str | List[str] | None = None, **options: OptionalPrimitiveType) -> None:
        '''
        Write the DataFrame out as a Delta Lake table.

        Parameters
        ----------
        path : str, required
            Path to write to.
        mode : str
            Python write mode, default \'w\'.

            .. note:: mode can accept the strings for Spark writing mode.
                Such as \'append\', \'overwrite\', \'ignore\', \'error\', \'errorifexists\'.

                - \'append\' (equivalent to \'a\'): Append the new data to existing data.
                - \'overwrite\' (equivalent to \'w\'): Overwrite existing data.
                - \'ignore\': Silently ignore this operation if data already exists.
                - \'error\' or \'errorifexists\': Throw an exception if data already exists.

        partition_cols : str or list of str, optional, default None
            Names of partitioning columns
        index_col: str or list of str, optional, default: None
            Column names to be used in Spark to represent pandas-on-Spark\'s index. The index name
            in pandas-on-Spark is ignored. By default the index is always lost.
        options : dict
            All other options passed directly into Delta Lake.

        See Also
        --------
        read_delta
        DataFrame.to_parquet
        DataFrame.to_table
        DataFrame.to_spark_io

        Examples
        --------

        >>> df = ps.DataFrame(dict(
        ...    date=list(pd.date_range(\'2012-1-1 12:00:00\', periods=3, freq=\'M\')),
        ...    country=[\'KR\', \'US\', \'JP\'],
        ...    code=[1, 2 ,3]), columns=[\'date\', \'country\', \'code\'])
        >>> df
                         date country  code
        0 2012-01-31 12:00:00      KR     1
        1 2012-02-29 12:00:00      US     2
        2 2012-03-31 12:00:00      JP     3

        Create a new Delta Lake table, partitioned by one column:

        >>> df.to_delta(\'%s/to_delta/foo\' % path, partition_cols=\'date\')  # doctest: +SKIP

        Partitioned by two columns:

        >>> df.to_delta(\'%s/to_delta/bar\' % path,
        ...             partition_cols=[\'date\', \'country\'])  # doctest: +SKIP

        Overwrite an existing table\'s partitions, using the \'replaceWhere\' capability in Delta:

        >>> df.to_delta(\'%s/to_delta/bar\' % path,
        ...             mode=\'overwrite\', replaceWhere=\'date >= "2012-01-01"\')  # doctest: +SKIP
        '''
    def to_parquet(self, path: str, mode: str = 'w', partition_cols: str | List[str] | None = None, compression: str | None = None, index_col: str | List[str] | None = None, **options: Any) -> None:
        """
        Write the DataFrame out as a Parquet file or directory.

        Parameters
        ----------
        path : str, required
            Path to write to.
        mode : str
            Python write mode, default 'w'.

            .. note:: mode can accept the strings for Spark writing mode.
                Such as 'append', 'overwrite', 'ignore', 'error', 'errorifexists'.

                - 'append' (equivalent to 'a'): Append the new data to existing data.
                - 'overwrite' (equivalent to 'w'): Overwrite existing data.
                - 'ignore': Silently ignore this operation if data already exists.
                - 'error' or 'errorifexists': Throw an exception if data already exists.

        partition_cols : str or list of str, optional, default None
            Names of partitioning columns
        compression : str {'none', 'uncompressed', 'snappy', 'gzip', 'lzo', 'brotli', 'lz4', 'zstd'}
            Compression codec to use when saving to file. If None is set, it uses the
            value specified in `spark.sql.parquet.compression.codec`.
        index_col: str or list of str, optional, default: None
            Column names to be used in Spark to represent pandas-on-Spark's index. The index name
            in pandas-on-Spark is ignored. By default the index is always lost.
        options : dict
            All other options passed directly into Spark's data source.

        See Also
        --------
        read_parquet
        DataFrame.to_delta
        DataFrame.to_table
        DataFrame.to_spark_io

        Examples
        --------
        >>> df = ps.DataFrame(dict(
        ...    date=list(pd.date_range('2012-1-1 12:00:00', periods=3, freq='M')),
        ...    country=['KR', 'US', 'JP'],
        ...    code=[1, 2 ,3]), columns=['date', 'country', 'code'])
        >>> df
                         date country  code
        0 2012-01-31 12:00:00      KR     1
        1 2012-02-29 12:00:00      US     2
        2 2012-03-31 12:00:00      JP     3

        >>> df.to_parquet('%s/to_parquet/foo.parquet' % path, partition_cols='date')

        >>> df.to_parquet(
        ...     '%s/to_parquet/foo.parquet' % path,
        ...     mode = 'overwrite',
        ...     partition_cols=['date', 'country'])

        Notes
        -----
        pandas API on Spark writes Parquet files into the directory, `path`, and writes
        multiple part files in the directory unlike pandas.
        pandas API on Spark respects HDFS's property such as 'fs.default.name'.
        """
    def to_orc(self, path: str, mode: str = 'w', partition_cols: str | List[str] | None = None, index_col: str | List[str] | None = None, **options: OptionalPrimitiveType) -> None:
        """
        Write a DataFrame to the ORC format.

        Parameters
        ----------
        path : str
            Path to write to.
        mode : str
            Python write mode, default 'w'.

            .. note:: mode can accept the strings for Spark writing mode.
                Such as 'append', 'overwrite', 'ignore', 'error', 'errorifexists'.

                - 'append' (equivalent to 'a'): Append the new data to existing data.
                - 'overwrite' (equivalent to 'w'): Overwrite existing data.
                - 'ignore': Silently ignore this operation if data already exists.
                - 'error' or 'errorifexists': Throw an exception if data already exists.

        partition_cols : str or list of str, optional, default None
            Names of partitioning columns
        index_col: str or list of str, optional, default: None
            Column names to be used in Spark to represent pandas-on-Spark's index. The index name
            in pandas-on-Spark is ignored. By default the index is always lost.
        options : dict
            All other options passed directly into Spark's data source.

        See Also
        --------
        read_orc
        DataFrame.to_delta
        DataFrame.to_parquet
        DataFrame.to_table
        DataFrame.to_spark_io

        Examples
        --------
        >>> df = ps.DataFrame(dict(
        ...    date=list(pd.date_range('2012-1-1 12:00:00', periods=3, freq='M')),
        ...    country=['KR', 'US', 'JP'],
        ...    code=[1, 2 ,3]), columns=['date', 'country', 'code'])
        >>> df
                         date country  code
        0 2012-01-31 12:00:00      KR     1
        1 2012-02-29 12:00:00      US     2
        2 2012-03-31 12:00:00      JP     3

        >>> df.to_orc('%s/to_orc/foo.orc' % path, partition_cols='date')

        >>> df.to_orc(
        ...     '%s/to_orc/foo.orc' % path,
        ...     mode = 'overwrite',
        ...     partition_cols=['date', 'country'])

        Notes
        -----
        pandas API on Spark writes ORC files into the directory, `path`, and writes
        multiple part files in the directory unlike pandas.
        pandas API on Spark respects HDFS's property such as 'fs.default.name'.
        """
    def to_spark_io(self, path: str | None = None, format: str | None = None, mode: str = 'overwrite', partition_cols: str | List[str] | None = None, index_col: str | List[str] | None = None, **options: OptionalPrimitiveType) -> None:
        """An alias for :func:`DataFrame.spark.to_spark_io`.
        See :meth:`pyspark.pandas.spark.accessors.SparkFrameMethods.to_spark_io`.

        .. deprecated:: 3.2.0
            Use :func:`DataFrame.spark.to_spark_io` instead.
        """
    def to_spark(self, index_col: str | List[str] | None = None) -> SparkDataFrame: ...
    def to_pandas(self) -> pd.DataFrame:
        """
        Return a pandas DataFrame.

        .. note:: This method should only be used if the resulting pandas DataFrame is expected
            to be small, as all the data is loaded into the driver's memory.

        Examples
        --------
        >>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
        ...                   columns=['dogs', 'cats'])
        >>> df.to_pandas()
           dogs  cats
        0   0.2   0.3
        1   0.0   0.6
        2   0.6   0.0
        3   0.2   0.1
        """
    def assign(self, **kwargs: Any) -> DataFrame:
        """
        Assign new columns to a DataFrame.

        Returns a new object with all original columns in addition to new ones.
        Existing columns that are re-assigned will be overwritten.

        Parameters
        ----------
        **kwargs : dict of {str: callable, Series or Index}
            The column names are keywords. If the values are
            callable, they are computed on the DataFrame and
            assigned to the new columns. The callable must not
            change input DataFrame (though pandas-on-Spark doesn't check it).
            If the values are not callable, (e.g. a Series or a literal),
            they are simply assigned.

        Returns
        -------
        DataFrame
            A new DataFrame with the new columns in addition to
            all the existing columns.

        Examples
        --------
        >>> df = ps.DataFrame({'temp_c': [17.0, 25.0]},
        ...                   index=['Portland', 'Berkeley'])
        >>> df
                  temp_c
        Portland    17.0
        Berkeley    25.0

        Where the value is a callable, evaluated on `df`:

        >>> df.assign(temp_f=lambda x: x.temp_c * 9 / 5 + 32)
                  temp_c  temp_f
        Portland    17.0    62.6
        Berkeley    25.0    77.0

        Alternatively, the same behavior can be achieved by directly
        referencing an existing Series or sequence and you can also
        create multiple columns within the same assign.

        >>> assigned = df.assign(temp_f=df['temp_c'] * 9 / 5 + 32,
        ...                      temp_k=df['temp_c'] + 273.15,
        ...                      temp_idx=df.index)
        >>> assigned[['temp_c', 'temp_f', 'temp_k', 'temp_idx']]
                  temp_c  temp_f  temp_k  temp_idx
        Portland    17.0    62.6  290.15  Portland
        Berkeley    25.0    77.0  298.15  Berkeley

        Notes
        -----
        Assigning multiple columns within the same ``assign`` is possible
        but you cannot refer to newly created or modified columns. This
        feature is supported in pandas for Python 3.6 and later but not in
        pandas-on-Spark. In pandas-on-Spark, all items are computed first,
        and then assigned.
        """
    @staticmethod
    def from_records(data: np.ndarray | List[tuple] | dict | pd.DataFrame, index: str | list | np.ndarray = None, exclude: list = None, columns: list = None, coerce_float: bool = False, nrows: int = None) -> DataFrame:
        """
        Convert structured or recorded ndarray to DataFrame.

        Parameters
        ----------
        data : ndarray (structured dtype), list of tuples, dict, or DataFrame
        index : string, list of fields, array-like
            Field of array to use as the index, alternately a specific set of input labels to use
        exclude : sequence, default None
            Columns or fields to exclude
        columns : sequence, default None
            Column names to use. If the passed data do not have names associated with them, this
            argument provides names for the columns. Otherwise this argument indicates the order of
            the columns in the result (any names not found in the data will become all-NA columns)
        coerce_float : boolean, default False
            Attempt to convert values of non-string, non-numeric objects (like decimal.Decimal) to
            floating point, useful for SQL result sets
        nrows : int, default None
            Number of rows to read if data is an iterator

        Returns
        -------
        df : DataFrame

        Examples
        --------
        Use dict as input

        >>> ps.DataFrame.from_records({'A': [1, 2, 3]})
           A
        0  1
        1  2
        2  3

        Use list of tuples as input

        >>> ps.DataFrame.from_records([(1, 2), (3, 4)])
           0  1
        0  1  2
        1  3  4

        Use NumPy array as input

        >>> ps.DataFrame.from_records(np.eye(3))
             0    1    2
        0  1.0  0.0  0.0
        1  0.0  1.0  0.0
        2  0.0  0.0  1.0
        """
    def to_records(self, index: bool = True, column_dtypes: str | Dtype | Dict[Name, str | Dtype] | None = None, index_dtypes: str | Dtype | Dict[Name, str | Dtype] | None = None) -> np.recarray:
        '''
        Convert DataFrame to a NumPy record array.

        Index will be included as the first field of the record array if
        requested.

        .. note:: This method should only be used if the resulting NumPy ndarray is
            expected to be small, as all the data is loaded into the driver\'s memory.

        Parameters
        ----------
        index : bool, default True
            Include index in resulting record array, stored in \'index\'
            field or using the index label, if set.
        column_dtypes : str, type, dict, default None
            If a string or type, the data type to store all columns. If
            a dictionary, a mapping of column names and indices (zero-indexed)
            to specific data types.
        index_dtypes : str, type, dict, default None
            If a string or type, the data type to store all index levels. If
            a dictionary, a mapping of index level names and indices
            (zero-indexed) to specific data types.
            This mapping is applied only if `index=True`.

        Returns
        -------
        numpy.recarray
            NumPy ndarray with the DataFrame labels as fields and each row
            of the DataFrame as entries.

        See Also
        --------
        DataFrame.from_records: Convert structured or record ndarray
            to DataFrame.
        numpy.recarray: An ndarray that allows field access using
            attributes, analogous to typed columns in a
            spreadsheet.

        Examples
        --------
        >>> df = ps.DataFrame({\'A\': [1, 2], \'B\': [0.5, 0.75]},
        ...                   index=[\'a\', \'b\'])
        >>> df
           A     B
        a  1  0.50
        b  2  0.75

        >>> df.to_records() # doctest: +SKIP
        rec.array([(\'a\', 1, 0.5 ), (\'b\', 2, 0.75)],
                  dtype=[(\'index\', \'O\'), (\'A\', \'<i8\'), (\'B\', \'<f8\')])

        The index can be excluded from the record array:

        >>> df.to_records(index=False) # doctest: +SKIP
        rec.array([(1, 0.5 ), (2, 0.75)],
                  dtype=[(\'A\', \'<i8\'), (\'B\', \'<f8\')])

        Specification of dtype for columns is new in pandas 0.24.0.
        Data types can be specified for the columns:

        >>> df.to_records(column_dtypes={"A": "int32"}) # doctest: +SKIP
        rec.array([(\'a\', 1, 0.5 ), (\'b\', 2, 0.75)],
                  dtype=[(\'index\', \'O\'), (\'A\', \'<i4\'), (\'B\', \'<f8\')])

        Specification of dtype for index is new in pandas 0.24.0.
        Data types can also be specified for the index:

        >>> df.to_records(index_dtypes="<S2") # doctest: +SKIP
        rec.array([(b\'a\', 1, 0.5 ), (b\'b\', 2, 0.75)],
                  dtype=[(\'index\', \'S2\'), (\'A\', \'<i8\'), (\'B\', \'<f8\')])
        '''
    def copy(self, deep: bool = True) -> DataFrame:
        """
        Make a copy of this object's indices and data.

        Parameters
        ----------
        deep : bool, default True
            this parameter is not supported but just dummy parameter to match pandas.

        Returns
        -------
        copy : DataFrame

        Examples
        --------
        >>> df = ps.DataFrame({'x': [1, 2], 'y': [3, 4], 'z': [5, 6], 'w': [7, 8]},
        ...                   columns=['x', 'y', 'z', 'w'])
        >>> df
           x  y  z  w
        0  1  3  5  7
        1  2  4  6  8
        >>> df_copy = df.copy()
        >>> df_copy
           x  y  z  w
        0  1  3  5  7
        1  2  4  6  8
        """
    def dropna(self, axis: Axis = 0, how: str = 'any', thresh: int | None = None, subset: Name | List[Name] | None = None, inplace: bool = False) -> DataFrame | None:
        '''
        Remove missing values.

        Parameters
        ----------
        axis : {0 or \'index\'}, default 0
            Determine if rows or columns which contain missing values are
            removed.

            * 0, or \'index\' : Drop rows which contain missing values.
        how : {\'any\', \'all\'}, default \'any\'
            Determine if row or column is removed from DataFrame, when we have
            at least one NA or all NA.

            * \'any\' : If any NA values are present, drop that row or column.
            * \'all\' : If all values are NA, drop that row or column.

        thresh : int, optional
            Require that many non-NA values.
        subset : array-like, optional
            Labels along other axis to consider, e.g. if you are dropping rows
            these would be a list of columns to include.
        inplace : bool, default False
            If True, do operation inplace and return None.

        Returns
        -------
        DataFrame
            DataFrame with NA entries dropped from it.

        See Also
        --------
        DataFrame.drop : Drop specified labels from columns.
        DataFrame.isnull: Indicate missing values.
        DataFrame.notnull : Indicate existing (non-missing) values.

        Examples
        --------
        >>> df = ps.DataFrame({"name": [\'Alfred\', \'Batman\', \'Catwoman\'],
        ...                    "toy": [None, \'Batmobile\', \'Bullwhip\'],
        ...                    "born": [None, "1940-04-25", None]},
        ...                   columns=[\'name\', \'toy\', \'born\'])
        >>> df
               name        toy        born
        0    Alfred       None        None
        1    Batman  Batmobile  1940-04-25
        2  Catwoman   Bullwhip        None

        Drop the rows where at least one element is missing.

        >>> df.dropna()
             name        toy        born
        1  Batman  Batmobile  1940-04-25

        Drop the columns where at least one element is missing.

        >>> df.dropna(axis=\'columns\')
               name
        0    Alfred
        1    Batman
        2  Catwoman

        Drop the rows where all elements are missing.

        >>> df.dropna(how=\'all\')
               name        toy        born
        0    Alfred       None        None
        1    Batman  Batmobile  1940-04-25
        2  Catwoman   Bullwhip        None

        Keep only the rows with at least 2 non-NA values.

        >>> df.dropna(thresh=2)
               name        toy        born
        1    Batman  Batmobile  1940-04-25
        2  Catwoman   Bullwhip        None

        Define in which columns to look for missing values.

        >>> df.dropna(subset=[\'name\', \'born\'])
             name        toy        born
        1  Batman  Batmobile  1940-04-25

        Keep the DataFrame with valid entries in the same variable.

        >>> df.dropna(inplace=True)
        >>> df
             name        toy        born
        1  Batman  Batmobile  1940-04-25
        '''
    def fillna(self, value: Any | Dict[Name, Any] | None = None, method: str | None = None, axis: Axis | None = None, inplace: bool = False, limit: int | None = None) -> DataFrame | None:
        """Fill NA/NaN values.

        .. note:: the current implementation of 'method' parameter in fillna uses Spark's Window
            without specifying partition specification. This leads to moving all data into
            a single partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

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
        ...     'A': [None, 3, None, None],
        ...     'B': [2, 4, None, 3],
        ...     'C': [None, None, None, 1],
        ...     'D': [0, 1, 5, 4]
        ...     },
        ...     columns=['A', 'B', 'C', 'D'])
        >>> df
             A    B    C  D
        0  NaN  2.0  NaN  0
        1  3.0  4.0  NaN  1
        2  NaN  NaN  NaN  5
        3  NaN  3.0  1.0  4

        Replace all NaN elements with 0s.

        >>> df.fillna(0)
             A    B    C  D
        0  0.0  2.0  0.0  0
        1  3.0  4.0  0.0  1
        2  0.0  0.0  0.0  5
        3  0.0  3.0  1.0  4

        We can also propagate non-null values forward or backward.

        >>> df.fillna(method='ffill')
             A    B    C  D
        0  NaN  2.0  NaN  0
        1  3.0  4.0  NaN  1
        2  3.0  4.0  NaN  5
        3  3.0  3.0  1.0  4

        Replace all NaN elements in column 'A', 'B', 'C', and 'D', with 0, 1,
        2, and 3 respectively.

        >>> values = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
        >>> df.fillna(value=values)
             A    B    C  D
        0  0.0  2.0  2.0  0
        1  3.0  4.0  2.0  1
        2  0.0  1.0  2.0  5
        3  0.0  3.0  1.0  4
        """
    def interpolate(self, method: str = 'linear', limit: int | None = None, limit_direction: str | None = None, limit_area: str | None = None) -> DataFrame: ...
    def replace(self, to_replace: Any | List | Tuple | Dict | None = None, value: Any | None = None, inplace: bool = False, limit: int | None = None, regex: bool = False, method: str = 'pad') -> DataFrame | None:
        '''
        Returns a new DataFrame replacing a value with another value.

        Parameters
        ----------
        to_replace : int, float, string, list, tuple or dict
            Value to be replaced.
        value : int, float, string, list or tuple
            Value to use to replace holes. The replacement value must be an int, float,
            or string.
            If value is a list or tuple, value should be of the same length with to_replace.
        inplace : boolean, default False
            Fill in place (do not create a new object)

        Returns
        -------
        DataFrame
            Object after replacement.

        Examples
        --------
        >>> df = ps.DataFrame({"name": [\'Ironman\', \'Captain America\', \'Thor\', \'Hulk\'],
        ...                    "weapon": [\'Mark-45\', \'Shield\', \'Mjolnir\', \'Smash\']},
        ...                   columns=[\'name\', \'weapon\'])
        >>> df
                      name   weapon
        0          Ironman  Mark-45
        1  Captain America   Shield
        2             Thor  Mjolnir
        3             Hulk    Smash

        Scalar `to_replace` and `value`

        >>> df.replace(\'Ironman\', \'War-Machine\')
                      name   weapon
        0      War-Machine  Mark-45
        1  Captain America   Shield
        2             Thor  Mjolnir
        3             Hulk    Smash

        List like `to_replace` and `value`

        >>> df.replace([\'Ironman\', \'Captain America\'], [\'Rescue\', \'Hawkeye\'], inplace=True)
        >>> df
              name   weapon
        0   Rescue  Mark-45
        1  Hawkeye   Shield
        2     Thor  Mjolnir
        3     Hulk    Smash

        Dicts can be used to specify different replacement values for different existing values
        To use a dict in this way the value parameter should be None

        >>> df.replace({\'Mjolnir\': \'Stormbuster\'})
              name       weapon
        0   Rescue      Mark-45
        1  Hawkeye       Shield
        2     Thor  Stormbuster
        3     Hulk        Smash

        Dict can specify that different values should be replaced in different columns
        The value parameter should not be None in this case

        >>> df.replace({\'weapon\': \'Mjolnir\'}, \'Stormbuster\')
              name       weapon
        0   Rescue      Mark-45
        1  Hawkeye       Shield
        2     Thor  Stormbuster
        3     Hulk        Smash

        Nested dictionaries
        The value parameter should be None to use a nested dict in this way

        >>> df.replace({\'weapon\': {\'Mjolnir\': \'Stormbuster\'}})
              name       weapon
        0   Rescue      Mark-45
        1  Hawkeye       Shield
        2     Thor  Stormbuster
        3     Hulk        Smash
        '''
    def clip(self, lower: float | int = None, upper: float | int = None) -> DataFrame:
        '''
        Trim values at input threshold(s).

        Assigns values outside boundary-to-boundary values.

        Parameters
        ----------
        lower : float or int, default None
            Minimum threshold value. All values below this threshold will be set to it.
        upper : float or int, default None
            Maximum threshold value. All values above this threshold will be set to it.

        Returns
        -------
        DataFrame
            DataFrame with the values outside the clip boundaries replaced.

        Examples
        --------
        >>> ps.DataFrame({\'A\': [0, 2, 4]}).clip(1, 3)
           A
        0  1
        1  2
        2  3

        Notes
        -----
        One difference between this implementation and pandas is that running
        pd.DataFrame({\'A\': [\'a\', \'b\']}).clip(0, 1) will crash with "TypeError: \'<=\' not supported
        between instances of \'str\' and \'int\'" while ps.DataFrame({\'A\': [\'a\', \'b\']}).clip(0, 1)
        will output the original DataFrame, simply ignoring the incompatible types.
        '''
    def head(self, n: int = 5) -> DataFrame:
        """
        Return the first `n` rows.

        This function returns the first `n` rows for the object based
        on position. It is useful for quickly testing if your object
        has the right type of data in it.

        Parameters
        ----------
        n : int, default 5
            Number of rows to select.

        Returns
        -------
        obj_head : same type as caller
            The first `n` rows of the caller object.

        Examples
        --------
        >>> df = ps.DataFrame({'animal':['alligator', 'bee', 'falcon', 'lion',
        ...                    'monkey', 'parrot', 'shark', 'whale', 'zebra']})
        >>> df
              animal
        0  alligator
        1        bee
        2     falcon
        3       lion
        4     monkey
        5     parrot
        6      shark
        7      whale
        8      zebra

        Viewing the first 5 lines

        >>> df.head()
              animal
        0  alligator
        1        bee
        2     falcon
        3       lion
        4     monkey

        Viewing the first `n` lines (three in this case)

        >>> df.head(3)
              animal
        0  alligator
        1        bee
        2     falcon
        """
    def last(self, offset: str | DateOffset) -> DataFrame:
        """
        Select final periods of time series data based on a date offset.

        When having a DataFrame with dates as index, this function can
        select the last few rows based on a date offset.

        Parameters
        ----------
        offset : str or DateOffset
            The offset length of the data that will be selected. For instance,
            '3D' will display all the rows having their index within the last 3 days.

        Returns
        -------
        DataFrame
            A subset of the caller.

        Raises
        ------
        TypeError
            If the index is not a :class:`DatetimeIndex`

        Examples
        --------

        >>> index = pd.date_range('2018-04-09', periods=4, freq='2D')
        >>> psdf = ps.DataFrame({'A': [1, 2, 3, 4]}, index=index)
        >>> psdf
                    A
        2018-04-09  1
        2018-04-11  2
        2018-04-13  3
        2018-04-15  4

        Get the rows for the last 3 days:

        >>> psdf.last('3D')
                    A
        2018-04-13  3
        2018-04-15  4

        Notice the data for 3 last calendar days were returned, not the last
        3 observed days in the dataset, and therefore data for 2018-04-11 was
        not returned.
        """
    def first(self, offset: str | DateOffset) -> DataFrame:
        """
        Select first periods of time series data based on a date offset.

        When having a DataFrame with dates as index, this function can
        select the first few rows based on a date offset.

        Parameters
        ----------
        offset : str or DateOffset
            The offset length of the data that will be selected. For instance,
            '3D' will display all the rows having their index within the first 3 days.

        Returns
        -------
        DataFrame
            A subset of the caller.

        Raises
        ------
        TypeError
            If the index is not a :class:`DatetimeIndex`

        Examples
        --------

        >>> index = pd.date_range('2018-04-09', periods=4, freq='2D')
        >>> psdf = ps.DataFrame({'A': [1, 2, 3, 4]}, index=index)
        >>> psdf
                    A
        2018-04-09  1
        2018-04-11  2
        2018-04-13  3
        2018-04-15  4

        Get the rows for the last 3 days:

        >>> psdf.first('3D')
                    A
        2018-04-09  1
        2018-04-11  2

        Notice the data for 3 first calendar days were returned, not the first
        3 observed days in the dataset, and therefore data for 2018-04-13 was
        not returned.
        """
    def pivot_table(self, values: Name | List[Name] | None = None, index: List[Name] | None = None, columns: Name | None = None, aggfunc: str | Dict[Name, str] = 'mean', fill_value: Any | None = None) -> DataFrame:
        '''
        Create a spreadsheet-style pivot table as a DataFrame. The levels in
        the pivot table will be stored in MultiIndex objects (hierarchical
        indexes) on the index and columns of the result DataFrame.

        Parameters
        ----------
        values : column to aggregate.
            They should be either a list less than three or a string.
        index : column (string) or list of columns
            If an array is passed, it must be the same length as the data.
            The list should contain string.
        columns : column
            Columns used in the pivot operation. Only one column is supported and
            it should be a string.
        aggfunc : function (string), dict, default mean
            If dict is passed, the key is column to aggregate and value
            is function or list of functions.
        fill_value : scalar, default None
            Value to replace missing values with.

        Returns
        -------
        table : DataFrame

        Examples
        --------
        >>> df = ps.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
        ...                          "bar", "bar", "bar", "bar"],
        ...                    "B": ["one", "one", "one", "two", "two",
        ...                          "one", "one", "two", "two"],
        ...                    "C": ["small", "large", "large", "small",
        ...                          "small", "large", "small", "small",
        ...                          "large"],
        ...                    "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
        ...                    "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]},
        ...                   columns=[\'A\', \'B\', \'C\', \'D\', \'E\'])
        >>> df
             A    B      C  D  E
        0  foo  one  small  1  2
        1  foo  one  large  2  4
        2  foo  one  large  2  5
        3  foo  two  small  3  5
        4  foo  two  small  3  6
        5  bar  one  large  4  6
        6  bar  one  small  5  8
        7  bar  two  small  6  9
        8  bar  two  large  7  9

        This first example aggregates values by taking the sum.

        >>> table = df.pivot_table(values=\'D\', index=[\'A\', \'B\'],
        ...                        columns=\'C\', aggfunc=\'sum\')
        >>> table.sort_index()  # doctest: +NORMALIZE_WHITESPACE
        C        large  small
        A   B
        bar one    4.0      5
            two    7.0      6
        foo one    4.0      1
            two    NaN      6

        We can also fill missing values using the `fill_value` parameter.

        >>> table = df.pivot_table(values=\'D\', index=[\'A\', \'B\'],
        ...                        columns=\'C\', aggfunc=\'sum\', fill_value=0)
        >>> table.sort_index()  # doctest: +NORMALIZE_WHITESPACE
        C        large  small
        A   B
        bar one      4      5
            two      7      6
        foo one      4      1
            two      0      6

        We can also calculate multiple types of aggregations for any given
        value column.

        >>> table = df.pivot_table(values=[\'D\'], index =[\'C\'],
        ...                        columns="A", aggfunc={\'D\': \'mean\'})
        >>> table.sort_index()  # doctest: +NORMALIZE_WHITESPACE
                 D
        A      bar       foo
        C
        large  5.5  2.000000
        small  5.5  2.333333

        The next example aggregates on multiple values.

        >>> table = df.pivot_table(index=[\'C\'], columns="A", values=[\'D\', \'E\'],
        ...                         aggfunc={\'D\': \'mean\', \'E\': \'sum\'})
        >>> table.sort_index() # doctest: +NORMALIZE_WHITESPACE
                 D             E
        A      bar       foo bar foo
        C
        large  5.5  2.000000  15   9
        small  5.5  2.333333  17  13
        '''
    def pivot(self, index: Name | None = None, columns: Name | None = None, values: Name | None = None) -> DataFrame:
        '''
        Return reshaped DataFrame organized by given index / column values.

        Reshape data (produce a "pivot" table) based on column values. Uses
        unique values from specified `index` / `columns` to form axes of the
        resulting DataFrame. This function does not support data
        aggregation.

        Parameters
        ----------
        index : string, optional
            Column to use to make new frame\'s index. If None, uses
            existing index.
        columns : string
            Column to use to make new frame\'s columns.
        values : string, object or a list of the previous
            Column(s) to use for populating new frame\'s values.

        Returns
        -------
        DataFrame
            Returns reshaped DataFrame.

        See Also
        --------
        DataFrame.pivot_table : Generalization of pivot that can handle
            duplicate values for one index/column pair.

        Examples
        --------
        >>> df = ps.DataFrame({\'foo\': [\'one\', \'one\', \'one\', \'two\', \'two\',
        ...                            \'two\'],
        ...                    \'bar\': [\'A\', \'B\', \'C\', \'A\', \'B\', \'C\'],
        ...                    \'baz\': [1, 2, 3, 4, 5, 6],
        ...                    \'zoo\': [\'x\', \'y\', \'z\', \'q\', \'w\', \'t\']},
        ...                   columns=[\'foo\', \'bar\', \'baz\', \'zoo\'])
        >>> df
           foo bar  baz zoo
        0  one   A    1   x
        1  one   B    2   y
        2  one   C    3   z
        3  two   A    4   q
        4  two   B    5   w
        5  two   C    6   t

        >>> df.pivot(index=\'foo\', columns=\'bar\', values=\'baz\').sort_index()
        ... # doctest: +NORMALIZE_WHITESPACE
        bar  A  B  C
        foo
        one  1  2  3
        two  4  5  6

        >>> df.pivot(columns=\'bar\', values=\'baz\').sort_index()  # doctest: +NORMALIZE_WHITESPACE
        bar  A    B    C
        0  1.0  NaN  NaN
        1  NaN  2.0  NaN
        2  NaN  NaN  3.0
        3  4.0  NaN  NaN
        4  NaN  5.0  NaN
        5  NaN  NaN  6.0

        Notice that, unlike pandas raises an ValueError when duplicated values are found.
        Pandas-on-Spark\'s pivot still works with its first value it meets during operation because
        pivot is an expensive operation, and it is preferred to permissively execute over failing
        fast when processing large data.

        >>> df = ps.DataFrame({"foo": [\'one\', \'one\', \'two\', \'two\'],
        ...                    "bar": [\'A\', \'A\', \'B\', \'C\'],
        ...                    "baz": [1, 2, 3, 4]}, columns=[\'foo\', \'bar\', \'baz\'])
        >>> df
           foo bar  baz
        0  one   A    1
        1  one   A    2
        2  two   B    3
        3  two   C    4

        >>> df.pivot(index=\'foo\', columns=\'bar\', values=\'baz\').sort_index()
        ... # doctest: +NORMALIZE_WHITESPACE
        bar    A    B    C
        foo
        one  1.0  NaN  NaN
        two  NaN  3.0  4.0

        It also supports multi-index and multi-index column.
        >>> df.columns = pd.MultiIndex.from_tuples([(\'a\', \'foo\'), (\'a\', \'bar\'), (\'b\', \'baz\')])

        >>> df = df.set_index((\'a\', \'bar\'), append=True)
        >>> df  # doctest: +NORMALIZE_WHITESPACE
                      a   b
                    foo baz
          (a, bar)
        0 A         one   1
        1 A         one   2
        2 B         two   3
        3 C         two   4

        >>> df.pivot(columns=(\'a\', \'foo\'), values=(\'b\', \'baz\')).sort_index()
        ... # doctest: +NORMALIZE_WHITESPACE
        (\'a\', \'foo\')  one  two
          (a, bar)
        0 A           1.0  NaN
        1 A           2.0  NaN
        2 B           NaN  3.0
        3 C           NaN  4.0

        '''
    @property
    def columns(self) -> pd.Index:
        """The column labels of the DataFrame."""
    @columns.setter
    def columns(self, columns: pd.Index | List[Name]) -> None: ...
    @property
    def dtypes(self) -> pd.Series:
        """Return the dtypes in the DataFrame.

        This returns a Series with the data type of each column. The result's index is the original
        DataFrame's columns. Columns with mixed types are stored with the object dtype.

        Returns
        -------
        pd.Series
            The data type of each column.

        Examples
        --------
        >>> df = ps.DataFrame({'a': list('abc'),
        ...                    'b': list(range(1, 4)),
        ...                    'c': np.arange(3, 6).astype('i1'),
        ...                    'd': np.arange(4.0, 7.0, dtype='float64'),
        ...                    'e': [True, False, True],
        ...                    'f': pd.date_range('20130101', periods=3)},
        ...                   columns=['a', 'b', 'c', 'd', 'e', 'f'])
        >>> df.dtypes
        a            object
        b             int64
        c              int8
        d           float64
        e              bool
        f    datetime64[ns]
        dtype: object
        """
    def select_dtypes(self, include: str | List[str] | None = None, exclude: str | List[str] | None = None) -> DataFrame:
        """
        Return a subset of the DataFrame's columns based on the column dtypes.

        Parameters
        ----------
        include, exclude : scalar or list-like
            A selection of dtypes or strings to be included/excluded. At least
            one of these parameters must be supplied. It also takes Spark SQL
            DDL type strings, for instance, 'string' and 'date'.

        Returns
        -------
        DataFrame
            The subset of the frame including the dtypes in ``include`` and
            excluding the dtypes in ``exclude``.

        Raises
        ------
        ValueError
            * If both of ``include`` and ``exclude`` are empty

                >>> df = ps.DataFrame({'a': [1, 2] * 3,
                ...                    'b': [True, False] * 3,
                ...                    'c': [1.0, 2.0] * 3})
                >>> df.select_dtypes()
                Traceback (most recent call last):
                ...
                ValueError: at least one of include or exclude must be nonempty

            * If ``include`` and ``exclude`` have overlapping elements

                >>> df = ps.DataFrame({'a': [1, 2] * 3,
                ...                    'b': [True, False] * 3,
                ...                    'c': [1.0, 2.0] * 3})
                >>> df.select_dtypes(include='a', exclude='a')
                Traceback (most recent call last):
                ...
                ValueError: include and exclude overlap on {'a'}

        Notes
        -----
        * To select datetimes, use ``np.datetime64``, ``'datetime'`` or
          ``'datetime64'``

        Examples
        --------
        >>> df = ps.DataFrame({'a': [1, 2] * 3,
        ...                    'b': [True, False] * 3,
        ...                    'c': [1.0, 2.0] * 3,
        ...                    'd': ['a', 'b'] * 3}, columns=['a', 'b', 'c', 'd'])
        >>> df
           a      b    c  d
        0  1   True  1.0  a
        1  2  False  2.0  b
        2  1   True  1.0  a
        3  2  False  2.0  b
        4  1   True  1.0  a
        5  2  False  2.0  b

        >>> df.select_dtypes(include='bool')
               b
        0   True
        1  False
        2   True
        3  False
        4   True
        5  False

        >>> df.select_dtypes(include=['float64'], exclude=['int'])
             c
        0  1.0
        1  2.0
        2  1.0
        3  2.0
        4  1.0
        5  2.0

        >>> df.select_dtypes(include=['int'], exclude=['float64'])
           a
        0  1
        1  2
        2  1
        3  2
        4  1
        5  2

        >>> df.select_dtypes(exclude=['int'])
               b    c  d
        0   True  1.0  a
        1  False  2.0  b
        2   True  1.0  a
        3  False  2.0  b
        4   True  1.0  a
        5  False  2.0  b

        Spark SQL DDL type strings can be used as well.

        >>> df.select_dtypes(exclude=['string'])
           a      b    c
        0  1   True  1.0
        1  2  False  2.0
        2  1   True  1.0
        3  2  False  2.0
        4  1   True  1.0
        5  2  False  2.0
        """
    def droplevel(self, level: int | Name | List[int | Name], axis: Axis = 0) -> DataFrame:
        '''
        Return DataFrame with requested index / column level(s) removed.

        Parameters
        ----------
        level: int, str, or list-like
            If a string is given, must be the name of a level If list-like, elements must
            be names or positional indexes of levels.

        axis: {0 or ‘index’, 1 or ‘columns’}, default 0

        Returns
        -------
        DataFrame with requested index / column level(s) removed.

        Examples
        --------
        >>> df = ps.DataFrame(
        ...     [[3, 4], [7, 8], [11, 12]],
        ...     index=pd.MultiIndex.from_tuples([(1, 2), (5, 6), (9, 10)], names=["a", "b"]),
        ... )

        >>> df.columns = pd.MultiIndex.from_tuples([
        ...   (\'c\', \'e\'), (\'d\', \'f\')
        ... ], names=[\'level_1\', \'level_2\'])

        >>> df  # doctest: +NORMALIZE_WHITESPACE
        level_1   c   d
        level_2   e   f
        a b
        1 2      3   4
        5 6      7   8
        9 10    11  12

        >>> df.droplevel(\'a\')  # doctest: +NORMALIZE_WHITESPACE
        level_1   c   d
        level_2   e   f
        b
        2        3   4
        6        7   8
        10      11  12

        >>> df.droplevel(\'level_2\', axis=1)  # doctest: +NORMALIZE_WHITESPACE
        level_1   c   d
        a b
        1 2      3   4
        5 6      7   8
        9 10    11  12
        '''
    def drop(self, labels: Name | List[Name] | None = None, axis: Axis | None = 0, index: Name | List[Name] = None, columns: Name | List[Name] = None) -> DataFrame:
        """
        Drop specified labels from columns.

        Remove rows and/or columns by specifying label names and corresponding axis,
        or by specifying directly index and/or column names.
        Drop rows of a MultiIndex DataFrame is not supported yet.

        Parameters
        ----------
        labels : single label or list-like
            Column labels to drop.
        axis : {0 or 'index', 1 or 'columns'}, default 0

            .. versionchanged:: 3.3
               Set dropping by index is default.
        index : single label or list-like
            Alternative to specifying axis (``labels, axis=0``
            is equivalent to ``index=columns``).

            .. versionchanged:: 3.3
               Added dropping rows by 'index'.
        columns : single label or list-like
            Alternative to specifying axis (``labels, axis=1``
            is equivalent to ``columns=labels``).

        Returns
        -------
        dropped : DataFrame

        See Also
        --------
        Series.dropna

        Examples
        --------
        >>> df = ps.DataFrame(np.arange(12).reshape(3, 4), columns=['A', 'B', 'C', 'D'])
        >>> df
           A  B   C   D
        0  0  1   2   3
        1  4  5   6   7
        2  8  9  10  11

        Drop columns

        >>> df.drop(['B', 'C'], axis=1)
           A   D
        0  0   3
        1  4   7
        2  8  11

        >>> df.drop(columns=['B', 'C'])
           A   D
        0  0   3
        1  4   7
        2  8  11

        Drop a row by index

        >>> df.drop([0, 1])
           A  B   C   D
        2  8  9  10  11

        >>> df.drop(index=[0, 1], columns='A')
           B   C   D
        2  9  10  11

        Also support dropping columns for MultiIndex

        >>> df = ps.DataFrame({'x': [1, 2], 'y': [3, 4], 'z': [5, 6], 'w': [7, 8]},
        ...                   columns=['x', 'y', 'z', 'w'])
        >>> columns = [('a', 'x'), ('a', 'y'), ('b', 'z'), ('b', 'w')]
        >>> df.columns = pd.MultiIndex.from_tuples(columns)
        >>> df  # doctest: +NORMALIZE_WHITESPACE
           a     b
           x  y  z  w
        0  1  3  5  7
        1  2  4  6  8
        >>> df.drop(labels='a', axis=1)  # doctest: +NORMALIZE_WHITESPACE
           b
           z  w
        0  5  7
        1  6  8

        Notes
        -----
        Currently, dropping rows of a MultiIndex DataFrame is not supported yet.
        """
    def sort_values(self, by: Name | List[Name], ascending: bool | List[bool] = True, inplace: bool = False, na_position: str = 'last', ignore_index: bool = False) -> DataFrame | None:
        """
        Sort by the values along either axis.

        Parameters
        ----------
        by : str or list of str
        ascending : bool or list of bool, default True
             Sort ascending vs. descending. Specify list for multiple sort
             orders.  If this is a list of bools, must match the length of
             the by.
        inplace : bool, default False
             if True, perform operation in-place
        na_position : {'first', 'last'}, default 'last'
             `first` puts NaNs at the beginning, `last` puts NaNs at the end
        ignore_index : bool, default False
            If True, the resulting axis will be labeled 0, 1, …, n - 1.

        Returns
        -------
        sorted_obj : DataFrame

        Examples
        --------
        >>> df = ps.DataFrame({
        ...     'col1': ['A', 'B', None, 'D', 'C'],
        ...     'col2': [2, 9, 8, 7, 4],
        ...     'col3': [0, 9, 4, 2, 3],
        ...   },
        ...   columns=['col1', 'col2', 'col3'],
        ...   index=['a', 'b', 'c', 'd', 'e'])
        >>> df
           col1  col2  col3
        a     A     2     0
        b     B     9     9
        c  None     8     4
        d     D     7     2
        e     C     4     3

        Sort by col1

        >>> df.sort_values(by=['col1'])
           col1  col2  col3
        a     A     2     0
        b     B     9     9
        e     C     4     3
        d     D     7     2
        c  None     8     4

        Ignore index for the resulting axis

        >>> df.sort_values(by=['col1'], ignore_index=True)
           col1  col2  col3
        0     A     2     0
        1     B     9     9
        2     C     4     3
        3     D     7     2
        4  None     8     4

        Sort Descending

        >>> df.sort_values(by='col1', ascending=False)
           col1  col2  col3
        d     D     7     2
        e     C     4     3
        b     B     9     9
        a     A     2     0
        c  None     8     4

        Sort by multiple columns

        >>> df = ps.DataFrame({
        ...     'col1': ['A', 'A', 'B', None, 'D', 'C'],
        ...     'col2': [2, 1, 9, 8, 7, 4],
        ...     'col3': [0, 1, 9, 4, 2, 3],
        ...   },
        ...   columns=['col1', 'col2', 'col3'])
        >>> df.sort_values(by=['col1', 'col2'])
           col1  col2  col3
        1     A     1     1
        0     A     2     0
        2     B     9     9
        5     C     4     3
        4     D     7     2
        3  None     8     4
        """
    def sort_index(self, axis: Axis = 0, level: int | List[int] | None = None, ascending: bool = True, inplace: bool = False, kind: str = None, na_position: str = 'last', ignore_index: bool = False) -> DataFrame | None:
        """
        Sort object by labels (along an axis)

        Parameters
        ----------
        axis : index, columns to direct sorting. Currently, only axis = 0 is supported.
        level : int or level name or list of ints or list of level names
            if not None, sort on values in specified index level(s)
        ascending : boolean, default True
            Sort ascending vs. descending
        inplace : bool, default False
            if True, perform operation in-place
        kind : str, default None
            pandas-on-Spark does not allow specifying the sorting algorithm now,
            default None
        na_position : {‘first’, ‘last’}, default ‘last’
            first puts NaNs at the beginning, last puts NaNs at the end. Not implemented for
            MultiIndex.
        ignore_index : bool, default False
            If True, the resulting axis will be labeled 0, 1, …, n - 1.

            .. versionadded:: 3.4.0

        Returns
        -------
        sorted_obj : DataFrame

        Examples
        --------
        >>> df = ps.DataFrame({'A': [2, 1, np.nan]}, index=['b', 'a', np.nan])

        >>> df.sort_index()  # doctest: +SKIP
                A
        a     1.0
        b     2.0
        None  NaN

        >>> df.sort_index(ascending=False)  # doctest: +SKIP
                A
        b     2.0
        a     1.0
        None  NaN

        >>> df.sort_index(na_position='first')  # doctest: +SKIP
                A
        None  NaN
        a     1.0
        b     2.0

        >>> df.sort_index(ignore_index=True)
             A
        0  1.0
        1  2.0
        2  NaN

        >>> df.sort_index(inplace=True)
        >>> df  # doctest: +SKIP
                A
        a     1.0
        b     2.0
        None  NaN

        >>> df = ps.DataFrame({'A': range(4), 'B': range(4)[::-1]},
        ...                   index=[['b', 'b', 'a', 'a'], [1, 0, 1, 0]],
        ...                   columns=['A', 'B'])

        >>> df.sort_index()
             A  B
        a 0  3  0
          1  2  1
        b 0  1  2
          1  0  3

        >>> df.sort_index(level=1)
             A  B
        b 0  1  2
        a 0  3  0
        b 1  0  3
        a 1  2  1

        >>> df.sort_index(level=[1, 0])
             A  B
        a 0  3  0
        b 0  1  2
        a 1  2  1
        b 1  0  3

        >>> df.sort_index(ignore_index=True)
           A  B
        0  3  0
        1  2  1
        2  1  2
        3  0  3
        """
    def swaplevel(self, i: int | Name = -2, j: int | Name = -1, axis: Axis = 0) -> DataFrame:
        """
        Swap levels i and j in a MultiIndex on a particular axis.

        Parameters
        ----------
        i, j : int or str
            Levels of the indices to be swapped. Can pass level name as string.
        axis : {0 or 'index', 1 or 'columns'}, default 0
            The axis to swap levels on. 0 or 'index' for row-wise, 1 or
            'columns' for column-wise.

        Returns
        -------
        DataFrame
            DataFrame with levels swapped in MultiIndex.

        Examples
        --------
        >>> midx = pd.MultiIndex.from_arrays(
        ...     [['red', 'blue'], [1, 2], ['s', 'm']], names = ['color', 'number', 'size'])
        >>> midx  # doctest: +SKIP
        MultiIndex([( 'red', 1, 's'),
                    ('blue', 2, 'm')],
                   names=['color', 'number', 'size'])

        Swap levels in a MultiIndex on index.

        >>> psdf = ps.DataFrame({'x': [5, 6], 'y':[5, 6]}, index=midx)
        >>> psdf  # doctest: +NORMALIZE_WHITESPACE
                           x  y
        color number size
        red   1      s     5  5
        blue  2      m     6  6

        >>> psdf.swaplevel()  # doctest: +NORMALIZE_WHITESPACE
                           x  y
        color size number
        red   s    1       5  5
        blue  m    2       6  6

        >>> psdf.swaplevel(0, 1)  # doctest: +NORMALIZE_WHITESPACE
                           x  y
        number color size
        1      red   s     5  5
        2      blue  m     6  6

        >>> psdf.swaplevel('number', 'size')  # doctest: +NORMALIZE_WHITESPACE
                           x  y
        color size number
        red   s    1       5  5
        blue  m    2       6  6

        Swap levels in a MultiIndex on columns.

        >>> psdf = ps.DataFrame({'x': [5, 6], 'y':[5, 6]})
        >>> psdf.columns = midx
        >>> psdf
        color  red blue
        number   1    2
        size     s    m
        0        5    5
        1        6    6

        >>> psdf.swaplevel(axis=1)
        color  red blue
        size     s    m
        number   1    2
        0        5    5
        1        6    6

        >>> psdf.swaplevel(axis=1)
        color  red blue
        size     s    m
        number   1    2
        0        5    5
        1        6    6

        >>> psdf.swaplevel(0, 1, axis=1)
        number   1    2
        color  red blue
        size     s    m
        0        5    5
        1        6    6

        >>> psdf.swaplevel('number', 'color', axis=1)
        number   1    2
        color  red blue
        size     s    m
        0        5    5
        1        6    6
        """
    def swapaxes(self, i: Axis, j: Axis, copy: bool = True) -> DataFrame:
        """
        Interchange axes and swap values axes appropriately.

        .. note:: This method is based on an expensive operation due to the nature
            of big data. Internally it needs to generate each row for each value, and
            then group twice - it is a huge operation. To prevent misuse, this method
            has the 'compute.max_rows' default limit of input length and raises a ValueError.

                >>> from pyspark.pandas.config import option_context
                >>> with option_context('compute.max_rows', 1000):  # doctest: +NORMALIZE_WHITESPACE
                ...     ps.DataFrame({'a': range(1001)}).swapaxes(i=0, j=1)
                Traceback (most recent call last):
                  ...
                ValueError: Current DataFrame's length exceeds the given limit of 1000 rows.
                Please set 'compute.max_rows' by using 'pyspark.pandas.config.set_option'
                to retrieve more than 1000 rows. Note that, before changing the
                'compute.max_rows', this operation is considerably expensive.

        Parameters
        ----------
        i: {0 or 'index', 1 or 'columns'}. The axis to swap.
        j: {0 or 'index', 1 or 'columns'}. The axis to swap.
        copy : bool, default True.

        Returns
        -------
        DataFrame

        Examples
        --------
        >>> psdf = ps.DataFrame(
        ...     [[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['x', 'y', 'z'], columns=['a', 'b', 'c']
        ... )
        >>> psdf
           a  b  c
        x  1  2  3
        y  4  5  6
        z  7  8  9
        >>> psdf.swapaxes(i=1, j=0)
           x  y  z
        a  1  4  7
        b  2  5  8
        c  3  6  9
        >>> psdf.swapaxes(i=1, j=1)
           a  b  c
        x  1  2  3
        y  4  5  6
        z  7  8  9
        """
    def nlargest(self, n: int, columns: Name | List[Name], keep: str = 'first') -> DataFrame:
        '''
        Return the first `n` rows ordered by `columns` in descending order.

        Return the first `n` rows with the largest values in `columns`, in
        descending order. The columns that are not specified are returned as
        well, but not used for ordering.

        This method is equivalent to
        ``df.sort_values(columns, ascending=False).head(n)``, but more
        performant in pandas.
        In pandas-on-Spark, thanks to Spark\'s lazy execution and query optimizer,
        the two would have same performance.

        Parameters
        ----------
        n : int
            Number of rows to return.
        columns : label or list of labels
            Column label(s) to order by.
        keep : {\'first\', \'last\'}, default \'first\'. \'all\' is not implemented yet.
            Determines which duplicates (if any) to keep.
            - ``first`` : Keep the first occurrence.
            - ``last`` : Keep the last occurrence.

        Returns
        -------
        DataFrame
            The first `n` rows ordered by the given columns in descending
            order.

        See Also
        --------
        DataFrame.nsmallest : Return the first `n` rows ordered by `columns` in
            ascending order.
        DataFrame.sort_values : Sort DataFrame by the values.
        DataFrame.head : Return the first `n` rows without re-ordering.

        Notes
        -----

        This function cannot be used with all column types. For example, when
        specifying columns with `object` or `category` dtypes, ``TypeError`` is
        raised.

        Examples
        --------
        >>> df = ps.DataFrame({\'X\': [1, 2, 3, 5, 6, 7, np.nan],
        ...                    \'Y\': [6, 7, 8, 9, 10, 11, 12]})
        >>> df
             X   Y
        0  1.0   6
        1  2.0   7
        2  3.0   8
        3  5.0   9
        4  6.0  10
        5  7.0  11
        6  NaN  12

        In the following example, we will use ``nlargest`` to select the three
        rows having the largest values in column "X".

        >>> df.nlargest(n=3, columns=\'X\')
             X   Y
        5  7.0  11
        4  6.0  10
        3  5.0   9

        To order by the largest values in column "Y" and then "X", we can
        specify multiple columns like in the next example.

        >>> df.nlargest(n=3, columns=[\'Y\', \'X\'])
             X   Y
        6  NaN  12
        5  7.0  11
        4  6.0  10

        The examples below show how ties are resolved, which is decided by `keep`.

        >>> tied_df = ps.DataFrame({\'X\': [1, 2, 2, 3, 3]}, index=[\'a\', \'b\', \'c\', \'d\', \'e\'])
        >>> tied_df
           X
        a  1
        b  2
        c  2
        d  3
        e  3

        When using keep=\'first\' (default), ties are resolved in order:

        >>> tied_df.nlargest(3, \'X\')
           X
        d  3
        e  3
        b  2

        >>> tied_df.nlargest(3, \'X\', keep=\'first\')
           X
        d  3
        e  3
        b  2

        When using keep=\'last\', ties are resolved in reverse order:

        >>> tied_df.nlargest(3, \'X\', keep=\'last\')
           X
        e  3
        d  3
        c  2
        '''
    def nsmallest(self, n: int, columns: Name | List[Name], keep: str = 'first') -> DataFrame:
        '''
        Return the first `n` rows ordered by `columns` in ascending order.

        Return the first `n` rows with the smallest values in `columns`, in
        ascending order. The columns that are not specified are returned as
        well, but not used for ordering.

        This method is equivalent to ``df.sort_values(columns, ascending=True).head(n)``,
        but more performant. In pandas-on-Spark, thanks to Spark\'s lazy execution and query
        optimizer, the two would have same performance.

        Parameters
        ----------
        n : int
            Number of items to retrieve.
        columns : list or str
            Column name or names to order by.
        keep : {\'first\', \'last\'}, default \'first\'. \'all\' is not implemented yet.
            Determines which duplicates (if any) to keep.
            - ``first`` : Keep the first occurrence.
            - ``last`` : Keep the last occurrence.

        Returns
        -------
        DataFrame

        See Also
        --------
        DataFrame.nlargest : Return the first `n` rows ordered by `columns` in
            descending order.
        DataFrame.sort_values : Sort DataFrame by the values.
        DataFrame.head : Return the first `n` rows without re-ordering.

        Examples
        --------
        >>> df = ps.DataFrame({\'X\': [1, 2, 3, 5, 6, 7, np.nan],
        ...                    \'Y\': [6, 7, 8, 9, 10, 11, 12]})
        >>> df
             X   Y
        0  1.0   6
        1  2.0   7
        2  3.0   8
        3  5.0   9
        4  6.0  10
        5  7.0  11
        6  NaN  12

        In the following example, we will use ``nsmallest`` to select the
        three rows having the smallest values in column "X".

        >>> df.nsmallest(n=3, columns=\'X\') # doctest: +NORMALIZE_WHITESPACE
             X   Y
        0  1.0   6
        1  2.0   7
        2  3.0   8

        To order by the smallest values in column "Y" and then "X", we can
        specify multiple columns like in the next example.

        >>> df.nsmallest(n=3, columns=[\'Y\', \'X\']) # doctest: +NORMALIZE_WHITESPACE
             X   Y
        0  1.0   6
        1  2.0   7
        2  3.0   8

        The examples below show how ties are resolved, which is decided by `keep`.

        >>> tied_df = ps.DataFrame({\'X\': [1, 1, 2, 2, 3]}, index=[\'a\', \'b\', \'c\', \'d\', \'e\'])
        >>> tied_df
           X
        a  1
        b  1
        c  2
        d  2
        e  3

        When using keep=\'first\' (default), ties are resolved in order:

        >>> tied_df.nsmallest(3, \'X\')
           X
        a  1
        b  1
        c  2

        >>> tied_df.nsmallest(3, \'X\', keep=\'first\')
           X
        a  1
        b  1
        c  2

        When using keep=\'last\', ties are resolved in reverse order:

        >>> tied_df.nsmallest(3, \'X\', keep=\'last\')
           X
        b  1
        a  1
        d  2
        '''
    def isin(self, values: List | Dict) -> DataFrame:
        """
        Whether each element in the DataFrame is contained in values.

        Parameters
        ----------
        values : iterable or dict
           The sequence of values to test. If values are a dict,
           the keys must be the column names, which must match.
           Series and DataFrame are not supported.

        Returns
        -------
        DataFrame
            DataFrame of booleans showing whether each element in the DataFrame
            is contained in values.

        Examples
        --------
        >>> df = ps.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]},
        ...                   index=['falcon', 'dog'],
        ...                   columns=['num_legs', 'num_wings'])
        >>> df
                num_legs  num_wings
        falcon         2          2
        dog            4          0

        When ``values`` is a list check whether every value in the DataFrame
        is present in the list (which animals have 0 or 2 legs or wings)

        >>> df.isin([0, 2])
                num_legs  num_wings
        falcon      True       True
        dog        False       True

        When ``values`` is a dict, we can pass values to check for each
        column separately:

        >>> df.isin({'num_wings': [0, 3]})
                num_legs  num_wings
        falcon     False      False
        dog        False       True
        """
    @property
    def shape(self) -> Tuple[int, int]:
        """
        Return a tuple representing the dimensionality of the DataFrame.

        Examples
        --------
        >>> df = ps.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.shape
        (2, 2)

        >>> df = ps.DataFrame({'col1': [1, 2], 'col2': [3, 4],
        ...                    'col3': [5, 6]})
        >>> df.shape
        (2, 3)
        """
    def merge(self, right: DataFrame, how: str = 'inner', on: Name | List[Name] | None = None, left_on: Name | List[Name] | None = None, right_on: Name | List[Name] | None = None, left_index: bool = False, right_index: bool = False, suffixes: Tuple[str, str] = ('_x', '_y')) -> DataFrame:
        """
        Merge DataFrame objects with a database-style join.

        The index of the resulting DataFrame will be one of the following:
            - 0...n if no index is used for merging
            - Index of the left DataFrame if merged only on the index of the right DataFrame
            - Index of the right DataFrame if merged only on the index of the left DataFrame
            - All involved indices if merged using the indices of both DataFrames
                e.g. if `left` with indices (a, x) and `right` with indices (b, x), the result will
                be an index (x, a, b)

        Parameters
        ----------
        right: Object to merge with.
        how: Type of merge to be performed.
            {'left', 'right', 'outer', 'inner'}, default 'inner'

            left: use only keys from left frame, like a SQL left outer join; not preserve
                key order unlike pandas.
            right: use only keys from right frame, like a SQL right outer join; not preserve
                key order unlike pandas.
            outer: use union of keys from both frames, like a SQL full outer join; sort keys
                lexicographically.
            inner: use intersection of keys from both frames, like a SQL inner join;
                not preserve the order of the left keys unlike pandas.
        on: Column or index level names to join on. These must be found in both DataFrames. If on
            is None and not merging on indexes then this defaults to the intersection of the
            columns in both DataFrames.
        left_on: Column or index level names to join on in the left DataFrame. Can also
            be an array or list of arrays of the length of the left DataFrame.
            These arrays are treated as if they are columns.
        right_on: Column or index level names to join on in the right DataFrame. Can also
            be an array or list of arrays of the length of the right DataFrame.
            These arrays are treated as if they are columns.
        left_index: Use the index from the left DataFrame as the join key(s). If it is a
            MultiIndex, the number of keys in the other DataFrame (either the index or a number of
            columns) must match the number of levels.
        right_index: Use the index from the right DataFrame as the join key. Same caveats as
            left_index.
        suffixes: Suffix to apply to overlapping column names in the left and right side,
            respectively.

        Returns
        -------
        DataFrame
            A DataFrame of the two merged objects.

        See Also
        --------
        DataFrame.join : Join columns of another DataFrame.
        DataFrame.update : Modify in place using non-NA values from another DataFrame.
        DataFrame.hint : Specifies some hint on the current DataFrame.
        broadcast : Marks a DataFrame as small enough for use in broadcast joins.

        Examples
        --------
        >>> df1 = ps.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
        ...                     'value': [1, 2, 3, 5]},
        ...                    columns=['lkey', 'value'])
        >>> df2 = ps.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
        ...                     'value': [5, 6, 7, 8]},
        ...                    columns=['rkey', 'value'])
        >>> df1
          lkey  value
        0  foo      1
        1  bar      2
        2  baz      3
        3  foo      5
        >>> df2
          rkey  value
        0  foo      5
        1  bar      6
        2  baz      7
        3  foo      8

        Merge df1 and df2 on the lkey and rkey columns. The value columns have
        the default suffixes, _x and _y, appended.

        >>> merged = df1.merge(df2, left_on='lkey', right_on='rkey')
        >>> merged.sort_values(by=['lkey', 'value_x', 'rkey', 'value_y'])  # doctest: +ELLIPSIS
          lkey  value_x rkey  value_y
        ...bar        2  bar        6
        ...baz        3  baz        7
        ...foo        1  foo        5
        ...foo        1  foo        8
        ...foo        5  foo        5
        ...foo        5  foo        8

        >>> left_psdf = ps.DataFrame({'A': [1, 2]})
        >>> right_psdf = ps.DataFrame({'B': ['x', 'y']}, index=[1, 2])

        >>> left_psdf.merge(right_psdf, left_index=True, right_index=True).sort_index()
           A  B
        1  2  x

        >>> left_psdf.merge(right_psdf, left_index=True, right_index=True, how='left').sort_index()
           A     B
        0  1  None
        1  2     x

        >>> left_psdf.merge(right_psdf, left_index=True, right_index=True, how='right').sort_index()
             A  B
        1  2.0  x
        2  NaN  y

        >>> left_psdf.merge(right_psdf, left_index=True, right_index=True, how='outer').sort_index()
             A     B
        0  1.0  None
        1  2.0     x
        2  NaN     y

        Notes
        -----
        As described in #263, joining string columns currently returns None for missing values
            instead of NaN.
        """
    def join(self, right: DataFrame, on: Name | List[Name] | None = None, how: str = 'left', lsuffix: str = '', rsuffix: str = '') -> DataFrame:
        """
        Join columns of another DataFrame.

        Join columns with `right` DataFrame either on index or on a key column. Efficiently join
        multiple DataFrame objects by index at once by passing a list.

        Parameters
        ----------
        right: DataFrame, Series
        on: str, list of str, or array-like, optional
            Column or index level name(s) in the caller to join on the index in `right`, otherwise
            joins index-on-index. If multiple values given, the `right` DataFrame must have a
            MultiIndex. Can pass an array as the join key if it is not already contained in the
            calling DataFrame. Like an Excel VLOOKUP operation.
        how: {'left', 'right', 'outer', 'inner'}, default 'left'
            How to handle the operation of the two objects.

            * left: use `left` frame’s index (or column if on is specified).
            * right: use `right`’s index.
            * outer: form union of `left` frame’s index (or column if on is specified) with
              right’s index, and sort it. lexicographically.
            * inner: form intersection of `left` frame’s index (or column if on is specified)
              with `right`’s index, preserving the order of the `left`’s one.
        lsuffix : str, default ''
            Suffix to use from left frame's overlapping columns.
        rsuffix : str, default ''
            Suffix to use from `right` frame's overlapping columns.

        Returns
        -------
        DataFrame
            A dataframe containing columns from both the `left` and `right`.

        See Also
        --------
        DataFrame.merge: For column(s)-on-columns(s) operations.
        DataFrame.update : Modify in place using non-NA values from another DataFrame.
        DataFrame.hint : Specifies some hint on the current DataFrame.
        broadcast : Marks a DataFrame as small enough for use in broadcast joins.

        Notes
        -----
        Parameters on, lsuffix, and rsuffix are not supported when passing a list of DataFrame
        objects.

        Examples
        --------
        >>> psdf1 = ps.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
        ...                      'A': ['A0', 'A1', 'A2', 'A3']},
        ...                     columns=['key', 'A'])
        >>> psdf2 = ps.DataFrame({'key': ['K0', 'K1', 'K2'],
        ...                      'B': ['B0', 'B1', 'B2']},
        ...                     columns=['key', 'B'])
        >>> psdf1
          key   A
        0  K0  A0
        1  K1  A1
        2  K2  A2
        3  K3  A3
        >>> psdf2
          key   B
        0  K0  B0
        1  K1  B1
        2  K2  B2

        Join DataFrames using their indexes.

        >>> join_psdf = psdf1.join(psdf2, lsuffix='_left', rsuffix='_right')
        >>> join_psdf.sort_values(by=join_psdf.columns)
          key_left   A key_right     B
        0       K0  A0        K0    B0
        1       K1  A1        K1    B1
        2       K2  A2        K2    B2
        3       K3  A3      None  None

        If we want to join using the key columns, we need to set key to be the index in both df and
        right. The joined DataFrame will have key as its index.

        >>> join_psdf = psdf1.set_index('key').join(psdf2.set_index('key'))
        >>> join_psdf.sort_values(by=join_psdf.columns) # doctest: +NORMALIZE_WHITESPACE
              A     B
        key
        K0   A0    B0
        K1   A1    B1
        K2   A2    B2
        K3   A3  None

        Another option to join using the key columns is to use the on parameter. DataFrame.join
        always uses right’s index but we can use any column in df. This method does not preserve
        the original DataFrame’s index in the result unlike pandas.

        >>> join_psdf = psdf1.join(psdf2.set_index('key'), on='key')
        >>> join_psdf.index
        Int64Index([0, 1, 2, 3], dtype='int64')
        """
    def combine_first(self, other: DataFrame) -> DataFrame:
        '''
        Update null elements with value in the same location in `other`.

        Combine two DataFrame objects by filling null values in one DataFrame
        with non-null values from other DataFrame. The row and column indexes
        of the resulting DataFrame will be the union of the two.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        other : DataFrame
            Provided DataFrame to use to fill null values.

        Returns
        -------
        DataFrame

        Examples
        --------
        >>> ps.set_option("compute.ops_on_diff_frames", True)
        >>> df1 = ps.DataFrame({\'A\': [None, 0], \'B\': [None, 4]})
        >>> df2 = ps.DataFrame({\'A\': [1, 1], \'B\': [3, 3]})

        >>> df1.combine_first(df2).sort_index()
             A    B
        0  1.0  3.0
        1  0.0  4.0

        Null values persist if the location of that null value does not exist in other

        >>> df1 = ps.DataFrame({\'A\': [None, 0], \'B\': [4, None]})
        >>> df2 = ps.DataFrame({\'B\': [3, 3], \'C\': [1, 1]}, index=[1, 2])

        >>> df1.combine_first(df2).sort_index()
             A    B    C
        0  NaN  4.0  NaN
        1  0.0  3.0  1.0
        2  NaN  3.0  1.0
        >>> ps.reset_option("compute.ops_on_diff_frames")
        '''
    def append(self, other: DataFrame, ignore_index: bool = False, verify_integrity: bool = False, sort: bool = False) -> DataFrame:
        """
        Append rows of other to the end of caller, returning a new object.

        Columns in other that are not in the caller are added as new columns.

        .. deprecated:: 3.4.0

        Parameters
        ----------
        other : DataFrame or Series/dict-like object, or list of these
            The data to append.

        ignore_index : boolean, default False
            If True, do not use the index labels.

        verify_integrity : boolean, default False
            If True, raise ValueError on creating index with duplicates.

        sort : boolean, default False
            Currently not supported.

        Returns
        -------
        appended : DataFrame

        Examples
        --------
        >>> df = ps.DataFrame([[1, 2], [3, 4]], columns=list('AB'))

        >>> df.append(df)
           A  B
        0  1  2
        1  3  4
        0  1  2
        1  3  4

        >>> df.append(df, ignore_index=True)
           A  B
        0  1  2
        1  3  4
        2  1  2
        3  3  4
        """
    def update(self, other: DataFrame, join: str = 'left', overwrite: bool = True) -> None:
        """
        Modify in place using non-NA values from another DataFrame.
        Aligns on indices. There is no return value.

        Parameters
        ----------
        other : DataFrame, or Series
        join : 'left', default 'left'
            Only left join is implemented, keeping the index and columns of the original object.
        overwrite : bool, default True
            How to handle non-NA values for overlapping keys:

            * True: overwrite original DataFrame's values with values from `other`.
            * False: only update values that are NA in the original DataFrame.

        Returns
        -------
        None : method directly changes calling object

        See Also
        --------
        DataFrame.merge : For column(s)-on-columns(s) operations.
        DataFrame.join : Join columns of another DataFrame.
        DataFrame.hint : Specifies some hint on the current DataFrame.
        broadcast : Marks a DataFrame as small enough for use in broadcast joins.

        Examples
        --------
        >>> df = ps.DataFrame({'A': [1, 2, 3], 'B': [400, 500, 600]}, columns=['A', 'B'])
        >>> new_df = ps.DataFrame({'B': [4, 5, 6], 'C': [7, 8, 9]}, columns=['B', 'C'])
        >>> df.update(new_df)
        >>> df.sort_index()
           A  B
        0  1  4
        1  2  5
        2  3  6

        The DataFrame's length does not increase because of the update,
        only values at matching index/column labels are updated.

        >>> df = ps.DataFrame({'A': ['a', 'b', 'c'], 'B': ['x', 'y', 'z']}, columns=['A', 'B'])
        >>> new_df = ps.DataFrame({'B': ['d', 'e', 'f', 'g', 'h', 'i']}, columns=['B'])
        >>> df.update(new_df)
        >>> df.sort_index()
           A  B
        0  a  d
        1  b  e
        2  c  f

        For Series, its name attribute must be set.

        >>> df = ps.DataFrame({'A': ['a', 'b', 'c'], 'B': ['x', 'y', 'z']}, columns=['A', 'B'])
        >>> new_column = ps.Series(['d', 'e'], name='B', index=[0, 2])
        >>> df.update(new_column)
        >>> df.sort_index()
           A  B
        0  a  d
        1  b  y
        2  c  e

        If `other` contains None the corresponding values are not updated in the original dataframe.

        >>> df = ps.DataFrame({'A': [1, 2, 3], 'B': [400, 500, 600]}, columns=['A', 'B'])
        >>> new_df = ps.DataFrame({'B': [4, None, 6]}, columns=['B'])
        >>> df.update(new_df)
        >>> df.sort_index()
           A      B
        0  1    4.0
        1  2  500.0
        2  3    6.0
        """
    def cov(self, min_periods: int | None = None, ddof: int = 1) -> DataFrame:
        """
        Compute pairwise covariance of columns, excluding NA/null values.

        Compute the pairwise covariance among the series of a DataFrame.
        The returned data frame is the `covariance matrix
        <https://en.wikipedia.org/wiki/Covariance_matrix>`__ of the columns
        of the DataFrame.

        Both NA and null values are automatically excluded from the
        calculation. (See the note below about bias from missing values.)
        A threshold can be set for the minimum number of
        observations for each value created. Comparisons with observations
        below this threshold will be returned as ``NaN``.

        This method is generally used for the analysis of time series data to
        understand the relationship between different measures across time.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        min_periods : int, optional
            Minimum number of observations required per pair of columns
            to have a valid result.
        ddof : int, default 1
            Delta degrees of freedom. The divisor used in calculations
            is ``N - ddof``, where ``N`` represents the number of elements.

            .. versionadded:: 3.4.0

        Returns
        -------
        DataFrame
            The covariance matrix of the series of the DataFrame.

        See Also
        --------
        Series.cov : Compute covariance with another Series.

        Examples
        --------
        >>> df = ps.DataFrame([(1, 2), (0, 3), (2, 0), (1, 1)],
        ...                   columns=['dogs', 'cats'])
        >>> df.cov()
                  dogs      cats
        dogs  0.666667 -1.000000
        cats -1.000000  1.666667

        >>> np.random.seed(42)
        >>> df = ps.DataFrame(np.random.randn(1000, 5),
        ...                   columns=['a', 'b', 'c', 'd', 'e'])
        >>> df.cov()
                  a         b         c         d         e
        a  0.998438 -0.020161  0.059277 -0.008943  0.014144
        b -0.020161  1.059352 -0.008543 -0.024738  0.009826
        c  0.059277 -0.008543  1.010670 -0.001486 -0.000271
        d -0.008943 -0.024738 -0.001486  0.921297 -0.013692
        e  0.014144  0.009826 -0.000271 -0.013692  0.977795
        >>> df.cov(ddof=2)
                  a         b         c         d         e
        a  0.999439 -0.020181  0.059336 -0.008952  0.014159
        b -0.020181  1.060413 -0.008551 -0.024762  0.009836
        c  0.059336 -0.008551  1.011683 -0.001487 -0.000271
        d -0.008952 -0.024762 -0.001487  0.922220 -0.013705
        e  0.014159  0.009836 -0.000271 -0.013705  0.978775
        >>> df.cov(ddof=-1)
          a         b         c         d         e
        a  0.996444 -0.020121  0.059158 -0.008926  0.014116
        b -0.020121  1.057235 -0.008526 -0.024688  0.009807
        c  0.059158 -0.008526  1.008650 -0.001483 -0.000270
        d -0.008926 -0.024688 -0.001483  0.919456 -0.013664
        e  0.014116  0.009807 -0.000270 -0.013664  0.975842

        **Minimum number of periods**

        This method also supports an optional ``min_periods`` keyword
        that specifies the required minimum number of non-NA observations for
        each column pair to have a valid result:

        >>> np.random.seed(42)
        >>> df = pd.DataFrame(np.random.randn(20, 3),
        ...                   columns=['a', 'b', 'c'])
        >>> df.loc[df.index[:5], 'a'] = np.nan
        >>> df.loc[df.index[5:10], 'b'] = np.nan
        >>> sdf = ps.from_pandas(df)
        >>> sdf.cov(min_periods=12)
                  a         b         c
        a  0.316741       NaN -0.150812
        b       NaN  1.248003  0.191417
        c -0.150812  0.191417  0.895202
        """
    def sample(self, n: int | None = None, frac: float | None = None, replace: bool = False, random_state: int | None = None, ignore_index: bool = False) -> DataFrame:
        """
        Return a random sample of items from an axis of object.

        Please call this function using named argument by specifying the ``frac`` argument.

        You can use `random_state` for reproducibility. However, note that different from pandas,
        specifying a seed in pandas-on-Spark/Spark does not guarantee the sampled rows will
        be fixed. The result set depends on not only the seed, but also how the data is distributed
        across machines and to some extent network randomness when shuffle operations are involved.
        Even in the simplest case, the result set will depend on the system's CPU core count.

        Parameters
        ----------
        n : int, optional
            Number of items to return. This is currently NOT supported. Use frac instead.
        frac : float, optional
            Fraction of axis items to return.
        replace : bool, default False
            Sample with or without replacement.
        random_state : int, optional
            Seed for the random number generator (if int).
        ignore_index : bool, default False
            If True, the resulting index will be labeled 0, 1, …, n - 1.

            .. versionadded:: 3.4.0

        Returns
        -------
        Series or DataFrame
            A new object of same type as caller containing the sampled items.

        Examples
        --------
        >>> df = ps.DataFrame({'num_legs': [2, 4, 8, 0],
        ...                    'num_wings': [2, 0, 0, 0],
        ...                    'num_specimen_seen': [10, 2, 1, 8]},
        ...                   index=['falcon', 'dog', 'spider', 'fish'],
        ...                   columns=['num_legs', 'num_wings', 'num_specimen_seen'])
        >>> df  # doctest: +SKIP
                num_legs  num_wings  num_specimen_seen
        falcon         2          2                 10
        dog            4          0                  2
        spider         8          0                  1
        fish           0          0                  8

        A random 25% sample of the ``DataFrame``.
        Note that we use `random_state` to ensure the reproducibility of
        the examples.

        >>> df.sample(frac=0.25, random_state=1)  # doctest: +SKIP
                num_legs  num_wings  num_specimen_seen
        falcon         2          2                 10
        fish           0          0                  8

        A random 50% sample of the ``DataFrame``, while ignoring the index.

        >>> df.sample(frac=0.5, random_state=1, ignore_index=True)  # doctest: +SKIP
           num_legs  num_wings  num_specimen_seen
        0         4          0                  2
        1         8          0                  1
        2         0          0                  8

        Extract 25% random elements from the ``Series`` ``df['num_legs']`` with replacement
        so, the same items could appear more than once.

        >>> df['num_legs'].sample(frac=0.4, replace=True, random_state=1)  # doctest: +SKIP
        falcon    2
        spider    8
        spider    8
        Name: num_legs, dtype: int64

        Specifying the exact number of items to return is not supported now.

        >>> df.sample(n=5)  # doctest: +ELLIPSIS
        Traceback (most recent call last):
            ...
        NotImplementedError: Function sample currently does not support specifying ...
        """
    def astype(self, dtype: str | Dtype | Dict[Name, str | Dtype]) -> DataFrame:
        """
        Cast a pandas-on-Spark object to a specified dtype ``dtype``.

        Parameters
        ----------
        dtype : data type, or dict of column name -> data type
            Use a numpy.dtype or Python type to cast entire pandas-on-Spark object to
            the same type. Alternatively, use {col: dtype, ...}, where col is a
            column label and dtype is a numpy.dtype or Python type to cast one
            or more of the DataFrame's columns to column-specific types.

        Returns
        -------
        casted : same type as caller

        See Also
        --------
        to_datetime : Convert argument to datetime.

        Examples
        --------
        >>> df = ps.DataFrame({'a': [1, 2, 3], 'b': [1, 2, 3]}, dtype='int64')
        >>> df
           a  b
        0  1  1
        1  2  2
        2  3  3

        Convert to float type:

        >>> df.astype('float')
             a    b
        0  1.0  1.0
        1  2.0  2.0
        2  3.0  3.0

        Convert to int64 type back:

        >>> df.astype('int64')
           a  b
        0  1  1
        1  2  2
        2  3  3

        Convert column a to float type:

        >>> df.astype({'a': float})
             a  b
        0  1.0  1
        1  2.0  2
        2  3.0  3

        """
    def add_prefix(self, prefix: str) -> DataFrame:
        """
        Prefix labels with string `prefix`.

        For Series, the row labels are prefixed.
        For DataFrame, the column labels are prefixed.

        Parameters
        ----------
        prefix : str
           The string to add before each label.

        Returns
        -------
        DataFrame
           New DataFrame with updated labels.

        See Also
        --------
        Series.add_prefix: Prefix row labels with string `prefix`.
        Series.add_suffix: Suffix row labels with string `suffix`.
        DataFrame.add_suffix: Suffix column labels with string `suffix`.

        Examples
        --------
        >>> df = ps.DataFrame({'A': [1, 2, 3, 4], 'B': [3, 4, 5, 6]}, columns=['A', 'B'])
        >>> df
           A  B
        0  1  3
        1  2  4
        2  3  5
        3  4  6

        >>> df.add_prefix('col_')
           col_A  col_B
        0      1      3
        1      2      4
        2      3      5
        3      4      6
        """
    def add_suffix(self, suffix: str) -> DataFrame:
        """
        Suffix labels with string `suffix`.

        For Series, the row labels are suffixed.
        For DataFrame, the column labels are suffixed.

        Parameters
        ----------
        suffix : str
           The string to add before each label.

        Returns
        -------
        DataFrame
           New DataFrame with updated labels.

        See Also
        --------
        Series.add_prefix: Prefix row labels with string `prefix`.
        Series.add_suffix: Suffix row labels with string `suffix`.
        DataFrame.add_prefix: Prefix column labels with string `prefix`.

        Examples
        --------
        >>> df = ps.DataFrame({'A': [1, 2, 3, 4], 'B': [3, 4, 5, 6]}, columns=['A', 'B'])
        >>> df
           A  B
        0  1  3
        1  2  4
        2  3  5
        3  4  6

        >>> df.add_suffix('_col')
           A_col  B_col
        0      1      3
        1      2      4
        2      3      5
        3      4      6
        """
    def describe(self, percentiles: List[float] | None = None) -> DataFrame:
        """
        Generate descriptive statistics that summarize the central tendency,
        dispersion and shape of a dataset's distribution, excluding
        ``NaN`` values.

        Analyzes both numeric and object series, as well
        as ``DataFrame`` column sets of mixed data types. The output
        will vary depending on what is provided. Refer to the notes
        below for more detail.

        Parameters
        ----------
        percentiles : list of ``float`` in range [0.0, 1.0], default [0.25, 0.5, 0.75]
            A list of percentiles to be computed.

        Returns
        -------
        DataFrame
            Summary statistics of the Dataframe provided.

        See Also
        --------
        DataFrame.count: Count number of non-NA/null observations.
        DataFrame.max: Maximum of the values in the object.
        DataFrame.min: Minimum of the values in the object.
        DataFrame.mean: Mean of the values.
        DataFrame.std: Standard deviation of the observations.

        Notes
        -----
        For numeric data, the result's index will include ``count``,
        ``mean``, ``std``, ``min``, ``25%``, ``50%``, ``75%``, ``max``.

        For object data (e.g. strings or timestamps), the result’s index will include
        ``count``, ``unique``, ``top``, and ``freq``.
        The ``top`` is the most common value. The ``freq`` is the most common value’s frequency.
        Timestamps also include the ``first`` and ``last`` items.

        Examples
        --------
        Describing a numeric ``Series``.

        >>> s = ps.Series([1, 2, 3])
        >>> s.describe()
        count    3.0
        mean     2.0
        std      1.0
        min      1.0
        25%      1.0
        50%      2.0
        75%      3.0
        max      3.0
        dtype: float64

        Describing a ``DataFrame``. Only numeric fields are returned.

        >>> df = ps.DataFrame({'numeric1': [1, 2, 3],
        ...                    'numeric2': [4.0, 5.0, 6.0],
        ...                    'object': ['a', 'b', 'c']
        ...                   },
        ...                   columns=['numeric1', 'numeric2', 'object'])
        >>> df.describe()
               numeric1  numeric2
        count       3.0       3.0
        mean        2.0       5.0
        std         1.0       1.0
        min         1.0       4.0
        25%         1.0       4.0
        50%         2.0       5.0
        75%         3.0       6.0
        max         3.0       6.0

        For multi-index columns:

        >>> df.columns = [('num', 'a'), ('num', 'b'), ('obj', 'c')]
        >>> df.describe()  # doctest: +NORMALIZE_WHITESPACE
               num
                 a    b
        count  3.0  3.0
        mean   2.0  5.0
        std    1.0  1.0
        min    1.0  4.0
        25%    1.0  4.0
        50%    2.0  5.0
        75%    3.0  6.0
        max    3.0  6.0

        >>> df[('num', 'b')].describe()
        count    3.0
        mean     5.0
        std      1.0
        min      4.0
        25%      4.0
        50%      5.0
        75%      6.0
        max      6.0
        Name: (num, b), dtype: float64

        Describing a ``DataFrame`` and selecting custom percentiles.

        >>> df = ps.DataFrame({'numeric1': [1, 2, 3],
        ...                    'numeric2': [4.0, 5.0, 6.0]
        ...                   },
        ...                   columns=['numeric1', 'numeric2'])
        >>> df.describe(percentiles = [0.85, 0.15])
               numeric1  numeric2
        count       3.0       3.0
        mean        2.0       5.0
        std         1.0       1.0
        min         1.0       4.0
        15%         1.0       4.0
        50%         2.0       5.0
        85%         3.0       6.0
        max         3.0       6.0

        Describing a column from a ``DataFrame`` by accessing it as
        an attribute.

        >>> df.numeric1.describe()
        count    3.0
        mean     2.0
        std      1.0
        min      1.0
        25%      1.0
        50%      2.0
        75%      3.0
        max      3.0
        Name: numeric1, dtype: float64

        Describing a column from a ``DataFrame`` by accessing it as
        an attribute and selecting custom percentiles.

        >>> df.numeric1.describe(percentiles = [0.85, 0.15])
        count    3.0
        mean     2.0
        std      1.0
        min      1.0
        15%      1.0
        50%      2.0
        85%      3.0
        max      3.0
        Name: numeric1, dtype: float64
        """
    def drop_duplicates(self, subset: Name | List[Name] | None = None, keep: bool | str = 'first', inplace: bool = False, ignore_index: bool = False) -> DataFrame | None:
        """
        Return DataFrame with duplicate rows removed, optionally only
        considering certain columns.

        Parameters
        ----------
        subset : column label or sequence of labels, optional
            Only consider certain columns for identifying duplicates, by
            default use all the columns.
        keep : {'first', 'last', False}, default 'first'
            Determines which duplicates (if any) to keep.
            - ``first`` : Drop duplicates except for the first occurrence.
            - ``last`` : Drop duplicates except for the last occurrence.
            - False : Drop all duplicates.
        inplace : boolean, default False
            Whether to drop duplicates in place or to return a copy.
        ignore_index : boolean, default False
            If True, the resulting axis will be labeled 0, 1, …, n - 1.

        Returns
        -------
        DataFrame
            DataFrame with duplicates removed or None if ``inplace=True``.

        >>> df = ps.DataFrame(
        ...     {'a': [1, 2, 2, 2, 3], 'b': ['a', 'a', 'a', 'c', 'd']}, columns = ['a', 'b'])
        >>> df
           a  b
        0  1  a
        1  2  a
        2  2  a
        3  2  c
        4  3  d

        >>> df.drop_duplicates().sort_index()
           a  b
        0  1  a
        1  2  a
        3  2  c
        4  3  d

        >>> df.drop_duplicates(ignore_index=True).sort_index()
           a  b
        0  1  a
        1  2  a
        2  2  c
        3  3  d

        >>> df.drop_duplicates('a').sort_index()
           a  b
        0  1  a
        1  2  a
        4  3  d

        >>> df.drop_duplicates(['a', 'b']).sort_index()
           a  b
        0  1  a
        1  2  a
        3  2  c
        4  3  d

        >>> df.drop_duplicates(keep='last').sort_index()
           a  b
        0  1  a
        2  2  a
        3  2  c
        4  3  d

        >>> df.drop_duplicates(keep=False).sort_index()
           a  b
        0  1  a
        3  2  c
        4  3  d
        """
    def reindex(self, labels: Sequence[Any] | None = None, index: Index | Sequence[Any] | None = None, columns: pd.Index | Sequence[Any] | None = None, axis: Axis | None = None, copy: bool | None = True, fill_value: Any | None = None) -> DataFrame:
        '''
        Conform DataFrame to new index with optional filling logic, placing
        NA/NaN in locations having no value in the previous index. A new object
        is produced unless the new index is equivalent to the current one and
        ``copy=False``.

        Parameters
        ----------
        labels: array-like, optional
            New labels / index to conform the axis specified by ‘axis’ to.
        index, columns: array-like, optional
            New labels / index to conform to, should be specified using keywords.
            Preferably an Index object to avoid duplicating data
        axis: int or str, optional
            Axis to target. Can be either the axis name (‘index’, ‘columns’) or
            number (0, 1).
        copy : bool, default True
            Return a new object, even if the passed indexes are the same.
        fill_value : scalar, default np.NaN
            Value to use for missing values. Defaults to NaN, but can be any
            "compatible" value.

        Returns
        -------
        DataFrame with changed index.

        See Also
        --------
        DataFrame.set_index : Set row labels.
        DataFrame.reset_index : Remove row labels or move them to new columns.

        Examples
        --------

        ``DataFrame.reindex`` supports two calling conventions

        * ``(index=index_labels, columns=column_labels, ...)``
        * ``(labels, axis={\'index\', \'columns\'}, ...)``

        We *highly* recommend using keyword arguments to clarify your
        intent.

        Create a dataframe with some fictional data.

        >>> index = [\'Firefox\', \'Chrome\', \'Safari\', \'IE10\', \'Konqueror\']
        >>> df = ps.DataFrame({
        ...      \'http_status\': [200, 200, 404, 404, 301],
        ...      \'response_time\': [0.04, 0.02, 0.07, 0.08, 1.0]},
        ...       index=index,
        ...       columns=[\'http_status\', \'response_time\'])
        >>> df
                   http_status  response_time
        Firefox            200           0.04
        Chrome             200           0.02
        Safari             404           0.07
        IE10               404           0.08
        Konqueror          301           1.00

        Create a new index and reindex the dataframe. By default
        values in the new index that do not have corresponding
        records in the dataframe are assigned ``NaN``.

        >>> new_index= [\'Safari\', \'Iceweasel\', \'Comodo Dragon\', \'IE10\',
        ...             \'Chrome\']
        >>> df.reindex(new_index).sort_index()
                       http_status  response_time
        Chrome               200.0           0.02
        Comodo Dragon          NaN            NaN
        IE10                 404.0           0.08
        Iceweasel              NaN            NaN
        Safari               404.0           0.07

        We can fill in the missing values by passing a value to
        the keyword ``fill_value``.

        >>> df.reindex(new_index, fill_value=0, copy=False).sort_index()
                       http_status  response_time
        Chrome                 200           0.02
        Comodo Dragon            0           0.00
        IE10                   404           0.08
        Iceweasel                0           0.00
        Safari                 404           0.07

        We can also reindex the columns.

        >>> df.reindex(columns=[\'http_status\', \'user_agent\']).sort_index()
                   http_status  user_agent
        Chrome             200         NaN
        Firefox            200         NaN
        IE10               404         NaN
        Konqueror          301         NaN
        Safari             404         NaN

        Or we can use "axis-style" keyword arguments

        >>> df.reindex([\'http_status\', \'user_agent\'], axis="columns").sort_index()
                   http_status  user_agent
        Chrome             200         NaN
        Firefox            200         NaN
        IE10               404         NaN
        Konqueror          301         NaN
        Safari             404         NaN

        To further illustrate the filling functionality in
        ``reindex``, we will create a dataframe with a
        monotonically increasing index (for example, a sequence
        of dates).

        >>> date_index = pd.date_range(\'1/1/2010\', periods=6, freq=\'D\')
        >>> df2 = ps.DataFrame({"prices": [100, 101, np.nan, 100, 89, 88]},
        ...                    index=date_index)
        >>> df2.sort_index()
                    prices
        2010-01-01   100.0
        2010-01-02   101.0
        2010-01-03     NaN
        2010-01-04   100.0
        2010-01-05    89.0
        2010-01-06    88.0

        Suppose we decide to expand the dataframe to cover a wider
        date range.

        >>> date_index2 = pd.date_range(\'12/29/2009\', periods=10, freq=\'D\')
        >>> df2.reindex(date_index2).sort_index()
                    prices
        2009-12-29     NaN
        2009-12-30     NaN
        2009-12-31     NaN
        2010-01-01   100.0
        2010-01-02   101.0
        2010-01-03     NaN
        2010-01-04   100.0
        2010-01-05    89.0
        2010-01-06    88.0
        2010-01-07     NaN
        '''
    def reindex_like(self, other: DataFrame, copy: bool = True) -> DataFrame:
        """
        Return a DataFrame with matching indices as other object.

        Conform the object to the same index on all axes. Places NA/NaN in locations
        having no value in the previous index. A new object is produced unless the
        new index is equivalent to the current one and copy=False.

        Parameters
        ----------
        other : DataFrame
            Its row and column indices are used to define the new indices
            of this object.
        copy : bool, default True
            Return a new object, even if the passed indexes are the same.

        Returns
        -------
        DataFrame
            DataFrame with changed indices on each axis.

        See Also
        --------
        DataFrame.set_index : Set row labels.
        DataFrame.reset_index : Remove row labels or move them to new columns.
        DataFrame.reindex : Change to new indices or expand indices.

        Notes
        -----
        Same as calling
        ``.reindex(index=other.index, columns=other.columns,...)``.

        Examples
        --------

        >>> df1 = ps.DataFrame([[24.3, 75.7, 'high'],
        ...                     [31, 87.8, 'high'],
        ...                     [22, 71.6, 'medium'],
        ...                     [35, 95, 'medium']],
        ...                    columns=['temp_celsius', 'temp_fahrenheit',
        ...                             'windspeed'],
        ...                    index=pd.date_range(start='2014-02-12',
        ...                                        end='2014-02-15', freq='D'))
        >>> df1
                    temp_celsius  temp_fahrenheit windspeed
        2014-02-12          24.3             75.7      high
        2014-02-13          31.0             87.8      high
        2014-02-14          22.0             71.6    medium
        2014-02-15          35.0             95.0    medium

        >>> df2 = ps.DataFrame([[28, 'low'],
        ...                     [30, 'low'],
        ...                     [35.1, 'medium']],
        ...                    columns=['temp_celsius', 'windspeed'],
        ...                    index=pd.DatetimeIndex(['2014-02-12', '2014-02-13',
        ...                                            '2014-02-15']))
        >>> df2
                    temp_celsius windspeed
        2014-02-12          28.0       low
        2014-02-13          30.0       low
        2014-02-15          35.1    medium

        >>> df2.reindex_like(df1).sort_index() # doctest: +NORMALIZE_WHITESPACE
                    temp_celsius  temp_fahrenheit windspeed
        2014-02-12          28.0              NaN       low
        2014-02-13          30.0              NaN       low
        2014-02-14           NaN              NaN       None
        2014-02-15          35.1              NaN    medium
        """
    def melt(self, id_vars: Name | List[Name] | None = None, value_vars: Name | List[Name] | None = None, var_name: str | List[str] | None = None, value_name: str = 'value') -> DataFrame:
        '''
        Unpivot a DataFrame from wide format to long format, optionally
        leaving identifier variables set.

        This function is useful to massage a DataFrame into a format where one
        or more columns are identifier variables (`id_vars`), while all other
        columns, considered measured variables (`value_vars`), are "unpivoted" to
        the row axis, leaving just two non-identifier columns, \'variable\' and
        \'value\'.

        Parameters
        ----------
        frame : DataFrame
        id_vars : tuple, list, or ndarray, optional
            Column(s) to use as identifier variables.
        value_vars : tuple, list, or ndarray, optional
            Column(s) to unpivot. If not specified, uses all columns that
            are not set as `id_vars`.
        var_name : scalar, default \'variable\'
            Name to use for the \'variable\' column. If None it uses `frame.columns.name` or
            ‘variable’.
        value_name : scalar, default \'value\'
            Name to use for the \'value\' column.

        Returns
        -------
        DataFrame
            Unpivoted DataFrame.

        Examples
        --------
        >>> df = ps.DataFrame({\'A\': {0: \'a\', 1: \'b\', 2: \'c\'},
        ...                    \'B\': {0: 1, 1: 3, 2: 5},
        ...                    \'C\': {0: 2, 1: 4, 2: 6}},
        ...                   columns=[\'A\', \'B\', \'C\'])
        >>> df
           A  B  C
        0  a  1  2
        1  b  3  4
        2  c  5  6

        >>> ps.melt(df)
          variable value
        0        A     a
        1        B     1
        2        C     2
        3        A     b
        4        B     3
        5        C     4
        6        A     c
        7        B     5
        8        C     6

        >>> df.melt(id_vars=\'A\')
           A variable  value
        0  a        B      1
        1  a        C      2
        2  b        B      3
        3  b        C      4
        4  c        B      5
        5  c        C      6

        >>> df.melt(value_vars=\'A\')
          variable value
        0        A     a
        1        A     b
        2        A     c

        >>> ps.melt(df, id_vars=[\'A\', \'B\'])
           A  B variable  value
        0  a  1        C      2
        1  b  3        C      4
        2  c  5        C      6

        >>> df.melt(id_vars=[\'A\'], value_vars=[\'C\'])
           A variable  value
        0  a        C      2
        1  b        C      4
        2  c        C      6

        The names of \'variable\' and \'value\' columns can be customized:

        >>> ps.melt(df, id_vars=[\'A\'], value_vars=[\'B\'],
        ...         var_name=\'myVarname\', value_name=\'myValname\')
           A myVarname  myValname
        0  a         B          1
        1  b         B          3
        2  c         B          5
        '''
    def stack(self) -> DataFrameOrSeries:
        """
        Stack the prescribed level(s) from columns to index.

        Return a reshaped DataFrame or Series having a multi-level
        index with one or more new inner-most levels compared to the current
        DataFrame. The new inner-most levels are created by pivoting the
        columns of the current dataframe:

          - if the columns have a single level, the output is a Series
          - if the columns have multiple levels, the new index
            level(s) is (are) taken from the prescribed level(s) and
            the output is a DataFrame.

        The new index levels are sorted.

        Returns
        -------
        DataFrame or Series
            Stacked dataframe or series.

        See Also
        --------
        DataFrame.unstack : Unstack prescribed level(s) from index axis
            onto column axis.
        DataFrame.pivot : Reshape dataframe from long format to wide
            format.
        DataFrame.pivot_table : Create a spreadsheet-style pivot table
            as a DataFrame.

        Notes
        -----
        The function is named by analogy with a collection of books
        being reorganized from being side by side on a horizontal
        position (the columns of the dataframe) to being stacked
        vertically on top of each other (in the index of the
        dataframe).

        Examples
        --------
        **Single level columns**

        >>> df_single_level_cols = ps.DataFrame([[0, 1], [2, 3]],
        ...                                     index=['cat', 'dog'],
        ...                                     columns=['weight', 'height'])

        Stacking a dataframe with a single level column axis returns a Series:

        >>> df_single_level_cols
             weight  height
        cat       0       1
        dog       2       3
        >>> df_single_level_cols.stack().sort_index()
        cat  height    1
             weight    0
        dog  height    3
             weight    2
        dtype: int64

        **Multi level columns: simple case**

        >>> multicol1 = pd.MultiIndex.from_tuples([('weight', 'kg'),
        ...                                        ('weight', 'pounds')])
        >>> df_multi_level_cols1 = ps.DataFrame([[1, 2], [2, 4]],
        ...                                     index=['cat', 'dog'],
        ...                                     columns=multicol1)

        Stacking a dataframe with a multi-level column axis:

        >>> df_multi_level_cols1  # doctest: +NORMALIZE_WHITESPACE
            weight
                kg pounds
        cat      1      2
        dog      2      4
        >>> df_multi_level_cols1.stack().sort_index()
                    weight
        cat kg           1
            pounds       2
        dog kg           2
            pounds       4

        **Missing values**

        >>> multicol2 = pd.MultiIndex.from_tuples([('weight', 'kg'),
        ...                                        ('height', 'm')])
        >>> df_multi_level_cols2 = ps.DataFrame([[1.0, 2.0], [3.0, 4.0]],
        ...                                     index=['cat', 'dog'],
        ...                                     columns=multicol2)

        It is common to have missing values when stacking a dataframe
        with multi-level columns, as the stacked dataframe typically
        has more values than the original dataframe. Missing values
        are filled with NaNs:

        >>> df_multi_level_cols2
            weight height
                kg      m
        cat    1.0    2.0
        dog    3.0    4.0
        >>> df_multi_level_cols2.stack().sort_index()  # doctest: +SKIP
                height  weight
        cat kg     NaN     1.0
            m      2.0     NaN
        dog kg     NaN     3.0
            m      4.0     NaN
        """
    def unstack(self) -> DataFrameOrSeries:
        '''
        Pivot the (necessarily hierarchical) index labels.

        Returns a DataFrame having a new level of column labels whose inner-most level
        consists of the pivoted index labels.

        If the index is not a MultiIndex, the output will be a Series.

        .. note:: If the index is a MultiIndex, the output DataFrame could be very wide, and
            it could cause a serious performance degradation since Spark partitions its row based.

        Returns
        -------
        Series or DataFrame

        See Also
        --------
        DataFrame.pivot : Pivot a table based on column values.
        DataFrame.stack : Pivot a level of the column labels (inverse operation from unstack).

        Examples
        --------
        >>> df = ps.DataFrame({"A": {"0": "a", "1": "b", "2": "c"},
        ...                    "B": {"0": "1", "1": "3", "2": "5"},
        ...                    "C": {"0": "2", "1": "4", "2": "6"}},
        ...                   columns=["A", "B", "C"])
        >>> df
           A  B  C
        0  a  1  2
        1  b  3  4
        2  c  5  6

        >>> df.unstack().sort_index()
        A  0    a
           1    b
           2    c
        B  0    1
           1    3
           2    5
        C  0    2
           1    4
           2    6
        dtype: object

        >>> df.columns = pd.MultiIndex.from_tuples([(\'X\', \'A\'), (\'X\', \'B\'), (\'Y\', \'C\')])
        >>> df.unstack().sort_index()
        X  A  0    a
              1    b
              2    c
           B  0    1
              1    3
              2    5
        Y  C  0    2
              1    4
              2    6
        dtype: object

        For MultiIndex case:

        >>> df = ps.DataFrame({"A": ["a", "b", "c"],
        ...                    "B": [1, 3, 5],
        ...                    "C": [2, 4, 6]},
        ...                   columns=["A", "B", "C"])
        >>> df = df.set_index(\'A\', append=True)
        >>> df  # doctest: +NORMALIZE_WHITESPACE
             B  C
          A
        0 a  1  2
        1 b  3  4
        2 c  5  6
        >>> df.unstack().sort_index()  # doctest: +NORMALIZE_WHITESPACE
             B              C
        A    a    b    c    a    b    c
        0  1.0  NaN  NaN  2.0  NaN  NaN
        1  NaN  3.0  NaN  NaN  4.0  NaN
        2  NaN  NaN  5.0  NaN  NaN  6.0
        '''
    def all(self, axis: Axis = 0, bool_only: bool | None = None, skipna: bool = True) -> Series:
        """
        Return whether all elements are True.

        Returns True unless there is at least one element within a series that is
        False or equivalent (e.g. zero or empty)

        Parameters
        ----------
        axis : {0 or 'index'}, default 0
            Indicate which axis or axes should be reduced.

            * 0 / 'index' : reduce the index, return a Series whose index is the
              original column labels.

        bool_only : bool, default None
            Include only boolean columns. If None, will attempt to use everything,
            then use only boolean data.

        skipna : boolean, default True
            Exclude NA values, such as None or numpy.NaN.
            If an entire row/column is NA values and `skipna` is True,
            then the result will be True, as for an empty row/column.
            If `skipna` is False, numpy.NaNs are treated as True because these are
            not equal to zero, Nones are treated as False.

        Returns
        -------
        Series

        Examples
        --------
        Create a dataframe from a dictionary.

        >>> df = ps.DataFrame({
        ...    'col1': [True, True, True],
        ...    'col2': [True, False, False],
        ...    'col3': [0, 0, 0],
        ...    'col4': [1, 2, 3],
        ...    'col5': [True, True, None],
        ...    'col6': [True, False, None]},
        ...    columns=['col1', 'col2', 'col3', 'col4', 'col5', 'col6'])

        Default behavior checks if column-wise values all return True.

        >>> df.all()
        col1     True
        col2    False
        col3    False
        col4     True
        col5     True
        col6    False
        dtype: bool

        Include NA values when set `skipna=False`.

        >>> df[['col5', 'col6']].all(skipna=False)
        col5    False
        col6    False
        dtype: bool

        Include only boolean columns when set `bool_only=True`.

        >>> df.all(bool_only=True)
        col1     True
        col2    False
        dtype: bool
        """
    def any(self, axis: Axis = 0, bool_only: bool | None = None) -> Series:
        """
        Return whether any element is True.

        Returns False unless there is at least one element within a series that is
        True or equivalent (e.g. non-zero or non-empty).

        Parameters
        ----------
        axis : {0 or 'index'}, default 0
            Indicate which axis or axes should be reduced.

            * 0 / 'index' : reduce the index, return a Series whose index is the
              original column labels.

        bool_only : bool, default None
            Include only boolean columns. If None, will attempt to use everything,
            then use only boolean data.

        Returns
        -------
        Series

        Examples
        --------
        Create a dataframe from a dictionary.

        >>> df = ps.DataFrame({
        ...    'col1': [False, False, False],
        ...    'col2': [True, False, False],
        ...    'col3': [0, 0, 1],
        ...    'col4': [0, 1, 2],
        ...    'col5': [False, False, None],
        ...    'col6': [True, False, None]},
        ...    columns=['col1', 'col2', 'col3', 'col4', 'col5', 'col6'])

        Default behavior checks if column-wise values all return True.

        >>> df.any()
        col1    False
        col2     True
        col3     True
        col4     True
        col5    False
        col6     True
        dtype: bool

        Include only boolean columns when set `bool_only=True`.

        >>> df.any(bool_only=True)
        col1    False
        col2     True
        dtype: bool

        Returns empty Series when the DataFrame is empty.
        >>> df[[]].any()
        Series([], dtype: bool)
        """
    def rank(self, method: str = 'average', ascending: bool = True, numeric_only: bool | None = None) -> DataFrame:
        """
        Compute numerical data ranks (1 through n) along axis. Equal values are
        assigned a rank that is the average of the ranks of those values.

        .. note:: the current implementation of rank uses Spark's Window without
            specifying partition specification. This leads to moving all data into
            a single partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

        Parameters
        ----------
        method : {'average', 'min', 'max', 'first', 'dense'}
            * average: average rank of group
            * min: lowest rank in group
            * max: highest rank in group
            * first: ranks assigned in order they appear in the array
            * dense: like 'min', but rank always increases by 1 between groups
        ascending : boolean, default True
            False for ranks by high (1) to low (N)
        numeric_only : bool, optional
            For DataFrame objects, rank only numeric columns if set to True.

        Returns
        -------
        ranks : same type as caller

        Examples
        --------
        >>> df = ps.DataFrame({'A': [1, 2, 2, 3], 'B': [4, 3, 2, 1]}, columns=['A', 'B'])
        >>> df
           A  B
        0  1  4
        1  2  3
        2  2  2
        3  3  1

        >>> df.rank().sort_index()
             A    B
        0  1.0  4.0
        1  2.5  3.0
        2  2.5  2.0
        3  4.0  1.0

        If method is set to 'min', it uses lowest rank in group.

        >>> df.rank(method='min').sort_index()
             A    B
        0  1.0  4.0
        1  2.0  3.0
        2  2.0  2.0
        3  4.0  1.0

        If method is set to 'max', it uses highest rank in group.

        >>> df.rank(method='max').sort_index()
             A    B
        0  1.0  4.0
        1  3.0  3.0
        2  3.0  2.0
        3  4.0  1.0

        If method is set to 'dense', it leaves no gaps in group.

        >>> df.rank(method='dense').sort_index()
             A    B
        0  1.0  4.0
        1  2.0  3.0
        2  2.0  2.0
        3  3.0  1.0

        If numeric_only is set to 'True', rank only numeric columns.

        >>> df = ps.DataFrame({'A': [1, 2, 2, 3], 'B': ['a', 'b', 'd', 'c']}, columns= ['A', 'B'])
        >>> df
           A  B
        0  1  a
        1  2  b
        2  2  d
        3  3  c
        >>> df.rank(numeric_only=True)
             A
        0  1.0
        1  2.5
        2  2.5
        3  4.0
        """
    def filter(self, items: Sequence[Any] | None = None, like: str | None = None, regex: str | None = None, axis: Axis | None = None) -> DataFrame:
        '''
        Subset rows or columns of dataframe according to labels in
        the specified index.

        Note that this routine does not filter a dataframe on its
        contents. The filter is applied to the labels of the index.

        Parameters
        ----------
        items : list-like
            Keep labels from axis which are in items.
        like : string
            Keep labels from axis for which "like in label == True".
        regex : string (regular expression)
            Keep labels from axis for which re.search(regex, label) == True.
        axis : int or string axis name
            The axis to filter on. By default this is the info axis,
            \'index\' for Series, \'columns\' for DataFrame.

        Returns
        -------
        same type as input object

        See Also
        --------
        DataFrame.loc

        Notes
        -----
        The ``items``, ``like``, and ``regex`` parameters are
        enforced to be mutually exclusive.

        ``axis`` defaults to the info axis that is used when indexing
        with ``[]``.

        Examples
        --------
        >>> df = ps.DataFrame(np.array(([1, 2, 3], [4, 5, 6])),
        ...                   index=[\'mouse\', \'rabbit\'],
        ...                   columns=[\'one\', \'two\', \'three\'])

        >>> # select columns by name
        >>> df.filter(items=[\'one\', \'three\'])
                one  three
        mouse     1      3
        rabbit    4      6

        >>> # select columns by regular expression
        >>> df.filter(regex=\'e$\', axis=1)
                one  three
        mouse     1      3
        rabbit    4      6

        >>> # select rows containing \'bbi\'
        >>> df.filter(like=\'bbi\', axis=0)
                one  two  three
        rabbit    4    5      6

        For a Series,

        >>> # select rows by name
        >>> df.one.filter(items=[\'rabbit\'])
        rabbit    4
        Name: one, dtype: int64

        >>> # select rows by regular expression
        >>> df.one.filter(regex=\'e$\')
        mouse    1
        Name: one, dtype: int64

        >>> # select rows containing \'bbi\'
        >>> df.one.filter(like=\'bbi\')
        rabbit    4
        Name: one, dtype: int64
        '''
    def rename(self, mapper: Dict | Callable[[Any], Any] | None = None, index: Dict | Callable[[Any], Any] | None = None, columns: Dict | Callable[[Any], Any] | None = None, axis: Axis = 'index', inplace: bool = False, level: int | None = None, errors: str = 'ignore') -> DataFrame | None:
        '''
        Alter axes labels.
        Function / dict values must be unique (1-to-1). Labels not contained in a dict / Series
        will be left as-is. Extra labels listed don’t throw an error.

        Parameters
        ----------
        mapper : dict-like or function
            Dict-like or functions transformations to apply to that axis’ values.
            Use either `mapper` and `axis` to specify the axis to target with `mapper`, or `index`
            and `columns`.
        index : dict-like or function
            Alternative to specifying axis ("mapper, axis=0" is equivalent to "index=mapper").
        columns : dict-like or function
            Alternative to specifying axis ("mapper, axis=1" is equivalent to "columns=mapper").
        axis : int or str, default \'index\'
            Axis to target with mapper. Can be either the axis name (\'index\', \'columns\') or
            number (0, 1).
        inplace : bool, default False
            Whether to return a new DataFrame.
        level : int or level name, default None
            In case of a MultiIndex, only rename labels in the specified level.
        errors : {\'ignore\', \'raise\'}, default \'ignore\'
            If \'raise\', raise a `KeyError` when a dict-like `mapper`, `index`, or `columns`
            contains labels that are not present in the Index being transformed. If \'ignore\',
            existing keys will be renamed, and extra keys will be ignored.

        Returns
        -------
        DataFrame with the renamed axis labels.

        Raises
        ------
        `KeyError`
            If any of the labels is not found in the selected axis and "errors=\'raise\'".

        Examples
        --------
        >>> psdf1 = ps.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        >>> psdf1.rename(columns={"A": "a", "B": "c"})  # doctest: +NORMALIZE_WHITESPACE
           a  c
        0  1  4
        1  2  5
        2  3  6

        >>> psdf1.rename(index={1: 10, 2: 20})  # doctest: +NORMALIZE_WHITESPACE
            A  B
        0   1  4
        10  2  5
        20  3  6

        >>> psdf1.rename(columns={"A": "a", "C": "c"}, errors="raise")
        Traceback (most recent call last):
            ...
        KeyError: \'Index include value which is not in the `mapper`\'

        >>> def str_lower(s) -> str:
        ...     return str.lower(s)
        >>> psdf1.rename(str_lower, axis=\'columns\')  # doctest: +NORMALIZE_WHITESPACE
           a  b
        0  1  4
        1  2  5
        2  3  6

        >>> def mul10(x) -> int:
        ...     return x * 10
        >>> psdf1.rename(mul10, axis=\'index\')  # doctest: +NORMALIZE_WHITESPACE
            A  B
        0   1  4
        10  2  5
        20  3  6

        >>> idx = pd.MultiIndex.from_tuples([(\'X\', \'A\'), (\'X\', \'B\'), (\'Y\', \'C\'), (\'Y\', \'D\')])
        >>> psdf2 = ps.DataFrame([[1, 2, 3, 4], [5, 6, 7, 8]], columns=idx)
        >>> psdf2.rename(columns=str_lower, level=0)  # doctest: +NORMALIZE_WHITESPACE
           x     y
           A  B  C  D
        0  1  2  3  4
        1  5  6  7  8

        >>> psdf3 = ps.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8]], index=idx, columns=list(\'ab\'))
        >>> psdf3.rename(index=str_lower)  # doctest: +NORMALIZE_WHITESPACE
             a  b
        x a  1  2
          b  3  4
        y c  5  6
          d  7  8
        '''
    def rename_axis(self, mapper: Any | Sequence[Any] | Dict[Name, Any] | Callable[[Name], Any] = None, index: Any | Sequence[Any] | Dict[Name, Any] | Callable[[Name], Any] = None, columns: Any | Sequence[Any] | Dict[Name, Any] | Callable[[Name], Any] = None, axis: Axis | None = 0, inplace: bool | None = False) -> DataFrame | None:
        '''
        Set the name of the axis for the index or columns.

        Parameters
        ----------
        mapper : scalar, list-like, optional
            A scalar, list-like, dict-like or functions transformations to
            apply to the axis name attribute.
        index, columns : scalar, list-like, dict-like or function, optional
            A scalar, list-like, dict-like or functions transformations to
            apply to that axis\' values.

            Use either ``mapper`` and ``axis`` to
            specify the axis to target with ``mapper``, or ``index``
            and/or ``columns``.
        axis : {0 or \'index\', 1 or \'columns\'}, default 0
            The axis to rename.
        inplace : bool, default False
            Modifies the object directly, instead of creating a new DataFrame.

        Returns
        -------
        DataFrame, or None if `inplace` is True.

        See Also
        --------
        Series.rename : Alter Series index labels or name.
        DataFrame.rename : Alter DataFrame index labels or name.
        Index.rename : Set new names on index.

        Notes
        -----
        ``DataFrame.rename_axis`` supports two calling conventions

        * ``(index=index_mapper, columns=columns_mapper, ...)``
        * ``(mapper, axis={\'index\', \'columns\'}, ...)``

        The first calling convention will only modify the names of
        the index and/or the names of the Index object that is the columns.

        The second calling convention will modify the names of the
        corresponding index specified by axis.

        We *highly* recommend using keyword arguments to clarify your
        intent.

        Examples
        --------
        >>> df = ps.DataFrame({"num_legs": [4, 4, 2],
        ...                    "num_arms": [0, 0, 2]},
        ...                   index=["dog", "cat", "monkey"],
        ...                   columns=["num_legs", "num_arms"])
        >>> df
                num_legs  num_arms
        dog            4         0
        cat            4         0
        monkey         2         2

        >>> df = df.rename_axis("animal").sort_index()
        >>> df  # doctest: +NORMALIZE_WHITESPACE
                num_legs  num_arms
        animal
        cat            4         0
        dog            4         0
        monkey         2         2

        >>> df = df.rename_axis("limbs", axis="columns").sort_index()
        >>> df # doctest: +NORMALIZE_WHITESPACE
        limbs   num_legs  num_arms
        animal
        cat            4         0
        dog            4         0
        monkey         2         2

        **MultiIndex**

        >>> index = pd.MultiIndex.from_product([[\'mammal\'],
        ...                                     [\'dog\', \'cat\', \'monkey\']],
        ...                                    names=[\'type\', \'name\'])
        >>> df = ps.DataFrame({"num_legs": [4, 4, 2],
        ...                    "num_arms": [0, 0, 2]},
        ...                   index=index,
        ...                   columns=["num_legs", "num_arms"])
        >>> df  # doctest: +NORMALIZE_WHITESPACE
                       num_legs  num_arms
        type   name
        mammal dog            4         0
               cat            4         0
               monkey         2         2

        >>> df.rename_axis(index={\'type\': \'class\'}).sort_index()  # doctest: +NORMALIZE_WHITESPACE
                       num_legs  num_arms
        class  name
        mammal cat            4         0
               dog            4         0
               monkey         2         2

        >>> df.rename_axis(index=str.upper).sort_index()  # doctest: +NORMALIZE_WHITESPACE
                       num_legs  num_arms
        TYPE   NAME
        mammal cat            4         0
               dog            4         0
               monkey         2         2
        '''
    def keys(self) -> pd.Index:
        """
        Return alias for columns.

        Returns
        -------
        Index
            Columns of the DataFrame.

        Examples
        --------
        >>> df = ps.DataFrame([[1, 2], [4, 5], [7, 8]],
        ...                   index=['cobra', 'viper', 'sidewinder'],
        ...                   columns=['max_speed', 'shield'])
        >>> df
                    max_speed  shield
        cobra               1       2
        viper               4       5
        sidewinder          7       8

        >>> df.keys()
        Index(['max_speed', 'shield'], dtype='object')
        """
    def pct_change(self, periods: int = 1) -> DataFrame:
        """
        Percentage change between the current and a prior element.

        .. note:: the current implementation of this API uses Spark's Window without
            specifying partition specification. This leads to moving all data into
            a single partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

        Parameters
        ----------
        periods : int, default 1
            Periods to shift for forming percent change.

        Returns
        -------
        DataFrame

        Examples
        --------
        Percentage change in French franc, Deutsche Mark, and Italian lira
        from 1980-01-01 to 1980-03-01.

        >>> df = ps.DataFrame({
        ...     'FR': [4.0405, 4.0963, 4.3149],
        ...     'GR': [1.7246, 1.7482, 1.8519],
        ...     'IT': [804.74, 810.01, 860.13]},
        ...     index=['1980-01-01', '1980-02-01', '1980-03-01'])
        >>> df
                        FR      GR      IT
        1980-01-01  4.0405  1.7246  804.74
        1980-02-01  4.0963  1.7482  810.01
        1980-03-01  4.3149  1.8519  860.13

        >>> df.pct_change()
                          FR        GR        IT
        1980-01-01       NaN       NaN       NaN
        1980-02-01  0.013810  0.013684  0.006549
        1980-03-01  0.053365  0.059318  0.061876

        You can set periods to shift for forming percent change

        >>> df.pct_change(2)
                          FR        GR       IT
        1980-01-01       NaN       NaN      NaN
        1980-02-01       NaN       NaN      NaN
        1980-03-01  0.067912  0.073814  0.06883
        """
    def idxmax(self, axis: Axis = 0) -> Series:
        """
        Return index of first occurrence of maximum over requested axis.
        NA/null values are excluded.

        .. note:: This API collect all rows with maximum value using `to_pandas()`
            because we suppose the number of rows with max values are usually small in general.

        Parameters
        ----------
        axis : 0 or 'index'
            Can only be set to 0 now.

        Returns
        -------
        Series

        See Also
        --------
        Series.idxmax

        Examples
        --------
        >>> psdf = ps.DataFrame({'a': [1, 2, 3, 2],
        ...                     'b': [4.0, 2.0, 3.0, 1.0],
        ...                     'c': [300, 200, 400, 200]})
        >>> psdf
           a    b    c
        0  1  4.0  300
        1  2  2.0  200
        2  3  3.0  400
        3  2  1.0  200

        >>> psdf.idxmax()
        a    2
        b    0
        c    2
        dtype: int64

        For Multi-column Index

        >>> psdf = ps.DataFrame({'a': [1, 2, 3, 2],
        ...                     'b': [4.0, 2.0, 3.0, 1.0],
        ...                     'c': [300, 200, 400, 200]})
        >>> psdf.columns = pd.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
        >>> psdf
           a    b    c
           x    y    z
        0  1  4.0  300
        1  2  2.0  200
        2  3  3.0  400
        3  2  1.0  200

        >>> psdf.idxmax()
        a  x    2
        b  y    0
        c  z    2
        dtype: int64
        """
    def idxmin(self, axis: Axis = 0) -> Series:
        """
        Return index of first occurrence of minimum over requested axis.
        NA/null values are excluded.

        .. note:: This API collect all rows with minimum value using `to_pandas()`
            because we suppose the number of rows with min values are usually small in general.

        Parameters
        ----------
        axis : 0 or 'index'
            Can only be set to 0 now.

        Returns
        -------
        Series

        See Also
        --------
        Series.idxmin

        Examples
        --------
        >>> psdf = ps.DataFrame({'a': [1, 2, 3, 2],
        ...                     'b': [4.0, 2.0, 3.0, 1.0],
        ...                     'c': [300, 200, 400, 200]})
        >>> psdf
           a    b    c
        0  1  4.0  300
        1  2  2.0  200
        2  3  3.0  400
        3  2  1.0  200

        >>> psdf.idxmin()
        a    0
        b    3
        c    1
        dtype: int64

        For Multi-column Index

        >>> psdf = ps.DataFrame({'a': [1, 2, 3, 2],
        ...                     'b': [4.0, 2.0, 3.0, 1.0],
        ...                     'c': [300, 200, 400, 200]})
        >>> psdf.columns = pd.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
        >>> psdf
           a    b    c
           x    y    z
        0  1  4.0  300
        1  2  2.0  200
        2  3  3.0  400
        3  2  1.0  200

        >>> psdf.idxmin()
        a  x    0
        b  y    3
        c  z    1
        dtype: int64
        """
    count: Incomplete
    def info(self, verbose: bool | None = None, buf: IO[str] | None = None, max_cols: int | None = None, null_counts: bool | None = None) -> None:
        '''
        Print a concise summary of a DataFrame.

        This method prints information about a DataFrame including
        the index dtype and column dtypes, non-null values and memory usage.

        Parameters
        ----------
        verbose : bool, optional
            Whether to print the full summary.
        buf : writable buffer, defaults to sys.stdout
            Where to send the output. By default the output is printed to
            sys.stdout. Pass a writable buffer if you need to further process
            the output.
        max_cols : int, optional
            When to switch from the verbose to the truncated output. If the
            DataFrame has more than `max_cols` columns, the truncated output
            is used.
        null_counts : bool, optional
            Whether to show the non-null counts.

            .. deprecated:: 3.4.0

        Returns
        -------
        None
            This method prints a summary of a DataFrame and returns None.

        See Also
        --------
        DataFrame.describe: Generate descriptive statistics of DataFrame
            columns.

        Examples
        --------
        >>> int_values = [1, 2, 3, 4, 5]
        >>> text_values = [\'alpha\', \'beta\', \'gamma\', \'delta\', \'epsilon\']
        >>> float_values = [0.0, 0.25, 0.5, 0.75, 1.0]
        >>> df = ps.DataFrame(
        ...     {"int_col": int_values, "text_col": text_values, "float_col": float_values},
        ...     columns=[\'int_col\', \'text_col\', \'float_col\'])
        >>> df
           int_col text_col  float_col
        0        1    alpha       0.00
        1        2     beta       0.25
        2        3    gamma       0.50
        3        4    delta       0.75
        4        5  epsilon       1.00

        Prints information of all columns:

        >>> df.info(verbose=True)  # doctest: +SKIP
        <class \'pyspark.pandas.frame.DataFrame\'>
        Index: 5 entries, 0 to 4
        Data columns (total 3 columns):
         #   Column     Non-Null Count  Dtype
        ---  ------     --------------  -----
         0   int_col    5 non-null      int64
         1   text_col   5 non-null      object
         2   float_col  5 non-null      float64
        dtypes: float64(1), int64(1), object(1)

        Prints a summary of columns count and its dtypes but not per column
        information:

        >>> df.info(verbose=False)  # doctest: +SKIP
        <class \'pyspark.pandas.frame.DataFrame\'>
        Index: 5 entries, 0 to 4
        Columns: 3 entries, int_col to float_col
        dtypes: float64(1), int64(1), object(1)

        Pipe output of DataFrame.info to buffer instead of sys.stdout, get
        buffer content and writes to a text file:

        >>> import io
        >>> buffer = io.StringIO()
        >>> df.info(buf=buffer)
        >>> s = buffer.getvalue()
        >>> with open(\'%s/info.txt\' % path, "w",
        ...           encoding="utf-8") as f:
        ...     _ = f.write(s)
        >>> with open(\'%s/info.txt\' % path) as f:
        ...     f.readlines()  # doctest: +SKIP
        ["<class \'pyspark.pandas.frame.DataFrame\'>\\n",
        \'Index: 5 entries, 0 to 4\\n\',
        \'Data columns (total 3 columns):\\n\',
        \' #   Column     Non-Null Count  Dtype  \\n\',
        \'---  ------     --------------  -----  \\n\',
        \' 0   int_col    5 non-null      int64  \\n\',
        \' 1   text_col   5 non-null      object \\n\',
        \' 2   float_col  5 non-null      float64\\n\',
        \'dtypes: float64(1), int64(1), object(1)\']
        '''
    def quantile(self, q: float | Iterable[float] = 0.5, axis: Axis = 0, numeric_only: bool = True, accuracy: int = 10000) -> DataFrameOrSeries:
        """
        Return value at the given quantile.

        .. note:: Unlike pandas', the quantile in pandas-on-Spark is an approximated quantile
            based upon approximate percentile computation because computing quantile across a
            large dataset is extremely expensive.

        Parameters
        ----------
        q : float or array-like, default 0.5 (50% quantile)
            0 <= q <= 1, the quantile(s) to compute.
        axis : int or str, default 0 or 'index'
            Can only be set to 0 now.
        numeric_only : bool, default True
            If False, the quantile of datetime and time delta data will be computed as well.
            Can only be set to True now.
        accuracy : int, optional
            Default accuracy of approximation. Larger value means better accuracy.
            The relative error can be deduced by 1.0 / accuracy.

        Returns
        -------
        Series or DataFrame
            If q is an array, a DataFrame will be returned where the
            index is q, the columns are the columns of self, and the values are the quantiles.
            If q is a float, a Series will be returned where the
            index is the columns of self and the values are the quantiles.

        Examples
        --------
        >>> psdf = ps.DataFrame({'a': [1, 2, 3, 4, 5], 'b': [6, 7, 8, 9, 0]})
        >>> psdf
           a  b
        0  1  6
        1  2  7
        2  3  8
        3  4  9
        4  5  0

        >>> psdf.quantile(.5)
        a    3.0
        b    7.0
        Name: 0.5, dtype: float64

        >>> psdf.quantile([.25, .5, .75])
                a    b
        0.25  2.0  6.0
        0.50  3.0  7.0
        0.75  4.0  8.0
        """
    def query(self, expr: str, inplace: bool = False) -> DataFrame | None:
        """
        Query the columns of a DataFrame with a boolean expression.

        .. note:: Internal columns that starting with a '__' prefix are able to access, however,
            they are not supposed to be accessed.

        .. note:: This API delegates to Spark SQL so the syntax follows Spark SQL. Therefore, the
            pandas specific syntax such as `@` is not supported. If you want the pandas syntax,
            you can work around with :meth:`DataFrame.pandas_on_spark.apply_batch`, but you should
            be aware that `query_func` will be executed at different nodes in a distributed manner.
            So, for example to use `@` syntax, make sure the variable is serialized by
            putting it within the closure as below.

            >>> df = ps.DataFrame({'A': range(2000), 'B': range(2000)})
            >>> def query_func(pdf):
            ...     num = 1995
            ...     return pdf.query('A > @num')
            >>> df.pandas_on_spark.apply_batch(query_func)
                     A     B
            1996  1996  1996
            1997  1997  1997
            1998  1998  1998
            1999  1999  1999

        Parameters
        ----------
        expr : str
            The query string to evaluate.

            You can refer to column names that contain spaces by surrounding
            them in backticks.

            For example, if one of your columns is called ``a a`` and you want
            to sum it with ``b``, your query should be ```a a` + b``.

        inplace : bool
            Whether the query should modify the data in place or return
            a modified copy.

        Returns
        -------
        DataFrame
            DataFrame resulting from the provided query expression.

        Examples
        --------
        >>> df = ps.DataFrame({'A': range(1, 6),
        ...                    'B': range(10, 0, -2),
        ...                    'C C': range(10, 5, -1)})
        >>> df
           A   B  C C
        0  1  10   10
        1  2   8    9
        2  3   6    8
        3  4   4    7
        4  5   2    6

        >>> df.query('A > B')
           A  B  C C
        4  5  2    6

        The previous expression is equivalent to

        >>> df[df.A > df.B]
           A  B  C C
        4  5  2    6

        For columns with spaces in their name, you can use backtick quoting.

        >>> df.query('B == `C C`')
           A   B  C C
        0  1  10   10

        The previous expression is equivalent to

        >>> df[df.B == df['C C']]
           A   B  C C
        0  1  10   10
        """
    def take(self, indices: List[int], axis: Axis = 0, **kwargs: Any) -> DataFrame:
        """
        Return the elements in the given *positional* indices along an axis.

        This means that we are not indexing according to actual values in
        the index attribute of the object. We are indexing according to the
        actual position of the element in the object.

        Parameters
        ----------
        indices : array-like
            An array of ints indicating which positions to take.
        axis : {0 or 'index', 1 or 'columns', None}, default 0
            The axis on which to select elements. ``0`` means that we are
            selecting rows, ``1`` means that we are selecting columns.
        **kwargs
            For compatibility with :meth:`numpy.take`. Has no effect on the
            output.

        Returns
        -------
        taken : same type as caller
            An array-like containing the elements taken from the object.

        See Also
        --------
        DataFrame.loc : Select a subset of a DataFrame by labels.
        DataFrame.iloc : Select a subset of a DataFrame by positions.
        numpy.take : Take elements from an array along an axis.

        Examples
        --------
        >>> df = ps.DataFrame([('falcon', 'bird', 389.0),
        ...                    ('parrot', 'bird', 24.0),
        ...                    ('lion', 'mammal', 80.5),
        ...                    ('monkey', 'mammal', np.nan)],
        ...                   columns=['name', 'class', 'max_speed'],
        ...                   index=[0, 2, 3, 1])
        >>> df
             name   class  max_speed
        0  falcon    bird      389.0
        2  parrot    bird       24.0
        3    lion  mammal       80.5
        1  monkey  mammal        NaN

        Take elements at positions 0 and 3 along the axis 0 (default).

        Note how the actual indices selected (0 and 1) do not correspond to
        our selected indices 0 and 3. That's because we are selecting the 0th
        and 3rd rows, not rows whose indices equal 0 and 3.

        >>> df.take([0, 3]).sort_index()
             name   class  max_speed
        0  falcon    bird      389.0
        1  monkey  mammal        NaN

        Take elements at indices 1 and 2 along the axis 1 (column selection).

        >>> df.take([1, 2], axis=1)
            class  max_speed
        0    bird      389.0
        2    bird       24.0
        3  mammal       80.5
        1  mammal        NaN

        We may take elements using negative integers for positive indices,
        starting from the end of the object, just like with Python lists.

        >>> df.take([-1, -2]).sort_index()
             name   class  max_speed
        1  monkey  mammal        NaN
        3    lion  mammal       80.5
        """
    def eval(self, expr: str, inplace: bool = False) -> DataFrameOrSeries | None:
        """
        Evaluate a string describing operations on DataFrame columns.

        Operates on columns only, not specific rows or elements. This allows
        `eval` to run arbitrary code, which can make you vulnerable to code
        injection if you pass user input to this function.

        Parameters
        ----------
        expr : str
            The expression string to evaluate.
        inplace : bool, default False
            If the expression contains an assignment, whether to perform the
            operation inplace and mutate the existing DataFrame. Otherwise,
            a new DataFrame is returned.

        Returns
        -------
        The result of the evaluation.

        See Also
        --------
        DataFrame.query : Evaluates a boolean expression to query the columns
            of a frame.
        DataFrame.assign : Can evaluate an expression or function to create new
            values for a column.
        eval : Evaluate a Python expression as a string using various
            backends.

        Examples
        --------
        >>> df = ps.DataFrame({'A': range(1, 6), 'B': range(10, 0, -2)})
        >>> df
           A   B
        0  1  10
        1  2   8
        2  3   6
        3  4   4
        4  5   2
        >>> df.eval('A + B')
        0    11
        1    10
        2     9
        3     8
        4     7
        dtype: int64

        Assignment is allowed though by default the original DataFrame is not
        modified.

        >>> df.eval('C = A + B')
           A   B   C
        0  1  10  11
        1  2   8  10
        2  3   6   9
        3  4   4   8
        4  5   2   7
        >>> df
           A   B
        0  1  10
        1  2   8
        2  3   6
        3  4   4
        4  5   2

        Use ``inplace=True`` to modify the original DataFrame.

        >>> df.eval('C = A + B', inplace=True)
        >>> df
           A   B   C
        0  1  10  11
        1  2   8  10
        2  3   6   9
        3  4   4   8
        4  5   2   7
        """
    def explode(self, column: Name, ignore_index: bool = False) -> DataFrame:
        """
        Transform each element of a list-like to a row, replicating index values.

        Parameters
        ----------
        column : str or tuple
            Column to explode.
        ignore_index : bool, default False
            If True, the resulting index will be labeled 0, 1, …, n - 1.

        Returns
        -------
        DataFrame
            Exploded lists to rows of the subset columns;
            index will be duplicated for these rows.

        See Also
        --------
        DataFrame.unstack : Pivot a level of the (necessarily hierarchical)
            index labels.
        DataFrame.melt : Unpivot a DataFrame from wide format to long format.

        Examples
        --------
        >>> df = ps.DataFrame({'A': [[1, 2, 3], [], [3, 4]], 'B': 1})
        >>> df
                   A  B
        0  [1, 2, 3]  1
        1         []  1
        2     [3, 4]  1

        >>> df.explode('A')
             A  B
        0  1.0  1
        0  2.0  1
        0  3.0  1
        1  NaN  1
        2  3.0  1
        2  4.0  1

        >>> df.explode('A', ignore_index=True)
             A  B
        0  1.0  1
        1  2.0  1
        2  3.0  1
        3  NaN  1
        4  3.0  1
        5  4.0  1
        """
    def mad(self, axis: Axis = 0) -> Series:
        """
        Return the mean absolute deviation of values.

        .. deprecated:: 3.4.0

        Parameters
        ----------
        axis : {index (0), columns (1)}
            Axis for the function to be applied on.

        Examples
        --------
        >>> df = ps.DataFrame({'a': [1, 2, 3, np.nan], 'b': [0.1, 0.2, 0.3, np.nan]},
        ...                   columns=['a', 'b'])

        >>> df.mad()
        a    0.666667
        b    0.066667
        dtype: float64

        >>> df.mad(axis=1)
        0    0.45
        1    0.90
        2    1.35
        3     NaN
        dtype: float64
        """
    def mode(self, axis: Axis = 0, numeric_only: bool = False, dropna: bool = True) -> DataFrame:
        """
        Get the mode(s) of each element along the selected axis.

        The mode of a set of values is the value that appears most often.
        It can be multiple values.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        axis : {0 or 'index'}, default 0
            Axis for the function to be applied on.
        numeric_only : bool, default False
            If True, only apply to numeric columns.
        dropna : bool, default True
            Don't consider counts of NaN/NaT.

        Returns
        -------
        DataFrame
            The modes of each column or row.

        See Also
        --------
        Series.mode : Return the highest frequency value in a Series.
        Series.value_counts : Return the counts of values in a Series.

        Examples
        --------
        >>> df = ps.DataFrame([('bird', 2, 2),
        ...                    ('mammal', 4, np.nan),
        ...                    ('arthropod', 8, 0),
        ...                    ('bird', 2, np.nan)],
        ...                   index=('falcon', 'horse', 'spider', 'ostrich'),
        ...                   columns=('species', 'legs', 'wings'))
        >>> df
                   species  legs  wings
        falcon        bird     2    2.0
        horse       mammal     4    NaN
        spider   arthropod     8    0.0
        ostrich       bird     2    NaN

        By default missing values are not considered, and the mode of wings
        are both 0 and 2. Because the resulting DataFrame has two rows,
        the second row of ``species`` and ``legs`` contains ``NaN``.

        >>> df.mode()
          species  legs  wings
        0    bird   2.0    0.0
        1    None   NaN    2.0

        Setting ``dropna=False`` ``NaN`` values are considered and they can be
        the mode (like for wings).

        >>> df.mode(dropna=False)
          species  legs  wings
        0    bird     2    NaN

        Setting ``numeric_only=True``, only the mode of numeric columns is
        computed, and columns of other types are ignored.

        >>> df.mode(numeric_only=True)
           legs  wings
        0   2.0    0.0
        1   NaN    2.0
        """
    def tail(self, n: int = 5) -> DataFrame:
        """
        Return the last `n` rows.

        This function returns last `n` rows from the object based on
        position. It is useful for quickly verifying data, for example,
        after sorting or appending rows.

        For negative values of `n`, this function returns all rows except
        the first `n` rows, equivalent to ``df[n:]``.

        Parameters
        ----------
        n : int, default 5
            Number of rows to select.

        Returns
        -------
        type of caller
            The last `n` rows of the caller object.

        See Also
        --------
        DataFrame.head : The first `n` rows of the caller object.

        Examples
        --------
        >>> df = ps.DataFrame({'animal': ['alligator', 'bee', 'falcon', 'lion',
        ...                    'monkey', 'parrot', 'shark', 'whale', 'zebra']})
        >>> df
              animal
        0  alligator
        1        bee
        2     falcon
        3       lion
        4     monkey
        5     parrot
        6      shark
        7      whale
        8      zebra

        Viewing the last 5 lines

        >>> df.tail()  # doctest: +SKIP
           animal
        4  monkey
        5  parrot
        6   shark
        7   whale
        8   zebra

        Viewing the last `n` lines (three in this case)

        >>> df.tail(3)  # doctest: +SKIP
          animal
        6  shark
        7  whale
        8  zebra

        For negative values of `n`

        >>> df.tail(-3)  # doctest: +SKIP
           animal
        3    lion
        4  monkey
        5  parrot
        6   shark
        7   whale
        8   zebra
        """
    def align(self, other: DataFrameOrSeries, join: str = 'outer', axis: Axis | None = None, copy: bool = True) -> Tuple['DataFrame', DataFrameOrSeries]:
        '''
        Align two objects on their axes with the specified join method.

        Join method is specified for each axis Index.

        Parameters
        ----------
        other : DataFrame or Series
        join : {{\'outer\', \'inner\', \'left\', \'right\'}}, default \'outer\'
        axis : allowed axis of the other object, default None
            Align on index (0), columns (1), or both (None).
        copy : bool, default True
            Always returns new objects. If copy=False and no reindexing is
            required then original objects are returned.

        Returns
        -------
        (left, right) : (DataFrame, type of other)
            Aligned objects.

        Examples
        --------
        >>> ps.set_option("compute.ops_on_diff_frames", True)
        >>> df1 = ps.DataFrame({"a": [1, 2, 3], "b": ["a", "b", "c"]}, index=[10, 20, 30])
        >>> df2 = ps.DataFrame({"a": [4, 5, 6], "c": ["d", "e", "f"]}, index=[10, 11, 12])

        Align both axis:

        >>> aligned_l, aligned_r = df1.align(df2)
        >>> aligned_l.sort_index()
              a     b   c
        10  1.0     a NaN
        11  NaN  None NaN
        12  NaN  None NaN
        20  2.0     b NaN
        30  3.0     c NaN
        >>> aligned_r.sort_index()
              a   b     c
        10  4.0 NaN     d
        11  5.0 NaN     e
        12  6.0 NaN     f
        20  NaN NaN  None
        30  NaN NaN  None

        Align only axis=0 (index):

        >>> aligned_l, aligned_r = df1.align(df2, axis=0)
        >>> aligned_l.sort_index()
              a     b
        10  1.0     a
        11  NaN  None
        12  NaN  None
        20  2.0     b
        30  3.0     c
        >>> aligned_r.sort_index()
              a     c
        10  4.0     d
        11  5.0     e
        12  6.0     f
        20  NaN  None
        30  NaN  None

        Align only axis=1 (column):

        >>> aligned_l, aligned_r = df1.align(df2, axis=1)
        >>> aligned_l.sort_index()
            a  b   c
        10  1  a NaN
        20  2  b NaN
        30  3  c NaN
        >>> aligned_r.sort_index()
            a   b  c
        10  4 NaN  d
        11  5 NaN  e
        12  6 NaN  f

        Align with the join type "inner":

        >>> aligned_l, aligned_r = df1.align(df2, join="inner")
        >>> aligned_l.sort_index()
            a
        10  1
        >>> aligned_r.sort_index()
            a
        10  4

        Align with a Series:

        >>> s = ps.Series([7, 8, 9], index=[10, 11, 12])
        >>> aligned_l, aligned_r = df1.align(s, axis=0)
        >>> aligned_l.sort_index()
              a     b
        10  1.0     a
        11  NaN  None
        12  NaN  None
        20  2.0     b
        30  3.0     c
        >>> aligned_r.sort_index()
        10    7.0
        11    8.0
        12    9.0
        20    NaN
        30    NaN
        dtype: float64

        >>> ps.reset_option("compute.ops_on_diff_frames")
        '''
    @staticmethod
    def from_dict(data: Dict[Name, Sequence[Any]], orient: str = 'columns', dtype: str | Dtype = None, columns: List[Name] | None = None) -> DataFrame:
        '''
        Construct DataFrame from dict of array-like or dicts.

        Creates DataFrame object from dictionary by columns or by index
        allowing dtype specification.

        Parameters
        ----------
        data : dict
            Of the form {field : array-like} or {field : dict}.
        orient : {\'columns\', \'index\'}, default \'columns\'
            The "orientation" of the data. If the keys of the passed dict
            should be the columns of the resulting DataFrame, pass \'columns\'
            (default). Otherwise, if the keys should be rows, pass \'index\'.
        dtype : dtype, default None
            Data type to force, otherwise infer.
        columns : list, default None
            Column labels to use when ``orient=\'index\'``. Raises a ValueError
            if used with ``orient=\'columns\'``.

        Returns
        -------
        DataFrame

        See Also
        --------
        DataFrame.from_records : DataFrame from structured ndarray, sequence
            of tuples or dicts, or DataFrame.
        DataFrame : DataFrame object creation using constructor.

        Examples
        --------
        By default the keys of the dict become the DataFrame columns:

        >>> data = {\'col_1\': [3, 2, 1, 0], \'col_2\': [10, 20, 30, 40]}
        >>> ps.DataFrame.from_dict(data)
           col_1  col_2
        0      3     10
        1      2     20
        2      1     30
        3      0     40

        Specify ``orient=\'index\'`` to create the DataFrame using dictionary
        keys as rows:

        >>> data = {\'row_1\': [3, 2, 1, 0], \'row_2\': [10, 20, 30, 40]}
        >>> ps.DataFrame.from_dict(data, orient=\'index\').sort_index()
                0   1   2   3
        row_1   3   2   1   0
        row_2  10  20  30  40

        When using the \'index\' orientation, the column names can be
        specified manually:

        >>> ps.DataFrame.from_dict(data, orient=\'index\',
        ...                        columns=[\'A\', \'B\', \'C\', \'D\']).sort_index()
                A   B   C   D
        row_1   3   2   1   0
        row_2  10  20  30  40
        '''
    def groupby(self, by: Name | Series | List[Name | Series], axis: Axis = 0, as_index: bool = True, dropna: bool = True) -> DataFrameGroupBy: ...
    def resample(self, rule: str, closed: str | None = None, label: str | None = None, on: Series | None = None) -> DataFrameResampler:
        """
        Resample time-series data.

        Convenience method for frequency conversion and resampling of time series.
        The object must have a datetime-like index (only support `DatetimeIndex` for now),
        or the caller must pass the label of a datetime-like
        series/index to the ``on`` keyword parameter.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        rule : str
            The offset string or object representing target conversion.
            Currently, supported units are {'Y', 'A', 'M', 'D', 'H',
            'T', 'MIN', 'S'}.
        closed : {{'right', 'left'}}, default None
            Which side of bin interval is closed. The default is 'left'
            for all frequency offsets except for 'A', 'Y' and 'M' which all
            have a default of 'right'.
        label : {{'right', 'left'}}, default None
            Which bin edge label to label bucket with. The default is 'left'
            for all frequency offsets except for 'A', 'Y' and 'M' which all
            have a default of 'right'.
        on : Series, optional
            For a DataFrame, column to use instead of index for resampling.
            Column must be datetime-like.

        Returns
        -------
        DataFrameResampler

        See Also
        --------
        Series.resample : Resample a Series.
        groupby : Group by mapping, function, label, or list of labels.
        """
    def __getitem__(self, key: Any) -> Any: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __getattr__(self, key: str) -> Any: ...
    def __setattr__(self, key: str, value: Any) -> None: ...
    def __len__(self) -> int: ...
    def __dir__(self) -> Iterable[str]: ...
    def __iter__(self) -> Iterator[Name]: ...
    def __array_ufunc__(self, ufunc: Callable, method: str, *inputs: Any, **kwargs: Any) -> DataFrame: ...
    def __class_getitem__(cls, params: Any) -> object: ...

class CachedDataFrame(DataFrame):
    """
    Cached pandas-on-Spark DataFrame, which corresponds to pandas DataFrame logically, but
    internally it caches the corresponding Spark DataFrame.
    """
    def __init__(self, internal: InternalFrame, storage_level: StorageLevel | None = None) -> None: ...
    def __enter__(self) -> CachedDataFrame: ...
    def __exit__(self, exception_type: Type[BaseException] | None, exception_value: BaseException | None, traceback: TracebackType | None) -> bool | None: ...
    spark: Incomplete
