from . import compare as compare, render as render
from .. import util as util
from ..config import Config as Config
from ..operations import ops as ops
from ..operations.ops import DowngradeOps as DowngradeOps, MigrationScript as MigrationScript, UpgradeOps as UpgradeOps
from ..runtime.environment import NameFilterParentNames as NameFilterParentNames, NameFilterType as NameFilterType, RenderItemFn as RenderItemFn
from ..runtime.migration import MigrationContext as MigrationContext
from ..script.base import Script as Script, ScriptDirectory as ScriptDirectory
from _typeshed import Incomplete
from sqlalchemy.engine import Connection as Connection, Dialect as Dialect, Inspector as Inspector
from sqlalchemy.sql.schema import MetaData as MetaData, SchemaItem as SchemaItem
from typing import Any, Callable, Dict, Iterator, Sequence, Set

def compare_metadata(context: MigrationContext, metadata: MetaData) -> Any:
    '''Compare a database schema to that given in a
    :class:`~sqlalchemy.schema.MetaData` instance.

    The database connection is presented in the context
    of a :class:`.MigrationContext` object, which
    provides database connectivity as well as optional
    comparison functions to use for datatypes and
    server defaults - see the "autogenerate" arguments
    at :meth:`.EnvironmentContext.configure`
    for details on these.

    The return format is a list of "diff" directives,
    each representing individual differences::

        from alembic.migration import MigrationContext
        from alembic.autogenerate import compare_metadata
        from sqlalchemy import (
            create_engine,
            MetaData,
            Column,
            Integer,
            String,
            Table,
            text,
        )
        import pprint

        engine = create_engine("sqlite://")

        with engine.begin() as conn:
            conn.execute(
                text(
                    \'\'\'
                        create table foo (
                            id integer not null primary key,
                            old_data varchar,
                            x integer
                        )
                    \'\'\'
                )
            )
            conn.execute(text("create table bar (data varchar)"))

        metadata = MetaData()
        Table(
            "foo",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("data", Integer),
            Column("x", Integer, nullable=False),
        )
        Table("bat", metadata, Column("info", String))

        mc = MigrationContext.configure(engine.connect())

        diff = compare_metadata(mc, metadata)
        pprint.pprint(diff, indent=2, width=20)

    Output::

        [
            (
                "add_table",
                Table(
                    "bat",
                    MetaData(),
                    Column("info", String(), table=<bat>),
                    schema=None,
                ),
            ),
            (
                "remove_table",
                Table(
                    "bar",
                    MetaData(),
                    Column("data", VARCHAR(), table=<bar>),
                    schema=None,
                ),
            ),
            (
                "add_column",
                None,
                "foo",
                Column("data", Integer(), table=<foo>),
            ),
            [
                (
                    "modify_nullable",
                    None,
                    "foo",
                    "x",
                    {
                        "existing_comment": None,
                        "existing_server_default": False,
                        "existing_type": INTEGER(),
                    },
                    True,
                    False,
                )
            ],
            (
                "remove_column",
                None,
                "foo",
                Column("old_data", VARCHAR(), table=<foo>),
            ),
        ]

    :param context: a :class:`.MigrationContext`
     instance.
    :param metadata: a :class:`~sqlalchemy.schema.MetaData`
     instance.

    .. seealso::

        :func:`.produce_migrations` - produces a :class:`.MigrationScript`
        structure based on metadata comparison.

    '''
def produce_migrations(context: MigrationContext, metadata: MetaData) -> MigrationScript:
    '''Produce a :class:`.MigrationScript` structure based on schema
    comparison.

    This function does essentially what :func:`.compare_metadata` does,
    but then runs the resulting list of diffs to produce the full
    :class:`.MigrationScript` object.   For an example of what this looks like,
    see the example in :ref:`customizing_revision`.

    .. seealso::

        :func:`.compare_metadata` - returns more fundamental "diff"
        data from comparing a schema.

    '''
