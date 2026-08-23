from .color_depth import ColorDepth
from _typeshed import Incomplete
from prompt_toolkit.cursor_shapes import CursorShape
from prompt_toolkit.data_structures import Size
from prompt_toolkit.output import Output
from prompt_toolkit.styles import Attrs
from typing import Callable, Dict, Sequence, TextIO, Tuple

__all__ = ['Vt100_Output']

class _16ColorCache:
    """
    Cache which maps (r, g, b) tuples to 16 ansi colors.

    :param bg: Cache for background colors, instead of foreground.
    """
    bg: Incomplete
    def __init__(self, bg: bool = False) -> None: ...
    def get_code(self, value: tuple[int, int, int], exclude: Sequence[str] = ()) -> _ColorCodeAndName:
        """
        Return a (ansi_code, ansi_name) tuple. (E.g. ``(44, 'ansiblue')``.) for
        a given (r,g,b) value.
        """

class _256ColorCache(Dict[Tuple[int, int, int], int]):
    """
    Cache which maps (r, g, b) tuples to 256 colors.
    """
    colors: Incomplete
    def __init__(self) -> None: ...
    def __missing__(self, value: tuple[int, int, int]) -> int: ...

class _EscapeCodeCache(Dict[Attrs, str]):
    """
    Cache for VT100 escape codes. It maps
    (fgcolor, bgcolor, bold, underline, strike, reverse) tuples to VT100
    escape sequences.

    :param true_color: When True, use 24bit colors instead of 256 colors.
    """
    color_depth: Incomplete
    def __init__(self, color_depth: ColorDepth) -> None: ...
    def __missing__(self, attrs: Attrs) -> str: ...

class Vt100_Output(Output):
    '''
    :param get_size: A callable which returns the `Size` of the output terminal.
    :param stdout: Any object with has a `write` and `flush` method + an \'encoding\' property.
    :param term: The terminal environment variable. (xterm, xterm-256color, linux, ...)
    :param enable_cpr: When `True` (the default), send "cursor position
        request" escape sequences to the output in order to detect the cursor
        position. That way, we can properly determine how much space there is
        available for the UI (especially for drop down menus) to render. The
        `Renderer` will still try to figure out whether the current terminal
        does respond to CPR escapes. When `False`, never attempt to send CPR
        requests.
    '''
    stdout: Incomplete
    default_color_depth: Incomplete
    term: Incomplete
    enable_bell: Incomplete
    enable_cpr: Incomplete
    def __init__(self, stdout: TextIO, get_size: Callable[[], Size], term: str | None = None, default_color_depth: ColorDepth | None = None, enable_bell: bool = True, enable_cpr: bool = True) -> None: ...
    @classmethod
    def from_pty(cls, stdout: TextIO, term: str | None = None, default_color_depth: ColorDepth | None = None, enable_bell: bool = True) -> Vt100_Output:
        """
        Create an Output class from a pseudo terminal.
        (This will take the dimensions by reading the pseudo
        terminal attributes.)
        """
    def get_size(self) -> Size: ...
    def fileno(self) -> int:
        """Return file descriptor."""
    def encoding(self) -> str:
        """Return encoding used for stdout."""
    def write_raw(self, data: str) -> None:
        """
        Write raw data to output.
        """
    def write(self, data: str) -> None:
        """
        Write text to output.
        (Removes vt100 escape codes. -- used for safely writing text.)
        """
    def set_title(self, title: str) -> None:
        """
        Set terminal title.
        """
    def clear_title(self) -> None: ...
    def erase_screen(self) -> None:
        """
        Erases the screen with the background colour and moves the cursor to
        home.
        """
    def enter_alternate_screen(self) -> None: ...
    def quit_alternate_screen(self) -> None: ...
    def enable_mouse_support(self) -> None: ...
    def disable_mouse_support(self) -> None: ...
    def erase_end_of_line(self) -> None:
        """
        Erases from the current cursor position to the end of the current line.
        """
    def erase_down(self) -> None:
        """
        Erases the screen from the current line down to the bottom of the
        screen.
        """
    def reset_attributes(self) -> None: ...
    def set_attributes(self, attrs: Attrs, color_depth: ColorDepth) -> None:
        """
        Create new style and output.

        :param attrs: `Attrs` instance.
        """
    def disable_autowrap(self) -> None: ...
    def enable_autowrap(self) -> None: ...
    def enable_bracketed_paste(self) -> None: ...
    def disable_bracketed_paste(self) -> None: ...
    def reset_cursor_key_mode(self) -> None:
        """
        For vt100 only.
        Put the terminal in cursor mode (instead of application mode).
        """
    def cursor_goto(self, row: int = 0, column: int = 0) -> None:
        """
        Move cursor position.
        """
    def cursor_up(self, amount: int) -> None: ...
    def cursor_down(self, amount: int) -> None: ...
    def cursor_forward(self, amount: int) -> None: ...
    def cursor_backward(self, amount: int) -> None: ...
    def hide_cursor(self) -> None: ...
    def show_cursor(self) -> None: ...
    def set_cursor_shape(self, cursor_shape: CursorShape) -> None: ...
    def reset_cursor_shape(self) -> None:
        """Reset cursor shape."""
    def flush(self) -> None:
        """
        Write to output stream and flush.
        """
    def ask_for_cpr(self) -> None:
        """
        Asks for a cursor position report (CPR).
        """
    @property
    def responds_to_cpr(self) -> bool: ...
    def bell(self) -> None:
        """Sound bell."""
    def get_default_color_depth(self) -> ColorDepth:
        """
        Return the default color depth for a vt100 terminal, according to the
        our term value.

        We prefer 256 colors almost always, because this is what most terminals
        support these days, and is a good default.
        """
