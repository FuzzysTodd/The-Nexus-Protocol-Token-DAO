from _typeshed import Incomplete
from pygments.lexer import DelegatingLexer, RegexLexer

__all__ = ['UL4Lexer', 'HTMLUL4Lexer', 'XMLUL4Lexer', 'CSSUL4Lexer', 'JavascriptUL4Lexer', 'PythonUL4Lexer']

class UL4Lexer(RegexLexer):
    """
    Generic lexer for UL4.

    .. versionadded:: 2.12
    """
    flags: Incomplete
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class HTMLUL4Lexer(DelegatingLexer):
    """
    Lexer for UL4 embedded in HTML.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...

class XMLUL4Lexer(DelegatingLexer):
    """
    Lexer for UL4 embedded in XML.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...

class CSSUL4Lexer(DelegatingLexer):
    """
    Lexer for UL4 embedded in CSS.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...

class JavascriptUL4Lexer(DelegatingLexer):
    """
    Lexer for UL4 embedded in Javascript.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...

class PythonUL4Lexer(DelegatingLexer):
    """
    Lexer for UL4 embedded in Python.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def __init__(self, **options) -> None: ...
