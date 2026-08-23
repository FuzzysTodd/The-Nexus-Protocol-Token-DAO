from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['SASLexer']

class SASLexer(RegexLexer):
    """
    For SAS files.

    .. versionadded:: 2.2
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    builtins_macros: Incomplete
    builtins_conditionals: Incomplete
    builtins_statements: Incomplete
    builtins_sql: Incomplete
    builtins_functions: Incomplete
    tokens: Incomplete
