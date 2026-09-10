import datetime as dt
import decimal
import enum
from . import coercions as coercions, elements as elements, operators as operators, roles as roles, type_api as type_api
from .. import event as event, exc as exc, inspection as inspection, util as util
from ..engine import processors as processors
from ..engine.interfaces import Dialect as Dialect
from ..util import OrderedDict as OrderedDict, langhelpers as langhelpers
from ..util.typing import Literal as Literal, is_literal as is_literal, typing_get_args as typing_get_args
from ._typing import _ColumnExpressionArgument, _TypeEngineArgument
from .base import NO_ARG as NO_ARG, SchemaEventTarget as SchemaEventTarget
from .cache_key import HasCacheKey as HasCacheKey
from .elements import Slice as Slice, quoted_name as quoted_name
from .operators import OperatorType as OperatorType
from .schema import MetaData as MetaData
from .type_api import Emulated as Emulated, NativeForEmulated as NativeForEmulated, TypeDecorator as TypeDecorator, TypeEngine as TypeEngine, TypeEngineMixin as TypeEngineMixin, Variant as Variant, _BindProcessorType, _ComparatorFactory, _ResultProcessorType
from .visitors import InternalTraversal as InternalTraversal
from _typeshed import Incomplete
from typing import Any, Callable, List, Sequence, Tuple, Type, overload

class HasExpressionLookup(TypeEngineMixin):
    """Mixin expression adaptations based on lookup tables.

    These rules are currently used by the numeric, integer and date types
    which have detailed cross-expression coercion rules.

    """
    class Comparator(TypeEngine.Comparator[_CT]): ...
    comparator_factory: _ComparatorFactory[Any]

class Concatenable(TypeEngineMixin):
    """A mixin that marks a type as supporting 'concatenation',
    typically strings."""
    class Comparator(TypeEngine.Comparator[_T]): ...
    comparator_factory: _ComparatorFactory[Any]

class Indexable(TypeEngineMixin):
    """A mixin that marks a type as supporting indexing operations,
    such as array or JSON structures.

    """
    class Comparator(TypeEngine.Comparator[_T]):
        def __getitem__(self, index): ...
    comparator_factory: _ComparatorFactory[Any]

class String(Concatenable, TypeEngine[str]):
    """The base for all string and character types.

    In SQL, corresponds to VARCHAR.

    The `length` field is usually required when the `String` type is
    used within a CREATE TABLE statement, as VARCHAR requires a length
    on most databases.

    """
    __visit_name__: str
    length: Incomplete
    collation: Incomplete
    def __init__(self, length: int | None = None, collation: str | None = None) -> None:
        """
        Create a string-holding type.

        :param length: optional, a length for the column for use in
          DDL and CAST expressions.  May be safely omitted if no ``CREATE
          TABLE`` will be issued.  Certain databases may require a
          ``length`` for use in DDL, and will raise an exception when
          the ``CREATE TABLE`` DDL is issued if a ``VARCHAR``
          with no length is included.  Whether the value is
          interpreted as bytes or characters is database specific.

        :param collation: Optional, a column-level collation for
          use in DDL and CAST expressions.  Renders using the
          COLLATE keyword supported by SQLite, MySQL, and PostgreSQL.
          E.g.:

          .. sourcecode:: pycon+sql

            >>> from sqlalchemy import cast, select, String
            >>> print(select(cast('some string', String(collation='utf8'))))
            {printsql}SELECT CAST(:param_1 AS VARCHAR COLLATE utf8) AS anon_1

          .. note::

            In most cases, the :class:`.Unicode` or :class:`.UnicodeText`
            datatypes should be used for a :class:`_schema.Column` that expects
            to store non-ascii data. These datatypes will ensure that the
            correct types are used on the database.

        """
    def literal_processor(self, dialect): ...
    def bind_processor(self, dialect) -> None: ...
    def result_processor(self, dialect, coltype) -> None: ...
    @property
    def python_type(self): ...
    def get_dbapi_type(self, dbapi): ...

class Text(String):
    """A variably sized string type.

    In SQL, usually corresponds to CLOB or TEXT.  In general, TEXT objects
    do not have a length; while some databases will accept a length
    argument here, it will be rejected by others.

    """
    __visit_name__: str

class Unicode(String):
    """A variable length Unicode string type.

    The :class:`.Unicode` type is a :class:`.String` subclass that assumes
    input and output strings that may contain non-ASCII characters, and for
    some backends implies an underlying column type that is explicitly
    supporting of non-ASCII data, such as ``NVARCHAR`` on Oracle and SQL
    Server.  This will impact the output of ``CREATE TABLE`` statements and
    ``CAST`` functions at the dialect level.

    The character encoding used by the :class:`.Unicode` type that is used to
    transmit and receive data to the database is usually determined by the
    DBAPI itself. All modern DBAPIs accommodate non-ASCII strings but may have
    different methods of managing database encodings; if necessary, this
    encoding should be configured as detailed in the notes for the target DBAPI
    in the :ref:`dialect_toplevel` section.

    In modern SQLAlchemy, use of the :class:`.Unicode` datatype does not
    imply any encoding/decoding behavior within SQLAlchemy itself.  In Python
    3, all string objects are inherently Unicode capable, and SQLAlchemy
    does not produce bytestring objects nor does it accommodate a DBAPI that
    does not return Python Unicode objects in result sets for string values.

    .. warning:: Some database backends, particularly SQL Server with pyodbc,
       are known to have undesirable behaviors regarding data that is noted
       as being of ``NVARCHAR`` type as opposed to ``VARCHAR``, including
       datatype mismatch errors and non-use of indexes.  See the section
       on :meth:`.DialectEvents.do_setinputsizes` for background on working
       around unicode character issues for backends like SQL Server with
       pyodbc as well as cx_Oracle.

    .. seealso::

        :class:`.UnicodeText` - unlengthed textual counterpart
        to :class:`.Unicode`.

        :meth:`.DialectEvents.do_setinputsizes`


    """
    __visit_name__: str
    def __init__(self, length: Incomplete | None = None, **kwargs) -> None:
        """
        Create a :class:`.Unicode` object.

        Parameters are the same as that of :class:`.String`.

        """

class UnicodeText(Text):
    """An unbounded-length Unicode string type.

    See :class:`.Unicode` for details on the unicode
    behavior of this object.

    Like :class:`.Unicode`, usage the :class:`.UnicodeText` type implies a
    unicode-capable type being used on the backend, such as
    ``NCLOB``, ``NTEXT``.

    """
    __visit_name__: str
    def __init__(self, length: Incomplete | None = None, **kwargs) -> None:
        """
        Create a Unicode-converting Text type.

        Parameters are the same as that of :class:`_expression.TextClause`.

        """

class Integer(HasExpressionLookup, TypeEngine[int]):
    """A type for ``int`` integers."""
    __visit_name__: str
    def get_dbapi_type(self, dbapi): ...
    @property
    def python_type(self): ...
    def literal_processor(self, dialect): ...

class SmallInteger(Integer):
    """A type for smaller ``int`` integers.

    Typically generates a ``SMALLINT`` in DDL, and otherwise acts like
    a normal :class:`.Integer` on the Python side.

    """
    __visit_name__: str

class BigInteger(Integer):
    """A type for bigger ``int`` integers.

    Typically generates a ``BIGINT`` in DDL, and otherwise acts like
    a normal :class:`.Integer` on the Python side.

    """
    __visit_name__: str

