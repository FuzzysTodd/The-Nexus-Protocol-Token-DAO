from mypy import message_registry as message_registry
from mypy.nodes import DictExpr as DictExpr, IntExpr as IntExpr, StrExpr as StrExpr, UnaryExpr as UnaryExpr
from mypy.plugin import AttributeContext as AttributeContext, ClassDefContext as ClassDefContext, FunctionContext as FunctionContext, FunctionSigContext as FunctionSigContext, MethodContext as MethodContext, MethodSigContext as MethodSigContext, Plugin as Plugin
from mypy.plugins.common import try_getting_str_literals as try_getting_str_literals
from mypy.subtypes import is_subtype as is_subtype
from mypy.typeops import is_literal_type_like as is_literal_type_like, make_simplified_union as make_simplified_union
from mypy.types import AnyType as AnyType, CallableType as CallableType, FunctionLike as FunctionLike, Instance as Instance, LiteralType as LiteralType, NoneType as NoneType, TPDICT_FB_NAMES as TPDICT_FB_NAMES, TupleType as TupleType, Type as Type, TypeOfAny as TypeOfAny, TypeVarType as TypeVarType, TypedDictType as TypedDictType, get_proper_type as get_proper_type
from typing import Callable

class DefaultPlugin(Plugin):
    """Type checker plugin that is enabled by default."""
    def get_function_hook(self, fullname: str) -> Callable[[FunctionContext], Type] | None: ...
    def get_function_signature_hook(self, fullname: str) -> Callable[[FunctionSigContext], FunctionLike] | None: ...
    def get_method_signature_hook(self, fullname: str) -> Callable[[MethodSigContext], FunctionLike] | None: ...
    def get_method_hook(self, fullname: str) -> Callable[[MethodContext], Type] | None: ...
    def get_attribute_hook(self, fullname: str) -> Callable[[AttributeContext], Type] | None: ...
    def get_class_decorator_hook(self, fullname: str) -> Callable[[ClassDefContext], None] | None: ...
    def get_class_decorator_hook_2(self, fullname: str) -> Callable[[ClassDefContext], bool] | None: ...

def typed_dict_get_signature_callback(ctx: MethodSigContext) -> CallableType:
    """Try to infer a better signature type for TypedDict.get.

    This is used to get better type context for the second argument that
    depends on a TypedDict value type.
    """
def typed_dict_get_callback(ctx: MethodContext) -> Type:
    """Infer a precise return type for TypedDict.get with literal first argument."""
def typed_dict_pop_signature_callback(ctx: MethodSigContext) -> CallableType:
    """Try to infer a better signature type for TypedDict.pop.

    This is used to get better type context for the second argument that
    depends on a TypedDict value type.
    """
def typed_dict_pop_callback(ctx: MethodContext) -> Type:
    """Type check and infer a precise return type for TypedDict.pop."""
def typed_dict_setdefault_signature_callback(ctx: MethodSigContext) -> CallableType:
    """Try to infer a better signature type for TypedDict.setdefault.

    This is used to get better type context for the second argument that
    depends on a TypedDict value type.
    """
def typed_dict_setdefault_callback(ctx: MethodContext) -> Type:
    """Type check TypedDict.setdefault and infer a precise return type."""
def typed_dict_delitem_callback(ctx: MethodContext) -> Type:
    """Type check TypedDict.__delitem__."""
def typed_dict_update_signature_callback(ctx: MethodSigContext) -> CallableType:
    """Try to infer a better signature type for TypedDict.update."""
def int_pow_callback(ctx: MethodContext) -> Type:
    """Infer a more precise return type for int.__pow__."""
def int_neg_callback(ctx: MethodContext) -> Type:
    """Infer a more precise return type for int.__neg__.

    This is mainly used to infer the return type as LiteralType
    if the original underlying object is a LiteralType object
    """
def tuple_mul_callback(ctx: MethodContext) -> Type:
    """Infer a more precise return type for tuple.__mul__ and tuple.__rmul__.

    This is used to return a specific sized tuple if multiplied by Literal int
    """
