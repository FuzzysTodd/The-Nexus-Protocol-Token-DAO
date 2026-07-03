from _typeshed import Incomplete
from tensorflow.python.autograph.core import converter as converter
from tensorflow.python.autograph.pyct import anno as anno, parser as parser, qual_names as qual_names, templates as templates
from tensorflow.python.autograph.pyct.static_analysis import activity as activity
from tensorflow.python.autograph.pyct.static_analysis.annos import NodeAnno as NodeAnno

BODY_DEFINITELY_RETURNS: str
ORELSE_DEFINITELY_RETURNS: str
STMT_DEFINITELY_RETURNS: str

class _RewriteBlock:
    definitely_returns: bool
    def __init__(self) -> None: ...

class ConditionalReturnRewriter(converter.Base):
    """Rewrites a pattern where it's unobvious that all paths return a value.

  This rewrite allows avoiding intermediate None return values.

  The following pattern:

      if cond:
        <block 1>
        return
      else:
        <block 2>
      <block 3>

  is converted to:

      if cond:
        <block 1>
        return
      else:
        <block 2>
        <block 3>

  and vice-versa (if the else returns, subsequent statements are moved under the
  if branch).
  """
    def visit_Return(self, node): ...
    def visit_While(self, node): ...
    def visit_For(self, node): ...
    def visit_With(self, node): ...
    def visit_Try(self, node): ...
    def visit_ExceptHandler(self, node): ...
    def visit_If(self, node): ...
    def visit_FunctionDef(self, node): ...

class _Block:
    is_function: bool
    return_used: bool
    create_guard_next: bool
    create_guard_now: bool
    def __init__(self) -> None: ...

class _Function:
    do_return_var_name: Incomplete
    retval_var_name: Incomplete
    def __init__(self) -> None: ...

class ReturnStatementsTransformer(converter.Base):
    """Lowers return statements into variables and conditionals.

  Specifically, the following pattern:

      <block 1>
      return val
      <block 2>

  is converted to:

      do_return = False
      retval = None

      <block 1>

      do_return = True
      retval = val

      if not do_return:
        <block 2>

      return retval

  The conversion adjusts loops as well:

      <block 1>
      while cond:
        <block 2>
        return retval

  is converted to:

      <block 1>
      while not do_return and cond:
        <block 2>
        do_return = True
        retval = val
  """
    allow_missing_return: Incomplete
    def __init__(self, ctx, allow_missing_return) -> None: ...
    def visit_Return(self, node): ...
    def visit_While(self, node): ...
    def visit_For(self, node): ...
    def visit_With(self, node): ...
    def visit_Try(self, node): ...
    def visit_ExceptHandler(self, node): ...
    def visit_If(self, node): ...
    def visit_FunctionDef(self, node): ...

def transform(node, ctx, default_to_null_return: bool = True):
    """Ensure a function has only a single return, at the end."""
