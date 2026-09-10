from .color_triplet import ColorTriplet as ColorTriplet
from .palette import Palette as Palette
from _typeshed import Incomplete
from typing import List

class TerminalTheme:
    """A color theme used when exporting console content.

    Args:
        background (Tuple[int, int, int]): The background color.
        foreground (Tuple[int, int, int]): The foreground (text) color.
        normal (List[Tuple[int, int, int]]): A list of 8 normal intensity colors.
        bright (List[Tuple[int, int, int]], optional): A list of 8 bright colors, or None
            to repeat normal intensity. Defaults to None.
    """
    background_color: Incomplete
    foreground_color: Incomplete
    ansi_colors: Incomplete
    def __init__(self, background: _ColorTuple, foreground: _ColorTuple, normal: List[_ColorTuple], bright: List[_ColorTuple] | None = None) -> None: ...

DEFAULT_TERMINAL_THEME: Incomplete
MONOKAI: Incomplete
DIMMED_MONOKAI: Incomplete
NIGHT_OWLISH: Incomplete
SVG_EXPORT_THEME: Incomplete
