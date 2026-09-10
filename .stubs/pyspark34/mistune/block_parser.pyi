from .core import BlockState as BlockState, Parser as Parser
from .helpers import BLOCK_TAGS as BLOCK_TAGS, HTML_ATTRIBUTES as HTML_ATTRIBUTES, HTML_TAGNAME as HTML_TAGNAME, LINK_LABEL as LINK_LABEL, PRE_TAGS as PRE_TAGS, parse_link_href as parse_link_href, parse_link_title as parse_link_title, unescape_char as unescape_char
from .list_parser import LIST_PATTERN as LIST_PATTERN, parse_list as parse_list
from .util import escape_url as escape_url, expand_leading_tab as expand_leading_tab, expand_tab as expand_tab, unikey as unikey
from _typeshed import Incomplete
from typing import List, Match, Tuple

class BlockParser(Parser):
    BLANK_LINE: Incomplete
    RAW_HTML: Incomplete
    BLOCK_HTML: Incomplete
    SPECIFICATION: Incomplete
    DEFAULT_RULES: Incomplete
    block_quote_rules: Incomplete
    list_rules: Incomplete
    max_nested_level: Incomplete
    def __init__(self, block_quote_rules: List[str] | None = None, list_rules: List[str] | None = None, max_nested_level: int = 6) -> None: ...
    def parse_blank_line(self, m: Match, state: BlockState) -> int:
        """Parse token for blank lines."""
    def parse_thematic_break(self, m: Match, state: BlockState) -> int:
        """Parse token for thematic break, e.g. ``<hr>`` tag in HTML."""
    def parse_indent_code(self, m: Match, state: BlockState) -> int:
        """Parse token for code block which is indented by 4 spaces."""
    def parse_fenced_code(self, m: Match, state: BlockState) -> int | None:
        """Parse token for fenced code block. A fenced code block is started with
        3 or more backtick(`) or tilde(~).

        An example of a fenced code block:

        .. code-block:: markdown

            ```python
            def markdown(text):
                return mistune.html(text)
            ```
        """
    def parse_axt_heading(self, m: Match, state: BlockState) -> int:
        """Parse token for AXT heading. An AXT heading is started with 1 to 6
        symbol of ``#``."""
    def parse_setex_heading(self, m: Match, state: BlockState) -> int | None:
        """Parse token for setex style heading. A setex heading syntax looks like:

        .. code-block:: markdown

            H1 title
            ========
        """
    def parse_ref_link(self, m: Match, state: BlockState) -> int | None:
        '''Parse link references and save the link information into ``state.env``.

        Here is an example of a link reference:

        .. code-block:: markdown

            a [link][example]

            [example]: https://example.com "Optional title"

        This method will save the link reference into ``state.env`` as::

            state.env[\'ref_links\'][\'example\'] = {
                \'url\': \'https://example.com\',
                \'title\': "Optional title",
            }
        '''
    def extract_block_quote(self, m: Match, state: BlockState) -> Tuple[str, int]:
        """Extract text and cursor end position of a block quote."""
    def parse_block_quote(self, m: Match, state: BlockState) -> int:
        """Parse token for block quote. Here is an example of the syntax:

        .. code-block:: markdown

            > a block quote starts
            > with right arrows
        """
    def parse_list(self, m: Match, state: BlockState) -> int:
        """Parse tokens for ordered and unordered list."""
    def parse_block_html(self, m: Match, state: BlockState) -> int | None: ...
    def parse_raw_html(self, m: Match, state: BlockState) -> int | None: ...
    def parse(self, state: BlockState, rules: List[str] | None = None) -> None: ...
