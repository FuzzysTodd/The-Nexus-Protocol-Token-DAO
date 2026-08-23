from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['SmalltalkLexer', 'NewspeakLexer']

class SmalltalkLexer(RegexLexer):
    """
    For Smalltalk syntax.
    Contributed by Stefan Matthias Aust.
    Rewritten by Nils Winter.

    .. versionadded:: 0.10
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class NewspeakLexer(RegexLexer):
    """
    For Newspeak syntax.

    .. versionadded:: 1.1
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
