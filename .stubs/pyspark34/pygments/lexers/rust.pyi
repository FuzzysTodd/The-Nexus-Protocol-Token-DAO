from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['RustLexer']

class RustLexer(RegexLexer):
    """
    Lexer for the Rust programming language (version 1.47).

    .. versionadded:: 1.6
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    keyword_types: Incomplete
    builtin_funcs_types: Incomplete
    builtin_macros: Incomplete
    tokens: Incomplete
