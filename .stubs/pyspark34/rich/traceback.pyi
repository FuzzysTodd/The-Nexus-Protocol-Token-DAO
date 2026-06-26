from . import pretty as pretty
from ._loop import loop_last as loop_last
from .columns import Columns as Columns
from .console import Console as Console, ConsoleOptions as ConsoleOptions, ConsoleRenderable as ConsoleRenderable, RenderResult as RenderResult, group as group
from .constrain import Constrain as Constrain
from .highlighter import RegexHighlighter as RegexHighlighter, ReprHighlighter as ReprHighlighter
from .panel import Panel as Panel
from .scope import render_scope as render_scope
from .style import Style as Style
from .syntax import Syntax as Syntax
from .text import Text as Text
from .theme import Theme as Theme
from _typeshed import Incomplete
from dataclasses import dataclass
from types import ModuleType, TracebackType
from typing import Any, Callable, Dict, Iterable, List, Type

WINDOWS: Incomplete
LOCALS_MAX_LENGTH: int
LOCALS_MAX_STRING: int

def install(*, console: Console | None = None, width: int | None = 100, extra_lines: int = 3, theme: str | None = None, word_wrap: bool = False, show_locals: bool = False, locals_max_length: int = ..., locals_max_string: int = ..., locals_hide_dunder: bool = True, locals_hide_sunder: bool | None = None, indent_guides: bool = True, suppress: Iterable[str | ModuleType] = (), max_frames: int = 100) -> Callable[[Type[BaseException], BaseException, TracebackType | None], Any]:
    """Install a rich traceback handler.

    Once installed, any tracebacks will be printed with syntax highlighting and rich formatting.


    Args:
        console (Optional[Console], optional): Console to write exception to. Default uses internal Console instance.
        width (Optional[int], optional): Width (in characters) of traceback. Defaults to 100.
        extra_lines (int, optional): Extra lines of code. Defaults to 3.
        theme (Optional[str], optional): Pygments theme to use in traceback. Defaults to ``None`` which will pick
            a theme appropriate for the platform.
        word_wrap (bool, optional): Enable word wrapping of long lines. Defaults to False.
        show_locals (bool, optional): Enable display of local variables. Defaults to False.
        locals_max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to 10.
        locals_max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to 80.
        locals_hide_dunder (bool, optional): Hide locals prefixed with double underscore. Defaults to True.
        locals_hide_sunder (bool, optional): Hide locals prefixed with single underscore. Defaults to False.
        indent_guides (bool, optional): Enable indent guides in code and locals. Defaults to True.
        suppress (Sequence[Union[str, ModuleType]]): Optional sequence of modules or paths to exclude from traceback.

    Returns:
        Callable: The previous exception handler that was replaced.

    """

@dataclass
class Frame:
    filename: str
    lineno: int
    name: str
    line: str = ...
    locals: Dict[str, pretty.Node] | None = ...
    def __init__(self, filename, lineno, name, line, locals) -> None: ...

@dataclass
class _SyntaxError:
    offset: int
    filename: str
    line: str
    lineno: int
    msg: str
    def __init__(self, offset, filename, line, lineno, msg) -> None: ...

@dataclass
class Stack:
    exc_type: str
    exc_value: str
    syntax_error: _SyntaxError | None = ...
    is_cause: bool = ...
    frames: List[Frame] = ...
    def __init__(self, exc_type, exc_value, syntax_error, is_cause, frames) -> None: ...

@dataclass
class Trace:
    stacks: List[Stack]
    def __init__(self, stacks) -> None: ...

class PathHighlighter(RegexHighlighter):
    highlights: Incomplete

