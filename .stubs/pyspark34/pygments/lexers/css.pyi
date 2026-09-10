from _typeshed import Incomplete
from pygments.lexer import ExtendedRegexLexer, RegexLexer

__all__ = ['CssLexer', 'SassLexer', 'ScssLexer', 'LessCssLexer']

class CssLexer(RegexLexer):
    """
    For CSS (Cascading Style Sheets).
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class SassLexer(ExtendedRegexLexer):
    """
    For Sass stylesheets.

    .. versionadded:: 1.3
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class ScssLexer(RegexLexer):
    """
    For SCSS stylesheets.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class LessCssLexer(CssLexer):
    """
    For LESS styleshets.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
