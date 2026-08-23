from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['IoLexer']

class IoLexer(RegexLexer):
    """
    For Io (a small, prototype-based programming language) source.

    .. versionadded:: 0.10
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
