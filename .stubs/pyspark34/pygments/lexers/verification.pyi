from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['BoogieLexer', 'SilverLexer']

class BoogieLexer(RegexLexer):
    """
    For Boogie source code.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class SilverLexer(RegexLexer):
    """
    For Silver source code.

    .. versionadded:: 2.2
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
