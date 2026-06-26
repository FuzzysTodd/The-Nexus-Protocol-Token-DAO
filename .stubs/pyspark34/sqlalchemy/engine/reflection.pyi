from .. import exc as exc, inspection as inspection, sql as sql, util as util
from ..sql import operators as operators, schema as sa_schema
from ..sql.elements import TextClause as TextClause
from ..sql.type_api import TypeEngine as TypeEngine
from ..sql.visitors import InternalTraversal as InternalTraversal
from ..util import topological as topological
from ..util.typing import final as final
from .base import Connection as Connection, Engine as Engine
from .interfaces import Dialect as Dialect, ReflectedCheckConstraint as ReflectedCheckConstraint, ReflectedColumn as ReflectedColumn, ReflectedForeignKeyConstraint as ReflectedForeignKeyConstraint, ReflectedIndex as ReflectedIndex, ReflectedPrimaryKeyConstraint as ReflectedPrimaryKeyConstraint, ReflectedTableComment as ReflectedTableComment, ReflectedUniqueConstraint as ReflectedUniqueConstraint, TableKey as TableKey
from _typeshed import Incomplete
from dataclasses import dataclass
from enum import Flag
from typing import Any, Callable, Collection, Dict, List, Sequence, Set, Tuple

def cache(fn: Callable[..., _R], self: Dialect, con: Connection, *args: Any, **kw: Any) -> _R: ...
def flexi_cache(*traverse_args: Tuple[str, InternalTraversal]) -> Callable[[Callable[..., _R]], Callable[..., _R]]: ...

class ObjectKind(Flag):
    """Enumerator that indicates which kind of object to return when calling
    the ``get_multi`` methods.

    This is a Flag enum, so custom combinations can be passed. For example,
    to reflect tables and plain views ``ObjectKind.TABLE | ObjectKind.VIEW``
    may be used.

    .. note::
      Not all dialect may support all kind of object. If a dialect does
      not support a particular object an empty dict is returned.
      In case a dialect supports an object, but the requested method
      is not applicable for the specified kind the default value
      will be returned for each reflected object. For example reflecting
      check constraints of view return a dict with all the views with
      empty lists as values.
    """
    TABLE: Incomplete
    VIEW: Incomplete
    MATERIALIZED_VIEW: Incomplete
    ANY_VIEW: Incomplete
    ANY: Incomplete

class ObjectScope(Flag):
    """Enumerator that indicates which scope to use when calling
    the ``get_multi`` methods.
    """
    DEFAULT: Incomplete
    TEMPORARY: Incomplete
    ANY: Incomplete

