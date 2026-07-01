from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import RegexLexer

__all__ = ['SchemeLexer', 'CommonLispLexer', 'HyLexer', 'RacketLexer', 'NewLispLexer', 'EmacsLispLexer', 'ShenLexer', 'CPSALexer', 'XtlangLexer', 'FennelLexer']

class SchemeLexer(RegexLexer):
    """
    A Scheme lexer.

    This parser is checked with pastes from the LISP pastebin
    at http://paste.lisp.org/ to cover as much syntax as possible.

    It supports the full Scheme syntax as defined in R5RS.

    .. versionadded:: 0.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    valid_name: str
    token_end: str
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...
    number_rules: Incomplete
    digit: str
    radix: str
    prefix: Incomplete
    ureal: Incomplete
    decimal: str
    naninf: str
    real: Incomplete
    complex_: Incomplete
    num: Incomplete
    def decimal_cb(self, match) -> Generator[Incomplete, None, None]: ...
    tokens: Incomplete

class CommonLispLexer(RegexLexer):
    """
    A Common Lisp lexer.

    .. versionadded:: 0.9
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    nonmacro: str
    constituent: Incomplete
    terminated: str
    symbol: Incomplete
    builtin_function: Incomplete
    special_forms: Incomplete
    macros: Incomplete
    lambda_list_keywords: Incomplete
    declarations: Incomplete
    builtin_types: Incomplete
    builtin_classes: Incomplete
    def __init__(self, **options) -> None: ...
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...
    tokens: Incomplete

class HyLexer(RegexLexer):
    """
    Lexer for Hy source code.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    special_forms: Incomplete
    declarations: Incomplete
    hy_builtins: Incomplete
    hy_core: Incomplete
    builtins: Incomplete
    valid_name: str
    tokens: Incomplete
    def analyse_text(text): ...

class RacketLexer(RegexLexer):
    """
    Lexer for Racket source code (formerly
    known as PLT Scheme).

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class NewLispLexer(RegexLexer):
    """
    For newLISP source code (version 10.3.0).

    .. versionadded:: 1.5
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    builtins: Incomplete
    valid_name: str
    tokens: Incomplete

class EmacsLispLexer(RegexLexer):
    """
    An ELisp lexer, parsing a stream and outputting the tokens
    needed to highlight elisp code.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    nonmacro: str
    constituent: Incomplete
    terminated: str
    symbol: Incomplete
    macros: Incomplete
    special_forms: Incomplete
    builtin_function: Incomplete
    builtin_function_highlighted: Incomplete
    lambda_list_keywords: Incomplete
    error_keywords: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...
    tokens: Incomplete

class ShenLexer(RegexLexer):
    """
    Lexer for Shen source code.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    DECLARATIONS: Incomplete
    SPECIAL_FORMS: Incomplete
    BUILTINS: Incomplete
    BUILTINS_ANYWHERE: Incomplete
    MAPPINGS: Incomplete
    valid_symbol_chars: str
    valid_name: Incomplete
    symbol_name: Incomplete
    variable: Incomplete
    tokens: Incomplete
    def get_tokens_unprocessed(self, text): ...

class CPSALexer(RegexLexer):
    """
    A CPSA lexer based on the CPSA language as of version 2.2.12

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    valid_name: str
    tokens: Incomplete

class XtlangLexer(RegexLexer):
    """An xtlang lexer for the Extempore programming environment.

    This is a mixture of Scheme and xtlang, really. Keyword lists are
    taken from the Extempore Emacs mode
    (https://github.com/extemporelang/extempore-emacs-mode)

    .. versionadded:: 2.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    common_keywords: Incomplete
    scheme_keywords: Incomplete
    xtlang_bind_keywords: Incomplete
    xtlang_keywords: Incomplete
    common_functions: Incomplete
    scheme_functions: Incomplete
    xtlang_functions: Incomplete
    valid_scheme_name: str
    valid_xtlang_name: str
    valid_xtlang_type: str
    tokens: Incomplete

class FennelLexer(RegexLexer):
    """A lexer for the Fennel programming language.

    Fennel compiles to Lua, so all the Lua builtins are recognized as well
    as the special forms that are particular to the Fennel compiler.

    .. versionadded:: 2.3
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    special_forms: Incomplete
    declarations: Incomplete
    builtins: Incomplete
    valid_name: str
    tokens: Incomplete
