from _typeshed import Incomplete
from pygments.lexer import Lexer

__all__ = ['TNTLexer']

class TNTLexer(Lexer):
    """
    Lexer for Typographic Number Theory, as described in the book
    Gödel, Escher, Bach, by Douglas R. Hofstadter

    .. versionadded:: 2.7
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    cur: Incomplete
    LOGIC: Incomplete
    OPERATORS: Incomplete
    VARIABLES: Incomplete
    PRIMES: Incomplete
    NEGATORS: Incomplete
    QUANTIFIERS: Incomplete
    NUMBERS: Incomplete
    WHITESPACE: Incomplete
    RULES: Incomplete
    LINENOS: Incomplete
    COMMENT: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def whitespace(self, start, text, required: bool = False):
        """Tokenize whitespace."""
    def variable(self, start, text):
        """Tokenize a variable."""
    def term(self, start, text):
        """Tokenize a term."""
    def formula(self, start, text):
        """Tokenize a formula."""
    def rule(self, start, text):
        """Tokenize a rule."""
    def lineno(self, start, text):
        """Tokenize a line referral."""
    def error_till_line_end(self, start, text):
        """Mark everything from ``start`` to the end of the line as Error."""
    def get_tokens_unprocessed(self, text):
        """Returns a list of TNT tokens."""
