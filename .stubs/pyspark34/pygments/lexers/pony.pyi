from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['PonyLexer']

class PonyLexer(RegexLexer):
    """
    For Pony source code.

    .. versionadded:: 2.4
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
