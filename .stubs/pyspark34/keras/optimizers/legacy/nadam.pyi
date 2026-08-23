from _typeshed import Incomplete
from keras import backend_config as backend_config
from keras.optimizers.legacy import optimizer_v2 as optimizer_v2
from keras.optimizers.schedules import learning_rate_schedule as learning_rate_schedule

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
      **kwargs: keyword arguments. Allowed arguments are `clipvalue`,
        `clipnorm`, `global_clipnorm`.
        If `clipvalue` (float) is set, the gradient of each weight
        is clipped to be no higher than this value.
        If `clipnorm` (float) is set, the gradient of each weight
        is individually clipped so that its norm is no higher than this value.
        If `global_clipnorm` (float) is set the gradient of all weights is
        clipped so that their global norm is no higher than this value.

    Usage Example:
      >>> opt = tf.keras.optimizers.legacy.Nadam(learning_rate=0.2)
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
