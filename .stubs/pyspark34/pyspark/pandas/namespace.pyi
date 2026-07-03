import pandas as pd
from _typeshed import Incomplete
from datetime import tzinfo
from pandas.tseries.offsets import DateOffset
from pyspark.pandas._typing import Axis, Dtype, Name
from pyspark.pandas.frame import DataFrame
from pyspark.pandas.indexes import DatetimeIndex, Index, TimedeltaIndex
from pyspark.pandas.series import Series
from pyspark.sql.types import StructType
from typing import Any, Callable, Dict, List, Tuple

__all__ = ['from_pandas', 'range', 'read_csv', 'read_delta', 'read_table', 'read_spark_io', 'read_parquet', 'read_clipboard', 'read_excel', 'read_html', 'to_datetime', 'date_range', 'to_timedelta', 'timedelta_range', 'get_dummies', 'concat', 'melt', 'isna', 'isnull', 'notna', 'notnull', 'read_sql_table', 'read_sql_query', 'read_sql', 'read_json', 'merge', 'merge_asof', 'to_numeric', 'broadcast', 'read_orc']

def from_pandas(pobj: pd.DataFrame | pd.Series | pd.Index) -> Series | DataFrame | Index:
    """Create a pandas-on-Spark DataFrame, Series or Index from a pandas DataFrame, Series or Index.

    This is similar to Spark's `SparkSession.createDataFrame()` with pandas DataFrame,
    but this also works with pandas Series and picks the index.

    Parameters
    ----------
    pobj : pandas.DataFrame or pandas.Series
        pandas DataFrame or Series to read.

    Returns
    -------
    Series or DataFrame
        If a pandas Series is passed in, this function returns a pandas-on-Spark Series.
        If a pandas DataFrame is passed in, this function returns a pandas-on-Spark DataFrame.
    """
def range(start: int, end: int | None = None, step: int = 1, num_partitions: int | None = None) -> DataFrame:
    """
    Create a DataFrame with some range of numbers.

    The resulting DataFrame has a single int64 column named `id`, containing elements in a range
    from ``start`` to ``end`` (exclusive) with step value ``step``. If only the first parameter
    (i.e. start) is specified, we treat it as the end value with the start value being 0.

    This is like the range function in SparkSession and is used primarily for testing.

    Parameters
    ----------
    start : int
        the start value (inclusive)
    end : int, optional
        the end value (exclusive)
    step : int, optional, default 1
        the incremental step
    num_partitions : int, optional
        the number of partitions of the DataFrame

    Returns
    -------
    DataFrame

    Examples
    --------
    When the first parameter is specified, we generate a range of values up till that number.

    >>> ps.range(5)
       id
    0   0
    1   1
    2   2
    3   3
    4   4

    When start, end, and step are specified:

    >>> ps.range(start = 100, end = 200, step = 20)
        id
    0  100
    1  120
    2  140
    3  160
    4  180
    """
def read_csv(path: str | List[str], sep: str = ',', header: str | int | None = 'infer', names: str | List[str] | None = None, index_col: str | List[str] | None = None, usecols: List[int] | List[str] | Callable[[str], bool] | None = None, squeeze: bool = False, mangle_dupe_cols: bool = True, dtype: str | Dtype | Dict[str, str | Dtype] | None = None, nrows: int | None = None, parse_dates: bool = False, quotechar: str | None = None, escapechar: str | None = None, comment: str | None = None, encoding: str | None = None, **options: Any) -> DataFrame | Series:
    """Read CSV (comma-separated) file into DataFrame or Series.

    Parameters
    ----------
    path : str or list
        Path(s) of the CSV file(s) to be read.
    sep : str, default ‘,’
        Delimiter to use. Non empty string.
    header : int, default ‘infer’
        Whether to use the column names, and the start of the data.
        Default behavior is to infer the column names: if no names are passed
        the behavior is identical to `header=0` and column names are inferred from
        the first line of the file, if column names are passed explicitly then
        the behavior is identical to `header=None`. Explicitly pass `header=0` to be
        able to replace existing names
    names : str or array-like, optional
        List of column names to use. If file contains no header row, then you should
        explicitly pass `header=None`. Duplicates in this list will cause an error to be issued.
        If a string is given, it should be a DDL-formatted string in Spark SQL, which is
        preferred to avoid schema inference for better performance.
    index_col: str or list of str, optional, default: None
        Index column of table in Spark.
    usecols : list-like or callable, optional
        Return a subset of the columns. If list-like, all elements must either be
        positional (i.e. integer indices into the document columns) or strings that
        correspond to column names provided either by the user in names or inferred
        from the document header row(s).
        If callable, the callable function will be evaluated against the column names,
        returning names where the callable function evaluates to `True`.
    squeeze : bool, default False
        If the parsed data only contains one column then return a Series.

        .. deprecated:: 3.4.0

    mangle_dupe_cols : bool, default True
        Duplicate columns will be specified as 'X0', 'X1', ... 'XN', rather
        than 'X' ... 'X'. Passing in False will cause data to be overwritten if
        there are duplicate names in the columns.
        Currently only `True` is allowed.

        .. deprecated:: 3.4.0

    dtype : Type name or dict of column -> type, default None
        Data type for data or columns. E.g. {‘a’: np.float64, ‘b’: np.int32} Use str or object
        together with suitable na_values settings to preserve and not interpret dtype.
    nrows : int, default None
        Number of rows to read from the CSV file.
    parse_dates : boolean or list of ints or names or list of lists or dict, default `False`.
        Currently only `False` is allowed.
    quotechar : str (length 1), optional
        The character used to denote the start and end of a quoted item. Quoted items can include
        the delimiter and it will be ignored.
    escapechar : str (length 1), default None
        One-character string used to escape other characters.
    comment: str, optional
        Indicates the line should not be parsed.
    encoding: str, optional
        Indicates the encoding to read file
    options : dict
        All other options passed directly into Spark's data source.

    Returns
    -------
    DataFrame or Series

    See Also
    --------
    DataFrame.to_csv : Write DataFrame to a comma-separated values (csv) file.

    Examples
    --------
    >>> ps.read_csv('data.csv')  # doctest: +SKIP

    Load multiple CSV files as a single DataFrame:

    >>> ps.read_csv(['data-01.csv', 'data-02.csv'])  # doctest: +SKIP
    """
def read_json(path: str, lines: bool = True, index_col: str | List[str] | None = None, **options: Any) -> DataFrame:
    '''
    Convert a JSON string to DataFrame.

    Parameters
    ----------
    path : string
        File path
    lines : bool, default True
        Read the file as a JSON object per line. It should be always True for now.
    index_col : str or list of str, optional, default: None
        Index column of table in Spark.
    options : dict
        All other options passed directly into Spark\'s data source.

    Examples
    --------
    >>> df = ps.DataFrame([[\'a\', \'b\'], [\'c\', \'d\']],
    ...                   columns=[\'col 1\', \'col 2\'])

    >>> df.to_json(path=r\'%s/read_json/foo.json\' % path, num_files=1)
    >>> ps.read_json(
    ...     path=r\'%s/read_json/foo.json\' % path
    ... ).sort_values(by="col 1")
      col 1 col 2
    0     a     b
    1     c     d

    >>> df.to_json(path=r\'%s/read_json/foo.json\' % path, num_files=1, lineSep=\'___\')
    >>> ps.read_json(
    ...     path=r\'%s/read_json/foo.json\' % path, lineSep=\'___\'
    ... ).sort_values(by="col 1")
      col 1 col 2
    0     a     b
    1     c     d

    You can preserve the index in the roundtrip as below.

    >>> df.to_json(path=r\'%s/read_json/bar.json\' % path, num_files=1, index_col="index")
    >>> ps.read_json(
    ...     path=r\'%s/read_json/bar.json\' % path, index_col="index"
    ... ).sort_values(by="col 1")  # doctest: +NORMALIZE_WHITESPACE
          col 1 col 2
    index
    0         a     b
    1         c     d
    '''
def read_delta(path: str, version: str | None = None, timestamp: str | None = None, index_col: str | List[str] | None = None, **options: Any) -> DataFrame:
    '''
    Read a Delta Lake table on some file system and return a DataFrame.

    If the Delta Lake table is already stored in the catalog (aka the metastore), use \'read_table\'.

    Parameters
    ----------
    path : string
        Path to the Delta Lake table.
    version : string, optional
        Specifies the table version (based on Delta\'s internal transaction version) to read from,
        using Delta\'s time travel feature. This sets Delta\'s \'versionAsOf\' option. Note that
        this parameter and `timestamp` parameter cannot be used together, otherwise it will raise a
        `ValueError`.
    timestamp : string, optional
        Specifies the table version (based on timestamp) to read from,
        using Delta\'s time travel feature. This must be a valid date or timestamp string in Spark,
        and sets Delta\'s \'timestampAsOf\' option. Note that this parameter and `version` parameter
        cannot be used together, otherwise it will raise a `ValueError`.
    index_col : str or list of str, optional, default: None
        Index column of table in Spark.
    options
        Additional options that can be passed onto Delta.

    Returns
    -------
    DataFrame

    See Also
    --------
    DataFrame.to_delta
    read_table
    read_spark_io
    read_parquet

    Examples
    --------
    >>> ps.range(1).to_delta(\'%s/read_delta/foo\' % path)  # doctest: +SKIP
    >>> ps.read_delta(\'%s/read_delta/foo\' % path)  # doctest: +SKIP
       id
    0   0

    >>> ps.range(10, 15, num_partitions=1).to_delta(\'%s/read_delta/foo\' % path,
    ...                                             mode=\'overwrite\')  # doctest: +SKIP
    >>> ps.read_delta(\'%s/read_delta/foo\' % path)  # doctest: +SKIP
       id
    0  10
    1  11
    2  12
    3  13
    4  14

    >>> ps.read_delta(\'%s/read_delta/foo\' % path, version=0)  # doctest: +SKIP
       id
    0   0

    You can preserve the index in the roundtrip as below.

    >>> ps.range(10, 15, num_partitions=1).to_delta(
    ...     \'%s/read_delta/bar\' % path, index_col="index")  # doctest: +SKIP
    >>> ps.read_delta(\'%s/read_delta/bar\' % path, index_col="index")  # doctest: +SKIP
           id
    index
    0      10
    1      11
    2      12
    3      13
    4      14
    '''
