from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops.numpy_ops import np_dtypes as np_dtypes

def convert_to_tensor(value, dtype: Incomplete | None = None, dtype_hint: Incomplete | None = None):
    """Wrapper over `tf.convert_to_tensor`.

  Args:
    value: value to convert
    dtype: (optional) the type we would like it to be converted to.
    dtype_hint: (optional) soft preference for the type we would like it to be
      converted to. `tf.convert_to_tensor` will attempt to convert value to this
      type first, but will not fail if conversion is not possible falling back
      to inferring the type instead.

  Returns:
    Value converted to tf.Tensor.
  """
ndarray = ops.Tensor
