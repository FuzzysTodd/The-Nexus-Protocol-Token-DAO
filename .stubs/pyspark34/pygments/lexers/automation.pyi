from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['AutohotkeyLexer', 'AutoItLexer']

class AutohotkeyLexer(RegexLexer):
    """
    For autohotkey source code.

    .. versionadded:: 1.4
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class AutoItLexer(RegexLexer):
    """
    For AutoIt files.

    AutoIt is a freeware BASIC-like scripting language
    designed for automating the Windows GUI and general scripting

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    keywords: Incomplete
    functions: Incomplete
    macros: Incomplete
    tokens: Incomplete
