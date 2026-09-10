from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['PraatLexer']

class PraatLexer(RegexLexer):
    """
    For Praat scripts.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    keywords: Incomplete
    functions_string: Incomplete
    functions_numeric: Incomplete
    functions_array: Incomplete
    objects: Incomplete
    variables_numeric: Incomplete
    variables_string: Incomplete
    object_attributes: Incomplete
    tokens: Incomplete
