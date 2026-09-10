from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['BQNLexer']

class BQNLexer(RegexLexer):
    """
    A simple BQN lexer.

    .. versionadded:: 2.16
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
