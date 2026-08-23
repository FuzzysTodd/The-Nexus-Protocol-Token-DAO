from tensorflow.python.framework import constant_op as constant_op, ops as ops
from tensorflow.python.ops import array_ops as array_ops, math_ops as math_ops
from tensorflow.python.training import optimizer as optimizer, training_ops as training_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

class AdagradDAOptimizer(optimizer.Optimizer):
    """Adagrad Dual Averaging algorithm for sparse linear models.

  This optimizer takes care of regularization of unseen features in a mini batch
  by updating them when they are seen with a closed form update rule that is
  equivalent to having updated them on every mini-batch.

  AdagradDA is typically used when there is a need for large sparsity in the
  trained model. This optimizer only guarantees sparsity for linear models. Be
  careful when using AdagradDA for deep networks as it will require careful
  initialization of the gradient accumulators for it to train.

  References:
    Adaptive Subgradient Methods for Online Learning and Stochastic Optimization
      :[Duchi et al., 2011](http://jmlr.org/papers/v12/duchi11a.html)
      ([pdf](http://www.jmlr.org/papers/volume12/duchi11a/duchi11a.pdf))
  """
    def __init__(self, learning_rate, global_step, initial_gradient_squared_accumulator_value: float = 0.1, l1_regularization_strength: float = 0.0, l2_regularization_strength: float = 0.0, use_locking: bool = False, name: str = 'AdagradDA') -> None:
        '''Construct a new AdagradDA optimizer.

    Args:
      learning_rate: A `Tensor` or a floating point value.  The learning rate.
      global_step: A `Tensor` containing the current training step number.
      initial_gradient_squared_accumulator_value: A floating point value.
        Starting value for the accumulators, must be positive.
      l1_regularization_strength: A float value, must be greater than or
        equal to zero.
      l2_regularization_strength: A float value, must be greater than or
        equal to zero.
      use_locking: If `True` use locks for update operations.
      name: Optional name prefix for the operations created when applying
        gradients.  Defaults to "AdagradDA".

    Raises:
      ValueError: If the `initial_gradient_squared_accumulator_value` is
      invalid.
    '''
