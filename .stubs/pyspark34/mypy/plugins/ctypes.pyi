import mypy.plugin
from mypy import nodes as nodes
from mypy.maptype import map_instance_to_supertype as map_instance_to_supertype
from mypy.messages import format_type as format_type
from mypy.subtypes import is_subtype as is_subtype
from mypy.typeops import make_simplified_union as make_simplified_union
from mypy.types import AnyType as AnyType, CallableType as CallableType, Instance as Instance, NoneType as NoneType, ProperType as ProperType, Type as Type, TypeOfAny as TypeOfAny, UnionType as UnionType, flatten_nested_unions as flatten_nested_unions, get_proper_type as get_proper_type

def array_constructor_callback(ctx: mypy.plugin.FunctionContext) -> Type:
    """Callback to provide an accurate signature for the ctypes.Array constructor."""
def array_getitem_callback(ctx: mypy.plugin.MethodContext) -> Type:
    """Callback to provide an accurate return type for ctypes.Array.__getitem__."""
def array_setitem_callback(ctx: mypy.plugin.MethodSigContext) -> CallableType:
    """Callback to provide an accurate signature for ctypes.Array.__setitem__."""
def array_iter_callback(ctx: mypy.plugin.MethodContext) -> Type:
    """Callback to provide an accurate return type for ctypes.Array.__iter__."""
def array_value_callback(ctx: mypy.plugin.AttributeContext) -> Type:
    """Callback to provide an accurate type for ctypes.Array.value."""
def array_raw_callback(ctx: mypy.plugin.AttributeContext) -> Type:
    """Callback to provide an accurate type for ctypes.Array.raw."""
