from .engine.interfaces import Dialect as Dialect, _AnyExecuteParams
from .sql.compiler import Compiled as Compiled, TypeCompiler as TypeCompiler
from .sql.elements import ClauseElement as ClauseElement
from .util import compat as compat
from _typeshed import Incomplete
from typing import Any, Tuple, Type, overload

class HasDescriptionCode:
    """helper which adds 'code' as an attribute and '_code_str' as a method"""
    code: str | None
    def __init__(self, *arg: Any, **kw: Any) -> None: ...

class SQLAlchemyError(HasDescriptionCode, Exception):
    """Generic error class."""
class ArgumentError(SQLAlchemyError):
    """Raised when an invalid or conflicting function argument is supplied.

    This error generally corresponds to construction time state errors.

    """
class DuplicateColumnError(ArgumentError):
    """a Column is being added to a Table that would replace another
    Column, without appropriate parameters to allow this in place.

    .. versionadded:: 2.0.0b4

    """

class ObjectNotExecutableError(ArgumentError):
    """Raised when an object is passed to .execute() that can't be
    executed as SQL.

    """
    target: Incomplete
    def __init__(self, target: Any) -> None: ...
    def __reduce__(self) -> str | Tuple[Any, ...]: ...

class NoSuchModuleError(ArgumentError):
    """Raised when a dynamically-loaded module (usually a database dialect)
    of a particular name cannot be located."""
class NoForeignKeysError(ArgumentError):
    """Raised when no foreign keys can be located between two selectables
    during a join."""
class AmbiguousForeignKeysError(ArgumentError):
    """Raised when more than one foreign key matching can be located
    between two selectables during a join."""
class ConstraintColumnNotFoundError(ArgumentError):
    """raised when a constraint refers to a string column name that
    is not present in the table being constrained.

    .. versionadded:: 2.0

    """

class CircularDependencyError(SQLAlchemyError):
    """Raised by topological sorts when a circular dependency is detected.

    There are two scenarios where this error occurs:

    * In a Session flush operation, if two objects are mutually dependent
      on each other, they can not be inserted or deleted via INSERT or
      DELETE statements alone; an UPDATE will be needed to post-associate
      or pre-deassociate one of the foreign key constrained values.
      The ``post_update`` flag described at :ref:`post_update` can resolve
      this cycle.
    * In a :attr:`_schema.MetaData.sorted_tables` operation, two
      :class:`_schema.ForeignKey`
      or :class:`_schema.ForeignKeyConstraint` objects mutually refer to each
      other.  Apply the ``use_alter=True`` flag to one or both,
      see :ref:`use_alter`.

    """
    cycles: Incomplete
    edges: Incomplete
    def __init__(self, message: str, cycles: Any, edges: Any, msg: str | None = None, code: str | None = None) -> None: ...
    def __reduce__(self) -> str | Tuple[Any, ...]: ...

class CompileError(SQLAlchemyError):
    """Raised when an error occurs during SQL compilation"""

class UnsupportedCompilationError(CompileError):
    """Raised when an operation is not supported by the given compiler.

    .. seealso::

        :ref:`faq_sql_expression_string`

        :ref:`error_l7de`
    """
    code: str
    compiler: Incomplete
    element_type: Incomplete
    message: Incomplete
    def __init__(self, compiler: Compiled | TypeCompiler, element_type: Type[ClauseElement], message: str | None = None) -> None: ...
    def __reduce__(self) -> str | Tuple[Any, ...]: ...

class IdentifierError(SQLAlchemyError):
    """Raised when a schema name is beyond the max character limit"""

class DisconnectionError(SQLAlchemyError):
    """A disconnect is detected on a raw DB-API connection.

    This error is raised and consumed internally by a connection pool.  It can
    be raised by the :meth:`_events.PoolEvents.checkout`
    event so that the host pool
    forces a retry; the exception will be caught three times in a row before
    the pool gives up and raises :class:`~sqlalchemy.exc.InvalidRequestError`
    regarding the connection attempt.

    """
    invalidate_pool: bool

class InvalidatePoolError(DisconnectionError):
    """Raised when the connection pool should invalidate all stale connections.

    A subclass of :class:`_exc.DisconnectionError` that indicates that the
    disconnect situation encountered on the connection probably means the
    entire pool should be invalidated, as the database has been restarted.

    This exception will be handled otherwise the same way as
    :class:`_exc.DisconnectionError`, allowing three attempts to reconnect
    before giving up.

    .. versionadded:: 1.2

    """
    invalidate_pool: bool

class TimeoutError(SQLAlchemyError):
    """Raised when a connection pool times out on getting a connection."""
class InvalidRequestError(SQLAlchemyError):
    """SQLAlchemy was asked to do something it can't do.

    This error generally corresponds to runtime state errors.

    """
class IllegalStateChangeError(InvalidRequestError):
    """An object that tracks state encountered an illegal state change
    of some kind.

    .. versionadded:: 2.0

    """
class NoInspectionAvailable(InvalidRequestError):
    """A subject passed to :func:`sqlalchemy.inspection.inspect` produced
    no context for inspection."""
class PendingRollbackError(InvalidRequestError):
    """A transaction has failed and needs to be rolled back before
    continuing.

    .. versionadded:: 1.4

    """
class ResourceClosedError(InvalidRequestError):
    """An operation was requested from a connection, cursor, or other
    object that's in a closed state."""
class NoSuchColumnError(InvalidRequestError, KeyError):
    """A nonexistent column is requested from a ``Row``."""
class NoResultFound(InvalidRequestError):
    """A database result was required but none was found.


    .. versionchanged:: 1.4  This exception is now part of the
       ``sqlalchemy.exc`` module in Core, moved from the ORM.  The symbol
       remains importable from ``sqlalchemy.orm.exc``.


    """
class MultipleResultsFound(InvalidRequestError):
    """A single database result was required but more than one were found.

    .. versionchanged:: 1.4  This exception is now part of the
       ``sqlalchemy.exc`` module in Core, moved from the ORM.  The symbol
       remains importable from ``sqlalchemy.orm.exc``.


    """

class NoReferenceError(InvalidRequestError):
    """Raised by ``ForeignKey`` to indicate a reference cannot be resolved."""
    table_name: str

class AwaitRequired(InvalidRequestError):
    """Error raised by the async greenlet spawn if no async operation
    was awaited when it required one.

    """
    code: str

class MissingGreenlet(InvalidRequestError):
    """Error raised by the async greenlet await\\_ if called while not inside
    the greenlet spawn context.

    """
    code: str

class NoReferencedTableError(NoReferenceError):
    """Raised by ``ForeignKey`` when the referred ``Table`` cannot be
    located.

    """
    table_name: Incomplete
    def __init__(self, message: str, tname: str) -> None: ...
    def __reduce__(self) -> str | Tuple[Any, ...]: ...

class NoReferencedColumnError(NoReferenceError):
    """Raised by ``ForeignKey`` when the referred ``Column`` cannot be
    located.

    """
    table_name: Incomplete
    column_name: Incomplete
    def __init__(self, message: str, tname: str, cname: str) -> None: ...
    def __reduce__(self) -> str | Tuple[Any, ...]: ...

class NoSuchTableError(InvalidRequestError):
    """Table does not exist or is not visible to a connection."""
class UnreflectableTableError(InvalidRequestError):
    """Table exists but can't be reflected for some reason.

    .. versionadded:: 1.2

    """
class UnboundExecutionError(InvalidRequestError):
    """SQL was attempted without a database connection to execute it on."""
class DontWrapMixin:
    '''A mixin class which, when applied to a user-defined Exception class,
    will not be wrapped inside of :exc:`.StatementError` if the error is
    emitted within the process of executing a statement.

    E.g.::

        from sqlalchemy.exc import DontWrapMixin

        class MyCustomException(Exception, DontWrapMixin):
            pass

        class MySpecialType(TypeDecorator):
            impl = String

            def process_bind_param(self, value, dialect):
                if value == \'invalid\':
                    raise MyCustomException("invalid!")

    '''

class StatementError(SQLAlchemyError):
    """An error occurred during execution of a SQL statement.

    :class:`StatementError` wraps the exception raised
    during execution, and features :attr:`.statement`
    and :attr:`.params` attributes which supply context regarding
    the specifics of the statement which had an issue.

    The wrapped exception object is available in
    the :attr:`.orig` attribute.

    """
    statement: str | None
    params: _AnyExecuteParams | None
    orig: BaseException | None
    ismulti: bool | None
    connection_invalidated: bool
    hide_parameters: Incomplete
    detail: Incomplete
    def __init__(self, message: str, statement: str | None, params: _AnyExecuteParams | None, orig: BaseException | None, hide_parameters: bool = False, code: str | None = None, ismulti: bool | None = None) -> None: ...
    def add_detail(self, msg: str) -> None: ...
    def __reduce__(self) -> str | Tuple[Any, ...]: ...

