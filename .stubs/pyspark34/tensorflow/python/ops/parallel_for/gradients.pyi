from _typeshed import Incomplete
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops
from tensorflow.python.ops.parallel_for import control_flow_ops as control_flow_ops
from tensorflow.python.util import nest as nest

def jacobian(output, inputs, use_pfor: bool = True, parallel_iterations: Incomplete | None = None):
    """Computes jacobian of `output` w.r.t. `inputs`.

  Args:
    output: A tensor.
    inputs: A tensor or a nested structure of tensor objects.
    use_pfor: If true, uses pfor for computing the jacobian. Else uses
      tf.while_loop.
    parallel_iterations: A knob to control how many iterations and dispatched in
      parallel. This knob can be used to control the total memory usage.

  Returns:
    A tensor or a nested structure of tensors with the same structure as
    `inputs`. Each entry is the jacobian of `output` w.r.t. to the corresponding
    value in `inputs`. If output has shape [y_1, ..., y_n] and inputs_i has
    shape [x_1, ..., x_m], the corresponding jacobian has shape
    [y_1, ..., y_n, x_1, ..., x_m]. Note that in cases where the gradient is
    sparse (IndexedSlices), jacobian function currently makes it dense and
    returns a Tensor instead. This may change in the future.
  """
def batch_jacobian(output, inp, use_pfor: bool = True, parallel_iterations: Incomplete | None = None):
    """Computes and stacks jacobians of `output[i,...]` w.r.t. `input[i,...]`.

  e.g.
  x = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
  y = x * x
  jacobian = batch_jacobian(y, x)
  # => [[[2,  0], [0,  4]], [[6,  0], [0,  8]]]

  Args:
    output: A tensor with shape [b, y1, ..., y_n]. `output[i,...]` should
      only depend on `inp[i,...]`.
    inp: A tensor with shape [b, x1, ..., x_m]
    use_pfor: If true, uses pfor for computing the Jacobian. Else uses a
      tf.while_loop.
    parallel_iterations: A knob to control how many iterations are vectorized
      and dispatched in parallel. The default value of None, when use_pfor is
      true, corresponds to vectorizing all the iterations. When use_pfor is
      false, the default value of None corresponds to parallel_iterations=10.
      This knob can be used to control the total memory usage.

  Returns:
    A tensor `t` with shape [b, y_1, ..., y_n, x1, ..., x_m] where `t[i, ...]`
    is the jacobian of `output[i, ...]` w.r.t. `inp[i, ...]`, i.e. stacked
    per-example jacobians.

  Raises:
    ValueError: if first dimension of `output` and `inp` do not match.
  """
