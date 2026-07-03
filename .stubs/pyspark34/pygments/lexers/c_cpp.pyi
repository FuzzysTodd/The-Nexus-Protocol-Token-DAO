from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import RegexLexer

__all__ = ['CLexer', 'CppLexer']

class CFamilyLexer(RegexLexer):
    """
    For C family source code.  This is used as a base class to avoid repetitious
    definitions.
    """
    tokens: Incomplete
    stdlib_types: Incomplete
    c99_types: Incomplete
    linux_types: Incomplete
    c11_atomic_types: Incomplete
    stdlibhighlighting: Incomplete
    c99highlighting: Incomplete
    c11highlighting: Incomplete
    platformhighlighting: Incomplete
    def __init__(self, **options) -> None: ...
    def get_tokens_unprocessed(self, text, stack=('root',)) -> Generator[Incomplete, None, None]: ...

class CLexer(CFamilyLexer):
    """
    For C source code with preprocessor directives.

    Additional options accepted:

    `stdlibhighlighting`
        Highlight common types found in the C/C++ standard library (e.g. `size_t`).
        (default: ``True``).

    `c99highlighting`
        Highlight common types found in the C99 standard library (e.g. `int8_t`).
        Actually, this includes all fixed-width integer types.
        (default: ``True``).

    `c11highlighting`
        Highlight atomic types found in the C11 standard library (e.g. `atomic_bool`).
        (default: ``True``).

    `platformhighlighting`
        Highlight common types found in the platform SDK headers (e.g. `clockid_t` on Linux).
        (default: ``True``).
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    priority: float
    tokens: Incomplete
    def analyse_text(text): ...

class CppLexer(CFamilyLexer):
    """
    For C++ source code with preprocessor directives.

    Additional options accepted:

    `stdlibhighlighting`
        Highlight common types found in the C/C++ standard library (e.g. `size_t`).
        (default: ``True``).

    `c99highlighting`
        Highlight common types found in the C99 standard library (e.g. `int8_t`).
        Actually, this includes all fixed-width integer types.
        (default: ``True``).

    `c11highlighting`
        Highlight atomic types found in the C11 standard library (e.g. `atomic_bool`).
        (default: ``True``).

    `platformhighlighting`
        Highlight common types found in the platform SDK headers (e.g. `clockid_t` on Linux).
        (default: ``True``).
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    priority: float
    tokens: Incomplete
    def analyse_text(text): ...
