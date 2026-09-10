from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['VCTreeStatusLexer', 'PyPyLogLexer']

class VCTreeStatusLexer(RegexLexer):
    '''
    For colorizing output of version control status commands, like "hg
    status" or "svn status".

    .. versionadded:: 2.0
    '''
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class PyPyLogLexer(RegexLexer):
    """
    Lexer for PyPy log files.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
