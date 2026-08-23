from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['GoLexer']

class GoLexer(RegexLexer):
    """
    For Go source.

    .. versionadded:: 1.2
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