def read_table(name: str, index_col: str | List[str] | None = None) -> DataFrame:
    '''
    Read a Spark table and return a DataFrame.

    Parameters
    ----------
    name : string
        Table name in Spark.

    index_col : str or list of str, optional, default: None
        Index column of table in Spark.

    Returns
    -------
    DataFrame

    See Also
    --------
    DataFrame.to_table
    read_delta
    read_parquet
    read_spark_io

    Examples
    --------
    >>> ps.range(1).to_table(\'%s.my_table\' % db)
    >>> ps.read_table(\'%s.my_table\' % db)
       id
    0   0

    >>> ps.range(1).to_table(\'%s.my_table\' % db, index_col="index")
    >>> ps.read_table(\'%s.my_table\' % db, index_col="index")  # doctest: +NORMALIZE_WHITESPACE
           id
    index
    0       0
    '''
def read_spark_io(path: str | None = None, format: str | None = None, schema: str | StructType = None, index_col: str | List[str] | None = None, **options: Any) -> DataFrame:
    '''Load a DataFrame from a Spark data source.

    Parameters
    ----------
    path : string, optional
        Path to the data source.
    format : string, optional
        Specifies the output data source format. Some common ones are:

        - \'delta\'
        - \'parquet\'
        - \'orc\'
        - \'json\'
        - \'csv\'
    schema : string or StructType, optional
        Input schema. If none, Spark tries to infer the schema automatically.
        The schema can either be a Spark StructType, or a DDL-formatted string like
        `col0 INT, col1 DOUBLE`.
    index_col : str or list of str, optional, default: None
        Index column of table in Spark.
    options : dict
        All other options passed directly into Spark\'s data source.

    See Also
    --------
    DataFrame.to_spark_io
    DataFrame.read_table
    DataFrame.read_delta
    DataFrame.read_parquet

    Examples
    --------
    >>> ps.range(1).to_spark_io(\'%s/read_spark_io/data.parquet\' % path)
    >>> ps.read_spark_io(
    ...     \'%s/read_spark_io/data.parquet\' % path, format=\'parquet\', schema=\'id long\')
       id
    0   0

    >>> ps.range(10, 15, num_partitions=1).to_spark_io(\'%s/read_spark_io/data.json\' % path,
    ...                                                format=\'json\', lineSep=\'__\')
    >>> ps.read_spark_io(
    ...     \'%s/read_spark_io/data.json\' % path, format=\'json\', schema=\'id long\', lineSep=\'__\')
       id
    0  10
    1  11
    2  12
    3  13
    4  14

    You can preserve the index in the roundtrip as below.

    >>> ps.range(10, 15, num_partitions=1).to_spark_io(\'%s/read_spark_io/data.orc\' % path,
    ...                                                format=\'orc\', index_col="index")
    >>> ps.read_spark_io(
    ...     path=r\'%s/read_spark_io/data.orc\' % path, format="orc", index_col="index")
    ... # doctest: +NORMALIZE_WHITESPACE
           id
    index
    0      10
    1      11
    2      12
    3      13
    4      14
    '''
def read_parquet(path: str, columns: List[str] | None = None, index_col: List[str] | None = None, pandas_metadata: bool = False, **options: Any) -> DataFrame:
    '''Load a parquet object from the file path, returning a DataFrame.

    Parameters
    ----------
    path : string
        File path
    columns : list, default=None
        If not None, only these columns will be read from the file.
    index_col : str or list of str, optional, default: None
        Index column of table in Spark.
    pandas_metadata : bool, default: False
        If True, try to respect the metadata if the Parquet file is written from pandas.
    options : dict
        All other options passed directly into Spark\'s data source.

    Returns
    -------
    DataFrame

    See Also
    --------
    DataFrame.to_parquet
    DataFrame.read_table
    DataFrame.read_delta
    DataFrame.read_spark_io

    Examples
    --------
    >>> ps.range(1).to_parquet(\'%s/read_spark_io/data.parquet\' % path)
    >>> ps.read_parquet(\'%s/read_spark_io/data.parquet\' % path, columns=[\'id\'])
       id
    0   0

    You can preserve the index in the roundtrip as below.

    >>> ps.range(1).to_parquet(\'%s/read_spark_io/data.parquet\' % path, index_col="index")
    >>> ps.read_parquet(\'%s/read_spark_io/data.parquet\' % path, columns=[\'id\'], index_col="index")
    ... # doctest: +NORMALIZE_WHITESPACE
           id
    index
    0       0
    '''
def read_clipboard(sep: str = '\\s+', **kwargs: Any) -> DataFrame:
    """
    Read text from clipboard and pass to read_csv. See read_csv for the
    full argument list

    Parameters
    ----------
    sep : str, default '\\s+'
        A string or regex delimiter. The default of '\\s+' denotes
        one or more whitespace characters.

    See Also
    --------
    DataFrame.to_clipboard : Write text out to clipboard.

    Returns
    -------
    parsed : DataFrame
    """
