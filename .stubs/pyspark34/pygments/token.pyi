from _typeshed import Incomplete

class _TokenType(tuple):
    parent: Incomplete
    def split(self): ...
    subtypes: Incomplete
    def __init__(self, *args) -> None: ...
    def __contains__(self, val) -> bool: ...
    def __getattr__(self, val): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...

Token: Incomplete
Text: Incomplete
Whitespace: Incomplete
Escape: Incomplete
Error: Incomplete
Other: Incomplete
Keyword: Incomplete
Name: Incomplete
Literal: Incomplete
String: Incomplete
Number: Incomplete
Punctuation: Incomplete
Operator: Incomplete
Comment: Incomplete
Generic: Incomplete

def is_token_subtype(ttype, other):
    """
    Return True if ``ttype`` is a subtype of ``other``.

    exists for backwards compatibility. use ``ttype in other`` now.
    """
def string_to_tokentype(s):
    """
    Convert a string into a token type::

        >>> string_to_token('String.Double')
        Token.Literal.String.Double
        >>> string_to_token('Token.Literal.Number')
        Token.Literal.Number
        >>> string_to_token('')
        Token

    Tokens that are already tokens are returned unchanged:

        >>> string_to_token(String)
        Token.Literal.String
    """

STANDARD_TYPES: Incomplete
