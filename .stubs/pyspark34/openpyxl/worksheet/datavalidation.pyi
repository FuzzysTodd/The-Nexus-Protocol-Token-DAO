from .cell_range import MultiCellRange as MultiCellRange
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Bool as Bool, Convertible as Convertible, Integer as Integer, NoneSet as NoneSet, Sequence as Sequence, String as String
from openpyxl.descriptors.nested import NestedText as NestedText
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.utils import coordinate_to_tuple as coordinate_to_tuple, get_column_letter as get_column_letter, rows_from_range as rows_from_range

def collapse_cell_addresses(cells, input_ranges=()):
    """ Collapse a collection of cell co-ordinates down into an optimal
        range or collection of ranges.

        E.g. Cells A1, A2, A3, B1, B2 and B3 should have the data-validation
        object applied, attempt to collapse down to a single range, A1:B3.

        Currently only collapsing contiguous vertical ranges (i.e. above
        example results in A1:A3 B1:B3).
    """
def expand_cell_ranges(range_string):
    '''
    Expand cell ranges to a sequence of addresses.
    Reverse of collapse_cell_addresses
    Eg. converts "A1:A2 B1:B2" to (A1, A2, B1, B2)
    '''

class DataValidation(Serialisable):
    tagname: str
    sqref: Incomplete
    cells: Incomplete
    ranges: Incomplete
    showDropDown: Incomplete
    hide_drop_down: Incomplete
    showInputMessage: Incomplete
    showErrorMessage: Incomplete
    allowBlank: Incomplete
    allow_blank: Incomplete
    errorTitle: Incomplete
    error: Incomplete
    promptTitle: Incomplete
    prompt: Incomplete
    formula1: Incomplete
    formula2: Incomplete
    type: Incomplete
    errorStyle: Incomplete
    imeMode: Incomplete
    operator: Incomplete
    validation_type: Incomplete
    def __init__(self, type: Incomplete | None = None, formula1: Incomplete | None = None, formula2: Incomplete | None = None, showErrorMessage: bool = False, showInputMessage: bool = False, showDropDown: bool = False, allowBlank: bool = False, sqref=(), promptTitle: Incomplete | None = None, errorStyle: Incomplete | None = None, error: Incomplete | None = None, prompt: Incomplete | None = None, errorTitle: Incomplete | None = None, imeMode: Incomplete | None = None, operator: Incomplete | None = None, allow_blank: bool = False) -> None: ...
    def add(self, cell) -> None:
        """Adds a cell or cell coordinate to this validator"""
    def __contains__(self, cell) -> bool: ...

class DataValidationList(Serialisable):
    tagname: str
    disablePrompts: Incomplete
    xWindow: Incomplete
    yWindow: Incomplete
    dataValidation: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(self, disablePrompts: Incomplete | None = None, xWindow: Incomplete | None = None, yWindow: Incomplete | None = None, count: Incomplete | None = None, dataValidation=()) -> None: ...
    @property
    def count(self): ...
    def __len__(self) -> int: ...
    def append(self, dv) -> None: ...
    def to_tree(self, tagname: Incomplete | None = None):
        """
        Need to skip validations that have no cell ranges
        """