def read_excel(io: str | Any, sheet_name: str | int | List[str | int] | None = 0, header: int | List[int] = 0, names: List | None = None, index_col: List[int] | None = None, usecols: int | str | List[int | str] | Callable[[str], bool] | None = None, squeeze: bool = False, dtype: Dict[str, str | Dtype] | None = None, engine: str | None = None, converters: Dict | None = None, true_values: Any | None = None, false_values: Any | None = None, skiprows: int | List[int] | None = None, nrows: int | None = None, na_values: Any | None = None, keep_default_na: bool = True, verbose: bool = False, parse_dates: bool | List | Dict = False, date_parser: Callable | None = None, thousands: str | None = None, comment: str | None = None, skipfooter: int = 0, convert_float: bool = True, mangle_dupe_cols: bool = True, **kwds: Any) -> DataFrame | Series | Dict[str, DataFrame | Series]:
    '''
    Read an Excel file into a pandas-on-Spark DataFrame or Series.

    Support both `xls` and `xlsx` file extensions from a local filesystem or URL.
    Support an option to read a single sheet or a list of sheets.

    Parameters
    ----------
    io : str, file descriptor, pathlib.Path, ExcelFile or xlrd.Book
        The string could be a URL. The value URL must be available in Spark\'s DataFrameReader.

        .. note::
            If the underlying Spark is below 3.0, the parameter as a string is not supported.
            You can use `ps.from_pandas(pd.read_excel(...))` as a workaround.

    sheet_name : str, int, list, or None, default 0
        Strings are used for sheet names. Integers are used in zero-indexed
        sheet positions. Lists of strings/integers are used to request
        multiple sheets. Specify None to get all sheets.

        Available cases:

        * Defaults to ``0``: 1st sheet as a `DataFrame`
        * ``1``: 2nd sheet as a `DataFrame`
        * ``"Sheet1"``: Load sheet with name "Sheet1"
        * ``[0, 1, "Sheet5"]``: Load first, second and sheet named "Sheet5"
          as a dict of `DataFrame`
        * None: All sheets.

    header : int, list of int, default 0
        Row (0-indexed) to use for the column labels of the parsed
        DataFrame. If a list of integers is passed those row positions will
        be combined into a ``MultiIndex``. Use None if there is no header.
    names : array-like, default None
        List of column names to use. If file contains no header row,
        then you should explicitly pass header=None.
    index_col : int, list of int, default None
        Column (0-indexed) to use as the row labels of the DataFrame.
        Pass None if there is no such column.  If a list is passed,
        those columns will be combined into a ``MultiIndex``.  If a
        subset of data is selected with ``usecols``, index_col
        is based on the subset.
    usecols : int, str, list-like, or callable default None
        Return a subset of the columns.

        * If None, then parse all columns.
        * If str, then indicates comma separated list of Excel column letters
          and column ranges (e.g. "A:E" or "A,C,E:F"). Ranges are inclusive of
          both sides.
        * If list of int, then indicates list of column numbers to be parsed.
        * If list of string, then indicates list of column names to be parsed.
        * If callable, then evaluate each column name against it and parse the
          column if the callable returns ``True``.
    squeeze : bool, default False
        If the parsed data only contains one column then return a Series.

        .. deprecated:: 3.4.0

    dtype : Type name or dict of column -> type, default None
        Data type for data or columns. E.g. {\'a\': np.float64, \'b\': np.int32}
        Use `object` to preserve data as stored in Excel and not interpret dtype.
        If converters are specified, they will be applied INSTEAD
        of dtype conversion.
    engine : str, default None
        If io is not a buffer or path, this must be set to identify io.
        Acceptable values are None or xlrd.
    converters : dict, default None
        Dict of functions for converting values in certain columns. Keys can
        either be integers or column labels, values are functions that take one
        input argument, the Excel cell content, and return the transformed
        content.
    true_values : list, default None
        Values to consider as True.
    false_values : list, default None
        Values to consider as False.
    skiprows : list-like
        Rows to skip at the beginning (0-indexed).
    nrows : int, default None
        Number of rows to parse.
    na_values : scalar, str, list-like, or dict, default None
        Additional strings to recognize as NA/NaN. If dict passed, specific
        per-column NA values. By default the following values are interpreted
        as NaN.
    keep_default_na : bool, default True
        If na_values are specified and keep_default_na is False the default NaN
        values are overridden, otherwise they\'re appended to.
    verbose : bool, default False
        Indicate number of NA values placed in non-numeric columns.
    parse_dates : bool, list-like, or dict, default False
        The behavior is as follows:

        * bool. If True -> try parsing the index.
        * list of int or names. e.g. If [1, 2, 3] -> try parsing columns 1, 2, 3
          each as a separate date column.
        * list of lists. e.g.  If [[1, 3]] -> combine columns 1 and 3 and parse as
          a single date column.
        * dict, e.g. {{\'foo\' : [1, 3]}} -> parse columns 1, 3 as date and call
          result \'foo\'

        If a column or index contains an unparseable date, the entire column or
        index will be returned unaltered as an object data type. For non-standard
        datetime parsing, use ``pd.to_datetime`` after ``pd.read_csv``

        Note: A fast-path exists for iso8601-formatted dates.
    date_parser : function, optional
        Function to use for converting a sequence of string columns to an array of
        datetime instances. The default uses ``dateutil.parser.parser`` to do the
        conversion. pandas-on-Spark will try to call `date_parser` in three different ways,
        advancing to the next if an exception occurs: 1) Pass one or more arrays
        (as defined by `parse_dates`) as arguments; 2) concatenate (row-wise) the
        string values from the columns defined by `parse_dates` into a single array
        and pass that; and 3) call `date_parser` once for each row using one or
        more strings (corresponding to the columns defined by `parse_dates`) as
        arguments.
    thousands : str, default None
        Thousands separator for parsing string columns to numeric.  Note that
        this parameter is only necessary for columns stored as TEXT in Excel,
        any numeric columns will automatically be parsed, regardless of display
        format.
    comment : str, default None
        Comments out remainder of line. Pass a character or characters to this
        argument to indicate comments in the input file. Any data between the
        comment string and the end of the current line is ignored.
    skipfooter : int, default 0
        Rows at the end to skip (0-indexed).
    convert_float : bool, default True
        Convert integral floats to int (i.e., 1.0 --> 1). If False, all numeric
        data will be read in as floats: Excel stores all numbers as floats
        internally.

        .. deprecated:: 3.4.0

    mangle_dupe_cols : bool, default True
        Duplicate columns will be specified as \'X\', \'X.1\', ...\'X.N\', rather than
        \'X\'...\'X\'. Passing in False will cause data to be overwritten if there
        are duplicate names in the columns.

        .. deprecated:: 3.4.0

    **kwds : optional
        Optional keyword arguments can be passed to ``TextFileReader``.

    Returns
    -------
    DataFrame or dict of DataFrames
        DataFrame from the passed in Excel file. See notes in sheet_name
        argument for more information on when a dict of DataFrames is returned.

    See Also
    --------
    DataFrame.to_excel : Write DataFrame to an Excel file.
    DataFrame.to_csv : Write DataFrame to a comma-separated values (csv) file.
    read_csv : Read a comma-separated values (csv) file into DataFrame.

    Examples
    --------
    The file can be read using the file name as string or an open file object:

    >>> ps.read_excel(\'tmp.xlsx\', index_col=0)  # doctest: +SKIP
           Name  Value
    0   string1      1
    1   string2      2
    2  #Comment      3

    >>> ps.read_excel(open(\'tmp.xlsx\', \'rb\'),
    ...               sheet_name=\'Sheet3\')  # doctest: +SKIP
       Unnamed: 0      Name  Value
    0           0   string1      1
    1           1   string2      2
    2           2  #Comment      3

    Index and header can be specified via the `index_col` and `header` arguments

    >>> ps.read_excel(\'tmp.xlsx\', index_col=None, header=None)  # doctest: +SKIP
         0         1      2
    0  NaN      Name  Value
    1  0.0   string1      1
    2  1.0   string2      2
    3  2.0  #Comment      3

    Column types are inferred but can be explicitly specified

    >>> ps.read_excel(\'tmp.xlsx\', index_col=0,
    ...               dtype={\'Name\': str, \'Value\': float})  # doctest: +SKIP
           Name  Value
    0   string1    1.0
    1   string2    2.0
    2  #Comment    3.0

    True, False, and NA values, and thousands separators have defaults,
    but can be explicitly specified, too. Supply the values you would like
    as strings or lists of strings!

    >>> ps.read_excel(\'tmp.xlsx\', index_col=0,
    ...               na_values=[\'string1\', \'string2\'])  # doctest: +SKIP
           Name  Value
    0      None      1
    1      None      2
    2  #Comment      3

    Comment lines in the excel input file can be skipped using the `comment` kwarg

    >>> ps.read_excel(\'tmp.xlsx\', index_col=0, comment=\'#\')  # doctest: +SKIP
          Name  Value
    0  string1    1.0
    1  string2    2.0
    2     None    NaN
    '''
def read_html(io: str | Any, match: str = '.+', flavor: str | None = None, header: int | List[int] | None = None, index_col: int | List[int] | None = None, skiprows: int | List[int] | slice | None = None, attrs: Dict[str, str] | None = None, parse_dates: bool = False, thousands: str = ',', encoding: str | None = None, decimal: str = '.', converters: Dict | None = None, na_values: Any | None = None, keep_default_na: bool = True, displayed_only: bool = True) -> List[DataFrame]:
    '''Read HTML tables into a ``list`` of ``DataFrame`` objects.

    Parameters
    ----------
    io : str or file-like
        A URL, a file-like object, or a raw string containing HTML. Note that
        lxml only accepts the http, FTP and file URL protocols. If you have a
        URL that starts with ``\'https\'`` you might try removing the ``\'s\'``.

    match : str or compiled regular expression, optional
        The set of tables containing text matching this regex or string will be
        returned. Unless the HTML is extremely simple you will probably need to
        pass a non-empty string here. Defaults to \'.+\' (match any non-empty
        string). The default value will return all tables contained on a page.
        This value is converted to a regular expression so that there is
        consistent behavior between Beautiful Soup and lxml.

    flavor : str or None, container of strings
        The parsing engine to use. \'bs4\' and \'html5lib\' are synonymous with
        each other, they are both there for backwards compatibility. The
        default of ``None`` tries to use ``lxml`` to parse and if that fails it
        falls back on ``bs4`` + ``html5lib``.

    header : int or list-like or None, optional
        The row (or list of rows for a :class:`~ps.MultiIndex`) to use to
        make the columns headers.

    index_col : int or list-like or None, optional
        The column (or list of columns) to use to create the index.

    skiprows : int or list-like or slice or None, optional
        0-based. Number of rows to skip after parsing the column integer. If a
        sequence of integers or a slice is given, will skip the rows indexed by
        that sequence.  Note that a single element sequence means \'skip the nth
        row\' whereas an integer means \'skip n rows\'.

    attrs : dict or None, optional
        This is a dictionary of attributes that you can pass to use to identify
        the table in the HTML. These are not checked for validity before being
        passed to lxml or Beautiful Soup. However, these attributes must be
        valid HTML table attributes to work correctly. For example, ::

            attrs = {\'id\': \'table\'}

        is a valid attribute dictionary because the \'id\' HTML tag attribute is
        a valid HTML attribute for *any* HTML tag as per `this document
        <http://www.w3.org/TR/html-markup/global-attributes.html>`__. ::

            attrs = {\'asdf\': \'table\'}

        is *not* a valid attribute dictionary because \'asdf\' is not a valid
        HTML attribute even if it is a valid XML attribute.  Valid HTML 4.01
        table attributes can be found `here
        <http://www.w3.org/TR/REC-html40/struct/tables.html#h-11.2>`__. A
        working draft of the HTML 5 spec can be found `here
        <http://www.w3.org/TR/html-markup/table.html>`__. It contains the
        latest information on table attributes for the modern web.

    parse_dates : bool, optional
        See :func:`~ps.read_csv` for more details.

    thousands : str, optional
        Separator to use to parse thousands. Defaults to ``\',\'``.

    encoding : str or None, optional
        The encoding used to decode the web page. Defaults to ``None``.``None``
        preserves the previous encoding behavior, which depends on the
        underlying parser library (e.g., the parser library will try to use
        the encoding provided by the document).

    decimal : str, default \'.\'
        Character to recognize as decimal point (example: use \',\' for European
        data).

    converters : dict, default None
        Dict of functions for converting values in certain columns. Keys can
        either be integers or column labels, values are functions that take one
        input argument, the cell (not column) content, and return the
        transformed content.

    na_values : iterable, default None
        Custom NA values

    keep_default_na : bool, default True
        If na_values are specified and keep_default_na is False the default NaN
        values are overridden, otherwise they\'re appended to

    displayed_only : bool, default True
        Whether elements with "display: none" should be parsed

    Returns
    -------
    dfs : list of DataFrames

    See Also
    --------
    read_csv
    DataFrame.to_html
    '''
