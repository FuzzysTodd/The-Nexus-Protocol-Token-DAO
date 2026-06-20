import abc
from ._ratio import ratio_resolve as ratio_resolve
from .align import Align as Align
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .highlighter import ReprHighlighter as ReprHighlighter
from .panel import Panel as Panel
from .pretty import Pretty as Pretty
from .region import Region as Region
from .repr import Result as Result, rich_repr as rich_repr
from .segment import Segment as Segment
from .style import StyleType as StyleType
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from rich.tree import Tree as Tree
from typing import Iterable, List, NamedTuple, Sequence, Tuple

class LayoutRender(NamedTuple):
    """An individual layout render."""
    region: Region
    render: List[List[Segment]]

RegionMap: Incomplete
RenderMap: Incomplete

class LayoutError(Exception):
    """Layout related error."""
class NoSplitter(LayoutError):
    """Requested splitter does not exist."""

class _Placeholder:
    """An internal renderable used as a Layout placeholder."""
    highlighter: Incomplete
    layout: Incomplete
    style: Incomplete
    def __init__(self, layout: Layout, style: StyleType = '') -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class Splitter(ABC, metaclass=abc.ABCMeta):
    """Base class for a splitter."""
    name: str
    @abstractmethod
    def get_tree_icon(self) -> str:
        """Get the icon (emoji) used in layout.tree"""
    @abstractmethod
    def divide(self, children: Sequence['Layout'], region: Region) -> Iterable[Tuple['Layout', Region]]:
        """Divide a region amongst several child layouts.

        Args:
            children (Sequence(Layout)): A number of child layouts.
            region (Region): A rectangular region to divide.
        """

class RowSplitter(Splitter):
    """Split a layout region in to rows."""
    name: str
    def get_tree_icon(self) -> str: ...
    def divide(self, children: Sequence['Layout'], region: Region) -> Iterable[Tuple['Layout', Region]]: ...

class ColumnSplitter(Splitter):
    """Split a layout region in to columns."""
    name: str
    def get_tree_icon(self) -> str: ...
    def divide(self, children: Sequence['Layout'], region: Region) -> Iterable[Tuple['Layout', Region]]: ...

class Layout:
    """A renderable to divide a fixed height in to rows or columns.

    Args:
        renderable (RenderableType, optional): Renderable content, or None for placeholder. Defaults to None.
        name (str, optional): Optional identifier for Layout. Defaults to None.
        size (int, optional): Optional fixed size of layout. Defaults to None.
        minimum_size (int, optional): Minimum size of layout. Defaults to 1.
        ratio (int, optional): Optional ratio for flexible layout. Defaults to 1.
        visible (bool, optional): Visibility of layout. Defaults to True.
    """
    splitters: Incomplete
    size: Incomplete
    minimum_size: Incomplete
    ratio: Incomplete
    name: Incomplete
    visible: Incomplete
    splitter: Incomplete
    def __init__(self, renderable: RenderableType | None = None, *, name: str | None = None, size: int | None = None, minimum_size: int = 1, ratio: int = 1, visible: bool = True) -> None: ...
    def __rich_repr__(self) -> Result: ...
    @property
    def renderable(self) -> RenderableType:
        """Layout renderable."""
    @property
    def children(self) -> List['Layout']:
        """Gets (visible) layout children."""
    @property
    def map(self) -> RenderMap:
        """Get a map of the last render."""
    def get(self, name: str) -> Layout | None:
        """Get a named layout, or None if it doesn't exist.

        Args:
            name (str): Name of layout.

        Returns:
            Optional[Layout]: Layout instance or None if no layout was found.
        """
    def __getitem__(self, name: str) -> Layout: ...
    @property
    def tree(self) -> Tree:
        """Get a tree renderable to show layout structure."""
    def split(self, *layouts: Layout | RenderableType, splitter: Splitter | str = 'column') -> None:
        """Split the layout in to multiple sub-layouts.

        Args:
            *layouts (Layout): Positional arguments should be (sub) Layout instances.
            splitter (Union[Splitter, str]): Splitter instance or name of splitter.
        """
    def add_split(self, *layouts: Layout | RenderableType) -> None:
        """Add a new layout(s) to existing split.

        Args:
            *layouts (Union[Layout, RenderableType]): Positional arguments should be renderables or (sub) Layout instances.

        """
    def split_row(self, *layouts: Layout | RenderableType) -> None:
        """Split the layout in to a row (layouts side by side).

        Args:
            *layouts (Layout): Positional arguments should be (sub) Layout instances.
        """
    def split_column(self, *layouts: Layout | RenderableType) -> None:
        """Split the layout in to a column (layouts stacked on top of each other).

        Args:
            *layouts (Layout): Positional arguments should be (sub) Layout instances.
        """
    def unsplit(self) -> None:
        """Reset splits to initial state."""
    def update(self, renderable: RenderableType) -> None:
        """Update renderable.

        Args:
            renderable (RenderableType): New renderable object.
        """
    def refresh_screen(self, console: Console, layout_name: str) -> None:
        """Refresh a sub-layout.

        Args:
            console (Console): Console instance where Layout is to be rendered.
            layout_name (str): Name of layout.
        """
    def render(self, console: Console, options: ConsoleOptions) -> RenderMap:
        """Render the sub_layouts.

        Args:
            console (Console): Console instance.
            options (ConsoleOptions): Console options.

        Returns:
            RenderMap: A dict that maps Layout on to a tuple of Region, lines
        """
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
