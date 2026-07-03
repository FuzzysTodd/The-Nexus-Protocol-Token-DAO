from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['SmaliLexer']

class SmaliLexer(RegexLexer):
    """
    For Smali (Android/Dalvik) assembly
    code.

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
