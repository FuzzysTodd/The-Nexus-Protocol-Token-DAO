from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['SrcinfoLexer']

class SrcinfoLexer(RegexLexer):
    """Lexer for .SRCINFO files used by Arch Linux Packages.

    .. versionadded:: 2.11
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
