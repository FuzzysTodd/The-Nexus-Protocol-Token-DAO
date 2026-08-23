import mypy.plugin
from _typeshed import Incomplete
from mypy.applytype import apply_generic_arguments as apply_generic_arguments
from mypy.checker import TypeChecker as TypeChecker
from mypy.errorcodes import LITERAL_REQ as LITERAL_REQ
from mypy.expandtype import expand_type as expand_type, expand_type_by_instance as expand_type_by_instance
from mypy.exprtotype import TypeTranslationError as TypeTranslationError, expr_to_unanalyzed_type as expr_to_unanalyzed_type
from mypy.meet import meet_types as meet_types
from mypy.messages import format_type_bare as format_type_bare
from mypy.nodes import ARG_NAMED as ARG_NAMED, ARG_NAMED_OPT as ARG_NAMED_OPT, ARG_OPT as ARG_OPT, ARG_POS as ARG_POS, Argument as Argument, AssignmentStmt as AssignmentStmt, CallExpr as CallExpr, Context as Context, Decorator as Decorator, Expression as Expression, FuncDef as FuncDef, IndexExpr as IndexExpr, JsonDict as JsonDict, LambdaExpr as LambdaExpr, ListExpr as ListExpr, MDEF as MDEF, MemberExpr as MemberExpr, NameExpr as NameExpr, OverloadedFuncDef as OverloadedFuncDef, PlaceholderNode as PlaceholderNode, RefExpr as RefExpr, SymbolTableNode as SymbolTableNode, TempNode as TempNode, TupleExpr as TupleExpr, TypeApplication as TypeApplication, TypeInfo as TypeInfo, TypeVarExpr as TypeVarExpr, Var as Var, is_class_var as is_class_var
from mypy.plugin import SemanticAnalyzerPluginInterface as SemanticAnalyzerPluginInterface
from mypy.plugins.common import add_attribute_to_class as add_attribute_to_class, add_method as add_method, deserialize_and_fixup_type as deserialize_and_fixup_type
from mypy.server.trigger import make_wildcard_trigger as make_wildcard_trigger
from mypy.typeops import get_type_vars as get_type_vars, make_simplified_union as make_simplified_union, map_type_from_supertype as map_type_from_supertype
from mypy.types import AnyType as AnyType, CallableType as CallableType, FunctionLike as FunctionLike, Instance as Instance, LiteralType as LiteralType, NoneType as NoneType, Overloaded as Overloaded, ProperType as ProperType, TupleType as TupleType, Type as Type, TypeOfAny as TypeOfAny, TypeVarType as TypeVarType, UninhabitedType as UninhabitedType, UnionType as UnionType, get_proper_type as get_proper_type
from mypy.typevars import fill_typevars as fill_typevars
from mypy.util import unmangle as unmangle
from typing_extensions import Final

attr_class_makers: Final[Incomplete]
attr_dataclass_makers: Final[Incomplete]
attr_frozen_makers: Final[Incomplete]
attr_define_makers: Final[Incomplete]
attr_attrib_makers: Final[Incomplete]
attr_optional_converters: Final[Incomplete]
SELF_TVAR_NAME: Final[str]
MAGIC_ATTR_NAME: Final[str]
MAGIC_ATTR_CLS_NAME_TEMPLATE: Final[str]
ATTRS_INIT_NAME: Final[str]

class Converter:
    """Holds information about a `converter=` argument"""
    init_type: Incomplete
    ret_type: Incomplete
    def __init__(self, init_type: Type | None = None, ret_type: Type | None = None) -> None: ...

class Attribute:
    """The value of an attr.ib() call."""
    name: Incomplete
    info: Incomplete
    has_default: Incomplete
    init: Incomplete
    kw_only: Incomplete
    converter: Incomplete
    context: Incomplete
    init_type: Incomplete
    def __init__(self, name: str, info: TypeInfo, has_default: bool, init: bool, kw_only: bool, converter: Converter | None, context: Context, init_type: Type | None) -> None: ...
    def argument(self, ctx: mypy.plugin.ClassDefContext) -> Argument:
        """Return this attribute as an argument to __init__."""
    def serialize(self) -> JsonDict:
        """Serialize this object so it can be saved and restored."""
    @classmethod
    def deserialize(cls, info: TypeInfo, data: JsonDict, api: SemanticAnalyzerPluginInterface) -> Attribute:
        """Return the Attribute that was serialized."""
    def expand_typevar_from_subtype(self, sub_type: TypeInfo) -> None:
        """Expands type vars in the context of a subtype when an attribute is inherited
        from a generic super type."""

def attr_tag_callback(ctx: mypy.plugin.ClassDefContext) -> None:
    """Record that we have an attrs class in the main semantic analysis pass.

    The later pass implemented by attr_class_maker_callback will use this
    to detect attrs classes in base classes.
    """
def attr_class_maker_callback(ctx: mypy.plugin.ClassDefContext, auto_attribs_default: bool | None = False, frozen_default: bool = False) -> bool:
    """Add necessary dunder methods to classes decorated with attr.s.

    attrs is a package that lets you define classes without writing dull boilerplate code.

    At a quick glance, the decorator searches the class body for assignments of `attr.ib`s (or
    annotated variables if auto_attribs=True), then depending on how the decorator is called,
    it will add an __init__ or all the compare methods.
    For frozen=True it will turn the attrs into properties.

    See https://www.attrs.org/en/stable/how-does-it-work.html for information on how attrs works.

    If this returns False, some required metadata was not ready yet and we need another
    pass.
    """
def is_valid_overloaded_converter(defn: OverloadedFuncDef) -> bool: ...

class MethodAdder:
    """Helper to add methods to a TypeInfo.

    ctx: The ClassDefCtx we are using on which we will add methods.
    """
    ctx: Incomplete
    self_type: Incomplete
    def __init__(self, ctx: mypy.plugin.ClassDefContext) -> None: ...
    def add_method(self, method_name: str, args: list[Argument], ret_type: Type, self_type: Type | None = None, tvd: TypeVarType | None = None) -> None:
        """Add a method: def <method_name>(self, <args>) -> <ret_type>): ... to info.

        self_type: The type to use for the self argument or None to use the inferred self type.
        tvd: If the method is generic these should be the type variables.
        """

def evolve_function_sig_callback(ctx: mypy.plugin.FunctionSigContext) -> CallableType:
    """
    Generates a signature for the 'attr.evolve' function that's specific to the call site
    and dependent on the type of the first argument.
    """
