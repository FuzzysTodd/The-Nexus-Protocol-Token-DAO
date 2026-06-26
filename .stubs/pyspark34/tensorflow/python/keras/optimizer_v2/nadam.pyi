from _typeshed import Incomplete
from tensorflow.python.framework import ops as ops
from tensorflow.python.keras import backend_config as backend_config
from tensorflow.python.keras.optimizer_v2 import learning_rate_schedule as learning_rate_schedule, optimizer_v2 as optimizer_v2
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, state_ops as state_ops
from tensorflow.python.util.tf_export import keras_export as keras_export

class Nadam(optimizer_v2.OptimizerV2):
    '''Optimizer that implements the NAdam algorithm.
  Much like Adam is essentially RMSprop with momentum, Nadam is Adam with
  Nesterov momentum.

  Args:
    learning_rate: A Tensor or a floating point value.  The learning rate.
    beta_1: A float value or a constant float tensor. The exponential decay
      rate for the 1st moment estimates.
    beta_2: A float value or a constant float tensor. The exponential decay
      rate for the exponentially weighted infinity norm.
    epsilon: A small constant for numerical stability.
    name: Optional name for the operations created when applying gradients.
      Defaults to `"Nadam"`.
    **kwargs: Keyword arguments. Allowed to be one of
      `"clipnorm"` or `"clipvalue"`.
      `"clipnorm"` (float) clips gradients by norm; `"clipvalue"` (float) clips
      gradients by value.

  Usage Example:
    >>> opt = tf.keras.optimizers.Nadam(learning_rate=0.2)
    >>> var1 = tf.Variable(10.0)
    >>> loss = lambda: (var1 ** 2) / 2.0
    >>> step_count = opt.minimize(loss, [var1]).numpy()
    >>> "{:.1f}".format(var1.numpy())
    9.8

  Reference:
    - [Dozat, 2015](http://cs229.stanford.edu/proj2015/054_report.pdf).
  '''
    epsilon: Incomplete
    def __init__(self, learning_rate: float = 0.001, beta_1: float = 0.9, beta_2: float = 0.999, epsilon: float = 1e-07, name: str = 'Nadam', **kwargs) -> None: ...
    def get_config(self): ...