def read_sql_table(table_name: str, con: str, schema: str | None = None, index_col: str | List[str] | None = None, columns: str | List[str] | None = None, **options: Any) -> DataFrame:
    """
    Read SQL database table into a DataFrame.

    Given a table name and a JDBC URI, returns a DataFrame.

    Parameters
    ----------
    table_name : str
        Name of SQL table in database.
    con : str
        A JDBC URI could be provided as str.

        .. note:: The URI must be JDBC URI instead of Python's database URI.

    schema : str, default None
        Name of SQL schema in database to query (if database flavor
        supports this). Uses default schema if None (default).
    index_col : str or list of str, optional, default: None
        Column(s) to set as index(MultiIndex).
    columns : list, default None
        List of column names to select from SQL table.
    options : dict
        All other options passed directly into Spark's JDBC data source.

    Returns
    -------
    DataFrame
        A SQL table is returned as two-dimensional data structure with labeled
        axes.

    See Also
    --------
    read_sql_query : Read SQL query into a DataFrame.
    read_sql : Read SQL query or database table into a DataFrame.

    Examples
    --------
    >>> ps.read_sql_table('table_name', 'jdbc:postgresql:db_name')  # doctest: +SKIP
    """
def read_sql_query(sql: str, con: str, index_col: str | List[str] | None = None, **options: Any) -> DataFrame:
    """Read SQL query into a DataFrame.

    Returns a DataFrame corresponding to the result set of the query
    string. Optionally provide an `index_col` parameter to use one of the
    columns as the index, otherwise default index will be used.

    .. note:: Some database might hit the issue of Spark: SPARK-27596

    Parameters
    ----------
    sql : string SQL query
        SQL query to be executed.
    con : str
        A JDBC URI could be provided as str.

        .. note:: The URI must be JDBC URI instead of Python's database URI.

    index_col : string or list of strings, optional, default: None
        Column(s) to set as index(MultiIndex).
    options : dict
        All other options passed directly into Spark's JDBC data source.

    Returns
    -------
    DataFrame

    See Also
    --------
    read_sql_table : Read SQL database table into a DataFrame.
    read_sql

    Examples
    --------
    >>> ps.read_sql_query('SELECT * FROM table_name', 'jdbc:postgresql:db_name')  # doctest: +SKIP
    """
def read_sql(sql: str, con: str, index_col: str | List[str] | None = None, columns: str | List[str] | None = None, **options: Any) -> DataFrame:
    """
    Read SQL query or database table into a DataFrame.

    This function is a convenience wrapper around ``read_sql_table`` and
    ``read_sql_query`` (for backward compatibility). It will delegate
    to the specific function depending on the provided input. A SQL query
    will be routed to ``read_sql_query``, while a database table name will
    be routed to ``read_sql_table``. Note that the delegated function might
    have more specific notes about their functionality not listed here.

    .. note:: Some database might hit the issue of Spark: SPARK-27596

    Parameters
    ----------
    sql : string
        SQL query to be executed or a table name.
    con : str
        A JDBC URI could be provided as str.

        .. note:: The URI must be JDBC URI instead of Python's database URI.

    index_col : string or list of strings, optional, default: None
        Column(s) to set as index(MultiIndex).
    columns : list, default: None
        List of column names to select from SQL table (only used when reading
        a table).
    options : dict
        All other options passed directly into Spark's JDBC data source.

    Returns
    -------
    DataFrame

    See Also
    --------
    read_sql_table : Read SQL database table into a DataFrame.
    read_sql_query : Read SQL query into a DataFrame.

    Examples
    --------
    >>> ps.read_sql('table_name', 'jdbc:postgresql:db_name')  # doctest: +SKIP
    >>> ps.read_sql('SELECT * FROM table_name', 'jdbc:postgresql:db_name')  # doctest: +SKIP
    """
def to_datetime(arg, errors: str = 'raise', format: Incomplete | None = None, unit: Incomplete | None = None, infer_datetime_format: bool = False, origin: str = 'unix'):
    '''
    Convert argument to datetime.

    Parameters
    ----------
    arg : integer, float, string, datetime, list, tuple, 1-d array, Series
           or DataFrame/dict-like

    errors : {\'ignore\', \'raise\', \'coerce\'}, default \'raise\'

        - If \'raise\', then invalid parsing will raise an exception
        - If \'coerce\', then invalid parsing will be set as NaT
        - If \'ignore\', then invalid parsing will return the input
    format : string, default None
        strftime to parse time, eg "%d/%m/%Y", note that "%f" will parse
        all the way up to nanoseconds.
    unit : string, default None
        unit of the arg (D,s,ms,us,ns) denote the unit, which is an
        integer or float number. This will be based off the origin.
        Example, with unit=\'ms\' and origin=\'unix\' (the default), this
        would calculate the number of milliseconds to the unix epoch start.
    infer_datetime_format : boolean, default False
        If True and no `format` is given, attempt to infer the format of the
        datetime strings, and if it can be inferred, switch to a faster
        method of parsing them. In some cases this can increase the parsing
        speed by ~5-10x.
    origin : scalar, default \'unix\'
        Define the reference date. The numeric values would be parsed as number
        of units (defined by `unit`) since this reference date.

        - If \'unix\' (or POSIX) time; origin is set to 1970-01-01.
        - If \'julian\', unit must be \'D\', and origin is set to beginning of
          Julian Calendar. Julian day number 0 is assigned to the day starting
          at noon on January 1, 4713 BC.
        - If Timestamp convertible, origin is set to Timestamp identified by
          origin.

    Returns
    -------
    ret : datetime if parsing succeeded.
        Return type depends on input:

        - list-like: DatetimeIndex
        - Series: Series of datetime64 dtype
        - scalar: Timestamp

        In case when it is not possible to return designated types (e.g. when
        any element of input is before Timestamp.min or after Timestamp.max)
        return will have datetime.datetime type (or corresponding
        array/Series).

    Examples
    --------
    Assembling a datetime from multiple columns of a DataFrame. The keys can be
    common abbreviations like [\'year\', \'month\', \'day\', \'minute\', \'second\',
    \'ms\', \'us\', \'ns\']) or plurals of the same

    >>> df = ps.DataFrame({\'year\': [2015, 2016],
    ...                    \'month\': [2, 3],
    ...                    \'day\': [4, 5]})
    >>> ps.to_datetime(df)
    0   2015-02-04
    1   2016-03-05
    dtype: datetime64[ns]

    If a date does not meet the `timestamp limitations
    <http://pandas.pydata.org/pandas-docs/stable/timeseries.html
    #timeseries-timestamp-limits>`_, passing errors=\'ignore\'
    will return the original input instead of raising any exception.

    Passing errors=\'coerce\' will force an out-of-bounds date to NaT,
    in addition to forcing non-dates (or non-parseable dates) to NaT.

    >>> ps.to_datetime(\'13000101\', format=\'%Y%m%d\', errors=\'ignore\')
    datetime.datetime(1300, 1, 1, 0, 0)
    >>> ps.to_datetime(\'13000101\', format=\'%Y%m%d\', errors=\'coerce\')
    NaT

    Passing infer_datetime_format=True can often-times speedup a parsing
    if its not an ISO8601 format exactly, but in a regular format.

    >>> s = ps.Series([\'3/11/2000\', \'3/12/2000\', \'3/13/2000\'] * 1000)
    >>> s.head()
    0    3/11/2000
    1    3/12/2000
    2    3/13/2000
    3    3/11/2000
    4    3/12/2000
    dtype: object

    >>> import timeit
    >>> timeit.timeit(
    ...    lambda: repr(ps.to_datetime(s, infer_datetime_format=True)),
    ...    number = 1)  # doctest: +SKIP
    0.35832712500000063

    >>> timeit.timeit(
    ...    lambda: repr(ps.to_datetime(s, infer_datetime_format=False)),
    ...    number = 1)  # doctest: +SKIP
    0.8895321660000004

    Using a unix epoch time

    >>> ps.to_datetime(1490195805, unit=\'s\')
    Timestamp(\'2017-03-22 15:16:45\')
    >>> ps.to_datetime(1490195805433502912, unit=\'ns\')
    Timestamp(\'2017-03-22 15:16:45.433502912\')

    Using a non-unix epoch origin

    >>> ps.to_datetime([1, 2, 3], unit=\'D\', origin=pd.Timestamp(\'1960-01-01\'))
    DatetimeIndex([\'1960-01-02\', \'1960-01-03\', \'1960-01-04\'], dtype=\'datetime64[ns]\', freq=None)
    '''
