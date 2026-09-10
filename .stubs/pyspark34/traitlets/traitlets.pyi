import enum
import typing as t
from .utils.bunch import Bunch
from .utils.sentinel import Sentinel
from _typeshed import Incomplete
from collections.abc import Generator
from typing_extensions import Literal, Self

__all__ = ['All', 'Any', 'BaseDescriptor', 'Bool', 'Bytes', 'CBool', 'CBytes', 'CComplex', 'CFloat', 'CInt', 'CLong', 'CRegExp', 'CUnicode', 'Callable', 'CaselessStrEnum', 'ClassBasedTraitType', 'Complex', 'Container', 'DefaultHandler', 'Dict', 'DottedObjectName', 'Enum', 'EventHandler', 'Float', 'ForwardDeclaredInstance', 'ForwardDeclaredMixin', 'ForwardDeclaredType', 'FuzzyEnum', 'HasDescriptors', 'HasTraits', 'Instance', 'Int', 'Integer', 'List', 'Long', 'MetaHasDescriptors', 'MetaHasTraits', 'ObjectName', 'ObserveHandler', 'Set', 'TCPAddress', 'This', 'TraitError', 'TraitType', 'Tuple', 'Type', 'Unicode', 'Undefined', 'Union', 'UseEnum', 'ValidateHandler', 'default', 'directional_link', 'dlink', 'link', 'observe', 'observe_compat', 'parse_notifier_name', 'validate']

Undefined: Incomplete
All: Incomplete
NoDefaultSpecified = Undefined

class TraitError(Exception): ...

def parse_notifier_name(names: Sentinel | str | t.Iterable[Sentinel | str]) -> t.Iterable[t.Any]:
    '''Convert the name argument to a list of names.

    Examples
    --------
    >>> parse_notifier_name([])
    [traitlets.All]
    >>> parse_notifier_name("a")
    [\'a\']
    >>> parse_notifier_name(["a", "b"])
    [\'a\', \'b\']
    >>> parse_notifier_name(All)
    [traitlets.All]
    '''

class _SimpleTest:
    value: Incomplete
    def __init__(self, value: t.Any) -> None: ...
    def __call__(self, test: t.Any) -> bool: ...

class link:
    '''Link traits from different objects together so they remain in sync.

    Parameters
    ----------
    source : (object / attribute name) pair
    target : (object / attribute name) pair
    transform: iterable with two callables (optional)
        Data transformation between source and target and target and source.

    Examples
    --------
    >>> class X(HasTraits):
    ...     value = Int()

    >>> src = X(value=1)
    >>> tgt = X(value=42)
    >>> c = link((src, "value"), (tgt, "value"))

    Setting source updates target objects:
    >>> src.value = 5
    >>> tgt.value
    5
    '''
    updating: bool
    def __init__(self, source: t.Any, target: t.Any, transform: t.Any = None) -> None: ...
    def link(self) -> None: ...
    def unlink(self) -> None: ...

class directional_link:
    '''Link the trait of a source object with traits of target objects.

    Parameters
    ----------
    source : (object, attribute name) pair
    target : (object, attribute name) pair
    transform: callable (optional)
        Data transformation between source and target.

    Examples
    --------
    >>> class X(HasTraits):
    ...     value = Int()

    >>> src = X(value=1)
    >>> tgt = X(value=42)
    >>> c = directional_link((src, "value"), (tgt, "value"))

    Setting source updates target objects:
    >>> src.value = 5
    >>> tgt.value
    5

    Setting target does not update source object:
    >>> tgt.value = 6
    >>> src.value
    5

    '''
    updating: bool
    def __init__(self, source: t.Any, target: t.Any, transform: t.Any = None) -> None: ...
    def link(self) -> None: ...
    def unlink(self) -> None: ...
dlink = directional_link

class BaseDescriptor:
    """Base descriptor class

    Notes
    -----
    This implements Python's descriptor protocol.

    This class is the base class for all such descriptors.  The
    only magic we use is a custom metaclass for the main :class:`HasTraits`
    class that does the following:

    1. Sets the :attr:`name` attribute of every :class:`BaseDescriptor`
       instance in the class dict to the name of the attribute.
    2. Sets the :attr:`this_class` attribute of every :class:`BaseDescriptor`
       instance in the class dict to the *class* that declared the trait.
       This is used by the :class:`This` trait to allow subclasses to
       accept superclasses for :class:`This` values.
    """
    name: str | None
    this_class: type[HasTraits] | None
    def class_init(self, cls: type[HasTraits], name: str | None) -> None:
        """Part of the initialization which may depend on the underlying
        HasDescriptors class.

        It is typically overloaded for specific types.

        This method is called by :meth:`MetaHasDescriptors.__init__`
        passing the class (`cls`) and `name` under which the descriptor
        has been assigned.
        """
    def subclass_init(self, cls: type[HasTraits]) -> None: ...
    def instance_init(self, obj: t.Any) -> None:
        """Part of the initialization which may depend on the underlying
        HasDescriptors instance.

        It is typically overloaded for specific types.

        This method is called by :meth:`HasTraits.__new__` and in the
        :meth:`BaseDescriptor.instance_init` method of descriptors holding
        other descriptors.
        """
G = t.TypeVar('G')
S = t.TypeVar('S')
T = t.TypeVar('T')

