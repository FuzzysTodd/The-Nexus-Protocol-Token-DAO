from . import box as box
from ._loop import loop_first as loop_first
from ._stack import Stack as Stack
from .console import Console as Console, ConsoleOptions as ConsoleOptions, JustifyMethod as JustifyMethod, RenderResult as RenderResult
from .containers import Renderables as Renderables
from .jupyter import JupyterMixin as JupyterMixin
from .panel import Panel as Panel
from .rule import Rule as Rule
from .segment import Segment as Segment
from .style import Style as Style, StyleStack as StyleStack
from .syntax import Syntax as Syntax
from .text import Text as Text, TextType as TextType
from _typeshed import Incomplete
from markdown_it.token import Token as Token
from rich.table import Table as Table
from typing import ClassVar, Dict, Type

class MarkdownElement:
    new_line: ClassVar[bool]
    @classmethod
    def create(cls, markdown: Markdown, token: Token) -> MarkdownElement:
        """Factory to create markdown element,

        Args:
            markdown (Markdown): The parent Markdown object.
            token (Token): A node from markdown-it.

        Returns:
            MarkdownElement: A new markdown element
        """
    def on_enter(self, context: MarkdownContext) -> None:
        """Called when the node is entered.

        Args:
            context (MarkdownContext): The markdown context.
        """
    def on_text(self, context: MarkdownContext, text: TextType) -> None:
        """Called when text is parsed.

        Args:
            context (MarkdownContext): The markdown context.
        """
    def on_leave(self, context: MarkdownContext) -> None:
        """Called when the parser leaves the element.

        Args:
            context (MarkdownContext): [description]
        """
    def on_child_close(self, context: MarkdownContext, child: MarkdownElement) -> bool:
        """Called when a child element is closed.

        This method allows a parent element to take over rendering of its children.

        Args:
            context (MarkdownContext): The markdown context.
            child (MarkdownElement): The child markdown element.

        Returns:
            bool: Return True to render the element, or False to not render the element.
        """
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class UnknownElement(MarkdownElement):
    """An unknown element.

    Hopefully there will be no unknown elements, and we will have a MarkdownElement for
    everything in the document.

    """

class TextElement(MarkdownElement):
    """Base class for elements that render text."""
    style_name: str
    style: Incomplete
    text: Incomplete
    def on_enter(self, context: MarkdownContext) -> None: ...
    def on_text(self, context: MarkdownContext, text: TextType) -> None: ...
    def on_leave(self, context: MarkdownContext) -> None: ...

class Paragraph(TextElement):
    """A Paragraph."""
    style_name: str
    justify: JustifyMethod
    @classmethod
    def create(cls, markdown: Markdown, token: Token) -> Paragraph: ...
    def __init__(self, justify: JustifyMethod) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class Heading(TextElement):
    """A heading."""
    @classmethod
    def create(cls, markdown: Markdown, token: Token) -> Heading: ...
    text: Incomplete
    def on_enter(self, context: MarkdownContext) -> None: ...
    tag: Incomplete
    style_name: Incomplete
    def __init__(self, tag: str) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class CodeBlock(TextElement):
    """A code block with syntax highlighting."""
    style_name: str
    @classmethod
    def create(cls, markdown: Markdown, token: Token) -> CodeBlock: ...
    lexer_name: Incomplete
    theme: Incomplete
    def __init__(self, lexer_name: str, theme: str) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class BlockQuote(TextElement):
    """A block quote."""
    style_name: str
    elements: Incomplete
    def __init__(self) -> None: ...
    def on_child_close(self, context: MarkdownContext, child: MarkdownElement) -> bool: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class HorizontalRule(MarkdownElement):
    """A horizontal rule to divide sections."""
    new_line: bool
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class TableElement(MarkdownElement):
    """MarkdownElement corresponding to `table_open`."""
    header: Incomplete
    body: Incomplete
    def __init__(self) -> None: ...
    def on_child_close(self, context: MarkdownContext, child: MarkdownElement) -> bool: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class TableHeaderElement(MarkdownElement):
    """MarkdownElement corresponding to `thead_open` and `thead_close`."""
    row: Incomplete
    def __init__(self) -> None: ...
    def on_child_close(self, context: MarkdownContext, child: MarkdownElement) -> bool: ...

class TableBodyElement(MarkdownElement):
    """MarkdownElement corresponding to `tbody_open` and `tbody_close`."""
    rows: Incomplete
    def __init__(self) -> None: ...
    def on_child_close(self, context: MarkdownContext, child: MarkdownElement) -> bool: ...

