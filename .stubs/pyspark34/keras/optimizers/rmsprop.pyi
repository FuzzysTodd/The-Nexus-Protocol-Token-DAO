from _typeshed import Incomplete
from keras.optimizers import optimizer as optimizer
from keras.saving.object_registration import register_keras_serializable as register_keras_serializable

class RMSprop(optimizer.Optimizer):
    '''Optimizer that implements the RMSprop algorithm.

    The gist of RMSprop is to:

    - Maintain a moving (discounted) average of the square of gradients
    - Divide the gradient by the root of this average

    This implementation of RMSprop uses plain momentum, not Nesterov momentum.

    The centered version additionally maintains a moving average of the
    gradients, and uses that average to estimate the variance.

    Args:
      learning_rate: Initial value for the learning rate:
        either a floating point value,
        or a `tf.keras.optimizers.schedules.LearningRateSchedule` instance.
        Defaults to 0.001.
      rho: float, defaults to 0.9. Discounting factor for the old gradients.
      momentum: float, defaults to 0.0. If not 0.0., the optimizer tracks the
        momentum value, with a decay rate equals to `1 - momentum`.
      epsilon: A small constant for numerical stability. This epsilon is
        "epsilon hat" in the Kingma and Ba paper (in the formula just before
        Section 2.1), not the epsilon in Algorithm 1 of the paper. Defaults to
        1e-7.
      centered: Boolean. If `True`, gradients are normalized by the estimated
        variance of the gradient; if False, by the uncentered second moment.
        Setting this to `True` may help with training, but is slightly more
        expensive in terms of computation and memory. Defaults to `False`.
      {{base_optimizer_keyword_args}}

    Usage:

    >>> opt = tf.keras.optimizers.experimental.RMSprop(learning_rate=0.1)
    >>> var1 = tf.Variable(10.0)
    >>> loss = lambda: (var1 ** 2) / 2.0  # d(loss) / d(var1) = var1
    >>> opt.minimize(loss, [var1])
    >>> var1.numpy()
    9.683772

    Reference:
      - [Hinton, 2012](
        http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf)
    '''
    rho: Incomplete
    momentum: Incomplete
    epsilon: Incomplete
    centered: Incomplete
    def __init__(self, learning_rate: float = 0.001, rho: float = 0.9, momentum: float = 0.0, epsilon: float = 1e-07, centered: bool = False, weight_decay: Incomplete | None = None, clipnorm: Incomplete | None = None, clipvalue: Incomplete | None = None, global_clipnorm: Incomplete | None = None, use_ema: bool = False, ema_momentum: float = 0.99, ema_overwrite_frequency: int = 100, jit_compile: bool = True, name: str = 'RMSprop', **kwargs) -> None: ...
    def build(self, var_list) -> None: ...
    def update_step(self, gradient, variable) -> None:
        """Update step given gradient and the associated model variable."""
    def get_config(self): ...
