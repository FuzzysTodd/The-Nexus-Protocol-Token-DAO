import abc
import typing
from _typeshed import Incomplete
from typing_extensions import TypedDict as TypedDict

__all__ = ['Any', 'ClassVar', 'Concatenate', 'Final', 'LiteralString', 'ParamSpec', 'ParamSpecArgs', 'ParamSpecKwargs', 'Self', 'Type', 'TypeVar', 'TypeVarTuple', 'Unpack', 'Awaitable', 'AsyncIterator', 'AsyncIterable', 'Coroutine', 'AsyncGenerator', 'AsyncContextManager', 'ChainMap', 'ContextManager', 'Counter', 'Deque', 'DefaultDict', 'NamedTuple', 'OrderedDict', 'TypedDict', 'SupportsIndex', 'Annotated', 'assert_never', 'assert_type', 'clear_overloads', 'dataclass_transform', 'deprecated', 'get_overloads', 'final', 'get_args', 'get_origin', 'get_type_hints', 'IntVar', 'is_typeddict', 'Literal', 'NewType', 'overload', 'override', 'Protocol', 'reveal_type', 'runtime', 'runtime_checkable', 'Text', 'TypeAlias', 'TypeGuard', 'TYPE_CHECKING', 'Never', 'NoReturn', 'Required', 'NotRequired']

GenericMeta = type
NoReturn: Incomplete
T = typing.TypeVar('T')
KT = typing.TypeVar('KT')
VT = typing.TypeVar('VT')
T_co = typing.TypeVar('T_co', covariant=True)
T_contra = typing.TypeVar('T_contra', contravariant=True)

class _AnyMeta(type):
    def __instancecheck__(self, obj): ...

class Any(metaclass=_AnyMeta):
    """Special type indicating an unconstrained type.
        - Any is compatible with every type.
        - Any assumed to have all methods.
        - All values assumed to be instances of Any.
        Note that all the above statements are true from the point of view of
        static type checkers. At runtime, Any should not be used with instance
        checks.
        """
    def __new__(cls, *args, **kwargs): ...

ClassVar: Incomplete
Final: Incomplete

class _FinalForm(typing._SpecialForm, _root=True):
    def __getitem__(self, parameters): ...

def final(f):
    """This decorator can be used to indicate to type checkers that
        the decorated method cannot be overridden, and decorated class
        cannot be subclassed. For example:

            class Base:
                @final
                def done(self) -> None:
                    ...
            class Sub(Base):
                def done(self) -> None:  # Error reported by type checker
                    ...
            @final
            class Leaf:
                ...
            class Other(Leaf):  # Error reported by type checker
                ...

        There is no runtime checking of these properties. The decorator
        sets the ``__final__`` attribute to ``True`` on the decorated object
        to allow runtime introspection.
        """
def IntVar(name): ...

Literal: Incomplete

class _LiteralForm(typing._SpecialForm, _root=True):
    def __getitem__(self, parameters): ...
overload = typing.overload
get_overloads: Incomplete
clear_overloads: Incomplete
Type: Incomplete
Awaitable = typing.Awaitable
Coroutine = typing.Coroutine
AsyncIterable = typing.AsyncIterable
AsyncIterator = typing.AsyncIterator
Deque: Incomplete
ContextManager: Incomplete
AsyncContextManager: Incomplete
DefaultDict: Incomplete
Counter: Incomplete
ChainMap: Incomplete
AsyncGenerator = typing.AsyncGenerator
NewType = typing.NewType
Text: Incomplete
TYPE_CHECKING: Incomplete
Protocol: Incomplete

class _ProtocolMeta(abc.ABCMeta):
    def __instancecheck__(cls, instance): ...

class Protocol(metaclass=_ProtocolMeta):
    """Base class for protocol classes. Protocol classes are defined as::

            class Proto(Protocol):
                def meth(self) -> int:
                    ...

        Such classes are primarily used with static type checkers that recognize
        structural subtyping (static duck-typing), for example::

            class C:
                def meth(self) -> int:
                    return 0

            def func(x: Proto) -> int:
                return x.meth()

            func(C())  # Passes static type check

        See PEP 544 for details. Protocol classes decorated with
        @typing_extensions.runtime act as simple-minded runtime protocol that checks
        only the presence of given attributes, ignoring their type signatures.

        Protocol classes can be generic, they are defined as::

            class GenProto(Protocol[T]):
                def meth(self) -> T:
                    ...
        """
    def __new__(cls, *args, **kwds): ...
    def __class_getitem__(cls, params): ...
    def __init_subclass__(cls, *args, **kwargs): ...
