from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['NimrodLexer']

class NimrodLexer(RegexLexer):
    """
    For Nim source code.

    .. versionadded:: 1.5
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    def underscorize(words): ...
    keywords: Incomplete
    keywordsPseudo: Incomplete
    opWords: Incomplete
    types: Incomplete
    tokens: Incomplete
