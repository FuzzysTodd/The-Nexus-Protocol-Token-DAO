from pandas._typing import FilePath as FilePath, ReadBuffer as ReadBuffer, Scalar as Scalar, StorageOptions as StorageOptions
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.io.excel._base import BaseExcelReader as BaseExcelReader
from pandas.util._decorators import doc as doc

class PyxlsbReader(BaseExcelReader):
    def __init__(self, filepath_or_buffer: FilePath | ReadBuffer[bytes], storage_options: StorageOptions = None) -> None:
        """
        Reader using pyxlsb engine.

        Parameters
        ----------
        filepath_or_buffer : str, path object, or Workbook
            Object to be parsed.
        {storage_options}
        """
    def load_workbook(self, filepath_or_buffer: FilePath | ReadBuffer[bytes]): ...
    @property
    def sheet_names(self) -> list[str]: ...
    def get_sheet_by_name(self, name: str): ...
    def get_sheet_by_index(self, index: int): ...
    def get_sheet_data(self, sheet, file_rows_needed: int | None = None) -> list[list[Scalar]]: ...