runtime_checkable = typing.runtime_checkable
runtime = runtime_checkable
SupportsIndex = typing.SupportsIndex

class SupportsIndex(Protocol):
    @abc.abstractmethod
    def __index__(self) -> int: ...

TypedDict: Incomplete
is_typeddict = typing.is_typeddict

class _TypedDictMeta(type):
    def __init__(cls, name, bases, ns, total: bool = True) -> None: ...
    def __new__(cls, name, bases, ns, total: bool = True): ...
    __instancecheck__: Incomplete
    __subclasscheck__: Incomplete

assert_type: Incomplete
get_type_hints = typing.get_type_hints
Annotated: Incomplete

class _AnnotatedAlias(typing._GenericAlias, _root=True):
    """Runtime representation of an annotated type.

        At its core 'Annotated[t, dec1, dec2, ...]' is an alias for the type 't'
        with extra annotations. The alias behaves like a normal typing alias,
        instantiating is the same as instantiating the underlying type, binding
        it to types is also the same.
        """
    __metadata__: Incomplete
    def __init__(self, origin, metadata) -> None: ...
    def copy_with(self, params): ...
    def __reduce__(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...

class Annotated:
    """Add context specific metadata to a type.

        Example: Annotated[int, runtime_check.Unsigned] indicates to the
        hypothetical runtime_check module that this type is an unsigned int.
        Every other consumer of this type can ignore this metadata and treat
        this type as int.

        The first argument to Annotated must be a valid type (and will be in
        the __origin__ field), the remaining arguments are kept as a tuple in
        the __extra__ field.

        Details:

        - It's an error to call `Annotated` with less than two arguments.
        - Nested Annotated are flattened::

            Annotated[Annotated[T, Ann1, Ann2], Ann3] == Annotated[T, Ann1, Ann2, Ann3]

        - Instantiating an annotated type is equivalent to instantiating the
        underlying type::

            Annotated[C, Ann1](5) == C(5)

        - Annotated can be used as a generic type alias::

            Optimized = Annotated[T, runtime.Optimize()]
            Optimized[int] == Annotated[int, runtime.Optimize()]

            OptimizedList = Annotated[List[T], runtime.Optimize()]
            OptimizedList[int] == Annotated[List[int], runtime.Optimize()]
        """
    def __new__(cls, *args, **kwargs) -> None: ...
    def __class_getitem__(cls, params): ...
    def __init_subclass__(cls, *args, **kwargs) -> None: ...

get_origin: Incomplete
get_args = typing.get_args
TypeAlias: Incomplete

class _TypeAliasForm(typing._SpecialForm, _root=True): ...

class _DefaultMixin:
    """Mixin for TypeVarLike defaults."""
    __default__: Incomplete
    def __init__(self, default) -> None: ...

class TypeVar(typing.TypeVar, _DefaultMixin, _root=True):
    """Type variable."""
    __module__: str
    __infer_variance__: Incomplete
    def __init__(self, name, *constraints, bound: Incomplete | None = None, covariant: bool = False, contravariant: bool = False, default=..., infer_variance: bool = False) -> None: ...
ParamSpecArgs = typing.ParamSpecArgs
ParamSpecKwargs = typing.ParamSpecKwargs

class _Immutable:
    """Mixin to indicate that object should not be copied."""
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...

class ParamSpecArgs(_Immutable):
    """The args for a ParamSpec object.

        Given a ParamSpec object P, P.args is an instance of ParamSpecArgs.

        ParamSpecArgs objects have a reference back to their ParamSpec:

        P.args.__origin__ is P

        This type is meant for runtime introspection and has no special meaning to
        static type checkers.
        """
    __origin__: Incomplete
    def __init__(self, origin) -> None: ...
    def __eq__(self, other): ...

class ParamSpecKwargs(_Immutable):
    """The kwargs for a ParamSpec object.

        Given a ParamSpec object P, P.kwargs is an instance of ParamSpecKwargs.

        ParamSpecKwargs objects have a reference back to their ParamSpec:

        P.kwargs.__origin__ is P

        This type is meant for runtime introspection and has no special meaning to
        static type checkers.
        """
    __origin__: Incomplete
    def __init__(self, origin) -> None: ...
    def __eq__(self, other): ...

class ParamSpec(typing.ParamSpec, _DefaultMixin, _root=True):
    """Parameter specification variable."""
    __module__: str
    def __init__(self, name, *, bound: Incomplete | None = None, covariant: bool = False, contravariant: bool = False, default=...) -> None: ...

class ParamSpec(list, _DefaultMixin):
    """Parameter specification variable.

        Usage::

           P = ParamSpec('P')

        Parameter specification variables exist primarily for the benefit of static
        type checkers.  They are used to forward the parameter types of one
        callable to another callable, a pattern commonly found in higher order
        functions and decorators.  They are only valid when used in ``Concatenate``,
        or s the first argument to ``Callable``. In Python 3.10 and higher,
        they are also supported in user-defined Generics at runtime.
        See class Generic for more information on generic types.  An
        example for annotating a decorator::

           T = TypeVar('T')
           P = ParamSpec('P')

           def add_logging(f: Callable[P, T]) -> Callable[P, T]:
               '''A type-safe decorator to add logging to a function.'''
               def inner(*args: P.args, **kwargs: P.kwargs) -> T:
                   logging.info(f'{f.__name__} was called')
                   return f(*args, **kwargs)
               return inner

           @add_logging
           def add_two(x: float, y: float) -> float:
               '''Add two numbers together.'''
               return x + y

        Parameter specification variables defined with covariant=True or
        contravariant=True can be used to declare covariant or contravariant
        generic types.  These keyword arguments are valid, but their actual semantics
        are yet to be decided.  See PEP 612 for details.

        Parameter specification variables can be introspected. e.g.:

           P.__name__ == 'T'
           P.__bound__ == None
           P.__covariant__ == False
           P.__contravariant__ == False

        Note that only parameter specification variables defined in global scope can
        be pickled.
        """
    __class__ = typing.TypeVar
    @property
    def args(self): ...
    @property
    def kwargs(self): ...
    __covariant__: Incomplete
    __contravariant__: Incomplete
    __bound__: Incomplete
    __module__: Incomplete
    def __init__(self, name, *, bound: Incomplete | None = None, covariant: bool = False, contravariant: bool = False, default=...) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __reduce__(self): ...
    def __call__(self, *args, **kwargs) -> None: ...

class _ConcatenateGenericAlias(list):
    __class__: Incomplete
    __origin__: Incomplete
    __args__: Incomplete
    def __init__(self, origin, args) -> None: ...
    def __hash__(self): ...
    def __call__(self, *args, **kwargs) -> None: ...
    @property
    def __parameters__(self): ...

Concatenate: Incomplete
TypeGuard: Incomplete

class _TypeGuardForm(typing._SpecialForm, _root=True): ...

class _SpecialForm(typing._Final, _root=True):
    __doc__: Incomplete
    def __init__(self, getitem) -> None: ...
    def __getattr__(self, item): ...
    def __mro_entries__(self, bases) -> None: ...
    def __reduce__(self): ...
    def __call__(self, *args, **kwds) -> None: ...
    def __or__(self, other): ...
    def __ror__(self, other): ...
    def __instancecheck__(self, obj) -> None: ...
    def __subclasscheck__(self, cls) -> None: ...
    def __getitem__(self, parameters): ...

def LiteralString(self, params) -> None:
    '''Represents an arbitrary literal string.

        Example::

          from typing_extensions import LiteralString

          def query(sql: LiteralString) -> ...:
              ...

          query("SELECT * FROM table")  # ok
          query(f"SELECT * FROM {input()}")  # not ok

        See PEP 675 for details.

        '''

Self: Incomplete
Never: Incomplete
Required: Incomplete
NotRequired: Incomplete

class _ExtensionsSpecialForm(typing._SpecialForm, _root=True): ...

Unpack: Incomplete

class _UnpackSpecialForm(typing._SpecialForm, _root=True): ...

class _UnpackAlias(typing._GenericAlias, _root=True):
    __class__ = typing.TypeVar

class TypeVarTuple(typing.TypeVarTuple, _DefaultMixin, _root=True):
    """Type variable tuple."""
    __module__: Incomplete
    def __init__(self, name, *, default=...) -> None: ...

class TypeVarTuple(_DefaultMixin):
    """Type variable tuple.

        Usage::

            Ts = TypeVarTuple('Ts')

        In the same way that a normal type variable is a stand-in for a single
        type such as ``int``, a type variable *tuple* is a stand-in for a *tuple*
        type such as ``Tuple[int, str]``.

        Type variable tuples can be used in ``Generic`` declarations.
        Consider the following example::

            class Array(Generic[*Ts]): ...

        The ``Ts`` type variable tuple here behaves like ``tuple[T1, T2]``,
        where ``T1`` and ``T2`` are type variables. To use these type variables
        as type parameters of ``Array``, we must *unpack* the type variable tuple using
        the star operator: ``*Ts``. The signature of ``Array`` then behaves
        as if we had simply written ``class Array(Generic[T1, T2]): ...``.
        In contrast to ``Generic[T1, T2]``, however, ``Generic[*Shape]`` allows
        us to parameterise the class with an *arbitrary* number of type parameters.

        Type variable tuples can be used anywhere a normal ``TypeVar`` can.
        This includes class definitions, as shown above, as well as function
        signatures and variable annotations::

            class Array(Generic[*Ts]):

                def __init__(self, shape: Tuple[*Ts]):
                    self._shape: Tuple[*Ts] = shape

                def get_shape(self) -> Tuple[*Ts]:
                    return self._shape

            shape = (Height(480), Width(640))
            x: Array[Height, Width] = Array(shape)
            y = abs(x)  # Inferred type is Array[Height, Width]
            z = x + x   #        ...    is Array[Height, Width]
            x.get_shape()  #     ...    is tuple[Height, Width]

        """
    __class__ = typing.TypeVar
    def __iter__(self): ...
    __module__: Incomplete
    __unpacked__: Incomplete
    def __init__(self, name, *, default=...) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __reduce__(self): ...
    def __init_subclass__(self, *args, **kwds) -> None: ...

reveal_type: Incomplete
assert_never: Incomplete

def dataclass_transform(*, eq_default: bool = True, order_default: bool = False, kw_only_default: bool = False, frozen_default: bool = False, field_specifiers: typing.Tuple[typing.Type[typing.Any] | typing.Callable[..., typing.Any], ...] = (), **kwargs: typing.Any) -> typing.Callable[[T], T]:
    '''Decorator that marks a function, class, or metaclass as providing
        dataclass-like behavior.

        Example:

            from typing_extensions import dataclass_transform

            _T = TypeVar("_T")

            # Used on a decorator function
            @dataclass_transform()
            def create_model(cls: type[_T]) -> type[_T]:
                ...
                return cls

            @create_model
            class CustomerModel:
                id: int
                name: str

            # Used on a base class
            @dataclass_transform()
            class ModelBase: ...

            class CustomerModel(ModelBase):
                id: int
                name: str

            # Used on a metaclass
            @dataclass_transform()
            class ModelMeta(type): ...

            class ModelBase(metaclass=ModelMeta): ...

            class CustomerModel(ModelBase):
                id: int
                name: str

        Each of the ``CustomerModel`` classes defined in this example will now
        behave similarly to a dataclass created with the ``@dataclasses.dataclass``
        decorator. For example, the type checker will synthesize an ``__init__``
        method.

        The arguments to this decorator can be used to customize this behavior:
        - ``eq_default`` indicates whether the ``eq`` parameter is assumed to be
          True or False if it is omitted by the caller.
        - ``order_default`` indicates whether the ``order`` parameter is
          assumed to be True or False if it is omitted by the caller.
        - ``kw_only_default`` indicates whether the ``kw_only`` parameter is
          assumed to be True or False if it is omitted by the caller.
        - ``frozen_default`` indicates whether the ``frozen`` parameter is
          assumed to be True or False if it is omitted by the caller.
        - ``field_specifiers`` specifies a static list of supported classes
          or functions that describe fields, similar to ``dataclasses.field()``.

        At runtime, this decorator records its arguments in the
        ``__dataclass_transform__`` attribute on the decorated object.

        See PEP 681 for details.

        '''

override: Incomplete
deprecated: Incomplete

class _NamedTupleMeta(type):
    def __new__(cls, typename, bases, ns): ...

def NamedTuple(__typename, __fields: Incomplete | None = None, **kwargs): ...

# Names in __all__ with no definition:
#   OrderedDict
