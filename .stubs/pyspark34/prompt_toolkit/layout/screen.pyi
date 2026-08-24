from .containers import Window
from _typeshed import Incomplete
from prompt_toolkit.data_structures import Point
from typing import Callable

__all__ = ['Screen', 'Char']

class Char:
    """
    Represent a single character in a :class:`.Screen`.

    This should be considered immutable.

    :param char: A single character (can be a double-width character).
    :param style: A style string. (Can contain classnames.)
    """
    display_mappings: dict[str, str]
    char: Incomplete
    style: Incomplete
    width: Incomplete
    def __init__(self, char: str = ' ', style: str = '') -> None: ...

class Screen:
    """
    Two dimensional buffer of :class:`.Char` instances.
    """
    data_buffer: Incomplete
    zero_width_escapes: Incomplete
    cursor_positions: Incomplete
    show_cursor: bool
    menu_positions: Incomplete
    width: Incomplete
    height: Incomplete
    visible_windows_to_write_positions: Incomplete
    def __init__(self, default_char: Char | None = None, initial_width: int = 0, initial_height: int = 0) -> None: ...
    @property
    def visible_windows(self) -> list[Window]: ...
    def set_cursor_position(self, window: Window, position: Point) -> None:
        """
        Set the cursor position for a given window.
        """
    def set_menu_position(self, window: Window, position: Point) -> None:
        """
        Set the cursor position for a given window.
        """
    def get_cursor_position(self, window: Window) -> Point:
        """
        Get the cursor position for a given window.
        Returns a `Point`.
        """
    def get_menu_position(self, window: Window) -> Point:
        """
        Get the menu position for a given window.
        (This falls back to the cursor position if no menu position was set.)
        """
    def draw_with_z_index(self, z_index: int, draw_func: Callable[[], None]) -> None:
        """
        Add a draw-function for a `Window` which has a >= 0 z_index.
        This will be postponed until `draw_all_floats` is called.
        """
    def draw_all_floats(self) -> None:
        """
        Draw all float functions in order of z-index.
        """
    def append_style_to_content(self, style_str: str) -> None:
        """
        For all the characters in the screen.
        Set the style string to the given `style_str`.
        """
    def fill_area(self, write_position: WritePosition, style: str = '', after: bool = False) -> None:
        """
        Fill the content of this area, using the given `style`.
        The style is prepended before whatever was here before.
        """

class WritePosition:
    xpos: Incomplete
    ypos: Incomplete
    width: Incomplete
    height: Incomplete
    def __init__(self, xpos: int, ypos: int, width: int, height: int) -> None: ...
