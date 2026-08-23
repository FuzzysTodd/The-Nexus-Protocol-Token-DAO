import numpy as np
import pandas as pd
from abc import ABCMeta, abstractmethod
from pyspark.pandas._typing import Axis as Axis, DataFrameOrSeries as DataFrameOrSeries, Dtype as Dtype, FrameLike as FrameLike, Label as Label, Name as Name, Scalar as Scalar
from pyspark.pandas.frame import DataFrame as DataFrame
from pyspark.pandas.groupby import GroupBy as GroupBy
from pyspark.pandas.indexes.base import Index as Index
from pyspark.pandas.indexing import AtIndexer as AtIndexer, LocIndexer as LocIndexer, iAtIndexer as iAtIndexer, iLocIndexer as iLocIndexer
from pyspark.pandas.internal import InternalFrame as InternalFrame
from pyspark.pandas.series import Series as Series
from pyspark.pandas.typedef import spark_type_to_pandas_dtype as spark_type_to_pandas_dtype
from pyspark.pandas.utils import SPARK_CONF_ARROW_ENABLED as SPARK_CONF_ARROW_ENABLED, is_name_like_tuple as is_name_like_tuple, is_name_like_value as is_name_like_value, log_advice as log_advice, name_like_string as name_like_string, scol_for as scol_for, sql_conf as sql_conf, validate_arguments_and_invoke_function as validate_arguments_and_invoke_function, validate_axis as validate_axis, validate_mode as validate_mode
from pyspark.pandas.window import Expanding as Expanding, ExponentialMoving as ExponentialMoving, Rolling as Rolling
from pyspark.sql import Column as Column
from pyspark.sql.types import BooleanType as BooleanType, DoubleType as DoubleType, LongType as LongType, NumericType as NumericType
from typing import Any, Callable, IO, List, NoReturn, Tuple

bool_type = bool

