from _typeshed import Incomplete
from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import anno as anno, parser as parser, qual_names as qual_names, templates as templates
from tensorflow.python.autograph.utils import ag_logging as ag_logging

class _Function:
    no_root: bool
    context_name: Incomplete
    def __init__(self) -> None: ...

set_trace_warned: bool

class _ArgTemplateBuilder:
    """Constructs a tuple representing the positional arguments in a call.

  Example (yes, it's legal Python 3):

      f(*args1, b, *args2, c, d)  ->  args1 + (b,) + args2 + (c, d)
  """
    def __init__(self) -> None: ...
    def add_arg(self, a) -> None: ...
    def add_stararg(self, a) -> None: ...
    def finalize(self) -> None: ...
    def to_ast(self): ...

class CallTreeTransformer(converter.Base):
    """Transforms the call tree by renaming transformed symbols."""
    def visit_Lambda(self, node): ...
    def visit_FunctionDef(self, node): ...
    def visit_With(self, node): ...
    def visit_Call(self, node): ...

def transform(node, ctx):
    """Transform function call to the compiled counterparts.

  Args:
    node: AST
    ctx: EntityContext
  Returns:
    A tuple (node, new_names):
        node: The transformed AST
        new_names: set(string), containing any newly-generated names
  """
