from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['YaraLexer']

class YaraLexer(RegexLexer):
    """
    For YARA rules

    .. versionadded:: 2.16
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
