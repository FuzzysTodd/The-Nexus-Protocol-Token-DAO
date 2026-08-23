from _typeshed import Incomplete
from mypy.nodes import AssignmentStmt as AssignmentStmt, Block as Block, BreakStmt as BreakStmt, ClassDef as ClassDef, ContinueStmt as ContinueStmt, ForStmt as ForStmt, FuncDef as FuncDef, Import as Import, ImportAll as ImportAll, ImportFrom as ImportFrom, IndexExpr as IndexExpr, ListExpr as ListExpr, Lvalue as Lvalue, MatchStmt as MatchStmt, MemberExpr as MemberExpr, MypyFile as MypyFile, NameExpr as NameExpr, StarExpr as StarExpr, TryStmt as TryStmt, TupleExpr as TupleExpr, WhileStmt as WhileStmt, WithStmt as WithStmt
from mypy.patterns import AsPattern as AsPattern
from mypy.traverser import TraverserVisitor as TraverserVisitor
from typing import Iterator
from typing_extensions import Final

FILE: Final[int]
FUNCTION: Final[int]
CLASS: Final[int]

class VariableRenameVisitor(TraverserVisitor):
    '''Rename variables to allow redefinition of variables.

    For example, consider this code:

      x = 0
      f(x)

      x = "a"
      g(x)

    It will be transformed like this:

      x\' = 0
      f(x\')

      x = "a"
      g(x)

    There will be two independent variables (x\' and x) that will have separate
    inferred types. The publicly exposed variant will get the non-suffixed name.
    This is the last definition at module top level and the first definition
    (argument) within a function.

    Renaming only happens for assignments within the same block. Renaming is
    performed before semantic analysis, immediately after parsing.

    The implementation performs a rudimentary static analysis. The analysis is
    overly conservative to keep things simple.
    '''
    block_id: int
    disallow_redef_depth: int
    loop_depth: int
    block_loop_depth: Incomplete
    blocks: Incomplete
    var_blocks: Incomplete
    refs: Incomplete
    num_reads: Incomplete
    scope_kinds: Incomplete
    def __init__(self) -> None: ...
    def visit_mypy_file(self, file_node: MypyFile) -> None:
        """Rename variables within a file.

        This is the main entry point to this class.
        """
    def visit_func_def(self, fdef: FuncDef) -> None: ...
    def visit_class_def(self, cdef: ClassDef) -> None: ...
    def visit_block(self, block: Block) -> None: ...
    def visit_while_stmt(self, stmt: WhileStmt) -> None: ...
    def visit_for_stmt(self, stmt: ForStmt) -> None: ...
    def visit_break_stmt(self, stmt: BreakStmt) -> None: ...
    def visit_continue_stmt(self, stmt: ContinueStmt) -> None: ...
    def visit_try_stmt(self, stmt: TryStmt) -> None: ...
    def visit_with_stmt(self, stmt: WithStmt) -> None: ...
    def visit_import(self, imp: Import) -> None: ...
    def visit_import_from(self, imp: ImportFrom) -> None: ...
    def visit_assignment_stmt(self, s: AssignmentStmt) -> None: ...
    def visit_match_stmt(self, s: MatchStmt) -> None: ...
    def visit_capture_pattern(self, p: AsPattern) -> None: ...
    def analyze_lvalue(self, lvalue: Lvalue, is_nested: bool = False) -> None:
        '''Process assignment; in particular, keep track of (re)defined names.

        Args:
            is_nested: True for non-outermost Lvalue in a multiple assignment such as
                "x, y = ..."
        '''
    def visit_name_expr(self, expr: NameExpr) -> None: ...
    def handle_arg(self, name: str) -> None:
        """Store function argument."""
    def handle_def(self, expr: NameExpr) -> None:
        """Store new name definition."""
    def handle_refine(self, expr: NameExpr) -> None:
        """Store assignment to an existing name (that replaces previous value, if any)."""
    def handle_ref(self, expr: NameExpr) -> None:
        """Store reference to defined name."""
    def flush_refs(self) -> None:
        """Rename all references within the current scope.

        This will be called at the end of a scope.
        """
    def clear(self) -> None: ...
    def enter_block(self) -> Iterator[None]: ...
    def enter_try(self) -> Iterator[None]: ...
    def enter_loop(self) -> Iterator[None]: ...
    def current_block(self) -> int: ...
    def enter_scope(self, kind: int) -> Iterator[None]: ...
    def is_nested(self) -> int: ...
    def reject_redefinition_of_vars_in_scope(self) -> None:
        """Make it impossible to redefine defined variables in the current scope.

        This is used if we encounter a function definition that
        can make it ambiguous which definition is live. Example:

          x = 0

          def f() -> int:
              return x

          x = ''  # Error -- cannot redefine x across function definition
        """
    def reject_redefinition_of_vars_in_loop(self) -> None:
        """Reject redefinition of variables in the innermost loop.

        If there is an early exit from a loop, there may be ambiguity about which
        value may escape the loop. Example where this matters:

          while f():
              x = 0
              if g():
                  break
              x = ''  # Error -- not a redefinition
          reveal_type(x)  # int

        This method ensures that the second assignment to 'x' doesn't introduce a new
        variable.
        """
    def record_assignment(self, name: str, can_be_redefined: bool) -> bool:
        """Record assignment to given name and return True if it defines a new variable.

        Args:
            can_be_redefined: If True, allows assignment in the same block to redefine
                this name (if this is a new definition)
        """

class LimitedVariableRenameVisitor(TraverserVisitor):
    """Perform some limited variable renaming in with statements.

    This allows reusing a variable in multiple with statements with
    different types. For example, the two instances of 'x' can have
    incompatible types:

       with C() as x:
           f(x)
       with D() as x:
           g(x)

    The above code gets renamed conceptually into this (not valid Python!):

       with C() as x':
           f(x')
       with D() as x:
           g(x)

    If there's a reference to a variable defined in 'with' outside the
    statement, or if there's any trickiness around variable visibility
    (e.g. function definitions), we give up and won't perform renaming.

    The main use case is to allow binding both readable and writable
    binary files into the same variable. These have different types:

        with open(fnam, 'rb') as f: ...
        with open(fnam, 'wb') as f: ...
    """
    bound_vars: Incomplete
    skipped: Incomplete
    refs: Incomplete
    def __init__(self) -> None: ...
    def visit_mypy_file(self, file_node: MypyFile) -> None:
        """Rename variables within a file.

        This is the main entry point to this class.
        """
    def visit_func_def(self, fdef: FuncDef) -> None: ...
    def visit_class_def(self, cdef: ClassDef) -> None: ...
    def visit_with_stmt(self, stmt: WithStmt) -> None: ...
    def analyze_lvalue(self, lvalue: Lvalue) -> None: ...
    def visit_import(self, imp: Import) -> None: ...
    def visit_import_from(self, imp: ImportFrom) -> None: ...
    def visit_import_all(self, imp: ImportAll) -> None: ...
    def visit_name_expr(self, expr: NameExpr) -> None: ...
    def enter_scope(self) -> Iterator[None]: ...
    def reject_redefinition_of_vars_in_scope(self) -> None: ...
    def record_skipped(self, name: str) -> None: ...
    def flush_refs(self) -> None: ...

def rename_refs(names: list[NameExpr], index: int) -> None: ...
