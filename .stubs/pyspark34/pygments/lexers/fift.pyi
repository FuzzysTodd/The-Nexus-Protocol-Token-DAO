from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['FiftLexer']

class FiftLexer(RegexLexer):
    """
    For Fift source code.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    url: str
    tokens: Incomplete
