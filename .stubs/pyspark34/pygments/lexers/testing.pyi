from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['GherkinLexer', 'TAPLexer']

class GherkinLexer(RegexLexer):
    """
    For Gherkin syntax.

    .. versionadded:: 1.2
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    feature_keywords: str
    feature_element_keywords: str
    examples_keywords: str
    step_keywords: str
    tokens: Incomplete
    def analyse_text(self, text) -> None: ...

class TAPLexer(RegexLexer):
    """
    For Test Anything Protocol (TAP) output.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
