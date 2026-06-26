import re
import types
from . import compat as compat
from .. import exc as exc
from ._has_cy import HAS_CYEXTENSION as HAS_CYEXTENSION
from .typing import Literal as Literal
from _typeshed import Incomplete
from collections.abc import Generator
from enum import IntFlag
from typing import Any, Callable, Dict, Generic, Iterator, List, Mapping, NoReturn, Sequence, Set, Tuple, Type, overload

def get_annotations(obj: Any) -> Mapping[str, Any]: ...
def md5_hex(x: Any) -> str: ...

class safe_reraise:
    '''Reraise an exception after invoking some
    handler code.

    Stores the existing exception info before
    invoking so that it is maintained across a potential
    coroutine context switch.

    e.g.::

        try:
            sess.commit()
        except:
            with safe_reraise():
                sess.rollback()

    TODO: we should at some point evaluate current behaviors in this regard
    based on current greenlet, gevent/eventlet implementations in Python 3, and
    also see the degree to which our own asyncio (based on greenlet also) is
    impacted by this. .rollback() will cause IO / context switch to occur in
    all these scenarios; what happens to the exception context from an
    "except:" block if we don\'t explicitly store it? Original issue was #2703.

    '''
    def __enter__(self) -> None: ...
    def __exit__(self, type_: Type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> NoReturn: ...

def walk_subclasses(cls) -> Iterator[Type[_T]]: ...
def string_or_unprintable(element: Any) -> str: ...
def clsname_as_plain_name(cls) -> str: ...
def method_is_overridden(instance_or_cls: Type[Any] | object, against_method: Callable[..., Any]) -> bool:
    """Return True if the two class methods don't match."""
def decode_slice(slc: slice) -> Tuple[Any, ...]:
    """decode a slice object as sent to __getitem__.

    takes into account the 2.5 __index__() method, basically.

    """
def map_bits(fn: Callable[[int], Any], n: int) -> Iterator[Any]:
    """Call the given function given each nonzero bit from n."""
def decorator(target: Callable[..., Any]) -> Callable[[_Fn], _Fn]:
    """A signature-matching decorator factory."""

class PluginLoader:
    group: Incomplete
    impls: Incomplete
    auto_fn: Incomplete
    def __init__(self, group: str, auto_fn: Callable[..., Any] | None = None) -> None: ...
    def clear(self) -> None: ...
    def load(self, name: str) -> Any: ...
    def register(self, name: str, modulepath: str, objname: str) -> None: ...

@overload
def get_cls_kwargs(cls, *, _set: Set[str] | None = None, raiseerr: Literal[True] = ...) -> Set[str]: ...
@overload
def get_cls_kwargs(cls, *, _set: Set[str] | None = None, raiseerr: bool = False) -> Set[str] | None: ...
def get_func_kwargs(func: Callable[..., Any]) -> List[str]:
    """Return the set of legal kwargs for the given `func`.

    Uses getargspec so is safe to call for methods, functions,
    etc.

    """
def get_callable_argspec(fn: Callable[..., Any], no_self: bool = False, _is_init: bool = False) -> compat.FullArgSpec:
    """Return the argument signature for any callable.

    All pure-Python callables are accepted, including
    functions, methods, classes, objects with __call__;
    builtins and other edge cases like functools.partial() objects
    raise a TypeError.

    """
def format_argspec_plus(fn: Callable[..., Any] | compat.FullArgSpec, grouped: bool = True) -> Dict[str, str | None]:
    """Returns a dictionary of formatted, introspected function arguments.

    A enhanced variant of inspect.formatargspec to support code generation.

    fn
       An inspectable callable or tuple of inspect getargspec() results.
    grouped
      Defaults to True; include (parens, around, argument) lists

    Returns:

    args
      Full inspect.formatargspec for fn
    self_arg
      The name of the first positional argument, varargs[0], or None
      if the function defines no positional arguments.
    apply_pos
      args, re-written in calling rather than receiving syntax.  Arguments are
      passed positionally.
    apply_kw
      Like apply_pos, except keyword-ish args are passed as keywords.
    apply_pos_proxied
      Like apply_pos but omits the self/cls argument

    Example::

      >>> format_argspec_plus(lambda self, a, b, c=3, **d: 123)
      {'grouped_args': '(self, a, b, c=3, **d)',
       'self_arg': 'self',
       'apply_kw': '(self, a, b, c=c, **d)',
       'apply_pos': '(self, a, b, c, **d)'}

    """
def format_argspec_init(method, grouped: bool = True):
    """format_argspec_plus with considerations for typical __init__ methods

    Wraps format_argspec_plus with error handling strategies for typical
    __init__ cases::

      object.__init__ -> (self)
      other unreflectable (usually C) -> (self, *args, **kwargs)

    """
def create_proxy_methods(target_cls: Type[Any], target_cls_sphinx_name: str, proxy_cls_sphinx_name: str, classmethods: Sequence[str] = (), methods: Sequence[str] = (), attributes: Sequence[str] = (), use_intermediate_variable: Sequence[str] = ()) -> Callable[[_T], _T]:
    '''A class decorator indicating attributes should refer to a proxy
    class.

    This decorator is now a "marker" that does nothing at runtime.  Instead,
    it is consumed by the tools/generate_proxy_methods.py script to
    statically generate proxy methods and attributes that are fully
    recognized by typing tools such as mypy.

    '''
def getargspec_init(method):
    """inspect.getargspec with considerations for typical __init__ methods

    Wraps inspect.getargspec with error handling for typical __init__ cases::

      object.__init__ -> (self)
      other unreflectable (usually C) -> (self, *args, **kwargs)

    """
def unbound_method_to_callable(func_or_cls):
    """Adjust the incoming callable such that a 'self' argument is not
    required.

    """
def generic_repr(obj: Any, additional_kw: Sequence[Tuple[str, Any]] = (), to_inspect: object | List[object] | None = None, omit_kwarg: Sequence[str] = ()) -> str:
    """Produce a __repr__() based on direct association of the __init__()
    specification vs. same-named attributes present.

    """

class portable_instancemethod:
    """Turn an instancemethod into a (parent, name) pair
    to produce a serializable callable.

    """
    target: Incomplete
    name: Incomplete
    kwargs: Incomplete
    def __init__(self, meth, kwargs=()) -> None: ...
    def __call__(self, *arg, **kw): ...

def class_hierarchy(cls):
    """Return an unordered sequence of all classes related to cls.

    Traverses diamond hierarchies.

    Fibs slightly: subclasses of builtin types are not returned.  Thus
    class_hierarchy(class A(object)) returns (A, object), not A plus every
    class systemwide that derives from object.

    """
def iterate_attributes(cls) -> Generator[Incomplete, None, None]:
    """iterate all the keys and attributes associated
    with a class, without using getattr().

    Does not use getattr() so that class-sensitive
    descriptors (i.e. property.__get__()) are not called.

    """
def monkeypatch_proxied_specials(into_cls, from_cls, skip: Incomplete | None = None, only: Incomplete | None = None, name: str = 'self.proxy', from_instance: Incomplete | None = None) -> None:
    """Automates delegation of __specials__ for a proxying type."""
def methods_equivalent(meth1, meth2):
    """Return True if the two methods are the same implementation."""
def as_interface(obj, cls: Incomplete | None = None, methods: Incomplete | None = None, required: Incomplete | None = None):
    """Ensure basic interface compliance for an instance or dict of callables.

    Checks that ``obj`` implements public methods of ``cls`` or has members
    listed in ``methods``. If ``required`` is not supplied, implementing at
    least one interface method is sufficient. Methods present on ``obj`` that
    are not in the interface are ignored.

    If ``obj`` is a dict and ``dict`` does not meet the interface
    requirements, the keys of the dictionary are inspected. Keys present in
    ``obj`` that are not in the interface will raise TypeErrors.

    Raises TypeError if ``obj`` does not meet the interface criteria.

    In all passing cases, an object with callable members is returned.  In the
    simple case, ``obj`` is returned as-is; if dict processing kicks in then
    an anonymous class is returned.

    obj
      A type, instance, or dictionary of callables.
    cls
      Optional, a type.  All public methods of cls are considered the
      interface.  An ``obj`` instance of cls will always pass, ignoring
      ``required``..
    methods
      Optional, a sequence of method names to consider as the interface.
    required
      Optional, a sequence of mandatory implementations. If omitted, an
      ``obj`` that provides at least one interface method is considered
      sufficient.  As a convenience, required may be a type, in which case
      all public methods of the type are required.

    """

class generic_fn_descriptor(Generic[_T_co]):
    '''Descriptor which proxies a function when the attribute is not
    present in dict

    This superclass is organized in a particular way with "memoized" and
    "non-memoized" implementation classes that are hidden from type checkers,
    as Mypy seems to not be able to handle seeing multiple kinds of descriptor
    classes used for the same attribute.

    '''
    fget: Callable[..., _T_co]
    __doc__: str | None
    def __init__(self, fget: Callable[..., _T_co], doc: str | None = None) -> None: ...
    @overload
    def __get__(self, obj: None, cls: Any) -> _GFD: ...
    @overload
    def __get__(self, obj: object, cls: Any) -> _T_co: ...
    def __set__(self, instance: Any, value: Any) -> None: ...
    def __delete__(self, instance: Any) -> None: ...
    @classmethod
    def reset(cls, obj: Any, name: str) -> None: ...

class _non_memoized_property(generic_fn_descriptor[_T_co]):
    """a plain descriptor that proxies a function.

    primary rationale is to provide a plain attribute that's
    compatible with memoized_property which is also recognized as equivalent
    by mypy.

    """

class _memoized_property(generic_fn_descriptor[_T_co]):
    """A read-only @property that is only evaluated once."""
    @classmethod
    def reset(cls, obj, name) -> None: ...
memoized_property = generic_fn_descriptor
non_memoized_property = generic_fn_descriptor
ro_memoized_property = property
ro_non_memoized_property = property

def memoized_instancemethod(fn: _F) -> _F:
    """Decorate a method memoize its return value.

    Best applied to no-arg methods: memoization is not sensitive to
    argument values, and will always return the same value even when
    called with different arguments.

    """

class HasMemoized:
    """A mixin class that maintains the names of memoized elements in a
    collection for easy cache clearing, generative, etc.

    """
    class memoized_attribute(memoized_property[_T]):
        """A read-only @property that is only evaluated once.

        :meta private:

        """
        fget: Callable[..., _T]
        __doc__: str | None
        def __init__(self, fget: Callable[..., _T], doc: str | None = None) -> None: ...
        @overload
        def __get__(self, obj: None, cls: Any) -> _MA: ...
        @overload
        def __get__(self, obj: Any, cls: Any) -> _T: ...
    @classmethod
    def memoized_instancemethod(cls, fn: _F) -> _F:
        """Decorate a method memoize its return value.

        :meta private:

        """
HasMemoized_ro_memoized_attribute = property

class MemoizedSlots:
    """Apply memoized items to an object using a __getattr__ scheme.

    This allows the functionality of memoized_property and
    memoized_instancemethod to be available to a class using __slots__.

    """
    def __getattr__(self, key: str) -> Any: ...

def asbool(obj: Any) -> bool: ...
def bool_or_str(*text: str) -> Callable[[str], str | bool]:
    '''Return a callable that will evaluate a string as
    boolean, or one of a set of "alternate" string values.

    '''
def asint(value: Any) -> int | None:
    """Coerce to integer."""
def coerce_kw_type(kw: Dict[str, Any], key: str, type_: Type[Any], flexi_bool: bool = True, dest: Dict[str, Any] | None = None) -> None:
    """If 'key' is present in dict 'kw', coerce its value to type 'type\\_' if
    necessary.  If 'flexi_bool' is True, the string '0' is considered false
    when coercing to boolean.
    """
def constructor_key(obj: Any, cls: Type[Any]) -> Tuple[Any, ...]:
    """Produce a tuple structure that is cacheable using the __dict__ of
    obj to retrieve values

    """
def constructor_copy(obj: _T, cls: Type[_T], *args: Any, **kw: Any) -> _T:
    """Instantiate cls using the __dict__ of obj as constructor arguments.

    Uses inspect to match the named arguments of ``cls``.

    """
def counter() -> Callable[[], int]:
    """Return a threadsafe counter function."""
def duck_type_collection(specimen: Any, default: Type[Any] | None = None) -> Type[Any] | None:
    """Given an instance or class, guess if it is or is acting as one of
    the basic collection types: list, set and dict.  If the __emulates__
    property is present, return that preferentially.
    """
def assert_arg_type(arg: Any, argtype: Tuple[Type[Any], ...] | Type[Any], name: str) -> Any: ...
def dictlike_iteritems(dictlike):
    """Return a (key, value) iterator for almost any dict-like object."""

class classproperty(property):
    """A decorator that behaves like @property except that operates
    on classes rather than instances.

    The decorator is currently special when using the declarative
    module, but note that the
    :class:`~.sqlalchemy.ext.declarative.declared_attr`
    decorator should be used for this purpose with declarative.

    """
    fget: Callable[[Any], Any]
    __doc__: Incomplete
    def __init__(self, fget: Callable[[Any], Any], *arg: Any, **kw: Any) -> None: ...
    def __get__(self, obj: Any, cls: type | None = None) -> Any: ...

class hybridproperty(Generic[_T]):
    func: Incomplete
    clslevel: Incomplete
    def __init__(self, func: Callable[..., _T]) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _T: ...
    def classlevel(self, func: Callable[..., Any]) -> hybridproperty[_T]: ...

class rw_hybridproperty(Generic[_T]):
    func: Incomplete
    clslevel: Incomplete
    setfn: Incomplete
    def __init__(self, func: Callable[..., _T]) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> _T: ...
    def __set__(self, instance: Any, value: Any) -> None: ...
    def setter(self, func: Callable[..., Any]) -> rw_hybridproperty[_T]: ...
    def classlevel(self, func: Callable[..., Any]) -> rw_hybridproperty[_T]: ...

class hybridmethod(Generic[_T]):
    """Decorate a function as cls- or instance- level."""
    func: Incomplete
    clslevel: Incomplete
    def __init__(self, func: Callable[..., _T]) -> None: ...
    def __get__(self, instance: Any, owner: Any) -> Callable[..., _T]: ...
    def classlevel(self, func: Callable[..., Any]) -> hybridmethod[_T]: ...

class symbol(int):
    """A constant symbol.

    >>> symbol('foo') is symbol('foo')
    True
    >>> symbol('foo')
    <symbol 'foo>

    A slight refinement of the MAGICCOOKIE=object() pattern.  The primary
    advantage of symbol() is its repr().  They are also singletons.

    Repeated calls of symbol('name') will all return the same instance.

    """
    name: str
    symbols: Dict[str, symbol]
    def __new__(cls, name: str, doc: str | None = None, canonical: int | None = None) -> symbol: ...
    def __reduce__(self): ...

class _IntFlagMeta(type):
    def __init__(cls, classname: str, bases: Tuple[Type[Any], ...], dict_: Dict[str, Any], **kw: Any) -> None: ...
    def __iter__(self) -> Iterator[symbol]: ...

class _FastIntFlag(metaclass=_IntFlagMeta):
    """An 'IntFlag' copycat that isn't slow when performing bitwise
    operations.

    the ``FastIntFlag`` class will return ``enum.IntFlag`` under TYPE_CHECKING
    and ``_FastIntFlag`` otherwise.

    """
FastIntFlag = IntFlag

def parse_user_argument_for_enum(arg: Any, choices: Dict[_E, List[Any]], name: str, resolve_symbol_names: bool = False) -> _E | None:
    """Given a user parameter, parse the parameter into a chosen value
    from a list of choice objects, typically Enum values.

    The user argument can be a string name that matches the name of a
    symbol, or the symbol object itself, or any number of alternate choices
    such as True/False/ None etc.

    :param arg: the user argument.
    :param choices: dictionary of enum values to lists of possible
        entries for each.
    :param name: name of the argument.   Used in an :class:`.ArgumentError`
        that is raised if the parameter doesn't match any available argument.

    """
def set_creation_order(instance: Any) -> None:
    """Assign a '_creation_order' sequence to the given instance.

    This allows multiple instances to be sorted in order of creation
    (typically within a single thread; the counter is not particularly
    threadsafe).

    """
def warn_exception(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """executes the given function, catches all exceptions and converts to
    a warning.

    """
def ellipses_string(value, len_: int = 25): ...

class _hash_limit_string(str):
    '''A string subclass that can only be hashed on a maximum amount
    of unique values.

    This is used for warnings so that we can send out parameterized warnings
    without the __warningregistry__ of the module,  or the non-overridable
    "once" registry within warnings.py, overloading memory,


    '''
    def __new__(cls, value: str, num: int, args: Sequence[Any]) -> _hash_limit_string: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...

def warn(msg: str, code: str | None = None) -> None:
    """Issue a warning.

    If msg is a string, :class:`.exc.SAWarning` is used as
    the category.

    """
def warn_limited(msg: str, args: Sequence[Any]) -> None:
    """Issue a warning with a parameterized string, limiting the number
    of registrations.

    """
def tag_method_for_warnings(message: str, category: Type[Warning]) -> Callable[[_F], _F]: ...
def only_once(fn: Callable[..., _T], retry_on_exception: bool) -> Callable[..., _T | None]:
    """Decorate the given function to be a no-op after it is called exactly
    once."""
def chop_traceback(tb: List[str], exclude_prefix: re.Pattern[str] = ..., exclude_suffix: re.Pattern[str] = ...) -> List[str]:
    """Chop extraneous lines off beginning and end of a traceback.

    :param tb:
      a list of traceback lines as returned by ``traceback.format_stack()``

    :param exclude_prefix:
      a regular expression object matching lines to skip at beginning of
      ``tb``

    :param exclude_suffix:
      a regular expression object matching lines to skip at end of ``tb``
    """

NoneType: Incomplete

def attrsetter(attrname): ...

class TypingOnly:
    """A mixin class that marks a class as 'typing only', meaning it has
    absolutely no methods, attributes, or runtime functionality whatsoever.

    """
    def __init_subclass__(cls) -> None: ...

class EnsureKWArg:
    """Apply translation of functions to accept \\**kw arguments if they
    don't already.

    Used to ensure cross-compatibility with third party legacy code, for things
    like compiler visit methods that need to accept ``**kw`` arguments,
    but may have been copied from old code that didn't accept them.

    """
    ensure_kwarg: str
    def __init_subclass__(cls) -> None: ...

def wrap_callable(wrapper, fn):
    """Augment functools.update_wrapper() to work with objects with
    a ``__call__()`` method.

    :param fn:
      object with __call__ method

    """
def quoted_token_parser(value):
    '''Parse a dotted identifier with accommodation for quoted names.

    Includes support for SQL-style double quotes as a literal character.

    E.g.::

        >>> quoted_token_parser("name")
        ["name"]
        >>> quoted_token_parser("schema.name")
        ["schema", "name"]
        >>> quoted_token_parser(\'"Schema"."Name"\')
        [\'Schema\', \'Name\']
        >>> quoted_token_parser(\'"Schema"."Name""Foo"\')
        [\'Schema\', \'Name""Foo\']

    '''
def add_parameter_text(params: Any, text: str) -> Callable[[_F], _F]: ...
def inject_docstring_text(given_doctext: str | None, injecttext: str, pos: int) -> str: ...
def inject_param_text(doctext: str, inject_params: Dict[str, str]) -> str: ...
def repr_tuple_names(names: List[str]) -> str | None:
    """Trims a list of strings from the middle and return a string of up to
    four elements. Strings greater than 11 characters will be truncated"""
def has_compiled_ext(raise_: bool = False): ...
