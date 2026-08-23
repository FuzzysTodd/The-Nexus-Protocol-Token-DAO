import pandas as pd
from pyspark.pandas._typing import DataFrameOrSeries as DataFrameOrSeries, Name as Name
from pyspark.pandas.frame import DataFrame as DataFrame
from pyspark.pandas.internal import InternalField as InternalField, InternalFrame as InternalFrame, SPARK_DEFAULT_SERIES_NAME as SPARK_DEFAULT_SERIES_NAME, SPARK_INDEX_NAME_FORMAT as SPARK_INDEX_NAME_FORMAT, SPARK_INDEX_NAME_PATTERN as SPARK_INDEX_NAME_PATTERN
from pyspark.pandas.series import Series as Series
from pyspark.pandas.typedef import DataFrameType as DataFrameType, ScalarType as ScalarType, SeriesType as SeriesType, infer_return_type as infer_return_type
from pyspark.pandas.utils import is_name_like_tuple as is_name_like_tuple, is_name_like_value as is_name_like_value, log_advice as log_advice, name_like_string as name_like_string, scol_for as scol_for, verify_temp_column_name as verify_temp_column_name
from pyspark.sql._typing import UserDefinedFunctionLike as UserDefinedFunctionLike
from pyspark.sql.functions import pandas_udf as pandas_udf
from pyspark.sql.types import DataType as DataType, LongType as LongType, StructField as StructField, StructType as StructType
from typing import Any, Callable, Tuple

