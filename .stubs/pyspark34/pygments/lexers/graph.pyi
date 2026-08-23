from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['CypherLexer']

class CypherLexer(RegexLexer):
    """
    For Cypher Query Language

    For the Cypher version in Neo4j 3.3

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete
