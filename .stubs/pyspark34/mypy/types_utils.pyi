from mypy.nodes import ARG_STAR as ARG_STAR, ARG_STAR2 as ARG_STAR2, FuncItem as FuncItem, TypeAlias as TypeAlias
from mypy.types import AnyType as AnyType, CallableType as CallableType, Instance as Instance, NoneType as NoneType, Overloaded as Overloaded, ParamSpecType as ParamSpecType, ProperType as ProperType, TupleType as TupleType, Type as Type, TypeAliasType as TypeAliasType, TypeType as TypeType, TypeVarType as TypeVarType, UnionType as UnionType, UnpackType as UnpackType, flatten_nested_unions as flatten_nested_unions, get_proper_type as get_proper_type, get_proper_types as get_proper_types
from typing import Callable, Iterable

def flatten_types(types: Iterable[Type]) -> Iterable[Type]: ...
def strip_type(typ: Type) -> Type:
    """Make a copy of type without 'debugging info' (function name)."""
def is_invalid_recursive_alias(seen_nodes: set[TypeAlias], target: Type) -> bool:
    """Flag aliases like A = Union[int, A] (and similar mutual aliases).

    Such aliases don't make much sense, and cause problems in later phases.
    """
def is_bad_type_type_item(item: Type) -> bool:
    """Prohibit types like Type[Type[...]].

    Such types are explicitly prohibited by PEP 484. Also, they cause problems
    with recursive types like T = Type[T], because internal representation of
    TypeType item is normalized (i.e. always a proper type).
    """
def is_union_with_any(tp: Type) -> bool:
    """Is this a union with Any or a plain Any type?"""
def is_generic_instance(tp: Type) -> bool: ...
def is_optional(t: Type) -> bool: ...
def remove_optional(typ: Type) -> Type: ...
def is_self_type_like(typ: Type, *, is_classmethod: bool) -> bool:
    """Does this look like a self-type annotation?"""
def store_argument_type(defn: FuncItem, i: int, typ: CallableType, named_type: Callable[[str, list[Type]], Instance]) -> None: ...
