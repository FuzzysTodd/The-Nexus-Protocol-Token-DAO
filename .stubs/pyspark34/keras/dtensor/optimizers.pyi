import abc
from _typeshed import Incomplete
from keras.optimizers import adadelta as adadelta, adagrad as adagrad, adam as adam, adamw as adamw, optimizer as optimizer_lib, rmsprop as rmsprop, sgd as sgd
from keras.optimizers.schedules import learning_rate_schedule as learning_rate_schedule

class Optimizer(optimizer_lib._BaseOptimizer, metaclass=abc.ABCMeta):
    """DTensor specific optimizers.

    The major changes for this class is that all the variable init logic will be
    mesh/layout aware.
    """
    def __init__(self, name, mesh: Incomplete | None = None) -> None:
        """Create a new Optimizer.

        Args:
          name: String. The name of the optimizer, which will appear in all the
            state variables created by this optimizer.
          mesh: dtensor.Mesh. The optional Mesh which will be used to create the
            states. Note that usually the state variable will use the layout
            from the corresponding model variables. This mesh only used for
            global variables like globle steps, learning rate, etc.
        """
    def add_variable_from_reference(self, model_variable, variable_name, initial_value: Incomplete | None = None):
        """Create an optimizer variable from model variable.

        Create an optimizer variable based on the information of model variable.
        For example, in SGD optimizer momemtum, for each model variable, a
        corresponding momemtum variable is created of the same shape and dtype.

        Args:
          model_variable: The corresponding model variable to the optimizer
            variable to be created.
          variable_name: The name prefix of the optimizer variable to be
            created.  The create variables name will follow the pattern
            `{variable_name}/{model_variable.name}`, e.g., `momemtum/dense_1`.
          initial_value: The initial value of the optimizer variable, if None,
            the value will be default to 0.

        Returns:
          An optimizer variable.
        """
    def aggregate_gradients(self, grads_and_vars) -> None: ...
    def apply_gradients(self, grads_and_vars) -> None:
        """Apply gradients to variables.

        Args:
          grads_and_vars: List of (gradient, variable) pairs.

        Returns:
          None

        Raises:
          TypeError: If `grads_and_vars` is malformed.
        """

class Adadelta(Optimizer, adadelta.Adadelta):
    rho: Incomplete
    epsilon: Incomplete
    def __init__(self, learning_rate: float = 0.001, rho: float = 0.95, epsilon: float = 1e-07, gradients_clip_option: Incomplete | None = None, ema_option: Incomplete | None = None, name: str = 'Adadelta', mesh: Incomplete | None = None) -> None: ...

class Adagrad(Optimizer, adagrad.Adagrad):
    initial_accumulator_value: Incomplete
    epsilon: Incomplete
    def __init__(self, learning_rate: float = 0.001, initial_accumulator_value: float = 0.1, epsilon: float = 1e-07, gradients_clip_option: Incomplete | None = None, ema_option: Incomplete | None = None, name: str = 'Adagrad', mesh: Incomplete | None = None) -> None: ...

class Adam(Optimizer, adam.Adam):
    beta_1: Incomplete
    beta_2: Incomplete
    epsilon: Incomplete
    amsgrad: Incomplete
    def __init__(self, learning_rate: float = 0.001, beta_1: float = 0.9, beta_2: float = 0.999, epsilon: float = 1e-07, amsgrad: bool = False, gradients_clip_option: Incomplete | None = None, ema_option: Incomplete | None = None, name: str = 'Adam', mesh: Incomplete | None = None) -> None: ...

class AdamW(Optimizer, adamw.AdamW):
    weight_decay: Incomplete
    beta_1: Incomplete
    beta_2: Incomplete
    epsilon: Incomplete
    amsgrad: Incomplete
    def __init__(self, learning_rate: float = 0.001, weight_decay: float = 0.004, beta_1: float = 0.9, beta_2: float = 0.999, epsilon: float = 1e-07, amsgrad: bool = False, name: str = 'AdamW', mesh: Incomplete | None = None) -> None: ...

class RMSprop(Optimizer, rmsprop.RMSprop, metaclass=abc.ABCMeta):
    rho: Incomplete
    momentum: Incomplete
    epsilon: Incomplete
    centered: Incomplete
    def __init__(self, learning_rate: float = 0.001, rho: float = 0.9, momentum: float = 0.0, epsilon: float = 1e-07, centered: bool = False, gradients_clip_option: Incomplete | None = None, ema_option: Incomplete | None = None, jit_compile: bool = False, name: str = 'RMSprop', mesh: Incomplete | None = None) -> None: ...

class SGD(Optimizer, sgd.SGD, metaclass=abc.ABCMeta):
    momentum: Incomplete
    nesterov: Incomplete
    def __init__(self, learning_rate: float = 0.01, momentum: float = 0.0, nesterov: bool = False, amsgrad: bool = False, gradients_clip_option: Incomplete | None = None, ema_option: Incomplete | None = None, jit_compile: bool = False, name: str = 'SGD', mesh: Incomplete | None = None) -> None: ...
