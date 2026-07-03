from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .segment import Segment as Segment
from .style import Style as Style
from _typeshed import Incomplete
from typing import Tuple

PaddingDimensions = int | Tuple[int] | Tuple[int, int] | Tuple[int, int, int, int]

class Padding(JupyterMixin):
    '''Draw space around content.

    Example:
        >>> print(Padding("Hello", (2, 4), style="on blue"))

    Args:
        renderable (RenderableType): String or other renderable.
        pad (Union[int, Tuple[int]]): Padding for top, right, bottom, and left borders.
            May be specified with 1, 2, or 4 integers (CSS style).
        style (Union[str, Style], optional): Style for padding characters. Defaults to "none".
        expand (bool, optional): Expand padding to fit available width. Defaults to True.
    '''
    renderable: Incomplete
    style: Incomplete
    expand: Incomplete
    def __init__(self, renderable: RenderableType, pad: PaddingDimensions = (0, 0, 0, 0), *, style: str | Style = 'none', expand: bool = True) -> None: ...
    @classmethod
    def indent(cls, renderable: RenderableType, level: int) -> Padding:
        """Make padding instance to render an indent.

        Args:
            renderable (RenderableType): String or other renderable.
            level (int): Number of characters to indent.

        Returns:
            Padding: A Padding instance.
        """
    @staticmethod
    def unpack(pad: PaddingDimensions) -> Tuple[int, int, int, int]:
        """Unpack padding specified in CSS style."""
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
