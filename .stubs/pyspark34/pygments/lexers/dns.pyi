from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['DnsZoneLexer']

class DnsZoneLexer(RegexLexer):
    """
    Lexer for DNS zone file

    .. versionadded:: 2.16
    """
    flags: Incomplete
    name: str
    aliases: Incomplete
    filenames: Incomplete
    url: str
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
