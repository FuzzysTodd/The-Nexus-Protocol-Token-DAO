from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['FutharkLexer']

class FutharkLexer(RegexLexer):
    """
    A Futhark lexer

    .. versionadded:: 2.8
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    num_types: Incomplete
    other_types: Incomplete
    reserved: Incomplete
    ascii: Incomplete
    num_postfix: Incomplete
    identifier_re: str
    tokens: Incomplete
