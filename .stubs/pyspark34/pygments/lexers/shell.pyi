from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import Lexer, RegexLexer

__all__ = ['BashLexer', 'BashSessionLexer', 'TcshLexer', 'BatchLexer', 'SlurmBashLexer', 'MSDOSSessionLexer', 'PowerShellLexer', 'PowerShellSessionLexer', 'TcshSessionLexer', 'FishShellLexer', 'ExeclineLexer']

class BashLexer(RegexLexer):
    """
    Lexer for (ba|k|z|)sh shell scripts.

    .. versionadded:: 0.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class SlurmBashLexer(BashLexer):
    """
    Lexer for (ba|k|z|)sh Slurm scripts.

    .. versionadded:: 2.4
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    EXTRA_KEYWORDS: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...

class ShellSessionBaseLexer(Lexer):
    """
    Base lexer for shell sessions.

    .. versionadded:: 2.1
    """
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...

class BashSessionLexer(ShellSessionBaseLexer):
    """
    Lexer for Bash shell sessions, i.e. command lines, including a
    prompt, interspersed with output.

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete

class BatchLexer(RegexLexer):
    """
    Lexer for the DOS/Windows Batch file format.

    .. versionadded:: 0.7
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class MSDOSSessionLexer(ShellSessionBaseLexer):
    """
    Lexer for MS DOS shell sessions, i.e. command lines, including a
    prompt, interspersed with output.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete

class TcshLexer(RegexLexer):
    """
    Lexer for tcsh scripts.

    .. versionadded:: 0.10
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class TcshSessionLexer(ShellSessionBaseLexer):
    """
    Lexer for Tcsh sessions, i.e. command lines, including a
    prompt, interspersed with output.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete

class PowerShellLexer(RegexLexer):
    """
    For Windows PowerShell code.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    keywords: Incomplete
    operators: Incomplete
    verbs: Incomplete
    aliases_: Incomplete
    commenthelp: Incomplete
    tokens: Incomplete

class PowerShellSessionLexer(ShellSessionBaseLexer):
    """
    Lexer for PowerShell sessions, i.e. command lines, including a
    prompt, interspersed with output.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete

class FishShellLexer(RegexLexer):
    """
    Lexer for Fish shell scripts.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class ExeclineLexer(RegexLexer):
    """
    Lexer for Laurent Bercot's execline language
    (https://skarnet.org/software/execline).

    .. versionadded:: 2.7
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...
