from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['AmplLexer']

class AmplLexer(RegexLexer):
    """
    For AMPL source code.

    .. versionadded:: 2.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
