from _typeshed import Incomplete
from mypy import errorcodes as errorcodes, message_registry as message_registry
from mypy.expandtype import expand_type as expand_type, expand_type_by_instance as expand_type_by_instance
from mypy.nodes import ARG_NAMED as ARG_NAMED, ARG_NAMED_OPT as ARG_NAMED_OPT, ARG_OPT as ARG_OPT, ARG_POS as ARG_POS, ARG_STAR as ARG_STAR, ARG_STAR2 as ARG_STAR2, Argument as Argument, AssignmentStmt as AssignmentStmt, Block as Block, CallExpr as CallExpr, ClassDef as ClassDef, Context as Context, DataclassTransformSpec as DataclassTransformSpec, Expression as Expression, FuncDef as FuncDef, IfStmt as IfStmt, JsonDict as JsonDict, MDEF as MDEF, NameExpr as NameExpr, Node as Node, PlaceholderNode as PlaceholderNode, RefExpr as RefExpr, Statement as Statement, SymbolTableNode as SymbolTableNode, TempNode as TempNode, TypeAlias as TypeAlias, TypeInfo as TypeInfo, TypeVarExpr as TypeVarExpr, Var as Var
from mypy.plugin import ClassDefContext as ClassDefContext, SemanticAnalyzerPluginInterface as SemanticAnalyzerPluginInterface
from mypy.plugins.common import add_attribute_to_class as add_attribute_to_class, add_method_to_class as add_method_to_class, deserialize_and_fixup_type as deserialize_and_fixup_type
from mypy.semanal_shared import find_dataclass_transform_spec as find_dataclass_transform_spec, require_bool_literal_argument as require_bool_literal_argument
from mypy.server.trigger import make_wildcard_trigger as make_wildcard_trigger
from mypy.state import state as state
from mypy.typeops import map_type_from_supertype as map_type_from_supertype, try_getting_literals_from_type as try_getting_literals_from_type
from mypy.types import AnyType as AnyType, CallableType as CallableType, Instance as Instance, LiteralType as LiteralType, NoneType as NoneType, TupleType as TupleType, Type as Type, TypeOfAny as TypeOfAny, TypeVarType as TypeVarType, get_proper_type as get_proper_type
from mypy.typevars import fill_typevars as fill_typevars
from typing import Optional
from typing_extensions import Final

dataclass_makers: Final[Incomplete]
SELF_TVAR_NAME: Final[str]

class DataclassAttribute:
    name: Incomplete
    alias: Incomplete
    is_in_init: Incomplete
    is_init_var: Incomplete
    has_default: Incomplete
    line: Incomplete
    column: Incomplete
    type: Incomplete
    info: Incomplete
    kw_only: Incomplete
    is_neither_frozen_nor_nonfrozen: Incomplete
    def __init__(self, name: str, alias: str | None, is_in_init: bool, is_init_var: bool, has_default: bool, line: int, column: int, type: Type | None, info: TypeInfo, kw_only: bool, is_neither_frozen_nor_nonfrozen: bool) -> None: ...
    def to_argument(self, current_info: TypeInfo) -> Argument: ...
    def expand_type(self, current_info: TypeInfo) -> Optional[Type]: ...
    def to_var(self, current_info: TypeInfo) -> Var: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, info: TypeInfo, data: JsonDict, api: SemanticAnalyzerPluginInterface) -> DataclassAttribute: ...
    def expand_typevar_from_subtype(self, sub_type: TypeInfo) -> None:
        """Expands type vars in the context of a subtype when an attribute is inherited
        from a generic super type."""

class DataclassTransformer:
    """Implement the behavior of @dataclass.

    Note that this may be executed multiple times on the same class, so
    everything here must be idempotent.

    This runs after the main semantic analysis pass, so you can assume that
    there are no placeholders.
    """
    def __init__(self, cls: ClassDef, reason: Expression | Statement, spec: DataclassTransformSpec, api: SemanticAnalyzerPluginInterface) -> None: ...
    def transform(self) -> bool:
        """Apply all the necessary transformations to the underlying
        dataclass so as to ensure it is fully type checked according
        to the rules in PEP 557.
        """
    def add_slots(self, info: TypeInfo, attributes: list[DataclassAttribute], *, correct_version: bool) -> None: ...
    def reset_init_only_vars(self, info: TypeInfo, attributes: list[DataclassAttribute]) -> None:
        """Remove init-only vars from the class and reset init var declarations."""
    def collect_attributes(self) -> list[DataclassAttribute] | None:
        """Collect all attributes declared in the dataclass and its parents.

        All assignments of the form

          a: SomeType
          b: SomeOtherType = ...

        are collected.

        Return None if some dataclass base class hasn't been processed
        yet and thus we'll need to ask for another pass.
        """

def add_dataclass_tag(info: TypeInfo) -> None: ...
def dataclass_tag_callback(ctx: ClassDefContext) -> None:
    """Record that we have a dataclass in the main semantic analysis pass.

    The later pass implemented by DataclassTransformer will use this
    to detect dataclasses in base classes.
    """
def dataclass_class_maker_callback(ctx: ClassDefContext) -> bool:
    """Hooks into the class typechecking process to add support for dataclasses."""
