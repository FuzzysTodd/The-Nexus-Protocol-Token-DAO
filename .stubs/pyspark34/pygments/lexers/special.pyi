from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import Lexer

__all__ = ['TextLexer', 'OutputLexer', 'RawTokenLexer']

class TextLexer(Lexer):
    '''
    "Null" lexer, doesn\'t highlight anything.
    '''
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    priority: float
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...
    def analyse_text(text): ...

class OutputLexer(Lexer):
    """
    Simple lexer that highlights everything as ``Token.Generic.Output``.

    .. versionadded:: 2.10
    """
    name: str
    aliases: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...

class RawTokenLexer(Lexer):
    '''
    Recreate a token stream formatted with the `RawTokenFormatter`.

    Additional options accepted:

    `compress`
        If set to ``"gz"`` or ``"bz2"``, decompress the token stream with
        the given compression algorithm before lexing (default: ``""``).
    '''
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    compress: Incomplete
    def __init__(self, **options) -> None: ...
    def get_tokens(self, text) -> Generator[Incomplete, None, None]: ...
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...
