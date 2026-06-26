from . import compat as compat
from _typeshed import Incomplete
from typing import Any, Callable, ForwardRef, Generic, Iterable, Mapping, NewType, NoReturn, Set, Tuple, Type, overload
from typing_extensions import Protocol as Protocol, TypeGuard as TypeGuard, get_args as get_args, get_origin as get_origin

NoneFwd: Incomplete
typing_get_args = get_args
typing_get_origin = get_origin

class ArgsTypeProcotol(Protocol):
    """protocol for types that have ``__args__``

    there's no public interface for this AFAIK

    """
    __args__: Tuple[_AnnotationScanType, ...]

class GenericProtocol(Protocol[_T]):
    """protocol for generic types.

    this since Python.typing _GenericAlias is private

    """
    __args__: Tuple[_AnnotationScanType, ...]
    __origin__: Type[_T]

class SupportsKeysAndGetItem(Protocol[_KT, _VT_co]):
    def keys(self) -> Iterable[_KT]: ...
    def __getitem__(self, __k: _KT) -> _VT_co: ...

def de_stringify_annotation(cls, annotation: _AnnotationScanType, originating_module: str, locals_: Mapping[str, Any], *, str_cleanup_fn: Callable[[str, str], str] | None = None, include_generic: bool = False, _already_seen: Set[Any] | None = None) -> Type[Any]:
    '''Resolve annotations that may be string based into real objects.

    This is particularly important if a module defines "from __future__ import
    annotations", as everything inside of __annotations__ is a string. We want
    to at least have generic containers like ``Mapped``, ``Union``, ``List``,
    etc.

    '''
def eval_expression(expression: str, module_name: str, *, locals_: Mapping[str, Any] | None = None) -> Any: ...
def eval_name_only(name: str, module_name: str, *, locals_: Mapping[str, Any] | None = None) -> Any: ...
def resolve_name_to_real_class_name(name: str, module_name: str) -> str: ...
def de_stringify_union_elements(cls, annotation: ArgsTypeProcotol, originating_module: str, locals_: Mapping[str, Any], *, str_cleanup_fn: Callable[[str, str], str] | None = None) -> Type[Any]: ...
def is_pep593(type_: _AnnotationScanType | None) -> bool: ...
def is_literal(type_: _AnnotationScanType) -> bool: ...
def is_newtype(type_: _AnnotationScanType | None) -> TypeGuard[NewType]: ...
def is_generic(type_: _AnnotationScanType) -> TypeGuard[GenericProtocol[Any]]: ...
def flatten_newtype(type_: NewType) -> Type[Any]: ...
def is_fwd_ref(type_: _AnnotationScanType, check_generic: bool = False) -> TypeGuard[ForwardRef]: ...
@overload
def de_optionalize_union_types(type_: str) -> str: ...
@overload
def de_optionalize_union_types(type_: Type[Any]) -> Type[Any]: ...
@overload
def de_optionalize_union_types(type_: _AnnotationScanType) -> _AnnotationScanType: ...
def de_optionalize_fwd_ref_union_types(type_: ForwardRef) -> _AnnotationScanType:
    """return the non-optional type for Optional[], Union[None, ...], x|None,
    etc. without de-stringifying forward refs.

    unfortunately this seems to require lots of hardcoded heuristics

    """
def make_union_type(*types: _AnnotationScanType) -> Type[Any]:
    """Make a Union type.

    This is needed by :func:`.de_optionalize_union_types` which removes
    ``NoneType`` from a ``Union``.

    """
def expand_unions(type_: Type[Any], include_union: bool = False, discard_none: bool = False) -> Tuple[Type[Any], ...]:
    """Return a type as a tuple of individual types, expanding for
    ``Union`` types."""
def is_optional(type_: Any) -> TypeGuard[ArgsTypeProcotol]: ...
def is_optional_union(type_: Any) -> bool: ...
def is_union(type_: Any) -> TypeGuard[ArgsTypeProcotol]: ...
def is_origin_of_cls(type_: Any, class_obj: Tuple[Type[Any], ...] | Type[Any]) -> bool:
    """return True if the given type has an __origin__ that shares a base
    with the given class"""
def is_origin_of(type_: Any, *names: str, module: str | None = None) -> bool:
    """return True if the given type has an __origin__ with the given name
    and optional module."""

class DescriptorProto(Protocol):
    def __get__(self, instance: object, owner: Any) -> Any: ...
    def __set__(self, instance: Any, value: Any) -> None: ...
    def __delete__(self, instance: Any) -> None: ...

class DescriptorReference(Generic[_DESC]):
    """a descriptor that refers to a descriptor.

    used for cases where we need to have an instance variable referring to an
    object that is itself a descriptor, which typically confuses typing tools
    as they don't know when they should use ``__get__`` or not when referring
    to the descriptor assignment as an instance variable. See
    sqlalchemy.orm.interfaces.PropComparator.prop

    """
    def __get__(self, instance: object, owner: Any) -> _DESC: ...
    def __set__(self, instance: Any, value: _DESC) -> None: ...
    def __delete__(self, instance: Any) -> None: ...

class RODescriptorReference(Generic[_DESC_co]):
    """a descriptor that refers to a descriptor.

    same as :class:`.DescriptorReference` but is read-only, so that subclasses
    can define a subtype as the generically contained element

    """
    def __get__(self, instance: object, owner: Any) -> _DESC_co: ...
    def __set__(self, instance: Any, value: Any) -> NoReturn: ...
    def __delete__(self, instance: Any) -> NoReturn: ...

class CallableReference(Generic[_FN]):
    """a descriptor that refers to a callable.

    works around mypy's limitation of not allowing callables assigned
    as instance variables


    """
    def __get__(self, instance: object, owner: Any) -> _FN: ...
    def __set__(self, instance: Any, value: _FN) -> None: ...
    def __delete__(self, instance: Any) -> None: ...
