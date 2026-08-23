from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['BrainfuckLexer', 'BefungeLexer', 'RedcodeLexer', 'CAmkESLexer', 'CapDLLexer', 'AheuiLexer']

class BrainfuckLexer(RegexLexer):
    """
    Lexer for the esoteric BrainFuck language.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """It's safe to assume that a program which mostly consists of + -
        and < > is brainfuck."""

class BefungeLexer(RegexLexer):
    """
    Lexer for the esoteric Befunge language.

    .. versionadded:: 0.7
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class CAmkESLexer(RegexLexer):
    """
    Basic lexer for the input language for the CAmkES component platform.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class CapDLLexer(RegexLexer):
    """
    Basic lexer for CapDL.

    The source of the primary tool that reads such specifications is available
    at https://github.com/seL4/capdl/tree/master/capDL-tool. Note that this
    lexer only supports a subset of the grammar. For example, identifiers can
    shadow type names, but these instances are currently incorrectly
    highlighted as types. Supporting this would need a stateful lexer that is
    considered unnecessarily complex for now.

    .. versionadded:: 2.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class RedcodeLexer(RegexLexer):
    """
    A simple Redcode lexer based on ICWS'94.
    Contributed by Adam Blinkinsop <blinks@acm.org>.

    .. versionadded:: 0.8
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    opcodes: Incomplete
    modifiers: Incomplete
    tokens: Incomplete

class AheuiLexer(RegexLexer):
    """
    Aheui is esoteric language based on Korean alphabets.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
