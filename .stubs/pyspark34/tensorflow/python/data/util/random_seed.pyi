from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, random_seed as random_seed
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops

def get_seed(seed):
    """Returns the local seeds an operation should use given an op-specific seed.

  See `random_seed.get_seed` for more details. This wrapper adds support for
  the case where `seed` may be a tensor.

  Args:
    seed: An integer or a `tf.int64` scalar tensor.

  Returns:
    A tuple of two `tf.int64` scalar tensors that should be used for the local
    seed of the calling dataset.
  """
