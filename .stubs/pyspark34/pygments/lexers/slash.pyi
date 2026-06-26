from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import DelegatingLexer, ExtendedRegexLexer

__all__ = ['SlashLexer']

class SlashLanguageLexer(ExtendedRegexLexer):
    def move_state(new_state): ...
    def right_angle_bracket(lexer, match, ctx) -> Generator[Incomplete, None, None]: ...
    tokens: Incomplete

class SlashLexer(DelegatingLexer):
    """
    Lexer for the Slash programming language.

    .. versionadded:: 2.4
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
