import abc
from ._loop import loop_first as loop_first
from .cells import cell_len as cell_len
from .color import Color as Color, blend_rgb as blend_rgb
from .console import Console as Console, ConsoleOptions as ConsoleOptions, JustifyMethod as JustifyMethod, RenderResult as RenderResult
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .segment import Segment as Segment, Segments as Segments
from .style import Style as Style, StyleType as StyleType
from .text import Text as Text
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from pygments.lexer import Lexer
from pygments.style import Style as PygmentsStyle
from rich.containers import Lines as Lines
from rich.padding import Padding as Padding, PaddingDimensions as PaddingDimensions
from typing import Dict, NamedTuple, Set, Tuple, Type

TokenType = Tuple[str, ...]
WINDOWS: Incomplete
DEFAULT_THEME: str
ANSI_LIGHT: Dict[TokenType, Style]
ANSI_DARK: Dict[TokenType, Style]
RICH_SYNTAX_THEMES: Incomplete
NUMBERS_COLUMN_DEFAULT_PADDING: int

class SyntaxTheme(ABC, metaclass=abc.ABCMeta):
    """Base class for a syntax theme."""
    @abstractmethod
    def get_style_for_token(self, token_type: TokenType) -> Style:
        """Get a style for a given Pygments token."""
    @abstractmethod
    def get_background_style(self) -> Style:
        """Get the background color."""

class PygmentsSyntaxTheme(SyntaxTheme):
    """Syntax theme that delegates to Pygments theme."""
    def __init__(self, theme: str | Type[PygmentsStyle]) -> None: ...
    def get_style_for_token(self, token_type: TokenType) -> Style:
        """Get a style from a Pygments class."""
    def get_background_style(self) -> Style: ...

class ANSISyntaxTheme(SyntaxTheme):
    """Syntax theme to use standard colors."""
    style_map: Incomplete
    def __init__(self, style_map: Dict[TokenType, Style]) -> None: ...
    def get_style_for_token(self, token_type: TokenType) -> Style:
        """Look up style in the style map."""
    def get_background_style(self) -> Style: ...
SyntaxPosition = Tuple[int, int]

class _SyntaxHighlightRange(NamedTuple):
    """
    A range to highlight in a Syntax object.
    `start` and `end` are 2-integers tuples, where the first integer is the line number
    (starting from 1) and the second integer is the column index (starting from 0).
    """
    style: StyleType
    start: SyntaxPosition
    end: SyntaxPosition

