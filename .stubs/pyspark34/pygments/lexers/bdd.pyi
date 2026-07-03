from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['BddLexer']

class BddLexer(RegexLexer):
    """
    Lexer for BDD(Behavior-driven development), which highlights not only
    keywords, but also comments, punctuations, strings, numbers, and variables.

    .. versionadded:: 2.11
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    step_keywords: str
    tokens: Incomplete
    def analyse_text(self, text) -> None: ...
