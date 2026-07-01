from . import ansi as ansi, constants as constants, utils as utils
from _typeshed import Incomplete
from enum import Enum
from typing import Any, Sequence

EMPTY: str
SPACE: str

class HorizontalAlignment(Enum):
    """Horizontal alignment of text in a cell"""
    LEFT: int
    CENTER: int
    RIGHT: int

class VerticalAlignment(Enum):
    """Vertical alignment of text in a cell"""
    TOP: int
    MIDDLE: int
    BOTTOM: int

class Column:
    """Table column configuration"""
    header: Incomplete
    width: Incomplete
    header_horiz_align: Incomplete
    header_vert_align: Incomplete
    style_header_text: Incomplete
    data_horiz_align: Incomplete
    data_vert_align: Incomplete
    style_data_text: Incomplete
    max_data_lines: Incomplete
    def __init__(self, header: str, *, width: int | None = None, header_horiz_align: HorizontalAlignment = ..., header_vert_align: VerticalAlignment = ..., style_header_text: bool = True, data_horiz_align: HorizontalAlignment = ..., data_vert_align: VerticalAlignment = ..., style_data_text: bool = True, max_data_lines: int | float = ...) -> None:
        """
        Column initializer

        :param header: label for column header
        :param width: display width of column. This does not account for any borders or padding which
                      may be added (e.g pre_line, inter_cell, and post_line). Header and data text wrap within
                      this width using word-based wrapping (defaults to actual width of header or 1 if header is blank)
        :param header_horiz_align: horizontal alignment of header cells (defaults to left)
        :param header_vert_align: vertical alignment of header cells (defaults to bottom)
        :param style_header_text: if True, then the table is allowed to apply styles to the header text, which may
                                  conflict with any styles the header already has. If False, the header is printed as is.
                                  Table classes which apply style to headers must account for the value of this flag.
                                  (defaults to True)
        :param data_horiz_align: horizontal alignment of data cells (defaults to left)
        :param data_vert_align: vertical alignment of data cells (defaults to top)
        :param style_data_text: if True, then the table is allowed to apply styles to the data text, which may
                                conflict with any styles the data already has. If False, the data is printed as is.
                                Table classes which apply style to data must account for the value of this flag.
                                (defaults to True)
        :param max_data_lines: maximum lines allowed in a data cell. If line count exceeds this, then the final
                               line displayed will be truncated with an ellipsis. (defaults to INFINITY)
        :raises: ValueError if width is less than 1
        :raises: ValueError if max_data_lines is less than 1
        """

class TableCreator:
    """
    Base table creation class. This class handles ANSI style sequences and characters with display widths greater than 1
    when performing width calculations. It was designed with the ability to build tables one row at a time. This helps
    when you have large data sets that you don't want to hold in memory or when you receive portions of the data set
    incrementally.

    TableCreator has one public method: generate_row()

    This function and the Column class provide all features needed to build tables with headers, borders, colors,
    horizontal and vertical alignment, and wrapped text. However, it's generally easier to inherit from this class and
    implement a more granular API rather than use TableCreator directly. There are ready-to-use examples of this
    defined after this class.
    """
    cols: Incomplete
    tab_width: Incomplete
    def __init__(self, cols: Sequence[Column], *, tab_width: int = 4) -> None:
        """
        TableCreator initializer

        :param cols: column definitions for this table
        :param tab_width: all tabs will be replaced with this many spaces. If a row's fill_char is a tab,
                          then it will be converted to one space.
        :raises: ValueError if tab_width is less than 1
        """
    lines: Incomplete
    width: int
    def generate_row(self, row_data: Sequence[Any], is_header: bool, *, fill_char: str = ..., pre_line: str = ..., inter_cell: str = ..., post_line: str = ...) -> str:
        """
        Generate a header or data table row

        :param row_data: data with an entry for each column in the row
        :param is_header: True if writing a header cell, otherwise writing a data cell. This determines whether to
                          use header or data alignment settings as well as maximum lines to wrap.
        :param fill_char: character that fills remaining space in a cell. Defaults to space. If this is a tab,
                          then it will be converted to one space. (Cannot be a line breaking character)
        :param pre_line: string to print before each line of a row. This can be used for a left row border and
                         padding before the first cell's text. (Defaults to blank)
        :param inter_cell: string to print where two cells meet. This can be used for a border between cells and padding
                           between it and the 2 cells' text. (Defaults to 2 spaces)
        :param post_line: string to print after each line of a row. This can be used for padding after
                          the last cell's text and a right row border. (Defaults to blank)
        :return: row string
        :raises: ValueError if row_data isn't the same length as self.cols
        :raises: TypeError if fill_char is more than one character (not including ANSI style sequences)
        :raises: ValueError if fill_char, pre_line, inter_cell, or post_line contains an unprintable
                 character like a newline
        """

