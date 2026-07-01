from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['InterfaceClass', 'Specification', 'adapter_hooks']

class Element:
    """
    Default implementation of `zope.interface.interfaces.IElement`.
    """
    __doc__: Incomplete
    def __init__(self, __name__, __doc__: str = '') -> None: ...
    def getName(self):
        """ Returns the name of the object. """
    def getDoc(self):
        """ Returns the documentation for the object. """
    def getTaggedValue(self, tag):
        """ Returns the value associated with 'tag'. """
    def queryTaggedValue(self, tag, default: Incomplete | None = None):
        """ Returns the value associated with 'tag'. """
    def getTaggedValueTags(self):
        """ Returns a collection of all tags. """
    def setTaggedValue(self, tag, value) -> None:
        """ Associates 'value' with 'key'. """
    queryDirectTaggedValue = queryTaggedValue
    getDirectTaggedValue = getTaggedValue
    getDirectTaggedValueTags = getTaggedValueTags
SpecificationBasePy = object

class SpecificationBase:
    def providedBy(self, ob):
        """Is the interface implemented by an object
        """
    def implementedBy(self, cls):
        """Test whether the specification is implemented by a class or factory.

        Raise TypeError if argument is neither a class nor a callable.
        """
    def isOrExtends(self, interface):
        """Is the interface the same as or extend the given interface
        """
    __call__ = isOrExtends

class NameAndModuleComparisonMixin:
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class InterfaceBase(NameAndModuleComparisonMixin, SpecificationBasePy):
    """Base class that wants to be replaced with a C base :)
    """
    __ibmodule__: Incomplete
    def __init__(self, name: Incomplete | None = None, module: Incomplete | None = None) -> None: ...
    @property
    def __module_property__(self): ...
    def __call__(self, obj, alternate=...):
        """Adapt an object to the interface
        """
    def __adapt__(self, obj):
        """Adapt an object to the receiver
        """
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

adapter_hooks: Incomplete

class Specification(SpecificationBase):
    """Specifications

    An interface specification is used to track interface declarations
    and component registrations.

    This class is a base class for both interfaces themselves and for
    interface specifications (declarations).

    Specifications are mutable.  If you reassign their bases, their
    relations with other specifications are adjusted accordingly.
    """
    isOrExtends: Incomplete
    providedBy: Incomplete
    __iro__: Incomplete
    __sro__: Incomplete
    __bases__: Incomplete
    def __init__(self, bases=()) -> None: ...
    @property
    def dependents(self): ...
    def subscribe(self, dependent) -> None: ...
    def unsubscribe(self, dependent) -> None: ...
    def changed(self, originally_changed) -> None:
        """
        We, or something we depend on, have changed.

        By the time this is called, the things we depend on,
        such as our bases, should themselves be stable.
        """
    def interfaces(self) -> Generator[Incomplete, None, None]:
        """Return an iterator for the interfaces in the specification.
        """
    def extends(self, interface, strict: bool = True):
        """Does the specification extend the given interface?

        Test whether an interface in the specification extends the
        given interface
        """
    def weakref(self, callback: Incomplete | None = None): ...
    def get(self, name, default: Incomplete | None = None):
        """Query for an attribute description
        """

class _InterfaceMetaClass(type):
    def __new__(cls, name, bases, attrs): ...
    @property
    def __module__(cls): ...

class InterfaceClass(_InterfaceClassBase):
    """
    Prototype (scarecrow) Interfaces Implementation.

    Note that it is not possible to change the ``__name__`` or ``__module__``
    after an instance of this object has been constructed.
    """
    def __new__(cls, name: Incomplete | None = None, bases=(), attrs: Incomplete | None = None, __doc__: Incomplete | None = None, __module__: Incomplete | None = None): ...
    __identifier__: Incomplete
    def __init__(self, name, bases=(), attrs: Incomplete | None = None, __doc__: Incomplete | None = None, __module__: Incomplete | None = None) -> None: ...
    def interfaces(self) -> Generator[Incomplete, None, None]:
        """Return an iterator for the interfaces in the specification.
        """
    def getBases(self): ...
    def isEqualOrExtendedBy(self, other):
        """Same interface or extends?"""
    def names(self, all: bool = False):
        """Return the attribute names defined by the interface."""
    def __iter__(self): ...
    def namesAndDescriptions(self, all: bool = False):
        """Return attribute names and descriptions defined by interface."""
    def getDescriptionFor(self, name):
        """Return the attribute description for the given name."""
    __getitem__ = getDescriptionFor
    def __contains__(self, name) -> bool: ...
    def direct(self, name): ...
    def queryDescriptionFor(self, name, default: Incomplete | None = None): ...
    def validateInvariants(self, obj, errors: Incomplete | None = None) -> None:
        """validate object to defined invariants."""
    def queryTaggedValue(self, tag, default: Incomplete | None = None):
        """
        Queries for the value associated with *tag*, returning it from the nearest
        interface in the ``__iro__``.

        If not found, returns *default*.
        """
    def getTaggedValue(self, tag):
        """ Returns the value associated with 'tag'. """
    def getTaggedValueTags(self):
        """ Returns a list of all tags. """
    def __reduce__(self): ...

class _InterfaceClassWithCustomMethods(InterfaceClass):
    """
    Marker class for interfaces with custom methods that override InterfaceClass methods.
    """

class Attribute(Element):
    """Attribute descriptions
    """
    interface: Incomplete

class Method(Attribute):
    """Method interfaces

    The idea here is that you have objects that describe methods.
    This provides an opportunity for rich meta-data.
    """
    positional: Incomplete
    required: Incomplete
    varargs: Incomplete
    kwargs: Incomplete
    optional: Incomplete
    def __call__(self, *args, **kw) -> None: ...
    def getSignatureInfo(self): ...
    def getSignatureString(self): ...
