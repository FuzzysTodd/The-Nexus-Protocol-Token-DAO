from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import ExtendedRegexLexer

__all__ = ['CrystalLexer']

class CrystalLexer(ExtendedRegexLexer):
    """
    For Crystal source code.

    .. versionadded:: 2.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    def heredoc_callback(self, match, ctx) -> Generator[Incomplete, Incomplete, None]: ...
    def gen_crystalstrings_rules(): ...
    tokens: Incomplete
