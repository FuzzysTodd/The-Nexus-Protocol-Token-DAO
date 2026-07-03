from _typeshed import Incomplete
from keras.optimizers import optimizer as optimizer
from keras.saving.object_registration import register_keras_serializable as register_keras_serializable

class SGD(optimizer.Optimizer):
    """Gradient descent (with momentum) optimizer.

    Update rule for parameter `w` with gradient `g` when `momentum` is 0:

    ```python
    w = w - learning_rate * g
    ```

    Update rule when `momentum` is larger than 0:

    ```python
    velocity = momentum * velocity - learning_rate * g
    w = w + velocity
    ```

    When `nesterov=True`, this rule becomes:

    ```python
    velocity = momentum * velocity - learning_rate * g
    w = w + momentum * velocity - learning_rate * g
    ```

    Args:
      learning_rate: A `Tensor`, floating point value, or a schedule that is a
        `tf.keras.optimizers.schedules.LearningRateSchedule`, or a callable
        that takes no arguments and returns the actual value to use. The
        learning rate. Defaults to 0.001.
      momentum: float hyperparameter >= 0 that accelerates gradient descent in
        the relevant direction and dampens oscillations. Defaults to 0, i.e.,
        vanilla gradient descent.
      nesterov: boolean. Whether to apply Nesterov momentum.
        Defaults to `False`.
      {{base_optimizer_keyword_args}}

    Usage:

    >>> opt = tf.keras.optimizers.experimental.SGD(learning_rate=0.1)
    >>> var = tf.Variable(1.0)
    >>> loss = lambda: (var ** 2)/2.0         # d(loss)/d(var1) = var1
    >>> opt.minimize(loss, [var])
    >>> # Step is `- learning_rate * grad`
    >>> var.numpy()
    0.9

    >>> opt = tf.keras.optimizers.experimental.SGD(0.1, momentum=0.9)
    >>> var = tf.Variable(1.0)
    >>> val0 = var.value()
    >>> loss = lambda: (var ** 2)/2.0         # d(loss)/d(var1) = var1
    >>> # First step is `- learning_rate * grad`
    >>> opt.minimize(loss, [var])
    >>> val1 = var.value()
    >>> (val0 - val1).numpy()
    0.1
    >>> # On later steps, step-size increases because of momentum
    >>> opt.minimize(loss, [var])
    >>> val2 = var.value()
    >>> (val1 - val2).numpy()
    0.18

    Reference:
        - For `nesterov=True`, See [Sutskever et al., 2013](
          http://proceedings.mlr.press/v28/sutskever13.pdf).
    """
    momentum: Incomplete
    nesterov: Incomplete
    def __init__(self, learning_rate: float = 0.01, momentum: float = 0.0, nesterov: bool = False, weight_decay: Incomplete | None = None, clipnorm: Incomplete | None = None, clipvalue: Incomplete | None = None, global_clipnorm: Incomplete | None = None, use_ema: bool = False, ema_momentum: float = 0.99, ema_overwrite_frequency: Incomplete | None = None, jit_compile: bool = True, name: str = 'SGD', **kwargs) -> None: ...
    momentums: Incomplete
    def build(self, var_list) -> None:
        """Initialize optimizer variables.

        SGD optimizer has one variable `momentums`, only set if `self.momentum`
        is not 0.

        Args:
          var_list: list of model variables to build SGD variables on.
        """
    def update_step(self, gradient, variable) -> None:
        """Update step given gradient and the associated model variable."""
    def get_config(self): ...