class Inspector(inspection.Inspectable['Inspector']):
    """Performs database schema inspection.

    The Inspector acts as a proxy to the reflection methods of the
    :class:`~sqlalchemy.engine.interfaces.Dialect`, providing a
    consistent interface as well as caching support for previously
    fetched metadata.

    A :class:`_reflection.Inspector` object is usually created via the
    :func:`_sa.inspect` function, which may be passed an
    :class:`_engine.Engine`
    or a :class:`_engine.Connection`::

        from sqlalchemy import inspect, create_engine
        engine = create_engine('...')
        insp = inspect(engine)

    Where above, the :class:`~sqlalchemy.engine.interfaces.Dialect` associated
    with the engine may opt to return an :class:`_reflection.Inspector`
    subclass that
    provides additional methods specific to the dialect's target database.

    """
    bind: Engine | Connection
    engine: Engine
    dialect: Dialect
    info_cache: Dict[Any, Any]
    def __init__(self, bind: Engine | Connection) -> None:
        """Initialize a new :class:`_reflection.Inspector`.

        :param bind: a :class:`~sqlalchemy.engine.Connection`,
          which is typically an instance of
          :class:`~sqlalchemy.engine.Engine` or
          :class:`~sqlalchemy.engine.Connection`.

        For a dialect-specific instance of :class:`_reflection.Inspector`, see
        :meth:`_reflection.Inspector.from_engine`

        """
    def clear_cache(self) -> None:
        """reset the cache for this :class:`.Inspector`.

        Inspection methods that have data cached will emit SQL queries
        when next called to get new data.

        .. versionadded:: 2.0

        """
    @classmethod
    def from_engine(cls, bind: Engine) -> Inspector:
        """Construct a new dialect-specific Inspector object from the given
        engine or connection.

        :param bind: a :class:`~sqlalchemy.engine.Connection`
         or :class:`~sqlalchemy.engine.Engine`.

        This method differs from direct a direct constructor call of
        :class:`_reflection.Inspector` in that the
        :class:`~sqlalchemy.engine.interfaces.Dialect` is given a chance to
        provide a dialect-specific :class:`_reflection.Inspector` instance,
        which may
        provide additional methods.

        See the example at :class:`_reflection.Inspector`.

        """
    @property
    def default_schema_name(self) -> str | None:
        """Return the default schema name presented by the dialect
        for the current engine's database user.

        E.g. this is typically ``public`` for PostgreSQL and ``dbo``
        for SQL Server.

        """
    def get_schema_names(self, **kw: Any) -> List[str]:
        """Return all schema names.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.
        """
    def get_table_names(self, schema: str | None = None, **kw: Any) -> List[str]:
        """Return all table names within a particular schema.

        The names are expected to be real tables only, not views.
        Views are instead returned using the
        :meth:`_reflection.Inspector.get_view_names` and/or
        :meth:`_reflection.Inspector.get_materialized_view_names`
        methods.

        :param schema: Schema name. If ``schema`` is left at ``None``, the
         database's default schema is
         used, else the named schema is searched.  If the database does not
         support named schemas, behavior is undefined if ``schema`` is not
         passed as ``None``.  For special quoting, use :class:`.quoted_name`.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        .. seealso::

            :meth:`_reflection.Inspector.get_sorted_table_and_fkc_names`

            :attr:`_schema.MetaData.sorted_tables`

        """
    def has_table(self, table_name: str, schema: str | None = None, **kw: Any) -> bool:
        """Return True if the backend has a table, view, or temporary
        table of the given name.

        :param table_name: name of the table to check
        :param schema: schema name to query, if not the default schema.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        .. versionadded:: 1.4 - the :meth:`.Inspector.has_table` method
           replaces the :meth:`_engine.Engine.has_table` method.

        .. versionchanged:: 2.0:: :meth:`.Inspector.has_table` now formally
           supports checking for additional table-like objects:

           * any type of views (plain or materialized)
           * temporary tables of any kind

           Previously, these two checks were not formally specified and
           different dialects would vary in their behavior.   The dialect
           testing suite now includes tests for all of these object types
           and should be supported by all SQLAlchemy-included dialects.
           Support among third party dialects may be lagging, however.

        """
    def has_sequence(self, sequence_name: str, schema: str | None = None, **kw: Any) -> bool:
        """Return True if the backend has a sequence with the given name.

        :param sequence_name: name of the sequence to check
        :param schema: schema name to query, if not the default schema.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        .. versionadded:: 1.4

        """
    def has_index(self, table_name: str, index_name: str, schema: str | None = None, **kw: Any) -> bool:
        """Check the existence of a particular index name in the database.

        :param table_name: the name of the table the index belongs to
        :param index_name: the name of the index to check
        :param schema: schema name to query, if not the default schema.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        .. versionadded:: 2.0

        """
    def has_schema(self, schema_name: str, **kw: Any) -> bool:
        """Return True if the backend has a schema with the given name.

        :param schema_name: name of the schema to check
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        .. versionadded:: 2.0

        """
    def get_sorted_table_and_fkc_names(self, schema: str | None = None, **kw: Any) -> List[Tuple[str | None, List[Tuple[str, str | None]]]]:
        """Return dependency-sorted table and foreign key constraint names in
        referred to within a particular schema.

        This will yield 2-tuples of
        ``(tablename, [(tname, fkname), (tname, fkname), ...])``
        consisting of table names in CREATE order grouped with the foreign key
        constraint names that are not detected as belonging to a cycle.
        The final element
        will be ``(None, [(tname, fkname), (tname, fkname), ..])``
        which will consist of remaining
        foreign key constraint names that would require a separate CREATE
        step after-the-fact, based on dependencies between tables.

        :param schema: schema name to query, if not the default schema.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        .. seealso::

            :meth:`_reflection.Inspector.get_table_names`

            :func:`.sort_tables_and_constraints` - similar method which works
            with an already-given :class:`_schema.MetaData`.

        """
    def sort_tables_on_foreign_key_dependency(self, consider_schemas: Collection[str | None] = (None,), **kw: Any) -> List[Tuple[Tuple[str | None, str] | None, List[Tuple[Tuple[str | None, str], str | None]]]]:
        """Return dependency-sorted table and foreign key constraint names
        referred to within multiple schemas.

        This method may be compared to
        :meth:`.Inspector.get_sorted_table_and_fkc_names`, which
        works on one schema at a time; here, the method is a generalization
        that will consider multiple schemas at once including that it will
        resolve for cross-schema foreign keys.

        .. versionadded:: 2.0

        """
    def get_temp_table_names(self, **kw: Any) -> List[str]:
        """Return a list of temporary table names for the current bind.

        This method is unsupported by most dialects; currently
        only Oracle, PostgreSQL and SQLite implements it.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        """
    def get_temp_view_names(self, **kw: Any) -> List[str]:
        """Return a list of temporary view names for the current bind.

        This method is unsupported by most dialects; currently
        only PostgreSQL and SQLite implements it.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        """
    def get_table_options(self, table_name: str, schema: str | None = None, **kw: Any) -> Dict[str, Any]:
        """Return a dictionary of options specified when the table of the
        given name was created.

        This currently includes some options that apply to MySQL and Oracle
        tables.

        :param table_name: string name of the table.  For special quoting,
         use :class:`.quoted_name`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dict with the table options. The returned keys depend on the
         dialect in use. Each one is prefixed with the dialect name.

        .. seealso:: :meth:`Inspector.get_multi_table_options`

        """
    def get_multi_table_options(self, schema: str | None = None, filter_names: Sequence[str] | None = None, kind: ObjectKind = ..., scope: ObjectScope = ..., **kw: Any) -> Dict[TableKey, Dict[str, Any]]:
        """Return a dictionary of options specified when the tables in the
        given schema were created.

        The tables can be filtered by passing the names to use to
        ``filter_names``.

        This currently includes some options that apply to MySQL and Oracle
        tables.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param filter_names: optionally return information only for the
         objects listed here.

        :param kind: a :class:`.ObjectKind` that specifies the type of objects
         to reflect. Defaults to ``ObjectKind.TABLE``.

        :param scope: a :class:`.ObjectScope` that specifies if options of
         default, temporary or any tables should be reflected.
         Defaults to ``ObjectScope.DEFAULT``.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary where the keys are two-tuple schema,table-name
         and the values are dictionaries with the table options.
         The returned keys in each dict depend on the
         dialect in use. Each one is prefixed with the dialect name.
         The schema is ``None`` if no schema is provided.

        .. versionadded:: 2.0

        .. seealso:: :meth:`Inspector.get_table_options`
        """
    def get_view_names(self, schema: str | None = None, **kw: Any) -> List[str]:
        """Return all non-materialized view names in `schema`.

        :param schema: Optional, retrieve names from a non-default schema.
         For special quoting, use :class:`.quoted_name`.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.


        .. versionchanged:: 2.0  For those dialects that previously included
           the names of materialized views in this list (currently PostgreSQL),
           this method no longer returns the names of materialized views.
           the :meth:`.Inspector.get_materialized_view_names` method should
           be used instead.

        .. seealso::

            :meth:`.Inspector.get_materialized_view_names`

        """
    def get_materialized_view_names(self, schema: str | None = None, **kw: Any) -> List[str]:
        """Return all materialized view names in `schema`.

        :param schema: Optional, retrieve names from a non-default schema.
         For special quoting, use :class:`.quoted_name`.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        .. versionadded:: 2.0

        .. seealso::

            :meth:`.Inspector.get_view_names`

        """
    def get_sequence_names(self, schema: str | None = None, **kw: Any) -> List[str]:
        """Return all sequence names in `schema`.

        :param schema: Optional, retrieve names from a non-default schema.
         For special quoting, use :class:`.quoted_name`.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        """
    def get_view_definition(self, view_name: str, schema: str | None = None, **kw: Any) -> str:
        """Return definition for the plain or materialized view called
        ``view_name``.

        :param view_name: Name of the view.
        :param schema: Optional, retrieve names from a non-default schema.
         For special quoting, use :class:`.quoted_name`.
        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        """
    def get_columns(self, table_name: str, schema: str | None = None, **kw: Any) -> List[ReflectedColumn]:
        """Return information about columns in ``table_name``.

        Given a string ``table_name`` and an optional string ``schema``,
        return column information as a list of :class:`.ReflectedColumn`.

        :param table_name: string name of the table.  For special quoting,
         use :class:`.quoted_name`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: list of dictionaries, each representing the definition of
         a database column.

        .. seealso:: :meth:`Inspector.get_multi_columns`.

        """
    def get_multi_columns(self, schema: str | None = None, filter_names: Sequence[str] | None = None, kind: ObjectKind = ..., scope: ObjectScope = ..., **kw: Any) -> Dict[TableKey, List[ReflectedColumn]]:
        """Return information about columns in all objects in the given
        schema.

        The objects can be filtered by passing the names to use to
        ``filter_names``.

        For each table the value is a list of :class:`.ReflectedColumn`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param filter_names: optionally return information only for the
         objects listed here.

        :param kind: a :class:`.ObjectKind` that specifies the type of objects
         to reflect. Defaults to ``ObjectKind.TABLE``.

        :param scope: a :class:`.ObjectScope` that specifies if columns of
         default, temporary or any tables should be reflected.
         Defaults to ``ObjectScope.DEFAULT``.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary where the keys are two-tuple schema,table-name
         and the values are list of dictionaries, each representing the
         definition of a database column.
         The schema is ``None`` if no schema is provided.

        .. versionadded:: 2.0

        .. seealso:: :meth:`Inspector.get_columns`
        """
    def get_pk_constraint(self, table_name: str, schema: str | None = None, **kw: Any) -> ReflectedPrimaryKeyConstraint:
        """Return information about primary key constraint in ``table_name``.

        Given a string ``table_name``, and an optional string `schema`, return
        primary key information as a :class:`.ReflectedPrimaryKeyConstraint`.

        :param table_name: string name of the table.  For special quoting,
         use :class:`.quoted_name`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary representing the definition of
         a primary key constraint.

        .. seealso:: :meth:`Inspector.get_multi_pk_constraint`
        """
    def get_multi_pk_constraint(self, schema: str | None = None, filter_names: Sequence[str] | None = None, kind: ObjectKind = ..., scope: ObjectScope = ..., **kw: Any) -> Dict[TableKey, ReflectedPrimaryKeyConstraint]:
        """Return information about primary key constraints in
        all tables in the given schema.

        The tables can be filtered by passing the names to use to
        ``filter_names``.

        For each table the value is a :class:`.ReflectedPrimaryKeyConstraint`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param filter_names: optionally return information only for the
         objects listed here.

        :param kind: a :class:`.ObjectKind` that specifies the type of objects
         to reflect. Defaults to ``ObjectKind.TABLE``.

        :param scope: a :class:`.ObjectScope` that specifies if primary keys of
         default, temporary or any tables should be reflected.
         Defaults to ``ObjectScope.DEFAULT``.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary where the keys are two-tuple schema,table-name
         and the values are dictionaries, each representing the
         definition of a primary key constraint.
         The schema is ``None`` if no schema is provided.

        .. versionadded:: 2.0

        .. seealso:: :meth:`Inspector.get_pk_constraint`
        """
    def get_foreign_keys(self, table_name: str, schema: str | None = None, **kw: Any) -> List[ReflectedForeignKeyConstraint]:
        """Return information about foreign_keys in ``table_name``.

        Given a string ``table_name``, and an optional string `schema`, return
        foreign key information as a list of
        :class:`.ReflectedForeignKeyConstraint`.

        :param table_name: string name of the table.  For special quoting,
         use :class:`.quoted_name`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a list of dictionaries, each representing the
         a foreign key definition.

        .. seealso:: :meth:`Inspector.get_multi_foreign_keys`
        """
    def get_multi_foreign_keys(self, schema: str | None = None, filter_names: Sequence[str] | None = None, kind: ObjectKind = ..., scope: ObjectScope = ..., **kw: Any) -> Dict[TableKey, List[ReflectedForeignKeyConstraint]]:
        """Return information about foreign_keys in all tables
        in the given schema.

        The tables can be filtered by passing the names to use to
        ``filter_names``.

        For each table the value is a list of
        :class:`.ReflectedForeignKeyConstraint`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param filter_names: optionally return information only for the
         objects listed here.

        :param kind: a :class:`.ObjectKind` that specifies the type of objects
         to reflect. Defaults to ``ObjectKind.TABLE``.

        :param scope: a :class:`.ObjectScope` that specifies if foreign keys of
         default, temporary or any tables should be reflected.
         Defaults to ``ObjectScope.DEFAULT``.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary where the keys are two-tuple schema,table-name
         and the values are list of dictionaries, each representing
         a foreign key definition.
         The schema is ``None`` if no schema is provided.

        .. versionadded:: 2.0

        .. seealso:: :meth:`Inspector.get_foreign_keys`
        """
    def get_indexes(self, table_name: str, schema: str | None = None, **kw: Any) -> List[ReflectedIndex]:
        """Return information about indexes in ``table_name``.

        Given a string ``table_name`` and an optional string `schema`, return
        index information as a list of :class:`.ReflectedIndex`.

        :param table_name: string name of the table.  For special quoting,
         use :class:`.quoted_name`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a list of dictionaries, each representing the
         definition of an index.

        .. seealso:: :meth:`Inspector.get_multi_indexes`
        """
    def get_multi_indexes(self, schema: str | None = None, filter_names: Sequence[str] | None = None, kind: ObjectKind = ..., scope: ObjectScope = ..., **kw: Any) -> Dict[TableKey, List[ReflectedIndex]]:
        """Return information about indexes in in all objects
        in the given schema.

        The objects can be filtered by passing the names to use to
        ``filter_names``.

        For each table the value is a list of :class:`.ReflectedIndex`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param filter_names: optionally return information only for the
         objects listed here.

        :param kind: a :class:`.ObjectKind` that specifies the type of objects
         to reflect. Defaults to ``ObjectKind.TABLE``.

        :param scope: a :class:`.ObjectScope` that specifies if indexes of
         default, temporary or any tables should be reflected.
         Defaults to ``ObjectScope.DEFAULT``.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary where the keys are two-tuple schema,table-name
         and the values are list of dictionaries, each representing the
         definition of an index.
         The schema is ``None`` if no schema is provided.

        .. versionadded:: 2.0

        .. seealso:: :meth:`Inspector.get_indexes`
        """
    def get_unique_constraints(self, table_name: str, schema: str | None = None, **kw: Any) -> List[ReflectedUniqueConstraint]:
        """Return information about unique constraints in ``table_name``.

        Given a string ``table_name`` and an optional string `schema`, return
        unique constraint information as a list of
        :class:`.ReflectedUniqueConstraint`.

        :param table_name: string name of the table.  For special quoting,
         use :class:`.quoted_name`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a list of dictionaries, each representing the
         definition of an unique constraint.

        .. seealso:: :meth:`Inspector.get_multi_unique_constraints`
        """
    def get_multi_unique_constraints(self, schema: str | None = None, filter_names: Sequence[str] | None = None, kind: ObjectKind = ..., scope: ObjectScope = ..., **kw: Any) -> Dict[TableKey, List[ReflectedUniqueConstraint]]:
        """Return information about unique constraints in all tables
        in the given schema.

        The tables can be filtered by passing the names to use to
        ``filter_names``.

        For each table the value is a list of
        :class:`.ReflectedUniqueConstraint`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param filter_names: optionally return information only for the
         objects listed here.

        :param kind: a :class:`.ObjectKind` that specifies the type of objects
         to reflect. Defaults to ``ObjectKind.TABLE``.

        :param scope: a :class:`.ObjectScope` that specifies if constraints of
         default, temporary or any tables should be reflected.
         Defaults to ``ObjectScope.DEFAULT``.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary where the keys are two-tuple schema,table-name
         and the values are list of dictionaries, each representing the
         definition of an unique constraint.
         The schema is ``None`` if no schema is provided.

        .. versionadded:: 2.0

        .. seealso:: :meth:`Inspector.get_unique_constraints`
        """
    def get_table_comment(self, table_name: str, schema: str | None = None, **kw: Any) -> ReflectedTableComment:
        """Return information about the table comment for ``table_name``.

        Given a string ``table_name`` and an optional string ``schema``,
        return table comment information as a :class:`.ReflectedTableComment`.

        Raises ``NotImplementedError`` for a dialect that does not support
        comments.

        :param table_name: string name of the table.  For special quoting,
         use :class:`.quoted_name`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary, with the table comment.

        .. versionadded:: 1.2

        .. seealso:: :meth:`Inspector.get_multi_table_comment`
        """
    def get_multi_table_comment(self, schema: str | None = None, filter_names: Sequence[str] | None = None, kind: ObjectKind = ..., scope: ObjectScope = ..., **kw: Any) -> Dict[TableKey, ReflectedTableComment]:
        """Return information about the table comment in all objects
        in the given schema.

        The objects can be filtered by passing the names to use to
        ``filter_names``.

        For each table the value is a :class:`.ReflectedTableComment`.

        Raises ``NotImplementedError`` for a dialect that does not support
        comments.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param filter_names: optionally return information only for the
         objects listed here.

        :param kind: a :class:`.ObjectKind` that specifies the type of objects
         to reflect. Defaults to ``ObjectKind.TABLE``.

        :param scope: a :class:`.ObjectScope` that specifies if comments of
         default, temporary or any tables should be reflected.
         Defaults to ``ObjectScope.DEFAULT``.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary where the keys are two-tuple schema,table-name
         and the values are dictionaries, representing the
         table comments.
         The schema is ``None`` if no schema is provided.

        .. versionadded:: 2.0

        .. seealso:: :meth:`Inspector.get_table_comment`
        """
    def get_check_constraints(self, table_name: str, schema: str | None = None, **kw: Any) -> List[ReflectedCheckConstraint]:
        """Return information about check constraints in ``table_name``.

        Given a string ``table_name`` and an optional string `schema`, return
        check constraint information as a list of
        :class:`.ReflectedCheckConstraint`.

        :param table_name: string name of the table.  For special quoting,
         use :class:`.quoted_name`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a list of dictionaries, each representing the
         definition of a check constraints.

        .. seealso:: :meth:`Inspector.get_multi_check_constraints`
        """
    def get_multi_check_constraints(self, schema: str | None = None, filter_names: Sequence[str] | None = None, kind: ObjectKind = ..., scope: ObjectScope = ..., **kw: Any) -> Dict[TableKey, List[ReflectedCheckConstraint]]:
        """Return information about check constraints in all tables
        in the given schema.

        The tables can be filtered by passing the names to use to
        ``filter_names``.

        For each table the value is a list of
        :class:`.ReflectedCheckConstraint`.

        :param schema: string schema name; if omitted, uses the default schema
         of the database connection.  For special quoting,
         use :class:`.quoted_name`.

        :param filter_names: optionally return information only for the
         objects listed here.

        :param kind: a :class:`.ObjectKind` that specifies the type of objects
         to reflect. Defaults to ``ObjectKind.TABLE``.

        :param scope: a :class:`.ObjectScope` that specifies if constraints of
         default, temporary or any tables should be reflected.
         Defaults to ``ObjectScope.DEFAULT``.

        :param \\**kw: Additional keyword argument to pass to the dialect
         specific implementation. See the documentation of the dialect
         in use for more information.

        :return: a dictionary where the keys are two-tuple schema,table-name
         and the values are list of dictionaries, each representing the
         definition of a check constraints.
         The schema is ``None`` if no schema is provided.

        .. versionadded:: 2.0

        .. seealso:: :meth:`Inspector.get_check_constraints`
        """
    def reflect_table(self, table: sa_schema.Table, include_columns: Collection[str] | None, exclude_columns: Collection[str] = (), resolve_fks: bool = True, _extend_on: Set[sa_schema.Table] | None = None, _reflect_info: _ReflectionInfo | None = None) -> None:
        """Given a :class:`_schema.Table` object, load its internal
        constructs based on introspection.

        This is the underlying method used by most dialects to produce
        table reflection.  Direct usage is like::

            from sqlalchemy import create_engine, MetaData, Table
            from sqlalchemy import inspect

            engine = create_engine('...')
            meta = MetaData()
            user_table = Table('user', meta)
            insp = inspect(engine)
            insp.reflect_table(user_table, None)

        .. versionchanged:: 1.4 Renamed from ``reflecttable`` to
           ``reflect_table``

        :param table: a :class:`~sqlalchemy.schema.Table` instance.
        :param include_columns: a list of string column names to include
          in the reflection process.  If ``None``, all columns are reflected.

        """