class TableRowElement(MarkdownElement):
    """MarkdownElement corresponding to `tr_open` and `tr_close`."""
    cells: Incomplete
    def __init__(self) -> None: ...
    def on_child_close(self, context: MarkdownContext, child: MarkdownElement) -> bool: ...

class TableDataElement(MarkdownElement):
    """MarkdownElement corresponding to `td_open` and `td_close`
    and `th_open` and `th_close`."""
    @classmethod
    def create(cls, markdown: Markdown, token: Token) -> MarkdownElement: ...
    content: Incomplete
    justify: Incomplete
    def __init__(self, justify: JustifyMethod) -> None: ...
    def on_text(self, context: MarkdownContext, text: TextType) -> None: ...

class ListElement(MarkdownElement):
    """A list element."""
    @classmethod
    def create(cls, markdown: Markdown, token: Token) -> ListElement: ...
    items: Incomplete
    list_type: Incomplete
    list_start: Incomplete
    def __init__(self, list_type: str, list_start: int | None) -> None: ...
    def on_child_close(self, context: MarkdownContext, child: MarkdownElement) -> bool: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class ListItem(TextElement):
    """An item in a list."""
    style_name: str
    elements: Incomplete
    def __init__(self) -> None: ...
    def on_child_close(self, context: MarkdownContext, child: MarkdownElement) -> bool: ...
    def render_bullet(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def render_number(self, console: Console, options: ConsoleOptions, number: int, last_number: int) -> RenderResult: ...

class Link(TextElement):
    @classmethod
    def create(cls, markdown: Markdown, token: Token) -> MarkdownElement: ...
    text: Incomplete
    href: Incomplete
    def __init__(self, text: str, href: str) -> None: ...

class ImageItem(TextElement):
    """Renders a placeholder for an image."""
    new_line: bool
    @classmethod
    def create(cls, markdown: Markdown, token: Token) -> MarkdownElement:
        """Factory to create markdown element,

        Args:
            markdown (Markdown): The parent Markdown object.
            token (Any): A token from markdown-it.

        Returns:
            MarkdownElement: A new markdown element
        """
    destination: Incomplete
    hyperlinks: Incomplete
    link: Incomplete
    def __init__(self, destination: str, hyperlinks: bool) -> None: ...
    text: Incomplete
    def on_enter(self, context: MarkdownContext) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class MarkdownContext:
    """Manages the console render state."""
    console: Incomplete
    options: Incomplete
    style_stack: Incomplete
    stack: Incomplete
    def __init__(self, console: Console, options: ConsoleOptions, style: Style, inline_code_lexer: str | None = None, inline_code_theme: str = 'monokai') -> None: ...
    @property
    def current_style(self) -> Style:
        """Current style which is the product of all styles on the stack."""
    def on_text(self, text: str, node_type: str) -> None:
        """Called when the parser visits text."""
    def enter_style(self, style_name: str | Style) -> Style:
        """Enter a style context."""
    def leave_style(self) -> Style:
        """Leave a style context."""

class Markdown(JupyterMixin):
    '''A Markdown renderable.

    Args:
        markup (str): A string containing markdown.
        code_theme (str, optional): Pygments theme for code blocks. Defaults to "monokai".
        justify (JustifyMethod, optional): Justify value for paragraphs. Defaults to None.
        style (Union[str, Style], optional): Optional style to apply to markdown.
        hyperlinks (bool, optional): Enable hyperlinks. Defaults to ``True``.
        inline_code_lexer: (str, optional): Lexer to use if inline code highlighting is
            enabled. Defaults to None.
        inline_code_theme: (Optional[str], optional): Pygments theme for inline code
            highlighting, or None for no highlighting. Defaults to None.
    '''
    elements: ClassVar[Dict[str, Type[MarkdownElement]]]
    inlines: Incomplete
    markup: Incomplete
    parsed: Incomplete
    code_theme: Incomplete
    justify: Incomplete
    style: Incomplete
    hyperlinks: Incomplete
    inline_code_lexer: Incomplete
    inline_code_theme: Incomplete
    def __init__(self, markup: str, code_theme: str = 'monokai', justify: JustifyMethod | None = None, style: str | Style = 'none', hyperlinks: bool = True, inline_code_lexer: str | None = None, inline_code_theme: str | None = None) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        """Render markdown to the console."""
