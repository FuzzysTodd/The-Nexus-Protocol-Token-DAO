from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['CapnProtoLexer']

class CapnProtoLexer(RegexLexer):
    """
    For Cap'n Proto source.

    .. versionadded:: 2.2
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    tokens: Incomplete
