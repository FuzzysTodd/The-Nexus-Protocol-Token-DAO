from _typeshed import Incomplete
from mypy import nodes as nodes
from mypy.infer import ArgumentInferContext as ArgumentInferContext
from mypy.maptype import map_instance_to_supertype as map_instance_to_supertype
from mypy.types import AnyType as AnyType, Instance as Instance, ParamSpecType as ParamSpecType, TupleType as TupleType, Type as Type, TypeOfAny as TypeOfAny, TypedDictType as TypedDictType, get_proper_type as get_proper_type
from typing import Callable, Sequence

def map_actuals_to_formals(actual_kinds: list[nodes.ArgKind], actual_names: Sequence[str | None] | None, formal_kinds: list[nodes.ArgKind], formal_names: Sequence[str | None], actual_arg_type: Callable[[int], Type]) -> list[list[int]]:
    """Calculate mapping between actual (caller) args and formals.

    The result contains a list of caller argument indexes mapping to each
    callee argument index, indexed by callee index.

    The caller_arg_type argument should evaluate to the type of the actual
    argument type with the given index.
    """
def map_formals_to_actuals(actual_kinds: list[nodes.ArgKind], actual_names: Sequence[str | None] | None, formal_kinds: list[nodes.ArgKind], formal_names: list[str | None], actual_arg_type: Callable[[int], Type]) -> list[list[int]]:
    """Calculate the reverse mapping of map_actuals_to_formals."""

class ArgTypeExpander:
    """Utility class for mapping actual argument types to formal arguments.

    One of the main responsibilities is to expand caller tuple *args and TypedDict
    **kwargs, and to keep track of which tuple/TypedDict items have already been
    consumed.

    Example:

       def f(x: int, *args: str) -> None: ...
       f(*(1, 'x', 1.1))

    We'd call expand_actual_type three times:

      1. The first call would provide 'int' as the actual type of 'x' (from '1').
      2. The second call would provide 'str' as one of the actual types for '*args'.
      2. The third call would provide 'float' as one of the actual types for '*args'.

    A single instance can process all the arguments for a single call. Each call
    needs a separate instance since instances have per-call state.
    """
    tuple_index: int
    kwargs_used: Incomplete
    context: Incomplete
    def __init__(self, context: ArgumentInferContext) -> None: ...
    def expand_actual_type(self, actual_type: Type, actual_kind: nodes.ArgKind, formal_name: str | None, formal_kind: nodes.ArgKind) -> Type:
        """Return the actual (caller) type(s) of a formal argument with the given kinds.

        If the actual argument is a tuple *args, return the next individual tuple item that
        maps to the formal arg.

        If the actual argument is a TypedDict **kwargs, return the next matching typed dict
        value type based on formal argument name and kind.

        This is supposed to be called for each formal, in order. Call multiple times per
        formal if multiple actuals map to a formal.
        """
