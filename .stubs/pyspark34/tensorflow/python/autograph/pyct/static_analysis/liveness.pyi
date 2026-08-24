from _typeshed import Incomplete
from tensorflow.python.autograph.pyct import anno as anno, cfg as cfg, transformer as transformer
from tensorflow.python.autograph.pyct.static_analysis import annos as annos

class Analyzer(cfg.GraphVisitor):
    """CFG visitor that performs liveness analysis at statement level."""
    include_annotations: Incomplete
    def __init__(self, graph, include_annotations) -> None: ...
    def init_state(self, _): ...
    def lamba_check(self, fn_ast_node): ...
    def visit_node(self, node): ...

class TreeAnnotator(transformer.Base):
    """Runs liveness analysis on each of the functions defined in the AST.

  If a function defined other local functions, those will have separate CFGs.
  However, dataflow analysis needs to tie up these CFGs to properly emulate the
  effect of closures. In the case of liveness, the parent function's live
  variables must account for the variables that are live at the entry of each
  subfunction. For example:

    def foo():
      # baz is live from here on
      def bar():
        print(baz)

  This analyzer runs liveness analysis on each individual function, accounting
  for the effect above.
  """
    include_annotations: Incomplete
    allow_skips: bool
    graphs: Incomplete
    current_analyzer: Incomplete
    def __init__(self, source_info, graphs, include_annotations) -> None: ...
    def visit(self, node): ...
    def visit_Lambda(self, node): ...
    def visit_FunctionDef(self, node): ...
    def visit_If(self, node): ...
    def visit_For(self, node): ...
    def visit_While(self, node): ...
    def visit_Try(self, node): ...
    def visit_ExceptHandler(self, node): ...
    def visit_With(self, node): ...
    def visit_Expr(self, node): ...

def resolve(node, source_info, graphs, include_annotations: bool = True):
    """Resolves the live symbols at the exit of control flow statements.

  Args:
    node: ast.AST
    source_info: transformer.SourceInfo
    graphs: Dict[ast.FunctionDef, cfg.Graph]
    include_annotations: Bool, whether type annotations should be included in
      the analysis.
  Returns:
    ast.AST
  """