class DBAPIError(StatementError):
    """Raised when the execution of a database operation fails.

    Wraps exceptions raised by the DB-API underlying the
    database operation.  Driver-specific implementations of the standard
    DB-API exception types are wrapped by matching sub-types of SQLAlchemy's
    :class:`DBAPIError` when possible.  DB-API's ``Error`` type maps to
    :class:`DBAPIError` in SQLAlchemy, otherwise the names are identical.  Note
    that there is no guarantee that different DB-API implementations will
    raise the same exception type for any given error condition.

    :class:`DBAPIError` features :attr:`~.StatementError.statement`
    and :attr:`~.StatementError.params` attributes which supply context
    regarding the specifics of the statement which had an issue, for the
    typical case when the error was raised within the context of
    emitting a SQL statement.

    The wrapped exception object is available in the
    :attr:`~.StatementError.orig` attribute. Its type and properties are
    DB-API implementation specific.

    """
    code: str
    @overload
    @classmethod
    def instance(cls, statement: str | None, params: _AnyExecuteParams | None, orig: Exception, dbapi_base_err: Type[Exception], hide_parameters: bool = False, connection_invalidated: bool = False, dialect: Dialect | None = None, ismulti: bool | None = None) -> StatementError: ...
    @overload
    @classmethod
    def instance(cls, statement: str | None, params: _AnyExecuteParams | None, orig: DontWrapMixin, dbapi_base_err: Type[Exception], hide_parameters: bool = False, connection_invalidated: bool = False, dialect: Dialect | None = None, ismulti: bool | None = None) -> DontWrapMixin: ...
    @overload
    @classmethod
    def instance(cls, statement: str | None, params: _AnyExecuteParams | None, orig: BaseException, dbapi_base_err: Type[Exception], hide_parameters: bool = False, connection_invalidated: bool = False, dialect: Dialect | None = None, ismulti: bool | None = None) -> BaseException: ...
    def __reduce__(self) -> str | Tuple[Any, ...]: ...
    connection_invalidated: Incomplete
    def __init__(self, statement: str | None, params: _AnyExecuteParams | None, orig: BaseException, hide_parameters: bool = False, connection_invalidated: bool = False, code: str | None = None, ismulti: bool | None = None) -> None: ...

class InterfaceError(DBAPIError):
    """Wraps a DB-API InterfaceError."""
    code: str

class DatabaseError(DBAPIError):
    """Wraps a DB-API DatabaseError."""
    code: str

class DataError(DatabaseError):
    """Wraps a DB-API DataError."""
    code: str

class OperationalError(DatabaseError):
    """Wraps a DB-API OperationalError."""
    code: str

class IntegrityError(DatabaseError):
    """Wraps a DB-API IntegrityError."""
    code: str

class InternalError(DatabaseError):
    """Wraps a DB-API InternalError."""
    code: str

class ProgrammingError(DatabaseError):
    """Wraps a DB-API ProgrammingError."""
    code: str

class NotSupportedError(DatabaseError):
    """Wraps a DB-API NotSupportedError."""
    code: str

class SATestSuiteWarning(Warning):
    """warning for a condition detected during tests that is non-fatal

    Currently outside of SAWarning so that we can work around tools like
    Alembic doing the wrong thing with warnings.

    """

class SADeprecationWarning(HasDescriptionCode, DeprecationWarning):
    """Issued for usage of deprecated APIs."""
    deprecated_since: str | None

class Base20DeprecationWarning(SADeprecationWarning):
    """Issued for usage of APIs specifically deprecated or legacy in
    SQLAlchemy 2.0.

    .. seealso::

        :ref:`error_b8d9`.

        :ref:`deprecation_20_mode`

    """
    deprecated_since: str | None

class LegacyAPIWarning(Base20DeprecationWarning):
    """indicates an API that is in 'legacy' status, a long term deprecation."""
class MovedIn20Warning(Base20DeprecationWarning):
    """Subtype of RemovedIn20Warning to indicate an API that moved only."""

class SAPendingDeprecationWarning(PendingDeprecationWarning):
    """A similar warning as :class:`_exc.SADeprecationWarning`, this warning
    is not used in modern versions of SQLAlchemy.

    """
    deprecated_since: str | None

class SAWarning(HasDescriptionCode, RuntimeWarning):
    """Issued at runtime."""