class PandasOnSparkFrameMethods:
    """pandas-on-Spark specific features for DataFrame."""
    def __init__(self, frame: DataFrame) -> None: ...
    def attach_id_column(self, id_type: str, column: Name) -> DataFrame:
        '''
        Attach a column to be used as an identifier of rows similar to the default index.

        See also `Default Index type
        <https://spark.apache.org/docs/latest/api/python/user_guide/pandas_on_spark/options.html#default-index-type>`_.

        Parameters
        ----------
        id_type : string
            The id type.

            - \'sequence\' : a sequence that increases one by one.

              .. note:: this uses Spark\'s Window without specifying partition specification.
                  This leads to moving all data into a single partition in a single machine and
                  could cause serious performance degradation.
                  Avoid this method with very large datasets.

            - \'distributed-sequence\' : a sequence that increases one by one,
              by group-by and group-map approach in a distributed manner.
            - \'distributed\' : a monotonically increasing sequence simply by using PySpark’s
              monotonically_increasing_id function in a fully distributed manner.

        column : string or tuple of string
            The column name.

        Returns
        -------
        DataFrame
            The DataFrame attached the column.

        Examples
        --------
        >>> df = ps.DataFrame({"x": [\'a\', \'b\', \'c\']})
        >>> df.pandas_on_spark.attach_id_column(id_type="sequence", column="id")
           x  id
        0  a   0
        1  b   1
        2  c   2

        >>> df.pandas_on_spark.attach_id_column(id_type="distributed-sequence", column=0)
           x  0
        0  a  0
        1  b  1
        2  c  2

        >>> df.pandas_on_spark.attach_id_column(id_type="distributed", column=0.0)
        ... # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
           x  0.0
        0  a  ...
        1  b  ...
        2  c  ...

        For multi-index columns:

        >>> df = ps.DataFrame({("x", "y"): [\'a\', \'b\', \'c\']})
        >>> df.pandas_on_spark.attach_id_column(id_type="sequence", column=("id-x", "id-y"))
           x id-x
           y id-y
        0  a    0
        1  b    1
        2  c    2

        >>> df.pandas_on_spark.attach_id_column(id_type="distributed-sequence", column=(0, 1.0))
           x   0
           y 1.0
        0  a   0
        1  b   1
        2  c   2
        '''
    def apply_batch(self, func: Callable[..., pd.DataFrame], args: Tuple = (), **kwds: Any) -> DataFrame:
        '''
        Apply a function that takes pandas DataFrame and outputs pandas DataFrame. The pandas
        DataFrame given to the function is of a batch used internally.

        See also `Transform and apply a function
        <https://spark.apache.org/docs/latest/api/python/user_guide/pandas_on_spark/transform_apply.html>`_.

        .. note:: the `func` is unable to access the whole input frame. pandas-on-Spark
            internally splits the input series into multiple batches and calls `func` with each
            batch multiple times. Therefore, operations such as global aggregations are impossible.
            See the example below.

            >>> # This case does not return the length of whole frame but of the batch internally
            ... # used.
            ... def length(pdf) -> ps.DataFrame[int, [int]]:
            ...     return pd.DataFrame([len(pdf)])
            ...
            >>> df = ps.DataFrame({\'A\': range(1000)})
            >>> df.pandas_on_spark.apply_batch(length)  # doctest: +SKIP
                c0
            0   83
            1   83
            2   83
            ...
            10  83
            11  83

        .. note:: this API executes the function once to infer the type which is
            potentially expensive, for instance, when the dataset is created after
            aggregations or sorting.

            To avoid this, specify return type in ``func``, for instance, as below:

            >>> def plus_one(x) -> ps.DataFrame[int, [float, float]]:
            ...     return x + 1

            If the return type is specified, the output column names become
            `c0, c1, c2 ... cn`. These names are positionally mapped to the returned
            DataFrame in ``func``.

            To specify the column names, you can assign them in a NumPy compound type style
            as below:

            >>> def plus_one(x) -> ps.DataFrame[("index", int), [("a", float), ("b", float)]]:
            ...     return x + 1

            >>> pdf = pd.DataFrame({\'a\': [1, 2, 3], \'b\': [3, 4, 5]})
            >>> def plus_one(x) -> ps.DataFrame[
            ...         (pdf.index.name, pdf.index.dtype), zip(pdf.dtypes, pdf.columns)]:
            ...     return x + 1

        Parameters
        ----------
        func : function
            Function to apply to each pandas frame.
        args : tuple
            Positional arguments to pass to `func` in addition to the
            array/series.
        **kwds
            Additional keyword arguments to pass as keywords arguments to
            `func`.

        Returns
        -------
        DataFrame

        See Also
        --------
        DataFrame.apply: For row/columnwise operations.
        DataFrame.applymap: For elementwise operations.
        DataFrame.aggregate: Only perform aggregating type operations.
        DataFrame.transform: Only perform transforming type operations.
        Series.pandas_on_spark.transform_batch: transform the search as each pandas chunks.

        Examples
        --------
        >>> df = ps.DataFrame([(1, 2), (3, 4), (5, 6)], columns=[\'A\', \'B\'])
        >>> df
           A  B
        0  1  2
        1  3  4
        2  5  6

        >>> def query_func(pdf) -> ps.DataFrame[int, [int, int]]:
        ...     return pdf.query(\'A == 1\')
        >>> df.pandas_on_spark.apply_batch(query_func)
           c0  c1
        0   1   2

        >>> def query_func(pdf) -> ps.DataFrame[("idx", int), [("A", int), ("B", int)]]:
        ...     return pdf.query(\'A == 1\')
        >>> df.pandas_on_spark.apply_batch(query_func)  # doctest: +NORMALIZE_WHITESPACE
             A  B
        idx
        0    1  2

        You can also omit the type hints so pandas-on-Spark infers the return schema as below:

        >>> df.pandas_on_spark.apply_batch(lambda pdf: pdf.query(\'A == 1\'))
           A  B
        0  1  2

        You can also specify extra arguments.

        >>> def calculation(pdf, y, z) -> ps.DataFrame[int, [int, int]]:
        ...     return pdf ** y + z
        >>> df.pandas_on_spark.apply_batch(calculation, args=(10,), z=20)
                c0        c1
        0       21      1044
        1    59069   1048596
        2  9765645  60466196

        You can also use ``np.ufunc`` and built-in functions as input.

        >>> df.pandas_on_spark.apply_batch(np.add, args=(10,))
            A   B
        0  11  12
        1  13  14
        2  15  16

        >>> (df * -1).pandas_on_spark.apply_batch(abs)
           A  B
        0  1  2
        1  3  4
        2  5  6

        '''
    def transform_batch(self, func: Callable[..., pd.DataFrame | pd.Series], *args: Any, **kwargs: Any) -> DataFrameOrSeries:
        '''
        Transform chunks with a function that takes pandas DataFrame and outputs pandas DataFrame.
        The pandas DataFrame given to the function is of a batch used internally. The length of
        each input and output should be the same.

        See also `Transform and apply a function
        <https://spark.apache.org/docs/latest/api/python/user_guide/pandas_on_spark/transform_apply.html>`_.

        .. note:: the `func` is unable to access the whole input frame. pandas-on-Spark
            internally splits the input series into multiple batches and calls `func` with each
            batch multiple times. Therefore, operations such as global aggregations are impossible.
            See the example below.

            >>> # This case does not return the length of whole frame but of the batch internally
            ... # used.
            ... def length(pdf) -> ps.DataFrame[int]:
            ...     return pd.DataFrame([len(pdf)] * len(pdf))
            ...
            >>> df = ps.DataFrame({\'A\': range(1000)})
            >>> df.pandas_on_spark.transform_batch(length)  # doctest: +SKIP
                c0
            0   83
            1   83
            2   83
            ...

        .. note:: this API executes the function once to infer the type which is
            potentially expensive, for instance, when the dataset is created after
            aggregations or sorting.

            To avoid this, specify return type in ``func``, for instance, as below:

            >>> def plus_one(x) -> ps.DataFrame[int, [float, float]]:
            ...     return x + 1

            If the return type is specified, the output column names become
            `c0, c1, c2 ... cn`. These names are positionally mapped to the returned
            DataFrame in ``func``.

            To specify the column names, you can assign them in a NumPy compound type style
            as below:

            >>> def plus_one(x) -> ps.DataFrame[("index", int), [("a", float), ("b", float)]]:
            ...     return x + 1

            >>> pdf = pd.DataFrame({\'a\': [1, 2, 3], \'b\': [3, 4, 5]})
            >>> def plus_one(x) -> ps.DataFrame[
            ...         (pdf.index.name, pdf.index.dtype), zip(pdf.dtypes, pdf.columns)]:
            ...     return x + 1

        Parameters
        ----------
        func : function
            Function to transform each pandas frame.
        *args
            Positional arguments to pass to func.
        **kwargs
            Keyword arguments to pass to func.

        Returns
        -------
        DataFrame or Series

        See Also
        --------
        DataFrame.pandas_on_spark.apply_batch: For row/columnwise operations.
        Series.pandas_on_spark.transform_batch: transform the search as each pandas chunks.

        Examples
        --------
        >>> df = ps.DataFrame([(1, 2), (3, 4), (5, 6)], columns=[\'A\', \'B\'])
        >>> df
           A  B
        0  1  2
        1  3  4
        2  5  6

        >>> def plus_one_func(pdf) -> ps.DataFrame[int, [int, int]]:
        ...     return pdf + 1
        >>> df.pandas_on_spark.transform_batch(plus_one_func)
           c0  c1
        0   2   3
        1   4   5
        2   6   7

        >>> def plus_one_func(pdf) -> ps.DataFrame[("index", int), [(\'A\', int), (\'B\', int)]]:
        ...     return pdf + 1
        >>> df.pandas_on_spark.transform_batch(plus_one_func)  # doctest: +NORMALIZE_WHITESPACE
               A  B
        index
        0      2  3
        1      4  5
        2      6  7

        >>> def plus_one_func(pdf) -> ps.Series[int]:
        ...     return pdf.B + 1
        >>> df.pandas_on_spark.transform_batch(plus_one_func)
        0    3
        1    5
        2    7
        dtype: int64

        You can also omit the type hints so pandas-on-Spark infers the return schema as below:

        >>> df.pandas_on_spark.transform_batch(lambda pdf: pdf + 1)
           A  B
        0  2  3
        1  4  5
        2  6  7

        >>> (df * -1).pandas_on_spark.transform_batch(abs)
           A  B
        0  1  2
        1  3  4
        2  5  6

        Note that you should not transform the index. The index information will not change.

        >>> df.pandas_on_spark.transform_batch(lambda pdf: pdf.B + 1)
        0    3
        1    5
        2    7
        Name: B, dtype: int64

        You can also specify extra arguments as below.

        >>> df.pandas_on_spark.transform_batch(lambda pdf, a, b, c: pdf.B + a + b + c, 1, 2, c=3)
        0     8
        1    10
        2    12
        Name: B, dtype: int64
        '''

