import mypy.plugin
from _typeshed import Incomplete
from mypy.nodes import ARG_POS as ARG_POS, ARG_STAR2 as ARG_STAR2, Argument as Argument, FuncItem as FuncItem, Var as Var
from mypy.plugins.common import add_method_to_class as add_method_to_class
from mypy.types import AnyType as AnyType, CallableType as CallableType, Type as Type, TypeOfAny as TypeOfAny, UnboundType as UnboundType, get_proper_type as get_proper_type
from typing import NamedTuple
from typing_extensions import Final

functools_total_ordering_makers: Final[Incomplete]

class _MethodInfo(NamedTuple):
    is_static: bool
    type: CallableType

def functools_total_ordering_maker_callback(ctx: mypy.plugin.ClassDefContext, auto_attribs_default: bool = False) -> bool:
    """Add dunder methods to classes decorated with functools.total_ordering."""
