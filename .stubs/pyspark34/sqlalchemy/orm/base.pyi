import typing
from . import exc as exc
from .. import inspection as inspection, util as util
from ..sql import roles as roles
from ..sql._typing import _ColumnExpressionArgument, _InfoType
from ..sql.elements import ColumnElement as ColumnElement, SQLColumnExpression as SQLColumnExpression, SQLCoreOperations as SQLCoreOperations
from ..sql.operators import OperatorType as OperatorType
from ..util import FastIntFlag as FastIntFlag
from ..util.langhelpers import TypingOnly as TypingOnly
from ..util.typing import Literal as Literal
from ._typing import _EntityType, insp_is_mapper as insp_is_mapper
from .attributes import InstrumentedAttribute as InstrumentedAttribute
from .dynamic import AppenderQuery as AppenderQuery
from .instrumentation import ClassManager as ClassManager
from .interfaces import PropComparator as PropComparator
from .mapper import Mapper as Mapper
from .state import InstanceState as InstanceState
from .util import AliasedClass as AliasedClass
from .writeonly import WriteOnlyCollection as WriteOnlyCollection
from _typeshed import Incomplete
from enum import Enum
from typing import Any, Dict, Generic, Type, overload

class LoaderCallableStatus(Enum):
    PASSIVE_NO_RESULT: int
    PASSIVE_CLASS_MISMATCH: int
    ATTR_WAS_SET: int
    ATTR_EMPTY: int
    NO_VALUE: int
    NEVER_SET = NO_VALUE

PASSIVE_NO_RESULT: Incomplete
PASSIVE_CLASS_MISMATCH: Incomplete
ATTR_WAS_SET: Incomplete
ATTR_EMPTY: Incomplete
NO_VALUE: Incomplete
NEVER_SET = NO_VALUE

class PassiveFlag(FastIntFlag):
    """Bitflag interface that passes options onto loader callables"""
    NO_CHANGE: int
    CALLABLES_OK: int
    SQL_OK: int
    RELATED_OBJECT_OK: int
    INIT_OK: int
    NON_PERSISTENT_OK: int
    LOAD_AGAINST_COMMITTED: int
    NO_AUTOFLUSH: int
    NO_RAISE: int
    DEFERRED_HISTORY_LOAD: int
    INCLUDE_PENDING_MUTATIONS: int
    PASSIVE_OFF: Incomplete
    PASSIVE_RETURN_NO_VALUE: Incomplete
    PASSIVE_NO_INITIALIZE: Incomplete
    PASSIVE_NO_FETCH: Incomplete
    PASSIVE_NO_FETCH_RELATED: Incomplete
    PASSIVE_ONLY_PERSISTENT: Incomplete
    PASSIVE_MERGE: Incomplete

NO_CHANGE: Incomplete
CALLABLES_OK: Incomplete
SQL_OK: Incomplete
RELATED_OBJECT_OK: Incomplete
INIT_OK: Incomplete
NON_PERSISTENT_OK: Incomplete
LOAD_AGAINST_COMMITTED: Incomplete
NO_AUTOFLUSH: Incomplete
NO_RAISE: Incomplete
DEFERRED_HISTORY_LOAD: Incomplete
INCLUDE_PENDING_MUTATIONS: Incomplete
PASSIVE_OFF: Incomplete
PASSIVE_RETURN_NO_VALUE: Incomplete
PASSIVE_NO_INITIALIZE: Incomplete
PASSIVE_NO_FETCH: Incomplete
PASSIVE_NO_FETCH_RELATED: Incomplete
PASSIVE_ONLY_PERSISTENT: Incomplete
PASSIVE_MERGE: Incomplete
DEFAULT_MANAGER_ATTR: str
DEFAULT_STATE_ATTR: str

class EventConstants(Enum):
    EXT_CONTINUE: int
    EXT_STOP: int
    EXT_SKIP: int
    NO_KEY: int

