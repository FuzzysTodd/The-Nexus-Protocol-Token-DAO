from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['RtsLexer']

class RtsLexer(RegexLexer):
    """
    For Riverbed Stingray Traffic Manager

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
