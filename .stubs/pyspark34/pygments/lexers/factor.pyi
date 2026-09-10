from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['FactorLexer']

class FactorLexer(RegexLexer):
    """
    Lexer for the Factor language.

    .. versionadded:: 1.4
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    builtin_kernel: Incomplete
    builtin_assocs: Incomplete
    builtin_combinators: Incomplete
    builtin_math: Incomplete
    builtin_sequences: Incomplete
    builtin_namespaces: Incomplete
    builtin_arrays: Incomplete
    builtin_io: Incomplete
    builtin_strings: Incomplete
    builtin_vectors: Incomplete
    builtin_continuations: Incomplete
    tokens: Incomplete
