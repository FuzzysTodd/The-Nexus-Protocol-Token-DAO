from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['IconLexer', 'UcodeLexer', 'UniconLexer']

class UniconLexer(RegexLexer):
    """
    For Unicon source code.

    .. versionadded:: 2.4
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class IconLexer(RegexLexer):
    """
    Lexer for Icon.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class UcodeLexer(RegexLexer):
    """
    Lexer for Icon ucode files.

    .. versionadded:: 2.4
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """endsuspend and endrepeat are unique to this language, and
        \\self, /self doesn't seem to get used anywhere else either."""
