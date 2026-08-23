from mypy.constraints import Constraint as Constraint, SUPERTYPE_OF as SUPERTYPE_OF
from mypy.join import join_types as join_types
from mypy.meet import meet_types as meet_types
from mypy.subtypes import is_subtype as is_subtype
from mypy.types import AnyType as AnyType, ProperType as ProperType, Type as Type, TypeOfAny as TypeOfAny, TypeVarId as TypeVarId, UninhabitedType as UninhabitedType, UnionType as UnionType, get_proper_type as get_proper_type
from mypy.typestate import type_state as type_state

def solve_constraints(vars: list[TypeVarId], constraints: list[Constraint], strict: bool = True) -> list[Type | None]:
    """Solve type constraints.

    Return the best type(s) for type variables; each type can be None if the value of the variable
    could not be solved.

    If a variable has no constraints, if strict=True then arbitrarily
    pick NoneType as the value of the type variable.  If strict=False,
    pick AnyType.
    """