class TraitType(BaseDescriptor, t.Generic[G, S]):
    """A base class for all trait types."""
    metadata: dict[str, t.Any]
    allow_none: bool
    read_only: bool
    info_text: str
    default_value: t.Any
    help: Incomplete
    __doc__: Incomplete
    def __init__(self, default_value: t.Any = ..., allow_none: bool = False, read_only: bool | None = None, help: str | None = None, config: t.Any = None, **kwargs: t.Any) -> None:
        """Declare a traitlet.

        If *allow_none* is True, None is a valid value in addition to any
        values that are normally valid. The default is up to the subclass.
        For most trait types, the default value for ``allow_none`` is False.

        If *read_only* is True, attempts to directly modify a trait attribute raises a TraitError.

        If *help* is a string, it documents the attribute's purpose.

        Extra metadata can be associated with the traitlet using the .tag() convenience method
        or by using the traitlet instance's .metadata dictionary.
        """
    def from_string(self, s: str) -> G | None:
        """Get a value from a config string

        such as an environment variable or CLI arguments.

        Traits can override this method to define their own
        parsing of config strings.

        .. seealso:: item_from_string

        .. versionadded:: 5.0
        """
    def default(self, obj: t.Any = None) -> G | None:
        """The default generator for this trait

        Notes
        -----
        This method is registered to HasTraits classes during ``class_init``
        in the same way that dynamic defaults defined by ``@default`` are.
        """
    def get_default_value(self) -> G | None:
        """DEPRECATED: Retrieve the static default value for this trait.
        Use self.default_value instead
        """
    def init_default_value(self, obj: t.Any) -> G:
        """DEPRECATED: Set the static default value for the trait type."""
    def get(self, obj: HasTraits, cls: t.Any = None) -> G | None: ...
    @t.overload
    def __new__(cls, default_value: S | Sentinel = ..., allow_none: Literal[False] = ..., read_only: bool | None = None, help: str | None = None, config: t.Any = None, **kwargs: t.Any) -> TraitType[G, S]: ...
    @t.overload
    def __new__(cls, default_value: S | None | Sentinel = ..., allow_none: Literal[True] = ..., read_only: bool | None = None, help: str | None = None, config: t.Any = None, **kwargs: t.Any) -> TraitType[G | None, S]: ...
    @t.overload
    def __get__(self, obj: None, cls: type[t.Any]) -> Self: ...
    @t.overload
    def __get__(self, obj: t.Any, cls: type[t.Any]) -> G: ...
    def set(self, obj: HasTraits, value: S) -> None: ...
    def __set__(self, obj: HasTraits, value: S) -> None:
        """Set the value of the trait by self.name for the instance.

        Values pass through a validation stage where errors are raised when
        impropper types, or types that cannot be coerced, are encountered.
        """
    def __or__(self, other): ...
    def info(self): ...
    def error(self, obj, value, error: Incomplete | None = None, info: Incomplete | None = None) -> None:
        '''Raise a TraitError

        Parameters
        ----------
        obj : HasTraits or None
            The instance which owns the trait. If not
            object is given, then an object agnostic
            error will be raised.
        value : any
            The value that caused the error.
        error : Exception (default: None)
            An error that was raised by a child trait.
            The arguments of this exception should be
            of the form ``(value, info, *traits)``.
            Where the ``value`` and ``info`` are the
            problem value, and string describing the
            expected value. The ``traits`` are a series
            of :class:`TraitType` instances that are
            "children" of this one (the first being
            the deepest).
        info : str (default: None)
            A description of the expected value. By
            default this is inferred from this trait\'s
            ``info`` method.
        '''
    def get_metadata(self, key, default: Incomplete | None = None):
        """DEPRECATED: Get a metadata value.

        Use .metadata[key] or .metadata.get(key, default) instead.
        """
    def set_metadata(self, key, value) -> None:
        """DEPRECATED: Set a metadata key/value.

        Use .metadata[key] = value instead.
        """
    def tag(self, **metadata: t.Any) -> Self:
        """Sets metadata and returns self.

        This allows convenient metadata tagging when initializing the trait, such as:

        Examples
        --------
        >>> Int(0).tag(config=True, sync=True)
        <traitlets.traitlets.Int object at ...>

        """
    def default_value_repr(self): ...

class _CallbackWrapper:
    """An object adapting a on_trait_change callback into an observe callback.

    The comparison operator __eq__ is implemented to enable removal of wrapped
    callbacks.
    """
    cb: Incomplete
    nargs: Incomplete
    def __init__(self, cb: t.Any) -> None: ...
    def __eq__(self, other): ...
    def __call__(self, change) -> None: ...

class MetaHasDescriptors(type):
    """A metaclass for HasDescriptors.

    This metaclass makes sure that any TraitType class attributes are
    instantiated and sets their name attribute.
    """
    def __new__(mcls, name, bases, classdict, **kwds):
        """Create the HasDescriptors class."""
    def __init__(cls, name: str, bases: t.Any, classdict: t.Any, **kwds) -> None:
        """Finish initializing the HasDescriptors class."""
    def setup_class(cls, classdict) -> None:
        """Setup descriptor instance on the class

        This sets the :attr:`this_class` and :attr:`name` attributes of each
        BaseDescriptor in the class dict of the newly created ``cls`` before
        calling their :attr:`class_init` method.
        """

class MetaHasTraits(MetaHasDescriptors):
    """A metaclass for HasTraits."""
    def setup_class(cls, classdict) -> None: ...

def observe(*names: Sentinel | str, type: str = 'change') -> ObserveHandler:
    """A decorator which can be used to observe Traits on a class.

    The handler passed to the decorator will be called with one ``change``
    dict argument. The change dictionary at least holds a 'type' key and a
    'name' key, corresponding respectively to the type of notification and the
    name of the attribute that triggered the notification.

    Other keys may be passed depending on the value of 'type'. In the case
    where type is 'change', we also have the following keys:
    * ``owner`` : the HasTraits instance
    * ``old`` : the old value of the modified trait attribute
    * ``new`` : the new value of the modified trait attribute
    * ``name`` : the name of the modified trait attribute.

    Parameters
    ----------
    *names
        The str names of the Traits to observe on the object.
    type : str, kwarg-only
        The type of event to observe (e.g. 'change')
    """
