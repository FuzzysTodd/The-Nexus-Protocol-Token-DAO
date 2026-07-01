from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['FloScriptLexer']

class FloScriptLexer(RegexLexer):
    """
    For FloScript configuration language source code.

    .. versionadded:: 2.4
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    def innerstring_rules(ttype): ...
    tokens: Incomplete
