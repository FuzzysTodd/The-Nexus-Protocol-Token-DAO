from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['SaviLexer']

class SaviLexer(RegexLexer):
    """
  For Savi source code.

  .. versionadded: 2.10
  """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