def observe_compat(func: FuncT) -> FuncT:
    """Backward-compatibility shim decorator for observers

    Use with:

    @observe('name')
    @observe_compat
    def _foo_changed(self, change):
        ...

    With this, `super()._foo_changed(self, name, old, new)` in subclasses will still work.
    Allows adoption of new observer API without breaking subclasses that override and super.
    """
def validate(*names: Sentinel | str) -> ValidateHandler:
    """A decorator to register cross validator of HasTraits object's state
    when a Trait is set.

    The handler passed to the decorator must have one ``proposal`` dict argument.
    The proposal dictionary must hold the following keys:

    * ``owner`` : the HasTraits instance
    * ``value`` : the proposed value for the modified trait attribute
    * ``trait`` : the TraitType instance associated with the attribute

    Parameters
    ----------
    *names
        The str names of the Traits to validate.

    Notes
    -----
    Since the owner has access to the ``HasTraits`` instance via the 'owner' key,
    the registered cross validator could potentially make changes to attributes
    of the ``HasTraits`` instance. However, we recommend not to do so. The reason
    is that the cross-validation of attributes may run in arbitrary order when
    exiting the ``hold_trait_notifications`` context, and such changes may not
    commute.
    """
def default(name: str) -> DefaultHandler:
    """A decorator which assigns a dynamic default for a Trait on a HasTraits object.

    Parameters
    ----------
    name
        The str name of the Trait on the object whose default should be generated.

    Notes
    -----
    Unlike observers and validators which are properties of the HasTraits
    instance, default value generators are class-level properties.

    Besides, default generators are only invoked if they are registered in
    subclasses of `this_type`.

    ::

        class A(HasTraits):
            bar = Int()

            @default('bar')
            def get_bar_default(self):
                return 11

        class B(A):
            bar = Float()  # This trait ignores the default generator defined in
                           # the base class A

        class C(B):

            @default('bar')
            def some_other_default(self):  # This default generator should not be
                return 3.0                 # ignored since it is defined in a
                                           # class derived from B.a.this_class.
    """
FuncT = t.TypeVar('FuncT', bound=t.Callable[..., t.Any])

class EventHandler(BaseDescriptor):
    @t.overload
    def __call__(self, func: FuncT, *args: t.Any, **kwargs: t.Any) -> FuncT: ...
    @t.overload
    def __call__(self, *args: t.Any, **kwargs: t.Any) -> t.Any: ...
    def __get__(self, inst, cls: Incomplete | None = None): ...

class ObserveHandler(EventHandler):
    trait_names: Incomplete
    type: Incomplete
    def __init__(self, names: t.Any, type: t.Any) -> None: ...
    def instance_init(self, inst) -> None: ...

class ValidateHandler(EventHandler):
    trait_names: Incomplete
    def __init__(self, names: t.Any) -> None: ...
    def instance_init(self, inst) -> None: ...

class DefaultHandler(EventHandler):
    trait_name: Incomplete
    def __init__(self, name: str) -> None: ...
    def class_init(self, cls, name) -> None: ...

class HasDescriptors(metaclass=MetaHasDescriptors):
    """The base class for all classes that have descriptors."""
    def __new__(*args: t.Any, **kwargs: t.Any) -> t.Any: ...
    def setup_instance(*args, **kwargs) -> None:
        """
        This is called **before** self.__init__ is called.
        """

