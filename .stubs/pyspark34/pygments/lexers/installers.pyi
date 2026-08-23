from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['NSISLexer', 'RPMSpecLexer', 'SourcesListLexer', 'DebianControlLexer']

class NSISLexer(RegexLexer):
    """
    For NSIS scripts.

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class RPMSpecLexer(RegexLexer):
    """
    For RPM ``.spec`` files.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class SourcesListLexer(RegexLexer):
    """
    Lexer that highlights debian sources.list files.

    .. versionadded:: 0.7
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetype: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class DebianControlLexer(RegexLexer):
    """
    Lexer for Debian ``control`` files and ``apt-cache show <pkg>`` outputs.

    .. versionadded:: 0.9
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