def date_range(start: str | Any = None, end: str | Any = None, periods: int | None = None, freq: str | DateOffset | None = None, tz: str | tzinfo | None = None, normalize: bool = False, name: str | None = None, closed: str | None = None, **kwargs: Any) -> DatetimeIndex:
    """
    Return a fixed frequency DatetimeIndex.

    Parameters
    ----------
    start : str or datetime-like, optional
        Left bound for generating dates.
    end : str or datetime-like, optional
        Right bound for generating dates.
    periods : int, optional
        Number of periods to generate.
    freq : str or DateOffset, default 'D'
        Frequency strings can have multiples, e.g. '5H'.
    tz : str or tzinfo, optional
        Time zone name for returning localized DatetimeIndex, for example
        'Asia/Hong_Kong'. By default, the resulting DatetimeIndex is
        time zone naive.
    normalize : bool, default False
        Normalize start/end dates to midnight before generating date range.
    name : str, default None
        Name of the resulting DatetimeIndex.
    closed : {None, 'left', 'right'}, optional
        Make the interval closed with respect to the given frequency to
        the 'left', 'right', or both sides (None, the default).

        .. deprecated:: 3.4.0

    **kwargs
        For compatibility. Has no effect on the result.

    Returns
    -------
    rng : DatetimeIndex

    See Also
    --------
    DatetimeIndex : An immutable container for datetimes.

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

    >>> ps.date_range(start='1/1/2018', end='1/08/2018')  # doctest: +NORMALIZE_WHITESPACE
    DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',
                   '2018-01-05', '2018-01-06', '2018-01-07', '2018-01-08'],
                  dtype='datetime64[ns]', freq=None)

    Specify `start` and `periods`, the number of periods (days).

    >>> ps.date_range(start='1/1/2018', periods=8)  # doctest: +NORMALIZE_WHITESPACE
    DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',
                   '2018-01-05', '2018-01-06', '2018-01-07', '2018-01-08'],
                  dtype='datetime64[ns]', freq=None)

    Specify `end` and `periods`, the number of periods (days).

    >>> ps.date_range(end='1/1/2018', periods=8)  # doctest: +NORMALIZE_WHITESPACE
    DatetimeIndex(['2017-12-25', '2017-12-26', '2017-12-27', '2017-12-28',
                   '2017-12-29', '2017-12-30', '2017-12-31', '2018-01-01'],
                  dtype='datetime64[ns]', freq=None)

    Specify `start`, `end`, and `periods`; the frequency is generated
    automatically (linearly spaced).

    >>> ps.date_range(
    ...     start='2018-04-24', end='2018-04-27', periods=3
    ... )  # doctest: +NORMALIZE_WHITESPACE
    DatetimeIndex(['2018-04-24 00:00:00', '2018-04-25 12:00:00',
                   '2018-04-27 00:00:00'],
                  dtype='datetime64[ns]', freq=None)

    **Other Parameters**

    Changed the `freq` (frequency) to ``'M'`` (month end frequency).

    >>> ps.date_range(start='1/1/2018', periods=5, freq='M')  # doctest: +NORMALIZE_WHITESPACE
    DatetimeIndex(['2018-01-31', '2018-02-28', '2018-03-31', '2018-04-30',
                   '2018-05-31'],
                  dtype='datetime64[ns]', freq=None)

    Multiples are allowed

    >>> ps.date_range(start='1/1/2018', periods=5, freq='3M')  # doctest: +NORMALIZE_WHITESPACE
    DatetimeIndex(['2018-01-31', '2018-04-30', '2018-07-31', '2018-10-31',
                   '2019-01-31'],
                  dtype='datetime64[ns]', freq=None)

    `freq` can also be specified as an Offset object.

    >>> ps.date_range(
    ...     start='1/1/2018', periods=5, freq=pd.offsets.MonthEnd(3)
    ... )  # doctest: +NORMALIZE_WHITESPACE
    DatetimeIndex(['2018-01-31', '2018-04-30', '2018-07-31', '2018-10-31',
                   '2019-01-31'],
                  dtype='datetime64[ns]', freq=None)

    `closed` controls whether to include `start` and `end` that are on the
    boundary. The default includes boundary points on either end.

    >>> ps.date_range(
    ...     start='2017-01-01', end='2017-01-04', closed=None
    ... )  # doctest: +NORMALIZE_WHITESPACE
    DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04'],
                   dtype='datetime64[ns]', freq=None)

    Use ``closed='left'`` to exclude `end` if it falls on the boundary.

    >>> ps.date_range(
    ...     start='2017-01-01', end='2017-01-04', closed='left'
    ... )  # doctest: +NORMALIZE_WHITESPACE
    DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03'], dtype='datetime64[ns]', freq=None)

    Use ``closed='right'`` to exclude `start` if it falls on the boundary.

    >>> ps.date_range(
    ...     start='2017-01-01', end='2017-01-04', closed='right'
    ... )  # doctest: +NORMALIZE_WHITESPACE
    DatetimeIndex(['2017-01-02', '2017-01-03', '2017-01-04'], dtype='datetime64[ns]', freq=None)
    """
def to_timedelta(arg, unit: Incomplete | None = None, errors: str = 'raise'):
    '''
    Convert argument to timedelta.

    Parameters
    ----------
    arg : str, timedelta, list-like or Series
        The data to be converted to timedelta.
    unit : str, optional
        Denotes the unit of the arg for numeric `arg`. Defaults to ``"ns"``.

        Possible values:
        * \'W\'
        * \'D\' / \'days\' / \'day\'
        * \'hours\' / \'hour\' / \'hr\' / \'h\'
        * \'m\' / \'minute\' / \'min\' / \'minutes\' / \'T\'
        * \'S\' / \'seconds\' / \'sec\' / \'second\'
        * \'ms\' / \'milliseconds\' / \'millisecond\' / \'milli\' / \'millis\' / \'L\'
        * \'us\' / \'microseconds\' / \'microsecond\' / \'micro\' / \'micros\' / \'U\'
        * \'ns\' / \'nanoseconds\' / \'nano\' / \'nanos\' / \'nanosecond\' / \'N\'

        Must not be specified when `arg` context strings and ``errors="raise"``.
    errors : {\'ignore\', \'raise\', \'coerce\'}, default \'raise\'
        - If \'raise\', then invalid parsing will raise an exception.
        - If \'coerce\', then invalid parsing will be set as NaT.
        - If \'ignore\', then invalid parsing will return the input.

    Returns
    -------
    ret : timedelta64, TimedeltaIndex or Series of timedelta64 if parsing succeeded.

    See Also
    --------
    DataFrame.astype : Cast argument to a specified dtype.
    to_datetime : Convert argument to datetime.

    Notes
    -----
    If the precision is higher than nanoseconds, the precision of the duration is
    truncated to nanoseconds for string inputs.

    Examples
    --------
    Parsing a single string to a Timedelta:

    >>> ps.to_timedelta(\'1 days 06:05:01.00003\')
    Timedelta(\'1 days 06:05:01.000030\')
    >>> ps.to_timedelta(\'15.5us\')  # doctest: +SKIP
    Timedelta(\'0 days 00:00:00.000015500\')

    Parsing a list or array of strings:

    >>> ps.to_timedelta([\'1 days 06:05:01.00003\', \'15.5us\', \'nan\'])  # doctest: +SKIP
    TimedeltaIndex([\'1 days 06:05:01.000030\', \'0 days 00:00:00.000015500\', NaT],
                   dtype=\'timedelta64[ns]\', freq=None)

    Converting numbers by specifying the `unit` keyword argument:

    >>> ps.to_timedelta(np.arange(5), unit=\'s\')  # doctest: +SKIP
    TimedeltaIndex([\'0 days 00:00:00\', \'0 days 00:00:01\', \'0 days 00:00:02\',
                    \'0 days 00:00:03\', \'0 days 00:00:04\'],
                   dtype=\'timedelta64[ns]\', freq=None)
    >>> ps.to_timedelta(np.arange(5), unit=\'d\')  # doctest: +NORMALIZE_WHITESPACE
    TimedeltaIndex([\'0 days\', \'1 days\', \'2 days\', \'3 days\', \'4 days\'],
                   dtype=\'timedelta64[ns]\', freq=None)
    '''
def timedelta_range(start: str | Any = None, end: str | Any = None, periods: int | None = None, freq: str | DateOffset | None = None, name: str | None = None, closed: str | None = None) -> TimedeltaIndex:
    """
    Return a fixed frequency TimedeltaIndex, with day as the default frequency.

    Parameters
    ----------
    start : str or timedelta-like, optional
        Left bound for generating timedeltas.
    end : str or timedelta-like, optional
        Right bound for generating timedeltas.
    periods : int, optional
        Number of periods to generate.
    freq : str or DateOffset, default 'D'
        Frequency strings can have multiples, e.g. '5H'.
    name : str, default None
        Name of the resulting TimedeltaIndex.
    closed : {None, 'left', 'right'}, optional
        Make the interval closed with respect to the given frequency to
        the 'left', 'right', or both sides (None, the default).

    Returns
    -------
    TimedeltaIndex

    Notes
    -----
    Of the four parameters ``start``, ``end``, ``periods``, and ``freq``,
    exactly three must be specified. If ``freq`` is omitted, the resulting
    ``TimedeltaIndex`` will have ``periods`` linearly spaced elements between
    ``start`` and ``end`` (closed on both sides).

    To learn more about the frequency strings, please see `this link
    <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases>`__.

    Examples
    --------
    >>> ps.timedelta_range(start='1 day', periods=4)  # doctest: +NORMALIZE_WHITESPACE
    TimedeltaIndex(['1 days', '2 days', '3 days', '4 days'], dtype='timedelta64[ns]', freq=None)

    The closed parameter specifies which endpoint is included.
    The default behavior is to include both endpoints.

    >>> ps.timedelta_range(start='1 day', periods=4, closed='right')
    ... # doctest: +NORMALIZE_WHITESPACE
    TimedeltaIndex(['2 days', '3 days', '4 days'], dtype='timedelta64[ns]', freq=None)

    The freq parameter specifies the frequency of the TimedeltaIndex.
    Only fixed frequencies can be passed, non-fixed frequencies such as ‘M’ (month end) will raise.

    >>> ps.timedelta_range(start='1 day', end='2 days', freq='6H')
    ... # doctest: +NORMALIZE_WHITESPACE
    TimedeltaIndex(['1 days 00:00:00', '1 days 06:00:00', '1 days 12:00:00',
                    '1 days 18:00:00', '2 days 00:00:00'],
                   dtype='timedelta64[ns]', freq=None)

    Specify start, end, and periods; the frequency is generated automatically (linearly spaced).

    >>> ps.timedelta_range(start='1 day', end='5 days', periods=4)
    ... # doctest: +NORMALIZE_WHITESPACE
    TimedeltaIndex(['1 days 00:00:00', '2 days 08:00:00', '3 days 16:00:00',
                    '5 days 00:00:00'],
                   dtype='timedelta64[ns]', freq=None)
    """
