from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['VerifpalLexer']

class VerifpalLexer(RegexLexer):
    """
    For Verifpal code.

    .. versionadded:: 2.16
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    url: str
    tokens: Incomplete