class Frame(metaclass=ABCMeta):
    """
    The base class for both DataFrame and Series.
    """
    @abstractmethod
    def __getitem__(self, key: Any) -> Any: ...
    @property
    @abstractmethod
    def dtypes(self) -> pd.Series | Dtype: ...
    @abstractmethod
    def to_pandas(self) -> pd.DataFrame | pd.Series: ...
    @property
    @abstractmethod
    def index(self) -> Index: ...
    @abstractmethod
    def copy(self) -> FrameLike: ...
    @abstractmethod
    def head(self, n: int = 5) -> FrameLike: ...
    def cummin(self, skipna: bool = True) -> FrameLike:
        """
        Return cumulative minimum over a DataFrame or Series axis.

        Returns a DataFrame or Series of the same size containing the cumulative minimum.

        .. note:: the current implementation of cummin uses Spark's Window without
            specifying partition specification. This leads to moveing all data into a
            single partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

        Parameters
        ----------
        skipna: boolean, default True
            Exclude NA/null values. If an entire row/column is NA, the result will be NA.

        Returns
        -------
        DataFrame or Series

        See Also
        --------
        DataFrame.min: Return the minimum over DataFrame axis.
        DataFrame.cummax: Return cumulative maximum over DataFrame axis.
        DataFrame.cummin: Return cumulative minimum over DataFrame axis.
        DataFrame.cumsum: Return cumulative sum over DataFrame axis.
        Series.min: Return the minimum over Series axis.
        Series.cummax: Return cumulative maximum over Series axis.
        Series.cummin: Return cumulative minimum over Series axis.
        Series.cumsum: Return cumulative sum over Series axis.
        Series.cumprod: Return cumulative product over Series axis.

        Examples
        --------
        >>> df = ps.DataFrame([[2.0, 1.0], [3.0, None], [1.0, 0.0]], columns=list('AB'))
        >>> df
             A    B
        0  2.0  1.0
        1  3.0  NaN
        2  1.0  0.0

        By default, iterates over rows and finds the minimum in each column.

        >>> df.cummin()
             A    B
        0  2.0  1.0
        1  2.0  NaN
        2  1.0  0.0

        It works identically in Series.

        >>> df.A.cummin()
        0    2.0
        1    2.0
        2    1.0
        Name: A, dtype: float64
        """
    def cummax(self, skipna: bool = True) -> FrameLike:
        """
        Return cumulative maximum over a DataFrame or Series axis.

        Returns a DataFrame or Series of the same size containing the cumulative maximum.

        .. note:: the current implementation of cummax uses Spark's Window without
            specifying partition specification. This leads to moveing all data into a
            single partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

        Parameters
        ----------
        skipna: boolean, default True
            Exclude NA/null values. If an entire row/column is NA, the result will be NA.

        Returns
        -------
        DataFrame or Series

        See Also
        --------
        DataFrame.max: Return the maximum over DataFrame axis.
        DataFrame.cummax: Return cumulative maximum over DataFrame axis.
        DataFrame.cummin: Return cumulative minimum over DataFrame axis.
        DataFrame.cumsum: Return cumulative sum over DataFrame axis.
        DataFrame.cumprod: Return cumulative product over DataFrame axis.
        Series.max: Return the maximum over Series axis.
        Series.cummax: Return cumulative maximum over Series axis.
        Series.cummin: Return cumulative minimum over Series axis.
        Series.cumsum: Return cumulative sum over Series axis.
        Series.cumprod: Return cumulative product over Series axis.

        Examples
        --------
        >>> df = ps.DataFrame([[2.0, 1.0], [3.0, None], [1.0, 0.0]], columns=list('AB'))
        >>> df
             A    B
        0  2.0  1.0
        1  3.0  NaN
        2  1.0  0.0

        By default, iterates over rows and finds the maximum in each column.

        >>> df.cummax()
             A    B
        0  2.0  1.0
        1  3.0  NaN
        2  3.0  1.0

        It works identically in Series.

        >>> df.B.cummax()
        0    1.0
        1    NaN
        2    1.0
        Name: B, dtype: float64
        """
    def cumsum(self, skipna: bool = True) -> FrameLike:
        """
        Return cumulative sum over a DataFrame or Series axis.

        Returns a DataFrame or Series of the same size containing the cumulative sum.

        .. note:: the current implementation of cumsum uses Spark's Window without
            specifying partition specification. This leads to moveing all data into a
            single partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

        Parameters
        ----------
        skipna: boolean, default True
            Exclude NA/null values. If an entire row/column is NA, the result will be NA.

        Returns
        -------
        DataFrame or Series

        See Also
        --------
        DataFrame.sum: Return the sum over DataFrame axis.
        DataFrame.cummax: Return cumulative maximum over DataFrame axis.
        DataFrame.cummin: Return cumulative minimum over DataFrame axis.
        DataFrame.cumsum: Return cumulative sum over DataFrame axis.
        DataFrame.cumprod: Return cumulative product over DataFrame axis.
        Series.sum: Return the sum over Series axis.
        Series.cummax: Return cumulative maximum over Series axis.
        Series.cummin: Return cumulative minimum over Series axis.
        Series.cumsum: Return cumulative sum over Series axis.
        Series.cumprod: Return cumulative product over Series axis.

        Examples
        --------
        >>> df = ps.DataFrame([[2.0, 1.0], [3.0, None], [1.0, 0.0]], columns=list('AB'))
        >>> df
             A    B
        0  2.0  1.0
        1  3.0  NaN
        2  1.0  0.0

        By default, iterates over rows and finds the sum in each column.

        >>> df.cumsum()
             A    B
        0  2.0  1.0
        1  5.0  NaN
        2  6.0  1.0

        It works identically in Series.

        >>> df.A.cumsum()
        0    2.0
        1    5.0
        2    6.0
        Name: A, dtype: float64
        """
    def cumprod(self, skipna: bool = True) -> FrameLike:
        """
        Return cumulative product over a DataFrame or Series axis.

        Returns a DataFrame or Series of the same size containing the cumulative product.

        .. note:: the current implementation of cumprod uses Spark's Window without
            specifying partition specification. This leads to moveing all data into a
            single partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

        .. note:: unlike pandas', pandas-on-Spark's emulates cumulative product by
            ``exp(sum(log(...)))`` trick. Therefore, it only works for positive numbers.

        Parameters
        ----------
        skipna: boolean, default True
            Exclude NA/null values. If an entire row/column is NA, the result will be NA.

        Returns
        -------
        DataFrame or Series

        See Also
        --------
        DataFrame.cummax: Return cumulative maximum over DataFrame axis.
        DataFrame.cummin: Return cumulative minimum over DataFrame axis.
        DataFrame.cumsum: Return cumulative sum over DataFrame axis.
        DataFrame.cumprod: Return cumulative product over DataFrame axis.
        Series.cummax: Return cumulative maximum over Series axis.
        Series.cummin: Return cumulative minimum over Series axis.
        Series.cumsum: Return cumulative sum over Series axis.
        Series.cumprod: Return cumulative product over Series axis.

        Raises
        ------
        Exception: If the values is equal to or lower than 0.

        Examples
        --------
        >>> df = ps.DataFrame([[2.0, 1.0], [3.0, None], [4.0, 10.0]], columns=list('AB'))
        >>> df
             A     B
        0  2.0   1.0
        1  3.0   NaN
        2  4.0  10.0

        By default, iterates over rows and finds the sum in each column.

        >>> df.cumprod()
              A     B
        0   2.0   1.0
        1   6.0   NaN
        2  24.0  10.0

        It works identically in Series.

        >>> df.A.cumprod()
        0     2.0
        1     6.0
        2    24.0
        Name: A, dtype: float64
        """
    def get_dtype_counts(self) -> pd.Series:
        """
        Return counts of unique dtypes in this object.

        .. deprecated:: 0.14.0

        Returns
        -------
        dtype: pd.Series
            Series with the count of columns with each dtype.

        See Also
        --------
        dtypes: Return the dtypes in this object.

        Examples
        --------
        >>> a = [['a', 1, 1], ['b', 2, 2], ['c', 3, 3]]
        >>> df = ps.DataFrame(a, columns=['str', 'int1', 'int2'])
        >>> df
          str  int1  int2
        0   a     1     1
        1   b     2     2
        2   c     3     3

        >>> df.get_dtype_counts().sort_values()
        object    1
        int64     2
        dtype: int64

        >>> df.str.get_dtype_counts().sort_values()
        object    1
        dtype: int64
        """
    def pipe(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        '''
        Apply func(self, \\*args, \\*\\*kwargs).

        Parameters
        ----------
        func: function
            function to apply to the DataFrame.
            ``args``, and ``kwargs`` are passed into ``func``.
            Alternatively a ``(callable, data_keyword)`` tuple where
            ``data_keyword`` is a string indicating the keyword of
            ``callable`` that expects the DataFrames.
        args: iterable, optional
            positional arguments passed into ``func``.
        kwargs: mapping, optional
            a dictionary of keyword arguments passed into ``func``.

        Returns
        -------
        object: the return type of ``func``.

        Notes
        -----
        Use ``.pipe`` when chaining together functions that expect
        Series, DataFrames or GroupBy objects. For example, given

        >>> df = ps.DataFrame({\'category\': [\'A\', \'A\', \'B\'],
        ...                    \'col1\': [1, 2, 3],
        ...                    \'col2\': [4, 5, 6]},
        ...                   columns=[\'category\', \'col1\', \'col2\'])
        >>> def keep_category_a(df):
        ...     return df[df[\'category\'] == \'A\']
        >>> def add_one(df, column):
        ...     return df.assign(col3=df[column] + 1)
        >>> def multiply(df, column1, column2):
        ...     return df.assign(col4=df[column1] * df[column2])


        instead of writing

        >>> multiply(add_one(keep_category_a(df), column="col1"), column1="col2", column2="col3")
          category  col1  col2  col3  col4
        0        A     1     4     2     8
        1        A     2     5     3    15


        You can write

        >>> (df.pipe(keep_category_a)
        ...    .pipe(add_one, column="col1")
        ...    .pipe(multiply, column1="col2", column2="col3")
        ... )
          category  col1  col2  col3  col4
        0        A     1     4     2     8
        1        A     2     5     3    15


        If you have a function that takes the data as the second
        argument, pass a tuple indicating which keyword expects the
        data. For example, suppose ``f`` takes its data as ``df``:

        >>> def multiply_2(column1, df, column2):
        ...     return df.assign(col4=df[column1] * df[column2])


        Then you can write

        >>> (df.pipe(keep_category_a)
        ...    .pipe(add_one, column="col1")
        ...    .pipe((multiply_2, \'df\'), column1="col2", column2="col3")
        ... )
          category  col1  col2  col3  col4
        0        A     1     4     2     8
        1        A     2     5     3    15

        You can use lambda as well

        >>> ps.Series([1, 2, 3]).pipe(lambda x: (x + 1).rename("value"))
        0    2
        1    3
        2    4
        Name: value, dtype: int64
        '''
    def to_numpy(self) -> np.ndarray:
        '''
        A NumPy ndarray representing the values in this DataFrame or Series.

        .. note:: This method should only be used if the resulting NumPy ndarray is expected
            to be small, as all the data is loaded into the driver\'s memory.

        Returns
        -------
        numpy.ndarray

        Examples
        --------
        >>> ps.DataFrame({"A": [1, 2], "B": [3, 4]}).to_numpy()
        array([[1, 3],
               [2, 4]])

        With heterogeneous data, the lowest common type will have to be used.

        >>> ps.DataFrame({"A": [1, 2], "B": [3.0, 4.5]}).to_numpy()
        array([[1. , 3. ],
               [2. , 4.5]])

        For a mix of numeric and non-numeric types, the output array will have object dtype.

        >>> df = ps.DataFrame({"A": [1, 2], "B": [3.0, 4.5], "C": pd.date_range(\'2000\', periods=2)})
        >>> df.to_numpy()
        array([[1, 3.0, Timestamp(\'2000-01-01 00:00:00\')],
               [2, 4.5, Timestamp(\'2000-01-02 00:00:00\')]], dtype=object)

        For Series,

        >>> ps.Series([\'a\', \'b\', \'a\']).to_numpy()
        array([\'a\', \'b\', \'a\'], dtype=object)
        '''
    @property
    def values(self) -> np.ndarray:
        """
        Return a Numpy representation of the DataFrame or the Series.

        .. warning:: We recommend using `DataFrame.to_numpy()` or `Series.to_numpy()` instead.

        .. note:: This method should only be used if the resulting NumPy ndarray is expected
            to be small, as all the data is loaded into the driver's memory.

        Returns
        -------
        numpy.ndarray

        Examples
        --------
        A DataFrame where all columns are the same type (e.g., int64) results in an array of
        the same type.

        >>> df = ps.DataFrame({'age':    [ 3,  29],
        ...                    'height': [94, 170],
        ...                    'weight': [31, 115]})
        >>> df
           age  height  weight
        0    3      94      31
        1   29     170     115
        >>> df.dtypes
        age       int64
        height    int64
        weight    int64
        dtype: object
        >>> df.values
        array([[  3,  94,  31],
               [ 29, 170, 115]])

        A DataFrame with mixed type columns(e.g., str/object, int64, float32) results in an ndarray
        of the broadest type that accommodates these mixed types (e.g., object).

        >>> df2 = ps.DataFrame([('parrot',   24.0, 'second'),
        ...                     ('lion',     80.5, 'first'),
        ...                     ('monkey', np.nan, None)],
        ...                   columns=('name', 'max_speed', 'rank'))
        >>> df2.dtypes
        name          object
        max_speed    float64
        rank          object
        dtype: object
        >>> df2.values
        array([['parrot', 24.0, 'second'],
               ['lion', 80.5, 'first'],
               ['monkey', nan, None]], dtype=object)

        For Series,

        >>> ps.Series([1, 2, 3]).values
        array([1, 2, 3])

        >>> ps.Series(list('aabc')).values
        array(['a', 'a', 'b', 'c'], dtype=object)
        """
    def to_csv(self, path: str | None = None, sep: str = ',', na_rep: str = '', columns: List[Name] | None = None, header: bool = True, quotechar: str = '"', date_format: str | None = None, escapechar: str | None = None, num_files: int | None = None, mode: str = 'w', partition_cols: str | List[str] | None = None, index_col: str | List[str] | None = None, **options: Any) -> str | None:
        '''
        Write object to a comma-separated values (csv) file.

        .. note:: pandas-on-Spark `to_csv` writes files to a path or URI. Unlike pandas\',
            pandas-on-Spark respects HDFS\'s property such as \'fs.default.name\'.

        .. note:: pandas-on-Spark writes CSV files into the directory, `path`, and writes
            multiple `part-...` files in the directory when `path` is specified.
            This behavior was inherited from Apache Spark. The number of partitions can
            be controlled by `num_files`. This is deprecated.
            Use `DataFrame.spark.repartition` instead.

        Parameters
        ----------
        path: str, default None
            File path. If None is provided the result is returned as a string.
        sep: str, default \',\'
            String of length 1. Field delimiter for the output file.
        na_rep: str, default \'\'
            Missing data representation.
        columns: sequence, optional
            Columns to write.
        header: bool or list of str, default True
            Write out the column names. If a list of strings is given it is
            assumed to be aliases for the column names.
        quotechar: str, default \'\\"\'
            String of length 1. Character used to quote fields.
        date_format: str, default None
            Format string for datetime objects.
        escapechar: str, default None
            String of length 1. Character used to escape `sep` and `quotechar`
            when appropriate.
        num_files: the number of partitions to be written in `path` directory when
            this is a path. This is deprecated. Use `DataFrame.spark.repartition` instead.
        mode: str
            Python write mode, default \'w\'.

            .. note:: mode can accept the strings for Spark writing mode.
                Such as \'append\', \'overwrite\', \'ignore\', \'error\', \'errorifexists\'.

                - \'append\' (equivalent to \'a\'): Append the new data to existing data.
                - \'overwrite\' (equivalent to \'w\'): Overwrite existing data.
                - \'ignore\': Silently ignore this operation if data already exists.
                - \'error\' or \'errorifexists\': Throw an exception if data already exists.

        partition_cols: str or list of str, optional, default None
            Names of partitioning columns
        index_col: str or list of str, optional, default: None
            Column names to be used in Spark to represent pandas-on-Spark\'s index. The index name
            in pandas-on-Spark is ignored. By default, the index is always lost.
        options: keyword arguments for additional options specific to PySpark.
            These kwargs are specific to PySpark\'s CSV options to pass. Check
            the options in PySpark\'s API documentation for spark.write.csv(...).
            It has higher priority and overwrites all other options.
            This parameter only works when `path` is specified.

        Returns
        -------
        str or None

        See Also
        --------
        read_csv
        DataFrame.to_delta
        DataFrame.to_table
        DataFrame.to_parquet
        DataFrame.to_spark_io

        Examples
        --------
        >>> df = ps.DataFrame(dict(
        ...    date=list(pd.date_range(\'2012-1-1 12:00:00\', periods=3, freq=\'M\')),
        ...    country=[\'KR\', \'US\', \'JP\'],
        ...    code=[1, 2 ,3]), columns=[\'date\', \'country\', \'code\'])
        >>> df.sort_values(by="date")  # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
                           date country  code
        ... 2012-01-31 12:00:00      KR     1
        ... 2012-02-29 12:00:00      US     2
        ... 2012-03-31 12:00:00      JP     3

        >>> print(df.to_csv())  # doctest: +NORMALIZE_WHITESPACE
        date,country,code
        2012-01-31 12:00:00,KR,1
        2012-02-29 12:00:00,US,2
        2012-03-31 12:00:00,JP,3

        >>> df.cummax().to_csv(path=r\'%s/to_csv/foo.csv\' % path, num_files=1)
        >>> ps.read_csv(
        ...    path=r\'%s/to_csv/foo.csv\' % path
        ... ).sort_values(by="date")  # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
                           date country  code
        ... 2012-01-31 12:00:00      KR     1
        ... 2012-02-29 12:00:00      US     2
        ... 2012-03-31 12:00:00      US     3

        In case of Series,

        >>> print(df.date.to_csv())  # doctest: +NORMALIZE_WHITESPACE
        date
        2012-01-31 12:00:00
        2012-02-29 12:00:00
        2012-03-31 12:00:00

        >>> df.date.to_csv(path=r\'%s/to_csv/foo.csv\' % path, num_files=1)
        >>> ps.read_csv(
        ...     path=r\'%s/to_csv/foo.csv\' % path
        ... ).sort_values(by="date")  # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
                           date
        ... 2012-01-31 12:00:00
        ... 2012-02-29 12:00:00
        ... 2012-03-31 12:00:00

        You can preserve the index in the roundtrip as below.

        >>> df.set_index("country", append=True, inplace=True)
        >>> df.date.to_csv(
        ...     path=r\'%s/to_csv/bar.csv\' % path,
        ...     num_files=1,
        ...     index_col=["index1", "index2"])
        >>> ps.read_csv(
        ...     path=r\'%s/to_csv/bar.csv\' % path, index_col=["index1", "index2"]
        ... ).sort_values(by="date")  # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
                                     date
        index1 index2
        ...    ...    2012-01-31 12:00:00
        ...    ...    2012-02-29 12:00:00
        ...    ...    2012-03-31 12:00:00
        '''
    def to_json(self, path: str | None = None, compression: str = 'uncompressed', num_files: int | None = None, mode: str = 'w', orient: str = 'records', lines: bool = True, partition_cols: str | List[str] | None = None, index_col: str | List[str] | None = None, **options: Any) -> str | None:
        '''
        Convert the object to a JSON string.

        .. note:: pandas-on-Spark `to_json` writes files to a path or URI. Unlike pandas\',
            pandas-on-Spark respects HDFS\'s property such as \'fs.default.name\'.

        .. note:: pandas-on-Spark writes JSON files into the directory, `path`, and writes
            multiple `part-...` files in the directory when `path` is specified.
            This behavior was inherited from Apache Spark. The number of partitions can
            be controlled by `num_files`. This is deprecated.
            Use `DataFrame.spark.repartition` instead.

        .. note:: output JSON format is different from pandas\'. It always uses `orient=\'records\'`
            for its output. This behavior might have to change soon.

        .. note:: Set `ignoreNullFields` keyword argument to `True` to omit `None` or `NaN` values
            when writing JSON objects. It works only when `path` is provided.

        Note NaN\'s and None will be converted to null and datetime objects
        will be converted to UNIX timestamps.

        Parameters
        ----------
        path: string, optional
            File path. If not specified, the result is returned as
            a string.
        lines: bool, default True
            If ‘orient’ is ‘records’ write out line delimited JSON format.
            Will throw ValueError if incorrect ‘orient’ since others are not
            list like. It should be always True for now.
        orient: str, default \'records\'
             It should be always \'records\' for now.
        compression: {\'gzip\', \'bz2\', \'xz\', None}
            A string representing the compression to use in the output file,
            only used when the first argument is a filename. By default, the
            compression is inferred from the filename.
        num_files: the number of partitions to be written in `path` directory when
            this is a path. This is deprecated. Use `DataFrame.spark.repartition` instead.
        mode: str
            Python write mode, default \'w\'.

            .. note:: mode can accept the strings for Spark writing mode.
                Such as \'append\', \'overwrite\', \'ignore\', \'error\', \'errorifexists\'.

                - \'append\' (equivalent to \'a\'): Append the new data to existing data.
                - \'overwrite\' (equivalent to \'w\'): Overwrite existing data.
                - \'ignore\': Silently ignore this operation if data already exists.
                - \'error\' or \'errorifexists\': Throw an exception if data already exists.

        partition_cols: str or list of str, optional, default None
            Names of partitioning columns
        index_col: str or list of str, optional, default: None
            Column names to be used in Spark to represent pandas-on-Spark\'s index. The index name
            in pandas-on-Spark is ignored. By default, the index is always lost.
        options: keyword arguments for additional options specific to PySpark.
            It is specific to PySpark\'s JSON options to pass. Check
            the options in PySpark\'s API documentation for `spark.write.json(...)`.
            It has a higher priority and overwrites all other options.
            This parameter only works when `path` is specified.

        Returns
        -------
        str or None

        Examples
        --------
        >>> df = ps.DataFrame([[\'a\', \'b\'], [\'c\', \'d\']],
        ...                   columns=[\'col 1\', \'col 2\'])
        >>> df.to_json()
        \'[{"col 1":"a","col 2":"b"},{"col 1":"c","col 2":"d"}]\'

        >>> df[\'col 1\'].to_json()
        \'[{"col 1":"a"},{"col 1":"c"}]\'

        >>> df.to_json(path=r\'%s/to_json/foo.json\' % path, num_files=1)
        >>> ps.read_json(
        ...     path=r\'%s/to_json/foo.json\' % path
        ... ).sort_values(by="col 1")
          col 1 col 2
        0     a     b
        1     c     d

        >>> df[\'col 1\'].to_json(path=r\'%s/to_json/foo.json\' % path, num_files=1, index_col="index")
        >>> ps.read_json(
        ...     path=r\'%s/to_json/foo.json\' % path, index_col="index"
        ... ).sort_values(by="col 1")  # doctest: +NORMALIZE_WHITESPACE
              col 1
        index
        0         a
        1         c
        '''
    def to_excel(self, excel_writer: str | pd.ExcelWriter, sheet_name: str = 'Sheet1', na_rep: str = '', float_format: str | None = None, columns: str | List[str] | None = None, header: bool = True, index: bool = True, index_label: str | List[str] | None = None, startrow: int = 0, startcol: int = 0, engine: str | None = None, merge_cells: bool = True, encoding: str | None = None, inf_rep: str = 'inf', verbose: bool = True, freeze_panes: Tuple[int, int] | None = None) -> None:
        '''
        Write object to an Excel sheet.

        .. note:: This method should only be used if the resulting DataFrame is expected
                  to be small, as all the data is loaded into the driver\'s memory.

        To write a single object to an Excel .xlsx file it is only necessary to
        specify a target file name. To write to multiple sheets it is necessary to
        create an `ExcelWriter` object with a target file name, and specify a sheet
        in the file to write to.

        Multiple sheets may be written to by specifying unique `sheet_name`.
        With all data written to the file it is necessary to save the changes.
        Note that creating an `ExcelWriter` object with a file name that already
        exists will result in the contents of the existing file being erased.

        Parameters
        ----------
        excel_writer: str or ExcelWriter object
            File path or existing ExcelWriter.
        sheet_name: str, default \'Sheet1\'
            Name of sheet which will contain DataFrame.
        na_rep: str, default \'\'
            Missing data representation.
        float_format: str, optional
            Format string for floating point numbers. For example
            ``float_format="%%.2f"`` will format 0.1234 to 0.12.
        columns: sequence or list of str, optional
            Columns to write.
        header: bool or list of str, default True
            Write out the column names. If a list of string is given it is
            assumed to be aliases for the column names.
        index: bool, default True
            Write row names (index).
        index_label: str or sequence, optional
            Column label for index column(s) if desired. If not specified, and
            `header` and `index` are True, then the index names are used. A
            sequence should be given if the DataFrame uses MultiIndex.
        startrow: int, default 0
            Upper left cell row to dump data frame.
        startcol: int, default 0
            Upper left cell column to dump data frame.
        engine: str, optional
            Write engine to use, \'openpyxl\' or \'xlsxwriter\'. You can also set this
            via the options ``io.excel.xlsx.writer``, ``io.excel.xls.writer``, and
            ``io.excel.xlsm.writer``.
        merge_cells: bool, default True
            Write MultiIndex and Hierarchical Rows as merged cells.
        encoding: str, optional
            Encoding of the resulting excel file. Only necessary for xlwt,
            other writers support unicode natively.

            .. deprecated:: 3.4.0

        inf_rep: str, default \'inf\'
            Representation for infinity (there is no native representation for
            infinity in Excel).
        verbose: bool, default True
            Display more information in the error logs.

            .. deprecated:: 3.4.0

        freeze_panes: tuple of int (length 2), optional
            Specifies the one-based bottommost row and rightmost column that
            is to be frozen.

        Notes
        -----
        Once a workbook has been saved it is not possible write further data
        without rewriting the whole workbook.

        See Also
        --------
        read_excel: Read Excel file.

        Examples
        --------
        Create, write to, and save a workbook:

        >>> df1 = ps.DataFrame([[\'a\', \'b\'], [\'c\', \'d\']],
        ...                    index=[\'row 1\', \'row 2\'],
        ...                    columns=[\'col 1\', \'col 2\'])
        >>> df1.to_excel("output.xlsx")  # doctest: +SKIP

        To specify the sheet name:

        >>> df1.to_excel("output.xlsx")  # doctest: +SKIP
        >>> df1.to_excel("output.xlsx",
        ...              sheet_name=\'Sheet_name_1\')  # doctest: +SKIP

        If you wish to write to more than one sheet in the workbook, it is
        necessary to specify an ExcelWriter object:

        >>> with pd.ExcelWriter(\'output.xlsx\') as writer:  # doctest: +SKIP
        ...      df1.to_excel(writer, sheet_name=\'Sheet_name_1\')
        ...      df2.to_excel(writer, sheet_name=\'Sheet_name_2\')

        To set the library that is used to write the Excel file,
        you can pass the `engine` keyword (the default engine is
        automatically chosen depending on the file extension):

        >>> df1.to_excel(\'output1.xlsx\', engine=\'xlsxwriter\')  # doctest: +SKIP
        '''
    def mean(self, axis: Axis | None = None, skipna: bool = True, numeric_only: bool = None) -> Scalar | Series:
        """
        Return the mean of the values.

        Parameters
        ----------
        axis: {index (0), columns (1)}
            Axis for the function to be applied on.
        skipna: bool, default True
            Exclude NA/null values when computing the result.

            .. versionchanged:: 3.4.0
               Supported including NA/null values.
        numeric_only: bool, default None
            Include only float, int, boolean columns. False is not supported. This parameter
            is mainly for pandas compatibility.

        Returns
        -------
        mean: scalar for a Series, and a Series for a DataFrame.

        Examples
        --------

        >>> df = ps.DataFrame({'a': [1, 2, 3, np.nan], 'b': [0.1, 0.2, 0.3, np.nan]},
        ...                   columns=['a', 'b'])

        On a DataFrame:

        >>> df.mean()
        a    2.0
        b    0.2
        dtype: float64

        >>> df.mean(axis=1)
        0    0.55
        1    1.10
        2    1.65
        3     NaN
        dtype: float64

        On a Series:

        >>> df['a'].mean()
        2.0
        """
    def sum(self, axis: Axis | None = None, skipna: bool = True, numeric_only: bool = None, min_count: int = 0) -> Scalar | Series:
        """
        Return the sum of the values.

        Parameters
        ----------
        axis: {index (0), columns (1)}
            Axis for the function to be applied on.
        skipna: bool, default True
            Exclude NA/null values when computing the result.

            .. versionchanged:: 3.4.0
               Added *skipna* to exclude.
        numeric_only: bool, default None
            Include only float, int, boolean columns. False is not supported. This parameter
            is mainly for pandas compatibility.
        min_count: int, default 0
            The required number of valid values to perform the operation. If fewer than
             ``min_count`` non-NA values are present the result will be NA.

        Returns
        -------
        sum: scalar for a Series, and a Series for a DataFrame.

        Examples
        --------

        >>> df = ps.DataFrame({'a': [1, 2, 3, np.nan], 'b': [0.1, np.nan, 0.3, np.nan]},
        ...                   columns=['a', 'b'])

        On a DataFrame:

        >>> df.sum()
        a    6.0
        b    0.4
        dtype: float64

        >>> df.sum(axis=1)
        0    1.1
        1    2.0
        2    3.3
        3    0.0
        dtype: float64

        >>> df.sum(min_count=3)
        a    6.0
        b    NaN
        dtype: float64

        >>> df.sum(axis=1, min_count=1)
        0    1.1
        1    2.0
        2    3.3
        3    NaN
        dtype: float64

        On a Series:

        >>> df['a'].sum()
        6.0

        >>> df['a'].sum(min_count=3)
        6.0
        >>> df['b'].sum(min_count=3)
        nan
        """
    def product(self, axis: Axis | None = None, skipna: bool = True, numeric_only: bool = None, min_count: int = 0) -> Scalar | Series:
        '''
        Return the product of the values.

        .. note:: unlike pandas\', pandas-on-Spark\'s emulates product by ``exp(sum(log(...)))``
            trick. Therefore, it only works for positive numbers.

        Parameters
        ----------
        axis: {index (0), columns (1)}
            Axis for the function to be applied on.
        skipna: bool, default True
            Exclude NA/null values when computing the result.

            .. versionchanged:: 3.4.0
               Supported including NA/null values.
        numeric_only: bool, default None
            Include only float, int, boolean columns. False is not supported. This parameter
            is mainly for pandas compatibility.
        min_count: int, default 0
            The required number of valid values to perform the operation. If fewer than
            ``min_count`` non-NA values are present the result will be NA.

        Examples
        --------
        On a DataFrame:

        Non-numeric type column is not included to the result.

        >>> psdf = ps.DataFrame({\'A\': [1, 2, 3, 4, 5],
        ...                     \'B\': [10, 20, 30, 40, 50],
        ...                     \'C\': [\'a\', \'b\', \'c\', \'d\', \'e\']})
        >>> psdf
           A   B  C
        0  1  10  a
        1  2  20  b
        2  3  30  c
        3  4  40  d
        4  5  50  e

        >>> psdf.prod()
        A         120
        B    12000000
        dtype: int64

        If there is no numeric type columns, returns empty Series.

        >>> ps.DataFrame({"key": [\'a\', \'b\', \'c\'], "val": [\'x\', \'y\', \'z\']}).prod()
        Series([], dtype: float64)

        On a Series:

        >>> ps.Series([1, 2, 3, 4, 5]).prod()
        120

        By default, the product of an empty or all-NA Series is ``1``

        >>> ps.Series([]).prod()
        1.0

        This can be controlled with the ``min_count`` parameter

        >>> ps.Series([]).prod(min_count=1)
        nan
        '''
    prod = product
    def skew(self, axis: Axis | None = None, skipna: bool = True, numeric_only: bool = None) -> Scalar | Series:
        """
        Return unbiased skew normalized by N-1.

        Parameters
        ----------
        axis: {index (0), columns (1)}
            Axis for the function to be applied on.
        skipna: bool, default True
            Exclude NA/null values when computing the result.

            .. versionchanged:: 3.4.0
               Supported including NA/null values.
        numeric_only: bool, default None
            Include only float, int, boolean columns. False is not supported. This parameter
            is mainly for pandas compatibility.

        Returns
        -------
        skew: scalar for a Series, and a Series for a DataFrame.

        Examples
        --------

        >>> df = ps.DataFrame({'a': [1, 2, 3, np.nan], 'b': [0.1, 0.2, 0.3, np.nan]},
        ...                   columns=['a', 'b'])

        On a DataFrame:

        >>> df.skew()
        a    0.0
        b    0.0
        dtype: float64

        On a Series:

        >>> df['a'].skew()
        0.0
        """
    def kurtosis(self, axis: Axis | None = None, skipna: bool = True, numeric_only: bool = None) -> Scalar | Series:
        """
        Return unbiased kurtosis using Fisher’s definition of kurtosis (kurtosis of normal == 0.0).
        Normalized by N-1.

        Parameters
        ----------
        axis: {index (0), columns (1)}
            Axis for the function to be applied on.
        skipna: bool, default True
            Exclude NA/null values when computing the result.

            .. versionchanged:: 3.4.0
               Supported including NA/null values.
        numeric_only: bool, default None
            Include only float, int, boolean columns. False is not supported. This parameter
            is mainly for pandas compatibility.

        Returns
        -------
        kurt: scalar for a Series, and a Series for a DataFrame.

        Examples
        --------

        >>> df = ps.DataFrame({'a': [1, 2, 3, np.nan, 6], 'b': [0.1, 0.2, 0.3, np.nan, 0.8]},
        ...                   columns=['a', 'b'])

        On a DataFrame:

        >>> df.kurtosis()
        a    1.500000
        b    2.703924
        dtype: float64

        On a Series:

        >>> df['a'].kurtosis()
        1.5
        """
    kurt = kurtosis
    def min(self, axis: Axis | None = None, skipna: bool = True, numeric_only: bool = None) -> Scalar | Series:
        """
        Return the minimum of the values.

        Parameters
        ----------
        axis: {index (0), columns (1)}
            Axis for the function to be applied on.
        skipna: bool, default True
            Exclude NA/null values when computing the result.

            .. versionchanged:: 3.4.0
               Supported including NA/null values.
        numeric_only: bool, default None
            If True, include only float, int, boolean columns. This parameter is mainly for
            pandas compatibility. False is supported; however, the columns should
            be all numeric or all non-numeric.

        Returns
        -------
        min: scalar for a Series, and a Series for a DataFrame.

        Examples
        --------

        >>> df = ps.DataFrame({'a': [1, 2, 3, np.nan], 'b': [0.1, 0.2, 0.3, np.nan]},
        ...                   columns=['a', 'b'])

        On a DataFrame:

        >>> df.min()
        a    1.0
        b    0.1
        dtype: float64

        >>> df.min(axis=1)
        0    0.1
        1    0.2
        2    0.3
        3    NaN
        dtype: float64

        On a Series:

        >>> df['a'].min()
        1.0
        """
    def max(self, axis: Axis | None = None, skipna: bool = True, numeric_only: bool = None) -> Scalar | Series:
        """
        Return the maximum of the values.

        Parameters
        ----------
        axis: {index (0), columns (1)}
            Axis for the function to be applied on.
        skipna: bool, default True
            Exclude NA/null values when computing the result.

            .. versionchanged:: 3.4.0
               Supported including NA/null values.
        numeric_only: bool, default None
            If True, include only float, int, boolean columns. This parameter is mainly for
            pandas compatibility. False is supported; however, the columns should
            be all numeric or all non-numeric.

        Returns
        -------
        max: scalar for a Series, and a Series for a DataFrame.

        Examples
        --------

        >>> df = ps.DataFrame({'a': [1, 2, 3, np.nan], 'b': [0.1, 0.2, 0.3, np.nan]},
        ...                   columns=['a', 'b'])

        On a DataFrame:

        >>> df.max()
        a    3.0
        b    0.3
        dtype: float64

        >>> df.max(axis=1)
        0    1.0
        1    2.0
        2    3.0
        3    NaN
        dtype: float64

        On a Series:

        >>> df['a'].max()
        3.0
        """
    def count(self, axis: Axis | None = None, numeric_only: bool = False) -> Scalar | Series:
        '''
        Count non-NA cells for each column.

        The values `None`, `NaN` are considered NA.

        Parameters
        ----------
        axis: {0 or ‘index’, 1 or ‘columns’}, default 0
            If 0 or ‘index’ counts are generated for each column. If 1 or ‘columns’ counts are
            generated for each row.
        numeric_only: bool, default False
            If True, include only float, int, boolean columns. This parameter is mainly for
            pandas compatibility.

        Returns
        -------
        max: scalar for a Series, and a Series for a DataFrame.

        See Also
        --------
        DataFrame.shape: Number of DataFrame rows and columns (including NA
            elements).
        DataFrame.isna: Boolean same-sized DataFrame showing places of NA
            elements.

        Examples
        --------
        Constructing DataFrame from a dictionary:

        >>> df = ps.DataFrame({"Person":
        ...                    ["John", "Myla", "Lewis", "John", "Myla"],
        ...                    "Age": [24., np.nan, 21., 33, 26],
        ...                    "Single": [False, True, True, True, False]},
        ...                   columns=["Person", "Age", "Single"])
        >>> df
          Person   Age  Single
        0   John  24.0   False
        1   Myla   NaN    True
        2  Lewis  21.0    True
        3   John  33.0    True
        4   Myla  26.0   False

        Notice the uncounted NA values:

        >>> df.count()
        Person    5
        Age       4
        Single    5
        dtype: int64

        >>> df.count(axis=1)
        0    3
        1    2
        2    3
        3    3
        4    3
        dtype: int64

        On a Series:

        >>> df[\'Person\'].count()
        5

        >>> df[\'Age\'].count()
        4
        '''
    def std(self, axis: Axis | None = None, skipna: bool = True, ddof: int = 1, numeric_only: bool = None) -> Scalar | Series:
        """
        Return sample standard deviation.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        axis: {index (0), columns (1)}
            Axis for the function to be applied on.
        skipna: bool, default True
            Exclude NA/null values when computing the result.

            .. versionchanged:: 3.4.0
               Supported including NA/null values.
        ddof: int, default 1
            Delta Degrees of Freedom. The divisor used in calculations is N - ddof,
            where N represents the number of elements.

            .. versionchanged:: 3.4.0
               Supported including arbitary integers.
        numeric_only: bool, default None
            Include only float, int, boolean columns. False is not supported. This parameter
            is mainly for pandas compatibility.

        Returns
        -------
        std: scalar for a Series, and a Series for a DataFrame.

        Examples
        --------

        >>> df = ps.DataFrame({'a': [1, 2, 3, np.nan], 'b': [0.1, 0.2, 0.3, np.nan]},
        ...                   columns=['a', 'b'])

        On a DataFrame:

        >>> df.std()
        a    1.0
        b    0.1
        dtype: float64

        >>> df.std(ddof=2)
        a    1.414214
        b    0.141421
        dtype: float64

        >>> df.std(axis=1)
        0    0.636396
        1    1.272792
        2    1.909188
        3         NaN
        dtype: float64

        >>> df.std(ddof=0)
        a    0.816497
        b    0.081650
        dtype: float64

        On a Series:

        >>> df['a'].std()
        1.0

        >>> df['a'].std(ddof=0)
        0.816496580927726

        >>> df['a'].std(ddof=-1)
        0.707106...
        """
    def var(self, axis: Axis | None = None, ddof: int = 1, numeric_only: bool = None) -> Scalar | Series:
        """
        Return unbiased variance.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        axis: {index (0), columns (1)}
            Axis for the function to be applied on.
        ddof: int, default 1
            Delta Degrees of Freedom. The divisor used in calculations is N - ddof,
            where N represents the number of elements.

            .. versionchanged:: 3.4.0
               Supported including arbitary integers.
        numeric_only: bool, default None
            Include only float, int, boolean columns. False is not supported. This parameter
            is mainly for pandas compatibility.

        Returns
        -------
        var: scalar for a Series, and a Series for a DataFrame.

        Examples
        --------

        >>> df = ps.DataFrame({'a': [1, 2, 3, np.nan], 'b': [0.1, 0.2, 0.3, np.nan]},
        ...                   columns=['a', 'b'])

        On a DataFrame:

        >>> df.var()
        a    1.00
        b    0.01
        dtype: float64

        >>> df.var(ddof=2)
        a    2.00
        b    0.02
        dtype: float64

        >>> df.var(axis=1)
        0    0.405
        1    1.620
        2    3.645
        3      NaN
        dtype: float64

        >>> df.var(ddof=0)
        a    0.666667
        b    0.006667
        dtype: float64

        On a Series:

        >>> df['a'].var()
        1.0

        >>> df['a'].var(ddof=0)
        0.6666666666666666

        >>> df['a'].var(ddof=-2)
        0.4
        """
    def median(self, axis: Axis | None = None, skipna: bool = True, numeric_only: bool = None, accuracy: int = 10000) -> Scalar | Series:
        """
        Return the median of the values for the requested axis.

        .. note:: Unlike pandas', the median in pandas-on-Spark is an approximated median based upon
            approximate percentile computation because computing median across a large dataset
            is extremely expensive.

        Parameters
        ----------
        axis: {index (0), columns (1)}
            Axis for the function to be applied on.
        skipna: bool, default True
            Exclude NA/null values when computing the result.

            .. versionchanged:: 3.4.0
               Supported including NA/null values.
        numeric_only: bool, default None
            Include only float, int, boolean columns. False is not supported. This parameter
            is mainly for pandas compatibility.
        accuracy: int, optional
            Default accuracy of approximation. Larger value means better accuracy.
            The relative error can be deduced by 1.0 / accuracy.

        Returns
        -------
        median: scalar or Series

        Examples
        --------
        >>> df = ps.DataFrame({
        ...     'a': [24., 21., 25., 33., 26.], 'b': [1, 2, 3, 4, 5]}, columns=['a', 'b'])
        >>> df
              a  b
        0  24.0  1
        1  21.0  2
        2  25.0  3
        3  33.0  4
        4  26.0  5

        On a DataFrame:

        >>> df.median()
        a    25.0
        b     3.0
        dtype: float64

        On a Series:

        >>> df['a'].median()
        25.0
        >>> (df['b'] + 100).median()
        103.0

        For multi-index columns,

        >>> df.columns = pd.MultiIndex.from_tuples([('x', 'a'), ('y', 'b')])
        >>> df
              x  y
              a  b
        0  24.0  1
        1  21.0  2
        2  25.0  3
        3  33.0  4
        4  26.0  5

        On a DataFrame:

        >>> df.median()
        x  a    25.0
        y  b     3.0
        dtype: float64

        >>> df.median(axis=1)
        0    12.5
        1    11.5
        2    14.0
        3    18.5
        4    15.5
        dtype: float64

        On a Series:

        >>> df[('x', 'a')].median()
        25.0
        >>> (df[('y', 'b')] + 100).median()
        103.0
        """
    def sem(self, axis: Axis | None = None, skipna: bool = True, ddof: int = 1, numeric_only: bool = None) -> Scalar | Series:
        '''
        Return unbiased standard error of the mean over requested axis.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        axis: {index (0), columns (1)}
            Axis for the function to be applied on.
        skipna: bool, default True
            Exclude NA/null values when computing the result.

            .. versionchanged:: 3.4.0
               Supported including NA/null values.
        ddof: int, default 1
            Delta Degrees of Freedom. The divisor used in calculations is N - ddof,
            where N represents the number of elements.

            .. versionchanged:: 3.4.0
               Supported including arbitary integers.
        numeric_only: bool, default None
            Include only float, int, boolean columns. False is not supported. This parameter
            is mainly for pandas compatibility.

        Returns
        -------
        scalar(for Series) or Series(for DataFrame)

        Examples
        --------
        >>> psdf = ps.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
        >>> psdf
           a  b
        0  1  4
        1  2  5
        2  3  6

        >>> psdf.sem()
        a    0.57735
        b    0.57735
        dtype: float64

        >>> psdf.sem(ddof=0)
        a    0.471405
        b    0.471405
        dtype: float64

        >>> psdf.sem(ddof=2)
        a    0.816497
        b    0.816497
        dtype: float64

        >>> psdf.sem(axis=1)
        0    1.5
        1    1.5
        2    1.5
        dtype: float64

        Support for Series

        >>> psser = psdf.a
        >>> psser
        0    1
        1    2
        2    3
        Name: a, dtype: int64

        >>> psser.sem()
        0.5773502691896258

        >>> psser.sem(ddof=0)
        0.47140452079103173
        '''
    @property
    def size(self) -> int:
        """
        Return an int representing the number of elements in this object.

        Return the number of rows if Series. Otherwise return the number of
        rows times number of columns if DataFrame.

        Examples
        --------
        >>> s = ps.Series({'a': 1, 'b': 2, 'c': None})
        >>> s.size
        3

        >>> df = ps.DataFrame({'col1': [1, 2, None], 'col2': [3, 4, None]})
        >>> df.size
        6

        >>> df = ps.DataFrame(index=[1, 2, None])
        >>> df.size
        0
        """
    def abs(self) -> FrameLike:
        """
        Return a Series/DataFrame with absolute numeric value of each element.

        Returns
        -------
        abs: Series/DataFrame containing the absolute value of each element.

        Examples
        --------

        Absolute numeric values in a Series.

        >>> s = ps.Series([-1.10, 2, -3.33, 4])
        >>> s.abs()
        0    1.10
        1    2.00
        2    3.33
        3    4.00
        dtype: float64

        Absolute numeric values in a DataFrame.

        >>> df = ps.DataFrame({
        ...     'a': [4, 5, 6, 7],
        ...     'b': [10, 20, 30, 40],
        ...     'c': [100, 50, -30, -50]
        ...   },
        ...   columns=['a', 'b', 'c'])
        >>> df.abs()
           a   b    c
        0  4  10  100
        1  5  20   50
        2  6  30   30
        3  7  40   50
        """
    def groupby(self, by: Name | Series | List[Name | Series], axis: Axis = 0, as_index: bool = True, dropna: bool = True) -> GroupBy[FrameLike]:
        '''
        Group DataFrame or Series using one or more columns.

        A groupby operation involves some combination of splitting the
        object, applying a function, and combining the results. This can be
        used to group large amounts of data and compute operations on these
        groups.

        Parameters
        ----------
        by: Series, label, or list of labels
            Used to determine the groups for the groupby.
            If Series is passed, the Series or dict VALUES
            will be used to determine the groups. A label or list of
            labels may be passed to group by the columns in ``self``.
        axis: int, default 0 or \'index\'
            Can only be set to 0 now.
        as_index: bool, default True
            For aggregated output, return object with group labels as the
            index. Only relevant for DataFrame input. as_index=False is
            effectively "SQL-style" grouped output.
        dropna: bool, default True
            If True, and if group keys contain NA values,
            NA values together with row/column will be dropped.
            If False, NA values will also be treated as the key in groups.

        Returns
        -------
        DataFrameGroupBy or SeriesGroupBy
            Depends on the calling object and returns groupby object that
            contains information about the groups.

        See Also
        --------
        pyspark.pandas.groupby.GroupBy

        Examples
        --------
        >>> df = ps.DataFrame({\'Animal\': [\'Falcon\', \'Falcon\',
        ...                               \'Parrot\', \'Parrot\'],
        ...                    \'Max Speed\': [380., 370., 24., 26.]},
        ...                   columns=[\'Animal\', \'Max Speed\'])
        >>> df
           Animal  Max Speed
        0  Falcon      380.0
        1  Falcon      370.0
        2  Parrot       24.0
        3  Parrot       26.0

        >>> df.groupby([\'Animal\']).mean().sort_index()  # doctest: +NORMALIZE_WHITESPACE
                Max Speed
        Animal
        Falcon      375.0
        Parrot       25.0

        >>> df.groupby([\'Animal\'], as_index=False).mean().sort_values(\'Animal\')
        ... # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
           Animal  Max Speed
        ...Falcon      375.0
        ...Parrot       25.0

        We can also choose to include NA in group keys or not by setting dropna parameter,
        the default setting is True:

        >>> l = [[1, 2, 3], [1, None, 4], [2, 1, 3], [1, 2, 2]]
        >>> df = ps.DataFrame(l, columns=["a", "b", "c"])
        >>> df.groupby(by=["b"]).sum().sort_index()  # doctest: +NORMALIZE_WHITESPACE
             a  c
        b
        1.0  2  3
        2.0  2  5

        >>> df.groupby(by=["b"], dropna=False).sum().sort_index()  # doctest: +NORMALIZE_WHITESPACE
             a  c
        b
        1.0  2  3
        2.0  2  5
        NaN  1  4
        '''
    def bool(self) -> bool:
        """
        Return the bool of a single element in the current object.

        This must be a boolean scalar value, either True or False. Raise a ValueError if
        the object does not have exactly 1 element, or that element is not boolean

        Returns
        -------
        bool

        Examples
        --------
        >>> ps.DataFrame({'a': [True]}).bool()
        True

        >>> ps.Series([False]).bool()
        False

        If there are non-boolean or multiple values exist, it raises an exception in all
        cases as below.

        >>> ps.DataFrame({'a': ['a']}).bool()
        Traceback (most recent call last):
          ...
        ValueError: bool cannot act on a non-boolean single element DataFrame

        >>> ps.DataFrame({'a': [True], 'b': [False]}).bool()  # doctest: +NORMALIZE_WHITESPACE
        Traceback (most recent call last):
          ...
        ValueError: The truth value of a DataFrame is ambiguous. Use a.empty, a.bool(),
        a.item(), a.any() or a.all().

        >>> ps.Series([1]).bool()
        Traceback (most recent call last):
          ...
        ValueError: bool cannot act on a non-boolean single element DataFrame
        """
    def first_valid_index(self) -> Scalar | Tuple[Scalar, ...] | None:
        """
        Retrieves the index of the first valid value.

        Returns
        -------
        scalar, tuple, or None

        Examples
        --------

        Support for DataFrame

        >>> psdf = ps.DataFrame({'a': [None, 2, 3, 2],
        ...                     'b': [None, 2.0, 3.0, 1.0],
        ...                     'c': [None, 200, 400, 200]},
        ...                     index=['Q', 'W', 'E', 'R'])
        >>> psdf
             a    b      c
        Q  NaN  NaN    NaN
        W  2.0  2.0  200.0
        E  3.0  3.0  400.0
        R  2.0  1.0  200.0

        >>> psdf.first_valid_index()
        'W'

        Support for MultiIndex columns

        >>> psdf.columns = pd.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
        >>> psdf
             a    b      c
             x    y      z
        Q  NaN  NaN    NaN
        W  2.0  2.0  200.0
        E  3.0  3.0  400.0
        R  2.0  1.0  200.0

        >>> psdf.first_valid_index()
        'W'

        Support for Series.

        >>> s = ps.Series([None, None, 3, 4, 5], index=[100, 200, 300, 400, 500])
        >>> s
        100    NaN
        200    NaN
        300    3.0
        400    4.0
        500    5.0
        dtype: float64

        >>> s.first_valid_index()
        300

        Support for MultiIndex

        >>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
        ...                       ['speed', 'weight', 'length']],
        ...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
        ...                       [0, 1, 2, 0, 1, 2, 0, 1, 2]])
        >>> s = ps.Series([None, None, None, None, 250, 1.5, 320, 1, 0.3], index=midx)
        >>> s
        lama    speed       NaN
                weight      NaN
                length      NaN
        cow     speed       NaN
                weight    250.0
                length      1.5
        falcon  speed     320.0
                weight      1.0
                length      0.3
        dtype: float64

        >>> s.first_valid_index()
        ('cow', 'weight')
        """
    def last_valid_index(self) -> Scalar | Tuple[Scalar, ...] | None:
        """
        Return index for last non-NA/null value.

        Returns
        -------
        scalar, tuple, or None

        Notes
        -----
        This API only works with PySpark >= 3.0.

        Examples
        --------

        Support for DataFrame

        >>> psdf = ps.DataFrame({'a': [1, 2, 3, None],
        ...                     'b': [1.0, 2.0, 3.0, None],
        ...                     'c': [100, 200, 400, None]},
        ...                     index=['Q', 'W', 'E', 'R'])
        >>> psdf
             a    b      c
        Q  1.0  1.0  100.0
        W  2.0  2.0  200.0
        E  3.0  3.0  400.0
        R  NaN  NaN    NaN

        >>> psdf.last_valid_index()  # doctest: +SKIP
        'E'

        Support for MultiIndex columns

        >>> psdf.columns = pd.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
        >>> psdf
             a    b      c
             x    y      z
        Q  1.0  1.0  100.0
        W  2.0  2.0  200.0
        E  3.0  3.0  400.0
        R  NaN  NaN    NaN

        >>> psdf.last_valid_index()  # doctest: +SKIP
        'E'

        Support for Series.

        >>> s = ps.Series([1, 2, 3, None, None], index=[100, 200, 300, 400, 500])
        >>> s
        100    1.0
        200    2.0
        300    3.0
        400    NaN
        500    NaN
        dtype: float64

        >>> s.last_valid_index()  # doctest: +SKIP
        300

        Support for MultiIndex

        >>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
        ...                       ['speed', 'weight', 'length']],
        ...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
        ...                       [0, 1, 2, 0, 1, 2, 0, 1, 2]])
        >>> s = ps.Series([250, 1.5, 320, 1, 0.3, None, None, None, None], index=midx)
        >>> s
        lama    speed     250.0
                weight      1.5
                length    320.0
        cow     speed       1.0
                weight      0.3
                length      NaN
        falcon  speed       NaN
                weight      NaN
                length      NaN
        dtype: float64

        >>> s.last_valid_index()  # doctest: +SKIP
        ('cow', 'weight')
        """
    def rolling(self, window: int, min_periods: int | None = None) -> Rolling[FrameLike]:
        """
        Provide rolling transformations.

        .. note:: 'min_periods' in pandas-on-Spark works as a fixed window size unlike pandas.
            Unlike pandas, NA is also counted as the period. This might be changed
            soon.

        Parameters
        ----------
        window: int, or offset
            Size of the moving window.
            This is the number of observations used for calculating the statistic.
            Each window will be a fixed size.

        min_periods: int, default None
            Minimum number of observations in window required to have a value
            (otherwise result is NA).
            For a window that is specified by an offset, min_periods will default to 1.
            Otherwise, min_periods will default to the size of the window.

        Returns
        -------
        a Window sub-classed for the operation
        """
    def expanding(self, min_periods: int = 1) -> Expanding[FrameLike]:
        """
        Provide expanding transformations.

        .. note:: 'min_periods' in pandas-on-Spark works as a fixed window size unlike pandas.
            Unlike pandas, NA is also counted as the period. This might be changed
            soon.

        Parameters
        ----------
        min_periods: int, default 1
            Minimum number of observations in window required to have a value
            (otherwise result is NA).

        Returns
        -------
        a Window sub-classed for the operation
        """
    def ewm(self, com: float | None = None, span: float | None = None, halflife: float | None = None, alpha: float | None = None, min_periods: int | None = None, ignore_na: bool_type = False) -> ExponentialMoving[FrameLike]:
        """
        Provide exponentially weighted window transformations.

        .. note:: 'min_periods' in pandas-on-Spark works as a fixed window size unlike pandas.
            Unlike pandas, NA is also counted as the period. This might be changed
            soon.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        com: float, optional
            Specify decay in terms of center of mass.
            alpha = 1 / (1 + com), for com >= 0.

        span: float, optional
            Specify decay in terms of span.
            alpha = 2 / (span + 1), for span >= 1.

        halflife: float, optional
            Specify decay in terms of half-life.
            alpha = 1 - exp(-ln(2) / halflife), for halflife > 0.

        alpha: float, optional
            Specify smoothing factor alpha directly.
            0 < alpha <= 1.

        min_periods: int, default None
            Minimum number of observations in window required to have a value
            (otherwise result is NA).

        ignore_na: bool, default False
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

        Returns
        -------
        a Window sub-classed for the operation
        """
    def get(self, key: Any, default: Any | None = None) -> Any:
        """
        Get item from object for given key (DataFrame column, Panel slice,
        etc.). Returns default value if not found.

        Parameters
        ----------
        key: object

        Returns
        -------
        value: same type as items contained in object

        Examples
        --------
        >>> df = ps.DataFrame({'x':range(3), 'y':['a','b','b'], 'z':['a','b','b']},
        ...                   columns=['x', 'y', 'z'], index=[10, 20, 20])
        >>> df
            x  y  z
        10  0  a  a
        20  1  b  b
        20  2  b  b

        >>> df.get('x')
        10    0
        20    1
        20    2
        Name: x, dtype: int64

        >>> df.get(['x', 'y'])
            x  y
        10  0  a
        20  1  b
        20  2  b

        >>> df.x.get(10)
        0

        >>> df.x.get(20)
        20    1
        20    2
        Name: x, dtype: int64

        >>> df.x.get(15, -1)
        -1
        """
    def squeeze(self, axis: Axis | None = None) -> Scalar | DataFrame | Series:
        """
        Squeeze 1 dimensional axis objects into scalars.

        Series or DataFrames with a single element are squeezed to a scalar.
        DataFrames with a single column or a single row are squeezed to a
        Series. Otherwise the object is unchanged.

        This method is most useful when you don't know if your
        object is a Series or DataFrame, but you do know it has just a single
        column. In that case you can safely call `squeeze` to ensure you have a
        Series.

        Parameters
        ----------
        axis: {0 or 'index', 1 or 'columns', None}, default None
            A specific axis to squeeze. By default, all length-1 axes are
            squeezed.

        Returns
        -------
        DataFrame, Series, or scalar
            The projection after squeezing `axis` or all the axes.

        See Also
        --------
        Series.iloc: Integer-location based indexing for selecting scalars.
        DataFrame.iloc: Integer-location based indexing for selecting Series.
        Series.to_frame: Inverse of DataFrame.squeeze for a
            single-column DataFrame.

        Examples
        --------
        >>> primes = ps.Series([2, 3, 5, 7])

        Slicing might produce a Series with a single value:

        >>> even_primes = primes[primes % 2 == 0]
        >>> even_primes
        0    2
        dtype: int64

        >>> even_primes.squeeze()
        2

        Squeezing objects with more than one value in every axis does nothing:

        >>> odd_primes = primes[primes % 2 == 1]
        >>> odd_primes
        1    3
        2    5
        3    7
        dtype: int64

        >>> odd_primes.squeeze()
        1    3
        2    5
        3    7
        dtype: int64

        Squeezing is even more effective when used with DataFrames.

        >>> df = ps.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
        >>> df
           a  b
        0  1  2
        1  3  4

        Slicing a single column will produce a DataFrame with the columns
        having only one value:

        >>> df_a = df[['a']]
        >>> df_a
           a
        0  1
        1  3

        The columns can be squeezed down, resulting in a Series:

        >>> df_a.squeeze('columns')
        0    1
        1    3
        Name: a, dtype: int64

        Slicing a single row from a single column will produce a single
        scalar DataFrame:

        >>> df_1a = df.loc[[1], ['a']]
        >>> df_1a
           a
        1  3

        Squeezing the rows produces a single scalar Series:

        >>> df_1a.squeeze('rows')
        a    3
        Name: 1, dtype: int64

        Squeezing all axes will project directly into a scalar:

        >>> df_1a.squeeze()
        3
        """
    def truncate(self, before: Any | None = None, after: Any | None = None, axis: Axis | None = None, copy: bool_type = True) -> DataFrameOrSeries:
        '''
        Truncate a Series or DataFrame before and after some index value.

        This is a useful shorthand for boolean indexing based on index
        values above or below certain thresholds.

        .. note:: This API is dependent on :meth:`Index.is_monotonic_increasing`
            which can be expensive.

        Parameters
        ----------
        before: date, str, int
            Truncate all rows before this index value.
        after: date, str, int
            Truncate all rows after this index value.
        axis: {0 or \'index\', 1 or \'columns\'}, optional
            Axis to truncate. Truncates the index (rows) by default.
        copy: bool, default is True,
            Return a copy of the truncated section.

        Returns
        -------
        type of caller
            The truncated Series or DataFrame.

        See Also
        --------
        DataFrame.loc: Select a subset of a DataFrame by label.
        DataFrame.iloc: Select a subset of a DataFrame by position.

        Examples
        --------
        >>> df = ps.DataFrame({\'A\': [\'a\', \'b\', \'c\', \'d\', \'e\'],
        ...                    \'B\': [\'f\', \'g\', \'h\', \'i\', \'j\'],
        ...                    \'C\': [\'k\', \'l\', \'m\', \'n\', \'o\']},
        ...                   index=[1, 2, 3, 4, 5])
        >>> df
           A  B  C
        1  a  f  k
        2  b  g  l
        3  c  h  m
        4  d  i  n
        5  e  j  o

        >>> df.truncate(before=2, after=4)
           A  B  C
        2  b  g  l
        3  c  h  m
        4  d  i  n

        The columns of a DataFrame can be truncated.

        >>> df.truncate(before="A", after="B", axis="columns")
           A  B
        1  a  f
        2  b  g
        3  c  h
        4  d  i
        5  e  j

        For Series, only rows can be truncated.

        >>> df[\'A\'].truncate(before=2, after=4)
        2    b
        3    c
        4    d
        Name: A, dtype: object

        A Series has index that sorted integers.

        >>> s = ps.Series([10, 20, 30, 40, 50, 60, 70],
        ...               index=[1, 2, 3, 4, 5, 6, 7])
        >>> s
        1    10
        2    20
        3    30
        4    40
        5    50
        6    60
        7    70
        dtype: int64

        >>> s.truncate(2, 5)
        2    20
        3    30
        4    40
        5    50
        dtype: int64

        A Series has index that sorted strings.

        >>> s = ps.Series([10, 20, 30, 40, 50, 60, 70],
        ...               index=[\'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\'])
        >>> s
        a    10
        b    20
        c    30
        d    40
        e    50
        f    60
        g    70
        dtype: int64

        >>> s.truncate(\'b\', \'e\')
        b    20
        c    30
        d    40
        e    50
        dtype: int64
        '''
    def to_markdown(self, buf: IO[str] | str | None = None, mode: str | None = None) -> str:
        '''
        Print Series or DataFrame in Markdown-friendly format.

        .. note:: This method should only be used if the resulting pandas object is expected
                  to be small, as all the data is loaded into the driver\'s memory.

        Parameters
        ----------
        buf: writable buffer, defaults to sys.stdout
            Where to send the output. By default, the output is printed to
            sys.stdout. Pass a writable buffer if you need to further process
            the output.
        mode: str, optional
            Mode in which file is opened.
        **kwargs
            These parameters will be passed to `tabulate`.

        Returns
        -------
        str
            Series or DataFrame in Markdown-friendly format.

        Notes
        -----
        Requires the `tabulate <https://pypi.org/project/tabulate>`_ package.

        Examples
        --------
        >>> psser = ps.Series(["elk", "pig", "dog", "quetzal"], name="animal")
        >>> print(psser.to_markdown())  # doctest: +SKIP
        |    | animal   |
        |---:|:---------|
        |  0 | elk      |
        |  1 | pig      |
        |  2 | dog      |
        |  3 | quetzal  |

        >>> psdf = ps.DataFrame(
        ...     data={"animal_1": ["elk", "pig"], "animal_2": ["dog", "quetzal"]}
        ... )
        >>> print(psdf.to_markdown())  # doctest: +SKIP
        |    | animal_1   | animal_2   |
        |---:|:-----------|:-----------|
        |  0 | elk        | dog        |
        |  1 | pig        | quetzal    |
        '''
    @abstractmethod
    def fillna(self, value: Any | None = None, method: str | None = None, axis: Axis | None = None, inplace: bool_type = False, limit: int | None = None) -> FrameLike: ...
    def bfill(self, axis: Axis | None = None, inplace: bool_type = False, limit: int | None = None) -> FrameLike:
        """
        Synonym for `DataFrame.fillna()` or `Series.fillna()` with ``method=`bfill```.

        .. note:: the current implementation of 'bfill' uses Spark's Window
            without specifying partition specification. This leads to moveing all data into a
            single partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

        Parameters
        ----------
        axis: {0 or `index`}
            1 and `columns` are not supported.
        inplace: boolean, default False
            Fill in place (do not create a new object)
        limit: int, default None
            If method is specified, this is the maximum number of consecutive NaN values to
            forward/backward fill. In other words, if there is a gap with more than this number of
            consecutive NaNs, it will only be partially filled. If method is not specified,
            this is the maximum number of entries along the entire axis where NaNs will be filled.
            Must be greater than 0 if not None

        Returns
        -------
        DataFrame or Series
            DataFrame or Series with NA entries filled.

        Examples
        --------
        >>> psdf = ps.DataFrame({
        ...     'A': [None, 3, None, None],
        ...     'B': [2, 4, None, 3],
        ...     'C': [None, None, None, 1],
        ...     'D': [0, 1, 5, 4]
        ...     },
        ...     columns=['A', 'B', 'C', 'D'])
        >>> psdf
             A    B    C  D
        0  NaN  2.0  NaN  0
        1  3.0  4.0  NaN  1
        2  NaN  NaN  NaN  5
        3  NaN  3.0  1.0  4

        Propagate non-null values backward.

        >>> psdf.bfill()
             A    B    C  D
        0  3.0  2.0  1.0  0
        1  3.0  4.0  1.0  1
        2  NaN  3.0  1.0  5
        3  NaN  3.0  1.0  4

        For Series

        >>> psser = ps.Series([None, None, None, 1])
        >>> psser
        0    NaN
        1    NaN
        2    NaN
        3    1.0
        dtype: float64

        >>> psser.bfill()
        0    1.0
        1    1.0
        2    1.0
        3    1.0
        dtype: float64
        """
    backfill = bfill
    def ffill(self, axis: Axis | None = None, inplace: bool_type = False, limit: int | None = None) -> FrameLike:
        """
        Synonym for `DataFrame.fillna()` or `Series.fillna()` with ``method=`ffill```.

        .. note:: the current implementation of 'ffill' uses Spark's Window
            without specifying partition specification. This leads to moveing all data into a
            single a partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

        Parameters
        ----------
        axis: {0 or `index`}
            1 and `columns` are not supported.
        inplace: boolean, default False
            Fill in place (do not create a new object)
        limit: int, default None
            If method is specified, this is the maximum number of consecutive NaN values to
            forward/backward fill. In other words, if there is a gap with more than this number of
            consecutive NaNs, it will only be partially filled. If method is not specified,
            this is the maximum number of entries along the entire axis where NaNs will be filled.
            Must be greater than 0 if not None

        Returns
        -------
        DataFrame or Series
            DataFrame or Series with NA entries filled.

        Examples
        --------
        >>> psdf = ps.DataFrame({
        ...     'A': [None, 3, None, None],
        ...     'B': [2, 4, None, 3],
        ...     'C': [None, None, None, 1],
        ...     'D': [0, 1, 5, 4]
        ...     },
        ...     columns=['A', 'B', 'C', 'D'])
        >>> psdf
             A    B    C  D
        0  NaN  2.0  NaN  0
        1  3.0  4.0  NaN  1
        2  NaN  NaN  NaN  5
        3  NaN  3.0  1.0  4

        Propagate non-null values forward.

        >>> psdf.ffill()
             A    B    C  D
        0  NaN  2.0  NaN  0
        1  3.0  4.0  NaN  1
        2  3.0  4.0  NaN  5
        3  3.0  3.0  1.0  4

        For Series

        >>> psser = ps.Series([2, 4, None, 3])
        >>> psser
        0    2.0
        1    4.0
        2    NaN
        3    3.0
        dtype: float64

        >>> psser.ffill()
        0    2.0
        1    4.0
        2    4.0
        3    3.0
        dtype: float64
        """
    pad = ffill
    def interpolate(self, method: str = 'linear', limit: int | None = None, limit_direction: str | None = None, limit_area: str | None = None) -> FrameLike:
        """
        Fill NaN values using an interpolation method.

        .. note:: the current implementation of interpolate uses Spark's Window without
            specifying partition specification. This leads to moveing all data into a
            single partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        method: str, default 'linear'
            Interpolation technique to use. One of:

            * 'linear': Ignore the index and treat the values as equally
              spaced.

        limit: int, optional
            Maximum number of consecutive NaNs to fill. Must be greater than
            0.

        limit_direction: str, default None
            Consecutive NaNs will be filled in this direction.
            One of {{'forward', 'backward', 'both'}}.

        limit_area: str, default None
            If limit is specified, consecutive NaNs will be filled with this restriction. One of:

            * None: No fill restriction.
            * 'inside': Only fill NaNs surrounded by valid values (interpolate).
            * 'outside': Only fill NaNs outside valid values (extrapolate).

        Returns
        -------
        Series or DataFrame or None
            Returns the same object type as the caller, interpolated at
            some or all NA values.

        See Also
        --------
        fillna: Fill missing values using different methods.

        Examples
        --------
        Filling in NA via linear interpolation.

        >>> s = ps.Series([0, 1, np.nan, 3])
        >>> s
        0    0.0
        1    1.0
        2    NaN
        3    3.0
        dtype: float64
        >>> s.interpolate()
        0    0.0
        1    1.0
        2    2.0
        3    3.0
        dtype: float64

        Fill the DataFrame forward (that is, going down) along each column
        using linear interpolation.

        Note how the last entry in column 'a' is interpolated differently,
        because there is no entry after it to use for interpolation.
        Note how the first entry in column 'b' remains NA, because there
        is no entry before it to use for interpolation.

        >>> df = ps.DataFrame([(0.0, np.nan, -1.0, 1.0),
        ...                    (np.nan, 2.0, np.nan, np.nan),
        ...                    (2.0, 3.0, np.nan, 9.0),
        ...                    (np.nan, 4.0, -4.0, 16.0)],
        ...                   columns=list('abcd'))
        >>> df
             a    b    c     d
        0  0.0  NaN -1.0   1.0
        1  NaN  2.0  NaN   NaN
        2  2.0  3.0  NaN   9.0
        3  NaN  4.0 -4.0  16.0
        >>> df.interpolate(method='linear')
             a    b    c     d
        0  0.0  NaN -1.0   1.0
        1  1.0  2.0 -2.0   5.0
        2  2.0  3.0 -3.0   9.0
        3  2.0  4.0 -4.0  16.0
        """
    @property
    def at(self) -> AtIndexer: ...
    @property
    def iat(self) -> iAtIndexer: ...
    @property
    def iloc(self) -> iLocIndexer: ...
    @property
    def loc(self) -> LocIndexer: ...
    def __bool__(self) -> NoReturn: ...
