from _typeshed import Incomplete
from keras import backend_config as backend_config
from keras.optimizers.legacy import optimizer_v2 as optimizer_v2

class Adamax(optimizer_v2.OptimizerV2):
    '''Optimizer that implements the Adamax algorithm.

    It is a variant of Adam based on the infinity norm.
    Default parameters follow those provided in the paper.
    Adamax is sometimes superior to adam, specially in models with embeddings.

    Initialization:

    ```python
    m = 0  # Initialize initial 1st moment vector
    v = 0  # Initialize the exponentially weighted infinity norm
    t = 0  # Initialize timestep
    ```

    The update rule for parameter `w` with gradient `g` is
    described at the end of section 7.1 of the paper:

    ```python
    t += 1
    m = beta1 * m + (1 - beta) * g
    v = max(beta2 * v, abs(g))
    current_lr = learning_rate / (1 - beta1 ** t)
    w = w - current_lr * m / (v + epsilon)
    ```

    Similarly to `Adam`, the epsilon is added for numerical stability
    (especially to get rid of division by zero when `v_t == 0`).

    In contrast to `Adam`, the sparse implementation of this algorithm
    (used when the gradient is an IndexedSlices object, typically because of
    `tf.gather` or an embedding lookup in the forward pass) only updates
    variable slices and corresponding `m_t`, `v_t` terms when that part of
    the variable was used in the forward pass. This means that the sparse
    behavior is contrast to the dense behavior (similar to some momentum
    implementations which ignore momentum unless a variable slice was actually
    used).

    Args:
      learning_rate: A `Tensor`, floating point value, or a schedule that is a
        `tf.keras.optimizers.schedules.LearningRateSchedule`. The learning rate.
      beta_1: A float value or a constant float tensor. The exponential decay
        rate for the 1st moment estimates.
      beta_2: A float value or a constant float tensor. The exponential decay
        rate for the exponentially weighted infinity norm.
      epsilon: A small constant for numerical stability.
      name: Optional name for the operations created when applying gradients.
        Defaults to `"Adamax"`.
      **kwargs: keyword arguments. Allowed arguments are `clipvalue`,
        `clipnorm`, `global_clipnorm`.
        If `clipvalue` (float) is set, the gradient of each weight
        is clipped to be no higher than this value.
        If `clipnorm` (float) is set, the gradient of each weight
        is individually clipped so that its norm is no higher than this value.
        If `global_clipnorm` (float) is set the gradient of all weights is
        clipped so that their global norm is no higher than this value.

    Reference:
      - [Kingma et al., 2014](http://arxiv.org/abs/1412.6980)
    '''
    epsilon: Incomplete
    def __init__(self, learning_rate: float = 0.001, beta_1: float = 0.9, beta_2: float = 0.999, epsilon: float = 1e-07, name: str = 'Adamax', **kwargs) -> None: ...
    def get_config(self): ...
