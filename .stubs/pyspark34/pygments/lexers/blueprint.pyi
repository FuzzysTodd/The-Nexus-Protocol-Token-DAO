from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['BlueprintLexer']

class BlueprintLexer(RegexLexer):
    """
    For Blueprint UI markup.

    .. versionadded:: 2.16
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    url: str
    flags: Incomplete
    tokens: Incomplete
