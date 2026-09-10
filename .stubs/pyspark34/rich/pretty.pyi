from . import get_console as get_console
from ._loop import loop_last as loop_last
from ._pick import pick_bool as pick_bool
from .abc import RichRenderable as RichRenderable
from .cells import cell_len as cell_len
from .console import Console as Console, ConsoleOptions as ConsoleOptions, HighlighterType as HighlighterType, JustifyMethod as JustifyMethod, OverflowMethod as OverflowMethod, RenderResult as RenderResult
from .highlighter import ReprHighlighter as ReprHighlighter
from .jupyter import JupyterMixin as JupyterMixin, JupyterRenderable as JupyterRenderable
from .measure import Measurement as Measurement
from .text import Text as Text
from _typeshed import Incomplete
from dataclasses import dataclass
from rich.repr import RichReprResult as RichReprResult
from typing import Any, Iterable, List, NamedTuple

class _dummy_namedtuple(NamedTuple): ...

def install(console: Console | None = None, overflow: OverflowMethod = 'ignore', crop: bool = False, indent_guides: bool = False, max_length: int | None = None, max_string: int | None = None, max_depth: int | None = None, expand_all: bool = False) -> None:
    '''Install automatic pretty printing in the Python REPL.

    Args:
        console (Console, optional): Console instance or ``None`` to use global console. Defaults to None.
        overflow (Optional[OverflowMethod], optional): Overflow method. Defaults to "ignore".
        crop (Optional[bool], optional): Enable cropping of long lines. Defaults to False.
        indent_guides (bool, optional): Enable indentation guides. Defaults to False.
        max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to None.
        max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to None.
        max_depth (int, optional): Maximum depth of nested data structures, or None for no maximum. Defaults to None.
        expand_all (bool, optional): Expand all containers. Defaults to False.
        max_frames (int): Maximum number of frames to show in a traceback, 0 for no maximum. Defaults to 100.
    '''

class Pretty(JupyterMixin):
    """A rich renderable that pretty prints an object.

    Args:
        _object (Any): An object to pretty print.
        highlighter (HighlighterType, optional): Highlighter object to apply to result, or None for ReprHighlighter. Defaults to None.
        indent_size (int, optional): Number of spaces in indent. Defaults to 4.
        justify (JustifyMethod, optional): Justify method, or None for default. Defaults to None.
        overflow (OverflowMethod, optional): Overflow method, or None for default. Defaults to None.
        no_wrap (Optional[bool], optional): Disable word wrapping. Defaults to False.
        indent_guides (bool, optional): Enable indentation guides. Defaults to False.
        max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to None.
        max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to None.
        max_depth (int, optional): Maximum depth of nested data structures, or None for no maximum. Defaults to None.
        expand_all (bool, optional): Expand all containers. Defaults to False.
        margin (int, optional): Subtrace a margin from width to force containers to expand earlier. Defaults to 0.
        insert_line (bool, optional): Insert a new line if the output has multiple new lines. Defaults to False.
    """
    highlighter: Incomplete
    indent_size: Incomplete
    justify: Incomplete
    overflow: Incomplete
    no_wrap: Incomplete
    indent_guides: Incomplete
    max_length: Incomplete
    max_string: Incomplete
    max_depth: Incomplete
    expand_all: Incomplete
    margin: Incomplete
    insert_line: Incomplete
    def __init__(self, _object: Any, highlighter: HighlighterType | None = None, *, indent_size: int = 4, justify: JustifyMethod | None = None, overflow: OverflowMethod | None = None, no_wrap: bool | None = False, indent_guides: bool = False, max_length: int | None = None, max_string: int | None = None, max_depth: int | None = None, expand_all: bool = False, margin: int = 0, insert_line: bool = False) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...

def is_expandable(obj: Any) -> bool:
    """Check if an object may be expanded by pretty print."""