class Numeric(HasExpressionLookup, TypeEngine[_N]):
    """Base for non-integer numeric types, such as
    ``NUMERIC``, ``FLOAT``, ``DECIMAL``, and other variants.

    The :class:`.Numeric` datatype when used directly will render DDL
    corresponding to precision numerics if available, such as
    ``NUMERIC(precision, scale)``.  The :class:`.Float` subclass will
    attempt to render a floating-point datatype such as ``FLOAT(precision)``.

    :class:`.Numeric` returns Python ``decimal.Decimal`` objects by default,
    based on the default value of ``True`` for the
    :paramref:`.Numeric.asdecimal` parameter.  If this parameter is set to
    False, returned values are coerced to Python ``float`` objects.

    The :class:`.Float` subtype, being more specific to floating point,
    defaults the :paramref:`.Float.asdecimal` flag to False so that the
    default Python datatype is ``float``.

    .. note::

        When using a :class:`.Numeric` datatype against a database type that
        returns Python floating point values to the driver, the accuracy of the
        decimal conversion indicated by :paramref:`.Numeric.asdecimal` may be
        limited.   The behavior of specific numeric/floating point datatypes
        is a product of the SQL datatype in use, the Python :term:`DBAPI`
        in use, as well as strategies that may be present within
        the SQLAlchemy dialect in use.   Users requiring specific precision/
        scale are encouraged to experiment with the available datatypes
        in order to determine the best results.

    """
    __visit_name__: str
    @overload
    def __init__(self, precision: int | None = ..., scale: int | None = ..., decimal_return_scale: int | None = ..., asdecimal: Literal[True] = ...) -> None: ...
    @overload
    def __init__(self, precision: int | None = ..., scale: int | None = ..., decimal_return_scale: int | None = ..., asdecimal: Literal[False] = ...) -> None: ...
    def get_dbapi_type(self, dbapi): ...
    def literal_processor(self, dialect): ...
    @property
    def python_type(self): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class Float(Numeric[_N]):
    """Type representing floating point types, such as ``FLOAT`` or ``REAL``.

    This type returns Python ``float`` objects by default, unless the
    :paramref:`.Float.asdecimal` flag is set to ``True``, in which case they
    are coerced to ``decimal.Decimal`` objects.

    When a :paramref:`.Float.precision` is not provided in a
    :class:`_types.Float` type some backend may compile this type as
    an 8 bytes / 64 bit float datatype. To use a 4 bytes / 32 bit float
    datatype a precision <= 24 can usually be provided or the
    :class:`_types.REAL` type can be used.
    This is known to be the case in the PostgreSQL and MSSQL dialects
    that render the type as ``FLOAT`` that's in both an alias of
    ``DOUBLE PRECISION``. Other third party dialects may have similar
    behavior.
    """
    __visit_name__: str
    scale: Incomplete
    @overload
    def __init__(self, precision: int | None = ..., asdecimal: Literal[False] = ..., decimal_return_scale: int | None = ...) -> None: ...
    @overload
    def __init__(self, precision: int | None = ..., asdecimal: Literal[True] = ..., decimal_return_scale: int | None = ...) -> None: ...
    def result_processor(self, dialect, coltype): ...

class Double(Float[_N]):
    """A type for double ``FLOAT`` floating point types.

    Typically generates a ``DOUBLE`` or ``DOUBLE_PRECISION`` in DDL,
    and otherwise acts like a normal :class:`.Float` on the Python
    side.

    .. versionadded:: 2.0

    """
    __visit_name__: str

class _RenderISO8601NoT: ...

class DateTime(_RenderISO8601NoT, HasExpressionLookup, TypeEngine[dt.datetime]):
    """A type for ``datetime.datetime()`` objects.

    Date and time types return objects from the Python ``datetime``
    module.  Most DBAPIs have built in support for the datetime
    module, with the noted exception of SQLite.  In the case of
    SQLite, date and time types are stored as strings which are then
    converted back to datetime objects when rows are returned.

    For the time representation within the datetime type, some
    backends include additional options, such as timezone support and
    fractional seconds support.  For fractional seconds, use the
    dialect-specific datatype, such as :class:`.mysql.TIME`.  For
    timezone support, use at least the :class:`_types.TIMESTAMP` datatype,
    if not the dialect-specific datatype object.

    """
    __visit_name__: str
    timezone: Incomplete
    def __init__(self, timezone: bool = False) -> None:
        """Construct a new :class:`.DateTime`.

        :param timezone: boolean.  Indicates that the datetime type should
         enable timezone support, if available on the
         **base date/time-holding type only**.   It is recommended
         to make use of the :class:`_types.TIMESTAMP` datatype directly when
         using this flag, as some databases include separate generic
         date/time-holding types distinct from the timezone-capable
         TIMESTAMP datatype, such as Oracle.


        """
    def get_dbapi_type(self, dbapi): ...
    def literal_processor(self, dialect): ...
    @property
    def python_type(self): ...

class Date(_RenderISO8601NoT, HasExpressionLookup, TypeEngine[dt.date]):
    """A type for ``datetime.date()`` objects."""
    __visit_name__: str
    def get_dbapi_type(self, dbapi): ...
    @property
    def python_type(self): ...
    def literal_processor(self, dialect): ...

class Time(_RenderISO8601NoT, HasExpressionLookup, TypeEngine[dt.time]):
    """A type for ``datetime.time()`` objects."""
    __visit_name__: str
    timezone: Incomplete
    def __init__(self, timezone: bool = False) -> None: ...
    def get_dbapi_type(self, dbapi): ...
    @property
    def python_type(self): ...
    def literal_processor(self, dialect): ...

class _Binary(TypeEngine[bytes]):
    """Define base behavior for binary types."""
    length: Incomplete
    def __init__(self, length: int | None = None) -> None: ...
    def literal_processor(self, dialect): ...
    @property
    def python_type(self): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...
    def coerce_compared_value(self, op, value):
        """See :meth:`.TypeEngine.coerce_compared_value` for a description."""
    def get_dbapi_type(self, dbapi): ...

class LargeBinary(_Binary):
    """A type for large binary byte data.

    The :class:`.LargeBinary` type corresponds to a large and/or unlengthed
    binary type for the target platform, such as BLOB on MySQL and BYTEA for
    PostgreSQL.  It also handles the necessary conversions for the DBAPI.

    """
    __visit_name__: str
    def __init__(self, length: int | None = None) -> None:
        """
        Construct a LargeBinary type.

        :param length: optional, a length for the column for use in
          DDL statements, for those binary types that accept a length,
          such as the MySQL BLOB type.

        """