class PandasOnSparkSeriesMethods:
    """pandas-on-Spark specific features for Series."""
    def __init__(self, series: Series) -> None: ...
    def transform_batch(self, func: Callable[..., pd.Series], *args: Any, **kwargs: Any) -> Series:
        """
        Transform the data with the function that takes pandas Series and outputs pandas Series.
        The pandas Series given to the function is of a batch used internally.

        See also `Transform and apply a function
        <https://spark.apache.org/docs/latest/api/python/user_guide/pandas_on_spark/transform_apply.html>`_.

        .. note:: the `func` is unable to access the whole input series. pandas-on-Spark
            internally splits the input series into multiple batches and calls `func` with each
            batch multiple times. Therefore, operations such as global aggregations are impossible.
            See the example below.

            >>> # This case does not return the length of whole frame but of the batch internally
            ... # used.
            ... def length(pser) -> ps.Series[int]:
            ...     return pd.Series([len(pser)] * len(pser))
            ...
            >>> df = ps.DataFrame({'A': range(1000)})
            >>> df.A.pandas_on_spark.transform_batch(length)  # doctest: +SKIP
                c0
            0   83
            1   83
            2   83
            ...

        .. note:: this API executes the function once to infer the type which is
            potentially expensive, for instance, when the dataset is created after
            aggregations or sorting.

            To avoid this, specify return type in ``func``, for instance, as below:

            >>> def plus_one(x) -> ps.Series[int]:
            ...     return x + 1

        Parameters
        ----------
        func : function
            Function to apply to each pandas frame.
        *args
            Positional arguments to pass to func.
        **kwargs
            Keyword arguments to pass to func.

        Returns
        -------
        DataFrame

        See Also
        --------
        DataFrame.pandas_on_spark.apply_batch : Similar but it takes pandas DataFrame as its
            internal batch.

        Examples
        --------
        >>> df = ps.DataFrame([(1, 2), (3, 4), (5, 6)], columns=['A', 'B'])
        >>> df
           A  B
        0  1  2
        1  3  4
        2  5  6

        >>> def plus_one_func(pser) -> ps.Series[np.int64]:
        ...     return pser + 1
        >>> df.A.pandas_on_spark.transform_batch(plus_one_func)
        0    2
        1    4
        2    6
        Name: A, dtype: int64

        You can also omit the type hints so pandas-on-Spark infers the return schema as below:

        >>> df.A.pandas_on_spark.transform_batch(lambda pser: pser + 1)
        0    2
        1    4
        2    6
        Name: A, dtype: int64

        You can also specify extra arguments.

        >>> def plus_one_func(pser, a, b, c=3) -> ps.Series[np.int64]:
        ...     return pser + a + b + c
        >>> df.A.pandas_on_spark.transform_batch(plus_one_func, 1, b=2)
        0     7
        1     9
        2    11
        Name: A, dtype: int64

        You can also use ``np.ufunc`` and built-in functions as input.

        >>> df.A.pandas_on_spark.transform_batch(np.add, 10)
        0    11
        1    13
        2    15
        Name: A, dtype: int64

        >>> (df * -1).A.pandas_on_spark.transform_batch(abs)
        0    1
        1    3
        2    5
        Name: A, dtype: int64
        """
