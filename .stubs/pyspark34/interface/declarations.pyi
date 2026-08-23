from _typeshed import Incomplete
from zope.interface.interface import NameAndModuleComparisonMixin, Specification, SpecificationBase

__docformat__: str
BuiltinImplementationSpecifications: Incomplete

class named:
    name: Incomplete
    def __init__(self, name) -> None: ...
    def __call__(self, ob): ...

class Declaration(Specification):
    """Interface declarations"""
    def __init__(self, *bases) -> None: ...
    def __contains__(self, interface) -> bool:
        """Test whether an interface is in the specification
        """
    def __iter__(self):
        """Return an iterator for the interfaces in the specification
        """
    def flattened(self):
        """Return an iterator of all included and extended interfaces
        """
    def __sub__(self, other):
        """Remove interfaces from a specification
        """
    def __add__(self, other):
        """
        Add two specifications or a specification and an interface
        and produce a new declaration.

        .. versionchanged:: 5.4.0
           Now tries to preserve a consistent resolution order. Interfaces
           being added to this object are added to the front of the resulting resolution
           order if they already extend an interface in this object. Previously,
           they were always added to the end of the order, which easily resulted in
           invalid orders.
        """
    __radd__ = __add__

class _ImmutableDeclaration(Declaration):
    def __new__(cls): ...
    def __reduce__(self): ...
    @property
    def __bases__(self): ...
    @__bases__.setter
    def __bases__(self, new_bases) -> None: ...
    @property
    def dependents(self): ...
    changed: Incomplete
    subscribe: Incomplete
    unsubscribe: Incomplete
    def interfaces(self): ...
    def extends(self, interface, strict: bool = True): ...
    def get(self, name, default: Incomplete | None = None): ...
    def weakref(self, callback: Incomplete | None = None): ...

class Implements(NameAndModuleComparisonMixin, Declaration):
    inherit: Incomplete
    declared: Incomplete
    @classmethod
    def named(cls, name, *bases): ...
    def changed(self, originally_changed): ...
    def __reduce__(self): ...

def implementedBy(cls):
    """Return the interfaces implemented for a class' instances

      The value returned is an `~zope.interface.interfaces.IDeclaration`.
    """
def classImplementsOnly(cls, *interfaces) -> None:
    """
    Declare the only interfaces implemented by instances of a class

    The arguments after the class are one or more interfaces or interface
    specifications (`~zope.interface.interfaces.IDeclaration` objects).

    The interfaces given (including the interfaces in the specifications)
    replace any previous declarations, *including* inherited definitions. If you
    wish to preserve inherited declarations, you can pass ``implementedBy(cls)``
    in *interfaces*. This can be used to alter the interface resolution order.
    """
def classImplements(cls, *interfaces) -> None:
    """
    Declare additional interfaces implemented for instances of a class

    The arguments after the class are one or more interfaces or
    interface specifications (`~zope.interface.interfaces.IDeclaration` objects).

    The interfaces given (including the interfaces in the specifications)
    are added to any interfaces previously declared. An effort is made to
    keep a consistent C3 resolution order, but this cannot be guaranteed.

    .. versionchanged:: 5.0.0
       Each individual interface in *interfaces* may be added to either the
       beginning or end of the list of interfaces declared for *cls*,
       based on inheritance, in order to try to maintain a consistent
       resolution order. Previously, all interfaces were added to the end.
    .. versionchanged:: 5.1.0
       If *cls* is already declared to implement an interface (or derived interface)
       in *interfaces* through inheritance, the interface is ignored. Previously, it
       would redundantly be made direct base of *cls*, which often produced inconsistent
       interface resolution orders. Now, the order will be consistent, but may change.
       Also, if the ``__bases__`` of the *cls* are later changed, the *cls* will no
       longer be considered to implement such an interface (changing the ``__bases__`` of *cls*
       has never been supported).
    """
def classImplementsFirst(cls, iface) -> None:
    """
    Declare that instances of *cls* additionally provide *iface*.

    The second argument is an interface or interface specification.
    It is added as the highest priority (first in the IRO) interface;
    no attempt is made to keep a consistent resolution order.

    .. versionadded:: 5.0.0
    """

class implementer:
    """
    Declare the interfaces implemented by instances of a class.

    This function is called as a class decorator.

    The arguments are one or more interfaces or interface
    specifications (`~zope.interface.interfaces.IDeclaration`
    objects).

    The interfaces given (including the interfaces in the
    specifications) are added to any interfaces previously declared,
    unless the interface is already implemented.

    Previous declarations include declarations for base classes unless
    implementsOnly was used.

    This function is provided for convenience. It provides a more
    convenient way to call `classImplements`. For example::

        @implementer(I1)
        class C(object):
            pass

    is equivalent to calling::

        classImplements(C, I1)

    after the class has been created.

    .. seealso:: `classImplements`
       The change history provided there applies to this function too.
    """
    interfaces: Incomplete
    def __init__(self, *interfaces) -> None: ...
    def __call__(self, ob): ...

