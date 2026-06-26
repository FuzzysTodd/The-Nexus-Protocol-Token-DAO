from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['ForthLexer']

class ForthLexer(RegexLexer):
    """
    Lexer for Forth files.

    .. versionadded:: 2.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """Forth uses : COMMAND ; quite a lot in a single line, so we're trying
        to find that."""
