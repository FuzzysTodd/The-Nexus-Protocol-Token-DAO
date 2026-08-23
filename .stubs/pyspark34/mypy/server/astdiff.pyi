from mypy.expandtype import expand_type as expand_type
from mypy.nodes import Decorator as Decorator, FuncBase as FuncBase, FuncDef as FuncDef, FuncItem as FuncItem, MypyFile as MypyFile, OverloadedFuncDef as OverloadedFuncDef, ParamSpecExpr as ParamSpecExpr, SymbolNode as SymbolNode, SymbolTable as SymbolTable, TypeAlias as TypeAlias, TypeInfo as TypeInfo, TypeVarExpr as TypeVarExpr, TypeVarTupleExpr as TypeVarTupleExpr, UNBOUND_IMPORTED as UNBOUND_IMPORTED, Var as Var
from mypy.semanal_shared import find_dataclass_transform_spec as find_dataclass_transform_spec
from mypy.types import AnyType as AnyType, CallableType as CallableType, DeletedType as DeletedType, ErasedType as ErasedType, Instance as Instance, LiteralType as LiteralType, NoneType as NoneType, Overloaded as Overloaded, ParamSpecType as ParamSpecType, Parameters as Parameters, PartialType as PartialType, TupleType as TupleType, Type as Type, TypeAliasType as TypeAliasType, TypeType as TypeType, TypeVarId as TypeVarId, TypeVarLikeType as TypeVarLikeType, TypeVarTupleType as TypeVarTupleType, TypeVarType as TypeVarType, TypeVisitor as TypeVisitor, TypedDictType as TypedDictType, UnboundType as UnboundType, UninhabitedType as UninhabitedType, UnionType as UnionType, UnpackType as UnpackType
from mypy.util import get_prefix as get_prefix
from typing import Sequence
from typing_extensions import TypeAlias as _TypeAlias

Primitive: _TypeAlias
SnapshotItem: _TypeAlias
SymbolSnapshot: _TypeAlias

def compare_symbol_table_snapshots(name_prefix: str, snapshot1: dict[str, SymbolSnapshot], snapshot2: dict[str, SymbolSnapshot]) -> set[str]:
    """Return names that are different in two snapshots of a symbol table.

    Only shallow (intra-module) differences are considered. References to things defined
    outside the module are compared based on the name of the target only.

    Recurse into class symbol tables (if the class is defined in the target module).

    Return a set of fully-qualified names (e.g., 'mod.func' or 'mod.Class.method').
    """
def snapshot_symbol_table(name_prefix: str, table: SymbolTable) -> dict[str, SymbolSnapshot]:
    '''Create a snapshot description that represents the state of a symbol table.

    The snapshot has a representation based on nested tuples and dicts
    that makes it easy and fast to find differences.

    Only "shallow" state is included in the snapshot -- references to
    things defined in other modules are represented just by the names of
    the targets.
    '''
def snapshot_definition(node: SymbolNode | None, common: SymbolSnapshot) -> SymbolSnapshot:
    """Create a snapshot description of a symbol table node.

    The representation is nested tuples and dicts. Only externally
    visible attributes are included.
    """
def snapshot_type(typ: Type) -> SnapshotItem:
    """Create a snapshot representation of a type using nested tuples."""
def snapshot_optional_type(typ: Type | None) -> SnapshotItem: ...
def snapshot_types(types: Sequence[Type]) -> SnapshotItem: ...
def snapshot_simple_type(typ: Type) -> SnapshotItem: ...
def encode_optional_str(s: str | None) -> str: ...

class SnapshotTypeVisitor(TypeVisitor[SnapshotItem]):
    """Creates a read-only, self-contained snapshot of a type object.

    Properties of a snapshot:

    - Contains (nested) tuples and other immutable primitive objects only.
    - References to AST nodes are replaced with full names of targets.
    - Has no references to mutable or non-primitive objects.
    - Two snapshots represent the same object if and only if they are
      equal.
    - Results must be sortable. It's important that tuples have
      consistent types and can't arbitrarily mix str and None values,
      for example, since they can't be compared.
    """
    def visit_unbound_type(self, typ: UnboundType) -> SnapshotItem: ...
    def visit_any(self, typ: AnyType) -> SnapshotItem: ...
    def visit_none_type(self, typ: None) -> SnapshotItem: ...
    def visit_uninhabited_type(self, typ: UninhabitedType) -> SnapshotItem: ...
    def visit_erased_type(self, typ: ErasedType) -> SnapshotItem: ...
    def visit_deleted_type(self, typ: DeletedType) -> SnapshotItem: ...
    def visit_instance(self, typ: Instance) -> SnapshotItem: ...
    def visit_type_var(self, typ: TypeVarType) -> SnapshotItem: ...
    def visit_param_spec(self, typ: ParamSpecType) -> SnapshotItem: ...
    def visit_type_var_tuple(self, typ: TypeVarTupleType) -> SnapshotItem: ...
    def visit_unpack_type(self, typ: UnpackType) -> SnapshotItem: ...
    def visit_parameters(self, typ: Parameters) -> SnapshotItem: ...
    def visit_callable_type(self, typ: CallableType) -> SnapshotItem: ...
    def normalize_callable_variables(self, typ: CallableType) -> CallableType:
        """Normalize all type variable ids to run from -1 to -len(variables)."""
    def visit_tuple_type(self, typ: TupleType) -> SnapshotItem: ...
    def visit_typeddict_type(self, typ: TypedDictType) -> SnapshotItem: ...
    def visit_literal_type(self, typ: LiteralType) -> SnapshotItem: ...
    def visit_union_type(self, typ: UnionType) -> SnapshotItem: ...
    def visit_overloaded(self, typ: Overloaded) -> SnapshotItem: ...
    def visit_partial_type(self, typ: PartialType) -> SnapshotItem: ...
    def visit_type_type(self, typ: TypeType) -> SnapshotItem: ...
    def visit_type_alias_type(self, typ: TypeAliasType) -> SnapshotItem: ...

def snapshot_untyped_signature(func: OverloadedFuncDef | FuncItem) -> SymbolSnapshot:
    """Create a snapshot of the signature of a function that has no explicit signature.

    If the arguments to a function without signature change, it must be
    considered as different. We have this special casing since we don't store
    the implicit signature anywhere, and we'd rather not construct new
    Callable objects in this module (the idea is to only read properties of
    the AST here).
    """
