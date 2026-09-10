from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['QlikLexer']

class QlikLexer(RegexLexer):
    """
    Lexer for qlik code, including .qvs files

    .. versionadded:: 2.12
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete
