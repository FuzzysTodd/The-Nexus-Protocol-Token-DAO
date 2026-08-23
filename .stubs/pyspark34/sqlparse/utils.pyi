from _typeshed import Incomplete
from collections.abc import Generator

SPLIT_REGEX: Incomplete
LINE_MATCH: Incomplete

def split_unquoted_newlines(stmt):
    """Split a string on all unquoted newlines.

    Unlike str.splitlines(), this will ignore CR/LF/CR+LF if the requisite
    character is inside of a string."""
def remove_quotes(val):
    """Helper that removes surrounding quotes from strings."""
def recurse(*cls):
    """Function decorator to help with recursion

    :param cls: Classes to not recurse over
    :return: function
    """
def imt(token, i: Incomplete | None = None, m: Incomplete | None = None, t: Incomplete | None = None):
    """Helper function to simplify comparisons Instance, Match and TokenType
    :param token:
    :param i: Class or Tuple/List of Classes
    :param m: Tuple of TokenType & Value. Can be list of Tuple for multiple
    :param t: TokenType or Tuple/List of TokenTypes
    :return:  bool
    """
def consume(iterator, n) -> None:
    """Advance the iterator n-steps ahead. If n is none, consume entirely."""
def offset(filter_, n: int = 0) -> Generator[None, None, None]: ...
def indent(filter_, n: int = 1) -> Generator[None, None, None]: ...
