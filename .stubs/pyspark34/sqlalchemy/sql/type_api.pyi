from .. import exc as exc, util as util
from ..engine.interfaces import Dialect as Dialect
from ..util.typing import GenericProtocol as GenericProtocol, Protocol as Protocol, Self as Self, TypeGuard as TypeGuard, TypedDict as TypedDict
from ._typing import _TypeEngineArgument
from .base import SchemaEventTarget as SchemaEventTarget
from .cache_key import CacheConst as CacheConst, NO_CACHE as NO_CACHE
from .elements import BindParameter as BindParameter, ColumnElement as ColumnElement
from .operators import ColumnOperators as ColumnOperators, OperatorType as OperatorType
from .visitors import Visitable as Visitable
from enum import Enum
from types import ModuleType
from typing import Any, Callable, Dict, Generic, Mapping, Sequence, Type, overload

class _NoValueInList(Enum):
    NO_VALUE_IN_LIST: int

class _LiteralProcessorType(Protocol[_T_co]):
    def __call__(self, value: Any) -> str: ...

class _BindProcessorType(Protocol[_T_con]):
    def __call__(self, value: _T_con | None) -> Any: ...

class _ResultProcessorType(Protocol[_T_co]):
    def __call__(self, value: Any) -> _T_co | None: ...

class _SentinelProcessorType(Protocol[_T_co]):
    def __call__(self, value: Any) -> _T_co | None: ...

class _BaseTypeMemoDict(TypedDict):
    impl: TypeEngine[Any]
    result: Dict[Any, _ResultProcessorType[Any] | None]

class _TypeMemoDict(_BaseTypeMemoDict, total=False):
    literal: _LiteralProcessorType[Any] | None
    bind: _BindProcessorType[Any] | None
    sentinel: _SentinelProcessorType[Any] | None
    custom: Dict[Any, object]

class _ComparatorFactory(Protocol[_T]):
    def __call__(self, expr: ColumnElement[_T]) -> TypeEngine.Comparator[_T]: ...

