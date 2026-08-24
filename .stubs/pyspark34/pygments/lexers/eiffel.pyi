from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['EiffelLexer']

class EiffelLexer(RegexLexer):
    """
    For Eiffel source code.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
