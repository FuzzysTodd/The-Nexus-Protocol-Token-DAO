from _typeshed import Incomplete
from keras.optimizers import optimizer as optimizer
from keras.saving.object_registration import register_keras_serializable as register_keras_serializable

class Adam(optimizer.Optimizer):
    '''Optimizer that implements the Adam algorithm.

    Adam optimization is a stochastic gradient descent method that is based on
    adaptive estimation of first-order and second-order moments.

    According to
    [Kingma et al., 2014](http://arxiv.org/abs/1412.6980),
    the method is "*computationally
    efficient, has little memory requirement, invariant to diagonal rescaling of
    gradients, and is well suited for problems that are large in terms of
    data/parameters*".

    Args:
      learning_rate: A `tf.Tensor`, floating point value, a schedule that is a
        `tf.keras.optimizers.schedules.LearningRateSchedule`, or a callable
        that takes no arguments and returns the actual value to use. The
        learning rate. Defaults to 0.001.
      beta_1: A float value or a constant float tensor, or a callable
        that takes no arguments and returns the actual value to use. The
        exponential decay rate for the 1st moment estimates. Defaults to 0.9.
      beta_2: A float value or a constant float tensor, or a callable
        that takes no arguments and returns the actual value to use. The
        exponential decay rate for the 2nd moment estimates. Defaults to 0.999.
      epsilon: A small constant for numerical stability. This epsilon is
        "epsilon hat" in the Kingma and Ba paper (in the formula just before
        Section 2.1), not the epsilon in Algorithm 1 of the paper. Defaults to
        1e-7.
      amsgrad: Boolean. Whether to apply AMSGrad variant of this algorithm from
        the paper "On the Convergence of Adam and beyond". Defaults to `False`.
      {{base_optimizer_keyword_args}}

    Reference:
      - [Kingma et al., 2014](http://arxiv.org/abs/1412.6980)
      - [Reddi et al., 2018](
          https://openreview.net/pdf?id=ryQu7f-RZ) for `amsgrad`.

    Notes:

    The default value of 1e-7 for epsilon might not be a good default in
    general. For example, when training an Inception network on ImageNet a
    current good choice is 1.0 or 0.1. Note that since Adam uses the
    formulation just before Section 2.1 of the Kingma and Ba paper rather than
    the formulation in Algorithm 1, the "epsilon" referred to here is "epsilon
    hat" in the paper.

    The sparse implementation of this algorithm (used when the gradient is an
    IndexedSlices object, typically because of `tf.gather` or an embedding
    lookup in the forward pass) does apply momentum to variable slices even if
    they were not used in the forward pass (meaning they have a gradient equal
    to zero). Momentum decay (beta1) is also applied to the entire momentum
    accumulator. This means that the sparse behavior is equivalent to the dense
    behavior (in contrast to some momentum implementations which ignore momentum
    unless a variable slice was actually used).
    '''
    beta_1: Incomplete
    beta_2: Incomplete
    epsilon: Incomplete
    amsgrad: Incomplete
    def __init__(self, learning_rate: float = 0.001, beta_1: float = 0.9, beta_2: float = 0.999, epsilon: float = 1e-07, amsgrad: bool = False, weight_decay: Incomplete | None = None, clipnorm: Incomplete | None = None, clipvalue: Incomplete | None = None, global_clipnorm: Incomplete | None = None, use_ema: bool = False, ema_momentum: float = 0.99, ema_overwrite_frequency: Incomplete | None = None, jit_compile: bool = True, name: str = 'Adam', **kwargs) -> None: ...
    def build(self, var_list) -> None:
        """Initialize optimizer variables.

        Adam optimizer has 3 types of variables: momentums, velocities and
        velocity_hat (only set when amsgrad is applied),

        Args:
          var_list: list of model variables to build Adam variables on.
        """
    def update_step(self, gradient, variable) -> None:
        """Update step given gradient and the associated model variable."""
    def get_config(self): ...
