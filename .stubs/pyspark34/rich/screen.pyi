from ._loop import loop_last as loop_last
from .console import Console as Console, ConsoleOptions as ConsoleOptions, Group as Group, RenderResult as RenderResult, RenderableType as RenderableType
from .segment import Segment as Segment
from .style import StyleType as StyleType
from _typeshed import Incomplete

class Screen:
    """A renderable that fills the terminal screen and crops excess.

    Args:
        renderable (RenderableType): Child renderable.
        style (StyleType, optional): Optional background style. Defaults to None.
    """
    renderable: RenderableType
    style: Incomplete
    application_mode: Incomplete
    def __init__(self, *renderables: RenderableType, style: StyleType | None = None, application_mode: bool = False) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
