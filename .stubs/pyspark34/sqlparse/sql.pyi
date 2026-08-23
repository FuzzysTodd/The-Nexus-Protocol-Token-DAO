from _typeshed import Incomplete
from collections.abc import Generator
from sqlparse.utils import imt as imt, remove_quotes as remove_quotes

class NameAliasMixin:
    """Implements get_real_name and get_alias."""
    def get_real_name(self):
        """Returns the real name (object name) of this identifier."""
    def get_alias(self):
        """Returns the alias for this identifier or ``None``."""

class Token:
    """Base class for all other classes in this module.

    It represents a single token and has two instance attributes:
    ``value`` is the unchanged value of the token and ``ttype`` is
    the type of the token.
    """
    value: Incomplete
    ttype: Incomplete
    parent: Incomplete
    is_group: bool
    is_keyword: Incomplete
    is_whitespace: Incomplete
    normalized: Incomplete
    def __init__(self, ttype, value) -> None: ...
    def flatten(self) -> Generator[Incomplete, None, None]:
        """Resolve subgroups."""
    def match(self, ttype, values, regex: bool = False):
        """Checks whether the token matches the given arguments.

        *ttype* is a token type. If this token doesn't match the given token
        type.
        *values* is a list of possible values for this token. The values
        are OR'ed together so if only one of the values matches ``True``
        is returned. Except for keyword tokens the comparison is
        case-sensitive. For convenience it's OK to pass in a single string.
        If *regex* is ``True`` (default is ``False``) the given values are
        treated as regular expressions.
        """
    def within(self, group_cls):
        """Returns ``True`` if this token is within *group_cls*.

        Use this method for example to check if an identifier is within
        a function: ``t.within(sql.Function)``.
        """
    def is_child_of(self, other):
        """Returns ``True`` if this token is a direct child of *other*."""
    def has_ancestor(self, other):
        """Returns ``True`` if *other* is in this tokens ancestry."""

class TokenList(Token):
    """A group of tokens.

    It has an additional instance attribute ``tokens`` which holds a
    list of child-tokens.
    """
    tokens: Incomplete
    is_group: bool
    def __init__(self, tokens: Incomplete | None = None) -> None: ...
    def __iter__(self): ...
    def __getitem__(self, item): ...
    def get_token_at_offset(self, offset):
        """Returns the token that is on position offset."""
    def flatten(self) -> Generator[Incomplete, Incomplete, None]:
        """Generator yielding ungrouped tokens.

        This method is recursively called for all child tokens.
        """
    def get_sublists(self) -> Generator[Incomplete, None, None]: ...
    def token_first(self, skip_ws: bool = True, skip_cm: bool = False):
        """Returns the first child token.

        If *skip_ws* is ``True`` (the default), whitespace
        tokens are ignored.

        if *skip_cm* is ``True`` (default: ``False``), comments are
        ignored too.
        """
    def token_next_by(self, i: Incomplete | None = None, m: Incomplete | None = None, t: Incomplete | None = None, idx: int = -1, end: Incomplete | None = None): ...
    def token_not_matching(self, funcs, idx): ...
    def token_matching(self, funcs, idx): ...
    def token_prev(self, idx, skip_ws: bool = True, skip_cm: bool = False):
        """Returns the previous token relative to *idx*.

        If *skip_ws* is ``True`` (the default) whitespace tokens are ignored.
        If *skip_cm* is ``True`` comments are ignored.
        ``None`` is returned if there's no previous token.
        """
    def token_next(self, idx, skip_ws: bool = True, skip_cm: bool = False, _reverse: bool = False):
        """Returns the next token relative to *idx*.

        If *skip_ws* is ``True`` (the default) whitespace tokens are ignored.
        If *skip_cm* is ``True`` comments are ignored.
        ``None`` is returned if there's no next token.
        """
    def token_index(self, token, start: int = 0):
        """Return list index of token."""
    def group_tokens(self, grp_cls, start, end, include_end: bool = True, extend: bool = False):
        """Replace tokens by an instance of *grp_cls*."""
    def insert_before(self, where, token) -> None:
        """Inserts *token* before *where*."""
    def insert_after(self, where, token, skip_ws: bool = True) -> None:
        """Inserts *token* after *where*."""
    def has_alias(self):
        """Returns ``True`` if an alias is present."""
    def get_alias(self) -> None:
        """Returns the alias for this identifier or ``None``."""
    def get_name(self):
        """Returns the name of this identifier.

        This is either it's alias or it's real name. The returned valued can
        be considered as the name under which the object corresponding to
        this identifier is known within the current statement.
        """
    def get_real_name(self) -> None:
        """Returns the real name (object name) of this identifier."""
    def get_parent_name(self):
        """Return name of the parent object if any.

        A parent object is identified by the first occurring dot.
        """

