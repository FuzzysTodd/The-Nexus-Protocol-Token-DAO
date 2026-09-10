from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['StataLexer']

class StataLexer(RegexLexer):
    """
    For Stata do files.

    .. versionadded:: 2.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
