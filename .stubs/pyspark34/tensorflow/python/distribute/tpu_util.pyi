from collections.abc import Generator
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops
from tensorflow.python.tpu import tpu as tpu

def enclosing_tpu_context():
    """Returns the TPUReplicateContext, which exists inside a tpu.rewrite()."""
def enclosing_tpu_context_and_graph():
    """Returns the TPUReplicateContext which exists inside a tpu.rewrite(), and its associated graph."""
def outside_or_skip_tpu_context() -> Generator[None, None, None]:
    """Returns a context manager that skips current enclosing context if there is any."""
def make_raw_assign_fn(raw_assign_fn, use_handle: bool = True):
    """Wrap `raw_assign_fn` with the proper graph context and device scope.

  Args:
    raw_assign_fn: the function to be wrapped.
    use_handle: if True, the `raw_assign_fn` will be applied to the handle of a
      variable; otherwise it will be applied to the variable itself.

  Returns:
    The wrapped function.
  """
def make_raw_scatter_xxx_fn(raw_scatter_xxx_fn):
    """Wrap `raw_scatter_xxx_fn` so that it can be called w/ and w/o packed handle."""
