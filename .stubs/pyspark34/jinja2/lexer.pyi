import typing as t
import typing_extensions as te
from .environment import Environment as Environment
from .exceptions import TemplateSyntaxError as TemplateSyntaxError
from .utils import LRUCache as LRUCache
from _typeshed import Incomplete

whitespace_re: Incomplete
newline_re: Incomplete
string_re: Incomplete
integer_re: Incomplete
float_re: Incomplete
TOKEN_ADD: Incomplete
TOKEN_ASSIGN: Incomplete
TOKEN_COLON: Incomplete
TOKEN_COMMA: Incomplete
TOKEN_DIV: Incomplete
TOKEN_DOT: Incomplete
TOKEN_EQ: Incomplete
TOKEN_FLOORDIV: Incomplete
TOKEN_GT: Incomplete
TOKEN_GTEQ: Incomplete
TOKEN_LBRACE: Incomplete
TOKEN_LBRACKET: Incomplete
TOKEN_LPAREN: Incomplete
TOKEN_LT: Incomplete
TOKEN_LTEQ: Incomplete
TOKEN_MOD: Incomplete
TOKEN_MUL: Incomplete
TOKEN_NE: Incomplete
TOKEN_PIPE: Incomplete
TOKEN_POW: Incomplete
TOKEN_RBRACE: Incomplete
TOKEN_RBRACKET: Incomplete
TOKEN_RPAREN: Incomplete
TOKEN_SEMICOLON: Incomplete
TOKEN_SUB: Incomplete
TOKEN_TILDE: Incomplete
TOKEN_WHITESPACE: Incomplete
TOKEN_FLOAT: Incomplete
TOKEN_INTEGER: Incomplete
TOKEN_NAME: Incomplete
TOKEN_STRING: Incomplete
TOKEN_OPERATOR: Incomplete
TOKEN_BLOCK_BEGIN: Incomplete
TOKEN_BLOCK_END: Incomplete
TOKEN_VARIABLE_BEGIN: Incomplete
TOKEN_VARIABLE_END: Incomplete
TOKEN_RAW_BEGIN: Incomplete
TOKEN_RAW_END: Incomplete
TOKEN_COMMENT_BEGIN: Incomplete
TOKEN_COMMENT_END: Incomplete
TOKEN_COMMENT: Incomplete
TOKEN_LINESTATEMENT_BEGIN: Incomplete
TOKEN_LINESTATEMENT_END: Incomplete
TOKEN_LINECOMMENT_BEGIN: Incomplete
TOKEN_LINECOMMENT_END: Incomplete
TOKEN_LINECOMMENT: Incomplete
TOKEN_DATA: Incomplete
TOKEN_INITIAL: Incomplete
TOKEN_EOF: Incomplete
operators: Incomplete
reverse_operators: Incomplete
operator_re: Incomplete
ignored_tokens: Incomplete
ignore_if_empty: Incomplete

def describe_token(token: Token) -> str:
    """Returns a description of the token."""
def describe_token_expr(expr: str) -> str:
    """Like `describe_token` but for token expressions."""
def count_newlines(value: str) -> int:
    """Count the number of newline characters in the string.  This is
    useful for extensions that filter a stream.
    """
def compile_rules(environment: Environment) -> t.List[t.Tuple[str, str]]:
    """Compiles all the rules from the environment into a list of rules."""

class Failure:
    """Class that raises a `TemplateSyntaxError` if called.
    Used by the `Lexer` to specify known errors.
    """
    message: Incomplete
    error_class: Incomplete
    def __init__(self, message: str, cls: t.Type[TemplateSyntaxError] = ...) -> None: ...
    def __call__(self, lineno: int, filename: str) -> te.NoReturn: ...

class Token(t.NamedTuple):
    lineno: int
    type: str
    value: str
    def test(self, expr: str) -> bool:
        """Test a token against a token expression.  This can either be a
        token type or ``'token_type:token_value'``.  This can only test
        against string values and types.
        """
    def test_any(self, *iterable: str) -> bool:
        """Test against multiple token expressions."""

class TokenStreamIterator:
    """The iterator for tokenstreams.  Iterate over the stream
    until the eof token is reached.
    """
    stream: Incomplete
    def __init__(self, stream: TokenStream) -> None: ...
    def __iter__(self) -> TokenStreamIterator: ...
    def __next__(self) -> Token: ...

class TokenStream:
    """A token stream is an iterable that yields :class:`Token`\\s.  The
    parser however does not iterate over it but calls :meth:`next` to go
    one token ahead.  The current active token is stored as :attr:`current`.
    """
    name: Incomplete
    filename: Incomplete
    closed: bool
    current: Incomplete
    def __init__(self, generator: t.Iterable[Token], name: str | None, filename: str | None) -> None: ...
    def __iter__(self) -> TokenStreamIterator: ...
    def __bool__(self) -> bool: ...
    @property
    def eos(self) -> bool:
        """Are we at the end of the stream?"""
    def push(self, token: Token) -> None:
        """Push a token back to the stream."""
    def look(self) -> Token:
        """Look at the next token."""
    def skip(self, n: int = 1) -> None:
        """Got n tokens ahead."""
    def next_if(self, expr: str) -> Token | None:
        """Perform the token test and return the token if it matched.
        Otherwise the return value is `None`.
        """
    def skip_if(self, expr: str) -> bool:
        """Like :meth:`next_if` but only returns `True` or `False`."""
    def __next__(self) -> Token:
        """Go one token ahead and return the old one.

        Use the built-in :func:`next` instead of calling this directly.
        """
    def close(self) -> None:
        """Close the stream."""
    def expect(self, expr: str) -> Token:
        """Expect a given token type and return it.  This accepts the same
        argument as :meth:`jinja2.lexer.Token.test`.
        """

def get_lexer(environment: Environment) -> Lexer:
    """Return a lexer which is probably cached."""

class OptionalLStrip(tuple):
    """A special tuple for marking a point in the state that can have
    lstrip applied.
    """
    def __new__(cls, *members, **kwargs): ...

class _Rule(t.NamedTuple):
    pattern: t.Pattern[str]
    tokens: str | t.Tuple[str, ...] | t.Tuple[Failure]
    command: str | None

class Lexer:
    """Class that implements a lexer for a given environment. Automatically
    created by the environment class, usually you don't have to do that.

    Note that the lexer is not automatically bound to an environment.
    Multiple environments can share the same lexer.
    """
    lstrip_blocks: Incomplete
    newline_sequence: Incomplete
    keep_trailing_newline: Incomplete
    rules: Incomplete
    def __init__(self, environment: Environment) -> None: ...
    def tokenize(self, source: str, name: str | None = None, filename: str | None = None, state: str | None = None) -> TokenStream:
        """Calls tokeniter + tokenize and wraps it in a token stream."""
    def wrap(self, stream: t.Iterable[t.Tuple[int, str, str]], name: str | None = None, filename: str | None = None) -> t.Iterator[Token]:
        """This is called with the stream as returned by `tokenize` and wraps
        every token in a :class:`Token` and converts the value.
        """
    def tokeniter(self, source: str, name: str | None, filename: str | None = None, state: str | None = None) -> t.Iterator[t.Tuple[int, str, str]]:
        """This method tokenizes the text and returns the tokens in a
        generator. Use this method if you just want to tokenize a template.

        .. versionchanged:: 3.0
            Only ``\\n``, ``\\r\\n`` and ``\\r`` are treated as line
            breaks.
        """
