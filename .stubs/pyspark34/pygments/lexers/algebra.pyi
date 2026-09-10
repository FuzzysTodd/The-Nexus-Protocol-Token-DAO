from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import Lexer, RegexLexer

__all__ = ['GAPLexer', 'GAPConsoleLexer', 'MathematicaLexer', 'MuPADLexer', 'BCLexer']

class GAPLexer(RegexLexer):
    """
    For GAP source code.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class GAPConsoleLexer(Lexer):
    """
    For GAP console sessions. Modeled after JuliaConsoleLexer.

    .. versionadded:: 2.14
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, Incomplete, None]: ...
    def analyse_text(text): ...

class MathematicaLexer(RegexLexer):
    """
    Lexer for Mathematica source code.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    operators: Incomplete
    punctuation: Incomplete
    tokens: Incomplete

class MuPADLexer(RegexLexer):
    """
    A MuPAD lexer.
    Contributed by Christopher Creutzig <christopher@creutzig.de>.

    .. versionadded:: 0.8
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class BCLexer(RegexLexer):
    """
    A BC lexer.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