class TypeEngine(Visitable, Generic[_T]):
    """The ultimate base class for all SQL datatypes.

    Common subclasses of :class:`.TypeEngine` include
    :class:`.String`, :class:`.Integer`, and :class:`.Boolean`.

    For an overview of the SQLAlchemy typing system, see
    :ref:`types_toplevel`.

    .. seealso::

        :ref:`types_toplevel`

    """
    render_bind_cast: bool
    render_literal_cast: bool
    class Comparator(ColumnOperators, Generic[_CT]):
        """Base class for custom comparison operations defined at the
        type level.  See :attr:`.TypeEngine.comparator_factory`.


        """
        expr: ColumnElement[_CT]
        type: TypeEngine[_CT]
        def __clause_element__(self) -> ColumnElement[_CT]: ...
        def __init__(self, expr: ColumnElement[_CT]) -> None: ...
        def operate(self, op: OperatorType, *other: Any, **kwargs: Any) -> ColumnElement[_CT]: ...
        def reverse_operate(self, op: OperatorType, other: Any, **kwargs: Any) -> ColumnElement[_CT]: ...
    hashable: bool
    comparator_factory: _ComparatorFactory[Any]
    sort_key_function: Callable[[Any], Any] | None
    should_evaluate_none: bool
    def evaluates_none(self) -> Self:
        '''Return a copy of this type which has the
        :attr:`.should_evaluate_none` flag set to True.

        E.g.::

                Table(
                    \'some_table\', metadata,
                    Column(
                        String(50).evaluates_none(),
                        nullable=True,
                        server_default=\'no value\')
                )

        The ORM uses this flag to indicate that a positive value of ``None``
        is passed to the column in an INSERT statement, rather than omitting
        the column from the INSERT statement which has the effect of firing
        off column-level defaults.   It also allows for types which have
        special behavior associated with the Python None value to indicate
        that the value doesn\'t necessarily translate into SQL NULL; a
        prime example of this is a JSON type which may wish to persist the
        JSON value ``\'null\'``.

        In all cases, the actual NULL SQL value can be always be
        persisted in any column by using
        the :obj:`_expression.null` SQL construct in an INSERT statement
        or associated with an ORM-mapped attribute.

        .. note::

            The "evaluates none" flag does **not** apply to a value
            of ``None`` passed to :paramref:`_schema.Column.default` or
            :paramref:`_schema.Column.server_default`; in these cases,
            ``None``
            still means "no default".

        .. seealso::

            :ref:`session_forcing_null` - in the ORM documentation

            :paramref:`.postgresql.JSON.none_as_null` - PostgreSQL JSON
            interaction with this flag.

            :attr:`.TypeEngine.should_evaluate_none` - class-level flag

        '''
    def copy(self, **kw: Any) -> Self: ...
    def compare_against_backend(self, dialect: Dialect, conn_type: TypeEngine[Any]) -> bool | None:
        """Compare this type against the given backend type.

        This function is currently not implemented for SQLAlchemy
        types, and for all built in types will return ``None``.  However,
        it can be implemented by a user-defined type
        where it can be consumed by schema comparison tools such as
        Alembic autogenerate.

        A future release of SQLAlchemy will potentially implement this method
        for builtin types as well.

        The function should return True if this type is equivalent to the
        given type; the type is typically reflected from the database
        so should be database specific.  The dialect in use is also
        passed.   It can also return False to assert that the type is
        not equivalent.

        :param dialect: a :class:`.Dialect` that is involved in the comparison.

        :param conn_type: the type object reflected from the backend.

        """
    def copy_value(self, value: Any) -> Any: ...
    def literal_processor(self, dialect: Dialect) -> _LiteralProcessorType[_T] | None:
        '''Return a conversion function for processing literal values that are
        to be rendered directly without using binds.

        This function is used when the compiler makes use of the
        "literal_binds" flag, typically used in DDL generation as well
        as in certain scenarios where backends don\'t accept bound parameters.

        Returns a callable which will receive a literal Python value
        as the sole positional argument and will return a string representation
        to be rendered in a SQL statement.

        .. note::

            This method is only called relative to a **dialect specific type
            object**, which is often **private to a dialect in use** and is not
            the same type object as the public facing one, which means it\'s not
            feasible to subclass a :class:`.types.TypeEngine` class in order to
            provide an alternate :meth:`_types.TypeEngine.literal_processor`
            method, unless subclassing the :class:`_types.UserDefinedType`
            class explicitly.

            To provide alternate behavior for
            :meth:`_types.TypeEngine.literal_processor`, implement a
            :class:`_types.TypeDecorator` class and provide an implementation
            of :meth:`_types.TypeDecorator.process_literal_param`.

            .. seealso::

                :ref:`types_typedecorator`


        '''
    def bind_processor(self, dialect: Dialect) -> _BindProcessorType[_T] | None:
        """Return a conversion function for processing bind values.

        Returns a callable which will receive a bind parameter value
        as the sole positional argument and will return a value to
        send to the DB-API.

        If processing is not necessary, the method should return ``None``.

        .. note::

            This method is only called relative to a **dialect specific type
            object**, which is often **private to a dialect in use** and is not
            the same type object as the public facing one, which means it's not
            feasible to subclass a :class:`.types.TypeEngine` class in order to
            provide an alternate :meth:`_types.TypeEngine.bind_processor`
            method, unless subclassing the :class:`_types.UserDefinedType`
            class explicitly.

            To provide alternate behavior for
            :meth:`_types.TypeEngine.bind_processor`, implement a
            :class:`_types.TypeDecorator` class and provide an implementation
            of :meth:`_types.TypeDecorator.process_bind_param`.

            .. seealso::

                :ref:`types_typedecorator`


        :param dialect: Dialect instance in use.

        """
    def result_processor(self, dialect: Dialect, coltype: object) -> _ResultProcessorType[_T] | None:
        """Return a conversion function for processing result row values.

        Returns a callable which will receive a result row column
        value as the sole positional argument and will return a value
        to return to the user.

        If processing is not necessary, the method should return ``None``.

        .. note::

            This method is only called relative to a **dialect specific type
            object**, which is often **private to a dialect in use** and is not
            the same type object as the public facing one, which means it's not
            feasible to subclass a :class:`.types.TypeEngine` class in order to
            provide an alternate :meth:`_types.TypeEngine.result_processor`
            method, unless subclassing the :class:`_types.UserDefinedType`
            class explicitly.

            To provide alternate behavior for
            :meth:`_types.TypeEngine.result_processor`, implement a
            :class:`_types.TypeDecorator` class and provide an implementation
            of :meth:`_types.TypeDecorator.process_result_value`.

            .. seealso::

                :ref:`types_typedecorator`

        :param dialect: Dialect instance in use.

        :param coltype: DBAPI coltype argument received in cursor.description.

        """
    def column_expression(self, colexpr: ColumnElement[_T]) -> ColumnElement[_T] | None:
        """Given a SELECT column expression, return a wrapping SQL expression.

        This is typically a SQL function that wraps a column expression
        as rendered in the columns clause of a SELECT statement.
        It is used for special data types that require
        columns to be wrapped in some special database function in order
        to coerce the value before being sent back to the application.
        It is the SQL analogue of the :meth:`.TypeEngine.result_processor`
        method.

        This method is called during the **SQL compilation** phase of a
        statement, when rendering a SQL string. It is **not** called
        against specific values.

        .. note::

            This method is only called relative to a **dialect specific type
            object**, which is often **private to a dialect in use** and is not
            the same type object as the public facing one, which means it's not
            feasible to subclass a :class:`.types.TypeEngine` class in order to
            provide an alternate :meth:`_types.TypeEngine.column_expression`
            method, unless subclassing the :class:`_types.UserDefinedType`
            class explicitly.

            To provide alternate behavior for
            :meth:`_types.TypeEngine.column_expression`, implement a
            :class:`_types.TypeDecorator` class and provide an implementation
            of :meth:`_types.TypeDecorator.column_expression`.

            .. seealso::

                :ref:`types_typedecorator`


        .. seealso::

            :ref:`types_sql_value_processing`

        """
    def bind_expression(self, bindvalue: BindParameter[_T]) -> ColumnElement[_T] | None:
        """Given a bind value (i.e. a :class:`.BindParameter` instance),
        return a SQL expression in its place.

        This is typically a SQL function that wraps the existing bound
        parameter within the statement.  It is used for special data types
        that require literals being wrapped in some special database function
        in order to coerce an application-level value into a database-specific
        format.  It is the SQL analogue of the
        :meth:`.TypeEngine.bind_processor` method.

        This method is called during the **SQL compilation** phase of a
        statement, when rendering a SQL string. It is **not** called
        against specific values.

        Note that this method, when implemented, should always return
        the exact same structure, without any conditional logic, as it
        may be used in an executemany() call against an arbitrary number
        of bound parameter sets.

        .. note::

            This method is only called relative to a **dialect specific type
            object**, which is often **private to a dialect in use** and is not
            the same type object as the public facing one, which means it's not
            feasible to subclass a :class:`.types.TypeEngine` class in order to
            provide an alternate :meth:`_types.TypeEngine.bind_expression`
            method, unless subclassing the :class:`_types.UserDefinedType`
            class explicitly.

            To provide alternate behavior for
            :meth:`_types.TypeEngine.bind_expression`, implement a
            :class:`_types.TypeDecorator` class and provide an implementation
            of :meth:`_types.TypeDecorator.bind_expression`.

            .. seealso::

                :ref:`types_typedecorator`

        .. seealso::

            :ref:`types_sql_value_processing`

        """
    def compare_values(self, x: Any, y: Any) -> bool:
        """Compare two values for equality."""
    def get_dbapi_type(self, dbapi: ModuleType) -> Any | None:
        """Return the corresponding type object from the underlying DB-API, if
        any.

        This can be useful for calling ``setinputsizes()``, for example.

        """
    @property
    def python_type(self) -> Type[Any]:
        """Return the Python type object expected to be returned
        by instances of this type, if known.

        Basically, for those types which enforce a return type,
        or are known across the board to do such for all common
        DBAPIs (like ``int`` for example), will return that type.

        If a return type is not defined, raises
        ``NotImplementedError``.

        Note that any type also accommodates NULL in SQL which
        means you can also get back ``None`` from any type
        in practice.

        """
    def with_variant(self, type_: _TypeEngineArgument[Any], *dialect_names: str) -> Self:
        '''Produce a copy of this type object that will utilize the given
        type when applied to the dialect of the given name.

        e.g.::

            from sqlalchemy.types import String
            from sqlalchemy.dialects import mysql

            string_type = String()

            string_type = string_type.with_variant(
                mysql.VARCHAR(collation=\'foo\'), \'mysql\', \'mariadb\'
            )

        The variant mapping indicates that when this type is
        interpreted by a specific dialect, it will instead be
        transmuted into the given type, rather than using the
        primary type.

        .. versionchanged:: 2.0 the :meth:`_types.TypeEngine.with_variant`
           method now works with a :class:`_types.TypeEngine` object "in
           place", returning a copy of the original type rather than returning
           a wrapping object; the ``Variant`` class is no longer used.

        :param type\\_: a :class:`.TypeEngine` that will be selected
         as a variant from the originating type, when a dialect
         of the given name is in use.
        :param \\*dialect_names: one or more base names of the dialect which
         uses this type. (i.e. ``\'postgresql\'``, ``\'mysql\'``, etc.)

         .. versionchanged:: 2.0 multiple dialect names can be specified
            for one variant.

        .. seealso::

            :ref:`types_with_variant` - illustrates the use of
            :meth:`_types.TypeEngine.with_variant`.

        '''
    def as_generic(self, allow_nulltype: bool = False) -> TypeEngine[_T]:
        """
        Return an instance of the generic type corresponding to this type
        using heuristic rule. The method may be overridden if this
        heuristic rule is not sufficient.

        >>> from sqlalchemy.dialects.mysql import INTEGER
        >>> INTEGER(display_width=4).as_generic()
        Integer()

        >>> from sqlalchemy.dialects.mysql import NVARCHAR
        >>> NVARCHAR(length=100).as_generic()
        Unicode(length=100)

        .. versionadded:: 1.4.0b2


        .. seealso::

            :ref:`metadata_reflection_dbagnostic_types` - describes the
            use of :meth:`_types.TypeEngine.as_generic` in conjunction with
            the :meth:`_sql.DDLEvents.column_reflect` event, which is its
            intended use.

        """
    def dialect_impl(self, dialect: Dialect) -> TypeEngine[_T]:
        """Return a dialect-specific implementation for this
        :class:`.TypeEngine`.

        """
    @overload
    def adapt(self, cls: Type[_TE], **kw: Any) -> _TE: ...
    @overload
    def adapt(self, cls: Type[TypeEngineMixin], **kw: Any) -> TypeEngine[Any]: ...
    def coerce_compared_value(self, op: OperatorType | None, value: Any) -> TypeEngine[Any]:
        """Suggest a type for a 'coerced' Python value in an expression.

        Given an operator and value, gives the type a chance
        to return a type which the value should be coerced into.

        The default behavior here is conservative; if the right-hand
        side is already coerced into a SQL type based on its
        Python type, it is usually left alone.

        End-user functionality extension here should generally be via
        :class:`.TypeDecorator`, which provides more liberal behavior in that
        it defaults to coercing the other side of the expression into this
        type, thus applying special Python conversions above and beyond those
        needed by the DBAPI to both ides. It also provides the public method
        :meth:`.TypeDecorator.coerce_compared_value` which is intended for
        end-user customization of this behavior.

        """
    def compile(self, dialect: Dialect | None = None) -> str:
        '''Produce a string-compiled form of this :class:`.TypeEngine`.

        When called with no arguments, uses a "default" dialect
        to produce a string result.

        :param dialect: a :class:`.Dialect` instance.

        '''

