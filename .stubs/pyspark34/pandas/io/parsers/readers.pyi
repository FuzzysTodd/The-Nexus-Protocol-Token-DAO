import csv
from _typeshed import Incomplete
from collections import abc
from pandas._libs import lib as lib
from pandas._libs.parsers import STR_NA_VALUES as STR_NA_VALUES
from pandas._typing import CSVEngine as CSVEngine, CompressionOptions as CompressionOptions, DtypeArg as DtypeArg, DtypeBackend as DtypeBackend, FilePath as FilePath, IndexLabel as IndexLabel, ReadCsvBuffer as ReadCsvBuffer, StorageOptions as StorageOptions
from pandas.core.dtypes.common import is_file_like as is_file_like, is_float as is_float, is_integer as is_integer, is_list_like as is_list_like
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.indexes.api import RangeIndex as RangeIndex
from pandas.errors import AbstractMethodError as AbstractMethodError, ParserWarning as ParserWarning
from pandas.io.common import IOHandles as IOHandles, get_handle as get_handle, stringify_path as stringify_path, validate_header_arg as validate_header_arg
from pandas.io.parsers.arrow_parser_wrapper import ArrowParserWrapper as ArrowParserWrapper
from pandas.io.parsers.base_parser import ParserBase as ParserBase, is_index_col as is_index_col, parser_defaults as parser_defaults
from pandas.io.parsers.c_parser_wrapper import CParserWrapper as CParserWrapper
from pandas.io.parsers.python_parser import FixedWidthFieldParser as FixedWidthFieldParser, PythonParser as PythonParser
from pandas.util._decorators import Appender as Appender
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import check_dtype_backend as check_dtype_backend
from types import TracebackType
from typing import Any, Hashable, Literal, NamedTuple, Sequence, overload

class _DeprecationConfig(NamedTuple):
    default_value: Any
    msg: str | None

