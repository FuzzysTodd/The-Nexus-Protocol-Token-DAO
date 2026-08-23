from _typeshed import Incomplete
from zope.interface.interface import InterfaceClass

class optional:
    __doc__: Incomplete
    def __init__(self, method) -> None: ...

class ABCInterfaceClass(InterfaceClass):
    """
    An interface that is automatically derived from a
    :class:`abc.ABCMeta` type.

    Internal use only.

    The body of the interface definition *must* define
    a property ``abc`` that is the ABC to base the interface on.

    If ``abc`` is *not* in the interface definition, a regular
    interface will be defined instead (but ``extra_classes`` is still
    respected).

    Use the ``@optional`` decorator on method definitions if
    the ABC defines methods that are not actually required in all cases
    because the Python language has multiple ways to implement a protocol.
    For example, the ``iter()`` protocol can be implemented with
    ``__iter__`` or the pair ``__len__`` and ``__getitem__``.

    When created, any existing classes that are registered to conform
    to the ABC are declared to implement this interface. This is *not*
    automatically updated as the ABC registry changes. If the body of the
    interface definition defines ``extra_classes``, it should be a
    tuple giving additional classes to declare implement the interface.

    Note that this is not fully symmetric. For example, it is usually
    the case that a subclass relationship carries the interface
    declarations over::

        >>> from zope.interface import Interface
        >>> class I1(Interface):
        ...     pass
        ...
        >>> from zope.interface import implementer
        >>> @implementer(I1)
        ... class Root(object):
        ...     pass
        ...
        >>> class Child(Root):
        ...     pass
        ...
        >>> child = Child()
        >>> isinstance(child, Root)
        True
        >>> from zope.interface import providedBy
        >>> list(providedBy(child))
        [<InterfaceClass __main__.I1>]

    However, that's not the case with ABCs and ABC interfaces. Just
    because ``isinstance(A(), AnABC)`` and ``isinstance(B(), AnABC)``
    are both true, that doesn't mean there's any class hierarchy
    relationship between ``A`` and ``B``, or between either of them
    and ``AnABC``. Thus, if ``AnABC`` implemented ``IAnABC``, it would
    not follow that either ``A`` or ``B`` implements ``IAnABC`` (nor
    their instances provide it)::

        >>> class SizedClass(object):
        ...     def __len__(self): return 1
        ...
        >>> from collections.abc import Sized
        >>> isinstance(SizedClass(), Sized)
        True
        >>> from zope.interface import classImplements
        >>> classImplements(Sized, I1)
        None
        >>> list(providedBy(SizedClass()))
        []

    Thus, to avoid conflicting assumptions, ABCs should not be
    declared to implement their parallel ABC interface. Only concrete
    classes specifically registered with the ABC should be declared to
    do so.

    .. versionadded:: 5.0.0
    """
    __class__: Incomplete
    def __init__(self, name, bases, attrs) -> None: ...
    def getABC(self):
        """
        Return the ABC this interface represents.
        """
    def getRegisteredConformers(self):
        """
        Return an iterable of the classes that are known to conform to
        the ABC this interface parallels.
        """

ABCInterface: Incomplete
