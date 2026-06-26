from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['WrenLexer']

class WrenLexer(RegexLexer):
    """
    For Wren source code, version 0.4.0.

    .. versionadded:: 2.14.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete
