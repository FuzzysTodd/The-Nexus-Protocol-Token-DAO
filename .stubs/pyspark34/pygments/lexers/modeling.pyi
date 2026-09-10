from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['ModelicaLexer', 'BugsLexer', 'JagsLexer', 'StanLexer']

class ModelicaLexer(RegexLexer):
    """
    For Modelica source code.

    .. versionadded:: 1.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class BugsLexer(RegexLexer):
    """
    Pygments Lexer for OpenBugs and WinBugs
    models.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class JagsLexer(RegexLexer):
    """
    Pygments Lexer for JAGS.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class StanLexer(RegexLexer):
    """Pygments Lexer for Stan models.

    The Stan modeling language is specified in the *Stan Modeling Language
    User's Guide and Reference Manual, v2.17.0*,
    `pdf <https://github.com/stan-dev/stan/releases/download/v2.17.0/stan-reference-2.17.0.pdf>`__.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
