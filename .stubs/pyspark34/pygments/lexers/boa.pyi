from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['BoaLexer']

class BoaLexer(RegexLexer):
    """
    Lexer for the `Boa <http://boa.cs.iastate.edu/docs/>`_ language.

    .. versionadded:: 2.4
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    reserved: Incomplete
    keywords: Incomplete
    classes: Incomplete
    operators: Incomplete
    string_sep: Incomplete
    built_in_functions: Incomplete
    tokens: Incomplete
