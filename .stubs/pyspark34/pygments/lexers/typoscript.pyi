from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['TypoScriptLexer', 'TypoScriptCssDataLexer', 'TypoScriptHtmlDataLexer']

class TypoScriptCssDataLexer(RegexLexer):
    """
    Lexer that highlights markers, constants and registers within css blocks.

    .. versionadded:: 2.2
    """
    name: str
    aliases: Incomplete
    tokens: Incomplete

class TypoScriptHtmlDataLexer(RegexLexer):
    """
    Lexer that highlights markers, constants and registers within html tags.

    .. versionadded:: 2.2
    """
    name: str
    aliases: Incomplete
    tokens: Incomplete

class TypoScriptLexer(RegexLexer):
    """
    Lexer for TypoScript code.

    .. versionadded:: 2.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
