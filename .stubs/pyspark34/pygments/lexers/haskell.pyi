from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import Lexer, RegexLexer

__all__ = ['HaskellLexer', 'HspecLexer', 'IdrisLexer', 'AgdaLexer', 'CryptolLexer', 'LiterateHaskellLexer', 'LiterateIdrisLexer', 'LiterateAgdaLexer', 'LiterateCryptolLexer', 'KokaLexer']

class HaskellLexer(RegexLexer):
    """
    A Haskell lexer based on the lexemes defined in the Haskell 98 Report.

    .. versionadded:: 0.8
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    reserved: Incomplete
    ascii: Incomplete
    tokens: Incomplete

class HspecLexer(HaskellLexer):
    """
    A Haskell lexer with support for Hspec constructs.

    .. versionadded:: 2.4.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class IdrisLexer(RegexLexer):
    """
    A lexer for the dependently typed programming language Idris.

    Based on the Haskell and Agda Lexer.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    reserved: Incomplete
    ascii: Incomplete
    directives: Incomplete
    tokens: Incomplete

class AgdaLexer(RegexLexer):
    """
    For the Agda dependently typed functional programming language and
    proof assistant.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    reserved: Incomplete
    tokens: Incomplete

class CryptolLexer(RegexLexer):
    """
    FIXME: A Cryptol2 lexer based on the lexemes defined in the Haskell 98 Report.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    reserved: Incomplete
    ascii: Incomplete
    tokens: Incomplete
    EXTRA_KEYWORDS: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...

class LiterateLexer(Lexer):
    '''
    Base class for lexers of literate file formats based on LaTeX or Bird-style
    (prefixing each code line with ">").

    Additional options accepted:

    `litstyle`
        If given, must be ``"bird"`` or ``"latex"``.  If not given, the style
        is autodetected: if the first non-whitespace character in the source
        is a backslash or percent character, LaTeX is assumed, else Bird.
    '''
    bird_re: Incomplete
    baselexer: Incomplete
    def __init__(self, baselexer, **options) -> None: ...
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, Incomplete, None]: ...

class LiterateHaskellLexer(LiterateLexer):
    '''
    For Literate Haskell (Bird-style or LaTeX) source.

    Additional options accepted:

    `litstyle`
        If given, must be ``"bird"`` or ``"latex"``.  If not given, the style
        is autodetected: if the first non-whitespace character in the source
        is a backslash or percent character, LaTeX is assumed, else Bird.

    .. versionadded:: 0.9
    '''
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class LiterateIdrisLexer(LiterateLexer):
    '''
    For Literate Idris (Bird-style or LaTeX) source.

    Additional options accepted:

    `litstyle`
        If given, must be ``"bird"`` or ``"latex"``.  If not given, the style
        is autodetected: if the first non-whitespace character in the source
        is a backslash or percent character, LaTeX is assumed, else Bird.

    .. versionadded:: 2.0
    '''
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class LiterateAgdaLexer(LiterateLexer):
    '''
    For Literate Agda source.

    Additional options accepted:

    `litstyle`
        If given, must be ``"bird"`` or ``"latex"``.  If not given, the style
        is autodetected: if the first non-whitespace character in the source
        is a backslash or percent character, LaTeX is assumed, else Bird.

    .. versionadded:: 2.0
    '''
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class LiterateCryptolLexer(LiterateLexer):
    '''
    For Literate Cryptol (Bird-style or LaTeX) source.

    Additional options accepted:

    `litstyle`
        If given, must be ``"bird"`` or ``"latex"``.  If not given, the style
        is autodetected: if the first non-whitespace character in the source
        is a backslash or percent character, LaTeX is assumed, else Bird.

    .. versionadded:: 2.0
    '''
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class KokaLexer(RegexLexer):
    """
    Lexer for the Koka language.

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    keywords: Incomplete
    typeStartKeywords: Incomplete
    typekeywords: Incomplete
    builtin: Incomplete
    symbols: str
    sboundary: Incomplete
    boundary: str
    tokenType: Incomplete
    tokenTypeDef: Incomplete
    tokenConstructor: Incomplete
    tokens: Incomplete
