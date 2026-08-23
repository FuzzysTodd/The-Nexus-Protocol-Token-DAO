from . import box as box, errors as errors
from ._loop import loop_first_last as loop_first_last, loop_last as loop_last
from ._pick import pick_bool as pick_bool
from ._ratio import ratio_distribute as ratio_distribute, ratio_reduce as ratio_reduce
from .align import VerticalAlignMethod as VerticalAlignMethod
from .console import Console as Console, ConsoleOptions as ConsoleOptions, JustifyMethod as JustifyMethod, OverflowMethod as OverflowMethod, RenderResult as RenderResult, RenderableType as RenderableType
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .padding import Padding as Padding, PaddingDimensions as PaddingDimensions
from .protocol import is_renderable as is_renderable
from .segment import Segment as Segment
from .style import Style as Style, StyleType as StyleType
from .text import Text as Text, TextType as TextType
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Iterable, List, NamedTuple, Tuple

@dataclass
class Column:
    '''Defines a column within a ~Table.

    Args:
        title (Union[str, Text], optional): The title of the table rendered at the top. Defaults to None.
        caption (Union[str, Text], optional): The table caption rendered below. Defaults to None.
        width (int, optional): The width in characters of the table, or ``None`` to automatically fit. Defaults to None.
        min_width (Optional[int], optional): The minimum width of the table, or ``None`` for no minimum. Defaults to None.
        box (box.Box, optional): One of the constants in box.py used to draw the edges (see :ref:`appendix_box`), or ``None`` for no box lines. Defaults to box.HEAVY_HEAD.
        safe_box (Optional[bool], optional): Disable box characters that don\'t display on windows legacy terminal with *raster* fonts. Defaults to True.
        padding (PaddingDimensions, optional): Padding for cells (top, right, bottom, left). Defaults to (0, 1).
        collapse_padding (bool, optional): Enable collapsing of padding around cells. Defaults to False.
        pad_edge (bool, optional): Enable padding of edge cells. Defaults to True.
        expand (bool, optional): Expand the table to fit the available space if ``True``, otherwise the table width will be auto-calculated. Defaults to False.
        show_header (bool, optional): Show a header row. Defaults to True.
        show_footer (bool, optional): Show a footer row. Defaults to False.
        show_edge (bool, optional): Draw a box around the outside of the table. Defaults to True.
        show_lines (bool, optional): Draw lines between every row. Defaults to False.
        leading (bool, optional): Number of blank lines between rows (precludes ``show_lines``). Defaults to 0.
        style (Union[str, Style], optional): Default style for the table. Defaults to "none".
        row_styles (List[Union, str], optional): Optional list of row styles, if more than one style is given then the styles will alternate. Defaults to None.
        header_style (Union[str, Style], optional): Style of the header. Defaults to "table.header".
        footer_style (Union[str, Style], optional): Style of the footer. Defaults to "table.footer".
        border_style (Union[str, Style], optional): Style of the border. Defaults to None.
        title_style (Union[str, Style], optional): Style of the title. Defaults to None.
        caption_style (Union[str, Style], optional): Style of the caption. Defaults to None.
        title_justify (str, optional): Justify method for title. Defaults to "center".
        caption_justify (str, optional): Justify method for caption. Defaults to "center".
        highlight (bool, optional): Highlight cell contents (if str). Defaults to False.
    '''
    header: RenderableType = ...
    footer: RenderableType = ...
    header_style: StyleType = ...
    footer_style: StyleType = ...
    style: StyleType = ...
    justify: JustifyMethod = ...
    vertical: VerticalAlignMethod = ...
    overflow: OverflowMethod = ...
    width: int | None = ...
    min_width: int | None = ...
    max_width: int | None = ...
    ratio: int | None = ...
    no_wrap: bool = ...
    def copy(self) -> Column:
        """Return a copy of this Column."""
    @property
    def cells(self) -> Iterable['RenderableType']:
        """Get all cells in the column, not including header."""
    @property
    def flexible(self) -> bool:
        """Check if this column is flexible."""
    def __init__(self, header, footer, header_style, footer_style, style, justify, vertical, overflow, width, min_width, max_width, ratio, no_wrap, _index, _cells) -> None: ...

