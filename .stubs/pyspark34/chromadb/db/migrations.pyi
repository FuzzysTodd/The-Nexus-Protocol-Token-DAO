import abc
from _typeshed import Incomplete
from abc import abstractmethod
from chromadb.config import Settings as Settings, System as System
from chromadb.db.base import Cursor as Cursor, SqlDB as SqlDB
from importlib_resources.abc import Traversable as Traversable
from typing import Sequence
from typing_extensions import NotRequired, TypedDict

class MigrationFile(TypedDict):
    path: NotRequired[Traversable]
    dir: str
    filename: str
    version: int
    scope: str

class Migration(MigrationFile):
    hash: str
    sql: str

class UninitializedMigrationsError(Exception):
    def __init__(self) -> None: ...

class UnappliedMigrationsError(Exception):
    dir: Incomplete
    version: Incomplete
    def __init__(self, dir: str, version: int) -> None: ...

class InconsistentVersionError(Exception):
    def __init__(self, dir: str, db_version: int, source_version: int) -> None: ...

class InconsistentHashError(Exception):
    def __init__(self, path: str, db_hash: str, source_hash: str) -> None: ...

class InvalidMigrationFilename(Exception): ...

class MigratableDB(SqlDB, metaclass=abc.ABCMeta):
    '''Simple base class for databases which support basic migrations.

    Migrations are SQL files stored as package resources and accessed via
    importlib_resources.

    All migrations in the same directory are assumed to be dependent on previous
    migrations in the same directory, where "previous" is defined on lexographical
    ordering of filenames.

    Migrations have a ascending numeric version number and a hash of the file contents.
    When migrations are applied, the hashes of previous migrations are checked to ensure
    that the database is consistent with the source repository. If they are not, an
    error is thrown and no migrations will be applied.

    Migration files must follow the naming convention:
    <version>.<description>.<scope>.sql, where <version> is a 5-digit zero-padded
    integer, <description> is a short textual description, and <scope> is a short string
    identifying the database implementation.
    '''
    def __init__(self, system: System) -> None: ...
    @staticmethod
    @abstractmethod
    def migration_scope() -> str:
        """The database implementation to use for migrations (e.g, sqlite, pgsql)"""
    @abstractmethod
    def migration_dirs(self) -> Sequence[Traversable]:
        """Directories containing the migration sequences that should be applied to this
        DB."""
    @abstractmethod
    def setup_migrations(self) -> None:
        """Idempotently creates the migrations table"""
    @abstractmethod
    def migrations_initialized(self) -> bool:
        """Return true if the migrations table exists"""
    @abstractmethod
    def db_migrations(self, dir: Traversable) -> Sequence[Migration]:
        """Return a list of all migrations already applied to this database, from the
        given source directory, in ascending order."""
    @abstractmethod
    def apply_migration(self, cur: Cursor, migration: Migration) -> None:
        """Apply a single migration to the database"""
    def initialize_migrations(self) -> None:
        """Initialize migrations for this DB"""
    def validate_migrations(self) -> None:
        """Validate all migrations and throw an exception if there are any unapplied
        migrations in the source repo."""
    def apply_migrations(self) -> None:
        """Validate existing migrations, and apply all new ones."""

filename_regex: Incomplete

def verify_migration_sequence(db_migrations: Sequence[Migration], source_migrations: Sequence[Migration]) -> Sequence[Migration]:
    """Given a list of migrations already applied to a database, and a list of
    migrations from the source code, validate that the applied migrations are correct
    and match the expected migrations.

    Throws an exception if any migrations are missing, out of order, or if the source
    hash does not match.

    Returns a list of all unapplied migrations, or an empty list if all migrations are
    applied and the database is up to date."""
def find_migrations(dir: Traversable, scope: str) -> Sequence[Migration]:
    """Return a list of all migration present in the given directory, in ascending
    order. Filter by scope."""
