from .align import AlignMethod as AlignMethod
from .box import Box as Box, ROUNDED as ROUNDED
from .cells import cell_len as cell_len
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement, measure_renderables as measure_renderables
from .padding import Padding as Padding, PaddingDimensions as PaddingDimensions
from .segment import Segment as Segment
from .style import Style as Style, StyleType as StyleType
from .text import Text as Text, TextType as TextType
from _typeshed import Incomplete

class Panel(JupyterMixin):
    '''A console renderable that draws a border around its contents.

    Example:
        >>> console.print(Panel("Hello, World!"))

    Args:
        renderable (RenderableType): A console renderable object.
        box (Box, optional): A Box instance that defines the look of the border (see :ref:`appendix_box`.
            Defaults to box.ROUNDED.
        safe_box (bool, optional): Disable box characters that don\'t display on windows legacy terminal with *raster* fonts. Defaults to True.
        expand (bool, optional): If True the panel will stretch to fill the console
            width, otherwise it will be sized to fit the contents. Defaults to True.
        style (str, optional): The style of the panel (border and contents). Defaults to "none".
        border_style (str, optional): The style of the border. Defaults to "none".
        width (Optional[int], optional): Optional width of panel. Defaults to None to auto-detect.
        height (Optional[int], optional): Optional height of panel. Defaults to None to auto-detect.
        padding (Optional[PaddingDimensions]): Optional padding around renderable. Defaults to 0.
        highlight (bool, optional): Enable automatic highlighting of panel title (if str). Defaults to False.
    '''
    renderable: Incomplete
    box: Incomplete
    title: Incomplete
    title_align: Incomplete
    subtitle: Incomplete
    subtitle_align: Incomplete
    safe_box: Incomplete
    expand: Incomplete
    style: Incomplete
    border_style: Incomplete
    width: Incomplete
    height: Incomplete
    padding: Incomplete
    highlight: Incomplete
    def __init__(self, renderable: RenderableType, box: Box = ..., *, title: TextType | None = None, title_align: AlignMethod = 'center', subtitle: TextType | None = None, subtitle_align: AlignMethod = 'center', safe_box: bool | None = None, expand: bool = True, style: StyleType = 'none', border_style: StyleType = 'none', width: int | None = None, height: int | None = None, padding: PaddingDimensions = (0, 1), highlight: bool = False) -> None: ...
    @classmethod
    def fit(cls, renderable: RenderableType, box: Box = ..., *, title: TextType | None = None, title_align: AlignMethod = 'center', subtitle: TextType | None = None, subtitle_align: AlignMethod = 'center', safe_box: bool | None = None, style: StyleType = 'none', border_style: StyleType = 'none', width: int | None = None, padding: PaddingDimensions = (0, 1)) -> Panel:
        """An alternative constructor that sets expand=False."""
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
