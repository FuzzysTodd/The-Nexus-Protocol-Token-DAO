from .cell_range import CellRange as CellRange
from _typeshed import Incomplete
from openpyxl.cell.cell import MergedCell as MergedCell
from openpyxl.descriptors import Integer as Integer, Sequence as Sequence
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.styles.borders import Border as Border

class MergeCell(CellRange):
    tagname: str
    ref: Incomplete
    __attrs__: Incomplete
    def __init__(self, ref: Incomplete | None = None) -> None: ...
    def __copy__(self): ...

class MergeCells(Serialisable):
    tagname: str
    count: Incomplete
    mergeCell: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, count: Incomplete | None = None, mergeCell=()) -> None: ...
    @property
    def count(self): ...

class MergedCellRange(CellRange):
    """
    MergedCellRange stores the border information of a merged cell in the top
    left cell of the merged cell.
    The remaining cells in the merged cell are stored as MergedCell objects and
    get their border information from the upper left cell.
    """
    ws: Incomplete
    start_cell: Incomplete
    def __init__(self, worksheet, coord) -> None: ...
    def format(self) -> None:
        """
        Each cell of the merged cell is created as MergedCell if it does not
        already exist.

        The MergedCells at the edge of the merged cell gets its borders from
        the upper left cell.

         - The top MergedCells get the top border from the top left cell.
         - The bottom MergedCells get the bottom border from the top left cell.
         - The left MergedCells get the left border from the top left cell.
         - The right MergedCells get the right border from the top left cell.
        """
    def __contains__(self, coord) -> bool: ...
    def __copy__(self): ...
