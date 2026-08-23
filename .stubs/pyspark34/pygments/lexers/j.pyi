from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['JLexer']

class JLexer(RegexLexer):
    """
    For J source code.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    validName: str
    tokens: Incomplete
