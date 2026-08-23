from ... import util as util
from mypy.nodes import CallExpr, ClassDef as ClassDef, Expression as Expression, MemberExpr, NameExpr, SymbolNode as SymbolNode, TypeInfo
from mypy.plugin import SemanticAnalyzerPluginInterface as SemanticAnalyzerPluginInterface
from mypy.types import UnboundType as UnboundType
from typing import List

COLUMN: int
RELATIONSHIP: int
REGISTRY: int
COLUMN_PROPERTY: int
TYPEENGINE: int
MAPPED: int
DECLARATIVE_BASE: int
DECLARATIVE_META: int
MAPPED_DECORATOR: int
SYNONYM_PROPERTY: int
COMPOSITE_PROPERTY: int
DECLARED_ATTR: int
MAPPER_PROPERTY: int
AS_DECLARATIVE: int
AS_DECLARATIVE_BASE: int
DECLARATIVE_MIXIN: int
QUERY_EXPRESSION: int
NAMED_TYPE_BUILTINS_OBJECT: str
NAMED_TYPE_BUILTINS_STR: str
NAMED_TYPE_BUILTINS_LIST: str
NAMED_TYPE_SQLA_MAPPED: str

def has_base_type_id(info: TypeInfo, type_id: int) -> bool: ...
def mro_has_id(mro: List[TypeInfo], type_id: int) -> bool: ...
def type_id_for_unbound_type(type_: UnboundType, cls: ClassDef, api: SemanticAnalyzerPluginInterface) -> int | None: ...
def type_id_for_callee(callee: Expression) -> int | None: ...
def type_id_for_named_node(node: NameExpr | MemberExpr | SymbolNode) -> int | None: ...
def type_id_for_fullname(fullname: str) -> int | None: ...
def expr_to_mapped_constructor(expr: Expression) -> CallExpr: ...
