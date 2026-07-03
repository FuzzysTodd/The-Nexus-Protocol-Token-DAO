from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['RitaLexer']

class RitaLexer(RegexLexer):
    """
    Lexer for RITA.

    .. versionadded:: 2.11
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
