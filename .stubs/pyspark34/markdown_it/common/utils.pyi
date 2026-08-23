from .entities import entities as entities
from _typeshed import Incomplete

def charCodeAt(src: str, pos: int) -> int | None:
    """
    Returns the Unicode value of the character at the specified location.

    @param - index The zero-based index of the desired character.
    If there is no character at the specified index, NaN is returned.

    This was added for compatibility with python
    """
def charStrAt(src: str, pos: int) -> str | None:
    """
    Returns the Unicode value of the character at the specified location.

    @param - index The zero-based index of the desired character.
    If there is no character at the specified index, NaN is returned.

    This was added for compatibility with python
    """
def arrayReplaceAt(src: list[_ItemTV], pos: int, newElements: list[_ItemTV]) -> list[_ItemTV]:
    """
    Remove element from array and put another array at those position.
    Useful for some operations with tokens
    """
def isValidEntityCode(c: int) -> bool: ...
def fromCodePoint(c: int) -> str:
    """Convert ordinal to unicode.

    Note, in the original Javascript two string characters were required,
    for codepoints larger than `0xFFFF`.
    But Python 3 can represent any unicode codepoint in one character.
    """

UNESCAPE_ALL_RE: Incomplete
DIGITAL_ENTITY_BASE10_RE: Incomplete
DIGITAL_ENTITY_BASE16_RE: Incomplete

def replaceEntityPattern(match: str, name: str) -> str:
    """Convert HTML entity patterns,
    see https://spec.commonmark.org/0.30/#entity-references
    """
def unescapeAll(string: str) -> str: ...

ESCAPABLE: str
ESCAPE_CHAR: Incomplete

def stripEscape(string: str) -> str:
    """Strip escape \\ characters"""
def escapeHtml(raw: str) -> str:
    '''Replace special characters "&", "<", ">" and \'"\' to HTML-safe sequences.'''

REGEXP_ESCAPE_RE: Incomplete

def escapeRE(string: str) -> str: ...
def isSpace(code: int | None) -> bool:
    """Check if character code is a whitespace."""
def isStrSpace(ch: str | None) -> bool:
    """Check if character is a whitespace."""

MD_WHITESPACE: Incomplete

def isWhiteSpace(code: int) -> bool:
    """Zs (unicode class) || [\\t\\f\\v\\r\\n]"""

UNICODE_PUNCT_RE: Incomplete

def isPunctChar(ch: str) -> bool:
    """Check if character is a punctuation character."""

MD_ASCII_PUNCT: Incomplete

def isMdAsciiPunct(ch: int) -> bool:
    '''Markdown ASCII punctuation characters.

    ::

        !, ", #, $, %, &, \', (, ), *, +, ,, -, ., /, :, ;, <, =, >, ?, @, [, \\, ], ^, _, `, {, |, }, or ~

    See http://spec.commonmark.org/0.15/#ascii-punctuation-character

    Don\'t confuse with unicode punctuation !!! It lacks some chars in ascii range.

    '''
def normalizeReference(string: str) -> str:
    """Helper to unify [reference labels]."""

LINK_OPEN_RE: Incomplete
LINK_CLOSE_RE: Incomplete

def isLinkOpen(string: str) -> bool: ...
def isLinkClose(string: str) -> bool: ...