class implementer_only:
    """Declare the only interfaces implemented by instances of a class

      This function is called as a class decorator.

      The arguments are one or more interfaces or interface
      specifications (`~zope.interface.interfaces.IDeclaration` objects).

      Previous declarations including declarations for base classes
      are overridden.

      This function is provided for convenience. It provides a more
      convenient way to call `classImplementsOnly`. For example::

        @implementer_only(I1)
        class C(object): pass

      is equivalent to calling::

        classImplementsOnly(I1)

      after the class has been created.
      """
    interfaces: Incomplete
    def __init__(self, *interfaces) -> None: ...
    def __call__(self, ob): ...

class Provides(Declaration):
    """Implement ``__provides__``, the instance-specific specification

    When an object is pickled, we pickle the interfaces that it implements.
    """
    def __init__(self, cls, *interfaces) -> None: ...
    def __reduce__(self): ...
    __module__: str
    def __get__(self, inst, cls):
        """Make sure that a class __provides__ doesn't leak to an instance
        """
ProvidesClass = Provides
InstanceDeclarations: Incomplete

def directlyProvides(object, *interfaces) -> None:
    """Declare interfaces declared directly for an object

      The arguments after the object are one or more interfaces or interface
      specifications (`~zope.interface.interfaces.IDeclaration` objects).

      The interfaces given (including the interfaces in the specifications)
      replace interfaces previously declared for the object.
    """
def alsoProvides(object, *interfaces) -> None:
    """Declare interfaces declared directly for an object

    The arguments after the object are one or more interfaces or interface
    specifications (`~zope.interface.interfaces.IDeclaration` objects).

    The interfaces given (including the interfaces in the specifications) are
    added to the interfaces previously declared for the object.
    """
def noLongerProvides(object, interface) -> None:
    """ Removes a directly provided interface from an object.
    """

class ClassProvidesBase(SpecificationBase):
    def __get__(self, inst, cls): ...

class ClassProvides(Declaration, ClassProvidesBase):
    """Special descriptor for class ``__provides__``

    The descriptor caches the implementedBy info, so that
    we can get declarations for objects without instance-specific
    interfaces a bit quicker.
    """
    def __init__(self, cls, metacls, *interfaces) -> None: ...
    def __reduce__(self): ...
    __get__: Incomplete

def directlyProvidedBy(object):
    """Return the interfaces directly provided by the given object

    The value returned is an `~zope.interface.interfaces.IDeclaration`.
    """

class provider:
    """Declare interfaces provided directly by a class

      This function is called in a class definition.

      The arguments are one or more interfaces or interface specifications
      (`~zope.interface.interfaces.IDeclaration` objects).

      The given interfaces (including the interfaces in the specifications)
      are used to create the class's direct-object interface specification.
      An error will be raised if the module class has an direct interface
      specification. In other words, it is an error to call this function more
      than once in a class definition.

      Note that the given interfaces have nothing to do with the interfaces
      implemented by instances of the class.

      This function is provided for convenience. It provides a more convenient
      way to call `directlyProvides` for a class. For example::

        @provider(I1)
        class C:
            pass

      is equivalent to calling::

        directlyProvides(C, I1)

      after the class has been created.
    """
    interfaces: Incomplete
    def __init__(self, *interfaces) -> None: ...
    def __call__(self, ob): ...

def moduleProvides(*interfaces) -> None:
    """Declare interfaces provided by a module

    This function is used in a module definition.

    The arguments are one or more interfaces or interface specifications
    (`~zope.interface.interfaces.IDeclaration` objects).

    The given interfaces (including the interfaces in the specifications) are
    used to create the module's direct-object interface specification.  An
    error will be raised if the module already has an interface specification.
    In other words, it is an error to call this function more than once in a
    module definition.

    This function is provided for convenience. It provides a more convenient
    way to call directlyProvides. For example::

      moduleProvides(I1)

    is equivalent to::

      directlyProvides(sys.modules[__name__], I1)
    """
def ObjectSpecification(direct, cls):
    """Provide object specifications

    These combine information for the object and for it's classes.
    """
def getObjectSpecification(ob): ...
def providedBy(ob):
    """
    Return the interfaces provided by *ob*.

    If *ob* is a :class:`super` object, then only interfaces implemented
    by the remainder of the classes in the method resolution order are
    considered. Interfaces directly provided by the object underlying *ob*
    are not.
    """

class ObjectSpecificationDescriptor:
    """Implement the ``__providedBy__`` attribute

    The ``__providedBy__`` attribute computes the interfaces provided by
    an object. If an object has an ``__provides__`` attribute, that is returned.
    Otherwise, `implementedBy` the *cls* is returned.

    .. versionchanged:: 5.4.0
       Both the default (C) implementation and the Python implementation
       now let exceptions raised by accessing ``__provides__`` propagate.
       Previously, the C version ignored all exceptions.
    .. versionchanged:: 5.4.0
       The Python implementation now matches the C implementation and lets
       a ``__provides__`` of ``None`` override what the class is declared to
       implement.
    """
    def __get__(self, inst, cls):
        """Get an object specification for an object
        """

objectSpecificationDescriptor: Incomplete
