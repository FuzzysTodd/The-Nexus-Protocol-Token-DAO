from .token import Token as Token
from _typeshed import Incomplete
from collections.abc import Generator, Sequence
from typing import Any, NamedTuple, overload

class _NesterTokens(NamedTuple):
    opening: Token
    closing: Token

class SyntaxTreeNode:
    '''A Markdown syntax tree node.

    A class that can be used to construct a tree representation of a linear
    `markdown-it-py` token stream.

    Each node in the tree represents either:
      - root of the Markdown document
      - a single unnested `Token`
      - a `Token` "_open" and "_close" token pair, and the tokens nested in
          between
    '''
    token: Incomplete
    nester_tokens: Incomplete
    def __init__(self, tokens: Sequence[Token] = (), *, create_root: bool = True) -> None:
        """Initialize a `SyntaxTreeNode` from a token stream.

        If `create_root` is True, create a root node for the document.
        """
    @overload
    def __getitem__(self, item: int) -> _NodeType: ...
    @overload
    def __getitem__(self, item: slice) -> list[_NodeType]: ...
    def to_tokens(self) -> list[Token]:
        """Recover the linear token stream."""
    @property
    def children(self) -> list[_NodeType]: ...
    @children.setter
    def children(self, value: list[_NodeType]) -> None: ...
    @property
    def parent(self) -> _NodeType | None: ...
    @parent.setter
    def parent(self, value: _NodeType | None) -> None: ...
    @property
    def is_root(self) -> bool:
        """Is the node a special root node?"""
    @property
    def is_nested(self) -> bool:
        """Is this node nested?.

        Returns `True` if the node represents a `Token` pair and tokens in the
        sequence between them, where `Token.nesting` of the first `Token` in
        the pair is 1 and nesting of the other `Token` is -1.
        """
    @property
    def siblings(self) -> Sequence[_NodeType]:
        """Get siblings of the node.

        Gets the whole group of siblings, including self.
        """
    @property
    def type(self) -> str:
        '''Get a string type of the represented syntax.

        - "root" for root nodes
        - `Token.type` if the node represents an unnested token
        - `Token.type` of the opening token, with "_open" suffix stripped, if
            the node represents a nester token pair
        '''
    @property
    def next_sibling(self) -> _NodeType | None:
        """Get the next node in the sequence of siblings.

        Returns `None` if this is the last sibling.
        """
    @property
    def previous_sibling(self) -> _NodeType | None:
        """Get the previous node in the sequence of siblings.

        Returns `None` if this is the first sibling.
        """
    def pretty(self, *, indent: int = 2, show_text: bool = False, _current: int = 0) -> str:
        """Create an XML style string of the tree."""
    def walk(self, *, include_self: bool = True) -> Generator[_NodeType, None, None]:
        """Recursively yield all descendant nodes in the tree starting at self.

        The order mimics the order of the underlying linear token
        stream (i.e. depth first).
        """
    @property
    def tag(self) -> str:
        '''html tag name, e.g. "p" '''
    @property
    def attrs(self) -> dict[str, str | int | float]:
        """Html attributes."""
    def attrGet(self, name: str) -> None | str | int | float:
        """Get the value of attribute `name`, or null if it does not exist."""
    @property
    def map(self) -> tuple[int, int] | None:
        """Source map info. Format: `tuple[ line_begin, line_end ]`"""
    @property
    def level(self) -> int:
        """nesting level, the same as `state.level`"""
    @property
    def content(self) -> str:
        """In a case of self-closing tag (code, html, fence, etc.), it
        has contents of this tag."""
    @property
    def markup(self) -> str:
        """'*' or '_' for emphasis, fence string for fence, etc."""
    @property
    def info(self) -> str:
        """fence infostring"""
    @property
    def meta(self) -> dict[Any, Any]:
        """A place for plugins to store an arbitrary data."""
    @property
    def block(self) -> bool:
        """True for block-level tokens, false for inline tokens."""
    @property
    def hidden(self) -> bool:
        """If it's true, ignore this element when rendering.
        Used for tight lists to hide paragraphs."""
