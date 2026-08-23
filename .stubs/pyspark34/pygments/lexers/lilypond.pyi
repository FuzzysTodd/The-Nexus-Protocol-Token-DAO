from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexers.lisp import SchemeLexer

__all__ = ['LilyPondLexer']

class LilyPondLexer(SchemeLexer):
    """
    Lexer for input to LilyPond, a text-based music typesetter.

    .. important::

       This lexer is meant to be used in conjunction with the ``lilypond`` style.

    .. versionadded:: 2.11
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]:
        """Highlight Scheme variables as LilyPond builtins when applicable."""
    tokens: Incomplete
