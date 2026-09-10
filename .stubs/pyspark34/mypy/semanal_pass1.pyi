from _typeshed import Incomplete
from mypy.nodes import AssertStmt as AssertStmt, AssignmentStmt as AssignmentStmt, Block as Block, ClassDef as ClassDef, ExpressionStmt as ExpressionStmt, ForStmt as ForStmt, FuncDef as FuncDef, IfStmt as IfStmt, Import as Import, ImportAll as ImportAll, ImportFrom as ImportFrom, MatchStmt as MatchStmt, MypyFile as MypyFile, ReturnStmt as ReturnStmt
from mypy.options import Options as Options
from mypy.reachability import assert_will_always_fail as assert_will_always_fail, infer_reachability_of_if_statement as infer_reachability_of_if_statement, infer_reachability_of_match_statement as infer_reachability_of_match_statement
from mypy.traverser import TraverserVisitor as TraverserVisitor

class SemanticAnalyzerPreAnalysis(TraverserVisitor):
    """Analyze reachability of blocks and imports and other local things.

    This runs before semantic analysis, so names have not been bound. Imports are
    also not resolved yet, so we can only access the current module.

    This determines static reachability of blocks and imports due to version and
    platform checks, among others.

    The main entry point is 'visit_file'.

    Reachability of imports needs to be determined very early in the build since
    this affects which modules will ultimately be processed.

    Consider this example:

      import sys

      def do_stuff():
          # type: () -> None:
          if sys.python_version < (3,):
              import xyz  # Only available in Python 2
              xyz.whatever()
          ...

    The block containing 'import xyz' is unreachable in Python 3 mode. The import
    shouldn't be processed in Python 3 mode, even if the module happens to exist.
    """
    platform: Incomplete
    cur_mod_id: Incomplete
    cur_mod_node: Incomplete
    options: Incomplete
    is_global_scope: bool
    unreachable_lines: Incomplete
    def visit_file(self, file: MypyFile, fnam: str, mod_id: str, options: Options) -> None: ...
    def visit_func_def(self, node: FuncDef) -> None: ...
    def visit_class_def(self, node: ClassDef) -> None: ...
    def visit_import_from(self, node: ImportFrom) -> None: ...
    def visit_import_all(self, node: ImportAll) -> None: ...
    def visit_import(self, node: Import) -> None: ...
    def visit_if_stmt(self, s: IfStmt) -> None: ...
    def visit_block(self, b: Block) -> None: ...
    def visit_match_stmt(self, s: MatchStmt) -> None: ...
    def visit_assignment_stmt(self, s: AssignmentStmt) -> None: ...
    def visit_expression_stmt(self, s: ExpressionStmt) -> None: ...
    def visit_return_stmt(self, s: ReturnStmt) -> None: ...
    def visit_for_stmt(self, s: ForStmt) -> None: ...
