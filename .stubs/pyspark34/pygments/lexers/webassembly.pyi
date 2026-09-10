from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['WatLexer']

class WatLexer(RegexLexer):
    """Lexer for the WebAssembly text format.

    .. versionadded:: 2.9
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
