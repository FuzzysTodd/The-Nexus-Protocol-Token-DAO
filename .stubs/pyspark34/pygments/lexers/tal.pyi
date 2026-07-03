from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['TalLexer']

class TalLexer(RegexLexer):
    """
    For `Uxntal <https://wiki.xxiivv.com/site/uxntal.html>`_ source code.

    .. versionadded:: 2.12
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    instructions: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
