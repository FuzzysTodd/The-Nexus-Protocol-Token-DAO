from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['IDLLexer']

class IDLLexer(RegexLexer):
    """
    Pygments Lexer for IDL (Interactive Data Language).

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """endelse seems to be unique to IDL, endswitch is rare at least."""