class HasTraits(HasDescriptors, metaclass=MetaHasTraits):
    def setup_instance(*args, **kwargs) -> None: ...
    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None: ...
    @property
    def cross_validation_lock(self) -> Generator[None, None, None]:
        """
        A contextmanager for running a block with our cross validation lock set
        to True.

        At the end of the block, the lock's value is restored to its value
        prior to entering the block.
        """
    def hold_trait_notifications(self) -> Generator[None, None, Incomplete]:
        """Context manager for bundling trait change notifications and cross
        validation.

        Use this when doing multiple trait assignments (init, config), to avoid
        race conditions in trait notifiers requesting other trait values.
        All trait notifications will fire after all values have been assigned.
        """
    def notify_change(self, change: Bunch) -> None:
        """Notify observers of a change event"""
    def on_trait_change(self, handler: Incomplete | None = None, name: Incomplete | None = None, remove: bool = False) -> None:
        """DEPRECATED: Setup a handler to be called when a trait changes.

        This is used to setup dynamic notifications of trait changes.

        Static handlers can be created by creating methods on a HasTraits
        subclass with the naming convention '_[traitname]_changed'.  Thus,
        to create static handler for the trait 'a', create the method
        _a_changed(self, name, old, new) (fewer arguments can be used, see
        below).

        If `remove` is True and `handler` is not specified, all change
        handlers for the specified name are uninstalled.

        Parameters
        ----------
        handler : callable, None
            A callable that is called when a trait changes.  Its
            signature can be handler(), handler(name), handler(name, new),
            handler(name, old, new), or handler(name, old, new, self).
        name : list, str, None
            If None, the handler will apply to all traits.  If a list
            of str, handler will apply to all names in the list.  If a
            str, the handler will apply just to that name.
        remove : bool
            If False (the default), then install the handler.  If True
            then unintall it.
        """
    def observe(self, handler: t.Callable[..., t.Any], names: Sentinel | str | t.Iterable[Sentinel | str] = ..., type: Sentinel | str = 'change') -> None:
        """Setup a handler to be called when a trait changes.

        This is used to setup dynamic notifications of trait changes.

        Parameters
        ----------
        handler : callable
            A callable that is called when a trait changes. Its
            signature should be ``handler(change)``, where ``change`` is a
            dictionary. The change dictionary at least holds a 'type' key.
            * ``type``: the type of notification.
            Other keys may be passed depending on the value of 'type'. In the
            case where type is 'change', we also have the following keys:
            * ``owner`` : the HasTraits instance
            * ``old`` : the old value of the modified trait attribute
            * ``new`` : the new value of the modified trait attribute
            * ``name`` : the name of the modified trait attribute.
        names : list, str, All
            If names is All, the handler will apply to all traits.  If a list
            of str, handler will apply to all names in the list.  If a
            str, the handler will apply just to that name.
        type : str, All (default: 'change')
            The type of notification to filter by. If equal to All, then all
            notifications are passed to the observe handler.
        """
    def unobserve(self, handler: t.Callable[..., t.Any], names: Sentinel | str | t.Iterable[Sentinel | str] = ..., type: Sentinel | str = 'change') -> None:
        """Remove a trait change handler.

        This is used to unregister handlers to trait change notifications.

        Parameters
        ----------
        handler : callable
            The callable called when a trait attribute changes.
        names : list, str, All (default: All)
            The names of the traits for which the specified handler should be
            uninstalled. If names is All, the specified handler is uninstalled
            from the list of notifiers corresponding to all changes.
        type : str or All (default: 'change')
            The type of notification to filter by. If All, the specified handler
            is uninstalled from the list of notifiers corresponding to all types.
        """
    def unobserve_all(self, name: str | t.Any = ...) -> None:
        """Remove trait change handlers of any type for the specified name.
        If name is not specified, removes all trait notifiers."""
    __class__: Incomplete
    def add_traits(self, **traits: t.Any) -> None:
        """Dynamically add trait attributes to the HasTraits instance."""
    def set_trait(self, name: str, value: t.Any) -> None:
        """Forcibly sets trait attribute, including read-only attributes."""
    @classmethod
    def class_trait_names(cls, **metadata: t.Any) -> list[str]:
        """Get a list of all the names of this class' traits.

        This method is just like the :meth:`trait_names` method,
        but is unbound.
        """
    @classmethod
    def class_traits(cls, **metadata: t.Any) -> dict[str, TraitType]:
        """Get a ``dict`` of all the traits of this class.  The dictionary
        is keyed on the name and the values are the TraitType objects.

        This method is just like the :meth:`traits` method, but is unbound.

        The TraitTypes returned don't know anything about the values
        that the various HasTrait's instances are holding.

        The metadata kwargs allow functions to be passed in which
        filter traits based on metadata values.  The functions should
        take a single value as an argument and return a boolean.  If
        any function returns False, then the trait is not included in
        the output.  If a metadata key doesn't exist, None will be passed
        to the function.
        """
    @classmethod
    def class_own_traits(cls, **metadata: t.Any) -> dict[str, TraitType]:
        """Get a dict of all the traitlets defined on this class, not a parent.

        Works like `class_traits`, except for excluding traits from parents.
        """
    def has_trait(self, name: str) -> bool:
        """Returns True if the object has a trait with the specified name."""
    def trait_has_value(self, name: str) -> bool:
        '''Returns True if the specified trait has a value.

        This will return false even if ``getattr`` would return a
        dynamically generated default value. These default values
        will be recognized as existing only after they have been
        generated.

        Example

        .. code-block:: python

            class MyClass(HasTraits):
                i = Int()


            mc = MyClass()
            assert not mc.trait_has_value("i")
            mc.i  # generates a default value
            assert mc.trait_has_value("i")
        '''
    def trait_values(self, **metadata: t.Any) -> dict[str, t.Any]:
        """A ``dict`` of trait names and their values.

        The metadata kwargs allow functions to be passed in which
        filter traits based on metadata values.  The functions should
        take a single value as an argument and return a boolean.  If
        any function returns False, then the trait is not included in
        the output.  If a metadata key doesn't exist, None will be passed
        to the function.

        Returns
        -------
        A ``dict`` of trait names and their values.

        Notes
        -----
        Trait values are retrieved via ``getattr``, any exceptions raised
        by traits or the operations they may trigger will result in the
        absence of a trait value in the result ``dict``.
        """
    def trait_defaults(self, *names: str, **metadata: t.Any) -> dict[str, t.Any]:
        """Return a trait's default value or a dictionary of them

        Notes
        -----
        Dynamically generated default values may
        depend on the current state of the object."""
    def trait_names(self, **metadata: t.Any) -> list[str]:
        """Get a list of all the names of this class' traits."""
    def traits(self, **metadata: t.Any) -> dict[str, TraitType]:
        """Get a ``dict`` of all the traits of this class.  The dictionary
        is keyed on the name and the values are the TraitType objects.

        The TraitTypes returned don't know anything about the values
        that the various HasTrait's instances are holding.

        The metadata kwargs allow functions to be passed in which
        filter traits based on metadata values.  The functions should
        take a single value as an argument and return a boolean.  If
        any function returns False, then the trait is not included in
        the output.  If a metadata key doesn't exist, None will be passed
        to the function.
        """
    def trait_metadata(self, traitname: str, key: str, default: t.Any = None) -> t.Any:
        """Get metadata values for trait by key."""
    @classmethod
    def class_own_trait_events(cls, name: str) -> dict[str, EventHandler]:
        """Get a dict of all event handlers defined on this class, not a parent.

        Works like ``event_handlers``, except for excluding traits from parents.
        """
    @classmethod
    def trait_events(cls, name: str | None = None) -> dict[str, EventHandler]:
        """Get a ``dict`` of all the event handlers of this class.

        Parameters
        ----------
        name : str (default: None)
            The name of a trait of this class. If name is ``None`` then all
            the event handlers of this class will be returned instead.

        Returns
        -------
        The event handlers associated with a trait name, or all event handlers.
        """

