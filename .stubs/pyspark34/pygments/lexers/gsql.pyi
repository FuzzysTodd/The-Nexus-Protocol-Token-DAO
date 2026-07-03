from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['GSQLLexer']

class GSQLLexer(RegexLexer):
    """
    For GSQL queries (version 3.x).

    .. versionadded:: 2.10
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete
