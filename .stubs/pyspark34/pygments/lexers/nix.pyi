from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['NixLexer']

class NixLexer(RegexLexer):
    """
    For the Nix language.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    keywords: Incomplete
    builtins: Incomplete
    operators: Incomplete
    punctuations: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
