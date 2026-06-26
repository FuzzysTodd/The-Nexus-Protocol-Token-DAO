from ._cell_widths import CELL_WIDTHS as CELL_WIDTHS
from typing import Callable, List

def cached_cell_len(text: str) -> int:
    """Get the number of cells required to display text.

    This method always caches, which may use up a lot of memory. It is recommended to use
    `cell_len` over this method.

    Args:
        text (str): Text to display.

    Returns:
        int: Get the number of cells required to display text.
    """
def cell_len(text: str, _cell_len: Callable[[str], int] = ...) -> int:
    """Get the number of cells required to display text.

    Args:
        text (str): Text to display.

    Returns:
        int: Get the number of cells required to display text.
    """
def get_character_cell_size(character: str) -> int:
    """Get the cell size of a character.

    Args:
        character (str): A single character.

    Returns:
        int: Number of cells (0, 1 or 2) occupied by that character.
    """
def set_cell_size(text: str, total: int) -> str:
    """Set the length of a string to fit within given number of cells."""
def chop_cells(text: str, max_size: int, position: int = 0) -> List[str]:
    """Break text in to equal (cell) length strings, returning the characters in reverse
    order"""
