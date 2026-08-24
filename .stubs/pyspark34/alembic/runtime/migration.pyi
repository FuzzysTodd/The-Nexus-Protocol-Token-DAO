from .. import ddl as ddl, util as util
from ..config import Config as Config
from ..script.base import Script as Script, ScriptDirectory as ScriptDirectory
from ..script.revision import Revision as Revision, RevisionMap as RevisionMap, _RevisionOrBase
from ..util import sqla_compat as sqla_compat
from ..util.compat import EncodedIO as EncodedIO
from .environment import EnvironmentContext as EnvironmentContext
from _typeshed import Incomplete
from sqlalchemy.engine import Dialect as Dialect, URL as URL
from sqlalchemy.engine.base import Connection as Connection, Transaction as Transaction
from sqlalchemy.engine.mock import MockConnection as MockConnection
from sqlalchemy.sql.elements import ClauseElement as ClauseElement
from typing import Any, Collection, ContextManager, Dict, Iterator, List, Set, Tuple

log: Incomplete

class _ProxyTransaction:
    migration_context: Incomplete
    def __init__(self, migration_context: MigrationContext) -> None: ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    def __enter__(self) -> _ProxyTransaction: ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...

class MigrationContext:
    '''Represent the database state made available to a migration
    script.

    :class:`.MigrationContext` is the front end to an actual
    database connection, or alternatively a string output
    stream given a particular database dialect,
    from an Alembic perspective.

    When inside the ``env.py`` script, the :class:`.MigrationContext`
    is available via the
    :meth:`.EnvironmentContext.get_context` method,
    which is available at ``alembic.context``::

        # from within env.py script
        from alembic import context

        migration_context = context.get_context()

    For usage outside of an ``env.py`` script, such as for
    utility routines that want to check the current version
    in the database, the :meth:`.MigrationContext.configure`
    method to create new :class:`.MigrationContext` objects.
    For example, to get at the current revision in the
    database using :meth:`.MigrationContext.get_current_revision`::

        # in any application, outside of an env.py script
        from alembic.migration import MigrationContext
        from sqlalchemy import create_engine

        engine = create_engine("postgresql://mydatabase")
        conn = engine.connect()

        context = MigrationContext.configure(conn)
        current_rev = context.get_current_revision()

    The above context can also be used to produce
    Alembic migration operations with an :class:`.Operations`
    instance::

        # in any application, outside of the normal Alembic environment
        from alembic.operations import Operations

        op = Operations(context)
        op.alter_column("mytable", "somecolumn", nullable=True)

    '''
    environment_context: Incomplete
    opts: Incomplete
    dialect: Incomplete
    script: Incomplete
    on_version_apply_callbacks: Incomplete
    connection: Incomplete
    as_sql: Incomplete
    purge: Incomplete
    output_buffer: Incomplete
    version_table: Incomplete
    version_table_schema: Incomplete
    impl: Incomplete
    def __init__(self, dialect: Dialect, connection: Connection | None, opts: Dict[str, Any], environment_context: EnvironmentContext | None = None) -> None: ...
    @classmethod
    def configure(cls, connection: Connection | None = None, url: str | URL | None = None, dialect_name: str | None = None, dialect: Dialect | None = None, environment_context: EnvironmentContext | None = None, dialect_opts: Dict[str, str] | None = None, opts: Any | None = None) -> MigrationContext:
        '''Create a new :class:`.MigrationContext`.

        This is a factory method usually called
        by :meth:`.EnvironmentContext.configure`.

        :param connection: a :class:`~sqlalchemy.engine.Connection`
         to use for SQL execution in "online" mode.  When present,
         is also used to determine the type of dialect in use.
        :param url: a string database url, or a
         :class:`sqlalchemy.engine.url.URL` object.
         The type of dialect to be used will be derived from this if
         ``connection`` is not passed.
        :param dialect_name: string name of a dialect, such as
         "postgresql", "mssql", etc.  The type of dialect to be used will be
         derived from this if ``connection`` and ``url`` are not passed.
        :param opts: dictionary of options.  Most other options
         accepted by :meth:`.EnvironmentContext.configure` are passed via
         this dictionary.

        '''
    def autocommit_block(self) -> Iterator[None]:
        '''Enter an "autocommit" block, for databases that support AUTOCOMMIT
        isolation levels.

        This special directive is intended to support the occasional database
        DDL or system operation that specifically has to be run outside of
        any kind of transaction block.   The PostgreSQL database platform
        is the most common target for this style of operation, as many
        of its DDL operations must be run outside of transaction blocks, even
        though the database overall supports transactional DDL.

        The method is used as a context manager within a migration script, by
        calling on :meth:`.Operations.get_context` to retrieve the
        :class:`.MigrationContext`, then invoking
        :meth:`.MigrationContext.autocommit_block` using the ``with:``
        statement::

            def upgrade():
                with op.get_context().autocommit_block():
                    op.execute("ALTER TYPE mood ADD VALUE \'soso\'")

        Above, a PostgreSQL "ALTER TYPE..ADD VALUE" directive is emitted,
        which must be run outside of a transaction block at the database level.
        The :meth:`.MigrationContext.autocommit_block` method makes use of the
        SQLAlchemy ``AUTOCOMMIT`` isolation level setting, which against the
        psycogp2 DBAPI corresponds to the ``connection.autocommit`` setting,
        to ensure that the database driver is not inside of a DBAPI level
        transaction block.

        .. warning::

            As is necessary, **the database transaction preceding the block is
            unconditionally committed**.  This means that the run of migrations
            preceding the operation will be committed, before the overall
            migration operation is complete.

            It is recommended that when an application includes migrations with
            "autocommit" blocks, that
            :paramref:`.EnvironmentContext.transaction_per_migration` be used
            so that the calling environment is tuned to expect short per-file
            migrations whether or not one of them has an autocommit block.


        '''
    def begin_transaction(self, _per_migration: bool = False) -> _ProxyTransaction | ContextManager[None]:
        '''Begin a logical transaction for migration operations.

        This method is used within an ``env.py`` script to demarcate where
        the outer "transaction" for a series of migrations begins.  Example::

            def run_migrations_online():
                connectable = create_engine(...)

                with connectable.connect() as connection:
                    context.configure(
                        connection=connection, target_metadata=target_metadata
                    )

                    with context.begin_transaction():
                        context.run_migrations()

        Above, :meth:`.MigrationContext.begin_transaction` is used to demarcate
        where the outer logical transaction occurs around the
        :meth:`.MigrationContext.run_migrations` operation.

        A "Logical" transaction means that the operation may or may not
        correspond to a real database transaction.   If the target database
        supports transactional DDL (or
        :paramref:`.EnvironmentContext.configure.transactional_ddl` is true),
        the :paramref:`.EnvironmentContext.configure.transaction_per_migration`
        flag is not set, and the migration is against a real database
        connection (as opposed to using "offline" ``--sql`` mode), a real
        transaction will be started.   If ``--sql`` mode is in effect, the
        operation would instead correspond to a string such as "BEGIN" being
        emitted to the string output.

        The returned object is a Python context manager that should only be
        used in the context of a ``with:`` statement as indicated above.
        The object has no other guaranteed API features present.

        .. seealso::

            :meth:`.MigrationContext.autocommit_block`

        '''
    def get_current_revision(self) -> str | None:
        '''Return the current revision, usually that which is present
        in the ``alembic_version`` table in the database.

        This method intends to be used only for a migration stream that
        does not contain unmerged branches in the target database;
        if there are multiple branches present, an exception is raised.
        The :meth:`.MigrationContext.get_current_heads` should be preferred
        over this method going forward in order to be compatible with
        branch migration support.

        If this :class:`.MigrationContext` was configured in "offline"
        mode, that is with ``as_sql=True``, the ``starting_rev``
        parameter is returned instead, if any.

        '''
    def get_current_heads(self) -> Tuple[str, ...]:
        '''Return a tuple of the current \'head versions\' that are represented
        in the target database.

        For a migration stream without branches, this will be a single
        value, synonymous with that of
        :meth:`.MigrationContext.get_current_revision`.   However when multiple
        unmerged branches exist within the target database, the returned tuple
        will contain a value for each head.

        If this :class:`.MigrationContext` was configured in "offline"
        mode, that is with ``as_sql=True``, the ``starting_rev``
        parameter is returned in a one-length tuple.

        If no version table is present, or if there are no revisions
        present, an empty tuple is returned.

        '''
    def stamp(self, script_directory: ScriptDirectory, revision: str) -> None:
        """Stamp the version table with a specific revision.

        This method calculates those branches to which the given revision
        can apply, and updates those branches as though they were migrated
        towards that revision (either up or down).  If no current branches
        include the revision, it is added as a new branch head.

        """
    def run_migrations(self, **kw: Any) -> None:
        '''Run the migration scripts established for this
        :class:`.MigrationContext`, if any.

        The commands in :mod:`alembic.command` will set up a function
        that is ultimately passed to the :class:`.MigrationContext`
        as the ``fn`` argument.  This function represents the "work"
        that will be done when :meth:`.MigrationContext.run_migrations`
        is called, typically from within the ``env.py`` script of the
        migration environment.  The "work function" then provides an iterable
        of version callables and other version information which
        in the case of the ``upgrade`` or ``downgrade`` commands are the
        list of version scripts to invoke.  Other commands yield nothing,
        in the case that a command wants to run some other operation
        against the database such as the ``current`` or ``stamp`` commands.

        :param \\**kw: keyword arguments here will be passed to each
         migration callable, that is the ``upgrade()`` or ``downgrade()``
         method within revision scripts.

        '''
    def execute(self, sql: ClauseElement | str, execution_options: dict | None = None) -> None:
        '''Execute a SQL construct or string statement.

        The underlying execution mechanics are used, that is
        if this is "offline mode" the SQL is written to the
        output buffer, otherwise the SQL is emitted on
        the current SQLAlchemy connection.

        '''
    @property
    def bind(self) -> Connection | None:
        '''Return the current "bind".

        In online mode, this is an instance of
        :class:`sqlalchemy.engine.Connection`, and is suitable
        for ad-hoc execution of any kind of usage described
        in SQLAlchemy Core documentation as well as
        for usage with the :meth:`sqlalchemy.schema.Table.create`
        and :meth:`sqlalchemy.schema.MetaData.create_all` methods
        of :class:`~sqlalchemy.schema.Table`,
        :class:`~sqlalchemy.schema.MetaData`.

        Note that when "standard output" mode is enabled,
        this bind will be a "mock" connection handler that cannot
        return results and is only appropriate for a very limited
        subset of commands.

        '''
    @property
    def config(self) -> Config | None:
        """Return the :class:`.Config` used by the current environment,
        if any."""

