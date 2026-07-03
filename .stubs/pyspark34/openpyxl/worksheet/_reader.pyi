from .datavalidation import DataValidationList as DataValidationList
from .dimensions import SheetDimension as SheetDimension
from .filters import AutoFilter as AutoFilter
from .formula import ArrayFormula as ArrayFormula, DataTableFormula as DataTableFormula
from .header_footer import HeaderFooter as HeaderFooter
from .hyperlink import HyperlinkList as HyperlinkList
from .merge import MergeCells as MergeCells
from .page import PageMargins as PageMargins, PrintOptions as PrintOptions, PrintPageSetup as PrintPageSetup
from .pagebreak import ColBreak as ColBreak, RowBreak as RowBreak
from .properties import WorksheetProperties as WorksheetProperties
from .protection import SheetProtection as SheetProtection
from .related import Related as Related
from .scenario import ScenarioList as ScenarioList
from .table import TablePartList as TablePartList
from .views import SheetViewList as SheetViewList
from _typeshed import Incomplete
from collections.abc import Generator
from openpyxl.cell import Cell as Cell, MergedCell as MergedCell
from openpyxl.cell.rich_text import CellRichText as CellRichText
from openpyxl.cell.text import Text as Text
from openpyxl.descriptors.excel import ExtensionList as ExtensionList
from openpyxl.formatting.formatting import ConditionalFormatting as ConditionalFormatting
from openpyxl.formula.translate import Translator as Translator
from openpyxl.utils import coordinate_to_tuple as coordinate_to_tuple, get_column_letter as get_column_letter
from openpyxl.utils.datetime import WINDOWS_EPOCH as WINDOWS_EPOCH, from_ISO8601 as from_ISO8601, from_excel as from_excel
from openpyxl.worksheet.dimensions import ColumnDimension as ColumnDimension, RowDimension as RowDimension, SheetFormatProperties as SheetFormatProperties
from openpyxl.xml.constants import EXT_TYPES as EXT_TYPES, SHEET_MAIN_NS as SHEET_MAIN_NS
from openpyxl.xml.functions import iterparse as iterparse

CELL_TAG: Incomplete
VALUE_TAG: Incomplete
FORMULA_TAG: Incomplete
MERGE_TAG: Incomplete
INLINE_STRING: Incomplete
COL_TAG: Incomplete
ROW_TAG: Incomplete
CF_TAG: Incomplete
LEGACY_TAG: Incomplete
PROT_TAG: Incomplete
EXT_TAG: Incomplete
HYPERLINK_TAG: Incomplete
TABLE_TAG: Incomplete
PRINT_TAG: Incomplete
MARGINS_TAG: Incomplete
PAGE_TAG: Incomplete
HEADER_TAG: Incomplete
FILTER_TAG: Incomplete
VALIDATION_TAG: Incomplete
PROPERTIES_TAG: Incomplete
VIEWS_TAG: Incomplete
FORMAT_TAG: Incomplete
ROW_BREAK_TAG: Incomplete
COL_BREAK_TAG: Incomplete
SCENARIOS_TAG: Incomplete
DATA_TAG: Incomplete
DIMENSION_TAG: Incomplete
CUSTOM_VIEWS_TAG: Incomplete

def parse_richtext_string(element):
    """
    Parse inline string and preserve rich text formatting
    """

class WorkSheetParser:
    min_row: Incomplete
    epoch: Incomplete
    source: Incomplete
    shared_strings: Incomplete
    data_only: Incomplete
    shared_formulae: Incomplete
    row_counter: int
    tables: Incomplete
    date_formats: Incomplete
    timedelta_formats: Incomplete
    row_dimensions: Incomplete
    column_dimensions: Incomplete
    number_formats: Incomplete
    keep_vba: bool
    hyperlinks: Incomplete
    formatting: Incomplete
    legacy_drawing: Incomplete
    merged_cells: Incomplete
    row_breaks: Incomplete
    col_breaks: Incomplete
    rich_text: Incomplete
    def __init__(self, src, shared_strings, data_only: bool = False, epoch=..., date_formats=..., timedelta_formats=..., rich_text: bool = False) -> None: ...
    def parse(self) -> Generator[Incomplete, None, None]: ...
    def parse_dimensions(self):
        """
        Get worksheet dimensions if they are provided.
        """
    col_counter: Incomplete
    def parse_cell(self, element): ...
    def parse_formula(self, element):
        """
        possible formulae types: shared, array, datatable
        """
    def parse_column_dimensions(self, col) -> None: ...
    def parse_row(self, row): ...
    def parse_formatting(self, element) -> None: ...
    protection: Incomplete
    def parse_sheet_protection(self, element) -> None: ...
    def parse_extensions(self, element) -> None: ...
    def parse_legacy(self, element) -> None: ...
    def parse_row_breaks(self, element) -> None: ...
    def parse_col_breaks(self, element) -> None: ...
    def parse_custom_views(self, element) -> None: ...

class WorksheetReader:
    """
    Create a parser and apply it to a workbook
    """
    ws: Incomplete
    parser: Incomplete
    tables: Incomplete
    def __init__(self, ws, xml_source, shared_strings, data_only, rich_text) -> None: ...
    def bind_cells(self) -> None: ...
    def bind_formatting(self) -> None: ...
    def bind_tables(self) -> None: ...
    def bind_merged_cells(self) -> None: ...
    def bind_hyperlinks(self) -> None: ...
    def normalize_merged_cell_link(self, coord):
        """
        Returns the appropriate cell to which a hyperlink, which references a merged cell at the specified coordinates,
        should be bound.
        """
    def bind_col_dimensions(self) -> None: ...
    def bind_row_dimensions(self) -> None: ...
    def bind_properties(self) -> None: ...
    def bind_all(self) -> None: ...
