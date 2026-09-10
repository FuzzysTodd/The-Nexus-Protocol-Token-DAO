import typing
from ..util import deprecated as deprecated
from ..util._has_cy import HAS_CYEXTENSION as HAS_CYEXTENSION
from ._py_row import BaseRow as BaseRow
from .result import RMKeyView as RMKeyView, _KeyType
from _typeshed import Incomplete
from abc import ABC
from typing import Any, Generic, Iterator, Mapping, NoReturn, Sequence, overload

class Row(BaseRow, Sequence[Any], Generic[_TP]):
    '''Represent a single result row.

    The :class:`.Row` object represents a row of a database result.  It is
    typically associated in the 1.x series of SQLAlchemy with the
    :class:`_engine.CursorResult` object, however is also used by the ORM for
    tuple-like results as of SQLAlchemy 1.4.

    The :class:`.Row` object seeks to act as much like a Python named
    tuple as possible.   For mapping (i.e. dictionary) behavior on a row,
    such as testing for containment of keys, refer to the :attr:`.Row._mapping`
    attribute.

    .. seealso::

        :ref:`tutorial_selecting_data` - includes examples of selecting
        rows from SELECT statements.

    .. versionchanged:: 1.4

        Renamed ``RowProxy`` to :class:`.Row`. :class:`.Row` is no longer a
        "proxy" object in that it contains the final form of data within it,
        and now acts mostly like a named tuple. Mapping-like functionality is
        moved to the :attr:`.Row._mapping` attribute. See
        :ref:`change_4710_core` for background on this change.

    '''
    def __setattr__(self, name: str, value: Any) -> NoReturn: ...
    def __delattr__(self, name: str) -> NoReturn: ...
    def tuple(self) -> _TP:
        """Return a 'tuple' form of this :class:`.Row`.

        .. versionadded:: 2.0

        """
    @property
    def t(self) -> _TP:
        """A synonym for :meth:`.Row._tuple`.

        .. versionadded:: 2.0

        """
    def __contains__(self, key: Any) -> bool: ...
    __hash__: Incomplete
    @overload
    def __getitem__(self, index: int) -> Any: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[Any]: ...
    def __lt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
BaseRowProxy = BaseRow
RowProxy = Row

class ROMappingView(ABC):
    def __init__(self, mapping: Mapping['_KeyType', Any], items: Sequence[Any]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __contains__(self, item: Any) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

class ROMappingKeysValuesView(ROMappingView, typing.KeysView['_KeyType'], typing.ValuesView[Any]): ...
class ROMappingItemsView(ROMappingView, typing.ItemsView['_KeyType', Any]): ...

class RowMapping(BaseRow, typing.Mapping['_KeyType', Any]):
    '''A ``Mapping`` that maps column names and objects to :class:`.Row`
    values.

    The :class:`.RowMapping` is available from a :class:`.Row` via the
    :attr:`.Row._mapping` attribute, as well as from the iterable interface
    provided by the :class:`.MappingResult` object returned by the
    :meth:`_engine.Result.mappings` method.

    :class:`.RowMapping` supplies Python mapping (i.e. dictionary) access to
    the  contents of the row.   This includes support for testing of
    containment of specific keys (string column names or objects), as well
    as iteration of keys, values, and items::

        for row in result:
            if \'a\' in row._mapping:
                print("Column \'a\': %s" % row._mapping[\'a\'])

            print("Column b: %s" % row._mapping[table.c.b])


    .. versionadded:: 1.4 The :class:`.RowMapping` object replaces the
       mapping-like access previously provided by a database result row,
       which now seeks to behave mostly like a named tuple.

    '''
    def __getitem__(self, key: _KeyType) -> Any: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __contains__(self, key: object) -> bool: ...
    def items(self) -> ROMappingItemsView:
        """Return a view of key/value tuples for the elements in the
        underlying :class:`.Row`.

        """
    def keys(self) -> RMKeyView:
        """Return a view of 'keys' for string column names represented
        by the underlying :class:`.Row`.

        """
    def values(self) -> ROMappingKeysValuesView:
        """Return a view of values for the values represented in the
        underlying :class:`.Row`.

        """