class SchemaType(SchemaEventTarget, TypeEngineMixin):
    """Add capabilities to a type which allow for schema-level DDL to be
    associated with a type.

    Supports types that must be explicitly created/dropped (i.e. PG ENUM type)
    as well as types that are complimented by table or schema level
    constraints, triggers, and other rules.

    :class:`.SchemaType` classes can also be targets for the
    :meth:`.DDLEvents.before_parent_attach` and
    :meth:`.DDLEvents.after_parent_attach` events, where the events fire off
    surrounding the association of the type object with a parent
    :class:`_schema.Column`.

    .. seealso::

        :class:`.Enum`

        :class:`.Boolean`


    """
    name: str | None
    schema: Incomplete
    metadata: Incomplete
    inherit_schema: Incomplete
    dispatch: Incomplete
    def __init__(self, name: str | None = None, schema: str | None = None, metadata: MetaData | None = None, inherit_schema: bool = False, quote: bool | None = None, _create_events: bool = True, _adapted_from: SchemaType | None = None) -> None: ...
    def copy(self, **kw): ...
    @overload
    def adapt(self, cls: Type[_TE], **kw: Any) -> _TE: ...
    @overload
    def adapt(self, cls: Type[TypeEngineMixin], **kw: Any) -> TypeEngine[Any]: ...
    def create(self, bind, checkfirst: bool = False) -> None:
        """Issue CREATE DDL for this type, if applicable."""
    def drop(self, bind, checkfirst: bool = False) -> None:
        """Issue DROP DDL for this type, if applicable."""

class Enum(String, SchemaType, Emulated, TypeEngine[str | enum.Enum]):
    '''Generic Enum Type.

    The :class:`.Enum` type provides a set of possible string values
    which the column is constrained towards.

    The :class:`.Enum` type will make use of the backend\'s native "ENUM"
    type if one is available; otherwise, it uses a VARCHAR datatype.
    An option also exists to automatically produce a CHECK constraint
    when the VARCHAR (so called "non-native") variant is produced;
    see the  :paramref:`.Enum.create_constraint` flag.

    The :class:`.Enum` type also provides in-Python validation of string
    values during both read and write operations.  When reading a value
    from the database in a result set, the string value is always checked
    against the list of possible values and a ``LookupError`` is raised
    if no match is found.  When passing a value to the database as a
    plain string within a SQL statement, if the
    :paramref:`.Enum.validate_strings` parameter is
    set to True, a ``LookupError`` is raised for any string value that\'s
    not located in the given list of possible values; note that this
    impacts usage of LIKE expressions with enumerated values (an unusual
    use case).

    The source of enumerated values may be a list of string values, or
    alternatively a PEP-435-compliant enumerated class.  For the purposes
    of the :class:`.Enum` datatype, this class need only provide a
    ``__members__`` method.

    When using an enumerated class, the enumerated objects are used
    both for input and output, rather than strings as is the case with
    a plain-string enumerated type::

        import enum
        from sqlalchemy import Enum

        class MyEnum(enum.Enum):
            one = 1
            two = 2
            three = 3

        t = Table(
            \'data\', MetaData(),
            Column(\'value\', Enum(MyEnum))
        )

        connection.execute(t.insert(), {"value": MyEnum.two})
        assert connection.scalar(t.select()) is MyEnum.two

    Above, the string names of each element, e.g. "one", "two", "three",
    are persisted to the database; the values of the Python Enum, here
    indicated as integers, are **not** used; the value of each enum can
    therefore be any kind of Python object whether or not it is persistable.

    In order to persist the values and not the names, the
    :paramref:`.Enum.values_callable` parameter may be used.   The value of
    this parameter is a user-supplied callable, which  is intended to be used
    with a PEP-435-compliant enumerated class and  returns a list of string
    values to be persisted.   For a simple enumeration that uses string values,
    a callable such as  ``lambda x: [e.value for e in x]`` is sufficient.

    .. seealso::

        :ref:`orm_declarative_mapped_column_enums` - background on using
        the :class:`_sqltypes.Enum` datatype with the ORM\'s
        :ref:`ORM Annotated Declarative <orm_declarative_mapped_column>`
        feature.

        :class:`_postgresql.ENUM` - PostgreSQL-specific type,
        which has additional functionality.

        :class:`.mysql.ENUM` - MySQL-specific type

    '''
    __visit_name__: str
    def __init__(self, *enums: object, **kw: Any) -> None:
        '''Construct an enum.

        Keyword arguments which don\'t apply to a specific backend are ignored
        by that backend.

        :param \\*enums: either exactly one PEP-435 compliant enumerated type
           or one or more string labels.

        :param create_constraint: defaults to False.  When creating a
           non-native enumerated type, also build a CHECK constraint on the
           database against the valid values.

           .. note:: it is strongly recommended that the CHECK constraint
              have an explicit name in order to support schema-management
              concerns.  This can be established either by setting the
              :paramref:`.Enum.name` parameter or by setting up an
              appropriate naming convention; see
              :ref:`constraint_naming_conventions` for background.

           .. versionchanged:: 1.4 - this flag now defaults to False, meaning
              no CHECK constraint is generated for a non-native enumerated
              type.

        :param metadata: Associate this type directly with a ``MetaData``
           object. For types that exist on the target database as an
           independent schema construct (PostgreSQL), this type will be
           created and dropped within ``create_all()`` and ``drop_all()``
           operations. If the type is not associated with any ``MetaData``
           object, it will associate itself with each ``Table`` in which it is
           used, and will be created when any of those individual tables are
           created, after a check is performed for its existence. The type is
           only dropped when ``drop_all()`` is called for that ``Table``
           object\'s metadata, however.

           The value of the :paramref:`_schema.MetaData.schema` parameter of
           the :class:`_schema.MetaData` object, if set, will be used as the
           default value of the :paramref:`_types.Enum.schema` on this object
           if an explicit value is not otherwise supplied.

           .. versionchanged:: 1.4.12 :class:`_types.Enum` inherits the
              :paramref:`_schema.MetaData.schema` parameter of the
              :class:`_schema.MetaData` object if present, when passed using
              the :paramref:`_types.Enum.metadata` parameter.

        :param name: The name of this type. This is required for PostgreSQL
           and any future supported database which requires an explicitly
           named type, or an explicitly named constraint in order to generate
           the type and/or a table that uses it. If a PEP-435 enumerated
           class was used, its name (converted to lower case) is used by
           default.

        :param native_enum: Use the database\'s native ENUM type when
           available. Defaults to True. When False, uses VARCHAR + check
           constraint for all backends. When False, the VARCHAR length can be
           controlled with :paramref:`.Enum.length`; currently "length" is
           ignored if native_enum=True.

        :param length: Allows specifying a custom length for the VARCHAR
           when a non-native enumeration datatype is used.  By default it uses
           the length of the longest value.

           .. versionchanged:: 2.0.0 The :paramref:`.Enum.length` parameter
              is used unconditionally for ``VARCHAR`` rendering regardless of
              the :paramref:`.Enum.native_enum` parameter, for those backends
              where ``VARCHAR`` is used for enumerated datatypes.


        :param schema: Schema name of this type. For types that exist on the
           target database as an independent schema construct (PostgreSQL),
           this parameter specifies the named schema in which the type is
           present.

           If not present, the schema name will be taken from the
           :class:`_schema.MetaData` collection if passed as
           :paramref:`_types.Enum.metadata`, for a :class:`_schema.MetaData`
           that includes the :paramref:`_schema.MetaData.schema` parameter.

           .. versionchanged:: 1.4.12 :class:`_types.Enum` inherits the
              :paramref:`_schema.MetaData.schema` parameter of the
              :class:`_schema.MetaData` object if present, when passed using
              the :paramref:`_types.Enum.metadata` parameter.

           Otherwise, if the :paramref:`_types.Enum.inherit_schema` flag is set
           to ``True``, the schema will be inherited from the associated
           :class:`_schema.Table` object if any; when
           :paramref:`_types.Enum.inherit_schema` is at its default of
           ``False``, the owning table\'s schema is **not** used.


        :param quote: Set explicit quoting preferences for the type\'s name.

        :param inherit_schema: When ``True``, the "schema" from the owning
           :class:`_schema.Table`
           will be copied to the "schema" attribute of this
           :class:`.Enum`, replacing whatever value was passed for the
           ``schema`` attribute.   This also takes effect when using the
           :meth:`_schema.Table.to_metadata` operation.

        :param validate_strings: when True, string values that are being
           passed to the database in a SQL statement will be checked
           for validity against the list of enumerated values.  Unrecognized
           values will result in a ``LookupError`` being raised.

        :param values_callable: A callable which will be passed the PEP-435
           compliant enumerated type, which should then return a list of string
           values to be persisted. This allows for alternate usages such as
           using the string value of an enum to be persisted to the database
           instead of its name. The callable must return the values to be
           persisted in the same order as iterating through the Enum\'s
           ``__member__`` attribute. For example
           ``lambda x: [i.value for i in x]``.

           .. versionadded:: 1.2.3

        :param sort_key_function: a Python callable which may be used as the
           "key" argument in the Python ``sorted()`` built-in.   The SQLAlchemy
           ORM requires that primary key columns which are mapped must
           be sortable in some way.  When using an unsortable enumeration
           object such as a Python 3 ``Enum`` object, this parameter may be
           used to set a default sort key function for the objects.  By
           default, the database value of the enumeration is used as the
           sorting function.

           .. versionadded:: 1.3.8

        :param omit_aliases: A boolean that when true will remove aliases from
           pep 435 enums. defaults to ``True``.

           .. versionchanged:: 2.0 This parameter now defaults to True.

        '''
    @property
    def sort_key_function(self): ...
    @property
    def native(self): ...
    class Comparator(String.Comparator[str]):
        type: String
    comparator_factory = Comparator
    def as_generic(self, allow_nulltype: bool = False): ...
    def adapt_to_emulated(self, impltype, **kw): ...
    def adapt(self, impltype, **kw): ...
    def literal_processor(self, dialect): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...
    def copy(self, **kw): ...
    @property
    def python_type(self): ...

