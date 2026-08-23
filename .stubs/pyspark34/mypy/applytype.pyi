from mypy.expandtype import expand_type as expand_type, expand_unpack_with_variables as expand_unpack_with_variables
from mypy.nodes import ARG_STAR as ARG_STAR, Context as Context
from mypy.types import AnyType as AnyType, CallableType as CallableType, Instance as Instance, ParamSpecType as ParamSpecType, Parameters as Parameters, PartialType as PartialType, TupleType as TupleType, Type as Type, TypeVarId as TypeVarId, TypeVarLikeType as TypeVarLikeType, TypeVarTupleType as TypeVarTupleType, TypeVarType as TypeVarType, UnpackType as UnpackType, get_proper_type as get_proper_type
from mypy.typevartuples import find_unpack_in_list as find_unpack_in_list, replace_starargs as replace_starargs
from typing import Callable, Sequence

def get_target_type(tvar: TypeVarLikeType, type: Type, callable: CallableType, report_incompatible_typevar_value: Callable[[CallableType, Type, str, Context], None], context: Context, skip_unsatisfied: bool) -> Type | None: ...
def apply_generic_arguments(callable: CallableType, orig_types: Sequence[Type | None], report_incompatible_typevar_value: Callable[[CallableType, Type, str, Context], None], context: Context, skip_unsatisfied: bool = False) -> CallableType:
    """Apply generic type arguments to a callable type.

    For example, applying [int] to 'def [T] (T) -> T' results in
    'def (int) -> int'.

    Note that each type can be None; in this case, it will not be applied.

    If `skip_unsatisfied` is True, then just skip the types that don't satisfy type variable
    bound or constraints, instead of giving an error.
    """
