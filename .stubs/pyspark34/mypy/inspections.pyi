from _typeshed import Incomplete
from mypy.build import State as State
from mypy.find_sources import InvalidSourceList as InvalidSourceList, SourceFinder as SourceFinder
from mypy.messages import format_type as format_type
from mypy.modulefinder import PYTHON_EXTENSIONS as PYTHON_EXTENSIONS
from mypy.nodes import Decorator as Decorator, Expression as Expression, FuncBase as FuncBase, LDEF as LDEF, MemberExpr as MemberExpr, MypyFile as MypyFile, Node as Node, OverloadedFuncDef as OverloadedFuncDef, RefExpr as RefExpr, SymbolNode as SymbolNode, TypeInfo as TypeInfo, Var as Var
from mypy.server.update import FineGrainedBuildManager as FineGrainedBuildManager
from mypy.traverser import ExtendedTraverserVisitor as ExtendedTraverserVisitor
from mypy.typeops import tuple_fallback as tuple_fallback
from mypy.types import FunctionLike as FunctionLike, Instance as Instance, LiteralType as LiteralType, ProperType as ProperType, TupleType as TupleType, TypeVarType as TypeVarType, TypedDictType as TypedDictType, UnionType as UnionType, get_proper_type as get_proper_type
from mypy.typevars import fill_typevars_with_any as fill_typevars_with_any
from typing import Callable

def node_starts_after(o: Node, line: int, column: int) -> bool: ...
def node_ends_before(o: Node, line: int, column: int) -> bool: ...
def expr_span(expr: Expression) -> str:
    """Format expression span as in mypy error messages."""
def get_instance_fallback(typ: ProperType) -> list[Instance]:
    """Returns the Instance fallback for this type if one exists or None."""
def find_node(name: str, info: TypeInfo) -> Var | FuncBase | None:
    """Find the node defining member 'name' in given TypeInfo."""
def find_module_by_fullname(fullname: str, modules: dict[str, State]) -> State | None:
    """Find module by a node fullname.

    This logic mimics the one we use in fixup, so should be good enough.
    """

class SearchVisitor(ExtendedTraverserVisitor):
    """Visitor looking for an expression whose span matches given one exactly."""
    line: Incomplete
    column: Incomplete
    end_line: Incomplete
    end_column: Incomplete
    result: Incomplete
    def __init__(self, line: int, column: int, end_line: int, end_column: int) -> None: ...
    def visit(self, o: Node) -> bool: ...

def find_by_location(tree: MypyFile, line: int, column: int, end_line: int, end_column: int) -> Expression | None:
    """Find an expression matching given span, or None if not found."""

class SearchAllVisitor(ExtendedTraverserVisitor):
    """Visitor looking for all expressions whose spans enclose given position."""
    line: Incomplete
    column: Incomplete
    result: Incomplete
    def __init__(self, line: int, column: int) -> None: ...
    def visit(self, o: Node) -> bool: ...

def find_all_by_location(tree: MypyFile, line: int, column: int) -> list[Expression]:
    """Find all expressions enclosing given position starting from innermost."""

class InspectionEngine:
    """Engine for locating and statically inspecting expressions."""
    fg_manager: Incomplete
    finder: Incomplete
    verbosity: Incomplete
    limit: Incomplete
    include_span: Incomplete
    include_kind: Incomplete
    include_object_attrs: Incomplete
    union_attrs: Incomplete
    force_reload: Incomplete
    module: Incomplete
    def __init__(self, fg_manager: FineGrainedBuildManager, *, verbosity: int = 0, limit: int = 0, include_span: bool = False, include_kind: bool = False, include_object_attrs: bool = False, union_attrs: bool = False, force_reload: bool = False) -> None: ...
    def parse_location(self, location: str) -> tuple[str, list[int]]: ...
    def reload_module(self, state: State) -> None:
        """Reload given module while temporary exporting types."""
    def expr_type(self, expression: Expression) -> tuple[str, bool]:
        """Format type for an expression using current options.

        If type is known, second item returned is True. If type is not known, an error
        message is returned instead, and second item returned is False.
        """
    def object_type(self) -> Instance: ...
    def collect_attrs(self, instances: list[Instance]) -> dict[TypeInfo, list[str]]:
        """Collect attributes from all union/typevar variants."""
    def expr_attrs(self, expression: Expression) -> tuple[str, bool]:
        """Format attributes that are valid for a given expression.

        If expression type is not an Instance, try using fallback. Attributes are
        returned as a JSON (ordered by MRO) that maps base class name to list of
        attributes. Attributes may appear in multiple bases if overridden (we simply
        follow usual mypy logic for creating new Vars etc).
        """
    def format_node(self, module: State, node: FuncBase | SymbolNode) -> str: ...
    def collect_nodes(self, expression: RefExpr) -> list[FuncBase | SymbolNode]:
        """Collect nodes that can be referred to by an expression.

        Note: it can be more than one for example in case of a union attribute.
        """
    def modules_for_nodes(self, nodes: list[FuncBase | SymbolNode], expression: RefExpr) -> tuple[dict[FuncBase | SymbolNode, State], bool]:
        """Gather modules where given nodes where defined.

        Also check if they need to be refreshed (cached nodes may have
        lines/columns missing).
        """
    def expression_def(self, expression: Expression) -> tuple[str, bool]:
        """Find and format definition location for an expression.

        If it is not a RefExpr, it is effectively skipped by returning an
        empty result.
        """
    def missing_type(self, expression: Expression) -> str: ...
    def missing_node(self, expression: Expression) -> str: ...
    def add_prefixes(self, result: str, expression: Expression) -> str: ...
    def run_inspection_by_exact_location(self, tree: MypyFile, line: int, column: int, end_line: int, end_column: int, method: Callable[[Expression], tuple[str, bool]]) -> dict[str, object]:
        """Get type of an expression matching a span.

        Type or error is returned as a standard daemon response dict.
        """
    def run_inspection_by_position(self, tree: MypyFile, line: int, column: int, method: Callable[[Expression], tuple[str, bool]]) -> dict[str, object]:
        """Get types of all expressions enclosing a position.

        Types and/or errors are returned as a standard daemon response dict.
        """
    def find_module(self, file: str) -> tuple[State | None, dict[str, object]]:
        """Find module by path, or return a suitable error message.

        Note we don't use exceptions to simplify handling 1 vs 2 statuses.
        """
    def run_inspection(self, location: str, method: Callable[[Expression], tuple[str, bool]]) -> dict[str, object]:
        """Top-level logic to inspect expression(s) at a location.

        This can be re-used by various simple inspections.
        """
    def get_type(self, location: str) -> dict[str, object]:
        """Get types of expression(s) at a location."""
    def get_attrs(self, location: str) -> dict[str, object]:
        """Get attributes of expression(s) at a location."""
    def get_definition(self, location: str) -> dict[str, object]:
        """Get symbol definitions of expression(s) at a location."""