class PickleType(TypeDecorator[object]):
    """Holds Python objects, which are serialized using pickle.

    PickleType builds upon the Binary type to apply Python's
    ``pickle.dumps()`` to incoming objects, and ``pickle.loads()`` on
    the way out, allowing any pickleable Python object to be stored as
    a serialized binary field.

    To allow ORM change events to propagate for elements associated
    with :class:`.PickleType`, see :ref:`mutable_toplevel`.

    """
    impl = LargeBinary
    cache_ok: bool
    protocol: Incomplete
    pickler: Incomplete
    comparator: Incomplete
    def __init__(self, protocol: int = ..., pickler: Any = None, comparator: Callable[[Any, Any], bool] | None = None, impl: _TypeEngineArgument[Any] | None = None) -> None:
        '''
        Construct a PickleType.

        :param protocol: defaults to ``pickle.HIGHEST_PROTOCOL``.

        :param pickler: defaults to pickle.  May be any object with
          pickle-compatible ``dumps`` and ``loads`` methods.

        :param comparator: a 2-arg callable predicate used
          to compare values of this type.  If left as ``None``,
          the Python "equals" operator is used to compare values.

        :param impl: A binary-storing :class:`_types.TypeEngine` class or
          instance to use in place of the default :class:`_types.LargeBinary`.
          For example the :class: `_mysql.LONGBLOB` class may be more effective
          when using MySQL.

          .. versionadded:: 1.4.20

        '''
    def __reduce__(self): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...
    def compare_values(self, x, y): ...

class Boolean(SchemaType, Emulated, TypeEngine[bool]):
    '''A bool datatype.

    :class:`.Boolean` typically uses BOOLEAN or SMALLINT on the DDL side,
    and on the Python side deals in ``True`` or ``False``.

    The :class:`.Boolean` datatype currently has two levels of assertion
    that the values persisted are simple true/false values.  For all
    backends, only the Python values ``None``, ``True``, ``False``, ``1``
    or ``0`` are accepted as parameter values.   For those backends that
    don\'t support a "native boolean" datatype, an option exists to
    also create a CHECK constraint on the target column

    .. versionchanged:: 1.2 the :class:`.Boolean` datatype now asserts that
       incoming Python values are already in pure boolean form.


    '''
    __visit_name__: str
    native: bool
    create_constraint: Incomplete
    name: Incomplete
    dispatch: Incomplete
    def __init__(self, create_constraint: bool = False, name: str | None = None, _create_events: bool = True, _adapted_from: SchemaType | None = None) -> None:
        """Construct a Boolean.

        :param create_constraint: defaults to False.  If the boolean
          is generated as an int/smallint, also create a CHECK constraint
          on the table that ensures 1 or 0 as a value.

          .. note:: it is strongly recommended that the CHECK constraint
             have an explicit name in order to support schema-management
             concerns.  This can be established either by setting the
             :paramref:`.Boolean.name` parameter or by setting up an
             appropriate naming convention; see
             :ref:`constraint_naming_conventions` for background.

          .. versionchanged:: 1.4 - this flag now defaults to False, meaning
             no CHECK constraint is generated for a non-native enumerated
             type.

        :param name: if a CHECK constraint is generated, specify
          the name of the constraint.

        """
    @property
    def python_type(self): ...
    def literal_processor(self, dialect): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class _AbstractInterval(HasExpressionLookup, TypeEngine[dt.timedelta]): ...

class Interval(Emulated, _AbstractInterval, TypeDecorator[dt.timedelta]):
    '''A type for ``datetime.timedelta()`` objects.

    The Interval type deals with ``datetime.timedelta`` objects.  In
    PostgreSQL, the native ``INTERVAL`` type is used; for others, the
    value is stored as a date which is relative to the "epoch"
    (Jan. 1, 1970).

    Note that the ``Interval`` type does not currently provide date arithmetic
    operations on platforms which do not support interval types natively. Such
    operations usually require transformation of both sides of the expression
    (such as, conversion of both sides into integer epoch values first) which
    currently is a manual procedure (such as via
    :attr:`~sqlalchemy.sql.expression.func`).

    '''
    impl = DateTime
    epoch: Incomplete
    cache_ok: bool
    native: Incomplete
    second_precision: Incomplete
    day_precision: Incomplete
    def __init__(self, native: bool = True, second_precision: int | None = None, day_precision: int | None = None) -> None:
        '''Construct an Interval object.

        :param native: when True, use the actual
          INTERVAL type provided by the database, if
          supported (currently PostgreSQL, Oracle).
          Otherwise, represent the interval data as
          an epoch value regardless.

        :param second_precision: For native interval types
          which support a "fractional seconds precision" parameter,
          i.e. Oracle and PostgreSQL

        :param day_precision: for native interval types which
          support a "day precision" parameter, i.e. Oracle.

        '''
    class Comparator(TypeDecorator.Comparator[_CT], _AbstractInterval.Comparator[_CT]): ...
    comparator_factory = Comparator
    @property
    def python_type(self): ...
    def adapt_to_emulated(self, impltype, **kw): ...
    def coerce_compared_value(self, op, value): ...
    def bind_processor(self, dialect: Dialect) -> _BindProcessorType[dt.timedelta]: ...
    def result_processor(self, dialect: Dialect, coltype: Any) -> _ResultProcessorType[dt.timedelta]: ...

