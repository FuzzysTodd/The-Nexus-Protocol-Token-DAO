from _typeshed import Incomplete
from keras.optimizers.legacy import optimizer_v2 as optimizer_v2

class SGD(optimizer_v2.OptimizerV2):
    '''Gradient descent (with momentum) optimizer.

    Update rule for parameter `w` with gradient `g` when `momentum=0`:

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
        learning rate. Defaults to 0.01.
      momentum: float hyperparameter >= 0 that accelerates gradient descent in
        the relevant direction and dampens oscillations. Defaults to 0, i.e.,
        vanilla gradient descent.
      nesterov: boolean. Whether to apply Nesterov momentum.
        Defaults to `False`.
      name: Optional name prefix for the operations created when applying
        gradients.  Defaults to `"SGD"`.
      **kwargs: keyword arguments. Allowed arguments are `clipvalue`,
        `clipnorm`, `global_clipnorm`.
        If `clipvalue` (float) is set, the gradient of each weight
        is clipped to be no higher than this value.
        If `clipnorm` (float) is set, the gradient of each weight
        is individually clipped so that its norm is no higher than this value.
        If `global_clipnorm` (float) is set the gradient of all weights is
        clipped so that their global norm is no higher than this value.

    Usage:

    >>> opt = tf.keras.optimizers.legacy.SGD(learning_rate=0.1)
    >>> var = tf.Variable(1.0)
    >>> loss = lambda: (var ** 2)/2.0         # d(loss)/d(var1) = var1
    >>> step_count = opt.minimize(loss, [var]).numpy()
    >>> # Step is `- learning_rate * grad`
    >>> var.numpy()
    0.9

    >>> opt = tf.keras.optimizers.legacy.SGD(learning_rate=0.1, momentum=0.9)
    >>> var = tf.Variable(1.0)
    >>> val0 = var.value()
    >>> loss = lambda: (var ** 2)/2.0         # d(loss)/d(var1) = var1
    >>> # First step is `- learning_rate * grad`
    >>> step_count = opt.minimize(loss, [var]).numpy()
    >>> val1 = var.value()
    >>> (val0 - val1).numpy()
    0.1
    >>> # On later steps, step-size increases because of momentum
    >>> step_count = opt.minimize(loss, [var]).numpy()
    >>> val2 = var.value()
    >>> (val1 - val2).numpy()
    0.18

    Reference:
        - For `nesterov=True`, See [Sutskever et al., 2013](
          https://github.com/mlresearch/v28/blob/gh-pages/sutskever13.pdf).
    '''
    nesterov: Incomplete
    def __init__(self, learning_rate: float = 0.01, momentum: float = 0.0, nesterov: bool = False, name: str = 'SGD', **kwargs) -> None: ...
    def get_config(self): ...
