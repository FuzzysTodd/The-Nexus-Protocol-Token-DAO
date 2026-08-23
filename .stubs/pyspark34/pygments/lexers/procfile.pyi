from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['ProcfileLexer']

class ProcfileLexer(RegexLexer):
    """
    Lexer for Procfile file format.

    The format is used to run processes on Heroku or is used by Foreman or
    Honcho tools.

    .. versionadded:: 2.10
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
