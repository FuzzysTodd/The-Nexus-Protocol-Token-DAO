from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .measure import Measurement as Measurement
from .segment import Segment as Segment
from .style import StyleType as StyleType
from _typeshed import Incomplete

class Styled:
    """Apply a style to a renderable.

    Args:
        renderable (RenderableType): Any renderable.
        style (StyleType): A style to apply across the entire renderable.
    """
    renderable: Incomplete
    style: Incomplete
    def __init__(self, renderable: RenderableType, style: StyleType) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
