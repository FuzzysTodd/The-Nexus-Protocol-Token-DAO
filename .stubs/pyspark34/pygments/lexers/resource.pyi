from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['ResourceLexer']

class ResourceLexer(RegexLexer):
    """Lexer for `ICU Resource bundles
    <http://userguide.icu-project.org/locale/resources>`_.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
