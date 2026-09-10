from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['CddlLexer']

class CddlLexer(RegexLexer):
    """
    Lexer for CDDL definitions.

    .. versionadded:: 2.8
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
