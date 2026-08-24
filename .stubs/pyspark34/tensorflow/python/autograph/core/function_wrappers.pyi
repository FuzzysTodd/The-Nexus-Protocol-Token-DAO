from _typeshed import Incomplete
from tensorflow.python.autograph.core import ag_ctx as ag_ctx, converter as converter
from tensorflow.python.autograph.operators import variables as variables
from tensorflow.python.framework import auto_control_deps as auto_control_deps, ops as ops, tensor_util as tensor_util
from tensorflow.python.util import nest as nest

class FunctionScope:
    """Context manager that wraps the body of a converted function.

  This context manager handles various operations related to the scope of a
  function:
    * optional TF name scopes - these name scopes match the name of the
        function, for easy visualization in tensorBoard;
    * optional automatic control dependencies - this adds the same mechanism
        for control dependencies that is used by `@tf.function`; it can be
        optionally enabled when using `tf.autograph.to_graph`;
    * tracking of autograph conversion state (whether it's enabled by the user,
        conversion options;
  """
    name: Incomplete
    options: Incomplete
    autograph_ctx: Incomplete
    callopts: Incomplete
    use_name_scope: Incomplete
    name_scope: Incomplete
    use_auto_deps: Incomplete
    autodeps_scope: Incomplete
    def __init__(self, function_name, scope_name, options) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def ret(self, value, did_return):
        """Marks a value as returned from the function guarded by the scope."""

def with_function_scope(thunk, scope_name, options):
    """Inline version of the FunctionScope context manager."""
