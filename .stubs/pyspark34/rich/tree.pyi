from ._loop import loop_first as loop_first, loop_last as loop_last
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .segment import Segment as Segment
from .style import Style as Style, StyleStack as StyleStack, StyleType as StyleType
from .styled import Styled as Styled
from _typeshed import Incomplete

class Tree(JupyterMixin):
    '''A renderable for a tree structure.

    Args:
        label (RenderableType): The renderable or str for the tree label.
        style (StyleType, optional): Style of this tree. Defaults to "tree".
        guide_style (StyleType, optional): Style of the guide lines. Defaults to "tree.line".
        expanded (bool, optional): Also display children. Defaults to True.
        highlight (bool, optional): Highlight renderable (if str). Defaults to False.
    '''
    label: Incomplete
    style: Incomplete
    guide_style: Incomplete
    children: Incomplete
    expanded: Incomplete
    highlight: Incomplete
    hide_root: Incomplete
    def __init__(self, label: RenderableType, *, style: StyleType = 'tree', guide_style: StyleType = 'tree.line', expanded: bool = True, highlight: bool = False, hide_root: bool = False) -> None: ...
    def add(self, label: RenderableType, *, style: StyleType | None = None, guide_style: StyleType | None = None, expanded: bool = True, highlight: bool | None = False) -> Tree:
        '''Add a child tree.

        Args:
            label (RenderableType): The renderable or str for the tree label.
            style (StyleType, optional): Style of this tree. Defaults to "tree".
            guide_style (StyleType, optional): Style of the guide lines. Defaults to "tree.line".
            expanded (bool, optional): Also display children. Defaults to True.
            highlight (Optional[bool], optional): Highlight renderable (if str). Defaults to False.

        Returns:
            Tree: A new child Tree, which may be further modified.
        '''
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
