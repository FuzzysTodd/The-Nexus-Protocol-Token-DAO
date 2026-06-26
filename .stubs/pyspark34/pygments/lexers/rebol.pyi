from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import RegexLexer

__all__ = ['RebolLexer', 'RedLexer']

class RebolLexer(RegexLexer):
    """
    A `REBOL <http://www.rebol.com/>`_ lexer.

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    escape_re: str
    def word_callback(lexer, match) -> Generator[Incomplete, None, None]: ...
    tokens: Incomplete
    def analyse_text(text):
        """
        Check if code contains REBOL header and so it probably not R code
        """

class RedLexer(RegexLexer):
    """
    A `Red-language <http://www.red-lang.org/>`_ lexer.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    escape_re: str
    def word_callback(lexer, match) -> Generator[Incomplete, None, None]: ...
    tokens: Incomplete
