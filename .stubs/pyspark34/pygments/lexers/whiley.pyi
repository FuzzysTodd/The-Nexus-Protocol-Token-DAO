from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['WhileyLexer']

class WhileyLexer(RegexLexer):
    """
    Lexer for the Whiley programming language.

    .. versionadded:: 2.2
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
