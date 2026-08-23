from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['AscLexer']

class AscLexer(RegexLexer):
    """
    Lexer for ASCII armored files, containing `-----BEGIN/END ...-----` wrapped
    base64 data.

    .. versionadded:: 2.10
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
