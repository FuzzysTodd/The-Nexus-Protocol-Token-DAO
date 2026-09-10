from pandas._libs.tslibs.nattype import NaTType as NaTType
from pandas._typing import FilePath as FilePath, ReadBuffer as ReadBuffer, Scalar as Scalar, StorageOptions as StorageOptions
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.io.excel._base import BaseExcelReader as BaseExcelReader
from pandas.util._decorators import doc as doc

class ODFReader(BaseExcelReader):
    def __init__(self, filepath_or_buffer: FilePath | ReadBuffer[bytes], storage_options: StorageOptions = None) -> None:
        """
        Read tables out of OpenDocument formatted files.

        Parameters
        ----------
        filepath_or_buffer : str, path to be parsed or
            an open readable stream.
        {storage_options}
        """
    def load_workbook(self, filepath_or_buffer: FilePath | ReadBuffer[bytes]): ...
    @property
    def empty_value(self) -> str:
        """Property for compat with other readers."""
    @property
    def sheet_names(self) -> list[str]:
        """Return a list of sheet names present in the document"""
    def get_sheet_by_index(self, index: int): ...
    def get_sheet_by_name(self, name: str): ...
    def get_sheet_data(self, sheet, file_rows_needed: int | None = None) -> list[list[Scalar | NaTType]]:
        """
        Parse an ODF Table into a list of lists
        """
