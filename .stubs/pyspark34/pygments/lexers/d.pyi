from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['DLexer', 'CrocLexer', 'MiniDLexer']

class DLexer(RegexLexer):
    """
    For D source.

    .. versionadded:: 1.2
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class CrocLexer(RegexLexer):
    """
    For Croc source.
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class MiniDLexer(CrocLexer):
    """
    For MiniD source. MiniD is now known as Croc.
    """
    name: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
