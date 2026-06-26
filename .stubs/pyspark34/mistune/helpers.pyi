from .util import escape_url as escape_url
from _typeshed import Incomplete

PREVENT_BACKSLASH: str
PUNCTUATION: Incomplete
LINK_LABEL: str
LINK_BRACKET_START: Incomplete
LINK_BRACKET_RE: Incomplete
LINK_HREF_BLOCK_RE: Incomplete
LINK_HREF_INLINE_RE: Incomplete
LINK_TITLE_RE: Incomplete
PAREN_END_RE: Incomplete
HTML_TAGNAME: str
HTML_ATTRIBUTES: str
BLOCK_TAGS: Incomplete
PRE_TAGS: Incomplete

def unescape_char(text): ...
def parse_link_text(src, pos): ...
def parse_link_label(src, start_pos): ...
def parse_link_href(src, start_pos, block: bool = False): ...
def parse_link_title(src, start_pos, max_pos): ...
def parse_link(src, pos): ...
