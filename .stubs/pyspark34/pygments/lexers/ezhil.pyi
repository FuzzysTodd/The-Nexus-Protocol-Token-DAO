from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['EzhilLexer']

class EzhilLexer(RegexLexer):
    """
    Lexer for Ezhil, a Tamil script-based programming language.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """This language uses Tamil-script. We'll assume that if there's a
        decent amount of Tamil-characters, it's this language. This assumption
        is obviously horribly off if someone uses string literals in tamil
        in another language."""
    encoding: Incomplete
    def __init__(self, **options) -> None: ...
