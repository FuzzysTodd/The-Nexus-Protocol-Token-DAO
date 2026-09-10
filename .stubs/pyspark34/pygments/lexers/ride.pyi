from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['RideLexer']

class RideLexer(RegexLexer):
    """
    For `Ride <https://docs.wavesplatform.com/en/ride/about-ride.html>`_
    source code.

    .. versionadded:: 2.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    validName: str
    builtinOps: Incomplete
    globalVariablesName: Incomplete
    typesName: Incomplete
    functionsName: Incomplete
    reservedWords: Incomplete
    tokens: Incomplete