def render_python_code(up_or_down_op: UpgradeOps | DowngradeOps, sqlalchemy_module_prefix: str = 'sa.', alembic_module_prefix: str = 'op.', render_as_batch: bool = False, imports: Sequence[str] = (), render_item: RenderItemFn | None = None, migration_context: MigrationContext | None = None, user_module_prefix: str | None = None) -> str:
    '''Render Python code given an :class:`.UpgradeOps` or
    :class:`.DowngradeOps` object.

    This is a convenience function that can be used to test the
    autogenerate output of a user-defined :class:`.MigrationScript` structure.

    :param up_or_down_op: :class:`.UpgradeOps` or :class:`.DowngradeOps` object
    :param sqlalchemy_module_prefix: module prefix for SQLAlchemy objects
    :param alembic_module_prefix: module prefix for Alembic constructs
    :param render_as_batch: use "batch operations" style for rendering
    :param imports: sequence of import symbols to add
    :param render_item: callable to render items
    :param migration_context: optional :class:`.MigrationContext`
    :param user_module_prefix: optional string prefix for user-defined types

     .. versionadded:: 1.11.0

    '''

class AutogenContext:
    """Maintains configuration and state that's specific to an
    autogenerate operation."""
    metadata: MetaData | None
    connection: Connection | None
    dialect: Dialect | None
    imports: Set[str]
    migration_context: MigrationContext
    opts: Incomplete
    def __init__(self, migration_context: MigrationContext, metadata: MetaData | None = None, opts: dict | None = None, autogenerate: bool = True) -> None: ...
    def inspector(self) -> Inspector: ...
    def run_name_filters(self, name: str | None, type_: NameFilterType, parent_names: NameFilterParentNames) -> bool:
        """Run the context's name filters and return True if the targets
        should be part of the autogenerate operation.

        This method should be run for every kind of name encountered within the
        reflection side of an autogenerate operation, giving the environment
        the chance to filter what names should be reflected as database
        objects.  The filters here are produced directly via the
        :paramref:`.EnvironmentContext.configure.include_name` parameter.

        """
    def run_object_filters(self, object_: SchemaItem, name: str | None, type_: NameFilterType, reflected: bool, compare_to: SchemaItem | None) -> bool:
        """Run the context's object filters and return True if the targets
        should be part of the autogenerate operation.

        This method should be run for every kind of object encountered within
        an autogenerate operation, giving the environment the chance
        to filter what objects should be included in the comparison.
        The filters here are produced directly via the
        :paramref:`.EnvironmentContext.configure.include_object` parameter.

        """
    run_filters = run_object_filters
    def sorted_tables(self):
        """Return an aggregate of the :attr:`.MetaData.sorted_tables`
        collection(s).

        For a sequence of :class:`.MetaData` objects, this
        concatenates the :attr:`.MetaData.sorted_tables` collection
        for each individual :class:`.MetaData`  in the order of the
        sequence.  It does **not** collate the sorted tables collections.

        """
    def table_key_to_table(self):
        """Return an aggregate  of the :attr:`.MetaData.tables` dictionaries.

        The :attr:`.MetaData.tables` collection is a dictionary of table key
        to :class:`.Table`; this method aggregates the dictionary across
        multiple :class:`.MetaData` objects into one dictionary.

        Duplicate table keys are **not** supported; if two :class:`.MetaData`
        objects contain the same table key, an exception is raised.

        """

class RevisionContext:
    """Maintains configuration and state that's specific to a revision
    file generation operation."""
    config: Incomplete
    script_directory: Incomplete
    command_args: Incomplete
    process_revision_directives: Incomplete
    template_args: Incomplete
    generated_revisions: Incomplete
    def __init__(self, config: Config, script_directory: ScriptDirectory, command_args: Dict[str, Any], process_revision_directives: Callable | None = None) -> None: ...
    def run_autogenerate(self, rev: tuple, migration_context: MigrationContext) -> None: ...
    def run_no_autogenerate(self, rev: tuple, migration_context: MigrationContext) -> None: ...
    def generate_scripts(self) -> Iterator[Script | None]: ...
