from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['BareLexer']

class BareLexer(RegexLexer):
    """
    For BARE schema source.

    .. versionadded:: 2.7
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    keywords: Incomplete
    tokens: Incomplete
