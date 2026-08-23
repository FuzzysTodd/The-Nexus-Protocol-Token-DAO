from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['UsdLexer']

class UsdLexer(RegexLexer):
    """
    A lexer that parses Pixar's Universal Scene Description file format.

    .. versionadded:: 2.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
