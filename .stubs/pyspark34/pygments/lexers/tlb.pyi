from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['TlbLexer']

class TlbLexer(RegexLexer):
    """
    For TL-b source code.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
