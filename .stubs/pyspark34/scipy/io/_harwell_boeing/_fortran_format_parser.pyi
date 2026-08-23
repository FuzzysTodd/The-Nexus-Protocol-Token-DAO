from _typeshed import Incomplete

__all__ = ['BadFortranFormat', 'FortranFormatParser', 'IntFormat', 'ExpFormat']

class BadFortranFormat(SyntaxError): ...

class IntFormat:
    @classmethod
    def from_number(cls, n, min: Incomplete | None = None):
        '''Given an integer, returns a "reasonable" IntFormat instance to represent
        any number between 0 and n if n > 0, -n and n if n < 0

        Parameters
        ----------
        n : int
            max number one wants to be able to represent
        min : int
            minimum number of characters to use for the format

        Returns
        -------
        res : IntFormat
            IntFormat instance with reasonable (see Notes) computed width

        Notes
        -----
        Reasonable should be understood as the minimal string length necessary
        without losing precision. For example, IntFormat.from_number(1) will
        return an IntFormat instance of width 2, so that any 0 and 1 may be
        represented as 1-character strings without loss of information.
        '''
    width: Incomplete
    repeat: Incomplete
    min: Incomplete
    def __init__(self, width, min: Incomplete | None = None, repeat: Incomplete | None = None) -> None: ...
    @property
    def fortran_format(self): ...
    @property
    def python_format(self): ...

class ExpFormat:
    @classmethod
    def from_number(cls, n, min: Incomplete | None = None):
        '''Given a float number, returns a "reasonable" ExpFormat instance to
        represent any number between -n and n.

        Parameters
        ----------
        n : float
            max number one wants to be able to represent
        min : int
            minimum number of characters to use for the format

        Returns
        -------
        res : ExpFormat
            ExpFormat instance with reasonable (see Notes) computed width

        Notes
        -----
        Reasonable should be understood as the minimal string length necessary
        to avoid losing precision.
        '''
    width: Incomplete
    significand: Incomplete
    repeat: Incomplete
    min: Incomplete
    def __init__(self, width, significand, min: Incomplete | None = None, repeat: Incomplete | None = None) -> None:
        """        Parameters
        ----------
        width : int
            number of characters taken by the string (includes space).
        """
    @property
    def fortran_format(self): ...
    @property
    def python_format(self): ...

class Token:
    type: Incomplete
    value: Incomplete
    pos: Incomplete
    def __init__(self, type, value, pos) -> None: ...

class Tokenizer:
    tokens: Incomplete
    res: Incomplete
    def __init__(self) -> None: ...
    data: Incomplete
    curpos: int
    len: Incomplete
    def input(self, s) -> None: ...
    def next_token(self): ...

class FortranFormatParser:
    """Parser for Fortran format strings. The parse method returns a *Format
    instance.

    Notes
    -----
    Only ExpFormat (exponential format for floating values) and IntFormat
    (integer format) for now.
    """
    tokenizer: Incomplete
    def __init__(self) -> None: ...
    def parse(self, s): ...
