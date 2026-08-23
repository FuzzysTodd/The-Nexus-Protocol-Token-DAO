from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['KLexer', 'QLexer']

class KLexer(RegexLexer):
    """
    For `K <https://code.kx.com/>`_ source code.

    .. versionadded:: 2.12
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class QLexer(KLexer):
    """
    For `Q <https://code.kx.com/>`_ source code.

    .. versionadded:: 2.12
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