class SimpleTable(TableCreator):
    """
    Implementation of TableCreator which generates a borderless table with an optional divider row after the header.
    This class can be used to create the whole table at once or one row at a time.
    """
    column_spacing: Incomplete
    divider_char: Incomplete
    header_bg: Incomplete
    data_bg: Incomplete
    def __init__(self, cols: Sequence[Column], *, column_spacing: int = 2, tab_width: int = 4, divider_char: str | None = '-', header_bg: ansi.BgColor | None = None, data_bg: ansi.BgColor | None = None) -> None:
        """
        SimpleTable initializer

        :param cols: column definitions for this table
        :param column_spacing: how many spaces to place between columns. Defaults to 2.
        :param tab_width: all tabs will be replaced with this many spaces. If a row's fill_char is a tab,
                          then it will be converted to one space.
        :param divider_char: optional character used to build the header divider row. Set this to blank or None if you don't
                             want a divider row. Defaults to dash. (Cannot be a line breaking character)
        :param header_bg: optional background color for header cells (defaults to None)
        :param data_bg: optional background color for data cells (defaults to None)
        :raises: ValueError if tab_width is less than 1
        :raises: ValueError if column_spacing is less than 0
        :raises: TypeError if divider_char is longer than one character
        :raises: ValueError if divider_char is an unprintable character
        """
    def apply_header_bg(self, value: Any) -> str:
        """
        If defined, apply the header background color to header text
        :param value: object whose text is to be colored
        :return: formatted text
        """
    def apply_data_bg(self, value: Any) -> str:
        """
        If defined, apply the data background color to data text
        :param value: object whose text is to be colored
        :return: formatted data string
        """
    @classmethod
    def base_width(cls, num_cols: int, *, column_spacing: int = 2) -> int:
        """
        Utility method to calculate the display width required for a table before data is added to it.
        This is useful when determining how wide to make your columns to have a table be a specific width.

        :param num_cols: how many columns the table will have
        :param column_spacing: how many spaces to place between columns. Defaults to 2.
        :return: base width
        :raises: ValueError if column_spacing is less than 0
        :raises: ValueError if num_cols is less than 1
        """
    def total_width(self) -> int:
        """Calculate the total display width of this table"""
    def generate_header(self) -> str:
        """Generate table header with an optional divider row"""
    def generate_divider(self) -> str:
        """Generate divider row"""
    def generate_data_row(self, row_data: Sequence[Any]) -> str:
        """
        Generate a data row

        :param row_data: data with an entry for each column in the row
        :return: data row string
        :raises: ValueError if row_data isn't the same length as self.cols
        """
    def generate_table(self, table_data: Sequence[Sequence[Any]], *, include_header: bool = True, row_spacing: int = 1) -> str:
        """
        Generate a table from a data set

        :param table_data: Data with an entry for each data row of the table. Each entry should have data for
                           each column in the row.
        :param include_header: If True, then a header will be included at top of table. (Defaults to True)
        :param row_spacing: A number 0 or greater specifying how many blank lines to place between
                            each row (Defaults to 1)
        :raises: ValueError if row_spacing is less than 0
        """

