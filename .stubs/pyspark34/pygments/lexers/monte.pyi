from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['MonteLexer']

class MonteLexer(RegexLexer):
    """
    Lexer for the Monte programming language.

    .. versionadded:: 2.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
