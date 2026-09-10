from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult
from .segment import ControlCode as ControlCode, ControlType as ControlType, Segment as Segment
from _typeshed import Incomplete
from typing import Callable, Dict, Final

STRIP_CONTROL_CODES: Final[Incomplete]
CONTROL_ESCAPE: Final[Incomplete]
CONTROL_CODES_FORMAT: Dict[int, Callable[..., str]]

class Control:
    """A renderable that inserts a control code (non printable but may move cursor).

    Args:
        *codes (str): Positional arguments are either a :class:`~rich.segment.ControlType` enum or a
            tuple of ControlType and an integer parameter
    """
    segment: Incomplete
    def __init__(self, *codes: ControlType | ControlCode) -> None: ...
    @classmethod
    def bell(cls) -> Control:
        """Ring the 'bell'."""
    @classmethod
    def home(cls) -> Control:
        """Move cursor to 'home' position."""
    @classmethod
    def move(cls, x: int = 0, y: int = 0) -> Control:
        """Move cursor relative to current position.

        Args:
            x (int): X offset.
            y (int): Y offset.

        Returns:
            ~Control: Control object.

        """
    @classmethod
    def move_to_column(cls, x: int, y: int = 0) -> Control:
        """Move to the given column, optionally add offset to row.

        Returns:
            x (int): absolute x (column)
            y (int): optional y offset (row)

        Returns:
            ~Control: Control object.
        """
    @classmethod
    def move_to(cls, x: int, y: int) -> Control:
        """Move cursor to absolute position.

        Args:
            x (int): x offset (column)
            y (int): y offset (row)

        Returns:
            ~Control: Control object.
        """
    @classmethod
    def clear(cls) -> Control:
        """Clear the screen."""
    @classmethod
    def show_cursor(cls, show: bool) -> Control:
        """Show or hide the cursor."""
    @classmethod
    def alt_screen(cls, enable: bool) -> Control:
        """Enable or disable alt screen."""
    @classmethod
    def title(cls, title: str) -> Control:
        """Set the terminal window title

        Args:
            title (str): The new terminal window title
        """
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

def strip_control_codes(text: str, _translate_table: Dict[int, None] = ...) -> str:
    """Remove control codes from text.

    Args:
        text (str): A string possibly contain control codes.

    Returns:
        str: String with control codes removed.
    """
def escape_control_codes(text: str, _translate_table: Dict[int, str] = ...) -> str:
    '''Replace control codes with their "escaped" equivalent in the given text.
    (e.g. "\x08" becomes "\\b")

    Args:
        text (str): A string possibly containing control codes.

    Returns:
        str: String with control codes replaced with their escaped version.
    '''
