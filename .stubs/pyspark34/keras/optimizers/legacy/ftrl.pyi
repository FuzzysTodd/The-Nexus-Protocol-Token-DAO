from keras.optimizers.legacy import optimizer_v2 as optimizer_v2

class Ftrl(optimizer_v2.OptimizerV2):
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
    sigma = (sqrt(n) - sqrt(prev_n)) / lr
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

    Check the documentation for the `l2_shrinkage_regularization_strength`
    parameter for more details when shrinkage is enabled, in which case gradient
    is replaced with a gradient with shrinkage.

    Args:
      learning_rate: A `Tensor`, floating point value, or a schedule that is a
        `tf.keras.optimizers.schedules.LearningRateSchedule`. The learning rate.
      learning_rate_power: A float value, must be less or equal to zero.
        Controls how the learning rate decreases during training. Use zero for
        a fixed learning rate.
      initial_accumulator_value: The starting value for accumulators.
        Only zero or positive values are allowed.
      l1_regularization_strength: A float value, must be greater than or
        equal to zero. Defaults to 0.0.
      l2_regularization_strength: A float value, must be greater than or
        equal to zero. Defaults to 0.0.
      name: Optional name prefix for the operations created when applying
        gradients.  Defaults to `"Ftrl"`.
      l2_shrinkage_regularization_strength: A float value, must be greater than
        or equal to zero. This differs from L2 above in that the L2 above is a
        stabilization penalty, whereas this L2 shrinkage is a magnitude penalty.
        When input is sparse shrinkage will only happen on the active weights.
      beta: A float value, representing the beta value from the paper.
        Defaults to 0.0.
      **kwargs: keyword arguments. Allowed arguments are `clipvalue`,
        `clipnorm`, `global_clipnorm`.
        If `clipvalue` (float) is set, the gradient of each weight
        is clipped to be no higher than this value.
        If `clipnorm` (float) is set, the gradient of each weight
        is individually clipped so that its norm is no higher than this value.
        If `global_clipnorm` (float) is set the gradient of all weights is
        clipped so that their global norm is no higher than this value.

    Reference:
      - [McMahan et al., 2013](
        https://research.google.com/pubs/archive/41159.pdf)
    '''
    def __init__(self, learning_rate: float = 0.001, learning_rate_power: float = -0.5, initial_accumulator_value: float = 0.1, l1_regularization_strength: float = 0.0, l2_regularization_strength: float = 0.0, name: str = 'Ftrl', l2_shrinkage_regularization_strength: float = 0.0, beta: float = 0.0, **kwargs) -> None: ...
    def get_config(self): ...
