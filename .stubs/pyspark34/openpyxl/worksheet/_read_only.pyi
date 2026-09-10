from ._reader import WorkSheetParser as WorkSheetParser
from .worksheet import Worksheet as Worksheet
from _typeshed import Incomplete
from openpyxl.cell.read_only import EMPTY_CELL as EMPTY_CELL, ReadOnlyCell as ReadOnlyCell
from openpyxl.utils import get_column_letter as get_column_letter
from openpyxl.workbook.defined_name import DefinedNameDict as DefinedNameDict

def read_dimension(source): ...

class ReadOnlyWorksheet:
    cell: Incomplete
    iter_rows: Incomplete
    values: Incomplete
    rows: Incomplete
    __getitem__: Incomplete
    __iter__: Incomplete
    parent: Incomplete
    title: Incomplete
    sheet_state: str
    defined_names: Incomplete
    def __init__(self, parent_workbook, title, worksheet_path, shared_strings) -> None: ...
    def calculate_dimension(self, force: bool = False): ...
    def reset_dimensions(self) -> None:
        """
        Remove worksheet dimensions if these are incorrect in the worksheet source.
        NB. This probably indicates a bug in the library or application that created
        the workbook.
        """
    @property
    def min_row(self): ...
    @property
    def max_row(self): ...
    @property
    def min_column(self): ...
    @property
    def max_column(self): ...
