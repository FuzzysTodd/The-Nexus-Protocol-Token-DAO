from _typeshed import Incomplete
from keras import backend_config as backend_config
from keras.optimizers.legacy import optimizer_v2 as optimizer_v2

class Adadelta(optimizer_v2.OptimizerV2):
    '''Optimizer that implements the Adadelta algorithm.

    Adadelta optimization is a stochastic gradient descent method that is based
    on adaptive learning rate per dimension to address two drawbacks:

    - The continual decay of learning rates throughout training.
    - The need for a manually selected global learning rate.

    Adadelta is a more robust extension of Adagrad that adapts learning rates
    based on a moving window of gradient updates, instead of accumulating all
    past gradients. This way, Adadelta continues learning even when many updates
    have been done. Compared to Adagrad, in the original version of Adadelta you
    don\'t have to set an initial learning rate. In this version, the initial
    learning rate can be set, as in most other Keras optimizers.

    Args:
      learning_rate: Initial value for the learning rate:
        either a floating point value,
        or a `tf.keras.optimizers.schedules.LearningRateSchedule` instance.
        Defaults to 0.001.
        Note that `Adadelta` tends to benefit from higher initial learning rate
        values compared to other optimizers.
        To match the exact form in the original paper, use 1.0.
      rho: A `Tensor` or a floating point value. The decay rate.
      epsilon: Small floating point value used to maintain numerical stability.
      name: Optional name prefix for the operations created when applying
        gradients.  Defaults to `"Adadelta"`.
      **kwargs: keyword arguments. Allowed arguments are `clipvalue`,
        `clipnorm`, `global_clipnorm`.
        If `clipvalue` (float) is set, the gradient of each weight
        is clipped to be no higher than this value.
        If `clipnorm` (float) is set, the gradient of each weight
        is individually clipped so that its norm is no higher than this value.
        If `global_clipnorm` (float) is set the gradient of all weights is
        clipped so that their global norm is no higher than this value.

    Reference:
      - [Zeiler, 2012](http://arxiv.org/abs/1212.5701)
    '''
    epsilon: Incomplete
    def __init__(self, learning_rate: float = 0.001, rho: float = 0.95, epsilon: float = 1e-07, name: str = 'Adadelta', **kwargs) -> None: ...
    def set_weights(self, weights) -> None: ...
    def get_config(self): ...
