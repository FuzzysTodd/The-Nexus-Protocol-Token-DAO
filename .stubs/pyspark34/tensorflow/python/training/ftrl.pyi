from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.training import optimizer as optimizer, training_ops as training_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

class FtrlOptimizer(optimizer.Optimizer):
    """Optimizer that implements the FTRL algorithm.

  This version has support for both online L2 (McMahan et al., 2013) and
  shrinkage-type L2, which is the addition of an L2 penalty
  to the loss function.

  References:
    Ad-click prediction:
      [McMahan et al., 2013](https://dl.acm.org/citation.cfm?id=2488200)
      ([pdf](https://dl.acm.org/ft_gateway.cfm?id=2488200&ftid=1388399&dwn=1&CFID=32233078&CFTOKEN=d60fe57a294c056a-CB75C374-F915-E7A6-1573FBBC7BF7D526))
  """
    def __init__(self, learning_rate, learning_rate_power: float = -0.5, initial_accumulator_value: float = 0.1, l1_regularization_strength: float = 0.0, l2_regularization_strength: float = 0.0, use_locking: bool = False, name: str = 'Ftrl', accum_name: Incomplete | None = None, linear_name: Incomplete | None = None, l2_shrinkage_regularization_strength: float = 0.0, beta: Incomplete | None = None) -> None:
        '''Construct a new FTRL optimizer.

    Args:
      learning_rate: A float value or a constant float `Tensor`.
      learning_rate_power: A float value, must be less or equal to zero.
        Controls how the learning rate decreases during training. Use zero for
        a fixed learning rate. See section 3.1 in (McMahan et al., 2013).
      initial_accumulator_value: The starting value for accumulators.
        Only zero or positive values are allowed.
      l1_regularization_strength: A float value, must be greater than or
        equal to zero.
      l2_regularization_strength: A float value, must be greater than or
        equal to zero.
      use_locking: If `True` use locks for update operations.
      name: Optional name prefix for the operations created when applying
        gradients.  Defaults to "Ftrl".
      accum_name: The suffix for the variable that keeps the gradient squared
        accumulator.  If not present, defaults to name.
      linear_name: The suffix for the variable that keeps the linear gradient
        accumulator.  If not present, defaults to name + "_1".
      l2_shrinkage_regularization_strength: A float value, must be greater than
        or equal to zero. This differs from L2 above in that the L2 above is a
        stabilization penalty, whereas this L2 shrinkage is a magnitude penalty.
        The FTRL formulation can be written as:
        w_{t+1} = argmin_w(\\hat{g}_{1:t}w + L1*||w||_1 + L2*||w||_2^2), where
        \\hat{g} = g + (2*L2_shrinkage*w), and g is the gradient of the loss
        function w.r.t. the weights w.
        Specifically, in the absence of L1 regularization, it is equivalent to
        the following update rule:
        w_{t+1} = w_t - lr_t / (beta + 2*L2*lr_t) * g_t -
                  2*L2_shrinkage*lr_t / (beta + 2*L2*lr_t) * w_t
        where lr_t is the learning rate at t.
        When input is sparse shrinkage will only happen on the active weights.
      beta: A float value; corresponds to the beta parameter in the paper.

    Raises:
      ValueError: If one of the arguments is invalid.

    References:
      Ad-click prediction:
        [McMahan et al., 2013](https://dl.acm.org/citation.cfm?id=2488200)
        ([pdf](https://dl.acm.org/ft_gateway.cfm?id=2488200&ftid=1388399&dwn=1&CFID=32233078&CFTOKEN=d60fe57a294c056a-CB75C374-F915-E7A6-1573FBBC7BF7D526))
    '''
