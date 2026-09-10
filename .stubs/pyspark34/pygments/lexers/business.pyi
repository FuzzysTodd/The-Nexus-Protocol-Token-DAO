from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['CobolLexer', 'CobolFreeformatLexer', 'ABAPLexer', 'OpenEdgeLexer', 'GoodDataCLLexer', 'MaqlLexer']

class CobolLexer(RegexLexer):
    """
    Lexer for OpenCOBOL code.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class CobolFreeformatLexer(CobolLexer):
    """
    Lexer for Free format OpenCOBOL code.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class ABAPLexer(RegexLexer):
    """
    Lexer for ABAP, SAP's integrated language.

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class OpenEdgeLexer(RegexLexer):
    """
    Lexer for `OpenEdge ABL (formerly Progress)
    <http://web.progress.com/en/openedge/abl.html>`_ source code.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    types: str
    keywords: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """Try to identify OpenEdge ABL based on a few common constructs."""

class GoodDataCLLexer(RegexLexer):
    """
    Lexer for `GoodData-CL
    <https://github.com/gooddata/GoodData-CL/raw/master/cli/src/main/resources/com/gooddata/processor/COMMANDS.txt>`_
    script files.

    .. versionadded:: 1.4
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class MaqlLexer(RegexLexer):
    """
    Lexer for `GoodData MAQL
    <https://secure.gooddata.com/docs/html/advanced.metric.tutorial.html>`_
    scripts.

    .. versionadded:: 1.4
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
