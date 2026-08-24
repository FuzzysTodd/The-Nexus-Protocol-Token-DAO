from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['OocLexer']

class OocLexer(RegexLexer):
    """
    For Ooc source code

    .. versionadded:: 1.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
