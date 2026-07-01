from _typeshed import Incomplete
from openpyxl.cell.rich_text import CellRichText as CellRichText
from openpyxl.compat import NUMERIC_TYPES as NUMERIC_TYPES
from openpyxl.styles import is_date_format as is_date_format, numbers as numbers
from openpyxl.styles.styleable import StyleableObject as StyleableObject
from openpyxl.utils import get_column_letter as get_column_letter
from openpyxl.utils.exceptions import IllegalCharacterError as IllegalCharacterError
from openpyxl.worksheet.formula import ArrayFormula as ArrayFormula, DataTableFormula as DataTableFormula
from openpyxl.worksheet.hyperlink import Hyperlink as Hyperlink

__docformat__: str
TIME_TYPES: Incomplete
TIME_FORMATS: Incomplete
STRING_TYPES: Incomplete
KNOWN_TYPES: Incomplete
ILLEGAL_CHARACTERS_RE: Incomplete
ERROR_CODES: Incomplete
TYPE_STRING: str
TYPE_FORMULA: str
TYPE_NUMERIC: str
TYPE_BOOL: str
TYPE_NULL: str
TYPE_INLINE: str
TYPE_ERROR: str
TYPE_FORMULA_CACHE_STRING: str
VALID_TYPES: Incomplete

def get_type(t, value): ...
def get_time_format(t): ...

class Cell(StyleableObject):
    """Describes cell associated properties.

    Properties of interest include style, type, value, and address.

    """
    row: Incomplete
    column: Incomplete
    data_type: str
    def __init__(self, worksheet, row: Incomplete | None = None, column: Incomplete | None = None, value: Incomplete | None = None, style_array: Incomplete | None = None) -> None: ...
    @property
    def coordinate(self):
        """This cell's coordinate (ex. 'A5')"""
    @property
    def col_idx(self):
        """The numerical index of the column"""
    @property
    def column_letter(self): ...
    @property
    def encoding(self): ...
    @property
    def base_date(self): ...
    def check_string(self, value):
        """Check string coding, length, and line break character"""
    def check_error(self, value):
        '''Tries to convert Error" else N/A'''
    @property
    def value(self):
        """Get or set the value held in the cell.

        :type: depends on the value (string, float, int or
            :class:`datetime.datetime`)
        """
    @value.setter
    def value(self, value) -> None:
        """Set the value and infer type and display options."""
    @property
    def internal_value(self):
        """Always returns the value for excel."""
    @property
    def hyperlink(self):
        """Return the hyperlink target or an empty string"""
    @hyperlink.setter
    def hyperlink(self, val) -> None:
        """Set value and display for hyperlinks in a cell.
        Automatically sets the `value` of the cell with link text,
        but you can modify it afterwards by setting the `value`
        property, and the hyperlink will remain.
        Hyperlink is removed if set to ``None``."""
    @property
    def is_date(self):
        """True if the value is formatted as a date

        :type: bool
        """
    def offset(self, row: int = 0, column: int = 0):
        """Returns a cell location relative to this cell.

        :param row: number of rows to offset
        :type row: int

        :param column: number of columns to offset
        :type column: int

        :rtype: :class:`openpyxl.cell.Cell`
        """
    @property
    def comment(self):
        """ Returns the comment associated with this cell

            :type: :class:`openpyxl.comments.Comment`
        """
    @comment.setter
    def comment(self, value) -> None:
        """
        Assign a comment to a cell
        """

class MergedCell(StyleableObject):
    """
    Describes the properties of a cell in a merged cell and helps to
    display the borders of the merged cell.

    The value of a MergedCell is always None.
    """
    data_type: str
    comment: Incomplete
    hyperlink: Incomplete
    row: Incomplete
    column: Incomplete
    def __init__(self, worksheet, row: Incomplete | None = None, column: Incomplete | None = None) -> None: ...
    coordinate: Incomplete
    value: Incomplete

def WriteOnlyCell(ws: Incomplete | None = None, value: Incomplete | None = None): ...
