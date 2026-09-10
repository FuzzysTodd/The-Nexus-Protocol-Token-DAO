from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['IgorLexer']

class IgorLexer(RegexLexer):
    """
    Pygments Lexer for Igor Pro procedure files (.ipf).
    See http://www.wavemetrics.com/ and http://www.igorexchange.com/.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    flowControl: Incomplete
    types: Incomplete
    keywords: Incomplete
    operations: Incomplete
    functions: Incomplete
    tokens: Incomplete
