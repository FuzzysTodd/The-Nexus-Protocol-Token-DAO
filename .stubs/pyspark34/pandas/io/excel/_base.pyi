import abc
from _typeshed import Incomplete
from pandas._config import config as config
from pandas._libs import lib as lib
from pandas._libs.parsers import STR_NA_VALUES as STR_NA_VALUES
from pandas._typing import DtypeArg as DtypeArg, DtypeBackend as DtypeBackend, FilePath as FilePath, IntStrT as IntStrT, ReadBuffer as ReadBuffer, StorageOptions as StorageOptions, WriteExcelBuffer as WriteExcelBuffer
from pandas.compat._optional import get_version as get_version, import_optional_dependency as import_optional_dependency
from pandas.core.dtypes.common import is_bool as is_bool, is_float as is_float, is_integer as is_integer, is_list_like as is_list_like
from pandas.core.frame import DataFrame as DataFrame
from pandas.errors import EmptyDataError as EmptyDataError
from pandas.io.common import IOHandles as IOHandles, get_handle as get_handle, stringify_path as stringify_path, validate_header_arg as validate_header_arg
from pandas.io.excel._odfreader import ODFReader as ODFReader
from pandas.io.excel._openpyxl import OpenpyxlReader as OpenpyxlReader
from pandas.io.excel._pyxlsb import PyxlsbReader as PyxlsbReader
from pandas.io.excel._util import fill_mi_header as fill_mi_header, get_default_engine as get_default_engine, get_writer as get_writer, maybe_convert_usecols as maybe_convert_usecols, pop_header_name as pop_header_name
from pandas.io.excel._xlrd import XlrdReader as XlrdReader
from pandas.io.parsers import TextParser as TextParser
from pandas.io.parsers.readers import validate_integer as validate_integer
from pandas.util._decorators import Appender as Appender, doc as doc
from pandas.util._validators import check_dtype_backend as check_dtype_backend
from pandas.util.version import Version as Version
from types import TracebackType
from typing import Any, Callable, Hashable, Iterable, Literal, Sequence, overload

@overload
def read_excel(io, sheet_name: str | int = ..., *, header: int | Sequence[int] | None = ..., names: list[str] | None = ..., index_col: int | Sequence[int] | None = ..., usecols: int | str | Sequence[int] | Sequence[str] | Callable[[str], bool] | None = ..., dtype: DtypeArg | None = ..., engine: Literal['xlrd', 'openpyxl', 'odf', 'pyxlsb'] | None = ..., converters: dict[str, Callable] | dict[int, Callable] | None = ..., true_values: Iterable[Hashable] | None = ..., false_values: Iterable[Hashable] | None = ..., skiprows: Sequence[int] | int | Callable[[int], object] | None = ..., nrows: int | None = ..., na_values=..., keep_default_na: bool = ..., na_filter: bool = ..., verbose: bool = ..., parse_dates: list | dict | bool = ..., date_parser: Callable | lib.NoDefault = ..., date_format: dict[Hashable, str] | str | None = ..., thousands: str | None = ..., decimal: str = ..., comment: str | None = ..., skipfooter: int = ..., storage_options: StorageOptions = ..., dtype_backend: DtypeBackend | lib.NoDefault = ...) -> DataFrame: ...
@overload
def read_excel(io, sheet_name: list[IntStrT] | None, *, header: int | Sequence[int] | None = ..., names: list[str] | None = ..., index_col: int | Sequence[int] | None = ..., usecols: int | str | Sequence[int] | Sequence[str] | Callable[[str], bool] | None = ..., dtype: DtypeArg | None = ..., engine: Literal['xlrd', 'openpyxl', 'odf', 'pyxlsb'] | None = ..., converters: dict[str, Callable] | dict[int, Callable] | None = ..., true_values: Iterable[Hashable] | None = ..., false_values: Iterable[Hashable] | None = ..., skiprows: Sequence[int] | int | Callable[[int], object] | None = ..., nrows: int | None = ..., na_values=..., keep_default_na: bool = ..., na_filter: bool = ..., verbose: bool = ..., parse_dates: list | dict | bool = ..., date_parser: Callable | lib.NoDefault = ..., date_format: dict[Hashable, str] | str | None = ..., thousands: str | None = ..., decimal: str = ..., comment: str | None = ..., skipfooter: int = ..., storage_options: StorageOptions = ..., dtype_backend: DtypeBackend | lib.NoDefault = ...) -> dict[IntStrT, DataFrame]: ...