class HeadMaintainer:
    context: Incomplete
    heads: Incomplete
    def __init__(self, context: MigrationContext, heads: Any) -> None: ...
    def update_to_step(self, step: RevisionStep | StampStep) -> None: ...

class MigrationInfo:
    """Exposes information about a migration step to a callback listener.

    The :class:`.MigrationInfo` object is available exclusively for the
    benefit of the :paramref:`.EnvironmentContext.on_version_apply`
    callback hook.

    """
    is_upgrade: bool
    is_stamp: bool
    up_revision_id: str | None
    up_revision_ids: Tuple[str, ...]
    down_revision_ids: Tuple[str, ...]
    revision_map: RevisionMap
    def __init__(self, revision_map: RevisionMap, is_upgrade: bool, is_stamp: bool, up_revisions: str | Tuple[str, ...], down_revisions: str | Tuple[str, ...]) -> None: ...
    @property
    def is_migration(self) -> bool:
        """True/False: indicates whether this operation is a migration.

        At present this is true if and only the migration is not a stamp.
        If other operation types are added in the future, both this attribute
        and :attr:`~.MigrationInfo.is_stamp` will be false.
        """
    @property
    def source_revision_ids(self) -> Tuple[str, ...]:
        """Active revisions before this migration step is applied."""
    @property
    def destination_revision_ids(self) -> Tuple[str, ...]:
        """Active revisions after this migration step is applied."""
    @property
    def up_revision(self) -> Revision | None:
        """Get :attr:`~.MigrationInfo.up_revision_id` as
        a :class:`.Revision`.

        """
    @property
    def up_revisions(self) -> Tuple[_RevisionOrBase | None, ...]:
        """Get :attr:`~.MigrationInfo.up_revision_ids` as a
        :class:`.Revision`."""
    @property
    def down_revisions(self) -> Tuple[_RevisionOrBase | None, ...]:
        """Get :attr:`~.MigrationInfo.down_revision_ids` as a tuple of
        :class:`Revisions <.Revision>`."""
    @property
    def source_revisions(self) -> Tuple[_RevisionOrBase | None, ...]:
        """Get :attr:`~MigrationInfo.source_revision_ids` as a tuple of
        :class:`Revisions <.Revision>`."""
    @property
    def destination_revisions(self) -> Tuple[_RevisionOrBase | None, ...]:
        """Get :attr:`~MigrationInfo.destination_revision_ids` as a tuple of
        :class:`Revisions <.Revision>`."""