class TypeEngineMixin:
    '''classes which subclass this can act as "mixin" classes for
    TypeEngine.'''
    @overload
    def adapt(self, cls: Type[_TE], **kw: Any) -> _TE: ...
    @overload
    def adapt(self, cls: Type[TypeEngineMixin], **kw: Any) -> TypeEngine[Any]: ...
    def dialect_impl(self, dialect: Dialect) -> TypeEngine[Any]: ...

class ExternalType(TypeEngineMixin):
    '''mixin that defines attributes and behaviors specific to third-party
    datatypes.

    "Third party" refers to datatypes that are defined outside the scope
    of SQLAlchemy within either end-user application code or within
    external extensions to SQLAlchemy.

    Subclasses currently include :class:`.TypeDecorator` and
    :class:`.UserDefinedType`.

    .. versionadded:: 1.4.28

    '''
    cache_ok: bool | None

class UserDefinedType(ExternalType, TypeEngineMixin, TypeEngine[_T], util.EnsureKWArg):
    '''Base for user defined types.

    This should be the base of new types.  Note that
    for most cases, :class:`.TypeDecorator` is probably
    more appropriate::

      import sqlalchemy.types as types

      class MyType(types.UserDefinedType):
          cache_ok = True

          def __init__(self, precision = 8):
              self.precision = precision

          def get_col_spec(self, **kw):
              return "MYTYPE(%s)" % self.precision

          def bind_processor(self, dialect):
              def process(value):
                  return value
              return process

          def result_processor(self, dialect, coltype):
              def process(value):
                  return value
              return process

    Once the type is made, it\'s immediately usable::

      table = Table(\'foo\', metadata_obj,
          Column(\'id\', Integer, primary_key=True),
          Column(\'data\', MyType(16))
          )

    The ``get_col_spec()`` method will in most cases receive a keyword
    argument ``type_expression`` which refers to the owning expression
    of the type as being compiled, such as a :class:`_schema.Column` or
    :func:`.cast` construct.  This keyword is only sent if the method
    accepts keyword arguments (e.g. ``**kw``) in its argument signature;
    introspection is used to check for this in order to support legacy
    forms of this function.

    The :attr:`.UserDefinedType.cache_ok` class-level flag indicates if this
    custom :class:`.UserDefinedType` is safe to be used as part of a cache key.
    This flag defaults to ``None`` which will initially generate a warning
    when the SQL compiler attempts to generate a cache key for a statement
    that uses this type.  If the :class:`.UserDefinedType` is not guaranteed
    to produce the same bind/result behavior and SQL generation
    every time, this flag should be set to ``False``; otherwise if the
    class produces the same behavior each time, it may be set to ``True``.
    See :attr:`.UserDefinedType.cache_ok` for further notes on how this works.

    .. versionadded:: 1.4.28 Generalized the :attr:`.ExternalType.cache_ok`
       flag so that it is available for both :class:`.TypeDecorator` as well
       as :class:`.UserDefinedType`.

    '''
    __visit_name__: str
    ensure_kwarg: str
    def coerce_compared_value(self, op: OperatorType | None, value: Any) -> TypeEngine[Any]:
        """Suggest a type for a 'coerced' Python value in an expression.

        Default behavior for :class:`.UserDefinedType` is the
        same as that of :class:`.TypeDecorator`; by default it returns
        ``self``, assuming the compared value should be coerced into
        the same type as this one.  See
        :meth:`.TypeDecorator.coerce_compared_value` for more detail.

        """

class Emulated(TypeEngineMixin):
    """Mixin for base types that emulate the behavior of a DB-native type.

    An :class:`.Emulated` type will use an available database type
    in conjunction with Python-side routines and/or database constraints
    in order to approximate the behavior of a database type that is provided
    natively by some backends.  When a native-providing backend is in
    use, the native version of the type is used.  This native version
    should include the :class:`.NativeForEmulated` mixin to allow it to be
    distinguished from :class:`.Emulated`.

    Current examples of :class:`.Emulated` are:  :class:`.Interval`,
    :class:`.Enum`, :class:`.Boolean`.

    .. versionadded:: 1.2.0b3

    """
    native: bool
    def adapt_to_emulated(self, impltype: Type[TypeEngine[Any] | TypeEngineMixin], **kw: Any) -> TypeEngine[Any]:
        '''Given an impl class, adapt this type to the impl assuming
        "emulated".

        The impl should also be an "emulated" version of this type,
        most likely the same class as this type itself.

        e.g.: sqltypes.Enum adapts to the Enum class.

        '''
    @overload
    def adapt(self, cls: Type[_TE], **kw: Any) -> _TE: ...
    @overload
    def adapt(self, cls: Type[TypeEngineMixin], **kw: Any) -> TypeEngine[Any]: ...

