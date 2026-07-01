from .rule import Rule as Rule
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Bool as Bool, Convertible as Convertible, Sequence as Sequence
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.worksheet.cell_range import MultiCellRange as MultiCellRange

class ConditionalFormatting(Serialisable):
    tagname: str
    sqref: Incomplete
    cells: Incomplete
    pivot: Incomplete
    cfRule: Incomplete
    rules: Incomplete
    def __init__(self, sqref=(), pivot: Incomplete | None = None, cfRule=(), extLst: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def __contains__(self, coord) -> bool:
        """
        Check whether a certain cell is affected by the formatting
        """

class ConditionalFormattingList:
    """Conditional formatting rules."""
    max_priority: int
    def __init__(self) -> None: ...
    def add(self, range_string, cfRule) -> None:
        """Add a rule such as ColorScaleRule, FormulaRule or CellIsRule

         The priority will be added automatically.
        """
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __getitem__(self, key):
        """
        Get the rules for a cell range
        """
    def __delitem__(self, key) -> None: ...
    def __setitem__(self, key, rule) -> None:
        """
        Add a rule for a cell range
        """
