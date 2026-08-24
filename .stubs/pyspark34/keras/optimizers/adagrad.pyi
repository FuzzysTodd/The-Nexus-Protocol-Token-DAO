from _typeshed import Incomplete
from keras import initializers as initializers
from keras.optimizers import optimizer as optimizer
from keras.saving.object_registration import register_keras_serializable as register_keras_serializable

class Adagrad(optimizer.Optimizer):
    """Optimizer that implements the Adagrad algorithm.

    Adagrad is an optimizer with parameter-specific learning rates,
    which are adapted relative to how frequently a parameter gets
    updated during training. The more updates a parameter receives,
    the smaller the updates.

    Args:
      learning_rate: Initial value for the learning rate:
        either a floating point value,
        or a `tf.keras.optimizers.schedules.LearningRateSchedule` instance.
        Defaults to 0.001.
        Note that `Adagrad` tends to benefit from higher initial learning rate
        values compared to other optimizers.
        To match the exact form in the original paper, use 1.0.
      initial_accumulator_value: Floating point value.
        Starting value for the accumulators (per-parameter momentum values).
        Must be non-negative.
      epsilon: Small floating point value used to maintain numerical stability.
      {{base_optimizer_keyword_args}}

    Reference:
      - [Duchi et al., 2011](
        http://www.jmlr.org/papers/volume12/duchi11a/duchi11a.pdf).
    """
    initial_accumulator_value: Incomplete
    epsilon: Incomplete
    def __init__(self, learning_rate: float = 0.001, initial_accumulator_value: float = 0.1, epsilon: float = 1e-07, weight_decay: Incomplete | None = None, clipnorm: Incomplete | None = None, clipvalue: Incomplete | None = None, global_clipnorm: Incomplete | None = None, use_ema: bool = False, ema_momentum: float = 0.99, ema_overwrite_frequency: Incomplete | None = None, jit_compile: bool = True, name: str = 'Adagrad', **kwargs) -> None: ...
    def build(self, var_list) -> None: ...
    def update_step(self, grad, variable) -> None:
        """Update step given gradient and the associated model variable."""
    def get_config(self): ...