class Syntax(JupyterMixin):
    '''Construct a Syntax object to render syntax highlighted code.

    Args:
        code (str): Code to highlight.
        lexer (Lexer | str): Lexer to use (see https://pygments.org/docs/lexers/)
        theme (str, optional): Color theme, aka Pygments style (see https://pygments.org/docs/styles/#getting-a-list-of-available-styles). Defaults to "monokai".
        dedent (bool, optional): Enable stripping of initial whitespace. Defaults to False.
        line_numbers (bool, optional): Enable rendering of line numbers. Defaults to False.
        start_line (int, optional): Starting number for line numbers. Defaults to 1.
        line_range (Tuple[int | None, int | None], optional): If given should be a tuple of the start and end line to render.
            A value of None in the tuple indicates the range is open in that direction.
        highlight_lines (Set[int]): A set of line numbers to highlight.
        code_width: Width of code to render (not including line numbers), or ``None`` to use all available width.
        tab_size (int, optional): Size of tabs. Defaults to 4.
        word_wrap (bool, optional): Enable word wrapping.
        background_color (str, optional): Optional background color, or None to use theme color. Defaults to None.
        indent_guides (bool, optional): Show indent guides. Defaults to False.
        padding (PaddingDimensions): Padding to apply around the syntax. Defaults to 0 (no padding).
    '''
    @classmethod
    def get_theme(cls, name: str | SyntaxTheme) -> SyntaxTheme:
        """Get a syntax theme instance."""
    code: Incomplete
    dedent: Incomplete
    line_numbers: Incomplete
    start_line: Incomplete
    line_range: Incomplete
    highlight_lines: Incomplete
    code_width: Incomplete
    tab_size: Incomplete
    word_wrap: Incomplete
    background_color: Incomplete
    background_style: Incomplete
    indent_guides: Incomplete
    padding: Incomplete
    def __init__(self, code: str, lexer: Lexer | str, *, theme: str | SyntaxTheme = ..., dedent: bool = False, line_numbers: bool = False, start_line: int = 1, line_range: Tuple[int | None, int | None] | None = None, highlight_lines: Set[int] | None = None, code_width: int | None = None, tab_size: int = 4, word_wrap: bool = False, background_color: str | None = None, indent_guides: bool = False, padding: PaddingDimensions = 0) -> None: ...
    @classmethod
    def from_path(cls, path: str, encoding: str = 'utf-8', lexer: Lexer | str | None = None, theme: str | SyntaxTheme = ..., dedent: bool = False, line_numbers: bool = False, line_range: Tuple[int, int] | None = None, start_line: int = 1, highlight_lines: Set[int] | None = None, code_width: int | None = None, tab_size: int = 4, word_wrap: bool = False, background_color: str | None = None, indent_guides: bool = False, padding: PaddingDimensions = 0) -> Syntax:
        '''Construct a Syntax object from a file.

        Args:
            path (str): Path to file to highlight.
            encoding (str): Encoding of file.
            lexer (str | Lexer, optional): Lexer to use. If None, lexer will be auto-detected from path/file content.
            theme (str, optional): Color theme, aka Pygments style (see https://pygments.org/docs/styles/#getting-a-list-of-available-styles). Defaults to "emacs".
            dedent (bool, optional): Enable stripping of initial whitespace. Defaults to True.
            line_numbers (bool, optional): Enable rendering of line numbers. Defaults to False.
            start_line (int, optional): Starting number for line numbers. Defaults to 1.
            line_range (Tuple[int, int], optional): If given should be a tuple of the start and end line to render.
            highlight_lines (Set[int]): A set of line numbers to highlight.
            code_width: Width of code to render (not including line numbers), or ``None`` to use all available width.
            tab_size (int, optional): Size of tabs. Defaults to 4.
            word_wrap (bool, optional): Enable word wrapping of code.
            background_color (str, optional): Optional background color, or None to use theme color. Defaults to None.
            indent_guides (bool, optional): Show indent guides. Defaults to False.
            padding (PaddingDimensions): Padding to apply around the syntax. Defaults to 0 (no padding).

        Returns:
            [Syntax]: A Syntax object that may be printed to the console
        '''
    @classmethod
    def guess_lexer(cls, path: str, code: str | None = None) -> str:
        '''Guess the alias of the Pygments lexer to use based on a path and an optional string of code.
        If code is supplied, it will use a combination of the code and the filename to determine the
        best lexer to use. For example, if the file is ``index.html`` and the file contains Django
        templating syntax, then "html+django" will be returned. If the file is ``index.html``, and no
        templating language is used, the "html" lexer will be used. If no string of code
        is supplied, the lexer will be chosen based on the file extension..

        Args:
             path (AnyStr): The path to the file containing the code you wish to know the lexer for.
             code (str, optional): Optional string of code that will be used as a fallback if no lexer
                is found for the supplied path.

        Returns:
            str: The name of the Pygments lexer that best matches the supplied path/code.
        '''
    @property
    def lexer(self) -> Lexer | None:
        """The lexer for this syntax, or None if no lexer was found.

        Tries to find the lexer by name if a string was passed to the constructor.
        """
    @property
    def default_lexer(self) -> Lexer:
        """A Pygments Lexer to use if one is not specified or invalid."""
    def highlight(self, code: str, line_range: Tuple[int | None, int | None] | None = None) -> Text:
        """Highlight code and return a Text instance.

        Args:
            code (str): Code to highlight.
            line_range(Tuple[int, int], optional): Optional line range to highlight.

        Returns:
            Text: A text instance containing highlighted syntax.
        """
    def stylize_range(self, style: StyleType, start: SyntaxPosition, end: SyntaxPosition) -> None:
        """
        Adds a custom style on a part of the code, that will be applied to the syntax display when it's rendered.
        Line numbers are 1-based, while column indexes are 0-based.

        Args:
            style (StyleType): The style to apply.
            start (Tuple[int, int]): The start of the range, in the form `[line number, column index]`.
            end (Tuple[int, int]): The end of the range, in the form `[line number, column index]`.
        """
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
