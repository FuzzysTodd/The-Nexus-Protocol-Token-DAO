from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['AmbientTalkLexer']

class AmbientTalkLexer(RegexLexer):
    """
    Lexer for AmbientTalk source code.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    builtin: Incomplete
    tokens: Incomplete