class JSON(Indexable, TypeEngine[Any]):
    '''Represent a SQL JSON type.

    .. note::  :class:`_types.JSON`
       is provided as a facade for vendor-specific
       JSON types.  Since it supports JSON SQL operations, it only
       works on backends that have an actual JSON type, currently:

       * PostgreSQL - see :class:`sqlalchemy.dialects.postgresql.JSON` and
         :class:`sqlalchemy.dialects.postgresql.JSONB` for backend-specific
         notes

       * MySQL - see
         :class:`sqlalchemy.dialects.mysql.JSON` for backend-specific notes

       * SQLite as of version 3.9 - see
         :class:`sqlalchemy.dialects.sqlite.JSON` for backend-specific notes

       * Microsoft SQL Server 2016 and later - see
         :class:`sqlalchemy.dialects.mssql.JSON` for backend-specific notes

    :class:`_types.JSON` is part of the Core in support of the growing
    popularity of native JSON datatypes.

    The :class:`_types.JSON` type stores arbitrary JSON format data, e.g.::

        data_table = Table(\'data_table\', metadata,
            Column(\'id\', Integer, primary_key=True),
            Column(\'data\', JSON)
        )

        with engine.connect() as conn:
            conn.execute(
                data_table.insert(),
                {"data": {"key1": "value1", "key2": "value2"}}
            )

    **JSON-Specific Expression Operators**

    The :class:`_types.JSON`
    datatype provides these additional SQL operations:

    * Keyed index operations::

        data_table.c.data[\'some key\']

    * Integer index operations::

        data_table.c.data[3]

    * Path index operations::

        data_table.c.data[(\'key_1\', \'key_2\', 5, ..., \'key_n\')]

    * Data casters for specific JSON element types, subsequent to an index
      or path operation being invoked::

        data_table.c.data["some key"].as_integer()

      .. versionadded:: 1.3.11

    Additional operations may be available from the dialect-specific versions
    of :class:`_types.JSON`, such as
    :class:`sqlalchemy.dialects.postgresql.JSON` and
    :class:`sqlalchemy.dialects.postgresql.JSONB` which both offer additional
    PostgreSQL-specific operations.

    **Casting JSON Elements to Other Types**

    Index operations, i.e. those invoked by calling upon the expression using
    the Python bracket operator as in ``some_column[\'some key\']``, return an
    expression object whose type defaults to :class:`_types.JSON` by default,
    so that
    further JSON-oriented instructions may be called upon the result type.
    However, it is likely more common that an index operation is expected
    to return a specific scalar element, such as a string or integer.  In
    order to provide access to these elements in a backend-agnostic way,
    a series of data casters are provided:

    * :meth:`.JSON.Comparator.as_string` - return the element as a string

    * :meth:`.JSON.Comparator.as_boolean` - return the element as a boolean

    * :meth:`.JSON.Comparator.as_float` - return the element as a float

    * :meth:`.JSON.Comparator.as_integer` - return the element as an integer

    These data casters are implemented by supporting dialects in order to
    assure that comparisons to the above types will work as expected, such as::

        # integer comparison
        data_table.c.data["some_integer_key"].as_integer() == 5

        # boolean comparison
        data_table.c.data["some_boolean"].as_boolean() == True

    .. versionadded:: 1.3.11 Added type-specific casters for the basic JSON
       data element types.

    .. note::

        The data caster functions are new in version 1.3.11, and supersede
        the previous documented approaches of using CAST; for reference,
        this looked like::

           from sqlalchemy import cast, type_coerce
           from sqlalchemy import String, JSON
           cast(
               data_table.c.data[\'some_key\'], String
           ) == type_coerce(55, JSON)

        The above case now works directly as::

            data_table.c.data[\'some_key\'].as_integer() == 5

        For details on the previous comparison approach within the 1.3.x
        series, see the documentation for SQLAlchemy 1.2 or the included HTML
        files in the doc/ directory of the version\'s distribution.

    **Detecting Changes in JSON columns when using the ORM**

    The :class:`_types.JSON` type, when used with the SQLAlchemy ORM, does not
    detect in-place mutations to the structure.  In order to detect these, the
    :mod:`sqlalchemy.ext.mutable` extension must be used, most typically
    using the :class:`.MutableDict` class.  This extension will
    allow "in-place" changes to the datastructure to produce events which
    will be detected by the unit of work.  See the example at :class:`.HSTORE`
    for a simple example involving a dictionary.

    Alternatively, assigning a JSON structure to an ORM element that
    replaces the old one will always trigger a change event.

    **Support for JSON null vs. SQL NULL**

    When working with NULL values, the :class:`_types.JSON` type recommends the
    use of two specific constants in order to differentiate between a column
    that evaluates to SQL NULL, e.g. no value, vs. the JSON-encoded string of
    ``"null"``. To insert or select against a value that is SQL NULL, use the
    constant :func:`.null`. This symbol may be passed as a parameter value
    specifically when using the :class:`_types.JSON` datatype, which contains
    special logic that interprets this symbol to mean that the column value
    should be SQL NULL as opposed to JSON ``"null"``::

        from sqlalchemy import null
        conn.execute(table.insert(), {"json_value": null()})

    To insert or select against a value that is JSON ``"null"``, use the
    constant :attr:`_types.JSON.NULL`::

        conn.execute(table.insert(), {"json_value": JSON.NULL})

    The :class:`_types.JSON` type supports a flag
    :paramref:`_types.JSON.none_as_null` which when set to True will result
    in the Python constant ``None`` evaluating to the value of SQL
    NULL, and when set to False results in the Python constant
    ``None`` evaluating to the value of JSON ``"null"``.    The Python
    value ``None`` may be used in conjunction with either
    :attr:`_types.JSON.NULL` and :func:`.null` in order to indicate NULL
    values, but care must be taken as to the value of the
    :paramref:`_types.JSON.none_as_null` in these cases.

    **Customizing the JSON Serializer**

    The JSON serializer and deserializer used by :class:`_types.JSON`
    defaults to
    Python\'s ``json.dumps`` and ``json.loads`` functions; in the case of the
    psycopg2 dialect, psycopg2 may be using its own custom loader function.

    In order to affect the serializer / deserializer, they are currently
    configurable at the :func:`_sa.create_engine` level via the
    :paramref:`_sa.create_engine.json_serializer` and
    :paramref:`_sa.create_engine.json_deserializer` parameters.  For example,
    to turn off ``ensure_ascii``::

        engine = create_engine(
            "sqlite://",
            json_serializer=lambda obj: json.dumps(obj, ensure_ascii=False))

    .. versionchanged:: 1.3.7

        SQLite dialect\'s ``json_serializer`` and ``json_deserializer``
        parameters renamed from ``_json_serializer`` and
        ``_json_deserializer``.

    .. seealso::

        :class:`sqlalchemy.dialects.postgresql.JSON`

        :class:`sqlalchemy.dialects.postgresql.JSONB`

        :class:`sqlalchemy.dialects.mysql.JSON`

        :class:`sqlalchemy.dialects.sqlite.JSON`

    '''
    __visit_name__: str
    hashable: bool
    NULL: Incomplete
    none_as_null: Incomplete
    def __init__(self, none_as_null: bool = False) -> None:
        '''Construct a :class:`_types.JSON` type.

        :param none_as_null=False: if True, persist the value ``None`` as a
         SQL NULL value, not the JSON encoding of ``null``. Note that when this
         flag is False, the :func:`.null` construct can still be used to
         persist a NULL value, which may be passed directly as a parameter
         value that is specially interpreted by the :class:`_types.JSON` type
         as SQL NULL::

             from sqlalchemy import null
             conn.execute(table.insert(), {"data": null()})

         .. note::

              :paramref:`_types.JSON.none_as_null` does **not** apply to the
              values passed to :paramref:`_schema.Column.default` and
              :paramref:`_schema.Column.server_default`; a value of ``None``
              passed for these parameters means "no default present".

              Additionally, when used in SQL comparison expressions, the
              Python value ``None`` continues to refer to SQL null, and not
              JSON NULL.  The :paramref:`_types.JSON.none_as_null` flag refers
              explicitly to the **persistence** of the value within an
              INSERT or UPDATE statement.   The :attr:`_types.JSON.NULL`
              value should be used for SQL expressions that wish to compare to
              JSON null.

         .. seealso::

              :attr:`.types.JSON.NULL`

        '''
    class JSONElementType(TypeEngine[Any]):
        """Common function for index / path elements in a JSON expression."""
        def string_bind_processor(self, dialect): ...
        def string_literal_processor(self, dialect): ...
        def bind_processor(self, dialect): ...
        def literal_processor(self, dialect): ...
    class JSONIndexType(JSONElementType):
        """Placeholder for the datatype of a JSON index value.

        This allows execution-time processing of JSON index values
        for special syntaxes.

        """
    class JSONIntIndexType(JSONIndexType):
        """Placeholder for the datatype of a JSON index value.

        This allows execution-time processing of JSON index values
        for special syntaxes.

        """
    class JSONStrIndexType(JSONIndexType):
        """Placeholder for the datatype of a JSON index value.

        This allows execution-time processing of JSON index values
        for special syntaxes.

        """
    class JSONPathType(JSONElementType):
        """Placeholder type for JSON path operations.

        This allows execution-time processing of a path-based
        index value into a specific SQL syntax.

        """
        __visit_name__: str
    class Comparator(Indexable.Comparator[_T], Concatenable.Comparator[_T]):
        """Define comparison operations for :class:`_types.JSON`."""
        def as_boolean(self):
            """Cast an indexed value as boolean.

            e.g.::

                stmt = select(
                    mytable.c.json_column['some_data'].as_boolean()
                ).where(
                    mytable.c.json_column['some_data'].as_boolean() == True
                )

            .. versionadded:: 1.3.11

            """
        def as_string(self):
            """Cast an indexed value as string.

            e.g.::

                stmt = select(
                    mytable.c.json_column['some_data'].as_string()
                ).where(
                    mytable.c.json_column['some_data'].as_string() ==
                    'some string'
                )

            .. versionadded:: 1.3.11

            """
        def as_integer(self):
            """Cast an indexed value as integer.

            e.g.::

                stmt = select(
                    mytable.c.json_column['some_data'].as_integer()
                ).where(
                    mytable.c.json_column['some_data'].as_integer() == 5
                )

            .. versionadded:: 1.3.11

            """
        def as_float(self):
            """Cast an indexed value as float.

            e.g.::

                stmt = select(
                    mytable.c.json_column['some_data'].as_float()
                ).where(
                    mytable.c.json_column['some_data'].as_float() == 29.75
                )

            .. versionadded:: 1.3.11

            """
        def as_numeric(self, precision, scale, asdecimal: bool = True):
            """Cast an indexed value as numeric/decimal.

            e.g.::

                stmt = select(
                    mytable.c.json_column['some_data'].as_numeric(10, 6)
                ).where(
                    mytable.c.
                    json_column['some_data'].as_numeric(10, 6) == 29.75
                )

            .. versionadded:: 1.4.0b2

            """
        def as_json(self):
            """Cast an indexed value as JSON.

            e.g.::

                stmt = select(mytable.c.json_column['some_data'].as_json())

            This is typically the default behavior of indexed elements in any
            case.

            Note that comparison of full JSON structures may not be
            supported by all backends.

            .. versionadded:: 1.3.11

            """
    comparator_factory = Comparator
    @property
    def python_type(self): ...
    @property
    def should_evaluate_none(self):
        """Alias of :attr:`_types.JSON.none_as_null`"""
    @should_evaluate_none.setter
    def should_evaluate_none(self, value) -> None: ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class ARRAY(SchemaEventTarget, Indexable, Concatenable, TypeEngine[Sequence[Any]]):
    '''Represent a SQL Array type.

    .. note::  This type serves as the basis for all ARRAY operations.
       However, currently **only the PostgreSQL backend has support for SQL
       arrays in SQLAlchemy**. It is recommended to use the PostgreSQL-specific
       :class:`sqlalchemy.dialects.postgresql.ARRAY` type directly when using
       ARRAY types with PostgreSQL, as it provides additional operators
       specific to that backend.

    :class:`_types.ARRAY` is part of the Core in support of various SQL
    standard functions such as :class:`_functions.array_agg`
    which explicitly involve
    arrays; however, with the exception of the PostgreSQL backend and possibly
    some third-party dialects, no other SQLAlchemy built-in dialect has support
    for this type.

    An :class:`_types.ARRAY` type is constructed given the "type"
    of element::

        mytable = Table("mytable", metadata,
                Column("data", ARRAY(Integer))
            )

    The above type represents an N-dimensional array,
    meaning a supporting backend such as PostgreSQL will interpret values
    with any number of dimensions automatically.   To produce an INSERT
    construct that passes in a 1-dimensional array of integers::

        connection.execute(
                mytable.insert(),
                {"data": [1,2,3]}
        )

    The :class:`_types.ARRAY` type can be constructed given a fixed number
    of dimensions::

        mytable = Table("mytable", metadata,
                Column("data", ARRAY(Integer, dimensions=2))
            )

    Sending a number of dimensions is optional, but recommended if the
    datatype is to represent arrays of more than one dimension.  This number
    is used:

    * When emitting the type declaration itself to the database, e.g.
      ``INTEGER[][]``

    * When translating Python values to database values, and vice versa, e.g.
      an ARRAY of :class:`.Unicode` objects uses this number to efficiently
      access the string values inside of array structures without resorting
      to per-row type inspection

    * When used with the Python ``getitem`` accessor, the number of dimensions
      serves to define the kind of type that the ``[]`` operator should
      return, e.g. for an ARRAY of INTEGER with two dimensions::

          >>> expr = table.c.column[5]  # returns ARRAY(Integer, dimensions=1)
          >>> expr = expr[6]  # returns Integer

    For 1-dimensional arrays, an :class:`_types.ARRAY` instance with no
    dimension parameter will generally assume single-dimensional behaviors.

    SQL expressions of type :class:`_types.ARRAY` have support for "index" and
    "slice" behavior.  The Python ``[]`` operator works normally here, given
    integer indexes or slices.  Arrays default to 1-based indexing.
    The operator produces binary expression
    constructs which will produce the appropriate SQL, both for
    SELECT statements::

        select(mytable.c.data[5], mytable.c.data[2:7])

    as well as UPDATE statements when the :meth:`_expression.Update.values`
    method
    is used::

        mytable.update().values({
            mytable.c.data[5]: 7,
            mytable.c.data[2:7]: [1, 2, 3]
        })

    The :class:`_types.ARRAY` type also provides for the operators
    :meth:`.types.ARRAY.Comparator.any` and
    :meth:`.types.ARRAY.Comparator.all`. The PostgreSQL-specific version of
    :class:`_types.ARRAY` also provides additional operators.

    .. container:: topic

        **Detecting Changes in ARRAY columns when using the ORM**

        The :class:`_sqltypes.ARRAY` type, when used with the SQLAlchemy ORM,
        does not detect in-place mutations to the array. In order to detect
        these, the :mod:`sqlalchemy.ext.mutable` extension must be used, using
        the :class:`.MutableList` class::

            from sqlalchemy import ARRAY
            from sqlalchemy.ext.mutable import MutableList

            class SomeOrmClass(Base):
                # ...

                data = Column(MutableList.as_mutable(ARRAY(Integer)))

        This extension will allow "in-place" changes such to the array
        such as ``.append()`` to produce events which will be detected by the
        unit of work.  Note that changes to elements **inside** the array,
        including subarrays that are mutated in place, are **not** detected.

        Alternatively, assigning a new array value to an ORM element that
        replaces the old one will always trigger a change event.

    .. seealso::

        :class:`sqlalchemy.dialects.postgresql.ARRAY`

    '''
    __visit_name__: str
    zero_indexes: bool
    class Comparator(Indexable.Comparator[Sequence[Any]], Concatenable.Comparator[Sequence[Any]]):
        """Define comparison operations for :class:`_types.ARRAY`.

        More operators are available on the dialect-specific form
        of this type.  See :class:`.postgresql.ARRAY.Comparator`.

        """
        type: ARRAY
        def contains(self, *arg, **kw) -> None: ...
        def any(self, other, operator: Incomplete | None = None):
            """Return ``other operator ANY (array)`` clause.

            .. note:: This method is an :class:`_types.ARRAY` - specific
                construct that is now superseded by the :func:`_sql.any_`
                function, which features a different calling style. The
                :func:`_sql.any_` function is also mirrored at the method level
                via the :meth:`_sql.ColumnOperators.any_` method.

            Usage of array-specific :meth:`_types.ARRAY.Comparator.any`
            is as follows::

                from sqlalchemy.sql import operators

                conn.execute(
                    select(table.c.data).where(
                            table.c.data.any(7, operator=operators.lt)
                        )
                )

            :param other: expression to be compared
            :param operator: an operator object from the
             :mod:`sqlalchemy.sql.operators`
             package, defaults to :func:`.operators.eq`.

            .. seealso::

                :func:`_expression.any_`

                :meth:`.types.ARRAY.Comparator.all`

            """
        def all(self, other, operator: Incomplete | None = None):
            """Return ``other operator ALL (array)`` clause.

            .. note:: This method is an :class:`_types.ARRAY` - specific
                construct that is now superseded by the :func:`_sql.any_`
                function, which features a different calling style. The
                :func:`_sql.any_` function is also mirrored at the method level
                via the :meth:`_sql.ColumnOperators.any_` method.

            Usage of array-specific :meth:`_types.ARRAY.Comparator.all`
            is as follows::

                from sqlalchemy.sql import operators

                conn.execute(
                    select(table.c.data).where(
                            table.c.data.all(7, operator=operators.lt)
                        )
                )

            :param other: expression to be compared
            :param operator: an operator object from the
             :mod:`sqlalchemy.sql.operators`
             package, defaults to :func:`.operators.eq`.

            .. seealso::

                :func:`_expression.all_`

                :meth:`.types.ARRAY.Comparator.any`

            """
    comparator_factory = Comparator
    item_type: Incomplete
    as_tuple: Incomplete
    dimensions: Incomplete
    def __init__(self, item_type: _TypeEngineArgument[Any], as_tuple: bool = False, dimensions: int | None = None, zero_indexes: bool = False) -> None:
        '''Construct an :class:`_types.ARRAY`.

        E.g.::

          Column(\'myarray\', ARRAY(Integer))

        Arguments are:

        :param item_type: The data type of items of this array. Note that
          dimensionality is irrelevant here, so multi-dimensional arrays like
          ``INTEGER[][]``, are constructed as ``ARRAY(Integer)``, not as
          ``ARRAY(ARRAY(Integer))`` or such.

        :param as_tuple=False: Specify whether return results
          should be converted to tuples from lists.  This parameter is
          not generally needed as a Python list corresponds well
          to a SQL array.

        :param dimensions: if non-None, the ARRAY will assume a fixed
         number of dimensions.   This impacts how the array is declared
         on the database, how it goes about interpreting Python and
         result values, as well as how expression behavior in conjunction
         with the "getitem" operator works.  See the description at
         :class:`_types.ARRAY` for additional detail.

        :param zero_indexes=False: when True, index values will be converted
         between Python zero-based and SQL one-based indexes, e.g.
         a value of one will be added to all index values before passing
         to the database.

        '''
    @property
    def hashable(self): ...
    @property
    def python_type(self): ...
    def compare_values(self, x, y): ...
    def literal_processor(self, dialect): ...

