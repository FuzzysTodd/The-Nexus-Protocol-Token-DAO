from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['PrologLexer', 'LogtalkLexer']

class PrologLexer(RegexLexer):
    """
    Lexer for Prolog files.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class LogtalkLexer(RegexLexer):
    """
    For Logtalk source code.

    .. versionadded:: 0.10
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
