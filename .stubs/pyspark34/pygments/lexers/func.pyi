from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['FuncLexer']

class FuncLexer(RegexLexer):
    """
    For FunC source code.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    identifier: str
    tokens: Incomplete
