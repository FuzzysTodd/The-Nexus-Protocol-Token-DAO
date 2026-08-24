from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops, nn as nn, random_ops as random_ops
from tensorflow.python.ops.distributions import distribution as distribution, kullback_leibler as kullback_leibler
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

class Bernoulli(distribution.Distribution):
    """Bernoulli distribution.

  The Bernoulli distribution with `probs` parameter, i.e., the probability of a
  `1` outcome (vs a `0` outcome).
  """
    def __init__(self, logits: Incomplete | None = None, probs: Incomplete | None = None, dtype=..., validate_args: bool = False, allow_nan_stats: bool = True, name: str = 'Bernoulli') -> None:
        '''Construct Bernoulli distributions.

    Args:
      logits: An N-D `Tensor` representing the log-odds of a `1` event. Each
        entry in the `Tensor` parametrizes an independent Bernoulli distribution
        where the probability of an event is sigmoid(logits). Only one of
        `logits` or `probs` should be passed in.
      probs: An N-D `Tensor` representing the probability of a `1`
        event. Each entry in the `Tensor` parameterizes an independent
        Bernoulli distribution. Only one of `logits` or `probs` should be passed
        in.
      dtype: The type of the event samples. Default: `int32`.
      validate_args: Python `bool`, default `False`. When `True` distribution
        parameters are checked for validity despite possibly degrading runtime
        performance. When `False` invalid inputs may silently render incorrect
        outputs.
      allow_nan_stats: Python `bool`, default `True`. When `True`,
        statistics (e.g., mean, mode, variance) use the value "`NaN`" to
        indicate the result is undefined. When `False`, an exception is raised
        if one or more of the statistic\'s batch members are undefined.
      name: Python `str` name prefixed to Ops created by this class.

    Raises:
      ValueError: If p and logits are passed, or if neither are passed.
    '''
    @property
    def logits(self):
        """Log-odds of a `1` outcome (vs `0`)."""
    @property
    def probs(self):
        """Probability of a `1` outcome (vs `0`)."""
