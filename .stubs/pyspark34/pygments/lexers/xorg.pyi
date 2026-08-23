from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['XorgLexer']

class XorgLexer(RegexLexer):
    """Lexer for xorg.conf files."""
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
