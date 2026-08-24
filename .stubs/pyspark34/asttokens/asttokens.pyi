import abc
from .line_numbers import LineNumbers as LineNumbers
from .util import AstNode as AstNode, Token as Token, TokenInfo as TokenInfo, annotate_fstring_nodes as annotate_fstring_nodes, generate_tokens as generate_tokens, is_module as is_module, is_non_coding_token as is_non_coding_token, is_stmt as is_stmt, last_stmt as last_stmt, match_token as match_token, patched_generate_tokens as patched_generate_tokens
from _typeshed import Incomplete
from ast import Module
from typing import Any, Iterable, Iterator, List, Tuple

class ASTTextBase(Incomplete, metaclass=abc.ABCMeta):
    def __init__(self, source_text: Any, filename: str) -> None: ...
    @abc.abstractmethod
    def get_text_positions(self, node: AstNode, padded: bool) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """
    Returns two ``(lineno, col_offset)`` tuples for the start and end of the given node.
    If the positions can't be determined, or the nodes don't correspond to any particular text,
    returns ``(1, 0)`` for both.

    ``padded`` corresponds to the ``padded`` argument to ``ast.get_source_segment()``.
    This means that if ``padded`` is True, the start position will be adjusted to include
    leading whitespace if ``node`` is a multiline statement.
    """
    def get_text_range(self, node: AstNode, padded: bool = True) -> Tuple[int, int]:
        """
    Returns the (startpos, endpos) positions in source text corresponding to the given node.
    Returns (0, 0) for nodes (like `Load`) that don't correspond to any particular text.

    See ``get_text_positions()`` for details on the ``padded`` argument.
    """
    def get_text(self, node: AstNode, padded: bool = True) -> str:
        """
    Returns the text corresponding to the given node.
    Returns '' for nodes (like `Load`) that don't correspond to any particular text.

    See ``get_text_positions()`` for details on the ``padded`` argument.
    """

class ASTTokens(ASTTextBase):
    """
  ASTTokens maintains the text of Python code in several forms: as a string, as line numbers, and
  as tokens, and is used to mark and access token and position information.

  ``source_text`` must be a unicode or UTF8-encoded string. If you pass in UTF8 bytes, remember
  that all offsets you'll get are to the unicode text, which is available as the ``.text``
  property.

  If ``parse`` is set, the ``source_text`` will be parsed with ``ast.parse()``, and the resulting
  tree marked with token info and made available as the ``.tree`` property.

  If ``tree`` is given, it will be marked and made available as the ``.tree`` property. In
  addition to the trees produced by the ``ast`` module, ASTTokens will also mark trees produced
  using ``astroid`` library <https://www.astroid.org>.

  If only ``source_text`` is given, you may use ``.mark_tokens(tree)`` to mark the nodes of an AST
  tree created separately.
  """
    def __init__(self, source_text: Any, parse: bool = False, tree: Module | None = None, filename: str = '<unknown>', tokens: Iterable[TokenInfo] = None) -> None: ...
    def mark_tokens(self, root_node: Module) -> None:
        """
    Given the root of the AST or Astroid tree produced from source_text, visits all nodes marking
    them with token and position information by adding ``.first_token`` and
    ``.last_token``attributes. This is done automatically in the constructor when ``parse`` or
    ``tree`` arguments are set, but may be used manually with a separate AST or Astroid tree.
    """
    @property
    def text(self) -> str:
        """The source code passed into the constructor."""
    @property
    def tokens(self) -> List[Token]:
        """The list of tokens corresponding to the source code from the constructor."""
    @property
    def tree(self) -> Module | None:
        """The root of the AST tree passed into the constructor or parsed from the source code."""
    @property
    def filename(self) -> str:
        """The filename that was parsed"""
    def get_token_from_offset(self, offset: int) -> Token:
        """
    Returns the token containing the given character offset (0-based position in source text),
    or the preceeding token if the position is between tokens.
    """
    def get_token(self, lineno: int, col_offset: int) -> Token:
        """
    Returns the token containing the given (lineno, col_offset) position, or the preceeding token
    if the position is between tokens.
    """
    def get_token_from_utf8(self, lineno: int, col_offset: int) -> Token:
        """
    Same as get_token(), but interprets col_offset as a UTF8 offset, which is what `ast` uses.
    """
    def next_token(self, tok: Token, include_extra: bool = False) -> Token:
        """
    Returns the next token after the given one. If include_extra is True, includes non-coding
    tokens from the tokenize module, such as NL and COMMENT.
    """
    def prev_token(self, tok: Token, include_extra: bool = False) -> Token:
        """
    Returns the previous token before the given one. If include_extra is True, includes non-coding
    tokens from the tokenize module, such as NL and COMMENT.
    """
    def find_token(self, start_token: Token, tok_type: int, tok_str: str | None = None, reverse: bool = False) -> Token:
        """
    Looks for the first token, starting at start_token, that matches tok_type and, if given, the
    token string. Searches backwards if reverse is True. Returns ENDMARKER token if not found (you
    can check it with `token.ISEOF(t.type)`).
    """
    def token_range(self, first_token: Token, last_token: Token, include_extra: bool = False) -> Iterator[Token]:
        """
    Yields all tokens in order from first_token through and including last_token. If
    include_extra is True, includes non-coding tokens such as tokenize.NL and .COMMENT.
    """
    def get_tokens(self, node: AstNode, include_extra: bool = False) -> Iterator[Token]:
        """
    Yields all tokens making up the given node. If include_extra is True, includes non-coding
    tokens such as tokenize.NL and .COMMENT.
    """
    def get_text_positions(self, node: AstNode, padded: bool) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """
    Returns two ``(lineno, col_offset)`` tuples for the start and end of the given node.
    If the positions can't be determined, or the nodes don't correspond to any particular text,
    returns ``(1, 0)`` for both.

    ``padded`` corresponds to the ``padded`` argument to ``ast.get_source_segment()``.
    This means that if ``padded`` is True, the start position will be adjusted to include
    leading whitespace if ``node`` is a multiline statement.
    """

