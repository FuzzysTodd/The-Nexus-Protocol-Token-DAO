from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any, Dict

class BlockState:
    """The state to save block parser's cursor and tokens."""
    src: str
    tokens: Incomplete
    cursor: int
    cursor_max: int
    list_tight: bool
    parent: Incomplete
    env: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def child_state(self, src: str): ...
    def process(self, src: str): ...
    def find_line_end(self): ...
    def get_text(self, end_pos: int): ...
    def last_token(self): ...
    def prepend_token(self, token: Dict[str, Any]):
        """Insert token before the last token."""
    def append_token(self, token: Dict[str, Any]):
        """Add token to the end of token list."""
    def add_paragraph(self, text: str): ...
    def append_paragraph(self): ...
    def depth(self): ...

class InlineState:
    """The state to save inline parser's tokens."""
    env: Incomplete
    src: str
    tokens: Incomplete
    in_image: bool
    in_link: bool
    in_emphasis: bool
    in_strong: bool
    def __init__(self, env: Dict[str, Any]) -> None: ...
    def prepend_token(self, token: Dict[str, Any]):
        """Insert token before the last token."""
    def append_token(self, token: Dict[str, Any]):
        """Add token to the end of token list."""
    def copy(self):
        """Create a copy of current state."""

class Parser:
    sc_flag: Incomplete
    state_cls = BlockState
    SPECIFICATION: Incomplete
    DEFAULT_RULES: Incomplete
    specification: Incomplete
    rules: Incomplete
    def __init__(self) -> None: ...
    def compile_sc(self, rules: Incomplete | None = None): ...
    def register(self, name: str, pattern, func, before: Incomplete | None = None):
        """Register a new rule to parse the token. This method is usually used to
        create a new plugin.

        :param name: name of the new grammar
        :param pattern: regex pattern in string
        :param func: the parsing function
        :param before: insert this rule before a built-in rule
        """
    def register_rule(self, name, pattern, func) -> None: ...
    @staticmethod
    def insert_rule(rules, name, before: Incomplete | None = None) -> None: ...
    def parse_method(self, m, state): ...

class BaseRenderer:
    NAME: str
    def __init__(self) -> None: ...
    def register(self, name: str, method):
        '''Register a render method for the named token. For example::

            def render_wiki(renderer, key, title):
                return f\'<a href="/wiki/{key}">{title}</a>\'

            renderer.register(\'wiki\', render_wiki)
        '''
    def render_token(self, token, state): ...
    def iter_tokens(self, tokens, state) -> Generator[Incomplete, None, None]: ...
    def render_tokens(self, tokens, state): ...
    def __call__(self, tokens, state): ...
