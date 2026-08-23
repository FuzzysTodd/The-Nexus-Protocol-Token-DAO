from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['ChapelLexer']

class ChapelLexer(RegexLexer):
    """
    For Chapel source.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    known_types: Incomplete
    type_modifiers_par: Incomplete
    type_modifiers_mem: Incomplete
    type_modifiers: Incomplete
    declarations: Incomplete
    constants: Incomplete
    other_keywords: Incomplete
    tokens: Incomplete
