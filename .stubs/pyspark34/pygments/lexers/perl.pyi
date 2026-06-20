from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import ExtendedRegexLexer, RegexLexer

__all__ = ['PerlLexer', 'Perl6Lexer']

class PerlLexer(RegexLexer):
    """
    For Perl source code.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class Perl6Lexer(ExtendedRegexLexer):
    """
    For Raku (a.k.a. Perl 6) source code.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    PERL6_IDENTIFIER_RANGE: str
    PERL6_KEYWORDS: Incomplete
    PERL6_BUILTINS: Incomplete
    PERL6_BUILTIN_CLASSES: Incomplete
    PERL6_OPERATORS: Incomplete
    PERL6_BRACKETS: Incomplete
    def brackets_callback(token_class): ...
    def opening_brace_callback(lexer, match, context) -> Generator[Incomplete, None, None]: ...
    def closing_brace_callback(lexer, match, context) -> Generator[Incomplete, None, None]: ...
    def embedded_perl6_callback(lexer, match, context) -> Generator[Incomplete, None, None]: ...
    tokens: Incomplete
    def analyse_text(text): ...
    encoding: Incomplete
    def __init__(self, **options) -> None: ...
