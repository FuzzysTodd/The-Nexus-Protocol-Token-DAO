from tensorflow.python.compat import compat as compat
from tensorflow.python.eager import context as context
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, gen_array_ops as gen_array_ops, gen_math_ops as gen_math_ops, math_ops as math_ops, special_math_ops as special_math_ops

def SmartBroadcastGradientArgs(x, y, grad):
    """Optimized version of `broadcast_gradient_args` that caches results.

  This implementation avoids creating `broadcast_gradient_args` ops in the case
  that the input shapes are fully defined, and provides hints to the calling
  code that can be used to avoid creating reduction and reshaping ops.

  Args:
    x: The left input tensor to a broadcasting binary op.
    y: The right input tensor to a broadcasting binary op.
    grad: The incoming gradient tensor for a broadcasting binary op.

  Returns:
    A pair of tuples, containing:
      * A 3-tuple of broadcast information for x, containing:
        * The shape of x (as a tuple or Tensor).
        * The reduction indices for x (as a tuple or Tensor).
        * A boolean, which if True, indicates that x's shape differs from grad's
          shape (and so x's gradient must be reduced and/or reshaped).
      * A 3-tuple of broadcast information for y, containing the respective
        details for y.
  """
