from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['TeraTermLexer']

class TeraTermLexer(RegexLexer):
    """
    For Tera Term macro source code.

    .. versionadded:: 2.4
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
