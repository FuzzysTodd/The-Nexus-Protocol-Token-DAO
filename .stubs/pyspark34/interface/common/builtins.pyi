from _typeshed import Incomplete
from zope.interface.common import collections, io, numbers

__all__ = ['IList', 'ITuple', 'ITextString', 'IByteString', 'INativeString', 'IBool', 'IDict', 'IFile']

class IList(collections.IMutableSequence):
    """
    Interface for :class:`list`
    """
    extra_classes: Incomplete
    def sort(key: Incomplete | None = None, reverse: bool = False) -> None:
        """
        Sort the list in place and return None.

        *key* and *reverse* must be passed by name only.
        """

class ITuple(collections.ISequence):
    """
    Interface for :class:`tuple`
    """
    extra_classes: Incomplete

class ITextString(collections.ISequence):
    '''
    Interface for text ("unicode") strings.

    This is :class:`str`
    '''
    extra_classes: Incomplete

class IByteString(collections.IByteString):
    """
    Interface for immutable byte strings.

    On all Python versions this is :class:`bytes`.

    Unlike :class:`zope.interface.common.collections.IByteString`
    (the parent of this interface) this does *not* include
    :class:`bytearray`.
    """
    extra_classes: Incomplete

class INativeString(ITextString):
    """
    Interface for native strings.

    On all Python versions, this is :class:`str`. Tt extends
    :class:`ITextString`.
    """

class IBool(numbers.IIntegral):
    """
    Interface for :class:`bool`
    """
    extra_classes: Incomplete

class IDict(collections.IMutableMapping):
    """
    Interface for :class:`dict`
    """
    extra_classes: Incomplete

class IFile(io.IIOBase):
    """
    Interface for :class:`file`.

    It is recommended to use the interfaces from :mod:`zope.interface.common.io`
    instead of this interface.

    On Python 3, there is no single implementation of this interface;
    depending on the arguments, the :func:`open` builtin can return
    many different classes that implement different interfaces from
    :mod:`zope.interface.common.io`.
    """
    extra_classes: Incomplete
