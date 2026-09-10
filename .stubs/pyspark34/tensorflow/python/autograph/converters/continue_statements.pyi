from _typeshed import Incomplete
from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import anno as anno, qual_names as qual_names, templates as templates
from tensorflow.python.autograph.pyct.static_analysis import activity as activity
from tensorflow.python.autograph.pyct.static_analysis.annos import NodeAnno as NodeAnno

class _Continue:
    used: bool
    control_var_name: Incomplete
    def __init__(self) -> None: ...

class _Block:
    """Tracks information about lexical blocks as they are visited in the AST.

  Mainly, this object tracks the creation of block guards that replace
  `continue` statements (e.g. `if not continue_:`).

  Attributes:
    create_guard_current: bool, whether to create a guard for the current
      statement.
    create_guard_next: bool, whether to create a guard for the next
      statement.
    is_loop_type: bool, whether this block is the body of a loop.
  """
    is_loop_type: bool
    create_guard_current: bool
    create_guard_next: bool
    def __init__(self) -> None: ...

class ContinueCanonicalizationTransformer(converter.Base):
    """Canonicalizes continue statements into additional conditionals."""
    def visit_Continue(self, node): ...
    def visit_While(self, node): ...
    def visit_For(self, node): ...
    def visit_If(self, node): ...
    def visit_With(self, node): ...
    def visit_Try(self, node): ...
    def visit_ExceptHandler(self, node): ...

def transform(node, ctx): ...
