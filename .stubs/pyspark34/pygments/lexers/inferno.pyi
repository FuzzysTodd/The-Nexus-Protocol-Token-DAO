from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['LimboLexer']

class LimboLexer(RegexLexer):
    """
    Lexer for Limbo programming language

    TODO:
        - maybe implement better var declaration highlighting
        - some simple syntax error highlighting

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