class BaseExcelReader(metaclass=abc.ABCMeta):
    handles: Incomplete
    book: Incomplete
    def __init__(self, filepath_or_buffer, storage_options: StorageOptions = None) -> None: ...
    @abc.abstractmethod
    def load_workbook(self, filepath_or_buffer): ...
    def close(self) -> None: ...
    @property
    @abc.abstractmethod
    def sheet_names(self) -> list[str]: ...
    @abc.abstractmethod
    def get_sheet_by_name(self, name: str): ...
    @abc.abstractmethod
    def get_sheet_by_index(self, index: int): ...
    @abc.abstractmethod
    def get_sheet_data(self, sheet, rows: int | None = None): ...
    def raise_if_bad_sheet_by_index(self, index: int) -> None: ...
    def raise_if_bad_sheet_by_name(self, name: str) -> None: ...
    def parse(self, sheet_name: str | int | list[int] | list[str] | None = 0, header: int | Sequence[int] | None = 0, names: Incomplete | None = None, index_col: int | Sequence[int] | None = None, usecols: Incomplete | None = None, dtype: DtypeArg | None = None, true_values: Iterable[Hashable] | None = None, false_values: Iterable[Hashable] | None = None, skiprows: Sequence[int] | int | Callable[[int], object] | None = None, nrows: int | None = None, na_values: Incomplete | None = None, verbose: bool = False, parse_dates: list | dict | bool = False, date_parser: Callable | lib.NoDefault = ..., date_format: dict[Hashable, str] | str | None = None, thousands: str | None = None, decimal: str = '.', comment: str | None = None, skipfooter: int = 0, dtype_backend: DtypeBackend | lib.NoDefault = ..., **kwds): ...

