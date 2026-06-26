from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import RegexLexer

__all__ = ['SMLLexer', 'OcamlLexer', 'OpaLexer', 'ReasonLexer', 'FStarLexer']

class SMLLexer(RegexLexer):
    """
    For the Standard ML language.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    alphanumid_reserved: Incomplete
    symbolicid_reserved: Incomplete
    nonid_reserved: Incomplete
    alphanumid_re: str
    symbolicid_re: str
    def stringy(whatkind): ...
    def long_id_callback(self, match) -> Generator[Incomplete, None, None]: ...
    def end_id_callback(self, match) -> Generator[Incomplete, None, None]: ...
    def id_callback(self, match) -> Generator[Incomplete, None, None]: ...
    tokens: Incomplete

class OcamlLexer(RegexLexer):
    """
    For the OCaml language.

    .. versionadded:: 0.7
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    keywords: Incomplete
    keyopts: Incomplete
    operators: str
    word_operators: Incomplete
    prefix_syms: str
    infix_syms: str
    primitives: Incomplete
    tokens: Incomplete

class OpaLexer(RegexLexer):
    """
    Lexer for the Opa language.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    keywords: Incomplete
    ident_re: str
    op_re: str
    punc_re: str
    tokens: Incomplete

class ReasonLexer(RegexLexer):
    """
    For the ReasonML language.

    .. versionadded:: 2.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    keywords: Incomplete
    keyopts: Incomplete
    operators: str
    word_operators: Incomplete
    prefix_syms: str
    infix_syms: str
    primitives: Incomplete
    tokens: Incomplete

class FStarLexer(RegexLexer):
    """
    For the F* language.
    .. versionadded:: 2.7
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    keywords: Incomplete
    decl_keywords: Incomplete
    assume_keywords: Incomplete
    keyopts: Incomplete
    operators: str
    prefix_syms: str
    infix_syms: str
    primitives: Incomplete
    tokens: Incomplete
