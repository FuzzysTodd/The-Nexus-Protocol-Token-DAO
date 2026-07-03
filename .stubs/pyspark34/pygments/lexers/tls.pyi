from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['TlsLexer']

class TlsLexer(RegexLexer):
    """
    The TLS presentation language, described in RFC 8446.

    .. versionadded:: 2.16
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
