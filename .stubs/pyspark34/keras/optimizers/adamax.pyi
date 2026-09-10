from _typeshed import Incomplete
from keras.optimizers import optimizer as optimizer
from keras.saving.object_registration import register_keras_serializable as register_keras_serializable

class Adamax(optimizer.Optimizer):
    """Optimizer that implements the Adamax algorithm.

    Adamax, a variant of Adam based on the infinity norm, is a first-order
    gradient-based optimization method. Due to its capability of adjusting the
    learning rate based on data characteristics, it is suited to learn
    time-variant process, e.g., speech data with dynamically changed noise
    conditions. Default parameters follow those provided in the paper (see
    references below).

    Initialization:

    ```python
    m = 0  # Initialize initial 1st moment vector
    u = 0  # Initialize the exponentially weighted infinity norm
    t = 0  # Initialize timestep
    ```

    The update rule for parameter `w` with gradient `g` is described at the end
    of section 7.1 of the paper (see the referenece section):

    ```python
    t += 1
    m = beta1 * m + (1 - beta) * g
    u = max(beta2 * u, abs(g))
    current_lr = learning_rate / (1 - beta1 ** t)
    w = w - current_lr * m / (u + epsilon)
    ```

    Args:
      learning_rate: A `tf.Tensor`, floating point value, a schedule that is a
        `tf.keras.optimizers.schedules.LearningRateSchedule`, or a callable
        that takes no arguments and returns the actual value to use. The
        learning rate. Defaults to 0.001.
      beta_1: A float value or a constant float tensor. The exponential decay
        rate for the 1st moment estimates.
      beta_2: A float value or a constant float tensor. The exponential decay
        rate for the exponentially weighted infinity norm.
      epsilon: A small constant for numerical stability.
      {{base_optimizer_keyword_args}}

    Reference:
      - [Kingma et al., 2014](http://arxiv.org/abs/1412.6980)
    """
    beta_1: Incomplete
    beta_2: Incomplete
    epsilon: Incomplete
    def __init__(self, learning_rate: float = 0.001, beta_1: float = 0.9, beta_2: float = 0.999, epsilon: float = 1e-07, weight_decay: Incomplete | None = None, clipnorm: Incomplete | None = None, clipvalue: Incomplete | None = None, global_clipnorm: Incomplete | None = None, use_ema: bool = False, ema_momentum: float = 0.99, ema_overwrite_frequency: Incomplete | None = None, jit_compile: bool = True, name: str = 'Adamax', **kwargs) -> None: ...
    def build(self, var_list) -> None:
        """Initialize optimizer variables.

        Adamax optimizer has 2 types of variables: momentums (denoted as m),
        exponentially weighted infinity norm (denoted as u).

        Args:
          var_list: list of model variables to build Adamax variables on.
        """
    def update_step(self, gradient, variable) -> None:
        """Update step given gradient and the associated model variable."""
    def get_config(self): ...
