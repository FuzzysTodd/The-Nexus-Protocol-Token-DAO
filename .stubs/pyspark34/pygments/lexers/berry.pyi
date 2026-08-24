from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['BerryLexer']

class BerryLexer(RegexLexer):
    """
    For `berry <http://github.com/berry-lang/berry>`_ source code.

    .. versionadded:: 2.12.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
