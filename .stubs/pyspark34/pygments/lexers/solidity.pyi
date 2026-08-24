from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['SolidityLexer']

class SolidityLexer(RegexLexer):
    """
    For Solidity source code.

    .. versionadded:: 2.5
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    datatype: str
    tokens: Incomplete
