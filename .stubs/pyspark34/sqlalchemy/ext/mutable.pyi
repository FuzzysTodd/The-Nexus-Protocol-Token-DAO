from .. import event as event, inspect as inspect, types as types
from ..orm import Mapper as Mapper
from ..orm._typing import _O, _T
from ..orm.attributes import AttributeEventToken as AttributeEventToken, InstrumentedAttribute as InstrumentedAttribute, QueryableAttribute as QueryableAttribute, flag_modified as flag_modified
from ..orm.context import QueryContext as QueryContext
from ..orm.decl_api import DeclarativeAttributeIntercept as DeclarativeAttributeIntercept
from ..orm.state import InstanceState as InstanceState
from ..orm.unitofwork import UOWTransaction as UOWTransaction
from ..sql.base import SchemaEventTarget as SchemaEventTarget
from ..sql.schema import Column as Column
from ..sql.type_api import TypeEngine as TypeEngine
from ..util import memoized_property as memoized_property
from ..util.typing import SupportsIndex as SupportsIndex, TypeGuard as TypeGuard
from typing import AbstractSet, Any, Dict, Iterable, List, Set, Tuple, overload

class MutableBase:
    """Common base class to :class:`.Mutable`
    and :class:`.MutableComposite`.

    """
    @classmethod
    def coerce(cls, key: str, value: Any) -> Any | None:
        """Given a value, coerce it into the target type.

        Can be overridden by custom subclasses to coerce incoming
        data into a particular type.

        By default, raises ``ValueError``.

        This method is called in different scenarios depending on if
        the parent class is of type :class:`.Mutable` or of type
        :class:`.MutableComposite`.  In the case of the former, it is called
        for both attribute-set operations as well as during ORM loading
        operations.  For the latter, it is only called during attribute-set
        operations; the mechanics of the :func:`.composite` construct
        handle coercion during load operations.


        :param key: string name of the ORM-mapped attribute being set.
        :param value: the incoming value.
        :return: the method should return the coerced value, or raise
         ``ValueError`` if the coercion cannot be completed.

        """

class Mutable(MutableBase):
    """Mixin that defines transparent propagation of change
    events to a parent object.

    See the example in :ref:`mutable_scalars` for usage information.

    """
    def changed(self) -> None:
        """Subclasses should call this method whenever change events occur."""
    @classmethod
    def associate_with_attribute(cls, attribute: InstrumentedAttribute[_O]) -> None:
        """Establish this type as a mutation listener for the given
        mapped descriptor.

        """
    @classmethod
    def associate_with(cls, sqltype: type) -> None:
        """Associate this wrapper with all future mapped columns
        of the given type.

        This is a convenience method that calls
        ``associate_with_attribute`` automatically.

        .. warning::

           The listeners established by this method are *global*
           to all mappers, and are *not* garbage collected.   Only use
           :meth:`.associate_with` for types that are permanent to an
           application, not with ad-hoc types else this will cause unbounded
           growth in memory usage.

        """
    @classmethod
    def as_mutable(cls, sqltype: TypeEngine[_T]) -> TypeEngine[_T]:
        """Associate a SQL type with this mutable Python type.

        This establishes listeners that will detect ORM mappings against
        the given type, adding mutation event trackers to those mappings.

        The type is returned, unconditionally as an instance, so that
        :meth:`.as_mutable` can be used inline::

            Table('mytable', metadata,
                Column('id', Integer, primary_key=True),
                Column('data', MyMutableType.as_mutable(PickleType))
            )

        Note that the returned type is always an instance, even if a class
        is given, and that only columns which are declared specifically with
        that type instance receive additional instrumentation.

        To associate a particular mutable type with all occurrences of a
        particular type, use the :meth:`.Mutable.associate_with` classmethod
        of the particular :class:`.Mutable` subclass to establish a global
        association.

        .. warning::

           The listeners established by this method are *global*
           to all mappers, and are *not* garbage collected.   Only use
           :meth:`.as_mutable` for types that are permanent to an application,
           not with ad-hoc types else this will cause unbounded growth
           in memory usage.

        """

class MutableComposite(MutableBase):
    '''Mixin that defines transparent propagation of change
    events on a SQLAlchemy "composite" object to its
    owning parent or parents.

    See the example in :ref:`mutable_composites` for usage information.

    '''
    def changed(self) -> None:
        """Subclasses should call this method whenever change events occur."""

