from . import AttributeEventToken as AttributeEventToken, Mapper as Mapper, base as base
from .. import util as util
from ..sql import coercions as coercions, expression as expression, roles as roles
from ..sql.elements import ColumnElement as ColumnElement
from ..util.typing import Literal as Literal
from .collections import CollectionAdapter as CollectionAdapter, collection as collection, collection_adapter as collection_adapter
from _typeshed import Incomplete
from typing import Any, Callable, Dict, Generic, Sequence, Tuple, Type

class _PlainColumnGetter(Generic[_KT]):
    """Plain column getter, stores collection of Column objects
    directly.

    Serializes to a :class:`._SerializableColumnGetterV2`
    which has more expensive __call__() performance
    and some rare caveats.

    """
    cols: Incomplete
    composite: Incomplete
    def __init__(self, cols: Sequence[ColumnElement[_KT]]) -> None: ...
    def __reduce__(self) -> Tuple[Type[_SerializableColumnGetterV2[_KT]], Tuple[Sequence[Tuple[str | None, str | None]]]]: ...
    def __call__(self, value: _KT) -> _KT | Tuple[_KT, ...]: ...

class _SerializableColumnGetterV2(_PlainColumnGetter[_KT]):
    """Updated serializable getter which deals with
    multi-table mapped classes.

    Two extremely unusual cases are not supported.
    Mappings which have tables across multiple metadata
    objects, or which are mapped to non-Table selectables
    linked across inheriting mappers may fail to function
    here.

    """
    colkeys: Incomplete
    composite: Incomplete
    def __init__(self, colkeys: Sequence[Tuple[str | None, str | None]]) -> None: ...
    def __reduce__(self) -> Tuple[Type[_SerializableColumnGetterV2[_KT]], Tuple[Sequence[Tuple[str | None, str | None]]]]: ...

def column_keyed_dict(mapping_spec: Type[_KT] | Callable[[_KT], _VT], *, ignore_unpopulated_attribute: bool = False) -> Type[KeyFuncDict[_KT, _KT]]:
    """A dictionary-based collection type with column-based keying.

    .. versionchanged:: 2.0 Renamed :data:`.column_mapped_collection` to
       :class:`.column_keyed_dict`.

    Returns a :class:`.KeyFuncDict` factory which will produce new
    dictionary keys based on the value of a particular :class:`.Column`-mapped
    attribute on ORM mapped instances to be added to the dictionary.

    .. note:: the value of the target attribute must be assigned with its
       value at the time that the object is being added to the
       dictionary collection.   Additionally, changes to the key attribute
       are **not tracked**, which means the key in the dictionary is not
       automatically synchronized with the key value on the target object
       itself.  See :ref:`key_collections_mutations` for further details.

    .. seealso::

        :ref:`orm_dictionary_collection` - background on use

    :param mapping_spec: a :class:`_schema.Column` object that is expected
     to be mapped by the target mapper to a particular attribute on the
     mapped class, the value of which on a particular instance is to be used
     as the key for a new dictionary entry for that instance.
    :param ignore_unpopulated_attribute:  if True, and the mapped attribute
     indicated by the given :class:`_schema.Column` target attribute
     on an object is not populated at all, the operation will be silently
     skipped.  By default, an error is raised.

     .. versionadded:: 2.0 an error is raised by default if the attribute
        being used for the dictionary key is determined that it was never
        populated with any value.  The
        :paramref:`_orm.column_keyed_dict.ignore_unpopulated_attribute`
        parameter may be set which will instead indicate that this condition
        should be ignored, and the append operation silently skipped.
        This is in contrast to the behavior of the 1.x series which would
        erroneously populate the value in the dictionary with an arbitrary key
        value of ``None``.


    """

class _AttrGetter:
    attr_name: Incomplete
    getter: Incomplete
    def __init__(self, attr_name: str) -> None: ...
    def __call__(self, mapped_object: Any) -> Any: ...
    def __reduce__(self) -> Tuple[Type[_AttrGetter], Tuple[str]]: ...

