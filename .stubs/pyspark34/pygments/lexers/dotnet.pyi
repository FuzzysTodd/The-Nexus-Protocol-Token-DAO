from _typeshed import Incomplete
from pygments.lexer import DelegatingLexer, RegexLexer

__all__ = ['CSharpLexer', 'NemerleLexer', 'BooLexer', 'VbNetLexer', 'CSharpAspxLexer', 'VbNetAspxLexer', 'FSharpLexer', 'XppLexer']

class CSharpLexer(RegexLexer):
    """
    For C# source code.

    Additional options accepted:

    `unicodelevel`
      Determines which Unicode characters this lexer allows for identifiers.
      The possible values are:

      * ``none`` -- only the ASCII letters and numbers are allowed. This
        is the fastest selection.
      * ``basic`` -- all Unicode characters from the specification except
        category ``Lo`` are allowed.
      * ``full`` -- all Unicode characters as specified in the C# specs
        are allowed.  Note that this means a considerable slowdown since the
        ``Lo`` category has more than 40,000 characters in it!

      The default value is ``basic``.

      .. versionadded:: 0.8
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    levels: Incomplete
    tokens: Incomplete
    token_variants: bool
    def __init__(self, **options) -> None: ...

class NemerleLexer(RegexLexer):
    """
    For Nemerle source code.

    Additional options accepted:

    `unicodelevel`
      Determines which Unicode characters this lexer allows for identifiers.
      The possible values are:

      * ``none`` -- only the ASCII letters and numbers are allowed. This
        is the fastest selection.
      * ``basic`` -- all Unicode characters from the specification except
        category ``Lo`` are allowed.
      * ``full`` -- all Unicode characters as specified in the C# specs
        are allowed.  Note that this means a considerable slowdown since the
        ``Lo`` category has more than 40,000 characters in it!

      The default value is ``basic``.

    .. versionadded:: 1.5
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    levels: Incomplete
    tokens: Incomplete
    token_variants: bool
    def __init__(self, **options) -> None: ...
    def analyse_text(text):
        """Nemerle is quite similar to Python, but @if is relatively uncommon
        elsewhere."""

class BooLexer(RegexLexer):
    """
    For Boo source code.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class VbNetLexer(RegexLexer):
    """
    For Visual Basic.NET source code.
    Also LibreOffice Basic, OpenOffice Basic, and StarOffice Basic.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    uni_name: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class GenericAspxLexer(RegexLexer):
    """
    Lexer for ASP.NET pages.
    """
    name: str
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class CSharpAspxLexer(DelegatingLexer):
    """
    Lexer for highlighting C# within ASP.NET pages.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class VbNetAspxLexer(DelegatingLexer):
    """
    Lexer for highlighting Visual Basic.net within ASP.NET pages.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...
    def analyse_text(text): ...

class FSharpLexer(RegexLexer):
    """
    For the F# language (version 3.0).

    .. versionadded:: 1.5
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    keywords: Incomplete
    keyopts: Incomplete
    operators: str
    word_operators: Incomplete
    prefix_syms: str
    infix_syms: str
    primitives: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """F# doesn't have that many unique features -- |> and <| are weak
        indicators."""

class XppLexer(RegexLexer):
    """
    For X++ source code. This is based loosely on the CSharpLexer

    .. versionadded:: 2.15
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    XPP_CHARS: Incomplete
    OPERATORS: Incomplete
    KEYWORDS: Incomplete
    RUNTIME_FUNCTIONS: Incomplete
    COMPILE_FUNCTIONS: Incomplete
    tokens: Incomplete
