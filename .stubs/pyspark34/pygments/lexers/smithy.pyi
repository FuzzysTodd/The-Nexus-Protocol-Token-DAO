from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['SmithyLexer']

class SmithyLexer(RegexLexer):
    """
    For Smithy IDL

    .. versionadded:: 2.10
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    unquoted: str
    identifier: str
    simple_shapes: Incomplete
    aggregate_shapes: Incomplete
    tokens: Incomplete