@overload
def validate_integer(name, val: None, min_val: int = ...) -> None: ...
@overload
def validate_integer(name, val: float, min_val: int = ...) -> int: ...
@overload
def validate_integer(name, val: int | None, min_val: int = ...) -> int | None: ...
@overload
def read_csv(filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str], *, sep: str | None | lib.NoDefault = ..., delimiter: str | None | lib.NoDefault = ..., header: int | Sequence[int] | None | Literal['infer'] = ..., names: Sequence[Hashable] | None | lib.NoDefault = ..., index_col: IndexLabel | Literal[False] | None = ..., usecols=..., dtype: DtypeArg | None = ..., engine: CSVEngine | None = ..., converters=..., true_values=..., false_values=..., skipinitialspace: bool = ..., skiprows=..., skipfooter: int = ..., nrows: int | None = ..., na_values=..., keep_default_na: bool = ..., na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ..., parse_dates: bool | Sequence[Hashable] | None = ..., infer_datetime_format: bool | lib.NoDefault = ..., keep_date_col: bool = ..., date_parser=..., date_format: str | None = ..., dayfirst: bool = ..., cache_dates: bool = ..., iterator: Literal[True], chunksize: int | None = ..., compression: CompressionOptions = ..., thousands: str | None = ..., decimal: str = ..., lineterminator: str | None = ..., quotechar: str = ..., quoting: int = ..., doublequote: bool = ..., escapechar: str | None = ..., comment: str | None = ..., encoding: str | None = ..., encoding_errors: str | None = ..., dialect: str | csv.Dialect | None = ..., on_bad_lines=..., delim_whitespace: bool = ..., low_memory=..., memory_map: bool = ..., float_precision: Literal['high', 'legacy'] | None = ..., storage_options: StorageOptions = ..., dtype_backend: DtypeBackend | lib.NoDefault = ...) -> TextFileReader: ...
@overload
def read_csv(filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str], *, sep: str | None | lib.NoDefault = ..., delimiter: str | None | lib.NoDefault = ..., header: int | Sequence[int] | None | Literal['infer'] = ..., names: Sequence[Hashable] | None | lib.NoDefault = ..., index_col: IndexLabel | Literal[False] | None = ..., usecols=..., dtype: DtypeArg | None = ..., engine: CSVEngine | None = ..., converters=..., true_values=..., false_values=..., skipinitialspace: bool = ..., skiprows=..., skipfooter: int = ..., nrows: int | None = ..., na_values=..., keep_default_na: bool = ..., na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ..., parse_dates: bool | Sequence[Hashable] | None = ..., infer_datetime_format: bool | lib.NoDefault = ..., keep_date_col: bool = ..., date_parser=..., date_format: str | None = ..., dayfirst: bool = ..., cache_dates: bool = ..., iterator: bool = ..., chunksize: int, compression: CompressionOptions = ..., thousands: str | None = ..., decimal: str = ..., lineterminator: str | None = ..., quotechar: str = ..., quoting: int = ..., doublequote: bool = ..., escapechar: str | None = ..., comment: str | None = ..., encoding: str | None = ..., encoding_errors: str | None = ..., dialect: str | csv.Dialect | None = ..., on_bad_lines=..., delim_whitespace: bool = ..., low_memory=..., memory_map: bool = ..., float_precision: Literal['high', 'legacy'] | None = ..., storage_options: StorageOptions = ..., dtype_backend: DtypeBackend | lib.NoDefault = ...) -> TextFileReader: ...
@overload
def read_csv(filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str], *, sep: str | None | lib.NoDefault = ..., delimiter: str | None | lib.NoDefault = ..., header: int | Sequence[int] | None | Literal['infer'] = ..., names: Sequence[Hashable] | None | lib.NoDefault = ..., index_col: IndexLabel | Literal[False] | None = ..., usecols=..., dtype: DtypeArg | None = ..., engine: CSVEngine | None = ..., converters=..., true_values=..., false_values=..., skipinitialspace: bool = ..., skiprows=..., skipfooter: int = ..., nrows: int | None = ..., na_values=..., keep_default_na: bool = ..., na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ..., parse_dates: bool | Sequence[Hashable] | None = ..., infer_datetime_format: bool | lib.NoDefault = ..., keep_date_col: bool = ..., date_parser=..., date_format: str | None = ..., dayfirst: bool = ..., cache_dates: bool = ..., iterator: Literal[False] = ..., chunksize: None = ..., compression: CompressionOptions = ..., thousands: str | None = ..., decimal: str = ..., lineterminator: str | None = ..., quotechar: str = ..., quoting: int = ..., doublequote: bool = ..., escapechar: str | None = ..., comment: str | None = ..., encoding: str | None = ..., encoding_errors: str | None = ..., dialect: str | csv.Dialect | None = ..., on_bad_lines=..., delim_whitespace: bool = ..., low_memory=..., memory_map: bool = ..., float_precision: Literal['high', 'legacy'] | None = ..., storage_options: StorageOptions = ..., dtype_backend: DtypeBackend | lib.NoDefault = ...) -> DataFrame: ...
@overload
def read_csv(filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str], *, sep: str | None | lib.NoDefault = ..., delimiter: str | None | lib.NoDefault = ..., header: int | Sequence[int] | None | Literal['infer'] = ..., names: Sequence[Hashable] | None | lib.NoDefault = ..., index_col: IndexLabel | Literal[False] | None = ..., usecols=..., dtype: DtypeArg | None = ..., engine: CSVEngine | None = ..., converters=..., true_values=..., false_values=..., skipinitialspace: bool = ..., skiprows=..., skipfooter: int = ..., nrows: int | None = ..., na_values=..., keep_default_na: bool = ..., na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ..., parse_dates: bool | Sequence[Hashable] | None = ..., infer_datetime_format: bool | lib.NoDefault = ..., keep_date_col: bool = ..., date_parser=..., date_format: str | None = ..., dayfirst: bool = ..., cache_dates: bool = ..., iterator: bool = ..., chunksize: int | None = ..., compression: CompressionOptions = ..., thousands: str | None = ..., decimal: str = ..., lineterminator: str | None = ..., quotechar: str = ..., quoting: int = ..., doublequote: bool = ..., escapechar: str | None = ..., comment: str | None = ..., encoding: str | None = ..., encoding_errors: str | None = ..., dialect: str | csv.Dialect | None = ..., on_bad_lines=..., delim_whitespace: bool = ..., low_memory=..., memory_map: bool = ..., float_precision: Literal['high', 'legacy'] | None = ..., storage_options: StorageOptions = ..., dtype_backend: DtypeBackend | lib.NoDefault = ...) -> DataFrame | TextFileReader: ...
@overload
def read_table(filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str], *, sep: str | None | lib.NoDefault = ..., delimiter: str | None | lib.NoDefault = ..., header: int | Sequence[int] | None | Literal['infer'] = ..., names: Sequence[Hashable] | None | lib.NoDefault = ..., index_col: IndexLabel | Literal[False] | None = ..., usecols=..., dtype: DtypeArg | None = ..., engine: CSVEngine | None = ..., converters=..., true_values=..., false_values=..., skipinitialspace: bool = ..., skiprows=..., skipfooter: int = ..., nrows: int | None = ..., na_values=..., keep_default_na: bool = ..., na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ..., parse_dates: bool | Sequence[Hashable] = ..., infer_datetime_format: bool | lib.NoDefault = ..., keep_date_col: bool = ..., date_parser=..., date_format: str | None = ..., dayfirst: bool = ..., cache_dates: bool = ..., iterator: Literal[True], chunksize: int | None = ..., compression: CompressionOptions = ..., thousands: str | None = ..., decimal: str = ..., lineterminator: str | None = ..., quotechar: str = ..., quoting: int = ..., doublequote: bool = ..., escapechar: str | None = ..., comment: str | None = ..., encoding: str | None = ..., encoding_errors: str | None = ..., dialect: str | csv.Dialect | None = ..., on_bad_lines=..., delim_whitespace: bool = ..., low_memory=..., memory_map: bool = ..., float_precision: str | None = ..., storage_options: StorageOptions = ..., dtype_backend: DtypeBackend | lib.NoDefault = ...) -> TextFileReader: ...
@overload
def read_table(filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str], *, sep: str | None | lib.NoDefault = ..., delimiter: str | None | lib.NoDefault = ..., header: int | Sequence[int] | None | Literal['infer'] = ..., names: Sequence[Hashable] | None | lib.NoDefault = ..., index_col: IndexLabel | Literal[False] | None = ..., usecols=..., dtype: DtypeArg | None = ..., engine: CSVEngine | None = ..., converters=..., true_values=..., false_values=..., skipinitialspace: bool = ..., skiprows=..., skipfooter: int = ..., nrows: int | None = ..., na_values=..., keep_default_na: bool = ..., na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ..., parse_dates: bool | Sequence[Hashable] = ..., infer_datetime_format: bool | lib.NoDefault = ..., keep_date_col: bool = ..., date_parser=..., date_format: str | None = ..., dayfirst: bool = ..., cache_dates: bool = ..., iterator: bool = ..., chunksize: int, compression: CompressionOptions = ..., thousands: str | None = ..., decimal: str = ..., lineterminator: str | None = ..., quotechar: str = ..., quoting: int = ..., doublequote: bool = ..., escapechar: str | None = ..., comment: str | None = ..., encoding: str | None = ..., encoding_errors: str | None = ..., dialect: str | csv.Dialect | None = ..., on_bad_lines=..., delim_whitespace: bool = ..., low_memory=..., memory_map: bool = ..., float_precision: str | None = ..., storage_options: StorageOptions = ..., dtype_backend: DtypeBackend | lib.NoDefault = ...) -> TextFileReader: ...
@overload
def read_table(filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str], *, sep: str | None | lib.NoDefault = ..., delimiter: str | None | lib.NoDefault = ..., header: int | Sequence[int] | None | Literal['infer'] = ..., names: Sequence[Hashable] | None | lib.NoDefault = ..., index_col: IndexLabel | Literal[False] | None = ..., usecols=..., dtype: DtypeArg | None = ..., engine: CSVEngine | None = ..., converters=..., true_values=..., false_values=..., skipinitialspace: bool = ..., skiprows=..., skipfooter: int = ..., nrows: int | None = ..., na_values=..., keep_default_na: bool = ..., na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ..., parse_dates: bool | Sequence[Hashable] = ..., infer_datetime_format: bool | lib.NoDefault = ..., keep_date_col: bool = ..., date_parser=..., date_format: str | None = ..., dayfirst: bool = ..., cache_dates: bool = ..., iterator: Literal[False] = ..., chunksize: None = ..., compression: CompressionOptions = ..., thousands: str | None = ..., decimal: str = ..., lineterminator: str | None = ..., quotechar: str = ..., quoting: int = ..., doublequote: bool = ..., escapechar: str | None = ..., comment: str | None = ..., encoding: str | None = ..., encoding_errors: str | None = ..., dialect: str | csv.Dialect | None = ..., on_bad_lines=..., delim_whitespace: bool = ..., low_memory=..., memory_map: bool = ..., float_precision: str | None = ..., storage_options: StorageOptions = ..., dtype_backend: DtypeBackend | lib.NoDefault = ...) -> DataFrame: ...
@overload
def read_table(filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str], *, sep: str | None | lib.NoDefault = ..., delimiter: str | None | lib.NoDefault = ..., header: int | Sequence[int] | None | Literal['infer'] = ..., names: Sequence[Hashable] | None | lib.NoDefault = ..., index_col: IndexLabel | Literal[False] | None = ..., usecols=..., dtype: DtypeArg | None = ..., engine: CSVEngine | None = ..., converters=..., true_values=..., false_values=..., skipinitialspace: bool = ..., skiprows=..., skipfooter: int = ..., nrows: int | None = ..., na_values=..., keep_default_na: bool = ..., na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ..., parse_dates: bool | Sequence[Hashable] = ..., infer_datetime_format: bool | lib.NoDefault = ..., keep_date_col: bool = ..., date_parser=..., date_format: str | None = ..., dayfirst: bool = ..., cache_dates: bool = ..., iterator: bool = ..., chunksize: int | None = ..., compression: CompressionOptions = ..., thousands: str | None = ..., decimal: str = ..., lineterminator: str | None = ..., quotechar: str = ..., quoting: int = ..., doublequote: bool = ..., escapechar: str | None = ..., comment: str | None = ..., encoding: str | None = ..., encoding_errors: str | None = ..., dialect: str | csv.Dialect | None = ..., on_bad_lines=..., delim_whitespace: bool = ..., low_memory=..., memory_map: bool = ..., float_precision: str | None = ..., storage_options: StorageOptions = ..., dtype_backend: DtypeBackend | lib.NoDefault = ...) -> DataFrame | TextFileReader: ...
def read_fwf(filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str], *, colspecs: Sequence[tuple[int, int]] | str | None = 'infer', widths: Sequence[int] | None = None, infer_nrows: int = 100, dtype_backend: DtypeBackend | lib.NoDefault = ..., **kwds) -> DataFrame | TextFileReader:
    '''
    Read a table of fixed-width formatted lines into DataFrame.

    Also supports optionally iterating or breaking of the file
    into chunks.

    Additional help can be found in the `online docs for IO Tools
    <https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html>`_.

    Parameters
    ----------
    filepath_or_buffer : str, path object, or file-like object
        String, path object (implementing ``os.PathLike[str]``), or file-like
        object implementing a text ``read()`` function.The string could be a URL.
        Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is
        expected. A local file could be:
        ``file://localhost/path/to/table.csv``.
    colspecs : list of tuple (int, int) or \'infer\'. optional
        A list of tuples giving the extents of the fixed-width
        fields of each line as half-open intervals (i.e.,  [from, to[ ).
        String value \'infer\' can be used to instruct the parser to try
        detecting the column specifications from the first 100 rows of
        the data which are not being skipped via skiprows (default=\'infer\').
    widths : list of int, optional
        A list of field widths which can be used instead of \'colspecs\' if
        the intervals are contiguous.
    infer_nrows : int, default 100
        The number of rows to consider when letting the parser determine the
        `colspecs`.
    dtype_backend : {"numpy_nullable", "pyarrow"}, defaults to NumPy backed DataFrames
        Which dtype_backend to use, e.g. whether a DataFrame should have NumPy
        arrays, nullable dtypes are used for all dtypes that have a nullable
        implementation when "numpy_nullable" is set, pyarrow is used for all
        dtypes if "pyarrow" is set.

        The dtype_backends are still experimential.

        .. versionadded:: 2.0

    **kwds : optional
        Optional keyword arguments can be passed to ``TextFileReader``.

    Returns
    -------
    DataFrame or TextFileReader
        A comma-separated values (csv) file is returned as two-dimensional
        data structure with labeled axes.

    See Also
    --------
    DataFrame.to_csv : Write DataFrame to a comma-separated values (csv) file.
    read_csv : Read a comma-separated values (csv) file into DataFrame.

    Examples
    --------
    >>> pd.read_fwf(\'data.csv\')  # doctest: +SKIP
    '''

