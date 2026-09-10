from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import array_ops as array_ops, gen_math_ops as gen_math_ops, math_ops as math_ops

def alias_tensors(*args):
    """Wraps any Tensor arguments with an identity op.

  Any other argument, including Variables, is returned unchanged.

  Args:
    *args: Any arguments. Must contain at least one element.

  Returns:
    Same as *args, with Tensor instances replaced as described.

  Raises:
    ValueError: If args doesn't meet the requirements.
  """
def get_range_len(start, limit, delta): ...
