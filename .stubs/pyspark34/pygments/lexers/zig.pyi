from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['ZigLexer']

class ZigLexer(RegexLexer):
    """
    Lexer for the Zig language.

    grammar: https://ziglang.org/documentation/master/#Grammar
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    type_keywords: Incomplete
    storage_keywords: Incomplete
    structure_keywords: Incomplete
    statement_keywords: Incomplete
    conditional_keywords: Incomplete
    repeat_keywords: Incomplete
    other_keywords: Incomplete
    constant_keywords: Incomplete
    tokens: Incomplete
