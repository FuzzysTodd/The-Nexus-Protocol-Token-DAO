from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['RNCCompactLexer']

class RNCCompactLexer(RegexLexer):
    """
    For RelaxNG-compact syntax.

    .. versionadded:: 2.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
