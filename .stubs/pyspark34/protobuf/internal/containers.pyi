from _typeshed import Incomplete
from typing import Any, Iterable, Iterator, List, MutableMapping, MutableSequence, NoReturn, Sequence, overload

class BaseContainer(Sequence[_T]):
    """Base container class."""
    def __init__(self, message_listener: Any) -> None:
        """
    Args:
      message_listener: A MessageListener implementation.
        The RepeatedScalarFieldContainer will call this object's
        Modified() method when it is modified.
    """
    @overload
    def __getitem__(self, key: int) -> _T: ...
    @overload
    def __getitem__(self, key: slice) -> List[_T]: ...
    def __len__(self) -> int:
        """Returns the number of elements in the container."""
    def __ne__(self, other: Any) -> bool:
        """Checks if another instance isn't equal to this one."""
    __hash__: Incomplete
    def sort(self, *args, **kwargs) -> None: ...
    def reverse(self) -> None: ...

class RepeatedScalarFieldContainer(BaseContainer[_T], MutableSequence[_T]):
    """Simple, type-checked, list-like container for holding repeated scalars."""
    def __init__(self, message_listener: Any, type_checker: Any) -> None:
        """Args:

      message_listener: A MessageListener implementation. The
      RepeatedScalarFieldContainer will call this object's Modified() method
      when it is modified.
      type_checker: A type_checkers.ValueChecker instance to run on elements
      inserted into this container.
    """
    def append(self, value: _T) -> None:
        """Appends an item to the list. Similar to list.append()."""
    def insert(self, key: int, value: _T) -> None:
        """Inserts the item at the specified position. Similar to list.insert()."""
    def extend(self, elem_seq: Iterable[_T]) -> None:
        """Extends by appending the given iterable. Similar to list.extend()."""
    def MergeFrom(self, other: RepeatedScalarFieldContainer[_T] | Iterable[_T]) -> None:
        """Appends the contents of another repeated field of the same type to this
    one. We do not check the types of the individual fields.
    """
    def remove(self, elem: _T):
        """Removes an item from the list. Similar to list.remove()."""
    def pop(self, key: int | None = -1) -> _T:
        """Removes and returns an item at a given index. Similar to list.pop()."""
    @overload
    def __setitem__(self, key: int, value: _T) -> None: ...
    @overload
    def __setitem__(self, key: slice, value: Iterable[_T]) -> None: ...
    def __delitem__(self, key: int | slice) -> None:
        """Deletes the item at the specified position."""
    def __eq__(self, other: Any) -> bool:
        """Compares the current instance with another one."""
    def __deepcopy__(self, unused_memo: Any = None) -> RepeatedScalarFieldContainer[_T]: ...
    def __reduce__(self, **kwargs) -> NoReturn: ...

class RepeatedCompositeFieldContainer(BaseContainer[_T], MutableSequence[_T]):
    """Simple, list-like container for holding repeated composite fields."""
    def __init__(self, message_listener: Any, message_descriptor: Any) -> None:
        """
    Note that we pass in a descriptor instead of the generated directly,
    since at the time we construct a _RepeatedCompositeFieldContainer we
    haven't yet necessarily initialized the type that will be contained in the
    container.

    Args:
      message_listener: A MessageListener implementation.
        The RepeatedCompositeFieldContainer will call this object's
        Modified() method when it is modified.
      message_descriptor: A Descriptor instance describing the protocol type
        that should be present in this container.  We'll use the
        _concrete_class field of this descriptor when the client calls add().
    """
    def add(self, **kwargs: Any) -> _T:
        """Adds a new element at the end of the list and returns it. Keyword
    arguments may be used to initialize the element.
    """
    def append(self, value: _T) -> None:
        """Appends one element by copying the message."""
    def insert(self, key: int, value: _T) -> None:
        """Inserts the item at the specified position by copying."""
    def extend(self, elem_seq: Iterable[_T]) -> None:
        """Extends by appending the given sequence of elements of the same type

    as this one, copying each individual message.
    """
    def MergeFrom(self, other: RepeatedCompositeFieldContainer[_T] | Iterable[_T]) -> None:
        """Appends the contents of another repeated field of the same type to this
    one, copying each individual message.
    """
    def remove(self, elem: _T) -> None:
        """Removes an item from the list. Similar to list.remove()."""
    def pop(self, key: int | None = -1) -> _T:
        """Removes and returns an item at a given index. Similar to list.pop()."""
    @overload
    def __setitem__(self, key: int, value: _T) -> None: ...
    @overload
    def __setitem__(self, key: slice, value: Iterable[_T]) -> None: ...
    def __delitem__(self, key: int | slice) -> None:
        """Deletes the item at the specified position."""
    def __eq__(self, other: Any) -> bool:
        """Compares the current instance with another one."""

