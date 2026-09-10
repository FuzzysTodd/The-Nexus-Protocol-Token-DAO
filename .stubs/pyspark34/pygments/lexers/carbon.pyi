from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['CarbonLexer']

class CarbonLexer(RegexLexer):
    """
    For Carbon source.

    .. versionadded:: 2.15
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
