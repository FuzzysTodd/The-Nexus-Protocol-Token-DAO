from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['SparqlLexer', 'TurtleLexer', 'ShExCLexer']

class SparqlLexer(RegexLexer):
    """
    Lexer for `SPARQL <https://www.w3.org/TR/sparql11-query/>`_ query language.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    PN_CHARS_BASE_GRP: str
    PN_CHARS_U_GRP: Incomplete
    PN_CHARS_GRP: Incomplete
    HEX_GRP: str
    PN_LOCAL_ESC_CHARS_GRP: str
    PN_CHARS_BASE: Incomplete
    PN_CHARS_U: Incomplete
    PN_CHARS: Incomplete
    HEX: Incomplete
    PN_LOCAL_ESC_CHARS: Incomplete
    IRIREF: str
    BLANK_NODE_LABEL: Incomplete
    PN_PREFIX: Incomplete
    VARNAME: Incomplete
    PERCENT: Incomplete
    PN_LOCAL_ESC: Incomplete
    PLX: Incomplete
    PN_LOCAL: Incomplete
    EXPONENT: str
    tokens: Incomplete

class TurtleLexer(RegexLexer):
    """
    Lexer for `Turtle <http://www.w3.org/TR/turtle/>`_ data language.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    PN_CHARS_BASE_GRP: str
    PN_CHARS_U_GRP: Incomplete
    PN_CHARS_GRP: Incomplete
    PN_CHARS: Incomplete
    PN_CHARS_BASE: Incomplete
    PN_PREFIX: Incomplete
    HEX_GRP: str
    HEX: Incomplete
    PERCENT: Incomplete
    PN_LOCAL_ESC_CHARS_GRP: str
    PN_LOCAL_ESC_CHARS: Incomplete
    PN_LOCAL_ESC: Incomplete
    PLX: Incomplete
    PN_LOCAL: Incomplete
    patterns: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class ShExCLexer(RegexLexer):
    """
    Lexer for `ShExC <https://shex.io/shex-semantics/#shexc>`_ shape expressions language syntax.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    PN_CHARS_BASE_GRP: str
    PN_CHARS_U_GRP: Incomplete
    PN_CHARS_GRP: Incomplete
    HEX_GRP: str
    PN_LOCAL_ESC_CHARS_GRP: str
    PN_CHARS_BASE: Incomplete
    PN_CHARS_U: Incomplete
    PN_CHARS: Incomplete
    HEX: Incomplete
    PN_LOCAL_ESC_CHARS: Incomplete
    UCHAR_NO_BACKSLASH: Incomplete
    UCHAR: Incomplete
    IRIREF: Incomplete
    BLANK_NODE_LABEL: Incomplete
    PN_PREFIX: Incomplete
    PERCENT: Incomplete
    PN_LOCAL_ESC: Incomplete
    PLX: Incomplete
    PN_LOCAL: Incomplete
    EXPONENT: str
    tokens: Incomplete
