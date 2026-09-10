from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['VCLLexer', 'VCLSnippetLexer']

class VCLLexer(RegexLexer):
    """
    For Varnish Configuration Language (VCL).

    .. versionadded:: 2.2
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def analyse_text(text): ...
    tokens: Incomplete

class VCLSnippetLexer(VCLLexer):
    """
    For Varnish Configuration Language snippets.

    .. versionadded:: 2.2
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    filenames: Incomplete
    def analyse_text(text): ...
    tokens: Incomplete
