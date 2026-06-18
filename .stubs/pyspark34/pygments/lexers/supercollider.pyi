from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['SuperColliderLexer']

class SuperColliderLexer(RegexLexer):
    """
    For SuperCollider source code.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """We're searching for a common function and a unique keyword here."""
