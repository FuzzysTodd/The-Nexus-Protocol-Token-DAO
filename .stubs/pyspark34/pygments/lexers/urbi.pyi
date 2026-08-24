from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import ExtendedRegexLexer

__all__ = ['UrbiscriptLexer']

class UrbiscriptLexer(ExtendedRegexLexer):
    """
    For UrbiScript source code.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    def blob_callback(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    tokens: Incomplete
    def analyse_text(text):
        """This is fairly similar to C and others, but freezeif and
        waituntil are unique keywords."""
