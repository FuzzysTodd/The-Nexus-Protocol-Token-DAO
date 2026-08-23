from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['FortranLexer', 'FortranFixedLexer']

class FortranLexer(RegexLexer):
    """
    Lexer for FORTRAN 90 code.

    .. versionadded:: 0.10
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class FortranFixedLexer(RegexLexer):
    """
    Lexer for fixed format Fortran.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete
