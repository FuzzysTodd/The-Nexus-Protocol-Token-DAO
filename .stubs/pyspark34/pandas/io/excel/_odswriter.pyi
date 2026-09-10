from _typeshed import Incomplete
from pandas._libs import json as json
from pandas._typing import FilePath as FilePath, StorageOptions as StorageOptions, WriteExcelBuffer as WriteExcelBuffer
from pandas.io.excel._base import ExcelWriter as ExcelWriter
from pandas.io.excel._util import combine_kwargs as combine_kwargs, validate_freeze_panes as validate_freeze_panes
from pandas.io.formats.excel import ExcelCell as ExcelCell
from typing import Any

class ODSWriter(ExcelWriter):
    def __init__(self, path: FilePath | WriteExcelBuffer | ExcelWriter, engine: str | None = None, date_format: str | None = None, datetime_format: Incomplete | None = None, mode: str = 'w', storage_options: StorageOptions = None, if_sheet_exists: str | None = None, engine_kwargs: dict[str, Any] | None = None, **kwargs) -> None: ...
    @property
    def book(self):
        """
        Book instance of class odf.opendocument.OpenDocumentSpreadsheet.

        This attribute can be used to access engine-specific features.
        """
    @property
    def sheets(self) -> dict[str, Any]:
        """Mapping of sheet names to sheet objects."""