def get_dummies(data: DataFrame | Series, prefix: str | List[str] | Dict[str, str] | None = None, prefix_sep: str = '_', dummy_na: bool = False, columns: Name | List[Name] | None = None, sparse: bool = False, drop_first: bool = False, dtype: str | Dtype | None = None) -> DataFrame:
    '''
    Convert categorical variable into dummy/indicator variables, also
    known as one hot encoding.

    Parameters
    ----------
    data : array-like, Series, or DataFrame
    prefix : string, list of strings, or dict of strings, default None
        String to append DataFrame column names.
        Pass a list with length equal to the number of columns
        when calling get_dummies on a DataFrame. Alternatively, `prefix`
        can be a dictionary mapping column names to prefixes.
    prefix_sep : string, default \'_\'
        If appending prefix, separator/delimiter to use. Or pass a
        list or dictionary as with `prefix.`
    dummy_na : bool, default False
        Add a column to indicate NaNs, if False NaNs are ignored.
    columns : list-like, default None
        Column names in the DataFrame to be encoded.
        If `columns` is None then all the columns with
        `object` or `category` dtype will be converted.
    sparse : bool, default False
        Whether the dummy-encoded columns should be be backed by
        a :class:`SparseArray` (True) or a regular NumPy array (False).
        In pandas-on-Spark, this value must be "False".
    drop_first : bool, default False
        Whether to get k-1 dummies out of k categorical levels by removing the
        first level.
    dtype : dtype, default np.uint8
        Data type for new columns. Only a single dtype is allowed.

    Returns
    -------
    dummies : DataFrame

    See Also
    --------
    Series.str.get_dummies

    Examples
    --------
    >>> s = ps.Series(list(\'abca\'))

    >>> ps.get_dummies(s)
       a  b  c
    0  1  0  0
    1  0  1  0
    2  0  0  1
    3  1  0  0

    >>> df = ps.DataFrame({\'A\': [\'a\', \'b\', \'a\'], \'B\': [\'b\', \'a\', \'c\'],
    ...                    \'C\': [1, 2, 3]},
    ...                   columns=[\'A\', \'B\', \'C\'])

    >>> ps.get_dummies(df, prefix=[\'col1\', \'col2\'])
       C  col1_a  col1_b  col2_a  col2_b  col2_c
    0  1       1       0       0       1       0
    1  2       0       1       1       0       0
    2  3       1       0       0       0       1

    >>> ps.get_dummies(ps.Series(list(\'abcaa\')))
       a  b  c
    0  1  0  0
    1  0  1  0
    2  0  0  1
    3  1  0  0
    4  1  0  0

    >>> ps.get_dummies(ps.Series(list(\'abcaa\')), drop_first=True)
       b  c
    0  0  0
    1  1  0
    2  0  1
    3  0  0
    4  0  0

    >>> ps.get_dummies(ps.Series(list(\'abc\')), dtype=float)
         a    b    c
    0  1.0  0.0  0.0
    1  0.0  1.0  0.0
    2  0.0  0.0  1.0
    '''
def concat(objs: List[DataFrame | Series], axis: Axis = 0, join: str = 'outer', ignore_index: bool = False, sort: bool = False) -> Series | DataFrame:
    '''
    Concatenate pandas-on-Spark objects along a particular axis with optional set logic
    along the other axes.

    Parameters
    ----------
    objs : a sequence of Series or DataFrame
        Any None objects will be dropped silently unless
        they are all None in which case a ValueError will be raised
    axis : {0/\'index\', 1/\'columns\'}, default 0
        The axis to concatenate along.
    join : {\'inner\', \'outer\'}, default \'outer\'
        How to handle indexes on other axis (or axes).
    ignore_index : bool, default False
        If True, do not use the index values along the concatenation axis. The
        resulting axis will be labeled 0, ..., n - 1. This is useful if you are
        concatenating objects where the concatenation axis does not have
        meaningful indexing information. Note the index values on the other
        axes are still respected in the join.
    sort : bool, default False
        Sort non-concatenation axis if it is not already aligned.

    Returns
    -------
    object, type of objs
        When concatenating all ``Series`` along the index (axis=0), a
        ``Series`` is returned. When ``objs`` contains at least one
        ``DataFrame``, a ``DataFrame`` is returned. When concatenating along
        the columns (axis=1), a ``DataFrame`` is returned.

    See Also
    --------
    Series.append : Concatenate Series.
    DataFrame.join : Join DataFrames using indexes.
    DataFrame.merge : Merge DataFrames by indexes or columns.

    Examples
    --------
    >>> from pyspark.pandas.config import set_option, reset_option
    >>> set_option("compute.ops_on_diff_frames", True)

    Combine two ``Series``.

    >>> s1 = ps.Series([\'a\', \'b\'])
    >>> s2 = ps.Series([\'c\', \'d\'])
    >>> ps.concat([s1, s2])
    0    a
    1    b
    0    c
    1    d
    dtype: object

    Clear the existing index and reset it in the result
    by setting the ``ignore_index`` option to ``True``.

    >>> ps.concat([s1, s2], ignore_index=True)
    0    a
    1    b
    2    c
    3    d
    dtype: object

    Combine two ``DataFrame`` objects with identical columns.

    >>> df1 = ps.DataFrame([[\'a\', 1], [\'b\', 2]],
    ...                    columns=[\'letter\', \'number\'])
    >>> df1
      letter  number
    0      a       1
    1      b       2
    >>> df2 = ps.DataFrame([[\'c\', 3], [\'d\', 4]],
    ...                    columns=[\'letter\', \'number\'])
    >>> df2
      letter  number
    0      c       3
    1      d       4

    >>> ps.concat([df1, df2])
      letter  number
    0      a       1
    1      b       2
    0      c       3
    1      d       4

    Combine ``DataFrame`` and ``Series`` objects with different columns.

    >>> ps.concat([df2, s1])
      letter  number     0
    0      c     3.0  None
    1      d     4.0  None
    0   None     NaN     a
    1   None     NaN     b

    Combine ``DataFrame`` objects with overlapping columns
    and return everything. Columns outside the intersection will
    be filled with ``None`` values.

    >>> df3 = ps.DataFrame([[\'c\', 3, \'cat\'], [\'d\', 4, \'dog\']],
    ...                    columns=[\'letter\', \'number\', \'animal\'])
    >>> df3
      letter  number animal
    0      c       3    cat
    1      d       4    dog

    >>> ps.concat([df1, df3])
      letter  number animal
    0      a       1   None
    1      b       2   None
    0      c       3    cat
    1      d       4    dog

    Sort the columns.

    >>> ps.concat([df1, df3], sort=True)
      animal letter  number
    0   None      a       1
    1   None      b       2
    0    cat      c       3
    1    dog      d       4

    Combine ``DataFrame`` objects with overlapping columns
    and return only those that are shared by passing ``inner`` to
    the ``join`` keyword argument.

    >>> ps.concat([df1, df3], join="inner")
      letter  number
    0      a       1
    1      b       2
    0      c       3
    1      d       4

    >>> df4 = ps.DataFrame([[\'bird\', \'polly\'], [\'monkey\', \'george\']],
    ...                    columns=[\'animal\', \'name\'])

    Combine with column axis.

    >>> ps.concat([df1, df4], axis=1)
      letter  number  animal    name
    0      a       1    bird   polly
    1      b       2  monkey  george

    >>> reset_option("compute.ops_on_diff_frames")
    '''
def melt(frame: DataFrame, id_vars: Name | List[Name] | None = None, value_vars: Name | List[Name] | None = None, var_name: str | List[str] | None = None, value_name: str = 'value') -> DataFrame: ...
def isna(obj):
    """
    Detect missing values for an array-like object.

    This function takes a scalar or array-like object and indicates
    whether values are missing (``NaN`` in numeric arrays, ``None`` or ``NaN``
    in object arrays).

    Parameters
    ----------
    obj : scalar or array-like
        Object to check for null or missing values.

    Returns
    -------
    bool or array-like of bool
        For scalar input, returns a scalar boolean.
        For array input, returns an array of boolean indicating whether each
        corresponding element is missing.

    See Also
    --------
    Series.isna : Detect missing values in a Series.
    Series.isnull : Detect missing values in a Series.
    DataFrame.isna : Detect missing values in a DataFrame.
    DataFrame.isnull : Detect missing values in a DataFrame.
    Index.isna : Detect missing values in an Index.
    Index.isnull : Detect missing values in an Index.

    Examples
    --------
    Scalar arguments (including strings) result in a scalar boolean.

    >>> ps.isna('dog')
    False

    >>> ps.isna(np.nan)
    True

    ndarrays result in an ndarray of booleans.

    >>> array = np.array([[1, np.nan, 3], [4, 5, np.nan]])
    >>> array
    array([[ 1., nan,  3.],
           [ 4.,  5., nan]])
    >>> ps.isna(array)
    array([[False,  True, False],
           [False, False,  True]])

    For Series and DataFrame, the same type is returned, containing booleans.

    >>> df = ps.DataFrame({'a': ['ant', 'bee', 'cat'], 'b': ['dog', None, 'fly']})
    >>> df
         a     b
    0  ant   dog
    1  bee  None
    2  cat   fly

    >>> ps.isna(df)
           a      b
    0  False  False
    1  False   True
    2  False  False

    >>> ps.isnull(df.b)
    0    False
    1     True
    2    False
    Name: b, dtype: bool
    """