class TupleType(TypeEngine[Tuple[Any, ...]]):
    """represent the composite type of a Tuple."""
    types: List[TypeEngine[Any]]
    def __init__(self, *types: _TypeEngineArgument[Any]) -> None: ...
    def coerce_compared_value(self, op: OperatorType | None, value: Any) -> TypeEngine[Any]: ...
    def result_processor(self, dialect, coltype) -> None: ...

class REAL(Float[_N]):
    """The SQL REAL type.

    .. seealso::

        :class:`_types.Float` - documentation for the base type.

    """
    __visit_name__: str

class FLOAT(Float[_N]):
    """The SQL FLOAT type.

    .. seealso::

        :class:`_types.Float` - documentation for the base type.

    """
    __visit_name__: str

class DOUBLE(Double[_N]):
    """The SQL DOUBLE type.

    .. versionadded:: 2.0

    .. seealso::

        :class:`_types.Double` - documentation for the base type.

    """
    __visit_name__: str

class DOUBLE_PRECISION(Double[_N]):
    """The SQL DOUBLE PRECISION type.

    .. versionadded:: 2.0

    .. seealso::

        :class:`_types.Double` - documentation for the base type.

    """
    __visit_name__: str

class NUMERIC(Numeric[_N]):
    """The SQL NUMERIC type.

    .. seealso::

        :class:`_types.Numeric` - documentation for the base type.

    """
    __visit_name__: str

