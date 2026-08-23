from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['SmartGameFormatLexer']

class SmartGameFormatLexer(RegexLexer):
    """
    Lexer for Smart Game Format (sgf) file format.

    The format is used to store game records of board games for two players
    (mainly Go game).

    .. versionadded:: 2.4
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
