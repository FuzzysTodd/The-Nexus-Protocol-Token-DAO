from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .constrain import Constrain as Constrain
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .segment import Segment as Segment
from .style import StyleType as StyleType
from _typeshed import Incomplete

AlignMethod: Incomplete
VerticalAlignMethod: Incomplete

class Align(JupyterMixin):
    '''Align a renderable by adding spaces if necessary.

    Args:
        renderable (RenderableType): A console renderable.
        align (AlignMethod): One of "left", "center", or "right""
        style (StyleType, optional): An optional style to apply to the background.
        vertical (Optional[VerticalAlginMethod], optional): Optional vertical align, one of "top", "middle", or "bottom". Defaults to None.
        pad (bool, optional): Pad the right with spaces. Defaults to True.
        width (int, optional): Restrict contents to given width, or None to use default width. Defaults to None.
        height (int, optional): Set height of align renderable, or None to fit to contents. Defaults to None.

    Raises:
        ValueError: if ``align`` is not one of the expected values.
    '''
    renderable: Incomplete
    align: Incomplete
    style: Incomplete
    vertical: Incomplete
    pad: Incomplete
    width: Incomplete
    height: Incomplete
    def __init__(self, renderable: RenderableType, align: AlignMethod = 'left', style: StyleType | None = None, *, vertical: VerticalAlignMethod | None = None, pad: bool = True, width: int | None = None, height: int | None = None) -> None: ...
    @classmethod
    def left(cls, renderable: RenderableType, style: StyleType | None = None, *, vertical: VerticalAlignMethod | None = None, pad: bool = True, width: int | None = None, height: int | None = None) -> Align:
        """Align a renderable to the left."""
    @classmethod
    def center(cls, renderable: RenderableType, style: StyleType | None = None, *, vertical: VerticalAlignMethod | None = None, pad: bool = True, width: int | None = None, height: int | None = None) -> Align:
        """Align a renderable to the center."""
    @classmethod
    def right(cls, renderable: RenderableType, style: StyleType | None = None, *, vertical: VerticalAlignMethod | None = None, pad: bool = True, width: int | None = None, height: int | None = None) -> Align:
        """Align a renderable to the right."""
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...

class VerticalCenter(JupyterMixin):
    '''Vertically aligns a renderable.

    Warn:
        This class is deprecated and may be removed in a future version. Use Align class with
        `vertical="middle"`.

    Args:
        renderable (RenderableType): A renderable object.
    '''
    renderable: Incomplete
    style: Incomplete
    def __init__(self, renderable: RenderableType, style: StyleType | None = None) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
