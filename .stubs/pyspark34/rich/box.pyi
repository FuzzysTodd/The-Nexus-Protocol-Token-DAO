from ._loop import loop_last as loop_last
from _typeshed import Incomplete
from rich.console import ConsoleOptions as ConsoleOptions
from typing import Iterable, Literal

class Box:
    """Defines characters to render boxes.

    ┌─┬┐ top
    │ ││ head
    ├─┼┤ head_row
    │ ││ mid
    ├─┼┤ row
    ├─┼┤ foot_row
    │ ││ foot
    └─┴┘ bottom

    Args:
        box (str): Characters making up box.
        ascii (bool, optional): True if this box uses ascii characters only. Default is False.
    """
    ascii: Incomplete
    def __init__(self, box: str, *, ascii: bool = False) -> None: ...
    def substitute(self, options: ConsoleOptions, safe: bool = True) -> Box:
        """Substitute this box for another if it won't render due to platform issues.

        Args:
            options (ConsoleOptions): Console options used in rendering.
            safe (bool, optional): Substitute this for another Box if there are known problems
                displaying on the platform (currently only relevant on Windows). Default is True.

        Returns:
            Box: A different Box or the same Box.
        """
    def get_plain_headed_box(self) -> Box:
        """If this box uses special characters for the borders of the header, then
        return the equivalent box that does not.

        Returns:
            Box: The most similar Box that doesn't use header-specific box characters.
                If the current Box already satisfies this criterion, then it's returned.
        """
    def get_top(self, widths: Iterable[int]) -> str:
        """Get the top of a simple box.

        Args:
            widths (List[int]): Widths of columns.

        Returns:
            str: A string of box characters.
        """
    def get_row(self, widths: Iterable[int], level: Literal['head', 'row', 'foot', 'mid'] = 'row', edge: bool = True) -> str:
        """Get the top of a simple box.

        Args:
            width (List[int]): Widths of columns.

        Returns:
            str: A string of box characters.
        """
    def get_bottom(self, widths: Iterable[int]) -> str:
        """Get the bottom of a simple box.

        Args:
            widths (List[int]): Widths of columns.

        Returns:
            str: A string of box characters.
        """

ASCII: Box
ASCII2: Box
ASCII_DOUBLE_HEAD: Box
SQUARE: Box
SQUARE_DOUBLE_HEAD: Box
MINIMAL: Box
MINIMAL_HEAVY_HEAD: Box
MINIMAL_DOUBLE_HEAD: Box
SIMPLE: Box
SIMPLE_HEAD: Box
SIMPLE_HEAVY: Box
HORIZONTALS: Box
ROUNDED: Box
HEAVY: Box
HEAVY_EDGE: Box
HEAVY_HEAD: Box
DOUBLE: Box
DOUBLE_EDGE: Box
MARKDOWN: Box
LEGACY_WINDOWS_SUBSTITUTIONS: Incomplete
PLAIN_HEADED_SUBSTITUTIONS: Incomplete
