from .align import Align as Align, AlignMethod as AlignMethod
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .constrain import Constrain as Constrain
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .padding import Padding as Padding, PaddingDimensions as PaddingDimensions
from .table import Table as Table
from .text import TextType as TextType
from _typeshed import Incomplete
from typing import Iterable

class Columns(JupyterMixin):
    '''Display renderables in neat columns.

    Args:
        renderables (Iterable[RenderableType]): Any number of Rich renderables (including str).
        width (int, optional): The desired width of the columns, or None to auto detect. Defaults to None.
        padding (PaddingDimensions, optional): Optional padding around cells. Defaults to (0, 1).
        expand (bool, optional): Expand columns to full width. Defaults to False.
        equal (bool, optional): Arrange in to equal sized columns. Defaults to False.
        column_first (bool, optional): Align items from top to bottom (rather than left to right). Defaults to False.
        right_to_left (bool, optional): Start column from right hand side. Defaults to False.
        align (str, optional): Align value ("left", "right", or "center") or None for default. Defaults to None.
        title (TextType, optional): Optional title for Columns.
    '''
    renderables: Incomplete
    width: Incomplete
    padding: Incomplete
    expand: Incomplete
    equal: Incomplete
    column_first: Incomplete
    right_to_left: Incomplete
    align: Incomplete
    title: Incomplete
    def __init__(self, renderables: Iterable[RenderableType] | None = None, padding: PaddingDimensions = (0, 1), *, width: int | None = None, expand: bool = False, equal: bool = False, column_first: bool = False, right_to_left: bool = False, align: AlignMethod | None = None, title: TextType | None = None) -> None: ...
    def add_renderable(self, renderable: RenderableType) -> None:
        """Add a renderable to the columns.

        Args:
            renderable (RenderableType): Any renderable object.
        """
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
