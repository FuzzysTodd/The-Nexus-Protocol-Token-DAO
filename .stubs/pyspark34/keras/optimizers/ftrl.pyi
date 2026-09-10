from _typeshed import Incomplete
from keras.optimizers import optimizer as optimizer
from keras.saving.object_registration import register_keras_serializable as register_keras_serializable

class Ftrl(optimizer.Optimizer):
    '''Optimizer that implements the FTRL algorithm.

    "Follow The Regularized Leader" (FTRL) is an optimization algorithm
    developed at Google for click-through rate prediction in the early 2010s. It
    is most suitable for shallow models with large and sparse feature spaces.
    The algorithm is described by
    [McMahan et al., 2013](https://research.google.com/pubs/archive/41159.pdf).
    The Keras version has support for both online L2 regularization
    (the L2 regularization described in the paper
    above) and shrinkage-type L2 regularization
    (which is the addition of an L2 penalty to the loss function).

    Initialization:

    ```python
    n = 0
    sigma = 0
    z = 0
    ```

    Update rule for one variable `w`:

    ```python
    prev_n = n
    n = n + g ** 2
    sigma = (n ** -lr_power - prev_n ** -lr_power) / lr
    z = z + g - sigma * w
    if abs(z) < lambda_1:
      w = 0
    else:
      w = (sgn(z) * lambda_1 - z) / ((beta + sqrt(n)) / alpha + lambda_2)
    ```

    Notation:

    - `lr` is the learning rate
    - `g` is the gradient for the variable
    - `lambda_1` is the L1 regularization strength
    - `lambda_2` is the L2 regularization strength
    - `lr_power` is the power to scale n.

    Check the documentation for the `l2_shrinkage_regularization_strength`
    parameter for more details when shrinkage is enabled, in which case gradient
    is replaced with a gradient with shrinkage.

    Args:
      learning_rate: A `Tensor`, floating point value, a schedule that is a
        `tf.keras.optimizers.schedules.LearningRateSchedule`, or a callable that
        takes no arguments and returns the actual value to use. The learning
        rate.  Defaults to 0.001.
      learning_rate_power: A float value, must be less or equal to zero.
        Controls how the learning rate decreases during training. Use zero for a
        fixed learning rate.
      initial_accumulator_value: The starting value for accumulators. Only zero
        or positive values are allowed.
      l1_regularization_strength: A float value, must be greater than or equal
        to zero. Defaults to 0.0.
      l2_regularization_strength: A float value, must be greater than or equal
        to zero. Defaults to 0.0.
      l2_shrinkage_regularization_strength: A float value, must be greater than
        or equal to zero. This differs from L2 above in that the L2 above is a
        stabilization penalty, whereas this L2 shrinkage is a magnitude penalty.
        When input is sparse shrinkage will only happen on the active weights.
      beta: A float value, representing the beta value from the paper. Defaults
        to 0.0.
      {{base_optimizer_keyword_args}}
    '''
    learning_rate_power: Incomplete
    initial_accumulator_value: Incomplete
    l1_regularization_strength: Incomplete
    l2_regularization_strength: Incomplete
    l2_shrinkage_regularization_strength: Incomplete
    beta: Incomplete
    def __init__(self, learning_rate: float = 0.001, learning_rate_power: float = -0.5, initial_accumulator_value: float = 0.1, l1_regularization_strength: float = 0.0, l2_regularization_strength: float = 0.0, l2_shrinkage_regularization_strength: float = 0.0, beta: float = 0.0, weight_decay: Incomplete | None = None, clipnorm: Incomplete | None = None, clipvalue: Incomplete | None = None, global_clipnorm: Incomplete | None = None, use_ema: bool = False, ema_momentum: float = 0.99, ema_overwrite_frequency: Incomplete | None = None, jit_compile: bool = True, name: str = 'Ftrl', **kwargs) -> None: ...
    def build(self, var_list) -> None:
        """Initialize optimizer variables.

        Args:
          var_list: list of model variables to build Ftrl variables on.
        """
    def update_step(self, gradient, variable) -> None:
        """Update step given gradient and the associated model variable."""
    def get_config(self): ...
