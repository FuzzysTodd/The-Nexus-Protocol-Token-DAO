from ._loop import loop_last as loop_last
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .control import Control as Control
from .segment import ControlType as ControlType, Segment as Segment
from .style import StyleType as StyleType
from .text import Text as Text
from _typeshed import Incomplete

VerticalOverflowMethod: Incomplete

class LiveRender:
    '''Creates a renderable that may be updated.

    Args:
        renderable (RenderableType): Any renderable object.
        style (StyleType, optional): An optional style to apply to the renderable. Defaults to "".
    '''
    renderable: Incomplete
    style: Incomplete
    vertical_overflow: Incomplete
    def __init__(self, renderable: RenderableType, style: StyleType = '', vertical_overflow: VerticalOverflowMethod = 'ellipsis') -> None: ...
    def set_renderable(self, renderable: RenderableType) -> None:
        """Set a new renderable.

        Args:
            renderable (RenderableType): Any renderable object, including str.
        """
    def position_cursor(self) -> Control:
        """Get control codes to move cursor to beginning of live render.

        Returns:
            Control: A control instance that may be printed.
        """
    def restore_cursor(self) -> Control:
        """Get control codes to clear the render and restore the cursor to its previous position.

        Returns:
            Control: A Control instance that may be printed.
        """
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
