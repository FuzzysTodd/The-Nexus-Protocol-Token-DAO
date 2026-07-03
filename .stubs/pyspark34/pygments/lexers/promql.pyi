from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['PromQLLexer']

class PromQLLexer(RegexLexer):
    """
    For PromQL queries.

    For details about the grammar see:
    https://github.com/prometheus/prometheus/tree/master/promql/parser

    .. versionadded: 2.7
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    base_keywords: Incomplete
    aggregator_keywords: Incomplete
    function_keywords: Incomplete
    tokens: Incomplete
