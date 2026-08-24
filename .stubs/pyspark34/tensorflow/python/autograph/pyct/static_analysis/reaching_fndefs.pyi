from _typeshed import Incomplete
from tensorflow.python.autograph.pyct import anno as anno, cfg as cfg, transformer as transformer

class Definition:
    """Definition objects describe a unique definition of a function."""
    def_node: Incomplete
    def __init__(self, def_node) -> None: ...

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
    def __add__(self, value): ...

class Analyzer(cfg.GraphVisitor):
    """CFG visitor that determines reaching definitions at statement level."""
    external_defs: Incomplete
    def __init__(self, graph, external_defs) -> None: ...
    def init_state(self, _): ...
    def visit_node(self, node): ...

class TreeAnnotator(transformer.Base):
    """AST visitor that annotates each symbol name with its reaching definitions.

  Simultaneously, the visitor runs the dataflow analysis on each function node,
  accounting for the effect of closures. For example:

    def foo():
      def f():
        pass
      def g():
        # `def f` reaches here
  """
    graphs: Incomplete
    allow_skips: bool
    current_analyzer: Incomplete
    def __init__(self, source_info, graphs) -> None: ...
    def visit_FunctionDef(self, node): ...
    def visit_Lambda(self, node): ...
    def visit(self, node): ...

def resolve(node, source_info, graphs):
    """Resolves reaching definitions for each symbol.

  Args:
    node: ast.AST
    source_info: transformer.SourceInfo
    graphs: Dict[ast.FunctionDef, cfg.Graph]
  Returns:
    ast.AST
  """
