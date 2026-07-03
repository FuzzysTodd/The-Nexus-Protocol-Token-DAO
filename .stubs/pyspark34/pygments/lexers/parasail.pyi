from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['ParaSailLexer']

class ParaSailLexer(RegexLexer):
    """
    For ParaSail source code.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