isnull = isna

def notna(obj):
    """
    Detect existing (non-missing) values.

    Return a boolean same-sized object indicating if the values are not NA.
    Non-missing values get mapped to True. NA values, such as None or
    :attr:`numpy.NaN`, get mapped to False values.

    Returns
    -------
    bool or array-like of bool
        Mask of bool values for each element that
        indicates whether an element is not an NA value.

    See Also
    --------
    isna : Detect missing values for an array-like object.
    Series.notna : Boolean inverse of Series.isna.
    DataFrame.notnull : Boolean inverse of DataFrame.isnull.
    Index.notna : Boolean inverse of Index.isna.
    Index.notnull : Boolean inverse of Index.isnull.

    Examples
    --------
    Show which entries in a DataFrame are not NA.

    >>> df = ps.DataFrame({'age': [5, 6, np.NaN],
    ...                    'born': [pd.NaT, pd.Timestamp('1939-05-27'),
    ...                             pd.Timestamp('1940-04-25')],
    ...                    'name': ['Alfred', 'Batman', ''],
    ...                    'toy': [None, 'Batmobile', 'Joker']})
    >>> df
       age       born    name        toy
    0  5.0        NaT  Alfred       None
    1  6.0 1939-05-27  Batman  Batmobile
    2  NaN 1940-04-25              Joker

    >>> df.notnull()
         age   born  name    toy
    0   True  False  True  False
    1   True   True  True   True
    2  False   True  True   True

    Show which entries in a Series are not NA.

    >>> ser = ps.Series([5, 6, np.NaN])
    >>> ser
    0    5.0
    1    6.0
    2    NaN
    dtype: float64

    >>> ps.notna(ser)
    0     True
    1     True
    2    False
    dtype: bool

    >>> ps.notna(ser.index)
    True
    """
notnull = notna

