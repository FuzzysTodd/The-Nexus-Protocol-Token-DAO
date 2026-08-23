from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import Lexer, RegexLexer

__all__ = ['MakefileLexer', 'BaseMakefileLexer', 'CMakeLexer']

class MakefileLexer(Lexer):
    """
    Lexer for BSD and GNU make extensions (lenient enough to handle both in
    the same file even).

    *Rewritten in Pygments 0.10.*
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    r_special: Incomplete
    r_comment: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, Incomplete, None]: ...
    def analyse_text(text): ...

class BaseMakefileLexer(RegexLexer):
    """
    Lexer for simple Makefiles (no preprocessing).

    .. versionadded:: 0.10
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class CMakeLexer(RegexLexer):
    """
    Lexer for CMake files.

    .. versionadded:: 1.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
