from tensorflow.python.framework import dtypes as dtypes, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, resource_variable_ops as resource_variable_ops

def get_zeros_dtype(t):
    """Return the dtype for the default gradient for a Tensor."""
def shape_and_dtype(t):
    """Return the shape and dtype for the default gradient for a Tensor."""
def zeros_like(t):
    """Like array_ops.zeros_like, but respects resource handles."""
def ones_like(t):
    """Like array_ops.ones_like, but respects resource handles."""
def supports_default_grad(t):
    """Whether tensor `t` supports creating a default gradient.

  This function assumes that `t` is of a trainable type.

  Args:
    t: Tensor

  Returns:
    Bool
  """