class ScalarMap(MutableMapping[_K, _V]):
    """Simple, type-checked, dict-like container for holding repeated scalars."""
    def __init__(self, message_listener: Any, key_checker: Any, value_checker: Any, entry_descriptor: Any) -> None:
        """
    Args:
      message_listener: A MessageListener implementation.
        The ScalarMap will call this object's Modified() method when it
        is modified.
      key_checker: A type_checkers.ValueChecker instance to run on keys
        inserted into this container.
      value_checker: A type_checkers.ValueChecker instance to run on values
        inserted into this container.
      entry_descriptor: The MessageDescriptor of a map entry: key and value.
    """
    def __getitem__(self, key: _K) -> _V: ...
    def __contains__(self, item: _K) -> bool: ...
    @overload
    def get(self, key: _K) -> _V | None: ...
    @overload
    def get(self, key: _K, default: _T) -> _V | _T: ...
    def __setitem__(self, key: _K, value: _V) -> _T: ...
    def __delitem__(self, key: _K) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_K]: ...
    def MergeFrom(self, other: ScalarMap[_K, _V]) -> None: ...
    def InvalidateIterators(self) -> None: ...
    def clear(self) -> None: ...
    def GetEntryClass(self) -> Any: ...

class MessageMap(MutableMapping[_K, _V]):
    """Simple, type-checked, dict-like container for with submessage values."""
    def __init__(self, message_listener: Any, message_descriptor: Any, key_checker: Any, entry_descriptor: Any) -> None:
        """
    Args:
      message_listener: A MessageListener implementation.
        The ScalarMap will call this object's Modified() method when it
        is modified.
      key_checker: A type_checkers.ValueChecker instance to run on keys
        inserted into this container.
      value_checker: A type_checkers.ValueChecker instance to run on values
        inserted into this container.
      entry_descriptor: The MessageDescriptor of a map entry: key and value.
    """
    def __getitem__(self, key: _K) -> _V: ...
    def get_or_create(self, key: _K) -> _V:
        """get_or_create() is an alias for getitem (ie. map[key]).

    Args:
      key: The key to get or create in the map.

    This is useful in cases where you want to be explicit that the call is
    mutating the map.  This can avoid lint errors for statements like this
    that otherwise would appear to be pointless statements:

      msg.my_map[key]
    """
    @overload
    def get(self, key: _K) -> _V | None: ...
    @overload
    def get(self, key: _K, default: _T) -> _V | _T: ...
    def __contains__(self, item: _K) -> bool: ...
    def __setitem__(self, key: _K, value: _V) -> NoReturn: ...
    def __delitem__(self, key: _K) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_K]: ...
    def MergeFrom(self, other: MessageMap[_K, _V]) -> None: ...
    def InvalidateIterators(self) -> None: ...
    def clear(self) -> None: ...
    def GetEntryClass(self) -> Any: ...

class _UnknownField:
    """A parsed unknown field."""
    def __init__(self, field_number, wire_type, data) -> None: ...
    def __lt__(self, other): ...
    def __eq__(self, other): ...

class UnknownFieldRef:
    def __init__(self, parent, index) -> None: ...
    @property
    def field_number(self): ...
    @property
    def wire_type(self): ...
    @property
    def data(self): ...

class UnknownFieldSet:
    """UnknownField container"""
    def __init__(self) -> None: ...
    def __getitem__(self, index): ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __eq__(self, other): ...