class MigrationStep:
    from_revisions_no_deps: Tuple[str, ...]
    to_revisions_no_deps: Tuple[str, ...]
    is_upgrade: bool
    migration_fn: Any
    @property
    def name(self) -> str: ...
    @classmethod
    def upgrade_from_script(cls, revision_map: RevisionMap, script: Script) -> RevisionStep: ...
    @classmethod
    def downgrade_from_script(cls, revision_map: RevisionMap, script: Script) -> RevisionStep: ...
    @property
    def is_downgrade(self) -> bool: ...
    @property
    def short_log(self) -> str: ...

class RevisionStep(MigrationStep):
    revision_map: Incomplete
    revision: Incomplete
    is_upgrade: Incomplete
    migration_fn: Incomplete
    def __init__(self, revision_map: RevisionMap, revision: Script, is_upgrade: bool) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    @property
    def doc(self) -> str: ...
    @property
    def from_revisions(self) -> Tuple[str, ...]: ...
    @property
    def from_revisions_no_deps(self) -> Tuple[str, ...]: ...
    @property
    def to_revisions(self) -> Tuple[str, ...]: ...
    @property
    def to_revisions_no_deps(self) -> Tuple[str, ...]: ...
    def should_delete_branch(self, heads: Set[str]) -> bool:
        '''A delete is when we are a. in a downgrade and b.
        we are going to the "base" or we are going to a version that
        is implied as a dependency on another version that is remaining.

        '''
    def merge_branch_idents(self, heads: Set[str]) -> Tuple[List[str], str, str]: ...
    def unmerge_branch_idents(self, heads: Collection[str]) -> Tuple[str, str, Tuple[str, ...]]: ...
    def should_create_branch(self, heads: Set[str]) -> bool: ...
    def should_merge_branches(self, heads: Set[str]) -> bool: ...
    def should_unmerge_branches(self, heads: Set[str]) -> bool: ...
    def update_version_num(self, heads: Set[str]) -> Tuple[str, str]: ...
    @property
    def delete_version_num(self) -> str: ...
    @property
    def insert_version_num(self) -> str: ...
    @property
    def info(self) -> MigrationInfo: ...

