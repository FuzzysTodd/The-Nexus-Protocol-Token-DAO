from ... import schema as schema, util as util
from ...sql import coercions as coercions, elements as elements, roles as roles, sqltypes as sqltypes, type_api as type_api
from ...sql._typing import _TypeEngineArgument
from ...sql.base import _NoArg
from ...sql.ddl import InvokeCreateDDLBase as InvokeCreateDDLBase, InvokeDropDDLBase as InvokeDropDDLBase
from _typeshed import Incomplete
from typing import Any, Type

class NamedType(sqltypes.TypeEngine):
    """Base for named types."""
    __abstract__: bool
    DDLGenerator: Type[NamedTypeGenerator]
    DDLDropper: Type[NamedTypeDropper]
    create_type: bool
    def create(self, bind, checkfirst: bool = True, **kw) -> None:
        """Emit ``CREATE`` DDL for this type.

        :param bind: a connectable :class:`_engine.Engine`,
         :class:`_engine.Connection`, or similar object to emit
         SQL.
        :param checkfirst: if ``True``, a query against
         the PG catalog will be first performed to see
         if the type does not exist already before
         creating.

        """
    def drop(self, bind, checkfirst: bool = True, **kw) -> None:
        """Emit ``DROP`` DDL for this type.

        :param bind: a connectable :class:`_engine.Engine`,
         :class:`_engine.Connection`, or similar object to emit
         SQL.
        :param checkfirst: if ``True``, a query against
         the PG catalog will be first performed to see
         if the type actually exists before dropping.

        """

class NamedTypeGenerator(InvokeCreateDDLBase):
    checkfirst: Incomplete
    def __init__(self, dialect, connection, checkfirst: bool = False, **kwargs) -> None: ...

class NamedTypeDropper(InvokeDropDDLBase):
    checkfirst: Incomplete
    def __init__(self, dialect, connection, checkfirst: bool = False, **kwargs) -> None: ...

class EnumGenerator(NamedTypeGenerator):
    def visit_enum(self, enum) -> None: ...

class EnumDropper(NamedTypeDropper):
    def visit_enum(self, enum) -> None: ...

class ENUM(NamedType, type_api.NativeForEmulated, sqltypes.Enum):
    '''PostgreSQL ENUM type.

    This is a subclass of :class:`_types.Enum` which includes
    support for PG\'s ``CREATE TYPE`` and ``DROP TYPE``.

    When the builtin type :class:`_types.Enum` is used and the
    :paramref:`.Enum.native_enum` flag is left at its default of
    True, the PostgreSQL backend will use a :class:`_postgresql.ENUM`
    type as the implementation, so the special create/drop rules
    will be used.

    The create/drop behavior of ENUM is necessarily intricate, due to the
    awkward relationship the ENUM type has in relationship to the
    parent table, in that it may be "owned" by just a single table, or
    may be shared among many tables.

    When using :class:`_types.Enum` or :class:`_postgresql.ENUM`
    in an "inline" fashion, the ``CREATE TYPE`` and ``DROP TYPE`` is emitted
    corresponding to when the :meth:`_schema.Table.create` and
    :meth:`_schema.Table.drop`
    methods are called::

        table = Table(\'sometable\', metadata,
            Column(\'some_enum\', ENUM(\'a\', \'b\', \'c\', name=\'myenum\'))
        )

        table.create(engine)  # will emit CREATE ENUM and CREATE TABLE
        table.drop(engine)  # will emit DROP TABLE and DROP ENUM

    To use a common enumerated type between multiple tables, the best
    practice is to declare the :class:`_types.Enum` or
    :class:`_postgresql.ENUM` independently, and associate it with the
    :class:`_schema.MetaData` object itself::

        my_enum = ENUM(\'a\', \'b\', \'c\', name=\'myenum\', metadata=metadata)

        t1 = Table(\'sometable_one\', metadata,
            Column(\'some_enum\', myenum)
        )

        t2 = Table(\'sometable_two\', metadata,
            Column(\'some_enum\', myenum)
        )

    When this pattern is used, care must still be taken at the level
    of individual table creates.  Emitting CREATE TABLE without also
    specifying ``checkfirst=True`` will still cause issues::

        t1.create(engine) # will fail: no such type \'myenum\'

    If we specify ``checkfirst=True``, the individual table-level create
    operation will check for the ``ENUM`` and create if not exists::

        # will check if enum exists, and emit CREATE TYPE if not
        t1.create(engine, checkfirst=True)

    When using a metadata-level ENUM type, the type will always be created
    and dropped if either the metadata-wide create/drop is called::

        metadata.create_all(engine)  # will emit CREATE TYPE
        metadata.drop_all(engine)  # will emit DROP TYPE

    The type can also be created and dropped directly::

        my_enum.create(engine)
        my_enum.drop(engine)

    '''
    native_enum: bool
    DDLGenerator = EnumGenerator
    DDLDropper = EnumDropper
    create_type: Incomplete
    def __init__(self, *enums, name: str | _NoArg | None = ..., create_type: bool = True, **kw) -> None:
        """Construct an :class:`_postgresql.ENUM`.

        Arguments are the same as that of
        :class:`_types.Enum`, but also including
        the following parameters.

        :param create_type: Defaults to True.
         Indicates that ``CREATE TYPE`` should be
         emitted, after optionally checking for the
         presence of the type, when the parent
         table is being created; and additionally
         that ``DROP TYPE`` is called when the table
         is dropped.    When ``False``, no check
         will be performed and no ``CREATE TYPE``
         or ``DROP TYPE`` is emitted, unless
         :meth:`~.postgresql.ENUM.create`
         or :meth:`~.postgresql.ENUM.drop`
         are called directly.
         Setting to ``False`` is helpful
         when invoking a creation scheme to a SQL file
         without access to the actual database -
         the :meth:`~.postgresql.ENUM.create` and
         :meth:`~.postgresql.ENUM.drop` methods can
         be used to emit SQL to a target bind.

        """
    def coerce_compared_value(self, op, value): ...
    @classmethod
    def __test_init__(cls): ...
    @classmethod
    def adapt_emulated_to_native(cls, impl, **kw):
        """Produce a PostgreSQL native :class:`_postgresql.ENUM` from plain
        :class:`.Enum`.

        """
    def create(self, bind: Incomplete | None = None, checkfirst: bool = True) -> None:
        """Emit ``CREATE TYPE`` for this
        :class:`_postgresql.ENUM`.

        If the underlying dialect does not support
        PostgreSQL CREATE TYPE, no action is taken.

        :param bind: a connectable :class:`_engine.Engine`,
         :class:`_engine.Connection`, or similar object to emit
         SQL.
        :param checkfirst: if ``True``, a query against
         the PG catalog will be first performed to see
         if the type does not exist already before
         creating.

        """
    def drop(self, bind: Incomplete | None = None, checkfirst: bool = True) -> None:
        """Emit ``DROP TYPE`` for this
        :class:`_postgresql.ENUM`.

        If the underlying dialect does not support
        PostgreSQL DROP TYPE, no action is taken.

        :param bind: a connectable :class:`_engine.Engine`,
         :class:`_engine.Connection`, or similar object to emit
         SQL.
        :param checkfirst: if ``True``, a query against
         the PG catalog will be first performed to see
         if the type actually exists before dropping.

        """
    def get_dbapi_type(self, dbapi) -> None:
        """dont return dbapi.STRING for ENUM in PostgreSQL, since that's
        a different type"""

