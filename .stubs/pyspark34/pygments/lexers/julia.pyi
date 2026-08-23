from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import Lexer, RegexLexer

__all__ = ['JuliaLexer', 'JuliaConsoleLexer']

class JuliaLexer(RegexLexer):
    """
    For Julia source code.

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class JuliaConsoleLexer(Lexer):
    """
    For Julia console sessions. Modeled after MatlabSessionLexer.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, Incomplete, None]: ...