EXT_CONTINUE: Incomplete
EXT_STOP: Incomplete
EXT_SKIP: Incomplete
NO_KEY: Incomplete

class RelationshipDirection(Enum):
    """enumeration which indicates the 'direction' of a
    :class:`_orm.RelationshipProperty`.

    :class:`.RelationshipDirection` is accessible from the
    :attr:`_orm.Relationship.direction` attribute of
    :class:`_orm.RelationshipProperty`.

    """
    ONETOMANY: int
    MANYTOONE: int
    MANYTOMANY: int

ONETOMANY: Incomplete
MANYTOONE: Incomplete
MANYTOMANY: Incomplete

class InspectionAttrExtensionType(Enum):
    """Symbols indicating the type of extension that a
    :class:`.InspectionAttr` is part of."""

class NotExtension(InspectionAttrExtensionType):
    NOT_EXTENSION: str

def manager_of_class(cls) -> ClassManager[_O]: ...
@overload
def opt_manager_of_class(cls) -> None: ...
@overload
def opt_manager_of_class(cls) -> ClassManager[_O] | None: ...
def instance_state(instance: _O) -> InstanceState[_O]: ...
def instance_dict(instance: object) -> Dict[str, Any]: ...
def instance_str(instance: object) -> str:
    """Return a string describing an instance."""
def state_str(state: InstanceState[Any]) -> str:
    """Return a string describing an instance via its InstanceState."""
def state_class_str(state: InstanceState[Any]) -> str:
    """Return a string describing an instance's class via its
    InstanceState.
    """
def attribute_str(instance: object, attribute: str) -> str: ...
def state_attribute_str(state: InstanceState[Any], attribute: str) -> str: ...
def object_mapper(instance: _T) -> Mapper[_T]:
    """Given an object, return the primary Mapper associated with the object
    instance.

    Raises :class:`sqlalchemy.orm.exc.UnmappedInstanceError`
    if no mapping is configured.

    This function is available via the inspection system as::

        inspect(instance).mapper

    Using the inspection system will raise
    :class:`sqlalchemy.exc.NoInspectionAvailable` if the instance is
    not part of a mapping.

    """
def object_state(instance: _T) -> InstanceState[_T]:
    """Given an object, return the :class:`.InstanceState`
    associated with the object.

    Raises :class:`sqlalchemy.orm.exc.UnmappedInstanceError`
    if no mapping is configured.

    Equivalent functionality is available via the :func:`_sa.inspect`
    function as::

        inspect(instance)

    Using the inspection system will raise
    :class:`sqlalchemy.exc.NoInspectionAvailable` if the instance is
    not part of a mapping.

    """
def class_mapper(class_: Type[_O], configure: bool = True) -> Mapper[_O]:
    """Given a class, return the primary :class:`_orm.Mapper` associated
    with the key.

    Raises :exc:`.UnmappedClassError` if no mapping is configured
    on the given class, or :exc:`.ArgumentError` if a non-class
    object is passed.

    Equivalent functionality is available via the :func:`_sa.inspect`
    function as::

        inspect(some_mapped_class)

    Using the inspection system will raise
    :class:`sqlalchemy.exc.NoInspectionAvailable` if the class is not mapped.

    """

class InspectionAttr:
    """A base class applied to all ORM objects and attributes that are
    related to things that can be returned by the :func:`_sa.inspect` function.

    The attributes defined here allow the usage of simple boolean
    checks to test basic facts about the object returned.

    While the boolean checks here are basically the same as using
    the Python isinstance() function, the flags here can be used without
    the need to import all of these classes, and also such that
    the SQLAlchemy class system can change while leaving the flags
    here intact for forwards-compatibility.

    """
    is_selectable: bool
    is_aliased_class: bool
    is_instance: bool
    is_mapper: bool
    is_bundle: bool
    is_property: bool
    is_attribute: bool
    is_clause_element: bool
    extension_type: InspectionAttrExtensionType

