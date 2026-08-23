from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['GraphQLLexer']

class GraphQLLexer(RegexLexer):
    """
    Lexer for GraphQL syntax

    .. versionadded:: 2.16
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    url: str
    tokens: Incomplete
