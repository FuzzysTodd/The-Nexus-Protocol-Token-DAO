from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import RegexLexer

__all__ = ['CsoundScoreLexer', 'CsoundOrchestraLexer', 'CsoundDocumentLexer']

class CsoundLexer(RegexLexer):
    url: str
    tokens: Incomplete

class CsoundScoreLexer(CsoundLexer):
    """
    For `Csound <https://csound.com>`_ scores.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class CsoundOrchestraLexer(CsoundLexer):
    """
    For `Csound <https://csound.com>`_ orchestras.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    user_defined_opcodes: Incomplete
    def opcode_name_callback(lexer, match) -> Generator[Incomplete, None, None]: ...
    def name_callback(lexer, match) -> Generator[Incomplete, None, None]: ...
    tokens: Incomplete

class CsoundDocumentLexer(RegexLexer):
    """
    For `Csound <https://csound.com>`_ documents.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
