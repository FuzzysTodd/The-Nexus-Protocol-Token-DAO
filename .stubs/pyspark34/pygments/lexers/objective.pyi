from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import RegexLexer

__all__ = ['ObjectiveCLexer', 'ObjectiveCppLexer', 'LogosLexer', 'SwiftLexer']

class ObjectiveCLexer(Incomplete):
    """
    For Objective-C source code with preprocessor directives.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    priority: float

class ObjectiveCppLexer(Incomplete):
    """
    For Objective-C++ source code with preprocessor directives.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    priority: float

class LogosLexer(ObjectiveCppLexer):
    """
    For Logos + Objective-C source code with preprocessor directives.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    priority: float
    tokens: Incomplete
    def analyse_text(text): ...

class SwiftLexer(RegexLexer):
    """
    For Swift source.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...
