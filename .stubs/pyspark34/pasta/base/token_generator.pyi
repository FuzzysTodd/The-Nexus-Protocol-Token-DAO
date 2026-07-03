import tokenize
from _typeshed import Incomplete
from collections.abc import Generator
from pasta.base import fstring_utils as fstring_utils
from typing import NamedTuple

TOKENS = tokenize

class Token(NamedTuple):
    type: Incomplete
    src: Incomplete
    start: Incomplete
    end: Incomplete
    line: Incomplete

FORMATTING_TOKENS: Incomplete

class TokenGenerator:
    """Helper for sequentially parsing Python source code, token by token.

  Holds internal state during parsing, including:
  _tokens: List of tokens in the source code, as parsed by `tokenize` module.
  _parens: Stack of open parenthesis at the current point in parsing.
  _hints: Number of open parentheses, brackets, etc. at the current point.
  _scope_stack: Stack containing tuples of nodes where the last parenthesis that
    was open is related to one of the nodes on the top of the stack.
  _lines: Full lines of the source code.
  _i: Index of the last token that was parsed. Initially -1.
  _loc: (lineno, column_offset) pair of the position in the source that has been
     parsed to. This should be either the start or end of the token at index _i.

  Arguments:
    ignore_error_tokens: If True, will ignore error tokens. Otherwise, an error
      token will cause an exception. This is useful when the source being parsed
      contains invalid syntax, e.g. if it is in an fstring context.
  """
    lines: Incomplete
    def __init__(self, source, ignore_error_token: bool = False) -> None: ...
    def chars_consumed(self): ...
    def loc_begin(self):
        """Get the start column of the current location parsed to."""
    def loc_end(self):
        """Get the end column of the current location parsed to."""
    def peek(self):
        """Get the next token without advancing."""
    def peek_non_whitespace(self):
        """Get the next non-whitespace token without advancing."""
    def peek_conditional(self, condition):
        """Get the next token of the given type without advancing."""
    def next(self, advance: bool = True):
        """Consume the next token and optionally advance the current location."""
    def rewind(self, amount: int = 1) -> None:
        """Rewind the token iterator."""
    def whitespace(self, max_lines: Incomplete | None = None, comment: bool = False):
        """Parses whitespace from the current _loc to the next non-whitespace.

    Arguments:
      max_lines: (optional int) Maximum number of lines to consider as part of
        the whitespace. Valid values are None, 0 and 1.
      comment: (boolean) If True, look for a trailing comment even when not in
        a parenthesized scope.

    Pre-condition:
      `_loc' represents the point before which everything has been parsed and
      after which nothing has been parsed.
    Post-condition:
      `_loc' is exactly at the character that was parsed to.
    """
    def block_whitespace(self, indent_level):
        """Parses whitespace from the current _loc to the end of the block."""
    def dots(self, num_dots):
        """Parse a number of dots.
    
    This is to work around an oddity in python3's tokenizer, which treats three
    `.` tokens next to each other in a FromImport's level as an ellipsis. This
    parses until the expected number of dots have been seen.
    """
    def open_scope(self, node, single_paren: bool = False):
        """Open a parenthesized scope on the given node."""
    def close_scope(self, node, prefix_attr: str = 'prefix', suffix_attr: str = 'suffix', trailing_comma: bool = False, single_paren: bool = False):
        """Close a parenthesized scope on the given node, if one is open."""
    def hint_open(self) -> None:
        """Indicates opening a group of parentheses or brackets."""
    def hint_closed(self) -> None:
        """Indicates closing a group of parentheses or brackets."""
    def scope(self, node, attr: Incomplete | None = None, trailing_comma: bool = False) -> Generator[None, None, None]:
        """Context manager to handle a parenthesized scope."""
    def is_in_scope(self):
        """Return True iff there is a scope open."""
    def str(self):
        """Parse a full string literal from the input."""
    def eat_tokens(self, predicate):
        """Parse input from tokens while a given condition is met."""
    def fstr(self):
        """Parses an fstring, including subexpressions.

    Returns:
      A generator function which, when repeatedly reads a chunk of the fstring
      up until the next subexpression and yields that chunk, plus a new token
      generator to use to parse the subexpression. The subexpressions in the
      original fstring data are replaced by placeholders to make it possible to
      fill them in with new values, if desired.
    """
    def next_name(self):
        """Parse the next name token."""
    def next_of_type(self, token_type):
        """Parse a token of the given type and return it."""
    def takewhile(self, condition, advance: bool = True) -> Generator[Incomplete, None, None]:
        """Parse tokens as long as a condition holds on the next token."""
