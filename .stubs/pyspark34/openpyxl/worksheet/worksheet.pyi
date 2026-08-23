from .cell_range import CellRange as CellRange, MultiCellRange as MultiCellRange
from .datavalidation import DataValidationList as DataValidationList
from .dimensions import ColumnDimension as ColumnDimension, DimensionHolder as DimensionHolder, RowDimension as RowDimension, SheetFormatProperties as SheetFormatProperties
from .filters import AutoFilter as AutoFilter
from .formula import ArrayFormula as ArrayFormula
from .merge import MergedCellRange as MergedCellRange
from .page import PageMargins as PageMargins, PrintOptions as PrintOptions, PrintPageSetup as PrintPageSetup
from .pagebreak import ColBreak as ColBreak, RowBreak as RowBreak
from .print_settings import ColRange as ColRange, PrintArea as PrintArea, PrintTitles as PrintTitles, RowRange as RowRange
from .properties import WorksheetProperties as WorksheetProperties
from .protection import SheetProtection as SheetProtection
from .scenario import ScenarioList as ScenarioList
from .table import TableList as TableList
from .views import Pane as Pane, Selection as Selection, SheetViewList as SheetViewList
from _typeshed import Incomplete
from collections.abc import Generator
from openpyxl.cell import Cell as Cell, MergedCell as MergedCell
from openpyxl.compat import deprecated as deprecated
from openpyxl.formatting.formatting import ConditionalFormattingList as ConditionalFormattingList
from openpyxl.formula.translate import Translator as Translator
from openpyxl.packaging.relationship import RelationshipList as RelationshipList
from openpyxl.utils import absolute_coordinate as absolute_coordinate, column_index_from_string as column_index_from_string, coordinate_to_tuple as coordinate_to_tuple, get_column_letter as get_column_letter, range_boundaries as range_boundaries
from openpyxl.workbook.child import _WorkbookChild
from openpyxl.workbook.defined_name import DefinedNameDict as DefinedNameDict

