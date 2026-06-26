from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['JSLTLexer']

class JSLTLexer(RegexLexer):
    """
    For JSLT source.

    .. versionadded:: 2.10
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
