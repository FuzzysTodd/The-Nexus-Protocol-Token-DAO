from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['Macaulay2Lexer']

class Macaulay2Lexer(RegexLexer):
    """Lexer for Macaulay2, a software system for research in algebraic geometry."""
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
