from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import Lexer, RegexLexer

__all__ = ['RConsoleLexer', 'SLexer', 'RdLexer']

class RConsoleLexer(Lexer):
    """
    For R console transcripts or R CMD BATCH output files.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, Incomplete, None]: ...

class SLexer(RegexLexer):
    """
    For S, S-plus, and R source code.

    .. versionadded:: 0.10
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    valid_name: str
    tokens: Incomplete
    def analyse_text(text): ...

class RdLexer(RegexLexer):
    """
    Pygments Lexer for R documentation (Rd) files

    This is a very minimal implementation, highlighting little more
    than the macros. A description of Rd syntax is found in `Writing R
    Extensions <http://cran.r-project.org/doc/manuals/R-exts.html>`_
    and `Parsing Rd files <http://developer.r-project.org/parseRd.pdf>`_.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