@dataclass
class Node:
    """A node in a repr tree. May be atomic or a container."""
    key_repr: str = ...
    value_repr: str = ...
    open_brace: str = ...
    close_brace: str = ...
    empty: str = ...
    last: bool = ...
    is_tuple: bool = ...
    is_namedtuple: bool = ...
    children: List['Node'] | None = ...
    key_separator: str = ...
    separator: str = ...
    def iter_tokens(self) -> Iterable[str]:
        """Generate tokens for this node."""
    def check_length(self, start_length: int, max_length: int) -> bool:
        """Check the length fits within a limit.

        Args:
            start_length (int): Starting length of the line (indent, prefix, suffix).
            max_length (int): Maximum length.

        Returns:
            bool: True if the node can be rendered within max length, otherwise False.
        """
    def render(self, max_width: int = 80, indent_size: int = 4, expand_all: bool = False) -> str:
        """Render the node to a pretty repr.

        Args:
            max_width (int, optional): Maximum width of the repr. Defaults to 80.
            indent_size (int, optional): Size of indents. Defaults to 4.
            expand_all (bool, optional): Expand all levels. Defaults to False.

        Returns:
            str: A repr string of the original object.
        """
    def __init__(self, key_repr, value_repr, open_brace, close_brace, empty, last, is_tuple, is_namedtuple, children, key_separator, separator) -> None: ...

@dataclass
class _Line:
    """A line in repr output."""
    parent: _Line | None = ...
    is_root: bool = ...
    node: Node | None = ...
    text: str = ...
    suffix: str = ...
    whitespace: str = ...
    expanded: bool = ...
    last: bool = ...
    @property
    def expandable(self) -> bool:
        """Check if the line may be expanded."""
    def check_length(self, max_length: int) -> bool:
        """Check this line fits within a given number of cells."""
    def expand(self, indent_size: int) -> Iterable['_Line']:
        """Expand this line by adding children on their own line."""
    def __init__(self, parent, is_root, node, text, suffix, whitespace, expanded, last) -> None: ...

def traverse(_object: Any, max_length: int | None = None, max_string: int | None = None, max_depth: int | None = None) -> Node:
    """Traverse object and generate a tree.

    Args:
        _object (Any): Object to be traversed.
        max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to None.
        max_string (int, optional): Maximum length of string before truncating, or None to disable truncating.
            Defaults to None.
        max_depth (int, optional): Maximum depth of data structures, or None for no maximum.
            Defaults to None.

    Returns:
        Node: The root of a tree structure which can be used to render a pretty repr.
    """
def pretty_repr(_object: Any, *, max_width: int = 80, indent_size: int = 4, max_length: int | None = None, max_string: int | None = None, max_depth: int | None = None, expand_all: bool = False) -> str:
    """Prettify repr string by expanding on to new lines to fit within a given width.

    Args:
        _object (Any): Object to repr.
        max_width (int, optional): Desired maximum width of repr string. Defaults to 80.
        indent_size (int, optional): Number of spaces to indent. Defaults to 4.
        max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to None.
        max_string (int, optional): Maximum length of string before truncating, or None to disable truncating.
            Defaults to None.
        max_depth (int, optional): Maximum depth of nested data structure, or None for no depth.
            Defaults to None.
        expand_all (bool, optional): Expand all containers regardless of available width. Defaults to False.

    Returns:
        str: A possibly multi-line representation of the object.
    """
def pprint(_object: Any, *, console: Console | None = None, indent_guides: bool = True, max_length: int | None = None, max_string: int | None = None, max_depth: int | None = None, expand_all: bool = False) -> None:
    """A convenience function for pretty printing.

    Args:
        _object (Any): Object to pretty print.
        console (Console, optional): Console instance, or None to use default. Defaults to None.
        max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to None.
        max_string (int, optional): Maximum length of strings before truncating, or None to disable. Defaults to None.
        max_depth (int, optional): Maximum depth for nested data structures, or None for unlimited depth. Defaults to None.
        indent_guides (bool, optional): Enable indentation guides. Defaults to True.
        expand_all (bool, optional): Expand all containers. Defaults to False.
    """
