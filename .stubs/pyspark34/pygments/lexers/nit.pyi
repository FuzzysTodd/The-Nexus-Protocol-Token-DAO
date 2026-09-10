from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['NitLexer']

class NitLexer(RegexLexer):
    """
    For nit source.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
