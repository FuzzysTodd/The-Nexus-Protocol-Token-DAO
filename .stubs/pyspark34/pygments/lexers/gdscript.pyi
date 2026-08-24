from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['GDScriptLexer']

class GDScriptLexer(RegexLexer):
    """
    For GDScript source code.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def innerstring_rules(ttype): ...
    tokens: Incomplete
    def analyse_text(text): ...
