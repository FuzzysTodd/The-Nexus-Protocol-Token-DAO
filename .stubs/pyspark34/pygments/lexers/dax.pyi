from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['DaxLexer']

class DaxLexer(RegexLexer):
    """
    Lexer for Power BI DAX
    Referenced from: https://github.com/sql-bi/SyntaxHighlighterBrushDax

    .. versionadded:: 2.15
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    url: str
    mimetypes: Incomplete
    tokens: Incomplete
