from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import Lexer, RegexLexer

__all__ = ['PostgresLexer', 'PlPgsqlLexer', 'PostgresConsoleLexer', 'PostgresExplainLexer', 'SqlLexer', 'TransactSqlLexer', 'MySqlLexer', 'SqliteConsoleLexer', 'RqlLexer']

class PostgresBase:
    """Base class for Postgres-related lexers.

    This is implemented as a mixin to avoid the Lexer metaclass kicking in.
    this way the different lexer don't have a common Lexer ancestor. If they
    had, _tokens could be created on this ancestor and not updated for the
    other classes, resulting e.g. in PL/pgSQL parsed as SQL. This shortcoming
    seem to suggest that regexp lexers are not really subclassable.
    """
    text: Incomplete
    def get_tokens_unprocessed(self, text, *args) -> Generator[Incomplete, Incomplete, None]: ...

class PostgresLexer(PostgresBase, RegexLexer):
    """
    Lexer for the PostgreSQL dialect of SQL.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class PlPgsqlLexer(PostgresBase, RegexLexer):
    """
    Handle the extra syntax in Pl/pgSQL language.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class PsqlRegexLexer(PostgresBase, RegexLexer):
    """
    Extend the PostgresLexer adding support specific for psql commands.

    This is not a complete psql lexer yet as it lacks prompt support
    and output rendering.
    """
    name: str
    aliases: Incomplete
    flags: Incomplete
    tokens: Incomplete

class lookahead:
    """Wrap an iterator and allow pushing back an item."""
    iter: Incomplete
    def __init__(self, x) -> None: ...
    def __iter__(self): ...
    def send(self, i): ...
    def __next__(self): ...
    next = __next__

class PostgresConsoleLexer(Lexer):
    """
    Lexer for psql sessions.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    def get_tokens_unprocessed(self, data) -> Generator[Incomplete, Incomplete, None]: ...

class PostgresExplainLexer(RegexLexer):
    """
    Handle PostgreSQL EXPLAIN output

    .. versionadded:: 2.15
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class SqlLexer(RegexLexer):
    """
    Lexer for Structured Query Language. Currently, this lexer does
    not recognize any special syntax except ANSI SQL.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(self, text) -> None: ...

class TransactSqlLexer(RegexLexer):
    """
    Transact-SQL (T-SQL) is Microsoft's and Sybase's proprietary extension to
    SQL.

    The list of keywords includes ODBC and keywords reserved for future use..
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class MySqlLexer(RegexLexer):
    """The Oracle MySQL lexer.

    This lexer does not attempt to maintain strict compatibility with
    MariaDB syntax or keywords. Although MySQL and MariaDB's common code
    history suggests there may be significant overlap between the two,
    compatibility between the two is not a target for this lexer.
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class SqliteConsoleLexer(Lexer):
    """
    Lexer for example sessions using sqlite3.

    .. versionadded:: 0.11
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def get_tokens_unprocessed(self, data) -> Generator[Incomplete, Incomplete, None]: ...

class RqlLexer(RegexLexer):
    """
    Lexer for Relation Query Language.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