def merge(obj: DataFrame, right: DataFrame, how: str = 'inner', on: Name | List[Name] | None = None, left_on: Name | List[Name] | None = None, right_on: Name | List[Name] | None = None, left_index: bool = False, right_index: bool = False, suffixes: Tuple[str, str] = ('_x', '_y')) -> DataFrame:
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

        left: use only keys from left frame, like a SQL left outer join; preserve key
            order.
        right: use only keys from right frame, like a SQL right outer join; preserve key
            order.
        outer: use union of keys from both frames, like a SQL full outer join; sort keys
            lexicographically.
        inner: use intersection of keys from both frames, like a SQL inner join;
            preserve the order of the left keys.
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

    >>> merged = ps.merge(df1, df2, left_on='lkey', right_on='rkey')
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

    >>> ps.merge(left_psdf, right_psdf, left_index=True, right_index=True).sort_index()
       A  B
    1  2  x

    >>> ps.merge(left_psdf, right_psdf, left_index=True, right_index=True, how='left').sort_index()
       A     B
    0  1  None
    1  2     x

    >>> ps.merge(left_psdf, right_psdf, left_index=True, right_index=True, how='right').sort_index()
         A  B
    1  2.0  x
    2  NaN  y

    >>> ps.merge(left_psdf, right_psdf, left_index=True, right_index=True, how='outer').sort_index()
         A     B
    0  1.0  None
    1  2.0     x
    2  NaN     y

    Notes
    -----
    As described in #263, joining string columns currently returns None for missing values
        instead of NaN.
    """
def merge_asof(left: DataFrame | Series, right: DataFrame | Series, on: Name | None = None, left_on: Name | None = None, right_on: Name | None = None, left_index: bool = False, right_index: bool = False, by: Name | List[Name] | None = None, left_by: Name | List[Name] | None = None, right_by: Name | List[Name] | None = None, suffixes: Tuple[str, str] = ('_x', '_y'), tolerance: Any | None = None, allow_exact_matches: bool = True, direction: str = 'backward') -> DataFrame:
    '''
    Perform an asof merge.

    This is like a left-join except that we match on nearest
    key rather than equal keys.

    For each row in the left DataFrame:

      - A "backward" search selects the last row in the right DataFrame whose
        \'on\' key is less than or equal to the left\'s key.

      - A "forward" search selects the first row in the right DataFrame whose
        \'on\' key is greater than or equal to the left\'s key.

      - A "nearest" search selects the row in the right DataFrame who\'s \'on\'
        key is closest in absolute distance to the left\'s key.

    Optionally match on equivalent keys with \'by\' before searching with \'on\'.

    .. versionadded:: 3.3.0

    Parameters
    ----------
    left : DataFrame or named Series
    right : DataFrame or named Series
    on : label
        Field name to join on. Must be found in both DataFrames.
        The data MUST be ordered. This must be a numeric column,
        such as datetimelike, integer, or float. On or left_on/right_on
        must be given.
    left_on : label
        Field name to join on in left DataFrame.
    right_on : label
        Field name to join on in right DataFrame.
    left_index : bool
        Use the index of the left DataFrame as the join key.
    right_index : bool
        Use the index of the right DataFrame as the join key.
    by : column name or list of column names
        Match on these columns before performing merge operation.
    left_by : column name
        Field names to match on in the left DataFrame.
    right_by : column name
        Field names to match on in the right DataFrame.
    suffixes : 2-length sequence (tuple, list, ...)
        Suffix to apply to overlapping column names in the left and right
        side, respectively.
    tolerance : int or Timedelta, optional, default None
        Select asof tolerance within this range; must be compatible
        with the merge index.
    allow_exact_matches : bool, default True

        - If True, allow matching with the same \'on\' value
          (i.e. less-than-or-equal-to / greater-than-or-equal-to)
        - If False, don\'t match the same \'on\' value
          (i.e., strictly less-than / strictly greater-than).

    direction : \'backward\' (default), \'forward\', or \'nearest\'
        Whether to search for prior, subsequent, or closest matches.

    Returns
    -------
    merged : DataFrame

    See Also
    --------
    merge : Merge with a database-style join.
    merge_ordered : Merge with optional filling/interpolation.

    Examples
    --------
    >>> left = ps.DataFrame({"a": [1, 5, 10], "left_val": ["a", "b", "c"]})
    >>> left
        a left_val
    0   1        a
    1   5        b
    2  10        c

    >>> right = ps.DataFrame({"a": [1, 2, 3, 6, 7], "right_val": [1, 2, 3, 6, 7]})
    >>> right
       a  right_val
    0  1          1
    1  2          2
    2  3          3
    3  6          6
    4  7          7

    >>> ps.merge_asof(left, right, on="a").sort_values("a").reset_index(drop=True)
        a left_val  right_val
    0   1        a          1
    1   5        b          3
    2  10        c          7

    >>> ps.merge_asof(
    ...     left,
    ...     right,
    ...     on="a",
    ...     allow_exact_matches=False
    ... ).sort_values("a").reset_index(drop=True)
        a left_val  right_val
    0   1        a        NaN
    1   5        b        3.0
    2  10        c        7.0

    >>> ps.merge_asof(
    ...     left,
    ...     right,
    ...     on="a",
    ...     direction="forward"
    ... ).sort_values("a").reset_index(drop=True)
        a left_val  right_val
    0   1        a        1.0
    1   5        b        6.0
    2  10        c        NaN

    >>> ps.merge_asof(
    ...     left,
    ...     right,
    ...     on="a",
    ...     direction="nearest"
    ... ).sort_values("a").reset_index(drop=True)
        a left_val  right_val
    0   1        a          1
    1   5        b          6
    2  10        c          7

    We can use indexed DataFrames as well.

    >>> left = ps.DataFrame({"left_val": ["a", "b", "c"]}, index=[1, 5, 10])
    >>> left
       left_val
    1         a
    5         b
    10        c

    >>> right = ps.DataFrame({"right_val": [1, 2, 3, 6, 7]}, index=[1, 2, 3, 6, 7])
    >>> right
       right_val
    1          1
    2          2
    3          3
    6          6
    7          7

    >>> ps.merge_asof(left, right, left_index=True, right_index=True).sort_index()
       left_val  right_val
    1         a          1
    5         b          3
    10        c          7

    Here is a real-world times-series example

    >>> quotes = ps.DataFrame(
    ...     {
    ...         "time": [
    ...             pd.Timestamp("2016-05-25 13:30:00.023"),
    ...             pd.Timestamp("2016-05-25 13:30:00.023"),
    ...             pd.Timestamp("2016-05-25 13:30:00.030"),
    ...             pd.Timestamp("2016-05-25 13:30:00.041"),
    ...             pd.Timestamp("2016-05-25 13:30:00.048"),
    ...             pd.Timestamp("2016-05-25 13:30:00.049"),
    ...             pd.Timestamp("2016-05-25 13:30:00.072"),
    ...             pd.Timestamp("2016-05-25 13:30:00.075")
    ...         ],
    ...         "ticker": [
    ...                "GOOG",
    ...                "MSFT",
    ...                "MSFT",
    ...                "MSFT",
    ...                "GOOG",
    ...                "AAPL",
    ...                "GOOG",
    ...                "MSFT"
    ...            ],
    ...            "bid": [720.50, 51.95, 51.97, 51.99, 720.50, 97.99, 720.50, 52.01],
    ...            "ask": [720.93, 51.96, 51.98, 52.00, 720.93, 98.01, 720.88, 52.03]
    ...     }
    ... )
    >>> quotes
                         time ticker     bid     ask
    0 2016-05-25 13:30:00.023   GOOG  720.50  720.93
    1 2016-05-25 13:30:00.023   MSFT   51.95   51.96
    2 2016-05-25 13:30:00.030   MSFT   51.97   51.98
    3 2016-05-25 13:30:00.041   MSFT   51.99   52.00
    4 2016-05-25 13:30:00.048   GOOG  720.50  720.93
    5 2016-05-25 13:30:00.049   AAPL   97.99   98.01
    6 2016-05-25 13:30:00.072   GOOG  720.50  720.88
    7 2016-05-25 13:30:00.075   MSFT   52.01   52.03

    >>> trades = ps.DataFrame(
    ...        {
    ...            "time": [
    ...                pd.Timestamp("2016-05-25 13:30:00.023"),
    ...                pd.Timestamp("2016-05-25 13:30:00.038"),
    ...                pd.Timestamp("2016-05-25 13:30:00.048"),
    ...                pd.Timestamp("2016-05-25 13:30:00.048"),
    ...                pd.Timestamp("2016-05-25 13:30:00.048")
    ...            ],
    ...            "ticker": ["MSFT", "MSFT", "GOOG", "GOOG", "AAPL"],
    ...            "price": [51.95, 51.95, 720.77, 720.92, 98.0],
    ...            "quantity": [75, 155, 100, 100, 100]
    ...        }
    ...    )
    >>> trades
                         time ticker   price  quantity
    0 2016-05-25 13:30:00.023   MSFT   51.95        75
    1 2016-05-25 13:30:00.038   MSFT   51.95       155
    2 2016-05-25 13:30:00.048   GOOG  720.77       100
    3 2016-05-25 13:30:00.048   GOOG  720.92       100
    4 2016-05-25 13:30:00.048   AAPL   98.00       100

    By default we are taking the asof of the quotes

    >>> ps.merge_asof(
    ...    trades, quotes, on="time", by="ticker"
    ... ).sort_values(["time", "ticker", "price"]).reset_index(drop=True)
                         time ticker   price  quantity     bid     ask
    0 2016-05-25 13:30:00.023   MSFT   51.95        75   51.95   51.96
    1 2016-05-25 13:30:00.038   MSFT   51.95       155   51.97   51.98
    2 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN
    3 2016-05-25 13:30:00.048   GOOG  720.77       100  720.50  720.93
    4 2016-05-25 13:30:00.048   GOOG  720.92       100  720.50  720.93

    We only asof within 2ms between the quote time and the trade time

    >>> ps.merge_asof(
    ...     trades,
    ...     quotes,
    ...     on="time",
    ...     by="ticker",
    ...     tolerance=F.expr("INTERVAL 2 MILLISECONDS")  # pd.Timedelta("2ms")
    ... ).sort_values(["time", "ticker", "price"]).reset_index(drop=True)
                         time ticker   price  quantity     bid     ask
    0 2016-05-25 13:30:00.023   MSFT   51.95        75   51.95   51.96
    1 2016-05-25 13:30:00.038   MSFT   51.95       155     NaN     NaN
    2 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN
    3 2016-05-25 13:30:00.048   GOOG  720.77       100  720.50  720.93
    4 2016-05-25 13:30:00.048   GOOG  720.92       100  720.50  720.93

    We only asof within 10ms between the quote time and the trade time
    and we exclude exact matches on time. However *prior* data will
    propagate forward

    >>> ps.merge_asof(
    ...     trades,
    ...     quotes,
    ...     on="time",
    ...     by="ticker",
    ...     tolerance=F.expr("INTERVAL 10 MILLISECONDS"),  # pd.Timedelta("10ms")
    ...     allow_exact_matches=False
    ... ).sort_values(["time", "ticker", "price"]).reset_index(drop=True)
                         time ticker   price  quantity     bid     ask
    0 2016-05-25 13:30:00.023   MSFT   51.95        75     NaN     NaN
    1 2016-05-25 13:30:00.038   MSFT   51.95       155   51.97   51.98
    2 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN
    3 2016-05-25 13:30:00.048   GOOG  720.77       100     NaN     NaN
    4 2016-05-25 13:30:00.048   GOOG  720.92       100     NaN     NaN
    '''
def to_numeric(arg, errors: str = 'raise'):
    '''
    Convert argument to a numeric type.

    Parameters
    ----------
    arg : scalar, list, tuple, 1-d array, or Series
        Argument to be converted.
    errors : {\'raise\', \'coerce\'}, default \'raise\'
        * If \'coerce\', then invalid parsing will be set as NaN.
        * If \'raise\', then invalid parsing will raise an exception.
        * If \'ignore\', then invalid parsing will return the input.

        .. note:: \'ignore\' doesn\'t work yet when `arg` is pandas-on-Spark Series.

    Returns
    -------
    ret : numeric if parsing succeeded.

    See Also
    --------
    DataFrame.astype : Cast argument to a specified dtype.
    to_datetime : Convert argument to datetime.
    to_timedelta : Convert argument to timedelta.
    numpy.ndarray.astype : Cast a numpy array to a specified type.

    Examples
    --------

    >>> psser = ps.Series([\'1.0\', \'2\', \'-3\'])
    >>> psser
    0    1.0
    1      2
    2     -3
    dtype: object

    >>> ps.to_numeric(psser)
    0    1.0
    1    2.0
    2   -3.0
    dtype: float32

    If given Series contains invalid value to cast float, just cast it to `np.nan`
    when `errors` is set to "coerce".

    >>> psser = ps.Series([\'apple\', \'1.0\', \'2\', \'-3\'])
    >>> psser
    0    apple
    1      1.0
    2        2
    3       -3
    dtype: object

    >>> ps.to_numeric(psser, errors="coerce")
    0    NaN
    1    1.0
    2    2.0
    3   -3.0
    dtype: float32

    Also support for list, tuple, np.array, or a scalar

    >>> ps.to_numeric([\'1.0\', \'2\', \'-3\'])
    array([ 1.,  2., -3.])

    >>> ps.to_numeric((\'1.0\', \'2\', \'-3\'))
    array([ 1.,  2., -3.])

    >>> ps.to_numeric(np.array([\'1.0\', \'2\', \'-3\']))
    array([ 1.,  2., -3.])

    >>> ps.to_numeric(\'1.0\')
    1.0
    '''
def broadcast(obj: DataFrame) -> DataFrame:
    """
    Marks a DataFrame as small enough for use in broadcast joins.

    .. deprecated:: 3.2.0
        Use :func:`DataFrame.spark.hint` instead.

    Parameters
    ----------
    obj : DataFrame

    Returns
    -------
    ret : DataFrame with broadcast hint.

    See Also
    --------
    DataFrame.merge : Merge DataFrame objects with a database-style join.
    DataFrame.join : Join columns of another DataFrame.
    DataFrame.update : Modify in place using non-NA values from another DataFrame.
    DataFrame.hint : Specifies some hint on the current DataFrame.

    Examples
    --------
    >>> df1 = ps.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
    ...                     'value': [1, 2, 3, 5]},
    ...                    columns=['lkey', 'value']).set_index('lkey')
    >>> df2 = ps.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
    ...                     'value': [5, 6, 7, 8]},
    ...                    columns=['rkey', 'value']).set_index('rkey')
    >>> merged = df1.merge(ps.broadcast(df2), left_index=True, right_index=True)
    >>> merged.spark.explain()  # doctest: +ELLIPSIS
    == Physical Plan ==
    ...
    ...BroadcastHashJoin...
    ...
    """
def read_orc(path: str, columns: List[str] | None = None, index_col: str | List[str] | None = None, **options: Any) -> DataFrame:
    '''
    Load an ORC object from the file path, returning a DataFrame.

    Parameters
    ----------
    path : str
        The path string storing the ORC file to be read.
    columns : list, default None
        If not None, only these columns will be read from the file.
    index_col : str or list of str, optional, default: None
        Index column of table in Spark.
    options : dict
        All other options passed directly into Spark\'s data source.

    Returns
    -------
    DataFrame

    Examples
    --------
    >>> ps.range(1).to_orc(\'%s/read_spark_io/data.orc\' % path)
    >>> ps.read_orc(\'%s/read_spark_io/data.orc\' % path, columns=[\'id\'])
       id
    0   0

    You can preserve the index in the roundtrip as below.

    >>> ps.range(1).to_orc(\'%s/read_spark_io/data.orc\' % path, index_col="index")
    >>> ps.read_orc(\'%s/read_spark_io/data.orc\' % path, columns=[\'id\'], index_col="index")
    ... # doctest: +NORMALIZE_WHITESPACE
           id
    index
    0       0
    '''
