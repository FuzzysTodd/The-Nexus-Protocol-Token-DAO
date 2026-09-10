from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import Lexer

__all__ = ['DelphiLexer', 'PortugolLexer']

class PortugolLexer(Lexer):
    """For Portugol, a Pascal dialect with keywords in Portuguese."""
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    url: str
    lexer: Incomplete
    def __init__(self, **options) -> None: ...
    def get_tokens_unprocessed(self, text): ...

class DelphiLexer(Lexer):
    """
    For Delphi (Borland Object Pascal),
    Turbo Pascal and Free Pascal source code.

    Additional options accepted:

    `turbopascal`
        Highlight Turbo Pascal specific keywords (default: ``True``).
    `delphi`
        Highlight Borland Delphi specific keywords (default: ``True``).
    `freepascal`
        Highlight Free Pascal specific keywords (default: ``True``).
    `units`
        A list of units that should be considered builtin, supported are
        ``System``, ``SysUtils``, ``Classes`` and ``Math``.
        Default is to consider all of them builtin.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    TURBO_PASCAL_KEYWORDS: Incomplete
    DELPHI_KEYWORDS: Incomplete
    FREE_PASCAL_KEYWORDS: Incomplete
    BLOCK_KEYWORDS: Incomplete
    FUNCTION_MODIFIERS: Incomplete
    DIRECTIVES: Incomplete
    BUILTIN_TYPES: Incomplete
    BUILTIN_UNITS: Incomplete
    ASM_REGISTERS: Incomplete
    ASM_INSTRUCTIONS: Incomplete
    PORTUGOL_KEYWORDS: Incomplete
    PORTUGOL_BUILTIN_TYPES: Incomplete
    keywords: Incomplete
    builtins: Incomplete
    is_portugol: bool
    def __init__(self, **options) -> None: ...
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...
