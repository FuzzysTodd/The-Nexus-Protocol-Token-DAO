from _typeshed import Incomplete
from tensorflow.python.framework import ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops

def gcd(a, b, name: Incomplete | None = None):
    """Returns the greatest common divisor via Euclid's algorithm.

  Args:
    a: The dividend. A scalar integer `Tensor`.
    b: The divisor. A scalar integer `Tensor`.
    name: An optional name for the operation.

  Returns:
    A scalar `Tensor` representing the greatest common divisor between `a` and
    `b`.

  Raises:
    ValueError: If `a` or `b` are not scalar integers.
  """
