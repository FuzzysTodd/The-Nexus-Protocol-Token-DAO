from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import Lexer, RegexLexer

__all__ = ['JavascriptLexer', 'KalLexer', 'LiveScriptLexer', 'DartLexer', 'TypeScriptLexer', 'LassoLexer', 'ObjectiveJLexer', 'CoffeeScriptLexer', 'MaskLexer', 'EarlGreyLexer', 'JuttleLexer', 'NodeConsoleLexer']

class JavascriptLexer(RegexLexer):
    """
    For JavaScript source code.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class TypeScriptLexer(JavascriptLexer):
    """
    For TypeScript source code.

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    priority: float
    tokens: Incomplete

class KalLexer(RegexLexer):
    """
    For Kal source code.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class LiveScriptLexer(RegexLexer):
    """
    For LiveScript source code.

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class DartLexer(RegexLexer):
    """
    For Dart source code.

    .. versionadded:: 1.5
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class LassoLexer(RegexLexer):
    """
    For Lasso source code, covering both Lasso 9
    syntax and LassoScript for Lasso 8.6 and earlier. For Lasso embedded in
    HTML, use the `LassoHtmlLexer`.

    Additional options accepted:

    `builtinshighlighting`
        If given and ``True``, highlight builtin types, traits, methods, and
        members (default: ``True``).
    `requiredelimiters`
        If given and ``True``, only highlight code between delimiters as Lasso
        (default: ``False``).

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    alias_filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    builtinshighlighting: Incomplete
    requiredelimiters: Incomplete
    def __init__(self, **options) -> None: ...
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...
    def analyse_text(text): ...

class ObjectiveJLexer(RegexLexer):
    """
    For Objective-J source code with preprocessor directives.

    .. versionadded:: 1.3
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class CoffeeScriptLexer(RegexLexer):
    """
    For CoffeeScript source code.

    .. versionadded:: 1.3
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class MaskLexer(RegexLexer):
    """
    For Mask markup.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class EarlGreyLexer(RegexLexer):
    """
    For Earl-Grey source code.

    .. versionadded: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class JuttleLexer(RegexLexer):
    """
    For Juttle source code.

    .. versionadded:: 2.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class NodeConsoleLexer(Lexer):
    """
    For parsing within an interactive Node.js REPL, such as:

    .. sourcecode:: nodejsrepl

        > let a = 3
        undefined
        > a
        3
        > let b = '4'
        undefined
        > b
        '4'
        > b == a
        false

    .. versionadded: 2.10
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, Incomplete, None]: ...
