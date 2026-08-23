from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['MaximaLexer']

class MaximaLexer(RegexLexer):
    """
    A Maxima lexer.
    Derived from pygments.lexers.MuPADLexer.

    .. versionadded:: 2.11
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    keywords: Incomplete
    constants: Incomplete
    operators: Incomplete
    operator_words: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