class ClassBasedTraitType(TraitType[G, S]):
    """
    A trait with error reporting and string -> type resolution for Type,
    Instance and This.
    """

class Type(ClassBasedTraitType[G, S]):
    """A trait whose value must be a subclass of a specified class."""
    @t.overload
    def __init__(self, default_value: Sentinel | None | str = ..., klass: None | str = ..., allow_none: Literal[False] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any | None = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, default_value: Sentinel | None | str = ..., klass: None | str = ..., allow_none: Literal[True] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any | None = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, default_value: S = ..., klass: type[S] = ..., allow_none: Literal[False] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any | None = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, default_value: S | None = ..., klass: type[S] = ..., allow_none: Literal[True] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any | None = ..., **kwargs: t.Any) -> None: ...
    def validate(self, obj, value):
        """Validates that the value is a valid object instance."""
    def info(self):
        """Returns a description of the trait."""
    def instance_init(self, obj) -> None: ...
    def default_value_repr(self): ...

class Instance(ClassBasedTraitType[T, T]):
    """A trait whose value must be an instance of a specified class.

    The value can also be an instance of a subclass of the specified class.

    Subclasses can declare default classes by overriding the klass attribute
    """
    klass: str | type[T] | None
    @t.overload
    def __init__(self, klass: type[T] = ..., args: tuple[t.Any, ...] | None = ..., kw: dict[str, t.Any] | None = ..., allow_none: Literal[False] = ..., read_only: bool | None = ..., help: str | None = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, klass: type[T] = ..., args: tuple[t.Any, ...] | None = ..., kw: dict[str, t.Any] | None = ..., allow_none: Literal[True] = ..., read_only: bool | None = ..., help: str | None = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, klass: str | None = ..., args: tuple[t.Any, ...] | None = ..., kw: dict[str, t.Any] | None = ..., allow_none: Literal[False] = ..., read_only: bool | None = ..., help: str | None = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, klass: str | None = ..., args: tuple[t.Any, ...] | None = ..., kw: dict[str, t.Any] | None = ..., allow_none: Literal[True] = ..., read_only: bool | None = ..., help: str | None = ..., **kwargs: t.Any) -> None: ...
    def validate(self, obj, value): ...
    def info(self): ...
    def instance_init(self, obj) -> None: ...
    def make_dynamic_default(self): ...
    def default_value_repr(self): ...
    def from_string(self, s): ...

class ForwardDeclaredMixin:
    """
    Mixin for forward-declared versions of Instance and Type.
    """
class ForwardDeclaredType(ForwardDeclaredMixin, Type[G, S]):
    """
    Forward-declared version of Type.
    """
class ForwardDeclaredInstance(ForwardDeclaredMixin, Instance[T]):
    """
    Forward-declared version of Instance.
    """

class This(ClassBasedTraitType[T | None, T | None]):
    """A trait for instances of the class containing this trait.

    Because how how and when class bodies are executed, the ``This``
    trait can only have a default value of None.  This, and because we
    always validate default values, ``allow_none`` is *always* true.
    """
    info_text: str
    def __init__(self, **kwargs: t.Any) -> None: ...
    def validate(self, obj, value): ...

class Union(TraitType[t.Any, t.Any]):
    """A trait type representing a Union type."""
    trait_types: Incomplete
    info_text: Incomplete
    def __init__(self, trait_types: t.Any, **kwargs: t.Any) -> None:
        """Construct a Union  trait.

        This trait allows values that are allowed by at least one of the
        specified trait types. A Union traitlet cannot have metadata on
        its own, besides the metadata of the listed types.

        Parameters
        ----------
        trait_types : sequence
            The list of trait types of length at least 1.
        **kwargs
            Extra kwargs passed to `TraitType`

        Notes
        -----
        Union([Float(), Bool(), Int()]) attempts to validate the provided values
        with the validation function of Float, then Bool, and finally Int.

        Parsing from string is ambiguous for container types which accept other
        collection-like literals (e.g. List accepting both `[]` and `()`
        precludes Union from ever parsing ``Union([List(), Tuple()])`` as a tuple;
        you can modify behaviour of too permissive container traits by overriding
        ``_literal_from_string_pairs`` in subclasses.
        Similarly, parsing unions of numeric types is only unambiguous if
        types are provided in order of increasing permissiveness, e.g.
        ``Union([Int(), Float()])`` (since floats accept integer-looking values).
        """
    def default(self, obj: Incomplete | None = None): ...
    def class_init(self, cls, name) -> None: ...
    def subclass_init(self, cls) -> None: ...
    def validate(self, obj, value): ...
    def __or__(self, other): ...
    def from_string(self, s): ...