class MutableDict(Mutable, Dict[_KT, _VT]):
    '''A dictionary type that implements :class:`.Mutable`.

    The :class:`.MutableDict` object implements a dictionary that will
    emit change events to the underlying mapping when the contents of
    the dictionary are altered, including when values are added or removed.

    Note that :class:`.MutableDict` does **not** apply mutable tracking to  the
    *values themselves* inside the dictionary. Therefore it is not a sufficient
    solution for the use case of tracking deep changes to a *recursive*
    dictionary structure, such as a JSON structure.  To support this use case,
    build a subclass of  :class:`.MutableDict` that provides appropriate
    coercion to the values placed in the dictionary so that they too are
    "mutable", and emit events up to their parent structure.

    .. seealso::

        :class:`.MutableList`

        :class:`.MutableSet`

    '''
    def __setitem__(self, key: _KT, value: _VT) -> None:
        """Detect dictionary set events and emit change events."""
    @overload
    def setdefault(self, key: _KT, value: None = None) -> _T | None: ...
    @overload
    def setdefault(self, key: _KT, value: _VT) -> _VT: ...
    def __delitem__(self, key: _KT) -> None:
        """Detect dictionary del events and emit change events."""
    def update(self, *a: Any, **kw: _VT) -> None: ...
    @overload
    def pop(self, __key: _KT) -> _VT: ...
    @overload
    def pop(self, __key: _KT, __default: _VT | _T) -> _VT | _T: ...
    def popitem(self) -> Tuple[_KT, _VT]: ...
    def clear(self) -> None: ...
    @classmethod
    def coerce(cls, key: str, value: Any) -> MutableDict[_KT, _VT] | None:
        """Convert plain dictionary to instance of this class."""

class MutableList(Mutable, List[_T]):
    '''A list type that implements :class:`.Mutable`.

    The :class:`.MutableList` object implements a list that will
    emit change events to the underlying mapping when the contents of
    the list are altered, including when values are added or removed.

    Note that :class:`.MutableList` does **not** apply mutable tracking to  the
    *values themselves* inside the list. Therefore it is not a sufficient
    solution for the use case of tracking deep changes to a *recursive*
    mutable structure, such as a JSON structure.  To support this use case,
    build a subclass of  :class:`.MutableList` that provides appropriate
    coercion to the values placed in the dictionary so that they too are
    "mutable", and emit events up to their parent structure.

    .. seealso::

        :class:`.MutableDict`

        :class:`.MutableSet`

    '''
    def __reduce_ex__(self, proto: SupportsIndex) -> Tuple[type, Tuple[List[int]]]: ...
    def is_scalar(self, value: _T | Iterable[_T]) -> TypeGuard[_T]: ...
    def is_iterable(self, value: _T | Iterable[_T]) -> TypeGuard[Iterable[_T]]: ...
    def __setitem__(self, index: SupportsIndex | slice, value: _T | Iterable[_T]) -> None:
        """Detect list set events and emit change events."""
    def __delitem__(self, index: SupportsIndex | slice) -> None:
        """Detect list del events and emit change events."""
    def pop(self, *arg: SupportsIndex) -> _T: ...
    def append(self, x: _T) -> None: ...
    def extend(self, x: Iterable[_T]) -> None: ...
    def __iadd__(self, x: Iterable[_T]) -> MutableList[_T]: ...
    def insert(self, i: SupportsIndex, x: _T) -> None: ...
    def remove(self, i: _T) -> None: ...
    def clear(self) -> None: ...
    def sort(self, **kw: Any) -> None: ...
    def reverse(self) -> None: ...
    @classmethod
    def coerce(cls, key: str, value: MutableList[_T] | _T) -> MutableList[_T] | None:
        """Convert plain list to instance of this class."""

class MutableSet(Mutable, Set[_T]):
    '''A set type that implements :class:`.Mutable`.

    The :class:`.MutableSet` object implements a set that will
    emit change events to the underlying mapping when the contents of
    the set are altered, including when values are added or removed.

    Note that :class:`.MutableSet` does **not** apply mutable tracking to  the
    *values themselves* inside the set. Therefore it is not a sufficient
    solution for the use case of tracking deep changes to a *recursive*
    mutable structure.  To support this use case,
    build a subclass of  :class:`.MutableSet` that provides appropriate
    coercion to the values placed in the dictionary so that they too are
    "mutable", and emit events up to their parent structure.

    .. seealso::

        :class:`.MutableDict`

        :class:`.MutableList`


    '''
    def update(self, *arg: Iterable[_T]) -> None: ...
    def intersection_update(self, *arg: Iterable[Any]) -> None: ...
    def difference_update(self, *arg: Iterable[Any]) -> None: ...
    def symmetric_difference_update(self, *arg: Iterable[_T]) -> None: ...
    def __ior__(self, other: AbstractSet[_T]) -> MutableSet[_T]: ...
    def __iand__(self, other: AbstractSet[object]) -> MutableSet[_T]: ...
    def __ixor__(self, other: AbstractSet[_T]) -> MutableSet[_T]: ...
    def __isub__(self, other: AbstractSet[object]) -> MutableSet[_T]: ...
    def add(self, elem: _T) -> None: ...
    def remove(self, elem: _T) -> None: ...
    def discard(self, elem: _T) -> None: ...
    def pop(self, *arg: Any) -> _T: ...
    def clear(self) -> None: ...
    @classmethod
    def coerce(cls, index: str, value: Any) -> MutableSet[_T] | None:
        """Convert plain set to instance of this class."""
    def __reduce_ex__(self, proto: SupportsIndex) -> Tuple[type, Tuple[List[int]]]: ...
