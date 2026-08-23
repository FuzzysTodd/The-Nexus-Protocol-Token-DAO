from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['WebIDLLexer']

class WebIDLLexer(RegexLexer):
    """
    For Web IDL.

    .. versionadded:: 2.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