class ExcelWriter(metaclass=abc.ABCMeta):
    '''
    Class for writing DataFrame objects into excel sheets.

    Default is to use:

    * `xlsxwriter <https://pypi.org/project/XlsxWriter/>`__ for xlsx files if xlsxwriter
      is installed otherwise `openpyxl <https://pypi.org/project/openpyxl/>`__
    * `odswriter <https://pypi.org/project/odswriter/>`__ for ods files

    See ``DataFrame.to_excel`` for typical usage.

    The writer should be used as a context manager. Otherwise, call `close()` to save
    and close any opened file handles.

    Parameters
    ----------
    path : str or typing.BinaryIO
        Path to xls or xlsx or ods file.
    engine : str (optional)
        Engine to use for writing. If None, defaults to
        ``io.excel.<extension>.writer``.  NOTE: can only be passed as a keyword
        argument.
    date_format : str, default None
        Format string for dates written into Excel files (e.g. \'YYYY-MM-DD\').
    datetime_format : str, default None
        Format string for datetime objects written into Excel files.
        (e.g. \'YYYY-MM-DD HH:MM:SS\').
    mode : {{\'w\', \'a\'}}, default \'w\'
        File mode to use (write or append). Append does not work with fsspec URLs.
    {storage_options}

        .. versionadded:: 1.2.0

    if_sheet_exists : {{\'error\', \'new\', \'replace\', \'overlay\'}}, default \'error\'
        How to behave when trying to write to a sheet that already
        exists (append mode only).

        * error: raise a ValueError.
        * new: Create a new sheet, with a name determined by the engine.
        * replace: Delete the contents of the sheet before writing to it.
        * overlay: Write contents to the existing sheet without removing the old
          contents.

        .. versionadded:: 1.3.0

        .. versionchanged:: 1.4.0

           Added ``overlay`` option

    engine_kwargs : dict, optional
        Keyword arguments to be passed into the engine. These will be passed to
        the following functions of the respective engines:

        * xlsxwriter: ``xlsxwriter.Workbook(file, **engine_kwargs)``
        * openpyxl (write mode): ``openpyxl.Workbook(**engine_kwargs)``
        * openpyxl (append mode): ``openpyxl.load_workbook(file, **engine_kwargs)``
        * odswriter: ``odf.opendocument.OpenDocumentSpreadsheet(**engine_kwargs)``

        .. versionadded:: 1.3.0

    Notes
    -----
    For compatibility with CSV writers, ExcelWriter serializes lists
    and dicts to strings before writing.

    Examples
    --------
    Default usage:

    >>> df = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])  # doctest: +SKIP
    >>> with pd.ExcelWriter("path_to_file.xlsx") as writer:
    ...     df.to_excel(writer)  # doctest: +SKIP

    To write to separate sheets in a single file:

    >>> df1 = pd.DataFrame([["AAA", "BBB"]], columns=["Spam", "Egg"])  # doctest: +SKIP
    >>> df2 = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])  # doctest: +SKIP
    >>> with pd.ExcelWriter("path_to_file.xlsx") as writer:
    ...     df1.to_excel(writer, sheet_name="Sheet1")  # doctest: +SKIP
    ...     df2.to_excel(writer, sheet_name="Sheet2")  # doctest: +SKIP

    You can set the date format or datetime format:

    >>> from datetime import date, datetime  # doctest: +SKIP
    >>> df = pd.DataFrame(
    ...     [
    ...         [date(2014, 1, 31), date(1999, 9, 24)],
    ...         [datetime(1998, 5, 26, 23, 33, 4), datetime(2014, 2, 28, 13, 5, 13)],
    ...     ],
    ...     index=["Date", "Datetime"],
    ...     columns=["X", "Y"],
    ... )  # doctest: +SKIP
    >>> with pd.ExcelWriter(
    ...     "path_to_file.xlsx",
    ...     date_format="YYYY-MM-DD",
    ...     datetime_format="YYYY-MM-DD HH:MM:SS"
    ... ) as writer:
    ...     df.to_excel(writer)  # doctest: +SKIP

    You can also append to an existing Excel file:

    >>> with pd.ExcelWriter("path_to_file.xlsx", mode="a", engine="openpyxl") as writer:
    ...     df.to_excel(writer, sheet_name="Sheet3")  # doctest: +SKIP

    Here, the `if_sheet_exists` parameter can be set to replace a sheet if it
    already exists:

    >>> with ExcelWriter(
    ...     "path_to_file.xlsx",
    ...     mode="a",
    ...     engine="openpyxl",
    ...     if_sheet_exists="replace",
    ... ) as writer:
    ...     df.to_excel(writer, sheet_name="Sheet1")  # doctest: +SKIP

    You can also write multiple DataFrames to a single sheet. Note that the
    ``if_sheet_exists`` parameter needs to be set to ``overlay``:

    >>> with ExcelWriter("path_to_file.xlsx",
    ...     mode="a",
    ...     engine="openpyxl",
    ...     if_sheet_exists="overlay",
    ... ) as writer:
    ...     df1.to_excel(writer, sheet_name="Sheet1")
    ...     df2.to_excel(writer, sheet_name="Sheet1", startcol=3)  # doctest: +SKIP

    You can store Excel file in RAM:

    >>> import io
    >>> df = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])
    >>> buffer = io.BytesIO()
    >>> with pd.ExcelWriter(buffer) as writer:
    ...     df.to_excel(writer)

    You can pack Excel file into zip archive:

    >>> import zipfile  # doctest: +SKIP
    >>> df = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])  # doctest: +SKIP
    >>> with zipfile.ZipFile("path_to_file.zip", "w") as zf:
    ...     with zf.open("filename.xlsx", "w") as buffer:
    ...         with pd.ExcelWriter(buffer) as writer:
    ...             df.to_excel(writer)  # doctest: +SKIP

    You can specify additional arguments to the underlying engine:

    >>> with pd.ExcelWriter(
    ...     "path_to_file.xlsx",
    ...     engine="xlsxwriter",
    ...     engine_kwargs={{"options": {{"nan_inf_to_errors": True}}}}
    ... ) as writer:
    ...     df.to_excel(writer)  # doctest: +SKIP

    In append mode, ``engine_kwargs`` are passed through to
    openpyxl\'s ``load_workbook``:

    >>> with pd.ExcelWriter(
    ...     "path_to_file.xlsx",
    ...     engine="openpyxl",
    ...     mode="a",
    ...     engine_kwargs={{"keep_vba": True}}
    ... ) as writer:
    ...     df.to_excel(writer, sheet_name="Sheet2")  # doctest: +SKIP
    '''
    def __new__(cls, path: FilePath | WriteExcelBuffer | ExcelWriter, engine: str | None = None, date_format: str | None = None, datetime_format: str | None = None, mode: str = 'w', storage_options: StorageOptions = None, if_sheet_exists: Literal['error', 'new', 'replace', 'overlay'] | None = None, engine_kwargs: dict | None = None) -> ExcelWriter: ...
    @property
    def supported_extensions(self) -> tuple[str, ...]:
        """Extensions that writer engine supports."""
    @property
    def engine(self) -> str:
        """Name of engine."""
    @property
    @abc.abstractmethod
    def sheets(self) -> dict[str, Any]:
        """Mapping of sheet names to sheet objects."""
    @property
    @abc.abstractmethod
    def book(self):
        """
        Book instance. Class type will depend on the engine used.

        This attribute can be used to access engine-specific features.
        """
    def __init__(self, path: FilePath | WriteExcelBuffer | ExcelWriter, engine: str | None = None, date_format: str | None = None, datetime_format: str | None = None, mode: str = 'w', storage_options: StorageOptions = None, if_sheet_exists: str | None = None, engine_kwargs: dict[str, Any] | None = None) -> None: ...
    @property
    def date_format(self) -> str:
        """
        Format string for dates written into Excel files (e.g. ‘YYYY-MM-DD’).
        """
    @property
    def datetime_format(self) -> str:
        """
        Format string for dates written into Excel files (e.g. ‘YYYY-MM-DD’).
        """
    @property
    def if_sheet_exists(self) -> str:
        """
        How to behave when writing to a sheet that already exists in append mode.
        """
    def __fspath__(self) -> str: ...
    @classmethod
    def check_extension(cls, ext: str) -> Literal[True]:
        """
        checks that path's extension against the Writer's supported
        extensions.  If it isn't supported, raises UnsupportedFiletypeError.
        """
    def __enter__(self) -> ExcelWriter: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...
    def close(self) -> None:
        """synonym for save, to make it more file-like"""