class NativeForEmulated(TypeEngineMixin):
    """Indicates DB-native types supported by an :class:`.Emulated` type.

    .. versionadded:: 1.2.0b3

    """
    @classmethod
    def adapt_native_to_emulated(cls, impl: TypeEngine[Any] | TypeEngineMixin, **kw: Any) -> TypeEngine[Any]:
        '''Given an impl, adapt this type\'s class to the impl assuming
        "emulated".


        '''
    @classmethod
    def adapt_emulated_to_native(cls, impl: TypeEngine[Any] | TypeEngineMixin, **kw: Any) -> TypeEngine[Any]:
        '''Given an impl, adapt this type\'s class to the impl assuming
        "native".

        The impl will be an :class:`.Emulated` class but not a
        :class:`.NativeForEmulated`.

        e.g.: postgresql.ENUM produces a type given an Enum instance.

        '''

class TypeDecorator(SchemaEventTarget, ExternalType, TypeEngine[_T]):
    '''Allows the creation of types which add additional functionality
    to an existing type.

    This method is preferred to direct subclassing of SQLAlchemy\'s
    built-in types as it ensures that all required functionality of
    the underlying type is kept in place.

    Typical usage::

      import sqlalchemy.types as types

      class MyType(types.TypeDecorator):
          \'\'\'Prefixes Unicode values with "PREFIX:" on the way in and
          strips it off on the way out.
          \'\'\'

          impl = types.Unicode

          cache_ok = True

          def process_bind_param(self, value, dialect):
              return "PREFIX:" + value

          def process_result_value(self, value, dialect):
              return value[7:]

          def copy(self, **kw):
              return MyType(self.impl.length)

    The class-level ``impl`` attribute is required, and can reference any
    :class:`.TypeEngine` class.  Alternatively, the :meth:`load_dialect_impl`
    method can be used to provide different type classes based on the dialect
    given; in this case, the ``impl`` variable can reference
    ``TypeEngine`` as a placeholder.

    The :attr:`.TypeDecorator.cache_ok` class-level flag indicates if this
    custom :class:`.TypeDecorator` is safe to be used as part of a cache key.
    This flag defaults to ``None`` which will initially generate a warning
    when the SQL compiler attempts to generate a cache key for a statement
    that uses this type.  If the :class:`.TypeDecorator` is not guaranteed
    to produce the same bind/result behavior and SQL generation
    every time, this flag should be set to ``False``; otherwise if the
    class produces the same behavior each time, it may be set to ``True``.
    See :attr:`.TypeDecorator.cache_ok` for further notes on how this works.

    Types that receive a Python type that isn\'t similar to the ultimate type
    used may want to define the :meth:`TypeDecorator.coerce_compared_value`
    method. This is used to give the expression system a hint when coercing
    Python objects into bind parameters within expressions. Consider this
    expression::

        mytable.c.somecol + datetime.date(2009, 5, 15)

    Above, if "somecol" is an ``Integer`` variant, it makes sense that
    we\'re doing date arithmetic, where above is usually interpreted
    by databases as adding a number of days to the given date.
    The expression system does the right thing by not attempting to
    coerce the "date()" value into an integer-oriented bind parameter.

    However, in the case of ``TypeDecorator``, we are usually changing an
    incoming Python type to something new - ``TypeDecorator`` by default will
    "coerce" the non-typed side to be the same type as itself. Such as below,
    we define an "epoch" type that stores a date value as an integer::

        class MyEpochType(types.TypeDecorator):
            impl = types.Integer

            epoch = datetime.date(1970, 1, 1)

            def process_bind_param(self, value, dialect):
                return (value - self.epoch).days

            def process_result_value(self, value, dialect):
                return self.epoch + timedelta(days=value)

    Our expression of ``somecol + date`` with the above type will coerce the
    "date" on the right side to also be treated as ``MyEpochType``.

    This behavior can be overridden via the
    :meth:`~TypeDecorator.coerce_compared_value` method, which returns a type
    that should be used for the value of the expression. Below we set it such
    that an integer value will be treated as an ``Integer``, and any other
    value is assumed to be a date and will be treated as a ``MyEpochType``::

        def coerce_compared_value(self, op, value):
            if isinstance(value, int):
                return Integer()
            else:
                return self

    .. warning::

       Note that the **behavior of coerce_compared_value is not inherited
       by default from that of the base type**.
       If the :class:`.TypeDecorator` is augmenting a
       type that requires special logic for certain types of operators,
       this method **must** be overridden.  A key example is when decorating
       the :class:`_postgresql.JSON` and :class:`_postgresql.JSONB` types;
       the default rules of :meth:`.TypeEngine.coerce_compared_value` should
       be used in order to deal with operators like index operations::

            from sqlalchemy import JSON
            from sqlalchemy import TypeDecorator

            class MyJsonType(TypeDecorator):
                impl = JSON

                cache_ok = True

                def coerce_compared_value(self, op, value):
                    return self.impl.coerce_compared_value(op, value)

       Without the above step, index operations such as ``mycol[\'foo\']``
       will cause the index value ``\'foo\'`` to be JSON encoded.

       Similarly, when working with the :class:`.ARRAY` datatype, the
       type coercion for index operations (e.g. ``mycol[5]``) is also
       handled by :meth:`.TypeDecorator.coerce_compared_value`, where
       again a simple override is sufficient unless special rules are needed
       for particular operators::

            from sqlalchemy import ARRAY
            from sqlalchemy import TypeDecorator

            class MyArrayType(TypeDecorator):
                impl = ARRAY

                cache_ok = True

                def coerce_compared_value(self, op, value):
                    return self.impl.coerce_compared_value(op, value)


    '''
    __visit_name__: str
    impl: TypeEngine[Any] | Type[TypeEngine[Any]]
    def impl_instance(self) -> TypeEngine[Any]: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Construct a :class:`.TypeDecorator`.

        Arguments sent here are passed to the constructor
        of the class assigned to the ``impl`` class level attribute,
        assuming the ``impl`` is a callable, and the resulting
        object is assigned to the ``self.impl`` instance attribute
        (thus overriding the class attribute of the same name).

        If the class level ``impl`` is not a callable (the unusual case),
        it will be assigned to the same instance attribute 'as-is',
        ignoring those arguments passed to the constructor.

        Subclasses can override this to customize the generation
        of ``self.impl`` entirely.

        """
    coerce_to_is_types: Sequence[Type[Any]]
    class Comparator(TypeEngine.Comparator[_CT]):
        """A :class:`.TypeEngine.Comparator` that is specific to
        :class:`.TypeDecorator`.

        User-defined :class:`.TypeDecorator` classes should not typically
        need to modify this.


        """
        def operate(self, op: OperatorType, *other: Any, **kwargs: Any) -> ColumnElement[_CT]: ...
        def reverse_operate(self, op: OperatorType, other: Any, **kwargs: Any) -> ColumnElement[_CT]: ...
    @property
    def comparator_factory(self) -> _ComparatorFactory[Any]: ...
    def type_engine(self, dialect: Dialect) -> TypeEngine[Any]:
        """Return a dialect-specific :class:`.TypeEngine` instance
        for this :class:`.TypeDecorator`.

        In most cases this returns a dialect-adapted form of
        the :class:`.TypeEngine` type represented by ``self.impl``.
        Makes usage of :meth:`dialect_impl`.
        Behavior can be customized here by overriding
        :meth:`load_dialect_impl`.

        """
    def load_dialect_impl(self, dialect: Dialect) -> TypeEngine[Any]:
        """Return a :class:`.TypeEngine` object corresponding to a dialect.

        This is an end-user override hook that can be used to provide
        differing types depending on the given dialect.  It is used
        by the :class:`.TypeDecorator` implementation of :meth:`type_engine`
        to help determine what type should ultimately be returned
        for a given :class:`.TypeDecorator`.

        By default returns ``self.impl``.

        """
    def __getattr__(self, key: str) -> Any:
        """Proxy all other undefined accessors to the underlying
        implementation."""
    def process_literal_param(self, value: _T | None, dialect: Dialect) -> str:
        """Receive a literal parameter value to be rendered inline within
        a statement.

        .. note::

            This method is called during the **SQL compilation** phase of a
            statement, when rendering a SQL string. Unlike other SQL
            compilation methods, it is passed a specific Python value to be
            rendered as a string. However it should not be confused with the
            :meth:`_types.TypeDecorator.process_bind_param` method, which is
            the more typical method that processes the actual value passed to a
            particular parameter at statement execution time.

        Custom subclasses of :class:`_types.TypeDecorator` should override
        this method to provide custom behaviors for incoming data values
        that are in the special case of being rendered as literals.

        The returned string will be rendered into the output string.

        """
    def process_bind_param(self, value: _T | None, dialect: Dialect) -> Any:
        """Receive a bound parameter value to be converted.

        Custom subclasses of :class:`_types.TypeDecorator` should override
        this method to provide custom behaviors for incoming data values.
        This method is called at **statement execution time** and is passed
        the literal Python data value which is to be associated with a bound
        parameter in the statement.

        The operation could be anything desired to perform custom
        behavior, such as transforming or serializing data.
        This could also be used as a hook for validating logic.

        :param value: Data to operate upon, of any type expected by
         this method in the subclass.  Can be ``None``.
        :param dialect: the :class:`.Dialect` in use.

        .. seealso::

            :ref:`types_typedecorator`

            :meth:`_types.TypeDecorator.process_result_value`

        """
    def process_result_value(self, value: Any | None, dialect: Dialect) -> _T | None:
        """Receive a result-row column value to be converted.

        Custom subclasses of :class:`_types.TypeDecorator` should override
        this method to provide custom behaviors for data values
        being received in result rows coming from the database.
        This method is called at **result fetching time** and is passed
        the literal Python data value that's extracted from a database result
        row.

        The operation could be anything desired to perform custom
        behavior, such as transforming or deserializing data.

        :param value: Data to operate upon, of any type expected by
         this method in the subclass.  Can be ``None``.
        :param dialect: the :class:`.Dialect` in use.

        .. seealso::

            :ref:`types_typedecorator`

            :meth:`_types.TypeDecorator.process_bind_param`


        """
    def literal_processor(self, dialect: Dialect) -> _LiteralProcessorType[_T] | None:
        '''Provide a literal processing function for the given
        :class:`.Dialect`.

        This is the method that fulfills the :class:`.TypeEngine`
        contract for literal value conversion which normally occurs via
        the :meth:`_types.TypeEngine.literal_processor` method.

        .. note::

            User-defined subclasses of :class:`_types.TypeDecorator` should
            **not** implement this method, and should instead implement
            :meth:`_types.TypeDecorator.process_literal_param` so that the
            "inner" processing provided by the implementing type is maintained.

        '''
    def bind_processor(self, dialect: Dialect) -> _BindProcessorType[_T] | None:
        '''Provide a bound value processing function for the
        given :class:`.Dialect`.

        This is the method that fulfills the :class:`.TypeEngine`
        contract for bound value conversion which normally occurs via
        the :meth:`_types.TypeEngine.bind_processor` method.

        .. note::

            User-defined subclasses of :class:`_types.TypeDecorator` should
            **not** implement this method, and should instead implement
            :meth:`_types.TypeDecorator.process_bind_param` so that the "inner"
            processing provided by the implementing type is maintained.

        :param dialect: Dialect instance in use.

        '''
    def result_processor(self, dialect: Dialect, coltype: Any) -> _ResultProcessorType[_T] | None:
        '''Provide a result value processing function for the given
        :class:`.Dialect`.

        This is the method that fulfills the :class:`.TypeEngine`
        contract for bound value conversion which normally occurs via
        the :meth:`_types.TypeEngine.result_processor` method.

        .. note::

            User-defined subclasses of :class:`_types.TypeDecorator` should
            **not** implement this method, and should instead implement
            :meth:`_types.TypeDecorator.process_result_value` so that the
            "inner" processing provided by the implementing type is maintained.

        :param dialect: Dialect instance in use.
        :param coltype: A SQLAlchemy data type

        '''
    def bind_expression(self, bindparam: BindParameter[_T]) -> ColumnElement[_T] | None:
        """Given a bind value (i.e. a :class:`.BindParameter` instance),
        return a SQL expression which will typically wrap the given parameter.

        .. note::

            This method is called during the **SQL compilation** phase of a
            statement, when rendering a SQL string. It is **not** necessarily
            called against specific values, and should not be confused with the
            :meth:`_types.TypeDecorator.process_bind_param` method, which is
            the more typical method that processes the actual value passed to a
            particular parameter at statement execution time.

        Subclasses of :class:`_types.TypeDecorator` can override this method
        to provide custom bind expression behavior for the type.  This
        implementation will **replace** that of the underlying implementation
        type.

        """
    def column_expression(self, column: ColumnElement[_T]) -> ColumnElement[_T] | None:
        """Given a SELECT column expression, return a wrapping SQL expression.

        .. note::

            This method is called during the **SQL compilation** phase of a
            statement, when rendering a SQL string. It is **not** called
            against specific values, and should not be confused with the
            :meth:`_types.TypeDecorator.process_result_value` method, which is
            the more typical method that processes the actual value returned
            in a result row subsequent to statement execution time.

        Subclasses of :class:`_types.TypeDecorator` can override this method
        to provide custom column expression behavior for the type.  This
        implementation will **replace** that of the underlying implementation
        type.

        See the description of :meth:`_types.TypeEngine.column_expression`
        for a complete description of the method's use.

        """
    def coerce_compared_value(self, op: OperatorType | None, value: Any) -> Any:
        """Suggest a type for a 'coerced' Python value in an expression.

        By default, returns self.   This method is called by
        the expression system when an object using this type is
        on the left or right side of an expression against a plain Python
        object which does not yet have a SQLAlchemy type assigned::

            expr = table.c.somecolumn + 35

        Where above, if ``somecolumn`` uses this type, this method will
        be called with the value ``operator.add``
        and ``35``.  The return value is whatever SQLAlchemy type should
        be used for ``35`` for this particular operation.

        """
    def copy(self, **kw: Any) -> Self:
        """Produce a copy of this :class:`.TypeDecorator` instance.

        This is a shallow copy and is provided to fulfill part of
        the :class:`.TypeEngine` contract.  It usually does not
        need to be overridden unless the user-defined :class:`.TypeDecorator`
        has local state that should be deep-copied.

        """
    def get_dbapi_type(self, dbapi: ModuleType) -> Any | None:
        '''Return the DBAPI type object represented by this
        :class:`.TypeDecorator`.

        By default this calls upon :meth:`.TypeEngine.get_dbapi_type` of the
        underlying "impl".
        '''
    def compare_values(self, x: Any, y: Any) -> bool:
        '''Given two values, compare them for equality.

        By default this calls upon :meth:`.TypeEngine.compare_values`
        of the underlying "impl", which in turn usually
        uses the Python equals operator ``==``.

        This function is used by the ORM to compare
        an original-loaded value with an intercepted
        "changed" value, to determine if a net change
        has occurred.

        '''
    @property
    def sort_key_function(self) -> Callable[[Any], Any] | None: ...

class Variant(TypeDecorator[_T]):
    """deprecated.  symbol is present for backwards-compatibility with
    workaround recipes, however this actual type should not be used.

    """
    def __init__(self, *arg: Any, **kw: Any) -> None: ...

@overload
def to_instance(typeobj: Type[_TE] | _TE, *arg: Any, **kw: Any) -> _TE: ...
@overload
def to_instance(typeobj: None, *arg: Any, **kw: Any) -> TypeEngine[None]: ...
def adapt_type(typeobj: TypeEngine[Any], colspecs: Mapping[Type[Any], Type[TypeEngine[Any]]]) -> TypeEngine[Any]: ...