class Any(TraitType[t.Any | None, t.Any | None]):
    """A trait which allows any value."""
    @t.overload
    def __init__(self, default_value: t.Any = ..., *, allow_none: Literal[False], read_only: bool | None = ..., help: str | None = ..., config: t.Any | None = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, default_value: t.Any = ..., *, allow_none: Literal[True], read_only: bool | None = ..., help: str | None = ..., config: t.Any | None = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, default_value: t.Any = ..., *, allow_none: Literal[True, False] = ..., help: str | None = ..., read_only: bool | None = False, config: t.Any = None, **kwargs: t.Any) -> None: ...
    @t.overload
    def __get__(self, obj: None, cls: type[t.Any]) -> Any: ...
    @t.overload
    def __get__(self, obj: t.Any, cls: type[t.Any]) -> t.Any: ...
    default_value: t.Any | None
    allow_none: bool
    info_text: str
    def subclass_init(self, cls) -> None: ...

class Int(TraitType[G, S]):
    """An int trait."""
    default_value: int
    info_text: str
    @t.overload
    def __init__(self, default_value: int | Sentinel = ..., allow_none: Literal[False] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any | None = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, default_value: int | Sentinel | None = ..., allow_none: Literal[True] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any | None = ..., **kwargs: t.Any) -> None: ...
    def validate(self, obj, value): ...
    def from_string(self, s): ...
    def subclass_init(self, cls) -> None: ...

class CInt(Int[G, S]):
    """A casting version of the int trait."""
    @t.overload
    def __init__(self, default_value: t.Any | Sentinel = ..., allow_none: Literal[False] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any | None = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, default_value: t.Any | Sentinel | None = ..., allow_none: Literal[True] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any | None = ..., **kwargs: t.Any) -> None: ...
    def validate(self, obj, value): ...

Long: Incomplete
CLong: Incomplete
Integer = Int

class Float(TraitType[G, S]):
    """A float trait."""
    default_value: float
    info_text: str
    @t.overload
    def __init__(self, default_value: float | Sentinel = ..., allow_none: Literal[False] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any | None = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, default_value: float | Sentinel | None = ..., allow_none: Literal[True] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any | None = ..., **kwargs: t.Any) -> None: ...
    def validate(self, obj, value): ...
    def from_string(self, s): ...
    def subclass_init(self, cls) -> None: ...

class CFloat(Float[G, S]):
    """A casting version of the float trait."""
    @t.overload
    def __init__(self, default_value: t.Any = ..., allow_none: Literal[False] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any | None = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, default_value: t.Any = ..., allow_none: Literal[True] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any | None = ..., **kwargs: t.Any) -> None: ...
    def validate(self, obj, value): ...

class Complex(TraitType[complex, complex | float | int]):
    """A trait for complex numbers."""
    default_value: complex
    info_text: str
    def validate(self, obj, value): ...
    def from_string(self, s): ...
    def subclass_init(self, cls) -> None: ...

class CComplex(Complex, TraitType[complex, t.Any]):
    """A casting version of the complex number trait."""
    def validate(self, obj, value): ...

class Bytes(TraitType[bytes, bytes]):
    """A trait for byte strings."""
    default_value: bytes
    info_text: str
    def validate(self, obj, value): ...
    def from_string(self, s): ...
    def subclass_init(self, cls) -> None: ...

class CBytes(Bytes, TraitType[bytes, t.Any]):
    """A casting version of the byte string trait."""
    def validate(self, obj, value): ...

class Unicode(TraitType[G, S]):
    """A trait for unicode strings."""
    default_value: str
    info_text: str
    @t.overload
    def __init__(self, default_value: str | Sentinel = ..., allow_none: Literal[False] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, default_value: str | Sentinel | None = ..., allow_none: Literal[True] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any = ..., **kwargs: t.Any) -> None: ...
    def validate(self, obj, value): ...
    def from_string(self, s): ...
    def subclass_init(self, cls) -> None: ...

class CUnicode(Unicode[G, S], TraitType[str, t.Any]):
    """A casting version of the unicode trait."""
    @t.overload
    def __init__(self, default_value: str | Sentinel = ..., allow_none: Literal[False] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, default_value: str | Sentinel | None = ..., allow_none: Literal[True] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any = ..., **kwargs: t.Any) -> None: ...
    def validate(self, obj, value): ...

class ObjectName(TraitType[str, str]):
    """A string holding a valid object name in this version of Python.

    This does not check that the name exists in any scope."""
    info_text: str
    coerce_str: Incomplete
    def validate(self, obj, value): ...
    def from_string(self, s): ...

class DottedObjectName(ObjectName):
    """A string holding a valid dotted object name in Python, such as A.b3._c"""
    def validate(self, obj, value): ...

class Bool(TraitType[G, S]):
    """A boolean (True, False) trait."""
    default_value: bool
    info_text: str
    @t.overload
    def __init__(self, default_value: bool | Sentinel = ..., allow_none: Literal[False] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, default_value: bool | Sentinel | None = ..., allow_none: Literal[True] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any = ..., **kwargs: t.Any) -> None: ...
    def validate(self, obj, value): ...
    def from_string(self, s): ...
    def subclass_init(self, cls) -> None: ...
    def argcompleter(self, **kwargs):
        """Completion hints for argcomplete"""

class CBool(Bool[G, S]):
    """A casting version of the boolean trait."""
    @t.overload
    def __init__(self, default_value: bool | Sentinel = ..., allow_none: Literal[False] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, default_value: bool | Sentinel | None = ..., allow_none: Literal[True] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any = ..., **kwargs: t.Any) -> None: ...
    def validate(self, obj, value): ...

class Enum(TraitType[G, S]):
    """An enum whose value must be in a given sequence."""
    values: Incomplete
    def __init__(self, values: t.Any, default_value: t.Any = ..., **kwargs: t.Any) -> None: ...
    def validate(self, obj, value): ...
    def info(self): ...
    def info_rst(self): ...
    def from_string(self, s): ...
    def subclass_init(self, cls) -> None: ...
    def argcompleter(self, **kwargs):
        """Completion hints for argcomplete"""

