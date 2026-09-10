from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['KuinLexer']

class KuinLexer(RegexLexer):
    """
    For Kuin source code.

    .. versionadded:: 2.9
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
