from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['JsonnetLexer']

class JsonnetLexer(RegexLexer):
    """Lexer for Jsonnet source code."""
    name: str
    aliases: Incomplete
    filenames: Incomplete
    url: str
    tokens: Incomplete
