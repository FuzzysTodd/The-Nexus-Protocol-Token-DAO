from tensorflow.python.framework import indexed_slices as indexed_slices, ops as ops
from tensorflow.python.ops import math_ops as math_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.training import optimizer as optimizer, training_ops as training_ops
from tensorflow.python.util.tf_export import tf_export as tf_export

class GradientDescentOptimizer(optimizer.Optimizer):
    """Optimizer that implements the gradient descent algorithm.
  """
    def __init__(self, learning_rate, use_locking: bool = False, name: str = 'GradientDescent') -> None:
        '''Construct a new gradient descent optimizer.

    Args:
      learning_rate: A Tensor or a floating point value.  The learning
        rate to use.
      use_locking: If True use locks for update operations.
      name: Optional name prefix for the operations created when applying
        gradients. Defaults to "GradientDescent".

    @compatibility(eager)
    When eager execution is enabled, `learning_rate` can be a callable that
    takes no arguments and returns the actual value to use. This can be useful
    for changing these values across different invocations of optimizer
    functions.
    @end_compatibility
    '''
