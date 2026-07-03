from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['FoxProLexer']

class FoxProLexer(RegexLexer):
    """Lexer for Microsoft Visual FoxPro language.

    FoxPro syntax allows to shorten all keywords and function names
    to 4 characters.  Shortened forms are not recognized by this lexer.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetype: Incomplete
    flags: Incomplete
    tokens: Incomplete