class StampStep(MigrationStep):
    from_: Incomplete
    to_: Incomplete
    is_upgrade: Incomplete
    branch_move: Incomplete
    migration_fn: Incomplete
    revision_map: Incomplete
    def __init__(self, from_: str | Collection[str] | None, to_: str | Collection[str] | None, is_upgrade: bool, branch_move: bool, revision_map: RevisionMap | None = None) -> None: ...
    doc: str | None
    def stamp_revision(self, **kw: Any) -> None: ...
    def __eq__(self, other): ...
    @property
    def from_revisions(self): ...
    @property
    def to_revisions(self) -> Tuple[str, ...]: ...
    @property
    def from_revisions_no_deps(self) -> Tuple[str, ...]: ...
    @property
    def to_revisions_no_deps(self) -> Tuple[str, ...]: ...
    @property
    def delete_version_num(self) -> str: ...
    @property
    def insert_version_num(self) -> str: ...
    def update_version_num(self, heads: Set[str]) -> Tuple[str, str]: ...
    def merge_branch_idents(self, heads: Set[str] | List[str]) -> Tuple[List[Any], str, str] | Tuple[List[str], str, str]: ...
    def unmerge_branch_idents(self, heads: Set[str]) -> Tuple[str, str, List[str]]: ...
    def should_delete_branch(self, heads: Set[str]) -> bool: ...
    def should_create_branch(self, heads: Set[str]) -> Set[str] | bool: ...
    def should_merge_branches(self, heads: Set[str]) -> bool: ...
    def should_unmerge_branches(self, heads: Set[str]) -> bool: ...
    @property
    def info(self) -> MigrationInfo: ...
