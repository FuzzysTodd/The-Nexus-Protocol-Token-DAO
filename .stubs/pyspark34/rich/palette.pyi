from .color_triplet import ColorTriplet as ColorTriplet
from rich.table import Table as Table
from typing import Sequence, Tuple

class Palette:
    """A palette of available colors."""
    def __init__(self, colors: Sequence[Tuple[int, int, int]]) -> None: ...
    def __getitem__(self, number: int) -> ColorTriplet: ...
    def __rich__(self) -> Table: ...
    def match(self, color: Tuple[int, int, int]) -> int:
        """Find a color from a palette that most closely matches a given color.

        Args:
            color (Tuple[int, int, int]): RGB components in range 0 > 255.

        Returns:
            int: Index of closes matching color.
        """
