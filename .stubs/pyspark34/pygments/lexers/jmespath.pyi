from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['JMESPathLexer']

class JMESPathLexer(RegexLexer):
    """
    For JMESPath queries.
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    tokens: Incomplete
