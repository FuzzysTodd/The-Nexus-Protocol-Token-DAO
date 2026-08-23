from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['DevicetreeLexer']

class DevicetreeLexer(RegexLexer):
    """
    Lexer for Devicetree files.

    .. versionadded:: 2.7
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