class DomainGenerator(NamedTypeGenerator):
    def visit_DOMAIN(self, domain) -> None: ...

class DomainDropper(NamedTypeDropper):
    def visit_DOMAIN(self, domain) -> None: ...

class DOMAIN(NamedType, sqltypes.SchemaType):
    '''Represent the DOMAIN PostgreSQL type.

    A domain is essentially a data type with optional constraints
    that restrict the allowed set of values. E.g.::

        PositiveInt = DOMAIN(
            "pos_int", Integer, check="VALUE > 0", not_null=True
        )

        UsPostalCode = DOMAIN(
            "us_postal_code",
            Text,
            check="VALUE ~ \'^\\d{5}$\' OR VALUE ~ \'^\\d{5}-\\d{4}$\'"
        )

    See the `PostgreSQL documentation`__ for additional details

    __ https://www.postgresql.org/docs/current/sql-createdomain.html

    .. versionadded:: 2.0

    '''
    DDLGenerator = DomainGenerator
    DDLDropper = DomainDropper
    __visit_name__: str
    data_type: Incomplete
    default: Incomplete
    collation: Incomplete
    constraint_name: Incomplete
    not_null: Incomplete
    check: Incomplete
    create_type: Incomplete
    def __init__(self, name: str, data_type: _TypeEngineArgument[Any], *, collation: str | None = None, default: str | elements.TextClause | None = None, constraint_name: str | None = None, not_null: bool | None = None, check: str | None = None, create_type: bool = True, **kw: Any) -> None:
        """
        Construct a DOMAIN.

        :param name: the name of the domain
        :param data_type: The underlying data type of the domain.
          This can include array specifiers.
        :param collation: An optional collation for the domain.
          If no collation is specified, the underlying data type's default
          collation is used. The underlying type must be collatable if
          ``collation`` is specified.
        :param default: The DEFAULT clause specifies a default value for
          columns of the domain data type. The default should be a string
          or a :func:`_expression.text` value.
          If no default value is specified, then the default value is
          the null value.
        :param constraint_name: An optional name for a constraint.
          If not specified, the backend generates a name.
        :param not_null: Values of this domain are prevented from being null.
          By default domain are allowed to be null. If not specified
          no nullability clause will be emitted.
        :param check: CHECK clause specify integrity constraint or test
          which values of the domain must satisfy. A constraint must be
          an expression producing a Boolean result that can use the key
          word VALUE to refer to the value being tested.
          Differently from PostgreSQL, only a single check clause is
          currently allowed in SQLAlchemy.
        :param schema: optional schema name
        :param metadata: optional :class:`_schema.MetaData` object which
         this :class:`_postgresql.DOMAIN` will be directly associated
        :param create_type: Defaults to True.
         Indicates that ``CREATE TYPE`` should be emitted, after optionally
         checking for the presence of the type, when the parent table is
         being created; and additionally that ``DROP TYPE`` is called
         when the table is dropped.

        """
    @classmethod
    def __test_init__(cls): ...

class CreateEnumType(schema._CreateDropBase):
    __visit_name__: str

class DropEnumType(schema._CreateDropBase):
    __visit_name__: str

class CreateDomainType(schema._CreateDropBase):
    """Represent a CREATE DOMAIN statement."""
    __visit_name__: str

class DropDomainType(schema._CreateDropBase):
    """Represent a DROP DOMAIN statement."""
    __visit_name__: str
