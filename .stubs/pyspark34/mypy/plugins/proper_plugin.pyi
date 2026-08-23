from mypy.checker import TypeChecker as TypeChecker
from mypy.nodes import TypeInfo as TypeInfo
from mypy.plugin import FunctionContext as FunctionContext, Plugin as Plugin
from mypy.subtypes import is_proper_subtype as is_proper_subtype
from mypy.types import AnyType as AnyType, FunctionLike as FunctionLike, Instance as Instance, NoneTyp as NoneTyp, ProperType as ProperType, TupleType as TupleType, Type as Type, UnionType as UnionType, get_proper_type as get_proper_type, get_proper_types as get_proper_types
from typing import Callable

class ProperTypePlugin(Plugin):
    """
    A plugin to ensure that every type is expanded before doing any special-casing.

    This solves the problem that we have hundreds of call sites like:

        if isinstance(typ, UnionType):
            ...  # special-case union

    But after introducing a new type TypeAliasType (and removing immediate expansion)
    all these became dangerous because typ may be e.g. an alias to union.
    """
    def get_function_hook(self, fullname: str) -> Callable[[FunctionContext], Type] | None: ...

def isinstance_proper_hook(ctx: FunctionContext) -> Type: ...
def is_special_target(right: ProperType) -> bool:
    """Whitelist some special cases for use in isinstance() with improper types."""
def is_improper_type(typ: Type) -> bool:
    """Is this a type that is not a subtype of ProperType?"""
def is_dangerous_target(typ: ProperType) -> bool:
    """Is this a dangerous target (right argument) for an isinstance() check?"""
def proper_type_hook(ctx: FunctionContext) -> Type:
    """Check if this get_proper_type() call is not redundant."""
def proper_types_hook(ctx: FunctionContext) -> Type:
    """Check if this get_proper_types() call is not redundant."""
def get_proper_type_instance(ctx: FunctionContext) -> Instance: ...
def plugin(version: str) -> type[ProperTypePlugin]: ...
