from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops
from tensorflow.python.util.tf_export import tf_export as tf_export

class _XlaScope:
    """Keeps track of previous XLA scope calls, and depth of current call."""
    count: Incomplete
    depth: Incomplete
    def __init__(self, count, depth) -> None: ...

def experimental_jit_scope(compile_ops: bool = True, separate_compiled_gradients: bool = False) -> Generator[None, None, Incomplete]:
    """Enable or disable JIT compilation of operators within the scope.

  NOTE: This is an experimental feature.

  The compilation is a hint and only supported on a best-effort basis.

  Example usage:

    ```python
    with tf.xla.experimental.jit_scope():
      c = tf.matmul(a, b)  # compiled
    with tf.xla.experimental.jit_scope(compile_ops=False):
      d = tf.matmul(a, c)  # not compiled
    with tf.xla.experimental.jit_scope(
        compile_ops=lambda node_def: 'matmul' in node_def.op.lower()):
      e = tf.matmul(a, b) + d  # matmul is compiled, the addition is not.
    ```

  Example of `separate_compiled_gradients`:

    ```python
    # In the example below, the computations for f, g and h will all be compiled
    # in separate scopes.
    with tf.xla.experimental.jit_scope(
        separate_compiled_gradients=True):
      f = tf.matmul(a, b)
    g = tf.gradients([f], [a, b], name='mygrads1')
    h = tf.gradients([f], [a, b], name='mygrads2')
    ```

  Ops that are not in the scope may be clustered and compiled with ops in
  the scope with `compile_ops=True`, while the ops in the scope with
  `compile_ops=False` will never be compiled.

  For example:

    ```python
    # In the example below, x and loss may be clustered and compiled together,
    # while y will not be compiled.
    with tf.xla.experimental.jit_scope():
      x = tf.matmul(a, b)
    with tf.xla.experimental.jit_scope(compile_ops=False):
      y = tf.matmul(c, d)
    loss = x + y
    ```

  If you want to only compile the ops in the scope with `compile_ops=True`,
  consider adding an outer `jit_scope(compile_ops=False)`:

    ```python
    # In the example below, only x will be compiled.
    with tf.xla.experimental.jit_scope(compile_ops=False):
      with tf.xla.experimental.jit_scope():
        x = tf.matmul(a, b)
      y = tf.matmul(c, d)
      loss = x + y
    ```

  Args:
    compile_ops: Whether to enable or disable compilation in the scope.
      Either a Python bool, or a callable that accepts the parameter
      `node_def` and returns a python bool.
    separate_compiled_gradients: If true put each gradient subgraph into a
      separate compilation scope. This gives fine-grained control over which
      portions of the graph will be compiled as a single unit. Compiling
      gradients separately may yield better performance for some graphs.
      The scope is named based on the scope of the forward computation as well
      as the name of the gradients. As a result, the gradients will be compiled
      in a scope that is separate from both the forward computation, and from
      other gradients.
  Raises:
    RuntimeError: if called when eager execution is enabled.
  Yields:
    The current scope, enabling or disabling compilation.
  """
