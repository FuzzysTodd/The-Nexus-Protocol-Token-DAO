from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['TclLexer']

class TclLexer(RegexLexer):
    """
    For Tcl source code.

    .. versionadded:: 0.10
    """
    keyword_cmds_re: Incomplete
    builtin_cmds_re: Incomplete
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
