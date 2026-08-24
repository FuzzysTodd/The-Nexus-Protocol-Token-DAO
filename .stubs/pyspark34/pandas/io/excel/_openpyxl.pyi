from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.workbook import Workbook
from pandas._typing import FilePath as FilePath, ReadBuffer as ReadBuffer, Scalar as Scalar, StorageOptions as StorageOptions, WriteExcelBuffer as WriteExcelBuffer
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.io.excel._base import BaseExcelReader as BaseExcelReader, ExcelWriter as ExcelWriter
from pandas.io.excel._util import combine_kwargs as combine_kwargs, validate_freeze_panes as validate_freeze_panes
from pandas.util._decorators import doc as doc
from typing import Any

class OpenpyxlWriter(ExcelWriter):
    def __init__(self, path: FilePath | WriteExcelBuffer | ExcelWriter, engine: str | None = None, date_format: str | None = None, datetime_format: str | None = None, mode: str = 'w', storage_options: StorageOptions = None, if_sheet_exists: str | None = None, engine_kwargs: dict[str, Any] | None = None, **kwargs) -> None: ...
    @property
    def book(self) -> Workbook:
        """
        Book instance of class openpyxl.workbook.Workbook.

        This attribute can be used to access engine-specific features.
        """
    @property
    def sheets(self) -> dict[str, Any]:
        """Mapping of sheet names to sheet objects."""

class OpenpyxlReader(BaseExcelReader):
    def __init__(self, filepath_or_buffer: FilePath | ReadBuffer[bytes], storage_options: StorageOptions = None) -> None:
        """
        Reader using openpyxl engine.

        Parameters
        ----------
        filepath_or_buffer : str, path object or Workbook
            Object to be parsed.
        {storage_options}
        """
    def load_workbook(self, filepath_or_buffer: FilePath | ReadBuffer[bytes]): ...
    @property
    def sheet_names(self) -> list[str]: ...
    def get_sheet_by_name(self, name: str): ...
    def get_sheet_by_index(self, index: int): ...
    def get_sheet_data(self, sheet, file_rows_needed: int | None = None) -> list[list[Scalar]]: ...
