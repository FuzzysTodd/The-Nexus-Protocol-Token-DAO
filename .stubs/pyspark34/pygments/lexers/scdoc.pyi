from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['ScdocLexer']

class ScdocLexer(RegexLexer):
    """
    `scdoc` is a simple man page generator for POSIX systems written in C99.

    .. versionadded:: 2.5
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """We checks for bold and underline text with * and _. Also
        every scdoc file must start with a strictly defined first line."""
