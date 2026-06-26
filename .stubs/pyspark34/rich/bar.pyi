from .color import Color as Color
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .segment import Segment as Segment
from .style import Style as Style
from _typeshed import Incomplete

BEGIN_BLOCK_ELEMENTS: Incomplete
END_BLOCK_ELEMENTS: Incomplete
FULL_BLOCK: str

class Bar(JupyterMixin):
    '''Renders a solid block bar.

    Args:
        size (float): Value for the end of the bar.
        begin (float): Begin point (between 0 and size, inclusive).
        end (float): End point (between 0 and size, inclusive).
        width (int, optional): Width of the bar, or ``None`` for maximum width. Defaults to None.
        color (Union[Color, str], optional): Color of the bar. Defaults to "default".
        bgcolor (Union[Color, str], optional): Color of bar background. Defaults to "default".
    '''
    size: Incomplete
    begin: Incomplete
    end: Incomplete
    width: Incomplete
    style: Incomplete
    def __init__(self, size: float, begin: float, end: float, *, width: int | None = None, color: Color | str = 'default', bgcolor: Color | str = 'default') -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