class ASTText(ASTTextBase):
    """
  Supports the same ``get_text*`` methods as ``ASTTokens``,
  but uses the AST to determine the text positions instead of tokens.
  This is faster than ``ASTTokens`` as it requires less setup work.

  It also (sometimes) supports nodes inside f-strings, which ``ASTTokens`` doesn't.

  Some node types and/or Python versions are not supported.
  In these cases the ``get_text*`` methods will fall back to using ``ASTTokens``
  which incurs the usual setup cost the first time.
  If you want to avoid this, check ``supports_tokenless(node)`` before calling ``get_text*`` methods.
  """
    def __init__(self, source_text: Any, tree: Module | None = None, filename: str = '<unknown>') -> None: ...
    @property
    def tree(self) -> Module: ...
    @property
    def asttokens(self) -> ASTTokens: ...
    def get_text_positions(self, node: AstNode, padded: bool) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """
    Returns two ``(lineno, col_offset)`` tuples for the start and end of the given node.
    If the positions can't be determined, or the nodes don't correspond to any particular text,
    returns ``(1, 0)`` for both.

    ``padded`` corresponds to the ``padded`` argument to ``ast.get_source_segment()``.
    This means that if ``padded`` is True, the start position will be adjusted to include
    leading whitespace if ``node`` is a multiline statement.
    """

def supports_tokenless(node: Any = None) -> bool:
    """
  Returns True if the Python version and the node (if given) are supported by
  the ``get_text*`` methods of ``ASTText`` without falling back to ``ASTTokens``.
  See ``ASTText`` for why this matters.

  The following cases are not supported:

    - Python 3.7 and earlier
    - PyPy
    - ``ast.arguments`` / ``astroid.Arguments``
    - ``ast.withitem``
    - ``astroid.Comprehension``
    - ``astroid.AssignName`` inside ``astroid.Arguments`` or ``astroid.ExceptHandler``
    - The following nodes in Python 3.8 only:
      - ``ast.arg``
      - ``ast.Starred``
      - ``ast.Slice``
      - ``ast.ExtSlice``
      - ``ast.Index``
      - ``ast.keyword``
  """
