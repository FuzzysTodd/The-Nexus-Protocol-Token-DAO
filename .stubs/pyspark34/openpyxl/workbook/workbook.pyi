from .defined_name import DefinedName as DefinedName, DefinedNameDict as DefinedNameDict
from .properties import CalcProperties as CalcProperties
from .protection import DocumentSecurity as DocumentSecurity
from .views import BookView as BookView
from _typeshed import Incomplete
from openpyxl.chartsheet import Chartsheet as Chartsheet
from openpyxl.compat import deprecated as deprecated
from openpyxl.packaging.core import DocumentProperties as DocumentProperties
from openpyxl.packaging.custom import CustomPropertyList as CustomPropertyList
from openpyxl.packaging.relationship import RelationshipList as RelationshipList
from openpyxl.styles.alignment import Alignment as Alignment
from openpyxl.styles.borders import DEFAULT_BORDER as DEFAULT_BORDER
from openpyxl.styles.cell_style import StyleArray as StyleArray
from openpyxl.styles.colors import COLOR_INDEX as COLOR_INDEX
from openpyxl.styles.differential import DifferentialStyleList as DifferentialStyleList
from openpyxl.styles.fills import DEFAULT_EMPTY_FILL as DEFAULT_EMPTY_FILL, DEFAULT_GRAY_FILL as DEFAULT_GRAY_FILL
from openpyxl.styles.fonts import DEFAULT_FONT as DEFAULT_FONT
from openpyxl.styles.named_styles import NamedStyle as NamedStyle, NamedStyleList as NamedStyleList
from openpyxl.styles.protection import Protection as Protection
from openpyxl.styles.table import TableStyleList as TableStyleList
from openpyxl.utils import quote_sheetname as quote_sheetname
from openpyxl.utils.datetime import MAC_EPOCH as MAC_EPOCH, WINDOWS_EPOCH as WINDOWS_EPOCH
from openpyxl.utils.exceptions import ReadOnlyWorkbookException as ReadOnlyWorkbookException
from openpyxl.utils.indexed_list import IndexedList as IndexedList
from openpyxl.worksheet._read_only import ReadOnlyWorksheet as ReadOnlyWorksheet
from openpyxl.worksheet._write_only import WriteOnlyWorksheet as WriteOnlyWorksheet
from openpyxl.worksheet.copier import WorksheetCopy as WorksheetCopy
from openpyxl.worksheet.worksheet import Worksheet as Worksheet
from openpyxl.writer.excel import save_workbook as save_workbook
from openpyxl.xml.constants import XLSM as XLSM, XLSX as XLSX, XLTM as XLTM, XLTX as XLTX

INTEGER_TYPES: Incomplete

class Workbook:
    """Workbook is the container for all other parts of the document."""
    template: bool
    path: str
    defined_names: Incomplete
    properties: Incomplete
    custom_doc_props: Incomplete
    security: Incomplete
    shared_strings: Incomplete
    loaded_theme: Incomplete
    vba_archive: Incomplete
    is_template: bool
    code_name: Incomplete
    encoding: str
    iso_dates: Incomplete
    rels: Incomplete
    calculation: Incomplete
    views: Incomplete
    def __init__(self, write_only: bool = False, iso_dates: bool = False) -> None: ...
    @property
    def epoch(self): ...
    @epoch.setter
    def epoch(self, value) -> None: ...
    @property
    def read_only(self): ...
    @property
    def data_only(self): ...
    @property
    def write_only(self): ...
    @property
    def excel_base_date(self): ...
    @property
    def active(self):
        """Get the currently active sheet or None

        :type: :class:`openpyxl.worksheet.worksheet.Worksheet`
        """
    @active.setter
    def active(self, value) -> None:
        """Set the active sheet"""
    def create_sheet(self, title: Incomplete | None = None, index: Incomplete | None = None):
        """Create a worksheet (at an optional index).

        :param title: optional title of the sheet
        :type title: str
        :param index: optional position at which the sheet will be inserted
        :type index: int

        """
    def move_sheet(self, sheet, offset: int = 0) -> None:
        """
        Move a sheet or sheetname
        """
    def remove(self, worksheet) -> None:
        """Remove `worksheet` from this workbook."""
    def remove_sheet(self, worksheet) -> None:
        """Remove `worksheet` from this workbook."""
    def create_chartsheet(self, title: Incomplete | None = None, index: Incomplete | None = None): ...
    def get_sheet_by_name(self, name):
        """Returns a worksheet by its name.

        :param name: the name of the worksheet to look for
        :type name: string

        """
    def __contains__(self, key) -> bool: ...
    def index(self, worksheet):
        """Return the index of a worksheet."""
    def get_index(self, worksheet):
        """Return the index of the worksheet."""
    def __getitem__(self, key):
        """Returns a worksheet by its name.

        :param name: the name of the worksheet to look for
        :type name: string

        """
    def __delitem__(self, key) -> None: ...
    def __iter__(self): ...
    def get_sheet_names(self): ...
    @property
    def worksheets(self):
        """A list of sheets in this workbook

        :type: list of :class:`openpyxl.worksheet.worksheet.Worksheet`
        """
    @property
    def chartsheets(self):
        """A list of Chartsheets in this workbook

        :type: list of :class:`openpyxl.chartsheet.chartsheet.Chartsheet`
        """
    @property
    def sheetnames(self):
        """Returns the list of the names of worksheets in this workbook.

        Names are returned in the worksheets order.

        :type: list of strings

        """
    def create_named_range(self, name, worksheet: Incomplete | None = None, value: Incomplete | None = None, scope: Incomplete | None = None) -> None:
        """Create a new named_range on a worksheet

        """
    def add_named_style(self, style) -> None:
        """
        Add a named style
        """
    @property
    def named_styles(self):
        """
        List available named styles
        """
    @property
    def mime_type(self):
        """
        The mime type is determined by whether a workbook is a template or
        not and whether it contains macros or not. Excel requires the file
        extension to match but openpyxl does not enforce this.

        """
    def save(self, filename) -> None:
        """Save the current workbook under the given `filename`.
        Use this function instead of using an `ExcelWriter`.

        .. warning::
            When creating your workbook using `write_only` set to True,
            you will only be able to call this function once. Subsequent attempts to
            modify or save the file will raise an :class:`openpyxl.shared.exc.WorkbookAlreadySaved` exception.
        """
    @property
    def style_names(self):
        """
        List of named styles
        """
    def copy_worksheet(self, from_worksheet):
        """Copy an existing worksheet in the current workbook

        .. warning::
            This function cannot copy worksheets between workbooks.
            worksheets can only be copied within the workbook that they belong

        :param from_worksheet: the worksheet to be copied from
        :return: copy of the initial worksheet
        """
    def close(self) -> None:
        """
        Close workbook file if open. Only affects read-only and write-only modes.
        """