class Worksheet(_WorkbookChild):
    """Represents a worksheet.

    Do not create worksheets yourself,
    use :func:`openpyxl.workbook.Workbook.create_sheet` instead

    """
    mime_type: str
    BREAK_NONE: int
    BREAK_ROW: int
    BREAK_COLUMN: int
    SHEETSTATE_VISIBLE: str
    SHEETSTATE_HIDDEN: str
    SHEETSTATE_VERYHIDDEN: str
    PAPERSIZE_LETTER: str
    PAPERSIZE_LETTER_SMALL: str
    PAPERSIZE_TABLOID: str
    PAPERSIZE_LEDGER: str
    PAPERSIZE_LEGAL: str
    PAPERSIZE_STATEMENT: str
    PAPERSIZE_EXECUTIVE: str
    PAPERSIZE_A3: str
    PAPERSIZE_A4: str
    PAPERSIZE_A4_SMALL: str
    PAPERSIZE_A5: str
    ORIENTATION_PORTRAIT: str
    ORIENTATION_LANDSCAPE: str
    def __init__(self, parent, title: Incomplete | None = None) -> None: ...
    @property
    def sheet_view(self): ...
    @property
    def selected_cell(self): ...
    @property
    def active_cell(self): ...
    @property
    def array_formulae(self):
        """Returns a dictionary of cells with array formulae and the cells in array"""
    @property
    def show_gridlines(self): ...
    @property
    def freeze_panes(self): ...
    @freeze_panes.setter
    def freeze_panes(self, topLeftCell: Incomplete | None = None) -> None: ...
    def cell(self, row, column, value: Incomplete | None = None):
        """
        Returns a cell object based on the given coordinates.

        Usage: cell(row=15, column=1, value=5)

        Calling `cell` creates cells in memory when they
        are first accessed.

        :param row: row index of the cell (e.g. 4)
        :type row: int

        :param column: column index of the cell (e.g. 3)
        :type column: int

        :param value: value of the cell (e.g. 5)
        :type value: numeric or time or string or bool or none

        :rtype: openpyxl.cell.cell.Cell
        """
    def __getitem__(self, key):
        """Convenience access by Excel style coordinates

        The key can be a single cell coordinate 'A1', a range of cells 'A1:D25',
        individual rows or columns 'A', 4 or ranges of rows or columns 'A:D',
        4:10.

        Single cells will always be created if they do not exist.

        Returns either a single cell or a tuple of rows or columns.
        """
    def __setitem__(self, key, value) -> None: ...
    def __iter__(self): ...
    def __delitem__(self, key) -> None: ...
    @property
    def min_row(self):
        """The minimum row index containing data (1-based)

        :type: int
        """
    @property
    def max_row(self):
        """The maximum row index containing data (1-based)

        :type: int
        """
    @property
    def min_column(self):
        """The minimum column index containing data (1-based)

        :type: int
        """
    @property
    def max_column(self):
        """The maximum column index containing data (1-based)

        :type: int
        """
    def calculate_dimension(self):
        """Return the minimum bounding range for all cells containing data (ex. 'A1:M24')

        :rtype: string
        """
    @property
    def dimensions(self):
        """Returns the result of :func:`calculate_dimension`"""
    def iter_rows(self, min_row: Incomplete | None = None, max_row: Incomplete | None = None, min_col: Incomplete | None = None, max_col: Incomplete | None = None, values_only: bool = False):
        """
        Produces cells from the worksheet, by row. Specify the iteration range
        using indices of rows and columns.

        If no indices are specified the range starts at A1.

        If no cells are in the worksheet an empty tuple will be returned.

        :param min_col: smallest column index (1-based index)
        :type min_col: int

        :param min_row: smallest row index (1-based index)
        :type min_row: int

        :param max_col: largest column index (1-based index)
        :type max_col: int

        :param max_row: largest row index (1-based index)
        :type max_row: int

        :param values_only: whether only cell values should be returned
        :type values_only: bool

        :rtype: generator
        """
    @property
    def rows(self):
        """Produces all cells in the worksheet, by row (see :func:`iter_rows`)

        :type: generator
        """
    @property
    def values(self) -> Generator[Incomplete, None, None]:
        """Produces all cell values in the worksheet, by row

        :type: generator
        """
    def iter_cols(self, min_col: Incomplete | None = None, max_col: Incomplete | None = None, min_row: Incomplete | None = None, max_row: Incomplete | None = None, values_only: bool = False):
        """
        Produces cells from the worksheet, by column. Specify the iteration range
        using indices of rows and columns.

        If no indices are specified the range starts at A1.

        If no cells are in the worksheet an empty tuple will be returned.

        :param min_col: smallest column index (1-based index)
        :type min_col: int

        :param min_row: smallest row index (1-based index)
        :type min_row: int

        :param max_col: largest column index (1-based index)
        :type max_col: int

        :param max_row: largest row index (1-based index)
        :type max_row: int

        :param values_only: whether only cell values should be returned
        :type values_only: bool

        :rtype: generator
        """
    @property
    def columns(self):
        """Produces all cells in the worksheet, by column  (see :func:`iter_cols`)"""
    def set_printer_settings(self, paper_size, orientation) -> None:
        """Set printer settings """
    def add_data_validation(self, data_validation) -> None:
        """ Add a data-validation object to the sheet.  The data-validation
            object defines the type of data-validation to be applied and the
            cell or range of cells it should apply to.
        """
    def add_chart(self, chart, anchor: Incomplete | None = None) -> None:
        """
        Add a chart to the sheet
        Optionally provide a cell for the top-left anchor
        """
    def add_image(self, img, anchor: Incomplete | None = None) -> None:
        """
        Add an image to the sheet.
        Optionally provide a cell for the top-left anchor
        """
    def add_table(self, table) -> None:
        """
        Check for duplicate name in definedNames and other worksheet tables
        before adding table.
        """
    @property
    def tables(self): ...
    def add_pivot(self, pivot) -> None: ...
    def merge_cells(self, range_string: Incomplete | None = None, start_row: Incomplete | None = None, start_column: Incomplete | None = None, end_row: Incomplete | None = None, end_column: Incomplete | None = None) -> None:
        """ Set merge on a cell range.  Range is a cell range (e.g. A1:E1) """
    @property
    def merged_cell_ranges(self):
        """Return a copy of cell ranges"""
    def unmerge_cells(self, range_string: Incomplete | None = None, start_row: Incomplete | None = None, start_column: Incomplete | None = None, end_row: Incomplete | None = None, end_column: Incomplete | None = None) -> None:
        """ Remove merge on a cell range.  Range is a cell range (e.g. A1:E1) """
    def append(self, iterable) -> None:
        """Appends a group of values at the bottom of the current sheet.

        * If it's a list: all values are added in order, starting from the first column
        * If it's a dict: values are assigned to the columns indicated by the keys (numbers or letters)

        :param iterable: list, range or generator, or dict containing values to append
        :type iterable: list|tuple|range|generator or dict

        Usage:

        * append(['This is A1', 'This is B1', 'This is C1'])
        * **or** append({'A' : 'This is A1', 'C' : 'This is C1'})
        * **or** append({1 : 'This is A1', 3 : 'This is C1'})

        :raise: TypeError when iterable is neither a list/tuple nor a dict

        """
    def insert_rows(self, idx, amount: int = 1) -> None:
        """
        Insert row or rows before row==idx
        """
    def insert_cols(self, idx, amount: int = 1) -> None:
        """
        Insert column or columns before col==idx
        """
    def delete_rows(self, idx, amount: int = 1) -> None:
        """
        Delete row or rows from row==idx
        """
    def delete_cols(self, idx, amount: int = 1) -> None:
        """
        Delete column or columns from col==idx
        """
    def move_range(self, cell_range, rows: int = 0, cols: int = 0, translate: bool = False) -> None:
        """
        Move a cell range by the number of rows and/or columns:
        down if rows > 0 and up if rows < 0
        right if cols > 0 and left if cols < 0
        Existing cells will be overwritten.
        Formulae and references will not be updated.
        """
    @property
    def print_title_rows(self):
        """Rows to be printed at the top of every page (ex: '1:3')"""
    @print_title_rows.setter
    def print_title_rows(self, rows) -> None:
        """
        Set rows to be printed on the top of every page
        format `1:3`
        """
    @property
    def print_title_cols(self):
        """Columns to be printed at the left side of every page (ex: 'A:C')"""
    @print_title_cols.setter
    def print_title_cols(self, cols) -> None:
        """
        Set cols to be printed on the left of every page
        format ``A:C`
        """
    @property
    def print_titles(self): ...
    @property
    def print_area(self):
        """
        The print area for the worksheet, or None if not set. To set, supply a range
        like 'A1:D4' or a list of ranges.
        """
    @print_area.setter
    def print_area(self, value) -> None:
        """
        Range of cells in the form A1:D4 or list of ranges. Print area can be cleared
        by passing `None` or an empty list
        """
