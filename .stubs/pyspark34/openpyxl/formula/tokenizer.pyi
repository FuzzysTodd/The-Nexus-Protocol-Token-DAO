from _typeshed import Incomplete

class TokenizerError(Exception):
    """Base class for all Tokenizer errors."""

class Tokenizer:
    """
    A tokenizer for Excel worksheet formulae.

    Converts a str string representing an Excel formula (in A1 notation)
    into a sequence of `Token` objects.

    `formula`: The str string to tokenize

    Tokenizer defines a method `._parse()` to parse the formula into tokens,
    which can then be accessed through the `.items` attribute.

    """
    SN_RE: Incomplete
    WSPACE_RE: Incomplete
    STRING_REGEXES: Incomplete
    ERROR_CODES: Incomplete
    TOKEN_ENDERS: str
    formula: Incomplete
    items: Incomplete
    token_stack: Incomplete
    offset: int
    token: Incomplete
    def __init__(self, formula) -> None: ...
    def check_scientific_notation(self):
        """
        Consumes a + or - character if part of a number in sci. notation.

        Returns True if the character was consumed and self.offset was
        updated, False otherwise.

        """
    def assert_empty_token(self, can_follow=()) -> None:
        """
        Ensure that there's no token currently being parsed.

        Or if there is a token being parsed, it must end with a character in
        can_follow.

        If there are unconsumed token contents, it means we hit an unexpected
        token transition. In this case, we raise a TokenizerError

        """
    def save_token(self) -> None:
        """If there's a token being parsed, add it to the item list."""
    def render(self):
        """Convert the parsed tokens back to a string."""

class Token:
    '''
    A token in an Excel formula.

    Tokens have three attributes:

    * `value`: The string value parsed that led to this token
    * `type`: A string identifying the type of token
    * `subtype`: A string identifying subtype of the token (optional, and
                 defaults to "")

    '''
    LITERAL: str
    OPERAND: str
    FUNC: str
    ARRAY: str
    PAREN: str
    SEP: str
    OP_PRE: str
    OP_IN: str
    OP_POST: str
    WSPACE: str
    value: Incomplete
    type: Incomplete
    subtype: Incomplete
    def __init__(self, value, type_, subtype: str = '') -> None: ...
    TEXT: str
    NUMBER: str
    LOGICAL: str
    ERROR: str
    RANGE: str
    @classmethod
    def make_operand(cls, value):
        """Create an operand token."""
    OPEN: str
    CLOSE: str
    @classmethod
    def make_subexp(cls, value, func: bool = False):
        """
        Create a subexpression token.

        `value`: The value of the token
        `func`: If True, force the token to be of type FUNC

        """
    def get_closer(self):
        """Return a closing token that matches this token's type."""
    ARG: str
    ROW: str
    @classmethod
    def make_separator(cls, value):
        """Create a separator token"""