class CaselessStrEnum(Enum[G, S]):
    """An enum of strings where the case should be ignored."""
    def __init__(self, values: t.Any, default_value: t.Any = ..., **kwargs: t.Any) -> None: ...
    def validate(self, obj, value): ...
    def info(self): ...
    def info_rst(self): ...

class FuzzyEnum(Enum[G, S]):
    """An case-ignoring enum matching choices by unique prefixes/substrings."""
    case_sensitive: bool
    substring_matching: bool
    def __init__(self, values: t.Any, default_value: t.Any = ..., case_sensitive: bool = False, substring_matching: bool = False, **kwargs: t.Any) -> None: ...
    def validate(self, obj, value): ...
    def info(self): ...
    def info_rst(self): ...

class Container(Instance[T]):
    """An instance of a container (list, set, etc.)

    To be subclassed by overriding klass.
    """
    klass: type[T] | None
    @t.overload
    def __init__(self, *, allow_none: Literal[False], read_only: bool | None = ..., help: str | None = ..., config: t.Any | None = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, *, allow_none: Literal[True], read_only: bool | None = ..., help: str | None = ..., config: t.Any | None = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, *, trait: t.Any = ..., default_value: t.Any = ..., help: str = ..., read_only: bool = ..., config: t.Any = ..., **kwargs: t.Any) -> None: ...
    def validate(self, obj, value): ...
    def validate_elements(self, obj, value): ...
    def class_init(self, cls, name) -> None: ...
    def subclass_init(self, cls) -> None: ...
    def from_string(self, s):
        """Load value from a single string"""
    def from_string_list(self, s_list):
        """Return the value from a list of config strings

        This is where we parse CLI configuration
        """
    def item_from_string(self, s, index: Incomplete | None = None):
        """Cast a single item from a string

        Evaluated when parsing CLI configuration from a string
        """

class List(Container[t.List[t.Any]]):
    """An instance of a Python list."""
    klass = list
    def __init__(self, trait: t.Any = None, default_value: t.Any = ..., minlen: int = 0, maxlen: int = ..., **kwargs: t.Any) -> None:
        """Create a List trait type from a list, set, or tuple.

        The default value is created by doing ``list(default_value)``,
        which creates a copy of the ``default_value``.

        ``trait`` can be specified, which restricts the type of elements
        in the container to that TraitType.

        If only one arg is given and it is not a Trait, it is taken as
        ``default_value``:

        ``c = List([1, 2, 3])``

        Parameters
        ----------
        trait : TraitType [ optional ]
            the type for restricting the contents of the Container.
            If unspecified, types are not checked.
        default_value : SequenceType [ optional ]
            The default value for the Trait.  Must be list/tuple/set, and
            will be cast to the container type.
        minlen : Int [ default 0 ]
            The minimum length of the input list
        maxlen : Int [ default sys.maxsize ]
            The maximum length of the input list
        """
    def length_error(self, obj, value) -> None: ...
    def validate_elements(self, obj, value): ...
    def set(self, obj, value): ...

class Set(Container[t.Set[t.Any]]):
    """An instance of a Python set."""
    klass = set
    def __init__(self, trait: t.Any = None, default_value: t.Any = ..., minlen: int = 0, maxlen: int = ..., **kwargs: t.Any) -> None:
        """Create a Set trait type from a list, set, or tuple.

        The default value is created by doing ``set(default_value)``,
        which creates a copy of the ``default_value``.

        ``trait`` can be specified, which restricts the type of elements
        in the container to that TraitType.

        If only one arg is given and it is not a Trait, it is taken as
        ``default_value``:

        ``c = Set({1, 2, 3})``

        Parameters
        ----------
        trait : TraitType [ optional ]
            the type for restricting the contents of the Container.
            If unspecified, types are not checked.
        default_value : SequenceType [ optional ]
            The default value for the Trait.  Must be list/tuple/set, and
            will be cast to the container type.
        minlen : Int [ default 0 ]
            The minimum length of the input list
        maxlen : Int [ default sys.maxsize ]
            The maximum length of the input list
        """
    def length_error(self, obj, value) -> None: ...
    def validate_elements(self, obj, value): ...
    def set(self, obj, value): ...
    def default_value_repr(self): ...

class Tuple(Container[t.Tuple[t.Any, ...]]):
    """An instance of a Python tuple."""
    klass = tuple
    def __init__(self, *traits: t.Any, **kwargs: t.Any) -> None:
        """Create a tuple from a list, set, or tuple.

        Create a fixed-type tuple with Traits:

        ``t = Tuple(Int(), Str(), CStr())``

        would be length 3, with Int,Str,CStr for each element.

        If only one arg is given and it is not a Trait, it is taken as
        default_value:

        ``t = Tuple((1, 2, 3))``

        Otherwise, ``default_value`` *must* be specified by keyword.

        Parameters
        ----------
        *traits : TraitTypes [ optional ]
            the types for restricting the contents of the Tuple.  If unspecified,
            types are not checked. If specified, then each positional argument
            corresponds to an element of the tuple.  Tuples defined with traits
            are of fixed length.
        default_value : SequenceType [ optional ]
            The default value for the Tuple.  Must be list/tuple/set, and
            will be cast to a tuple. If ``traits`` are specified,
            ``default_value`` must conform to the shape and type they specify.
        **kwargs
            Other kwargs passed to `Container`
        """
    def item_from_string(self, s, index):
        """Cast a single item from a string

        Evaluated when parsing CLI configuration from a string
        """
    def validate_elements(self, obj, value): ...
    def class_init(self, cls, name) -> None: ...
    def subclass_init(self, cls) -> None: ...