@dataclass
class Row:
    """Information regarding a row."""
    style: StyleType | None = ...
    end_section: bool = ...
    def __init__(self, style, end_section) -> None: ...

class _Cell(NamedTuple):
    """A single cell in a table."""
    style: StyleType
    renderable: RenderableType
    vertical: VerticalAlignMethod

class Table(JupyterMixin):
    '''A console renderable to draw a table.

    Args:
        *headers (Union[Column, str]): Column headers, either as a string, or :class:`~rich.table.Column` instance.
        title (Union[str, Text], optional): The title of the table rendered at the top. Defaults to None.
        caption (Union[str, Text], optional): The table caption rendered below. Defaults to None.
        width (int, optional): The width in characters of the table, or ``None`` to automatically fit. Defaults to None.
        min_width (Optional[int], optional): The minimum width of the table, or ``None`` for no minimum. Defaults to None.
        box (box.Box, optional): One of the constants in box.py used to draw the edges (see :ref:`appendix_box`), or ``None`` for no box lines. Defaults to box.HEAVY_HEAD.
        safe_box (Optional[bool], optional): Disable box characters that don\'t display on windows legacy terminal with *raster* fonts. Defaults to True.
        padding (PaddingDimensions, optional): Padding for cells (top, right, bottom, left). Defaults to (0, 1).
        collapse_padding (bool, optional): Enable collapsing of padding around cells. Defaults to False.
        pad_edge (bool, optional): Enable padding of edge cells. Defaults to True.
        expand (bool, optional): Expand the table to fit the available space if ``True``, otherwise the table width will be auto-calculated. Defaults to False.
        show_header (bool, optional): Show a header row. Defaults to True.
        show_footer (bool, optional): Show a footer row. Defaults to False.
        show_edge (bool, optional): Draw a box around the outside of the table. Defaults to True.
        show_lines (bool, optional): Draw lines between every row. Defaults to False.
        leading (bool, optional): Number of blank lines between rows (precludes ``show_lines``). Defaults to 0.
        style (Union[str, Style], optional): Default style for the table. Defaults to "none".
        row_styles (List[Union, str], optional): Optional list of row styles, if more than one style is given then the styles will alternate. Defaults to None.
        header_style (Union[str, Style], optional): Style of the header. Defaults to "table.header".
        footer_style (Union[str, Style], optional): Style of the footer. Defaults to "table.footer".
        border_style (Union[str, Style], optional): Style of the border. Defaults to None.
        title_style (Union[str, Style], optional): Style of the title. Defaults to None.
        caption_style (Union[str, Style], optional): Style of the caption. Defaults to None.
        title_justify (str, optional): Justify method for title. Defaults to "center".
        caption_justify (str, optional): Justify method for caption. Defaults to "center".
        highlight (bool, optional): Highlight cell contents (if str). Defaults to False.
    '''
    columns: List[Column]
    rows: List[Row]
    title: Incomplete
    caption: Incomplete
    width: Incomplete
    min_width: Incomplete
    box: Incomplete
    safe_box: Incomplete
    pad_edge: Incomplete
    show_header: Incomplete
    show_footer: Incomplete
    show_edge: Incomplete
    show_lines: Incomplete
    leading: Incomplete
    collapse_padding: Incomplete
    style: Incomplete
    header_style: Incomplete
    footer_style: Incomplete
    border_style: Incomplete
    title_style: Incomplete
    caption_style: Incomplete
    title_justify: Incomplete
    caption_justify: Incomplete
    highlight: Incomplete
    row_styles: Incomplete
    def __init__(self, *headers: Column | str, title: TextType | None = None, caption: TextType | None = None, width: int | None = None, min_width: int | None = None, box: box.Box | None = ..., safe_box: bool | None = None, padding: PaddingDimensions = (0, 1), collapse_padding: bool = False, pad_edge: bool = True, expand: bool = False, show_header: bool = True, show_footer: bool = False, show_edge: bool = True, show_lines: bool = False, leading: int = 0, style: StyleType = 'none', row_styles: Iterable[StyleType] | None = None, header_style: StyleType | None = 'table.header', footer_style: StyleType | None = 'table.footer', border_style: StyleType | None = None, title_style: StyleType | None = None, caption_style: StyleType | None = None, title_justify: JustifyMethod = 'center', caption_justify: JustifyMethod = 'center', highlight: bool = False) -> None: ...
    @classmethod
    def grid(cls, *headers: Column | str, padding: PaddingDimensions = 0, collapse_padding: bool = True, pad_edge: bool = False, expand: bool = False) -> Table:
        """Get a table with no lines, headers, or footer.

        Args:
            *headers (Union[Column, str]): Column headers, either as a string, or :class:`~rich.table.Column` instance.
            padding (PaddingDimensions, optional): Get padding around cells. Defaults to 0.
            collapse_padding (bool, optional): Enable collapsing of padding around cells. Defaults to True.
            pad_edge (bool, optional): Enable padding around edges of table. Defaults to False.
            expand (bool, optional): Expand the table to fit the available space if ``True``, otherwise the table width will be auto-calculated. Defaults to False.

        Returns:
            Table: A table instance.
        """
    @property
    def expand(self) -> bool:
        """Setting a non-None self.width implies expand."""
    @expand.setter
    def expand(self, expand: bool) -> None:
        """Set expand."""
    @property
    def row_count(self) -> int:
        """Get the current number of rows."""
    def get_row_style(self, console: Console, index: int) -> StyleType:
        """Get the current row style."""
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
    @property
    def padding(self) -> Tuple[int, int, int, int]:
        """Get cell padding."""
    @padding.setter
    def padding(self, padding: PaddingDimensions) -> Table:
        """Set cell padding."""
    def add_column(self, header: RenderableType = '', footer: RenderableType = '', *, header_style: StyleType | None = None, footer_style: StyleType | None = None, style: StyleType | None = None, justify: JustifyMethod = 'left', vertical: VerticalAlignMethod = 'top', overflow: OverflowMethod = 'ellipsis', width: int | None = None, min_width: int | None = None, max_width: int | None = None, ratio: int | None = None, no_wrap: bool = False) -> None:
        '''Add a column to the table.

        Args:
            header (RenderableType, optional): Text or renderable for the header.
                Defaults to "".
            footer (RenderableType, optional): Text or renderable for the footer.
                Defaults to "".
            header_style (Union[str, Style], optional): Style for the header, or None for default. Defaults to None.
            footer_style (Union[str, Style], optional): Style for the footer, or None for default. Defaults to None.
            style (Union[str, Style], optional): Style for the column cells, or None for default. Defaults to None.
            justify (JustifyMethod, optional): Alignment for cells. Defaults to "left".
            vertical (VerticalAlignMethod, optional): Vertical alignment, one of "top", "middle", or "bottom". Defaults to "top".
            overflow (OverflowMethod): Overflow method: "crop", "fold", "ellipsis". Defaults to "ellipsis".
            width (int, optional): Desired width of column in characters, or None to fit to contents. Defaults to None.
            min_width (Optional[int], optional): Minimum width of column, or ``None`` for no minimum. Defaults to None.
            max_width (Optional[int], optional): Maximum width of column, or ``None`` for no maximum. Defaults to None.
            ratio (int, optional): Flexible ratio for the column (requires ``Table.expand`` or ``Table.width``). Defaults to None.
            no_wrap (bool, optional): Set to ``True`` to disable wrapping of this column.
        '''
    def add_row(self, *renderables: RenderableType | None, style: StyleType | None = None, end_section: bool = False) -> None:
        """Add a row of renderables.

        Args:
            *renderables (None or renderable): Each cell in a row must be a renderable object (including str),
                or ``None`` for a blank cell.
            style (StyleType, optional): An optional style to apply to the entire row. Defaults to None.
            end_section (bool, optional): End a section and draw a line. Defaults to False.

        Raises:
            errors.NotRenderableError: If you add something that can't be rendered.
        """
    def add_section(self) -> None:
        """Add a new section (draw a line after current row)."""
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
