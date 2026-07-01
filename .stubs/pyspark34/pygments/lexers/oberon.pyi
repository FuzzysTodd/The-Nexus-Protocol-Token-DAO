from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['ComponentPascalLexer']

class ComponentPascalLexer(RegexLexer):
    """
    For Component Pascal source code.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """The only other lexer using .cp is the C++ one, so we check if for
        a few common Pascal keywords here. Those are unfortunately quite
        common across various business languages as well."""
