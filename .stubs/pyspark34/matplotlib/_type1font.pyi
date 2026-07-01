from _typeshed import Incomplete

class _Token:
    """
    A token in a PostScript stream.

    Attributes
    ----------
    pos : int
        Position, i.e. offset from the beginning of the data.
    raw : str
        Raw text of the token.
    kind : str
        Description of the token (for debugging or testing).
    """
    kind: str
    pos: Incomplete
    raw: Incomplete
    def __init__(self, pos, raw) -> None: ...
    def endpos(self):
        """Position one past the end of the token"""
    def is_keyword(self, *names):
        """Is this a name token with one of the names?"""
    def is_slash_name(self):
        """Is this a name token that starts with a slash?"""
    def is_delim(self):
        """Is this a delimiter token?"""
    def is_number(self):
        """Is this a number token?"""
    def value(self): ...

class _NameToken(_Token):
    kind: str
    def is_slash_name(self): ...
    def value(self): ...

class _BooleanToken(_Token):
    kind: str
    def value(self): ...

class _KeywordToken(_Token):
    kind: str
    def is_keyword(self, *names): ...

class _DelimiterToken(_Token):
    kind: str
    def is_delim(self): ...
    def opposite(self): ...

class _WhitespaceToken(_Token):
    kind: str

class _StringToken(_Token):
    kind: str
    def value(self): ...

class _BinaryToken(_Token):
    kind: str
    def value(self): ...

class _NumberToken(_Token):
    kind: str
    def is_number(self): ...
    def value(self): ...

class _BalancedExpression(_Token): ...

class Type1Font:
    """
    A class representing a Type-1 font, for use by backends.

    Attributes
    ----------
    parts : tuple
        A 3-tuple of the cleartext part, the encrypted part, and the finale of
        zeros.

    decrypted : bytes
        The decrypted form of ``parts[1]``.

    prop : dict[str, Any]
        A dictionary of font properties. Noteworthy keys include:

        - FontName: PostScript name of the font
        - Encoding: dict from numeric codes to glyph names
        - FontMatrix: bytes object encoding a matrix
        - UniqueID: optional font identifier, dropped when modifying the font
        - CharStrings: dict from glyph names to byte code
        - Subrs: array of byte code subroutines
        - OtherSubrs: bytes object encoding some PostScript code
    """
    parts: Incomplete
    decrypted: Incomplete
    def __init__(self, input) -> None:
        """
        Initialize a Type-1 font.

        Parameters
        ----------
        input : str or 3-tuple
            Either a pfb file name, or a 3-tuple of already-decoded Type-1
            font `~.Type1Font.parts`.
        """
    def transform(self, effects):
        """
        Return a new font that is slanted and/or extended.

        Parameters
        ----------
        effects : dict
            A dict with optional entries:

            - 'slant' : float, default: 0
                Tangent of the angle that the font is to be slanted to the
                right. Negative values slant to the left.
            - 'extend' : float, default: 1
                Scaling factor for the font width. Values less than 1 condense
                the glyphs.

        Returns
        -------
        `Type1Font`
        """
