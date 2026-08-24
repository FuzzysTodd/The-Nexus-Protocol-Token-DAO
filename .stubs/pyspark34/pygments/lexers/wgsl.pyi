from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['WgslLexer']

class WgslLexer(RegexLexer):
    """
    Lexer for the WebGPU Shading Language.

    .. versionadded:: 2.15
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    keyword_decl: Incomplete
    keywords: Incomplete
    keyword_reserved: Incomplete
    predeclared_enums: Incomplete
    predeclared_types: Incomplete
    predeclared_type_generators: Incomplete
    predeclared_type_alias_vectors: Incomplete
    predeclared_type_alias_matrices: Incomplete
    tokens: Incomplete
