from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['MoselLexer']

class MoselLexer(RegexLexer):
    """
    For the Mosel optimization language.

    .. versionadded:: 2.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
