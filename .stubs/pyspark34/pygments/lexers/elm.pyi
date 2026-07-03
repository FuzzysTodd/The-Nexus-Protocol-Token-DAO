from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['ElmLexer']

class ElmLexer(RegexLexer):
    """
    For Elm source code.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    validName: str
    specialName: str
    builtinOps: Incomplete
    reservedWords: Incomplete
    tokens: Incomplete
