from _typeshed import Incomplete
from keras.optimizers import optimizer as optimizer
from keras.saving.object_registration import register_keras_serializable as register_keras_serializable

class Adadelta(optimizer.Optimizer):
    """Optimizer that implements the Adadelta algorithm.

    Adadelta optimization is a stochastic gradient descent method that is based
    on adaptive learning rate per dimension to address two drawbacks:

    - The continual decay of learning rates throughout training.
    - The need for a manually selected global learning rate.

    Adadelta is a more robust extension of Adagrad that adapts learning rates
    based on a moving window of gradient updates, instead of accumulating all
    past gradients. This way, Adadelta continues learning even when many updates
    have been done. Compared to Adagrad, in the original version of Adadelta you
    don't have to set an initial learning rate. In this version, the initial
    learning rate can be set, as in most other Keras optimizers.

    Args:
      learning_rate: Initial value for the learning rate: either a floating
        point value, or a `tf.keras.optimizers.schedules.LearningRateSchedule`
        instance. Defaults to 0.001. Note that `Adadelta` tends to benefit from
        higher initial learning rate values compared to other optimizers. To
        match the exact form in the original paper, use 1.0.
      rho: A `Tensor` or a floating point value. The decay rate. Defaults to
        0.95.
      epsilon: Small floating point value used to maintain numerical stability.
        Defaults to 1e-7.
      {{base_optimizer_keyword_args}}

    Reference:
      - [Zeiler, 2012](http://arxiv.org/abs/1212.5701)
    """
    rho: Incomplete
    epsilon: Incomplete
    def __init__(self, learning_rate: float = 0.001, rho: float = 0.95, epsilon: float = 1e-07, weight_decay: Incomplete | None = None, clipnorm: Incomplete | None = None, clipvalue: Incomplete | None = None, global_clipnorm: Incomplete | None = None, use_ema: bool = False, ema_momentum: float = 0.99, ema_overwrite_frequency: Incomplete | None = None, jit_compile: bool = True, name: str = 'Adadelta', **kwargs) -> None: ...
    def build(self, var_list) -> None: ...
    def update_step(self, grad, variable):
        """Update step given gradient and the associated model variable."""
    def get_config(self): ...
