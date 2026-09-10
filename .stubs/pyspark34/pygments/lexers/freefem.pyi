from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexers.c_cpp import CppLexer

__all__ = ['FreeFemLexer']

class FreeFemLexer(CppLexer):
    """
    For FreeFem++ source.

    This is an extension of the CppLexer, as the FreeFem Language is a superset
    of C++.

    .. versionadded:: 2.4
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    operators: Incomplete
    types: Incomplete
    fespaces: Incomplete
    preprocessor: Incomplete
    keywords: Incomplete
    functions: Incomplete
    parameters: Incomplete
    deprecated: Incomplete
    suppress_highlight: Incomplete
    def get_tokens_unprocessed(self, text, stack=('root',)) -> Generator[Incomplete, None, None]: ...
