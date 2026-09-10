from _typeshed import Incomplete
from mistune import BlockParser, BlockState as BlockState, HTMLRenderer, InlineParser, InlineState as InlineState, Markdown
from nbconvert.filters.strings import add_anchor as add_anchor
from pygments.lexer import Lexer as Lexer
from typing import Any, Callable, Dict, Iterable, Match, Tuple

MISTUNE_V3: bool

class InvalidNotebook(Exception):
    """An invalid notebook model."""

class MathBlockParser(BlockParser):
    """This acts as a pass-through to the MathInlineParser. It is needed in
        order to avoid other block level rules splitting math sections apart.

        It works by matching each multiline math environment as a single paragraph,
        so that other rules don't think each section is its own paragraph. Inline
        is ignored here.
        """
    AXT_HEADING_WITHOUT_LEADING_SPACES: str
    MULTILINE_MATH: Incomplete
    SPECIFICATION: Incomplete
    DEFAULT_RULES: Tuple[str, ...]
    def parse_multiline_math(self, m: Match[str], state: BlockState) -> int:
        """Send mutiline math as a single paragraph to MathInlineParser."""

class MathInlineParser(InlineParser):
    """This interprets the content of LaTeX style math objects.

        In particular this grabs ``$$...$$``, ``\\\\[...\\\\]``, ``\\\\(...\\\\)``, ``$...$``,
        and ``\\begin{foo}...\\end{foo}`` styles for declaring mathematics. It strips
        delimiters from all these varieties, and extracts the type of environment
        in the last case (``foo`` in this example).
        """
    BLOCK_MATH_TEX: Incomplete
    BLOCK_MATH_LATEX: Incomplete
    INLINE_MATH_TEX: Incomplete
    INLINE_MATH_LATEX: Incomplete
    LATEX_ENVIRONMENT: Incomplete
    SPECIFICATION: Incomplete
    DEFAULT_RULES: Tuple[str, ...]
    def parse_block_math_tex(self, m: Match[str], state: InlineState) -> int:
        """Parse older TeX-style display math."""
    def parse_block_math_latex(self, m: Match[str], state: InlineState) -> int:
        """Parse newer LaTeX-style display math."""
    def parse_inline_math_tex(self, m: Match[str], state: InlineState) -> int:
        """Parse older TeX-style inline math."""
    def parse_inline_math_latex(self, m: Match[str], state: InlineState) -> int:
        """Parse newer LaTeX-style inline math."""
    def parse_latex_environment(self, m: Match[str], state: InlineState) -> int:
        """Parse a latex environment."""

class MathBlockParser(BlockParser):
    """This acts as a pass-through to the MathInlineParser. It is needed in
        order to avoid other block level rules splitting math sections apart.
        """
    MULTILINE_MATH: Incomplete
    AXT_HEADING: Incomplete
    RULE_NAMES: Incomplete
    def parse_multiline_math(self, m: Match[str], state: Any) -> Dict[str, str]:
        """Pass token through mutiline math."""

class MathInlineParser(InlineParser):
    """This interprets the content of LaTeX style math objects.

        In particular this grabs ``$$...$$``, ``\\\\[...\\\\]``, ``\\\\(...\\\\)``, ``$...$``,
        and ``\\begin{foo}...\\end{foo}`` styles for declaring mathematics. It strips
        delimiters from all these varieties, and extracts the type of environment
        in the last case (``foo`` in this example).
        """
    BLOCK_MATH_TEX: Incomplete
    BLOCK_MATH_LATEX: Incomplete
    INLINE_MATH_TEX: Incomplete
    INLINE_MATH_LATEX: Incomplete
    LATEX_ENVIRONMENT: Incomplete
    RULE_NAMES: Incomplete
    def parse_block_math_tex(self, m: Match[str], state: Any) -> Tuple[str, str]:
        """Parse block text math."""
    def parse_block_math_latex(self, m: Match[str], state: Any) -> Tuple[str, str]:
        """Parse block latex math ."""
    def parse_inline_math_tex(self, m: Match[str], state: Any) -> Tuple[str, str]:
        """Parse inline tex math."""
    def parse_inline_math_latex(self, m: Match[str], state: Any) -> Tuple[str, str]:
        """Parse inline latex math."""
    def parse_latex_environment(self, m: Match[str], state: Any) -> Tuple[str, str, str]:
        """Parse a latex environment."""

class IPythonRenderer(HTMLRenderer):
    """An ipython html renderer."""
    embed_images: Incomplete
    exclude_anchor_links: Incomplete
    anchor_link_text: Incomplete
    path: Incomplete
    attachments: Incomplete
    def __init__(self, escape: bool = True, allow_harmful_protocols: bool = True, embed_images: bool = False, exclude_anchor_links: bool = False, anchor_link_text: str = '¶', path: str = '', attachments: Dict[str, Dict[str, str]] | None = None) -> None:
        """Initialize the renderer."""
    def block_code(self, code: str, info: str | None = None) -> str:
        """Handle block code."""
    def block_mermaidjs(self, code: str) -> str:
        """Handle mermaid syntax."""
    def block_html(self, html: str) -> str:
        """Handle block html."""
    def inline_html(self, html: str) -> str:
        """Handle inline html."""
    def heading(self, text: str, level: int, **attrs: Dict[str, Any]) -> str:
        """Handle a heading."""
    def escape_html(self, text: str) -> str:
        """Escape html content."""
    def block_math(self, body: str) -> str:
        """Handle block math."""
    def multiline_math(self, text: str) -> str:
        """Handle mulitline math for older mistune versions."""
    def latex_environment(self, name: str, body: str) -> str:
        """Handle a latex environment."""
    def inline_math(self, body: str) -> str:
        """Handle inline math."""
    def image(self, text: str, url: str, title: str | None = None) -> str:
        """Rendering a image with title and text.

        :param text: alt text of the image.
        :param url: source link of the image.
        :param title: title text of the image.

        :note: The parameters `text` and `url` are swapped in older versions
            of mistune.
        """
MarkdownPlugin = Callable[[Markdown], None]

class MarkdownWithMath(Markdown):
    """Markdown text with math enabled."""
    DEFAULT_PLUGINS: Incomplete
    def __init__(self, renderer: HTMLRenderer, block: BlockParser | None = None, inline: InlineParser | None = None, plugins: Iterable[MarkdownPlugin] | None = None) -> None:
        """Initialize the parser."""
    def render(self, source: str) -> str:
        """Render the HTML output for a Markdown source."""

def markdown2html_mistune(source: str) -> str:
    """Convert a markdown string to HTML using mistune"""
