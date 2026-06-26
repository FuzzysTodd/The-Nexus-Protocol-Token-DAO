from _typeshed import Incomplete
from tensorflow.python.framework import random_seed as random_seed
from tensorflow.python.ops import array_ops as array_ops, random_ops as random_ops
from tensorflow.python.ops.numpy_ops import np_array_ops as np_array_ops, np_dtypes as np_dtypes, np_utils as np_utils

DEFAULT_RANDN_DTYPE: Incomplete

def seed(s) -> None:
    """Sets the seed for the random number generator.

  Uses `tf.set_random_seed`.

  Args:
    s: an integer.
  """
def randn(*args):
    """Returns samples from a normal distribution.

  Uses `tf.random_normal`.

  Args:
    *args: The shape of the output array.

  Returns:
    An ndarray with shape `args` and dtype `float64`.
  """
def standard_normal(size: Incomplete | None = None): ...
def uniform(low: float = 0.0, high: float = 1.0, size: Incomplete | None = None): ...
def poisson(lam: float = 1.0, size: Incomplete | None = None): ...
def random(size: Incomplete | None = None): ...
def rand(*size): ...
def randint(low, high: Incomplete | None = None, size: Incomplete | None = None, dtype=...): ...