class InspectionAttrInfo(InspectionAttr):
    """Adds the ``.info`` attribute to :class:`.InspectionAttr`.

    The rationale for :class:`.InspectionAttr` vs. :class:`.InspectionAttrInfo`
    is that the former is compatible as a mixin for classes that specify
    ``__slots__``; this is essentially an implementation artifact.

    """
    def info(self) -> _InfoType:
        """Info dictionary associated with the object, allowing user-defined
        data to be associated with this :class:`.InspectionAttr`.

        The dictionary is generated when first accessed.  Alternatively,
        it can be specified as a constructor argument to the
        :func:`.column_property`, :func:`_orm.relationship`, or
        :func:`.composite`
        functions.

        .. seealso::

            :attr:`.QueryableAttribute.info`

            :attr:`.SchemaItem.info`

        """

class SQLORMOperations(SQLCoreOperations[_T_co], TypingOnly):
    def of_type(self, class_: _EntityType[Any]) -> PropComparator[_T_co]: ...
    def and_(self, *criteria: _ColumnExpressionArgument[bool]) -> PropComparator[bool]: ...
    def any(self, criterion: _ColumnExpressionArgument[bool] | None = None, **kwargs: Any) -> ColumnElement[bool]: ...
    def has(self, criterion: _ColumnExpressionArgument[bool] | None = None, **kwargs: Any) -> ColumnElement[bool]: ...

class ORMDescriptor(TypingOnly, Generic[_T_co]):
    """Represent any Python descriptor that provides a SQL expression
    construct at the class level."""
    @overload
    def __get__(self, instance: Any, owner: Literal[None]) -> ORMDescriptor[_T_co]: ...
    @overload
    def __get__(self, instance: Literal[None], owner: Any) -> SQLCoreOperations[_T_co]: ...
    @overload
    def __get__(self, instance: object, owner: Any) -> _T_co: ...

class _MappedAnnotationBase(TypingOnly, Generic[_T_co]):
    """common class for Mapped and similar ORM container classes.

    these are classes that can appear on the left side of an ORM declarative
    mapping, containing a mapped class or in some cases a collection
    surrounding a mapped class.

    """
class SQLORMExpression(SQLORMOperations[_T_co], SQLColumnExpression[_T_co], TypingOnly):
    """A type that may be used to indicate any ORM-level attribute or
    object that acts in place of one, in the context of SQL expression
    construction.

    :class:`.SQLORMExpression` extends from the Core
    :class:`.SQLColumnExpression` to add additional SQL methods that are ORM
    specific, such as :meth:`.PropComparator.of_type`, and is part of the bases
    for :class:`.InstrumentedAttribute`. It may be used in :pep:`484` typing to
    indicate arguments or return values that should behave as ORM-level
    attribute expressions.

    .. versionadded:: 2.0.0b4


    """

class Mapped(SQLORMExpression[_T_co], ORMDescriptor[_T_co], _MappedAnnotationBase[_T_co], roles.DDLConstraintColumnRole):
    """Represent an ORM mapped attribute on a mapped class.

    This class represents the complete descriptor interface for any class
    attribute that will have been :term:`instrumented` by the ORM
    :class:`_orm.Mapper` class.   Provides appropriate information to type
    checkers such as pylance and mypy so that ORM-mapped attributes
    are correctly typed.

    The most prominent use of :class:`_orm.Mapped` is in
    the :ref:`Declarative Mapping <orm_explicit_declarative_base>` form
    of :class:`_orm.Mapper` configuration, where used explicitly it drives
    the configuration of ORM attributes such as :func:`_orm.mapped_class`
    and :func:`_orm.relationship`.

    .. seealso::

        :ref:`orm_explicit_declarative_base`

        :ref:`orm_declarative_table`

    .. tip::

        The :class:`_orm.Mapped` class represents attributes that are handled
        directly by the :class:`_orm.Mapper` class. It does not include other
        Python descriptor classes that are provided as extensions, including
        :ref:`hybrids_toplevel` and the :ref:`associationproxy_toplevel`.
        While these systems still make use of ORM-specific superclasses
        and structures, they are not :term:`instrumented` by the
        :class:`_orm.Mapper` and instead provide their own functionality
        when they are accessed on a class.

    .. versionadded:: 1.4


    """
    @overload
    def __get__(self, instance: None, owner: Any) -> InstrumentedAttribute[_T_co]: ...
    @overload
    def __get__(self, instance: object, owner: Any) -> _T_co: ...
    def __set__(self, instance: Any, value: SQLCoreOperations[_T_co] | _T_co) -> None: ...
    def __delete__(self, instance: Any) -> None: ...

