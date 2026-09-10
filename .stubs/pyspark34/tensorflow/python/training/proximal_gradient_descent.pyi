from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import math_ops as math_ops
from tensorflow.python.training import optimizer as optimizer, training_ops as training_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

class ProximalGradientDescentOptimizer(optimizer.Optimizer):
    """Optimizer that implements the proximal gradient descent algorithm.

  References:
    Efficient Learning using Forward-Backward Splitting:
      [Duchi et al., 2009](http://papers.nips.cc/paper/3793-efficient-learning-using-forward-backward-splitting)
      ([pdf](http://papers.nips.cc/paper/3793-efficient-learning-using-forward-backward-splitting.pdf))
  """
    def __init__(self, learning_rate, l1_regularization_strength: float = 0.0, l2_regularization_strength: float = 0.0, use_locking: bool = False, name: str = 'ProximalGradientDescent') -> None:
        '''Construct a new proximal gradient descent optimizer.

    Args:
      learning_rate: A Tensor or a floating point value.  The learning
        rate to use.
      l1_regularization_strength: A float value, must be greater than or
        equal to zero.
      l2_regularization_strength: A float value, must be greater than or
        equal to zero.
      use_locking: If True use locks for update operations.
      name: Optional name prefix for the operations created when applying
        gradients. Defaults to "GradientDescent".
    '''
