from .cell_range import MultiCellRange as MultiCellRange
from _typeshed import Incomplete
from openpyxl.descriptors import Integer as Integer, Strict as Strict, String as String, Typed as Typed
from openpyxl.utils import absolute_coordinate as absolute_coordinate, quote_sheetname as quote_sheetname
from openpyxl.utils.cell import RANGE_EXPR as RANGE_EXPR, SHEETRANGE_RE as SHEETRANGE_RE, SHEET_TITLE as SHEET_TITLE

COL_RANGE: str
COL_RANGE_RE: Incomplete
ROW_RANGE: str
ROW_RANGE_RE: Incomplete
TITLES_REGEX: Incomplete
PRINT_AREA_RE: Incomplete

class ColRange(Strict):
    """
    Represent a range of at least one column
    """
    min_col: Incomplete
    max_col: Incomplete
    def __init__(self, range_string: Incomplete | None = None, min_col: Incomplete | None = None, max_col: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...

class RowRange(Strict):
    """
    Represent a range of at least one row
    """
    min_row: Incomplete
    max_row: Incomplete
    def __init__(self, range_string: Incomplete | None = None, min_row: Incomplete | None = None, max_row: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...

class PrintTitles(Strict):
    """
    Contains at least either a range of rows or columns
    """
    cols: Incomplete
    rows: Incomplete
    title: Incomplete
    def __init__(self, cols: Incomplete | None = None, rows: Incomplete | None = None, title: str = '') -> None: ...
    @classmethod
    def from_string(cls, value): ...
    def __eq__(self, other): ...

class PrintArea(MultiCellRange):
    @classmethod
    def from_string(cls, value): ...
    title: str
    def __init__(self, ranges=(), title: str = '') -> None: ...
    def __eq__(self, other): ...