class _MappedAttribute(TypingOnly, Generic[_T_co]):
    """Mixin for attributes which should be replaced by mapper-assigned
    attributes.

    """

class _DeclarativeMapped(Mapped[_T_co], _MappedAttribute[_T_co]):
    """Mixin for :class:`.MapperProperty` subclasses that allows them to
    be compatible with ORM-annotated declarative mappings.

    """
    def operate(self, op: OperatorType, *other: Any, **kwargs: Any) -> Any: ...
    __sa_operate__ = operate
    def reverse_operate(self, op: OperatorType, other: Any, **kwargs: Any) -> Any: ...

class DynamicMapped(_MappedAnnotationBase[_T_co]):
    '''Represent the ORM mapped attribute type for a "dynamic" relationship.

    The :class:`_orm.DynamicMapped` type annotation may be used in an
    :ref:`Annotated Declarative Table <orm_declarative_mapped_column>` mapping
    to indicate that the ``lazy="dynamic"`` loader strategy should be used
    for a particular :func:`_orm.relationship`.

    .. legacy::  The "dynamic" lazy loader strategy is the legacy form of what
       is now the "write_only" strategy described in the section
       :ref:`write_only_relationship`.

    E.g.::

        class User(Base):
            __tablename__ = "user"
            id: Mapped[int] = mapped_column(primary_key=True)
            addresses: DynamicMapped[Address] = relationship(
                cascade="all,delete-orphan"
            )

    See the section :ref:`dynamic_relationship` for background.

    .. versionadded:: 2.0

    .. seealso::

        :ref:`dynamic_relationship` - complete background

        :class:`.WriteOnlyMapped` - fully 2.0 style version

    '''
    @overload
    def __get__(self, instance: None, owner: Any) -> InstrumentedAttribute[_T_co]: ...
    @overload
    def __get__(self, instance: object, owner: Any) -> AppenderQuery[_T_co]: ...
    def __set__(self, instance: Any, value: typing.Collection[_T_co]) -> None: ...

class WriteOnlyMapped(_MappedAnnotationBase[_T_co]):
    '''Represent the ORM mapped attribute type for a "write only" relationship.

    The :class:`_orm.WriteOnlyMapped` type annotation may be used in an
    :ref:`Annotated Declarative Table <orm_declarative_mapped_column>` mapping
    to indicate that the ``lazy="write_only"`` loader strategy should be used
    for a particular :func:`_orm.relationship`.

    E.g.::

        class User(Base):
            __tablename__ = "user"
            id: Mapped[int] = mapped_column(primary_key=True)
            addresses: WriteOnlyMapped[Address] = relationship(
                cascade="all,delete-orphan"
            )

    See the section :ref:`write_only_relationship` for background.

    .. versionadded:: 2.0

    .. seealso::

        :ref:`write_only_relationship` - complete background

        :class:`.DynamicMapped` - includes legacy :class:`_orm.Query` support

    '''
    @overload
    def __get__(self, instance: None, owner: Any) -> InstrumentedAttribute[_T_co]: ...
    @overload
    def __get__(self, instance: object, owner: Any) -> WriteOnlyCollection[_T_co]: ...
    def __set__(self, instance: Any, value: typing.Collection[_T_co]) -> None: ...
