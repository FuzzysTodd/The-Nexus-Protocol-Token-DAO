from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['FantomLexer']

class FantomLexer(RegexLexer):
    """
    For Fantom source code.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def s(str): ...
    tokens: Incomplete
