from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['MIPSLexer']

class MIPSLexer(RegexLexer):
    """
    A MIPS Assembly Lexer.

    Based on the Emacs major mode by hlissner:
    https://github.com/hlissner/emacs-mips-mode
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    keywords: Incomplete
    pseudoinstructions: Incomplete
    directives: Incomplete
    deprecated: Incomplete
    tokens: Incomplete
