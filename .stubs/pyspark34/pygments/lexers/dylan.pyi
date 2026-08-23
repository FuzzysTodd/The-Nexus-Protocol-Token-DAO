from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import Lexer, RegexLexer

__all__ = ['DylanLexer', 'DylanConsoleLexer', 'DylanLidLexer']

class DylanLexer(RegexLexer):
    """
    For the Dylan language.

    .. versionadded:: 0.7
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    builtins: Incomplete
    keywords: Incomplete
    operators: Incomplete
    functions: Incomplete
    valid_name: str
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...
    tokens: Incomplete

class DylanLidLexer(RegexLexer):
    """
    For Dylan LID (Library Interchange Definition) files.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class DylanConsoleLexer(Lexer):
    """
    For Dylan interactive console output.

    This is based on a copy of the RubyConsoleLexer.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, Incomplete, None]: ...
