from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import ExtendedRegexLexer, RegexLexer

__all__ = ['BibTeXLexer', 'BSTLexer']

class BibTeXLexer(ExtendedRegexLexer):
    """
    A lexer for BibTeX bibliography data format.

    .. versionadded:: 2.2
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    ALLOWED_CHARS: str
    IDENTIFIER: Incomplete
    def open_brace_callback(self, match, ctx) -> Generator[Incomplete, None, None]: ...
    def close_brace_callback(self, match, ctx) -> Generator[Incomplete, None, None]: ...
    tokens: Incomplete

class BSTLexer(RegexLexer):
    """
    A lexer for BibTeX bibliography styles.

    .. versionadded:: 2.2
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete
