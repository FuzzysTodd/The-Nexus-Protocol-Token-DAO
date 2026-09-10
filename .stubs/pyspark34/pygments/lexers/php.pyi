from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import Lexer, RegexLexer

__all__ = ['ZephirLexer', 'PsyshConsoleLexer', 'PhpLexer']

class ZephirLexer(RegexLexer):
    """
    For Zephir language source code.

    Zephir is a compiled high level language aimed
    to the creation of C-extensions for PHP.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    zephir_keywords: Incomplete
    zephir_type: Incomplete
    flags: Incomplete
    tokens: Incomplete

class PsyshConsoleLexer(Lexer):
    '''
    For PsySH console output, such as:

    .. sourcecode:: psysh

        >>> $greeting = function($name): string {
        ...     return "Hello, {$name}";
        ... };
        => Closure($name): string {#2371 …3}
        >>> $greeting(\'World\')
        => "Hello, World"

    .. versionadded:: 2.7
    '''
    name: str
    url: str
    aliases: Incomplete
    def __init__(self, **options) -> None: ...
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, Incomplete, None]: ...

class PhpLexer(RegexLexer):
    """
    For PHP source code.
    For PHP embedded in HTML, use the `HtmlPhpLexer`.

    Additional options accepted:

    `startinline`
        If given and ``True`` the lexer starts highlighting with
        php code (i.e.: no starting ``<?php`` required).  The default
        is ``False``.
    `funcnamehighlighting`
        If given and ``True``, highlight builtin function names
        (default: ``True``).
    `disabledmodules`
        If given, must be a list of module names whose function names
        should not be highlighted. By default all modules are highlighted
        except the special ``'unknown'`` module that includes functions
        that are known to php but are undocumented.

        To get a list of allowed modules have a look into the
        `_php_builtins` module:

        .. sourcecode:: pycon

            >>> from pygments.lexers._php_builtins import MODULES
            >>> MODULES.keys()
            ['PHP Options/Info', 'Zip', 'dba', ...]

        In fact the names of those modules match the module names from
        the php documentation.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    funcnamehighlighting: Incomplete
    disabledmodules: Incomplete
    startinline: Incomplete
    def __init__(self, **options) -> None: ...
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...
    def analyse_text(text): ...
