from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import DelegatingLexer, RegexLexer

__all__ = ['EmailLexer']

class EmailHeaderLexer(RegexLexer):
    """
    Sub-lexer for raw E-mail. This lexer only process header part of e-mail.

    .. versionadded:: 2.5
    """
    highlight_x: Incomplete
    def __init__(self, **options) -> None: ...
    def get_x_header_tokens(self, match) -> Generator[Incomplete, Incomplete, None]: ...
    tokens: Incomplete

class EmailLexer(DelegatingLexer):
    """
    Lexer for raw E-mail.

    Additional options accepted:

    `highlight-X-header`
        Highlight the fields of ``X-`` user-defined email header. (default:
        ``False``).

    .. versionadded:: 2.5
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
