from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import DelegatingLexer, RegexLexer

__all__ = ['PythonLexer', 'PythonConsoleLexer', 'PythonTracebackLexer', 'Python2Lexer', 'Python2TracebackLexer', 'CythonLexer', 'DgLexer', 'NumPyLexer']

class PythonLexer(RegexLexer):
    """
    For Python source code (version 3.x).

    .. versionadded:: 0.10

    .. versionchanged:: 2.5
       This is now the default ``PythonLexer``.  It is still available as the
       alias ``Python3Lexer``.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    uni_name: Incomplete
    def innerstring_rules(ttype): ...
    def fstring_rules(ttype): ...
    tokens: Incomplete
    def analyse_text(text): ...
Python3Lexer = PythonLexer

class Python2Lexer(RegexLexer):
    """
    For Python 2.x source code.

    .. versionchanged:: 2.5
       This class has been renamed from ``PythonLexer``.  ``PythonLexer`` now
       refers to the Python 3 variant.  File name patterns like ``*.py`` have
       been moved to Python 3 as well.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def innerstring_rules(ttype): ...
    tokens: Incomplete
    def analyse_text(text): ...

class _PythonConsoleLexerBase(RegexLexer):
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class PythonConsoleLexer(DelegatingLexer):
    '''
    For Python console output or doctests, such as:

    .. sourcecode:: pycon

        >>> a = \'foo\'
        >>> print(a)
        foo
        >>> 1 / 0
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        ZeroDivisionError: integer division or modulo by zero

    Additional options:

    `python3`
        Use Python 3 lexer for code.  Default is ``True``.

        .. versionadded:: 1.0
        .. versionchanged:: 2.5
           Now defaults to ``True``.
    '''
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class PythonTracebackLexer(RegexLexer):
    """
    For Python 3.x tracebacks, with support for chained exceptions.

    .. versionadded:: 1.0

    .. versionchanged:: 2.5
       This is now the default ``PythonTracebackLexer``.  It is still available
       as the alias ``Python3TracebackLexer``.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
Python3TracebackLexer = PythonTracebackLexer

class Python2TracebackLexer(RegexLexer):
    """
    For Python tracebacks.

    .. versionadded:: 0.7

    .. versionchanged:: 2.5
       This class has been renamed from ``PythonTracebackLexer``.
       ``PythonTracebackLexer`` now refers to the Python 3 variant.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class CythonLexer(RegexLexer):
    """
    For Pyrex and Cython source code.

    .. versionadded:: 1.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class DgLexer(RegexLexer):
    """
    Lexer for dg,
    a functional and object-oriented programming language
    running on the CPython 3 VM.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class NumPyLexer(PythonLexer):
    """
    A Python lexer recognizing Numerical Python builtins.

    .. versionadded:: 0.10
    """
    name: str
    url: str
    aliases: Incomplete
    mimetypes: Incomplete
    filenames: Incomplete
    EXTRA_KEYWORDS: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...
    def analyse_text(text): ...
