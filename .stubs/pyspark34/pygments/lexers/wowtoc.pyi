from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['WoWTocLexer']

class WoWTocLexer(RegexLexer):
    """
    Lexer for World of Warcraft TOC files.

    .. versionadded:: 2.14
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