class Dict(Instance[t.Dict[t.Any, t.Any]]):
    """An instance of a Python dict.

    One or more traits can be passed to the constructor
    to validate the keys and/or values of the dict.
    If you need more detailed validation,
    you may use a custom validator method.

    .. versionchanged:: 5.0
        Added key_trait for validating dict keys.

    .. versionchanged:: 5.0
        Deprecated ambiguous ``trait``, ``traits`` args in favor of ``value_trait``, ``per_key_traits``.
    """
    def __init__(self, value_trait: t.Any = None, per_key_traits: t.Any = None, key_trait: t.Any = None, default_value: t.Any = ..., **kwargs: t.Any) -> None:
        '''Create a dict trait type from a Python dict.

        The default value is created by doing ``dict(default_value)``,
        which creates a copy of the ``default_value``.

        Parameters
        ----------
        value_trait : TraitType [ optional ]
            The specified trait type to check and use to restrict the values of
            the dict. If unspecified, values are not checked.
        per_key_traits : Dictionary of {keys:trait types} [ optional, keyword-only ]
            A Python dictionary containing the types that are valid for
            restricting the values of the dict on a per-key basis.
            Each value in this dict should be a Trait for validating
        key_trait : TraitType [ optional, keyword-only ]
            The type for restricting the keys of the dict. If
            unspecified, the types of the keys are not checked.
        default_value : SequenceType [ optional, keyword-only ]
            The default value for the Dict.  Must be dict, tuple, or None, and
            will be cast to a dict if not None. If any key or value traits are specified,
            the `default_value` must conform to the constraints.

        Examples
        --------
        a dict whose values must be text
        >>> d = Dict(Unicode())

        d2[\'n\'] must be an integer
        d2[\'s\'] must be text
        >>> d2 = Dict(per_key_traits={"n": Integer(), "s": Unicode()})

        d3\'s keys must be text
        d3\'s values must be integers
        >>> d3 = Dict(value_trait=Integer(), key_trait=Unicode())

        '''
    def element_error(self, obj, element, validator, side: str = 'Values') -> None: ...
    def validate(self, obj, value): ...
    def validate_elements(self, obj, value): ...
    def class_init(self, cls, name) -> None: ...
    def subclass_init(self, cls) -> None: ...
    def from_string(self, s):
        """Load value from a single string"""
    def from_string_list(self, s_list):
        '''Return a dict from a list of config strings.

        This is where we parse CLI configuration.

        Each item should have the form ``"key=value"``.

        item parsing is done in :meth:`.item_from_string`.
        '''
    def item_from_string(self, s):
        """Cast a single-key dict from a string.

        Evaluated when parsing CLI configuration from a string.

        Dicts expect strings of the form key=value.

        Returns a one-key dictionary,
        which will be merged in :meth:`.from_string_list`.
        """

class TCPAddress(TraitType[G, S]):
    """A trait for an (ip, port) tuple.

    This allows for both IPv4 IP addresses as well as hostnames.
    """
    default_value: Incomplete
    info_text: str
    @t.overload
    def __init__(self, default_value: bool | Sentinel = ..., allow_none: Literal[False] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any = ..., **kwargs: t.Any) -> None: ...
    @t.overload
    def __init__(self, default_value: bool | None | Sentinel = ..., allow_none: Literal[True] = ..., read_only: bool | None = ..., help: str | None = ..., config: t.Any = ..., **kwargs: t.Any) -> None: ...
    def validate(self, obj, value): ...
    def from_string(self, s): ...

class CRegExp(TraitType['re.Pattern[t.Any]', 're.Pattern[t.Any]' | str]):
    """A casting compiled regular expression trait.

    Accepts both strings and compiled regular expressions. The resulting
    attribute will be a compiled regular expression."""
    info_text: str
    def validate(self, obj, value): ...

class UseEnum(TraitType[t.Any, t.Any]):
    '''Use a Enum class as model for the data type description.
    Note that if no default-value is provided, the first enum-value is used
    as default-value.

    .. sourcecode:: python

        # -- SINCE: Python 3.4 (or install backport: pip install enum34)
        import enum
        from traitlets import HasTraits, UseEnum


        class Color(enum.Enum):
            red = 1  # -- IMPLICIT: default_value
            blue = 2
            green = 3


        class MyEntity(HasTraits):
            color = UseEnum(Color, default_value=Color.blue)


        entity = MyEntity(color=Color.red)
        entity.color = Color.green  # USE: Enum-value (preferred)
        entity.color = "green"  # USE: name (as string)
        entity.color = "Color.green"  # USE: scoped-name (as string)
        entity.color = 3  # USE: number (as int)
        assert entity.color is Color.green
    '''
    default_value: enum.Enum | None
    info_text: str
    enum_class: Incomplete
    name_prefix: Incomplete
    def __init__(self, enum_class: type[t.Any], default_value: t.Any = None, **kwargs: t.Any) -> None: ...
    def select_by_number(self, value, default=...):
        """Selects enum-value by using its number-constant."""
    def select_by_name(self, value, default=...):
        """Selects enum-value by using its name or scoped-name."""
    def validate(self, obj, value): ...
    def info(self): ...
    def info_rst(self): ...

class Callable(TraitType[t.Callable[..., t.Any], t.Callable[..., t.Any]]):
    """A trait which is callable.

    Notes
    -----
    Classes are callable, as are instances
    with a __call__() method."""
    info_text: str
    def validate(self, obj, value): ...
