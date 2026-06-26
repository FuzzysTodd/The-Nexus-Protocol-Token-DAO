from _typeshed import Incomplete
from mypy.literals import literal as literal
from mypy.nodes import AssertStmt as AssertStmt, Block as Block, CallExpr as CallExpr, ComparisonExpr as ComparisonExpr, Expression as Expression, FuncDef as FuncDef, IfStmt as IfStmt, Import as Import, ImportAll as ImportAll, ImportFrom as ImportFrom, IndexExpr as IndexExpr, IntExpr as IntExpr, LITERAL_YES as LITERAL_YES, MatchStmt as MatchStmt, MemberExpr as MemberExpr, NameExpr as NameExpr, OpExpr as OpExpr, SliceExpr as SliceExpr, StrExpr as StrExpr, TupleExpr as TupleExpr, UnaryExpr as UnaryExpr
from mypy.options import Options as Options
from mypy.patterns import AsPattern as AsPattern, OrPattern as OrPattern, Pattern as Pattern
from mypy.traverser import TraverserVisitor as TraverserVisitor
from typing import Tuple, TypeVar
from typing_extensions import Final

ALWAYS_TRUE: Final[int]
MYPY_TRUE: Final[int]
ALWAYS_FALSE: Final[int]
MYPY_FALSE: Final[int]
TRUTH_VALUE_UNKNOWN: Final[int]
inverted_truth_mapping: Final[Incomplete]
reverse_op: Final[Incomplete]

def infer_reachability_of_if_statement(s: IfStmt, options: Options) -> None: ...
def infer_reachability_of_match_statement(s: MatchStmt, options: Options) -> None: ...
def assert_will_always_fail(s: AssertStmt, options: Options) -> bool: ...
def infer_condition_value(expr: Expression, options: Options) -> int:
    """Infer whether the given condition is always true/false.

    Return ALWAYS_TRUE if always true, ALWAYS_FALSE if always false,
    MYPY_TRUE if true under mypy and false at runtime, MYPY_FALSE if
    false under mypy and true at runtime, else TRUTH_VALUE_UNKNOWN.
    """
def infer_pattern_value(pattern: Pattern) -> int: ...
def consider_sys_version_info(expr: Expression, pyversion: tuple[int, ...]) -> int:
    """Consider whether expr is a comparison involving sys.version_info.

    Return ALWAYS_TRUE, ALWAYS_FALSE, or TRUTH_VALUE_UNKNOWN.
    """
def consider_sys_platform(expr: Expression, platform: str) -> int:
    """Consider whether expr is a comparison involving sys.platform.

    Return ALWAYS_TRUE, ALWAYS_FALSE, or TRUTH_VALUE_UNKNOWN.
    """
Targ = TypeVar('Targ', int, str, Tuple[int, ...])

def fixed_comparison(left: Targ, op: str, right: Targ) -> int: ...
def contains_int_or_tuple_of_ints(expr: Expression) -> None | int | tuple[int, ...]: ...
def contains_sys_version_info(expr: Expression) -> None | int | tuple[int | None, int | None]: ...
def is_sys_attr(expr: Expression, name: str) -> bool: ...
def mark_block_unreachable(block: Block) -> None: ...

class MarkImportsUnreachableVisitor(TraverserVisitor):
    """Visitor that flags all imports nested within a node as unreachable."""
    def visit_import(self, node: Import) -> None: ...
    def visit_import_from(self, node: ImportFrom) -> None: ...
    def visit_import_all(self, node: ImportAll) -> None: ...

def mark_block_mypy_only(block: Block) -> None: ...

class MarkImportsMypyOnlyVisitor(TraverserVisitor):
    """Visitor that sets is_mypy_only (which affects priority)."""
    def visit_import(self, node: Import) -> None: ...
    def visit_import_from(self, node: ImportFrom) -> None: ...
    def visit_import_all(self, node: ImportAll) -> None: ...
    def visit_func_def(self, node: FuncDef) -> None: ...
