from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['AMDGPULexer']

class AMDGPULexer(RegexLexer):
    """
    For AMD GPU assembly.

    .. versionadded:: 2.8
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete
