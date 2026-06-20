from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['GcodeLexer']

class GcodeLexer(RegexLexer):
    """
    For gcode source code.

    .. versionadded:: 2.9
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
