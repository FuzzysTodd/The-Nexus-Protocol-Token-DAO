from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['TealLexer']

class TealLexer(RegexLexer):
    """
    For the Transaction Execution Approval Language (TEAL)

    For more information about the grammar, see:
    https://github.com/algorand/go-algorand/blob/master/data/transactions/logic/assembler.go

    .. versionadded:: 2.9
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    keywords: Incomplete
    identifier: str
    newline: str
    tokens: Incomplete
