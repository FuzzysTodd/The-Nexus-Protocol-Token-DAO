from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import Lexer, RegexLexer

__all__ = ['MatlabLexer', 'MatlabSessionLexer', 'OctaveLexer', 'ScilabLexer']

class MatlabLexer(RegexLexer):
    """
    For Matlab source code.

    .. versionadded:: 0.10
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class MatlabSessionLexer(Lexer):
    """
    For Matlab sessions.  Modeled after PythonConsoleLexer.
    Contributed by Ken Schutte <kschutte@csail.mit.edu>.

    .. versionadded:: 0.10
    """
    name: str
    aliases: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, Incomplete, None]: ...

class OctaveLexer(RegexLexer):
    """
    For GNU Octave source code.

    .. versionadded:: 1.5
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    builtin_kw: Incomplete
    command_kw: Incomplete
    function_kw: Incomplete
    loadable_kw: Incomplete
    mapping_kw: Incomplete
    builtin_consts: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """Octave is quite hard to spot, and it looks like Matlab as well."""

class ScilabLexer(RegexLexer):
    """
    For Scilab source code.

    .. versionadded:: 1.5
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
