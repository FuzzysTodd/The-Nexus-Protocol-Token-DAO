from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['VerilogLexer', 'SystemVerilogLexer', 'VhdlLexer']

class VerilogLexer(RegexLexer):
    """
    For verilog source code with preprocessor directives.

    .. versionadded:: 1.4
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """Verilog code will use one of reg/wire/assign for sure, and that
        is not common elsewhere."""

class SystemVerilogLexer(RegexLexer):
    """
    Extends verilog lexer to recognise all SystemVerilog keywords from IEEE
    1800-2009 standard.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class VhdlLexer(RegexLexer):
    """
    For VHDL source code.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
