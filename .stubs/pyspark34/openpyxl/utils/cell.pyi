from .exceptions import CellCoordinatesException as CellCoordinatesException
from _typeshed import Incomplete
from collections.abc import Generator

COORD_RE: Incomplete
COL_RANGE: str
ROW_RANGE: str
RANGE_EXPR: str
ABSOLUTE_RE: Incomplete
SHEET_TITLE: str
SHEETRANGE_RE: Incomplete

def get_column_interval(start, end):
    """
    Given the start and end columns, return all the columns in the series.

    The start and end columns can be either column letters or 1-based
    indexes.
    """
def coordinate_from_string(coord_string):
    """Convert a coordinate string like 'B12' to a tuple ('B', 12)"""
def absolute_coordinate(coord_string):
    """Convert a coordinate to an absolute coordinate string (B12 -> $B$12)"""

col: Incomplete

def get_column_letter(idx):
    """Convert a column index into a column letter
    (3 -> 'C')
    """
def column_index_from_string(str_col):
    """Convert a column name into a numerical index
    ('A' -> 1)
    """
def range_boundaries(range_string):
    """
    Convert a range string into a tuple of boundaries:
    (min_col, min_row, max_col, max_row)
    Cell coordinates will be converted into a range with the cell at both end
    """
def rows_from_range(range_string) -> Generator[Incomplete, None, None]:
    """
    Get individual addresses for every cell in a range.
    Yields one row at a time.
    """
def cols_from_range(range_string) -> Generator[Incomplete, None, None]:
    """
    Get individual addresses for every cell in a range.
    Yields one row at a time.
    """
def coordinate_to_tuple(coordinate):
    """
    Convert an Excel style coordinate to (row, column) tuple
    """
def range_to_tuple(range_string):
    """
    Convert a worksheet range to the sheetname and maximum and minimum
    coordinate indices
    """
def quote_sheetname(sheetname):
    """
    Add quotes around sheetnames if they contain spaces.
    """