class ReflectionDefaults:
    """provides blank default values for reflection methods."""
    @classmethod
    def columns(cls) -> List[ReflectedColumn]: ...
    @classmethod
    def pk_constraint(cls) -> ReflectedPrimaryKeyConstraint: ...
    @classmethod
    def foreign_keys(cls) -> List[ReflectedForeignKeyConstraint]: ...
    @classmethod
    def indexes(cls) -> List[ReflectedIndex]: ...
    @classmethod
    def unique_constraints(cls) -> List[ReflectedUniqueConstraint]: ...
    @classmethod
    def check_constraints(cls) -> List[ReflectedCheckConstraint]: ...
    @classmethod
    def table_options(cls) -> Dict[str, Any]: ...
    @classmethod
    def table_comment(cls) -> ReflectedTableComment: ...

@dataclass
class _ReflectionInfo:
    columns: Dict[TableKey, List[ReflectedColumn]]
    pk_constraint: Dict[TableKey, ReflectedPrimaryKeyConstraint | None]
    foreign_keys: Dict[TableKey, List[ReflectedForeignKeyConstraint]]
    indexes: Dict[TableKey, List[ReflectedIndex]]
    unique_constraints: Dict[TableKey, List[ReflectedUniqueConstraint]]
    table_comment: Dict[TableKey, ReflectedTableComment | None]
    check_constraints: Dict[TableKey, List[ReflectedCheckConstraint]]
    table_options: Dict[TableKey, Dict[str, Any]]
    unreflectable: Dict[TableKey, exc.UnreflectableTableError]
    def update(self, other: _ReflectionInfo) -> None: ...
    def __init__(self, columns, pk_constraint, foreign_keys, indexes, unique_constraints, table_comment, check_constraints, table_options, unreflectable) -> None: ...
