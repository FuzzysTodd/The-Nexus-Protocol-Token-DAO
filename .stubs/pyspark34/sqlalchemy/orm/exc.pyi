from .. import exc as sa_exc, util as util
from ..exc import MultipleResultsFound as MultipleResultsFound, NoResultFound as NoResultFound
from .interfaces import LoaderStrategy as LoaderStrategy, MapperProperty as MapperProperty
from .state import InstanceState as InstanceState
from _typeshed import Incomplete
from typing import Any, Tuple, Type

NO_STATE: Incomplete

class StaleDataError(sa_exc.SQLAlchemyError):
    '''An operation encountered database state that is unaccounted for.

    Conditions which cause this to happen include:

    * A flush may have attempted to update or delete rows
      and an unexpected number of rows were matched during
      the UPDATE or DELETE statement.   Note that when
      version_id_col is used, rows in UPDATE or DELETE statements
      are also matched against the current known version
      identifier.

    * A mapped object with version_id_col was refreshed,
      and the version number coming back from the database does
      not match that of the object itself.

    * A object is detached from its parent object, however
      the object was previously attached to a different parent
      identity which was garbage collected, and a decision
      cannot be made if the new parent was really the most
      recent "parent".

    '''
ConcurrentModificationError = StaleDataError

class FlushError(sa_exc.SQLAlchemyError):
    """A invalid condition was detected during flush()."""
class UnmappedError(sa_exc.InvalidRequestError):
    """Base for exceptions that involve expected mappings not present."""
class ObjectDereferencedError(sa_exc.SQLAlchemyError):
    """An operation cannot complete due to an object being garbage
    collected.

    """

class DetachedInstanceError(sa_exc.SQLAlchemyError):
    """An attempt to access unloaded attributes on a
    mapped instance that is detached."""
    code: str

class UnmappedInstanceError(UnmappedError):
    """An mapping operation was requested for an unknown instance."""
    def __init__(self, obj: object, msg: str | None = None) -> None: ...
    def __reduce__(self) -> Any: ...

class UnmappedClassError(UnmappedError):
    """An mapping operation was requested for an unknown class."""
    def __init__(self, cls: Type[_T], msg: str | None = None) -> None: ...
    def __reduce__(self) -> Any: ...

class ObjectDeletedError(sa_exc.InvalidRequestError):
    """A refresh operation failed to retrieve the database
    row corresponding to an object's known primary key identity.

    A refresh operation proceeds when an expired attribute is
    accessed on an object, or when :meth:`_query.Query.get` is
    used to retrieve an object which is, upon retrieval, detected
    as expired.   A SELECT is emitted for the target row
    based on primary key; if no row is returned, this
    exception is raised.

    The true meaning of this exception is simply that
    no row exists for the primary key identifier associated
    with a persistent object.   The row may have been
    deleted, or in some cases the primary key updated
    to a new value, outside of the ORM's management of the target
    object.

    """
    def __init__(self, state: InstanceState[Any], msg: str | None = None) -> None: ...
    def __reduce__(self) -> Any: ...

class UnmappedColumnError(sa_exc.InvalidRequestError):
    """Mapping operation was requested on an unknown column."""

class LoaderStrategyException(sa_exc.InvalidRequestError):
    """A loader strategy for an attribute does not exist."""
    def __init__(self, applied_to_property_type: Type[Any], requesting_property: MapperProperty[Any], applies_to: Type[MapperProperty[Any]] | None, actual_strategy_type: Type[LoaderStrategy] | None, strategy_key: Tuple[Any, ...]) -> None: ...
