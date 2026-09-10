from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import RegexLexer

__all__ = ['SourcePawnLexer', 'PawnLexer']

class SourcePawnLexer(RegexLexer):
    """
    For SourcePawn source code with preprocessor directives.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    SM_TYPES: Incomplete
    smhighlighting: Incomplete
    def __init__(self, **options) -> None: ...
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...

class PawnLexer(RegexLexer):
    """
    For Pawn source code.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """This is basically C. There is a keyword which doesn't exist in C
        though and is nearly unique to this language."""
