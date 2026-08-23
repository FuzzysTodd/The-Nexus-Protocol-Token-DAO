from .dimensions import SheetDimension as SheetDimension
from .hyperlink import HyperlinkList as HyperlinkList
from .merge import MergeCell as MergeCell, MergeCells as MergeCells
from .related import Related as Related
from .table import TablePartList as TablePartList
from _typeshed import Incomplete
from collections.abc import Generator
from openpyxl.cell._writer import write_cell as write_cell
from openpyxl.comments.comment_sheet import CommentRecord as CommentRecord
from openpyxl.packaging.relationship import Relationship as Relationship, RelationshipList as RelationshipList
from openpyxl.styles.differential import DifferentialStyle as DifferentialStyle
from openpyxl.xml.constants import SHEET_MAIN_NS as SHEET_MAIN_NS
from openpyxl.xml.functions import xmlfile as xmlfile

ALL_TEMP_FILES: Incomplete

def create_temporary_file(suffix: str = ''): ...

class WorksheetWriter:
    ws: Incomplete
    out: Incomplete
    xf: Incomplete
    def __init__(self, ws, out: Incomplete | None = None) -> None: ...
    def write_properties(self) -> None: ...
    def write_dimensions(self) -> None:
        """
        Write worksheet size if known
        """
    def write_format(self) -> None: ...
    def write_views(self) -> None: ...
    def write_cols(self) -> None: ...
    def write_top(self) -> None:
        """
        Write all elements up to rows:
        properties
        dimensions
        views
        format
        cols
        """
    def rows(self):
        """Return all rows, and any cells that they contain"""
    def write_rows(self) -> None: ...
    def write_row(self, xf, row, row_idx) -> None: ...
    def write_protection(self) -> None: ...
    def write_scenarios(self) -> None: ...
    def write_filter(self) -> None: ...
    def write_sort(self) -> None:
        """
        As per discusion with the OOXML Working Group global sort state is not required.
        openpyxl never reads it from existing files
        """
    def write_merged_cells(self) -> None: ...
    def write_formatting(self) -> None: ...
    def write_validations(self) -> None: ...
    def write_hyperlinks(self) -> None: ...
    def write_print(self) -> None: ...
    def write_margins(self) -> None: ...
    def write_page(self) -> None: ...
    def write_header(self) -> None: ...
    def write_breaks(self) -> None: ...
    def write_drawings(self) -> None: ...
    def write_legacy(self) -> None:
        """
        Comments & VBA controls use VML and require an additional element
        that is no longer in the specification.
        """
    def write_tables(self) -> None: ...
    def get_stream(self) -> Generator[Incomplete, Incomplete, None]: ...
    def write_tail(self) -> None:
        """
        Write all elements after the rows
        calc properties
        protection
        protected ranges #
        scenarios
        filters
        sorts # always ignored
        data consolidation #
        custom views #
        merged cells
        phonetic properties #
        conditional formatting
        data validation
        hyperlinks
        print options
        page margins
        page setup
        header
        row breaks
        col breaks
        custom properties #
        cell watches #
        ignored errors #
        smart tags #
        drawing
        drawingHF #
        background #
        OLE objects #
        controls #
        web publishing #
        tables
        """
    def write(self) -> None:
        """
        High level
        """
    def close(self) -> None:
        """
        Close the context manager
        """
    def read(self):
        """
        Close the context manager and return serialised XML
        """
    def cleanup(self) -> None:
        """
        Remove tempfile
        """
