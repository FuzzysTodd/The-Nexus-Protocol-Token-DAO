from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['OpenScadLexer']

class OpenScadLexer(RegexLexer):
    """For openSCAD code.

    .. versionadded:: 2.16
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
