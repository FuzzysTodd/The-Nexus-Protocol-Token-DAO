from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['SieveLexer']

class SieveLexer(RegexLexer):
    """
    Lexer for sieve format.

    .. versionadded:: 2.6
    """
    name: str
    filenames: Incomplete
    aliases: Incomplete
    tokens: Incomplete
