from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['RoboconfGraphLexer', 'RoboconfInstancesLexer']

class RoboconfGraphLexer(RegexLexer):
    """
    Lexer for Roboconf graph files.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete

class RoboconfInstancesLexer(RegexLexer):
    """
    Lexer for Roboconf instances files.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete
