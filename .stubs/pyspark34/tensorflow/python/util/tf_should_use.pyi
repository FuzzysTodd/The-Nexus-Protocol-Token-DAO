from _typeshed import Incomplete
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.util import tf_decorator as tf_decorator

class _TFShouldUseHelper:
    """Object stored in TFShouldUse-wrapped objects.

  When it is deleted it will emit a warning or error if its `sate` method
  has not been called by time of deletion, and Tensorflow is not executing
  eagerly or inside a tf.function (which use autodeps and resolve the
  main issues this wrapper warns about).
  """
    def __init__(self, type_, repr_, stack_frame, error_in_function, warn_in_eager) -> None: ...
    def sate(self) -> None: ...
    def __del__(self) -> None: ...

def should_use_result(fn: Incomplete | None = None, warn_in_eager: bool = False, error_in_function: bool = False):
    """Function wrapper that ensures the function's output is used.

  If the output is not used, a `logging.error` is logged.  If
  `error_in_function` is set, then a `RuntimeError` will be raised at the
  end of function tracing if the output is not used by that point.

  An output is marked as used if any of its attributes are read, modified, or
  updated.  Examples when the output is a `Tensor` include:

  - Using it in any capacity (e.g. `y = t + 0`, `sess.run(t)`)
  - Accessing a property (e.g. getting `t.name` or `t.op`).
  - Calling `t.mark_used()`.

  Note, certain behaviors cannot be tracked - for these the object may not
  be marked as used.  Examples include:

  - `t != 0`.  In this case, comparison is done on types / ids.
  - `isinstance(t, tf.Tensor)`.  Similar to above.

  Args:
    fn: The function to wrap.
    warn_in_eager: Whether to create warnings in Eager as well.
    error_in_function: Whether to raise an error when creating a tf.function.

  Returns:
    The wrapped function.
  """
