from mypy.erasetype import erase_typevars as erase_typevars
from mypy.nodes import TypeInfo as TypeInfo
from mypy.types import AnyType as AnyType, Instance as Instance, ParamSpecType as ParamSpecType, TupleType as TupleType, Type as Type, TypeOfAny as TypeOfAny, TypeVarLikeType as TypeVarLikeType, TypeVarTupleType as TypeVarTupleType, TypeVarType as TypeVarType, UnpackType as UnpackType

def fill_typevars(typ: TypeInfo) -> Instance | TupleType:
    """For a non-generic type, return instance type representing the type.

    For a generic G type with parameters T1, .., Tn, return G[T1, ..., Tn].
    """
def fill_typevars_with_any(typ: TypeInfo) -> Instance | TupleType:
    """Apply a correct number of Any's as type arguments to a type."""
def has_no_typevars(typ: Type) -> bool: ...