class BorderedTable(TableCreator):
    """
    Implementation of TableCreator which generates a table with borders around the table and between rows. Borders
    between columns can also be toggled. This class can be used to create the whole table at once or one row at a time.
    """
    empty_data: Incomplete
    column_borders: Incomplete
    padding: Incomplete
    border_fg: Incomplete
    border_bg: Incomplete
    header_bg: Incomplete
    data_bg: Incomplete
    def __init__(self, cols: Sequence[Column], *, tab_width: int = 4, column_borders: bool = True, padding: int = 1, border_fg: ansi.FgColor | None = None, border_bg: ansi.BgColor | None = None, header_bg: ansi.BgColor | None = None, data_bg: ansi.BgColor | None = None) -> None:
        """
        BorderedTable initializer

        :param cols: column definitions for this table
        :param tab_width: all tabs will be replaced with this many spaces. If a row's fill_char is a tab,
                          then it will be converted to one space.
        :param column_borders: if True, borders between columns will be included. This gives the table a grid-like
                               appearance. Turning off column borders results in a unified appearance between
                               a row's cells. (Defaults to True)
        :param padding: number of spaces between text and left/right borders of cell
        :param border_fg: optional foreground color for borders (defaults to None)
        :param border_bg: optional background color for borders (defaults to None)
        :param header_bg: optional background color for header cells (defaults to None)
        :param data_bg: optional background color for data cells (defaults to None)
        :raises: ValueError if tab_width is less than 1
        :raises: ValueError if padding is less than 0
        """
    def apply_border_color(self, value: Any) -> str:
        """
        If defined, apply the border foreground and background colors
        :param value: object whose text is to be colored
        :return: formatted text
        """
    def apply_header_bg(self, value: Any) -> str:
        """
        If defined, apply the header background color to header text
        :param value: object whose text is to be colored
        :return: formatted text
        """
    def apply_data_bg(self, value: Any) -> str:
        """
        If defined, apply the data background color to data text
        :param value: object whose text is to be colored
        :return: formatted data string
        """
    @classmethod
    def base_width(cls, num_cols: int, *, column_borders: bool = True, padding: int = 1) -> int:
        """
        Utility method to calculate the display width required for a table before data is added to it.
        This is useful when determining how wide to make your columns to have a table be a specific width.

        :param num_cols: how many columns the table will have
        :param column_borders: if True, borders between columns will be included in the calculation (Defaults to True)
        :param padding: number of spaces between text and left/right borders of cell
        :return: base width
        :raises: ValueError if num_cols is less than 1
        """
    def total_width(self) -> int:
        """Calculate the total display width of this table"""
    def generate_table_top_border(self) -> str:
        """Generate a border which appears at the top of the header and data section"""
    def generate_header_bottom_border(self) -> str:
        """Generate a border which appears at the bottom of the header"""
    def generate_row_bottom_border(self) -> str:
        """Generate a border which appears at the bottom of rows"""
    def generate_table_bottom_border(self) -> str:
        """Generate a border which appears at the bottom of the table"""
    def generate_header(self) -> str:
        """Generate table header"""
    def generate_data_row(self, row_data: Sequence[Any]) -> str:
        """
        Generate a data row

        :param row_data: data with an entry for each column in the row
        :return: data row string
        :raises: ValueError if row_data isn't the same length as self.cols
        """
    def generate_table(self, table_data: Sequence[Sequence[Any]], *, include_header: bool = True) -> str:
        """
        Generate a table from a data set

        :param table_data: Data with an entry for each data row of the table. Each entry should have data for
                           each column in the row.
        :param include_header: If True, then a header will be included at top of table. (Defaults to True)
        """

class AlternatingTable(BorderedTable):
    """
    Implementation of BorderedTable which uses background colors to distinguish between rows instead of row border
    lines. This class can be used to create the whole table at once or one row at a time.

    To nest an AlternatingTable within another AlternatingTable, set style_data_text to False on the Column
    which contains the nested table. That will prevent the current row's background color from affecting the colors
    of the nested table.
    """
    row_num: int
    odd_bg: Incomplete
    even_bg: Incomplete
    def __init__(self, cols: Sequence[Column], *, tab_width: int = 4, column_borders: bool = True, padding: int = 1, border_fg: ansi.FgColor | None = None, border_bg: ansi.BgColor | None = None, header_bg: ansi.BgColor | None = None, odd_bg: ansi.BgColor | None = None, even_bg: ansi.BgColor | None = ...) -> None:
        """
        AlternatingTable initializer

        Note: Specify background colors using subclasses of BgColor (e.g. Bg, EightBitBg, RgbBg)

        :param cols: column definitions for this table
        :param tab_width: all tabs will be replaced with this many spaces. If a row's fill_char is a tab,
                          then it will be converted to one space.
        :param column_borders: if True, borders between columns will be included. This gives the table a grid-like
                               appearance. Turning off column borders results in a unified appearance between
                               a row's cells. (Defaults to True)
        :param padding: number of spaces between text and left/right borders of cell
        :param border_fg: optional foreground color for borders (defaults to None)
        :param border_bg: optional background color for borders (defaults to None)
        :param header_bg: optional background color for header cells (defaults to None)
        :param odd_bg: optional background color for odd numbered data rows (defaults to None)
        :param even_bg: optional background color for even numbered data rows (defaults to StdBg.DARK_GRAY)
        :raises: ValueError if tab_width is less than 1
        :raises: ValueError if padding is less than 0
        """
    def apply_data_bg(self, value: Any) -> str:
        """
        Apply background color to data text based on what row is being generated and whether a color has been defined
        :param value: object whose text is to be colored
        :return: formatted data string
        """
    def generate_data_row(self, row_data: Sequence[Any]) -> str:
        """
        Generate a data row

        :param row_data: data with an entry for each column in the row
        :return: data row string
        """
    def generate_table(self, table_data: Sequence[Sequence[Any]], *, include_header: bool = True) -> str:
        """
        Generate a table from a data set

        :param table_data: Data with an entry for each data row of the table. Each entry should have data for
                           each column in the row.
        :param include_header: If True, then a header will be included at top of table. (Defaults to True)
        """
