from _typeshed import Incomplete
from collections import abc
from zope.interface.common import ABCInterface

__all__ = ['IAsyncGenerator', 'IAsyncIterable', 'IAsyncIterator', 'IAwaitable', 'ICollection', 'IContainer', 'ICoroutine', 'IGenerator', 'IHashable', 'IItemsView', 'IIterable', 'IIterator', 'IKeysView', 'IMapping', 'IMappingView', 'IMutableMapping', 'IMutableSequence', 'IMutableSet', 'IReversible', 'ISequence', 'ISet', 'ISized', 'IValuesView']

class IContainer(ABCInterface):
    abc = abc.Container
    def __contains__(other) -> bool:
        """
        Optional method. If not provided, the interpreter will use
        ``__iter__`` or the old ``__getitem__`` protocol
        to implement ``in``.
        """

class IHashable(ABCInterface):
    abc = abc.Hashable

class IIterable(ABCInterface):
    abc = abc.Iterable
    def __iter__():
        """
        Optional method. If not provided, the interpreter will
        implement `iter` using the old ``__getitem__`` protocol.
        """

class IIterator(IIterable):
    abc = abc.Iterator

class IReversible(IIterable):
    abc: Incomplete
    def __reversed__() -> None:
        """
        Optional method. If this isn't present, the interpreter
        will use ``__len__`` and ``__getitem__`` to implement the
        `reversed` builtin.
        """

class IGenerator(IIterator):
    abc: Incomplete

class ISized(ABCInterface):
    abc = abc.Sized

class ICollection(ISized, IIterable, IContainer):
    abc: Incomplete

class ISequence(IReversible, ICollection):
    abc = abc.Sequence
    extra_classes: Incomplete
    ignored_classes: Incomplete
    def __reversed__() -> None:
        """
        Optional method. If this isn't present, the interpreter
        will use ``__len__`` and ``__getitem__`` to implement the
        `reversed` builtin.
        """
    def __iter__():
        """
        Optional method. If not provided, the interpreter will
        implement `iter` using the old ``__getitem__`` protocol.
        """

class IMutableSequence(ISequence):
    abc = abc.MutableSequence
    extra_classes: Incomplete

class IByteString(ISequence):
    """
    This unifies `bytes` and `bytearray`.
    """
    abc: Incomplete

class ISet(ICollection):
    abc = abc.Set

class IMutableSet(ISet):
    abc = abc.MutableSet

class IMapping(ICollection):
    abc = abc.Mapping
    extra_classes: Incomplete
    ignored_classes: Incomplete

class IMutableMapping(IMapping):
    abc = abc.MutableMapping
    extra_classes: Incomplete
    ignored_classes: Incomplete

class IMappingView(ISized):
    abc = abc.MappingView

class IItemsView(IMappingView, ISet):
    abc = abc.ItemsView

class IKeysView(IMappingView, ISet):
    abc = abc.KeysView

class IValuesView(IMappingView, ICollection):
    abc = abc.ValuesView
    def __contains__(other) -> bool:
        """
        Optional method. If not provided, the interpreter will use
        ``__iter__`` or the old ``__len__`` and ``__getitem__`` protocol
        to implement ``in``.
        """

class IAwaitable(ABCInterface):
    abc: Incomplete

class ICoroutine(IAwaitable):
    abc: Incomplete

class IAsyncIterable(ABCInterface):
    abc: Incomplete

class IAsyncIterator(IAsyncIterable):
    abc: Incomplete

class IAsyncGenerator(IAsyncIterator):
    abc: Incomplete
