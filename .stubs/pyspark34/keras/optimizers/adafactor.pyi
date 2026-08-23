from _typeshed import Incomplete
from keras.optimizers import optimizer as optimizer
from keras.optimizers.schedules import learning_rate_schedule as learning_rate_schedule
from keras.saving.object_registration import register_keras_serializable as register_keras_serializable

class Adafactor(optimizer.Optimizer):
    """Optimizer that implements the Adafactor algorithm.

    Adafactor is commonly used in NLP tasks, and has the advantage
    of taking less memory because it only saves partial information of previous
    gradients.

    The default argument setup is based on the original paper (see reference).
    When gradients are of dimension > 2, Adafactor optimizer will delete the
    last 2 dimensions separately in its accumulator variables.

    Args:
      learning_rate: Initial value for the learning rate:
        either a floating point value,
        or a `tf.keras.optimizers.schedules.LearningRateSchedule` instance.
        Defaults to 0.001.
      beta_2_decay: float, defaults to -0.8. The decay rate of `beta_2`.
      epsilon_1: float, defaults to 1e-30. A small offset to keep demoninator
        away from 0.
      epsilon_2: float, defaults to 1e-3. A small offset to avoid learning
        rate becoming too small by time.
      clip_threshold: float, defaults to 1.0. Clipping threshold. This is a part
        of Adafactor algorithm, independent from `clipnorm`, `clipvalue` and
        `global_clipnorm`.
      relative_step: bool, defaults to True. If `learning_rate` is a
        constant and `relative_step=True`, learning rate will be adjusted
        based on current iterations. This is a default learning rate decay
        in Adafactor.
      {{base_optimizer_keyword_args}}

    Reference:
      - [Shazeer, Noam et al., 2018](https://arxiv.org/abs/1804.04235).

    """
    beta_2_decay: Incomplete
    epsilon_1: Incomplete
    epsilon_2: Incomplete
    clip_threshold: Incomplete
    relative_step: Incomplete
    def __init__(self, learning_rate: float = 0.001, beta_2_decay: float = -0.8, epsilon_1: float = 1e-30, epsilon_2: float = 0.001, clip_threshold: float = 1.0, relative_step: bool = True, weight_decay: Incomplete | None = None, clipnorm: Incomplete | None = None, clipvalue: Incomplete | None = None, global_clipnorm: Incomplete | None = None, use_ema: bool = False, ema_momentum: float = 0.99, ema_overwrite_frequency: Incomplete | None = None, jit_compile: bool = True, name: str = 'Adafactor', **kwargs) -> None: ...
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
