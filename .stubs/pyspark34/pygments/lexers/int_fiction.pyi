from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import RegexLexer

__all__ = ['Inform6Lexer', 'Inform6TemplateLexer', 'Inform7Lexer', 'Tads3Lexer']

class Inform6Lexer(RegexLexer):
    """
    For Inform 6 source code.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...
    def analyse_text(text):
        """We try to find a keyword which seem relatively common, unfortunately
        there is a decent overlap with Smalltalk keywords otherwise here.."""

class Inform7Lexer(RegexLexer):
    """
    For Inform 7 source code.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete
    token_variants: Incomplete
    def __init__(self, **options) -> None: ...

class Inform6TemplateLexer(Inform7Lexer):
    """
    For Inform 6 template code.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def get_tokens_unprocessed(self, text, stack=('+i6t-root',)): ...

class Tads3Lexer(RegexLexer):
    """
    For TADS 3 source code.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def get_tokens_unprocessed(self, text, **kwargs) -> Generator[Incomplete, None, None]: ...
    def analyse_text(text):
        """This is a rather generic descriptive language without strong
        identifiers. It looks like a 'GameMainDef' has to be present,
        and/or a 'versionInfo' with an 'IFID' field."""
