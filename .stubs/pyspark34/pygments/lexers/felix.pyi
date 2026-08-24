from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['FelixLexer']

class FelixLexer(RegexLexer):
    """
    For Felix source code.

    .. versionadded:: 1.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    preproc: Incomplete
    keywords: Incomplete
    keyword_directives: Incomplete
    keyword_declarations: Incomplete
    keyword_types: Incomplete
    keyword_constants: Incomplete
    operator_words: Incomplete
    name_builtins: Incomplete
    name_pseudo: Incomplete
    decimal_suffixes: str
    tokens: Incomplete
