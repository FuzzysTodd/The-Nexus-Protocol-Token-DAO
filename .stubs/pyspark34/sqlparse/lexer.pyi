from _typeshed import Incomplete
from collections.abc import Generator
from sqlparse import keywords as keywords, tokens as tokens
from sqlparse.utils import consume as consume

class Lexer:
    """The Lexer supports configurable syntax.
    To add support for additional keywords, use the `add_keywords` method."""
    @classmethod
    def get_default_instance(cls):
        """Returns the lexer instance used internally
        by the sqlparse core functions."""
    def default_initialization(self) -> None:
        """Initialize the lexer with default dictionaries.
        Useful if you need to revert custom syntax settings."""
    def clear(self) -> None:
        """Clear all syntax configurations.
        Useful if you want to load a reduced set of syntax configurations.
        After this call, regexps and keyword dictionaries need to be loaded
        to make the lexer functional again."""
    def set_SQL_REGEX(self, SQL_REGEX) -> None:
        """Set the list of regex that will parse the SQL."""
    def add_keywords(self, keywords) -> None:
        """Add keyword dictionaries. Keywords are looked up in the same order
        that dictionaries were added."""
    def is_keyword(self, value):
        """Checks for a keyword.

        If the given value is in one of the KEYWORDS_* dictionary
        it's considered a keyword. Otherwise, tokens.Name is returned.
        """
    def get_tokens(self, text, encoding: Incomplete | None = None) -> Generator[Incomplete, None, None]:
        """
        Return an iterable of (tokentype, value) pairs generated from
        `text`. If `unfiltered` is set to `True`, the filtering mechanism
        is bypassed even if filters are defined.

        Also preprocess the text, i.e. expand tabs and strip it if
        wanted and applies registered filters.

        Split ``text`` into (tokentype, text) pairs.

        ``stack`` is the initial stack (default: ``['root']``)
        """

def tokenize(sql, encoding: Incomplete | None = None):
    """Tokenize sql.

    Tokenize *sql* using the :class:`Lexer` and return a 2-tuple stream
    of ``(token type, value)`` items.
    """
