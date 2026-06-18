from .cells import cached_cell_len as cached_cell_len, cell_len as cell_len, get_character_cell_size as get_character_cell_size, set_cell_size as set_cell_size
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult
from .repr import Result as Result, rich_repr as rich_repr
from .style import Style as Style
from _typeshed import Incomplete
from enum import IntEnum
from typing import Iterable, List, NamedTuple, Sequence, Tuple

log: Incomplete

class ControlType(IntEnum):
    """Non-printable control codes which typically translate to ANSI codes."""
    BELL: int
    CARRIAGE_RETURN: int
    HOME: int
    CLEAR: int
    SHOW_CURSOR: int
    HIDE_CURSOR: int
    ENABLE_ALT_SCREEN: int
    DISABLE_ALT_SCREEN: int
    CURSOR_UP: int
    CURSOR_DOWN: int
    CURSOR_FORWARD: int
    CURSOR_BACKWARD: int
    CURSOR_MOVE_TO_COLUMN: int
    CURSOR_MOVE_TO: int
    ERASE_IN_LINE: int
    SET_WINDOW_TITLE: int
ControlCode = Tuple[ControlType] | Tuple[ControlType, int | str] | Tuple[ControlType, int, int]

class Segment(NamedTuple):
    """A piece of text with associated style. Segments are produced by the Console render process and
    are ultimately converted in to strings to be written to the terminal.

    Args:
        text (str): A piece of text.
        style (:class:`~rich.style.Style`, optional): An optional style to apply to the text.
        control (Tuple[ControlCode], optional): Optional sequence of control codes.

    Attributes:
        cell_length (int): The cell length of this Segment.
    """
    text: str
    style: Style | None = ...
    control: Sequence[ControlCode] | None = ...
    @property
    def cell_length(self) -> int:
        """The number of terminal cells required to display self.text.

        Returns:
            int: A number of cells.
        """
    def __rich_repr__(self) -> Result: ...
    def __bool__(self) -> bool:
        """Check if the segment contains text."""
    @property
    def is_control(self) -> bool:
        """Check if the segment contains control codes."""
    def split_cells(self, cut: int) -> Tuple['Segment', 'Segment']:
        """Split segment in to two segments at the specified column.

        If the cut point falls in the middle of a 2-cell wide character then it is replaced
        by two spaces, to preserve the display width of the parent segment.

        Returns:
            Tuple[Segment, Segment]: Two segments.
        """
    @classmethod
    def line(cls) -> Segment:
        """Make a new line segment."""
    @classmethod
    def apply_style(cls, segments: Iterable['Segment'], style: Style | None = None, post_style: Style | None = None) -> Iterable['Segment']:
        """Apply style(s) to an iterable of segments.

        Returns an iterable of segments where the style is replaced by ``style + segment.style + post_style``.

        Args:
            segments (Iterable[Segment]): Segments to process.
            style (Style, optional): Base style. Defaults to None.
            post_style (Style, optional): Style to apply on top of segment style. Defaults to None.

        Returns:
            Iterable[Segments]: A new iterable of segments (possibly the same iterable).
        """
    @classmethod
    def filter_control(cls, segments: Iterable['Segment'], is_control: bool = False) -> Iterable['Segment']:
        """Filter segments by ``is_control`` attribute.

        Args:
            segments (Iterable[Segment]): An iterable of Segment instances.
            is_control (bool, optional): is_control flag to match in search.

        Returns:
            Iterable[Segment]: And iterable of Segment instances.

        """
    @classmethod
    def split_lines(cls, segments: Iterable['Segment']) -> Iterable[List['Segment']]:
        """Split a sequence of segments in to a list of lines.

        Args:
            segments (Iterable[Segment]): Segments potentially containing line feeds.

        Yields:
            Iterable[List[Segment]]: Iterable of segment lists, one per line.
        """
    @classmethod
    def split_and_crop_lines(cls, segments: Iterable['Segment'], length: int, style: Style | None = None, pad: bool = True, include_new_lines: bool = True) -> Iterable[List['Segment']]:
        """Split segments in to lines, and crop lines greater than a given length.

        Args:
            segments (Iterable[Segment]): An iterable of segments, probably
                generated from console.render.
            length (int): Desired line length.
            style (Style, optional): Style to use for any padding.
            pad (bool): Enable padding of lines that are less than `length`.

        Returns:
            Iterable[List[Segment]]: An iterable of lines of segments.
        """
    @classmethod
    def adjust_line_length(cls, line: List['Segment'], length: int, style: Style | None = None, pad: bool = True) -> List['Segment']:
        """Adjust a line to a given width (cropping or padding as required).

        Args:
            segments (Iterable[Segment]): A list of segments in a single line.
            length (int): The desired width of the line.
            style (Style, optional): The style of padding if used (space on the end). Defaults to None.
            pad (bool, optional): Pad lines with spaces if they are shorter than `length`. Defaults to True.

        Returns:
            List[Segment]: A line of segments with the desired length.
        """
    @classmethod
    def get_line_length(cls, line: List['Segment']) -> int:
        """Get the length of list of segments.

        Args:
            line (List[Segment]): A line encoded as a list of Segments (assumes no '\\\\n' characters),

        Returns:
            int: The length of the line.
        """
    @classmethod
    def get_shape(cls, lines: List[List['Segment']]) -> Tuple[int, int]:
        """Get the shape (enclosing rectangle) of a list of lines.

        Args:
            lines (List[List[Segment]]): A list of lines (no '\\\\n' characters).

        Returns:
            Tuple[int, int]: Width and height in characters.
        """
    @classmethod
    def set_shape(cls, lines: List[List['Segment']], width: int, height: int | None = None, style: Style | None = None, new_lines: bool = False) -> List[List['Segment']]:
        '''Set the shape of a list of lines (enclosing rectangle).

        Args:
            lines (List[List[Segment]]): A list of lines.
            width (int): Desired width.
            height (int, optional): Desired height or None for no change.
            style (Style, optional): Style of any padding added.
            new_lines (bool, optional): Padded lines should include "
". Defaults to False.

        Returns:
            List[List[Segment]]: New list of lines.
        '''
    @classmethod
    def align_top(cls, lines: List[List['Segment']], width: int, height: int, style: Style, new_lines: bool = False) -> List[List['Segment']]:
        '''Aligns lines to top (adds extra lines to bottom as required).

        Args:
            lines (List[List[Segment]]): A list of lines.
            width (int): Desired width.
            height (int, optional): Desired height or None for no change.
            style (Style): Style of any padding added.
            new_lines (bool, optional): Padded lines should include "
". Defaults to False.

        Returns:
            List[List[Segment]]: New list of lines.
        '''
    @classmethod
    def align_bottom(cls, lines: List[List['Segment']], width: int, height: int, style: Style, new_lines: bool = False) -> List[List['Segment']]:
        '''Aligns render to bottom (adds extra lines above as required).

        Args:
            lines (List[List[Segment]]): A list of lines.
            width (int): Desired width.
            height (int, optional): Desired height or None for no change.
            style (Style): Style of any padding added. Defaults to None.
            new_lines (bool, optional): Padded lines should include "
". Defaults to False.

        Returns:
            List[List[Segment]]: New list of lines.
        '''
    @classmethod
    def align_middle(cls, lines: List[List['Segment']], width: int, height: int, style: Style, new_lines: bool = False) -> List[List['Segment']]:
        '''Aligns lines to middle (adds extra lines to above and below as required).

        Args:
            lines (List[List[Segment]]): A list of lines.
            width (int): Desired width.
            height (int, optional): Desired height or None for no change.
            style (Style): Style of any padding added.
            new_lines (bool, optional): Padded lines should include "
". Defaults to False.

        Returns:
            List[List[Segment]]: New list of lines.
        '''
    @classmethod
    def simplify(cls, segments: Iterable['Segment']) -> Iterable['Segment']:
        """Simplify an iterable of segments by combining contiguous segments with the same style.

        Args:
            segments (Iterable[Segment]): An iterable of segments.

        Returns:
            Iterable[Segment]: A possibly smaller iterable of segments that will render the same way.
        """
    @classmethod
    def strip_links(cls, segments: Iterable['Segment']) -> Iterable['Segment']:
        """Remove all links from an iterable of styles.

        Args:
            segments (Iterable[Segment]): An iterable segments.

        Yields:
            Segment: Segments with link removed.
        """
    @classmethod
    def strip_styles(cls, segments: Iterable['Segment']) -> Iterable['Segment']:
        """Remove all styles from an iterable of segments.

        Args:
            segments (Iterable[Segment]): An iterable segments.

        Yields:
            Segment: Segments with styles replace with None
        """
    @classmethod
    def remove_color(cls, segments: Iterable['Segment']) -> Iterable['Segment']:
        """Remove all color from an iterable of segments.

        Args:
            segments (Iterable[Segment]): An iterable segments.

        Yields:
            Segment: Segments with colorless style.
        """
    @classmethod
    def divide(cls, segments: Iterable['Segment'], cuts: Iterable[int]) -> Iterable[List['Segment']]:
        """Divides an iterable of segments in to portions.

        Args:
            cuts (Iterable[int]): Cell positions where to divide.

        Yields:
            [Iterable[List[Segment]]]: An iterable of Segments in List.
        """

class Segments:
    """A simple renderable to render an iterable of segments. This class may be useful if
    you want to print segments outside of a __rich_console__ method.

    Args:
        segments (Iterable[Segment]): An iterable of segments.
        new_lines (bool, optional): Add new lines between segments. Defaults to False.
    """
    segments: Incomplete
    new_lines: Incomplete
    def __init__(self, segments: Iterable[Segment], new_lines: bool = False) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class SegmentLines:
    lines: Incomplete
    new_lines: Incomplete
    def __init__(self, lines: Iterable[List[Segment]], new_lines: bool = False) -> None:
        """A simple renderable containing a number of lines of segments. May be used as an intermediate
        in rendering process.

        Args:
            lines (Iterable[List[Segment]]): Lists of segments forming lines.
            new_lines (bool, optional): Insert new lines after each line. Defaults to False.
        """
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
