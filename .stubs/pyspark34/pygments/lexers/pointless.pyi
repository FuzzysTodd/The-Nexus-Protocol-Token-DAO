from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['PointlessLexer']

class PointlessLexer(RegexLexer):
    """
    For Pointless source code.

    .. versionadded:: 2.7
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    ops: Incomplete
    keywords: Incomplete
    tokens: Incomplete
