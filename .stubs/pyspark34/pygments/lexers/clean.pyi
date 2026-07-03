from _typeshed import Incomplete
from pygments.lexer import ExtendedRegexLexer

__all__ = ['CleanLexer']

class CleanLexer(ExtendedRegexLexer):
    """
    Lexer for the general purpose, state-of-the-art, pure and lazy functional
    programming language Clean.

    .. versionadded: 2.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    keywords: Incomplete
    modulewords: Incomplete
    lowerId: str
    upperId: str
    funnyId: str
    scoreUpperId: Incomplete
    scoreLowerId: Incomplete
    moduleId: str
    classId: Incomplete
    tokens: Incomplete
