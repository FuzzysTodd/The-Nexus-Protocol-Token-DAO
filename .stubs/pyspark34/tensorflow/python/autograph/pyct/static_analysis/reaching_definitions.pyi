from _typeshed import Incomplete
from tensorflow.python.autograph.pyct import anno as anno, cfg as cfg, transformer as transformer

class Definition:
    """Definition objects describe a unique definition of a variable.

  Subclasses of this may be used by passing an appropriate factory function to
  resolve.

  Attributes:
    param_of: Optional[ast.AST]
    directives: Dict, optional definition annotations
  """
    param_of: Incomplete
    directives: Incomplete
    def __init__(self) -> None: ...

class _NodeState:
    """Abstraction for the state of the CFG walk for reaching definition analysis.

  This is a value type. Only implements the strictly necessary operators.

  Attributes:
    value: Dict[qual_names.QN, Set[Definition, ...]], the defined symbols and
        their possible definitions
  """
    value: Incomplete
    def __init__(self, init_from: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __or__(self, other): ...
    def __sub__(self, other): ...

class Analyzer(cfg.GraphVisitor):
    """CFG visitor that determines reaching definitions at statement level."""
    gen_map: Incomplete
    def __init__(self, graph, definition_factory) -> None: ...
    def init_state(self, _): ...
    def visit_node(self, node): ...

class TreeAnnotator(transformer.Base):
    """AST visitor that annotates each symbol name with its reaching definitions.

  Simultaneously, the visitor runs the dataflow analysis on each function node,
  accounting for the effect of closures. For example:

    def foo():
      bar = 1
      def baz():
        # bar = 1 reaches here
  """
    allow_skips: bool
    definition_factory: Incomplete
    graphs: Incomplete
    current_analyzer: Incomplete
    current_cfg_node: Incomplete
    def __init__(self, source_info, graphs, definition_factory) -> None: ...
    def visit_FunctionDef(self, node): ...
    def visit_Name(self, node): ...
    def visit_If(self, node): ...
    def visit_For(self, node): ...
    def visit_While(self, node): ...
    def visit_Try(self, node): ...
    def visit_ExceptHandler(self, node): ...
    def visit(self, node): ...

def resolve(node, source_info, graphs, definition_factory=...):
    """Resolves reaching definitions for each symbol.

  Args:
    node: ast.AST
    source_info: transformer.SourceInfo
    graphs: Dict[ast.FunctionDef, cfg.Graph]
    definition_factory: Callable[[], Definition]
  Returns:
    ast.AST
  """