class DECIMAL(Numeric[_N]):
    """The SQL DECIMAL type.

    .. seealso::

        :class:`_types.Numeric` - documentation for the base type.

    """
    __visit_name__: str

class INTEGER(Integer):
    """The SQL INT or INTEGER type.

    .. seealso::

        :class:`_types.Integer` - documentation for the base type.

    """
    __visit_name__: str
INT = INTEGER

class SMALLINT(SmallInteger):
    """The SQL SMALLINT type.

    .. seealso::

        :class:`_types.SmallInteger` - documentation for the base type.

    """
    __visit_name__: str

class BIGINT(BigInteger):
    """The SQL BIGINT type.

    .. seealso::

        :class:`_types.BigInteger` - documentation for the base type.

    """
    __visit_name__: str

class TIMESTAMP(DateTime):
    '''The SQL TIMESTAMP type.

    :class:`_types.TIMESTAMP` datatypes have support for timezone
    storage on some backends, such as PostgreSQL and Oracle.  Use the
    :paramref:`~types.TIMESTAMP.timezone` argument in order to enable
    "TIMESTAMP WITH TIMEZONE" for these backends.

    '''
    __visit_name__: str
    def __init__(self, timezone: bool = False) -> None:
        '''Construct a new :class:`_types.TIMESTAMP`.

        :param timezone: boolean.  Indicates that the TIMESTAMP type should
         enable timezone support, if available on the target database.
         On a per-dialect basis is similar to "TIMESTAMP WITH TIMEZONE".
         If the target database does not support timezones, this flag is
         ignored.


        '''
    def get_dbapi_type(self, dbapi): ...

