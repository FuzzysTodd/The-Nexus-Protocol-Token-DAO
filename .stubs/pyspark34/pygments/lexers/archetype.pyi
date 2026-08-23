from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['OdinLexer', 'CadlLexer', 'AdlLexer']

class AtomsLexer(RegexLexer):
    """
    Lexer for Values used in ADL and ODIN.

    .. versionadded:: 2.1
    """
    tokens: Incomplete

class OdinLexer(AtomsLexer):
    """
    Lexer for ODIN syntax.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class CadlLexer(AtomsLexer):
    """
    Lexer for cADL syntax.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class AdlLexer(AtomsLexer):
    """
    Lexer for ADL syntax.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
