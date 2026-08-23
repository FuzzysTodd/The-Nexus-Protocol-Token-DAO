from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['ECLLexer']

class ECLLexer(RegexLexer):
    """
    Lexer for the declarative big-data ECL language.

    .. versionadded:: 1.5
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """This is very difficult to guess relative to other business languages.
        -> in conjunction with BEGIN/END seems relatively rare though."""
