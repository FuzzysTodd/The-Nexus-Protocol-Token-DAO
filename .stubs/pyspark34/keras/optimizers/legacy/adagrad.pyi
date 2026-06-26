from _typeshed import Incomplete
from keras import backend_config as backend_config
from keras.optimizers.legacy import optimizer_v2 as optimizer_v2

class Adagrad(optimizer_v2.OptimizerV2):
    '''Optimizer that implements the Adagrad algorithm.

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
      name: Optional name prefix for the operations created when applying
        gradients.  Defaults to `"Adagrad"`.
      **kwargs: keyword arguments. Allowed arguments are `clipvalue`,
        `clipnorm`, `global_clipnorm`.
        If `clipvalue` (float) is set, the gradient of each weight
        is clipped to be no higher than this value.
        If `clipnorm` (float) is set, the gradient of each weight
        is individually clipped so that its norm is no higher than this value.
        If `global_clipnorm` (float) is set the gradient of all weights is
        clipped so that their global norm is no higher than this value..

    Reference:
      - [Duchi et al., 2011](
        http://www.jmlr.org/papers/volume12/duchi11a/duchi11a.pdf).
    '''
    epsilon: Incomplete
    def __init__(self, learning_rate: float = 0.001, initial_accumulator_value: float = 0.1, epsilon: float = 1e-07, name: str = 'Adagrad', **kwargs) -> None: ...
    def set_weights(self, weights) -> None: ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None):
        """Creates an optimizer from its config.

        This method is the reverse of `get_config`,
        capable of instantiating the same optimizer from the config
        dictionary.

        Args:
            config: A Python dictionary, typically the output of get_config.
            custom_objects: A Python dictionary mapping names to additional
              Python objects used to create this optimizer, such as a function
              used for a hyperparameter.

        Returns:
            An optimizer instance.
        """
    def get_config(self): ...
