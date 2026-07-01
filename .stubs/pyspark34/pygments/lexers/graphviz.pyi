from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['GraphvizLexer']

class GraphvizLexer(RegexLexer):
    """
    For graphviz DOT graph description language.

    .. versionadded:: 2.8
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
