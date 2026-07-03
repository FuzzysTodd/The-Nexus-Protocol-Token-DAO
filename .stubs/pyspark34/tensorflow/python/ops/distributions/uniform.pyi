from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, math_ops as math_ops, random_ops as random_ops
from tensorflow.python.ops.distributions import distribution as distribution
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

class Uniform(distribution.Distribution):
    """Uniform distribution with `low` and `high` parameters.

  #### Mathematical Details

  The probability density function (pdf) is,

  ```none
  pdf(x; a, b) = I[a <= x < b] / Z
  Z = b - a
  ```

  where

  - `low = a`,
  - `high = b`,
  - `Z` is the normalizing constant, and
  - `I[predicate]` is the [indicator function](
    https://en.wikipedia.org/wiki/Indicator_function) for `predicate`.

  The parameters `low` and `high` must be shaped in a way that supports
  broadcasting (e.g., `high - low` is a valid operation).

  #### Examples

  ```python
  # Without broadcasting:
  u1 = Uniform(low=3.0, high=4.0)  # a single uniform distribution [3, 4]
  u2 = Uniform(low=[1.0, 2.0],
               high=[3.0, 4.0])  # 2 distributions [1, 3], [2, 4]
  u3 = Uniform(low=[[1.0, 2.0],
                    [3.0, 4.0]],
               high=[[1.5, 2.5],
                     [3.5, 4.5]])  # 4 distributions
  ```

  ```python
  # With broadcasting:
  u1 = Uniform(low=3.0, high=[5.0, 6.0, 7.0])  # 3 distributions
  ```

  """
    def __init__(self, low: float = 0.0, high: float = 1.0, validate_args: bool = False, allow_nan_stats: bool = True, name: str = 'Uniform') -> None:
        '''Initialize a batch of Uniform distributions.

    Args:
      low: Floating point tensor, lower boundary of the output interval. Must
        have `low < high`.
      high: Floating point tensor, upper boundary of the output interval. Must
        have `low < high`.
      validate_args: Python `bool`, default `False`. When `True` distribution
        parameters are checked for validity despite possibly degrading runtime
        performance. When `False` invalid inputs may silently render incorrect
        outputs.
      allow_nan_stats: Python `bool`, default `True`. When `True`, statistics
        (e.g., mean, mode, variance) use the value "`NaN`" to indicate the
        result is undefined. When `False`, an exception is raised if one or
        more of the statistic\'s batch members are undefined.
      name: Python `str` name prefixed to Ops created by this class.

    Raises:
      InvalidArgumentError: if `low >= high` and `validate_args=False`.
    '''
    @property
    def low(self):
        """Lower boundary of the output interval."""
    @property
    def high(self):
        """Upper boundary of the output interval."""
    def range(self, name: str = 'range'):
        """`high - low`."""
