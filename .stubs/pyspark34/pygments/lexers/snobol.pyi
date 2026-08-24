from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['SnobolLexer']

class SnobolLexer(RegexLexer):
    """
    Lexer for the SNOBOL4 programming language.

    Recognizes the common ASCII equivalents of the original SNOBOL4 operators.
    Does not require spaces around binary operators.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