class DATETIME(DateTime):
    """The SQL DATETIME type."""
    __visit_name__: str

class DATE(Date):
    """The SQL DATE type."""
    __visit_name__: str

class TIME(Time):
    """The SQL TIME type."""
    __visit_name__: str

class TEXT(Text):
    """The SQL TEXT type."""
    __visit_name__: str

class CLOB(Text):
    """The CLOB type.

    This type is found in Oracle and Informix.
    """
    __visit_name__: str

class VARCHAR(String):
    """The SQL VARCHAR type."""
    __visit_name__: str

class NVARCHAR(Unicode):
    """The SQL NVARCHAR type."""
    __visit_name__: str

class CHAR(String):
    """The SQL CHAR type."""
    __visit_name__: str

class NCHAR(Unicode):
    """The SQL NCHAR type."""
    __visit_name__: str

class BLOB(LargeBinary):
    """The SQL BLOB type."""
    __visit_name__: str

class BINARY(_Binary):
    """The SQL BINARY type."""
    __visit_name__: str

class VARBINARY(_Binary):
    """The SQL VARBINARY type."""
    __visit_name__: str

class BOOLEAN(Boolean):
    """The SQL BOOLEAN type."""
    __visit_name__: str

class NullType(TypeEngine[None]):
    """An unknown type.

    :class:`.NullType` is used as a default type for those cases where
    a type cannot be determined, including:

    * During table reflection, when the type of a column is not recognized
      by the :class:`.Dialect`
    * When constructing SQL expressions using plain Python objects of
      unknown types (e.g. ``somecolumn == my_special_object``)
    * When a new :class:`_schema.Column` is created,
      and the given type is passed
      as ``None`` or is not passed at all.

    The :class:`.NullType` can be used within SQL expression invocation
    without issue, it just has no behavior either at the expression
    construction level or at the bind-parameter/result processing level.
    :class:`.NullType` will result in a :exc:`.CompileError` if the compiler
    is asked to render the type itself, such as if it is used in a
    :func:`.cast` operation or within a schema creation operation such as that
    invoked by :meth:`_schema.MetaData.create_all` or the
    :class:`.CreateTable`
    construct.

    """
    __visit_name__: str
    def literal_processor(self, dialect) -> None: ...
    class Comparator(TypeEngine.Comparator[_T]): ...
    comparator_factory = Comparator

class TableValueType(HasCacheKey, TypeEngine[Any]):
    """Refers to a table value type."""
    def __init__(self, *elements: str | _ColumnExpressionArgument[Any]) -> None: ...

class MatchType(Boolean):
    """Refers to the return type of the MATCH operator.

    As the :meth:`.ColumnOperators.match` is probably the most open-ended
    operator in generic SQLAlchemy Core, we can't assume the return type
    at SQL evaluation time, as MySQL returns a floating point, not a boolean,
    and other backends might do something different.    So this type
    acts as a placeholder, currently subclassing :class:`.Boolean`.
    The type allows dialects to inject result-processing functionality
    if needed, and on MySQL will return floating-point values.

    """

class Uuid(Emulated, TypeEngine[_UUID_RETURN]):
    '''Represent a database agnostic UUID datatype.

    For backends that have no "native" UUID datatype, the value will
    make use of ``CHAR(32)`` and store the UUID as a 32-character alphanumeric
    hex string.

    For backends which are known to support ``UUID`` directly or a similar
    uuid-storing datatype such as SQL Server\'s ``UNIQUEIDENTIFIER``, a
    "native" mode enabled by default allows these types will be used on those
    backends.

    In its default mode of use, the :class:`_sqltypes.Uuid` datatype expects
    **Python uuid objects**, from the Python
    `uuid <https://docs.python.org/3/library/uuid.html>`_
    module::

        import uuid

        from sqlalchemy import Uuid
        from sqlalchemy import Table, Column, MetaData, String


        metadata_obj = MetaData()

        t = Table(
            "t",
            metadata_obj,
            Column(\'uuid_data\', Uuid, primary_key=True),
            Column("other_data", String)
        )

        with engine.begin() as conn:
            conn.execute(
                t.insert(),
                {"uuid_data": uuid.uuid4(), "other_data", "some data"}
            )

    To have the :class:`_sqltypes.Uuid` datatype work with string-based
    Uuids (e.g. 32 character hexadecimal strings), pass the
    :paramref:`_sqltypes.Uuid.as_uuid` parameter with the value ``False``.

    .. versionadded:: 2.0

    .. seealso::

        :class:`_sqltypes.UUID` - represents exactly the ``UUID`` datatype
        without any backend-agnostic behaviors.

    '''
    __visit_name__: str
    collation: str | None
    @overload
    def __init__(self, as_uuid: Literal[True] = ..., native_uuid: bool = ...) -> None: ...
    @overload
    def __init__(self, as_uuid: Literal[False] = ..., native_uuid: bool = ...) -> None: ...
    @property
    def python_type(self): ...
    @property
    def native(self): ...
    def coerce_compared_value(self, op, value):
        """See :meth:`.TypeEngine.coerce_compared_value` for a description."""
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...
    def literal_processor(self, dialect): ...

class UUID(Uuid[_UUID_RETURN], type_api.NativeForEmulated):
    """Represent the SQL UUID type.

    This is the SQL-native form of the :class:`_types.Uuid` database agnostic
    datatype, and is backwards compatible with the previous PostgreSQL-only
    version of ``UUID``.

    The :class:`_sqltypes.UUID` datatype only works on databases that have a
    SQL datatype named ``UUID``. It will not function for backends which don't
    have this exact-named type, including SQL Server. For backend-agnostic UUID
    values with native support, including for SQL Server's ``UNIQUEIDENTIFIER``
    datatype, use the :class:`_sqltypes.Uuid` datatype.

    .. versionadded:: 2.0

    .. seealso::

        :class:`_sqltypes.Uuid`

    """
    __visit_name__: str
    @overload
    def __init__(self, as_uuid: Literal[True] = ...) -> None: ...
    @overload
    def __init__(self, as_uuid: Literal[False] = ...) -> None: ...
    @classmethod
    def adapt_emulated_to_native(cls, impl, **kw): ...

NULLTYPE: Incomplete
BOOLEANTYPE: Incomplete
STRINGTYPE: Incomplete
INTEGERTYPE: Incomplete
NUMERICTYPE: Numeric[decimal.Decimal]
MATCHTYPE: Incomplete
TABLEVALUE: Incomplete
DATETIME_TIMEZONE: Incomplete
TIME_TIMEZONE: Incomplete
INDEXABLE = Indexable