class Statement(TokenList):
    """Represents a SQL statement."""
    def get_type(self):
        '''Returns the type of a statement.

        The returned value is a string holding an upper-cased reprint of
        the first DML or DDL keyword. If the first token in this group
        isn\'t a DML or DDL keyword "UNKNOWN" is returned.

        Whitespaces and comments at the beginning of the statement
        are ignored.
        '''

class Identifier(NameAliasMixin, TokenList):
    """Represents an identifier.

    Identifiers may have aliases or typecasts.
    """
    def is_wildcard(self):
        """Return ``True`` if this identifier contains a wildcard."""
    def get_typecast(self):
        """Returns the typecast or ``None`` of this object as a string."""
    def get_ordering(self):
        """Returns the ordering or ``None`` as uppercase string."""
    def get_array_indices(self) -> Generator[Incomplete, None, None]:
        """Returns an iterator of index token lists"""

class IdentifierList(TokenList):
    """A list of :class:`~sqlparse.sql.Identifier`'s."""
    def get_identifiers(self) -> Generator[Incomplete, None, None]:
        """Returns the identifiers.

        Whitespaces and punctuations are not included in this generator.
        """

class TypedLiteral(TokenList):
    '''A typed literal, such as "date \'2001-09-28\'" or "interval \'2 hours\'".'''
    M_OPEN: Incomplete
    M_CLOSE: Incomplete
    M_EXTEND: Incomplete

class Parenthesis(TokenList):
    """Tokens between parenthesis."""
    M_OPEN: Incomplete
    M_CLOSE: Incomplete

class SquareBrackets(TokenList):
    """Tokens between square brackets"""
    M_OPEN: Incomplete
    M_CLOSE: Incomplete

class Assignment(TokenList):
    """An assignment like 'var := val;'"""

class If(TokenList):
    """An 'if' clause with possible 'else if' or 'else' parts."""
    M_OPEN: Incomplete
    M_CLOSE: Incomplete

class For(TokenList):
    """A 'FOR' loop."""
    M_OPEN: Incomplete
    M_CLOSE: Incomplete

class Comparison(TokenList):
    """A comparison used for example in WHERE clauses."""
    @property
    def left(self): ...
    @property
    def right(self): ...

class Comment(TokenList):
    """A comment."""
    def is_multiline(self): ...

class Where(TokenList):
    """A WHERE clause."""
    M_OPEN: Incomplete
    M_CLOSE: Incomplete

class Having(TokenList):
    """A HAVING clause."""
    M_OPEN: Incomplete
    M_CLOSE: Incomplete

class Case(TokenList):
    """A CASE statement with one or more WHEN and possibly an ELSE part."""
    M_OPEN: Incomplete
    M_CLOSE: Incomplete
    def get_cases(self, skip_ws: bool = False):
        """Returns a list of 2-tuples (condition, value).

        If an ELSE exists condition is None.
        """

class Function(NameAliasMixin, TokenList):
    """A function or procedure call."""
    def get_parameters(self):
        """Return a list of parameters."""

class Begin(TokenList):
    """A BEGIN/END block."""
    M_OPEN: Incomplete
    M_CLOSE: Incomplete

class Operation(TokenList):
    """Grouping of operations"""
class Values(TokenList):
    """Grouping of values"""
class Command(TokenList):
    """Grouping of CLI commands."""
