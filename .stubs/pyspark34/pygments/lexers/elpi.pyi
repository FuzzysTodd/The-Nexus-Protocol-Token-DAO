from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['ElpiLexer']

class ElpiLexer(RegexLexer):
    """
    Lexer for the Elpi programming language.

    .. versionadded:: 2.11
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    lcase_re: str
    ucase_re: str
    digit_re: str
    schar2_re: str
    schar_re: Incomplete
    idchar_re: Incomplete
    idcharstarns_re: Incomplete
    symbchar_re: Incomplete
    constant_re: Incomplete
    symbol_re: str
    escape_re: Incomplete
    const_sym_re: Incomplete
    tokens: Incomplete
