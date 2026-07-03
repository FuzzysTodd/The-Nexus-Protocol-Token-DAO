from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['PhixLexer']

class PhixLexer(RegexLexer):
    """
    Pygments Lexer for Phix files (.exw).
    See http://phix.x10.mx

    .. versionadded:: 2.14.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    preproc: Incomplete
    types: Incomplete
    keywords: Incomplete
    routines: Incomplete
    constants: Incomplete
    tokens: Incomplete
