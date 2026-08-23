from _typeshed import Incomplete
from pygments.lexers import PrologLexer

__all__ = ['CplintLexer']

class CplintLexer(PrologLexer):
    """
    Lexer for cplint files, including CP-logic, Logic Programs with Annotated
    Disjunctions, Distributional Clauses syntax, ProbLog, DTProbLog.

    .. versionadded:: 2.12
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