class Traceback:
    """A Console renderable that renders a traceback.

    Args:
        trace (Trace, optional): A `Trace` object produced from `extract`. Defaults to None, which uses
            the last exception.
        width (Optional[int], optional): Number of characters used to traceback. Defaults to 100.
        extra_lines (int, optional): Additional lines of code to render. Defaults to 3.
        theme (str, optional): Override pygments theme used in traceback.
        word_wrap (bool, optional): Enable word wrapping of long lines. Defaults to False.
        show_locals (bool, optional): Enable display of local variables. Defaults to False.
        indent_guides (bool, optional): Enable indent guides in code and locals. Defaults to True.
        locals_max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to 10.
        locals_max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to 80.
        locals_hide_dunder (bool, optional): Hide locals prefixed with double underscore. Defaults to True.
        locals_hide_sunder (bool, optional): Hide locals prefixed with single underscore. Defaults to False.
        suppress (Sequence[Union[str, ModuleType]]): Optional sequence of modules or paths to exclude from traceback.
        max_frames (int): Maximum number of frames to show in a traceback, 0 for no maximum. Defaults to 100.

    """
    LEXERS: Incomplete
    trace: Incomplete
    width: Incomplete
    extra_lines: Incomplete
    theme: Incomplete
    word_wrap: Incomplete
    show_locals: Incomplete
    indent_guides: Incomplete
    locals_max_length: Incomplete
    locals_max_string: Incomplete
    locals_hide_dunder: Incomplete
    locals_hide_sunder: Incomplete
    suppress: Incomplete
    max_frames: Incomplete
    def __init__(self, trace: Trace | None = None, *, width: int | None = 100, extra_lines: int = 3, theme: str | None = None, word_wrap: bool = False, show_locals: bool = False, locals_max_length: int = ..., locals_max_string: int = ..., locals_hide_dunder: bool = True, locals_hide_sunder: bool = False, indent_guides: bool = True, suppress: Iterable[str | ModuleType] = (), max_frames: int = 100) -> None: ...
    @classmethod
    def from_exception(cls, exc_type: Type[Any], exc_value: BaseException, traceback: TracebackType | None, *, width: int | None = 100, extra_lines: int = 3, theme: str | None = None, word_wrap: bool = False, show_locals: bool = False, locals_max_length: int = ..., locals_max_string: int = ..., locals_hide_dunder: bool = True, locals_hide_sunder: bool = False, indent_guides: bool = True, suppress: Iterable[str | ModuleType] = (), max_frames: int = 100) -> Traceback:
        """Create a traceback from exception info

        Args:
            exc_type (Type[BaseException]): Exception type.
            exc_value (BaseException): Exception value.
            traceback (TracebackType): Python Traceback object.
            width (Optional[int], optional): Number of characters used to traceback. Defaults to 100.
            extra_lines (int, optional): Additional lines of code to render. Defaults to 3.
            theme (str, optional): Override pygments theme used in traceback.
            word_wrap (bool, optional): Enable word wrapping of long lines. Defaults to False.
            show_locals (bool, optional): Enable display of local variables. Defaults to False.
            indent_guides (bool, optional): Enable indent guides in code and locals. Defaults to True.
            locals_max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
                Defaults to 10.
            locals_max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to 80.
            locals_hide_dunder (bool, optional): Hide locals prefixed with double underscore. Defaults to True.
            locals_hide_sunder (bool, optional): Hide locals prefixed with single underscore. Defaults to False.
            suppress (Iterable[Union[str, ModuleType]]): Optional sequence of modules or paths to exclude from traceback.
            max_frames (int): Maximum number of frames to show in a traceback, 0 for no maximum. Defaults to 100.

        Returns:
            Traceback: A Traceback instance that may be printed.
        """
    @classmethod
    def extract(cls, exc_type: Type[BaseException], exc_value: BaseException, traceback: TracebackType | None, *, show_locals: bool = False, locals_max_length: int = ..., locals_max_string: int = ..., locals_hide_dunder: bool = True, locals_hide_sunder: bool = False) -> Trace:
        """Extract traceback information.

        Args:
            exc_type (Type[BaseException]): Exception type.
            exc_value (BaseException): Exception value.
            traceback (TracebackType): Python Traceback object.
            show_locals (bool, optional): Enable display of local variables. Defaults to False.
            locals_max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
                Defaults to 10.
            locals_max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to 80.
            locals_hide_dunder (bool, optional): Hide locals prefixed with double underscore. Defaults to True.
            locals_hide_sunder (bool, optional): Hide locals prefixed with single underscore. Defaults to False.

        Returns:
            Trace: A Trace instance which you can use to construct a `Traceback`.
        """
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
