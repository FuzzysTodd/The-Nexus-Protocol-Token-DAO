from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import ExtendedRegexLexer, RegexLexer

__all__ = ['HaxeLexer', 'HxmlLexer']

class HaxeLexer(ExtendedRegexLexer):
    """
    For Haxe source code.

    .. versionadded:: 1.3
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    keyword: str
    typeid: str
    ident: Incomplete
    binop: str
    ident_no_keyword: Incomplete
    flags: Incomplete
    preproc_stack: Incomplete
    def preproc_callback(self, match, ctx) -> Generator[Incomplete, None, None]: ...
    tokens: Incomplete
    def analyse_text(text): ...

class HxmlLexer(RegexLexer):
    """
    Lexer for haXe build files.

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