XLS_SIGNATURES: Incomplete
ZIP_SIGNATURE: bytes
PEEK_SIZE: Incomplete

def inspect_excel_format(content_or_path: FilePath | ReadBuffer[bytes], storage_options: StorageOptions = None) -> str | None:
    """
    Inspect the path or content of an excel file and get its format.

    Adopted from xlrd: https://github.com/python-excel/xlrd.

    Parameters
    ----------
    content_or_path : str or file-like object
        Path to file or content of file to inspect. May be a URL.
    {storage_options}

    Returns
    -------
    str or None
        Format of file if it can be determined.

    Raises
    ------
    ValueError
        If resulting stream is empty.
    BadZipFile
        If resulting stream does not have an XLS signature and is not a valid zipfile.
    """

class ExcelFile:
    """
    Class for parsing tabular Excel sheets into DataFrame objects.

    See read_excel for more documentation.

    Parameters
    ----------
    path_or_buffer : str, bytes, path object (pathlib.Path or py._path.local.LocalPath),
        A file-like object, xlrd workbook or openpyxl workbook.
        If a string or path object, expected to be a path to a
        .xls, .xlsx, .xlsb, .xlsm, .odf, .ods, or .odt file.
    engine : str, default None
        If io is not a buffer or path, this must be set to identify io.
        Supported engines: ``xlrd``, ``openpyxl``, ``odf``, ``pyxlsb``
        Engine compatibility :

        - ``xlrd`` supports old-style Excel files (.xls).
        - ``openpyxl`` supports newer Excel file formats.
        - ``odf`` supports OpenDocument file formats (.odf, .ods, .odt).
        - ``pyxlsb`` supports Binary Excel files.

        .. versionchanged:: 1.2.0

           The engine `xlrd <https://xlrd.readthedocs.io/en/latest/>`_
           now only supports old-style ``.xls`` files.
           When ``engine=None``, the following logic will be
           used to determine the engine:

           - If ``path_or_buffer`` is an OpenDocument format (.odf, .ods, .odt),
             then `odf <https://pypi.org/project/odfpy/>`_ will be used.
           - Otherwise if ``path_or_buffer`` is an xls format,
             ``xlrd`` will be used.
           - Otherwise if ``path_or_buffer`` is in xlsb format,
             `pyxlsb <https://pypi.org/project/pyxlsb/>`_ will be used.

           .. versionadded:: 1.3.0

           - Otherwise if `openpyxl <https://pypi.org/project/openpyxl/>`_ is installed,
             then ``openpyxl`` will be used.
           - Otherwise if ``xlrd >= 2.0`` is installed, a ``ValueError`` will be raised.

           .. warning::

            Please do not report issues when using ``xlrd`` to read ``.xlsx`` files.
            This is not supported, switch to using ``openpyxl`` instead.
    """
    io: Incomplete
    engine: Incomplete
    storage_options: Incomplete
    def __init__(self, path_or_buffer, engine: str | None = None, storage_options: StorageOptions = None) -> None: ...
    def __fspath__(self): ...
    def parse(self, sheet_name: str | int | list[int] | list[str] | None = 0, header: int | Sequence[int] | None = 0, names: Incomplete | None = None, index_col: int | Sequence[int] | None = None, usecols: Incomplete | None = None, converters: Incomplete | None = None, true_values: Iterable[Hashable] | None = None, false_values: Iterable[Hashable] | None = None, skiprows: Sequence[int] | int | Callable[[int], object] | None = None, nrows: int | None = None, na_values: Incomplete | None = None, parse_dates: list | dict | bool = False, date_parser: Callable | lib.NoDefault = ..., date_format: str | dict[Hashable, str] | None = None, thousands: str | None = None, comment: str | None = None, skipfooter: int = 0, dtype_backend: DtypeBackend | lib.NoDefault = ..., **kwds) -> DataFrame | dict[str, DataFrame] | dict[int, DataFrame]:
        """
        Parse specified sheet(s) into a DataFrame.

        Equivalent to read_excel(ExcelFile, ...)  See the read_excel
        docstring for more info on accepted parameters.

        Returns
        -------
        DataFrame or dict of DataFrames
            DataFrame from the passed in Excel file.
        """
    @property
    def book(self): ...
    @property
    def sheet_names(self): ...
    def close(self) -> None:
        """close io if necessary"""
    def __enter__(self) -> ExcelFile: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...