def attribute_keyed_dict(attr_name: str, *, ignore_unpopulated_attribute: bool = False) -> Type[KeyFuncDict[_KT, _KT]]:
    """A dictionary-based collection type with attribute-based keying.

    .. versionchanged:: 2.0 Renamed :data:`.attribute_mapped_collection` to
       :func:`.attribute_keyed_dict`.

    Returns a :class:`.KeyFuncDict` factory which will produce new
    dictionary keys based on the value of a particular named attribute on
    ORM mapped instances to be added to the dictionary.

    .. note:: the value of the target attribute must be assigned with its
       value at the time that the object is being added to the
       dictionary collection.   Additionally, changes to the key attribute
       are **not tracked**, which means the key in the dictionary is not
       automatically synchronized with the key value on the target object
       itself.  See :ref:`key_collections_mutations` for further details.

    .. seealso::

        :ref:`orm_dictionary_collection` - background on use

    :param attr_name: string name of an ORM-mapped attribute
     on the mapped class, the value of which on a particular instance
     is to be used as the key for a new dictionary entry for that instance.
    :param ignore_unpopulated_attribute:  if True, and the target attribute
     on an object is not populated at all, the operation will be silently
     skipped.  By default, an error is raised.

     .. versionadded:: 2.0 an error is raised by default if the attribute
        being used for the dictionary key is determined that it was never
        populated with any value.  The
        :paramref:`_orm.attribute_keyed_dict.ignore_unpopulated_attribute`
        parameter may be set which will instead indicate that this condition
        should be ignored, and the append operation silently skipped.
        This is in contrast to the behavior of the 1.x series which would
        erroneously populate the value in the dictionary with an arbitrary key
        value of ``None``.


    """
def keyfunc_mapping(keyfunc: _F, *, ignore_unpopulated_attribute: bool = False) -> Type[KeyFuncDict[_KT, Any]]:
    """A dictionary-based collection type with arbitrary keying.

    .. versionchanged:: 2.0 Renamed :data:`.mapped_collection` to
       :func:`.keyfunc_mapping`.

    Returns a :class:`.KeyFuncDict` factory with a keying function
    generated from keyfunc, a callable that takes an entity and returns a
    key value.

    .. note:: the given keyfunc is called only once at the time that the
       target object is being added to the collection.   Changes to the
       effective value returned by the function are not tracked.


    .. seealso::

        :ref:`orm_dictionary_collection` - background on use

    :param keyfunc: a callable that will be passed the ORM-mapped instance
     which should then generate a new key to use in the dictionary.
     If the value returned is :attr:`.LoaderCallableStatus.NO_VALUE`, an error
     is raised.
    :param ignore_unpopulated_attribute:  if True, and the callable returns
     :attr:`.LoaderCallableStatus.NO_VALUE` for a particular instance, the
     operation will be silently skipped.  By default, an error is raised.

     .. versionadded:: 2.0 an error is raised by default if the callable
        being used for the dictionary key returns
        :attr:`.LoaderCallableStatus.NO_VALUE`, which in an ORM attribute
        context indicates an attribute that was never populated with any value.
        The :paramref:`_orm.mapped_collection.ignore_unpopulated_attribute`
        parameter may be set which will instead indicate that this condition
        should be ignored, and the append operation silently skipped. This is
        in contrast to the behavior of the 1.x series which would erroneously
        populate the value in the dictionary with an arbitrary key value of
        ``None``.


    """

class KeyFuncDict(Dict[_KT, _VT]):
    """Base for ORM mapped dictionary classes.

    Extends the ``dict`` type with additional methods needed by SQLAlchemy ORM
    collection classes. Use of :class:`_orm.KeyFuncDict` is most directly
    by using the :func:`.attribute_keyed_dict` or
    :func:`.column_keyed_dict` class factories.
    :class:`_orm.KeyFuncDict` may also serve as the base for user-defined
    custom dictionary classes.

    .. versionchanged:: 2.0 Renamed :class:`.MappedCollection` to
       :class:`.KeyFuncDict`.

    .. seealso::

        :func:`_orm.attribute_keyed_dict`

        :func:`_orm.column_keyed_dict`

        :ref:`orm_dictionary_collection`

        :ref:`orm_custom_collection`


    """
    keyfunc: Incomplete
    ignore_unpopulated_attribute: Incomplete
    def __init__(self, keyfunc: _F, *dict_args: Any, ignore_unpopulated_attribute: bool = False) -> None:
        '''Create a new collection with keying provided by keyfunc.

        keyfunc may be any callable that takes an object and returns an object
        for use as a dictionary key.

        The keyfunc will be called every time the ORM needs to add a member by
        value-only (such as when loading instances from the database) or
        remove a member.  The usual cautions about dictionary keying apply-
        ``keyfunc(object)`` should return the same output for the life of the
        collection.  Keying based on mutable properties can result in
        unreachable instances "lost" in the collection.

        '''
    def __reduce__(self) -> Tuple[Callable[[_KT, _KT], KeyFuncDict[_KT, _KT]], Tuple[Any, Dict[_KT, _KT] | Dict[_KT, _KT], CollectionAdapter]]: ...
    def set(self, value: _KT, _sa_initiator: AttributeEventToken | Literal[None, False] = None) -> None:
        """Add an item by value, consulting the keyfunc for the key."""
    def remove(self, value: _KT, _sa_initiator: AttributeEventToken | Literal[None, False] = None) -> None:
        """Remove an item by value, consulting the keyfunc for the key."""
MappedCollection = KeyFuncDict
mapped_collection = keyfunc_mapping
attribute_mapped_collection = attribute_keyed_dict
column_mapped_collection = column_keyed_dict