class TextFileReader(abc.Iterator):
    """

    Passed dialect overrides any of the related parser options

    """
    engine: Incomplete
    orig_options: Incomplete
    chunksize: Incomplete
    nrows: Incomplete
    handles: Incomplete
    def __init__(self, f: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str] | list, engine: CSVEngine | None = None, **kwds) -> None: ...
    def close(self) -> None: ...
    def __next__(self) -> DataFrame: ...
    def read(self, nrows: int | None = None) -> DataFrame: ...
    def get_chunk(self, size: int | None = None) -> DataFrame: ...
    def __enter__(self) -> TextFileReader: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...

def TextParser(*args, **kwds) -> TextFileReader:
    """
    Converts lists of lists/tuples into DataFrames with proper type inference
    and optional (e.g. string to datetime) conversion. Also enables iterating
    lazily over chunks of large files

    Parameters
    ----------
    data : file-like object or list
    delimiter : separator character to use
    dialect : str or csv.Dialect instance, optional
        Ignored if delimiter is longer than 1 character
    names : sequence, default
    header : int, default 0
        Row to use to parse column labels. Defaults to the first row. Prior
        rows will be discarded
    index_col : int or list, optional
        Column or columns to use as the (possibly hierarchical) index
    has_index_names: bool, default False
        True if the cols defined in index_col have an index name and are
        not in the header.
    na_values : scalar, str, list-like, or dict, optional
        Additional strings to recognize as NA/NaN.
    keep_default_na : bool, default True
    thousands : str, optional
        Thousands separator
    comment : str, optional
        Comment out remainder of line
    parse_dates : bool, default False
    keep_date_col : bool, default False
    date_parser : function, optional

        .. deprecated:: 2.0.0
    date_format : str or dict of column -> format, default ``None``

        .. versionadded:: 2.0.0
    skiprows : list of integers
        Row numbers to skip
    skipfooter : int
        Number of line at bottom of file to skip
    converters : dict, optional
        Dict of functions for converting values in certain columns. Keys can
        either be integers or column labels, values are functions that take one
        input argument, the cell (not column) content, and return the
        transformed content.
    encoding : str, optional
        Encoding to use for UTF when reading/writing (ex. 'utf-8')
    float_precision : str, optional
        Specifies which converter the C engine should use for floating-point
        values. The options are `None` or `high` for the ordinary converter,
        `legacy` for the original lower precision pandas converter, and
        `round_trip` for the round-trip converter.

        .. versionchanged:: 1.2
    """

MANDATORY_DIALECT_ATTRS: Incomplete
