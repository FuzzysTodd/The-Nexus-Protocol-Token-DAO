import tensorflow.compat.v2 as tf
from _typeshed import Incomplete
from keras import backend as backend

class Optimizer:
    """Abstract optimizer base class.

    Note: this is the parent class of all optimizers, not an actual optimizer
    that can be used for training models.

    All Keras optimizers support the following keyword arguments:

        clipnorm: float >= 0. Gradients will be clipped
            when their L2 norm exceeds this value.
        clipvalue: float >= 0. Gradients will be clipped
            when their absolute value exceeds this value.
    """
    updates: Incomplete
    weights: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def get_updates(self, loss, params) -> None: ...
    def get_gradients(self, loss, params):
        """Returns gradients of `loss` with respect to `params`.

        Args:
            loss: Loss tensor.
            params: List of variables.

        Returns:
            List of gradient tensors.

        Raises:
            ValueError: In case any gradient cannot be computed (e.g. if
              gradient function not implemented).
        """
    def set_weights(self, weights) -> None:
        """Sets the weights of the optimizer, from Numpy arrays.

        Should only be called after computing the gradients
        (otherwise the optimizer has no weights).

        Args:
            weights: a list of Numpy arrays. The number of arrays and their
              shape must match number of the dimensions of the weights of the
              optimizer (i.e. it should match the output of `get_weights`).

        Raises:
            ValueError: in case of incompatible weight shapes.
        """
    def get_weights(self):
        """Returns the current value of the weights of the optimizer.

        Returns:
            A list of numpy arrays.
        """
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...

class SGD(Optimizer):
    """Stochastic gradient descent optimizer.

    Includes support for momentum,
    learning rate decay, and Nesterov momentum.

    Args:
        lr: float >= 0. Learning rate.
        momentum: float >= 0. Parameter that accelerates SGD in the relevant
          direction and dampens oscillations.
        decay: float >= 0. Learning rate decay over each update.
        nesterov: boolean. Whether to apply Nesterov momentum.
    """
    iterations: Incomplete
    lr: Incomplete
    momentum: Incomplete
    decay: Incomplete
    initial_decay: Incomplete
    nesterov: Incomplete
    def __init__(self, lr: float = 0.01, momentum: float = 0.0, decay: float = 0.0, nesterov: bool = False, **kwargs) -> None: ...
    updates: Incomplete
    def get_updates(self, loss, params): ...
    def get_config(self): ...

class RMSprop(Optimizer):
    """RMSProp optimizer.

    It is recommended to leave the parameters of this optimizer
    at their default values
    (except the learning rate, which can be freely tuned).

    Args:
      lr: float >= 0. Learning rate.
      rho: float >= 0.
      epsilon: float >= 0. Fuzz factor.
        If `None`, defaults to `backend.epsilon()`.
      decay: float >= 0. Learning rate decay over each update.
    """
    lr: Incomplete
    rho: Incomplete
    decay: Incomplete
    iterations: Incomplete
    epsilon: Incomplete
    initial_decay: Incomplete
    def __init__(self, lr: float = 0.001, rho: float = 0.9, epsilon: Incomplete | None = None, decay: float = 0.0, **kwargs) -> None: ...
    updates: Incomplete
    def get_updates(self, loss, params): ...
    def get_config(self): ...

class Adagrad(Optimizer):
    """Adagrad optimizer.

    Adagrad is an optimizer with parameter-specific learning rates,
    which are adapted relative to how frequently a parameter gets
    updated during training. The more updates a parameter receives,
    the smaller the updates.

    It is recommended to leave the parameters of this optimizer
    at their default values.

    # Arguments
        lr: float >= 0. Initial learning rate.
        epsilon: float >= 0. If `None`, defaults to `backend.epsilon()`.
        decay: float >= 0. Learning rate decay over each update.

    # References
        - [Adaptive Subgradient Methods for Online Learning and Stochastic
        Optimization](http://www.jmlr.org/papers/volume12/duchi11a/duchi11a.pdf)
    """
    lr: Incomplete
    decay: Incomplete
    iterations: Incomplete
    epsilon: Incomplete
    initial_decay: Incomplete
    def __init__(self, lr: float = 0.01, epsilon: Incomplete | None = None, decay: float = 0.0, **kwargs) -> None: ...
    updates: Incomplete
    def get_updates(self, loss, params): ...
    def get_config(self): ...

class Adadelta(Optimizer):
    """Adadelta optimizer.

    Adadelta is a more robust extension of Adagrad
    that adapts learning rates based on a moving window of gradient updates,
    instead of accumulating all past gradients. This way, Adadelta continues
    learning even when many updates have been done. Compared to Adagrad, in the
    original version of Adadelta you don't have to set an initial learning
    rate. In this version, initial learning rate and decay factor can
    be set, as in most other Keras optimizers.

    It is recommended to leave the parameters of this optimizer
    at their default values.

    Arguments:
      lr: float >= 0. Initial learning rate, defaults to 1.
          It is recommended to leave it at the default value.
      rho: float >= 0. Adadelta decay factor, corresponding to fraction of
          gradient to keep at each time step.
      epsilon: float >= 0. Fuzz factor.
        If `None`, defaults to `backend.epsilon()`.
      decay: float >= 0. Initial learning rate decay.

    References:
        - [Adadelta - an adaptive learning rate
        method](http://arxiv.org/abs/1212.5701)
    """
    lr: Incomplete
    decay: Incomplete
    iterations: Incomplete
    rho: Incomplete
    epsilon: Incomplete
    initial_decay: Incomplete
    def __init__(self, lr: float = 1.0, rho: float = 0.95, epsilon: Incomplete | None = None, decay: float = 0.0, **kwargs) -> None: ...
    updates: Incomplete
    def get_updates(self, loss, params): ...
    def get_config(self): ...

class Adam(Optimizer):
    '''Adam optimizer.

    Default parameters follow those provided in the original paper.

    Args:
      lr: float >= 0. Learning rate.
      beta_1: float, 0 < beta < 1. Generally close to 1.
      beta_2: float, 0 < beta < 1. Generally close to 1.
      epsilon: float >= 0. Fuzz factor.
        If `None`, defaults to `backend.epsilon()`.
      decay: float >= 0. Learning rate decay over each update.
      amsgrad: boolean. Whether to apply the AMSGrad variant of this algorithm
        from the paper "On the Convergence of Adam and Beyond".
    '''
    iterations: Incomplete
    lr: Incomplete
    beta_1: Incomplete
    beta_2: Incomplete
    decay: Incomplete
    epsilon: Incomplete
    initial_decay: Incomplete
    amsgrad: Incomplete
    def __init__(self, lr: float = 0.001, beta_1: float = 0.9, beta_2: float = 0.999, epsilon: Incomplete | None = None, decay: float = 0.0, amsgrad: bool = False, **kwargs) -> None: ...
    updates: Incomplete
    def get_updates(self, loss, params): ...
    def get_config(self): ...

class Adamax(Optimizer):
    """Adamax optimizer from Adam paper's Section 7.

    It is a variant of Adam based on the infinity norm.
    Default parameters follow those provided in the paper.

    Args:
      lr: float >= 0. Learning rate.
      beta_1/beta_2: floats, 0 < beta < 1. Generally close to 1.
      epsilon: float >= 0. Fuzz factor.
        If `None`, defaults to `backend.epsilon()`.
      decay: float >= 0. Learning rate decay over each update.
    """
    iterations: Incomplete
    lr: Incomplete
    beta_1: Incomplete
    beta_2: Incomplete
    decay: Incomplete
    epsilon: Incomplete
    initial_decay: Incomplete
    def __init__(self, lr: float = 0.002, beta_1: float = 0.9, beta_2: float = 0.999, epsilon: Incomplete | None = None, decay: float = 0.0, **kwargs) -> None: ...
    updates: Incomplete
    def get_updates(self, loss, params): ...
    def get_config(self): ...

class Nadam(Optimizer):
    """Nesterov Adam optimizer.

    Much like Adam is essentially RMSprop with momentum,
    Nadam is Adam RMSprop with Nesterov momentum.

    Default parameters follow those provided in the paper.
    It is recommended to leave the parameters of this optimizer
    at their default values.

    Args:
      lr: float >= 0. Learning rate.
      beta_1/beta_2: floats, 0 < beta < 1. Generally close to 1.
      epsilon: float >= 0. Fuzz factor.
        If `None`, defaults to `backend.epsilon()`.
    """
    iterations: Incomplete
    m_schedule: Incomplete
    lr: Incomplete
    beta_1: Incomplete
    beta_2: Incomplete
    epsilon: Incomplete
    schedule_decay: Incomplete
    def __init__(self, lr: float = 0.002, beta_1: float = 0.9, beta_2: float = 0.999, epsilon: Incomplete | None = None, schedule_decay: float = 0.004, **kwargs) -> None: ...
    updates: Incomplete
    def get_updates(self, loss, params): ...
    def get_config(self): ...

class TFOptimizer(Optimizer, tf.__internal__.tracking.Trackable):
    """Wrapper class for native TensorFlow optimizers."""
    optimizer: Incomplete
    iterations: Incomplete
    def __init__(self, optimizer, iterations: Incomplete | None = None) -> None: ...
    def minimize(self, loss, var_list, grad_loss: Incomplete | None = None, tape: Incomplete | None = None) -> None:
        """Mimics the `OptimizerV2.minimize` API."""
    def apply_gradients(self, grads_and_vars) -> None: ...
    def get_grads(self, loss, params): ...
    updates: Incomplete
    def get_updates(self, loss, params): ...
    @property
    def weights(self) -> None: ...
    def get_config(self) -> None: ...
    def from_config(self, config) -> None: ...
sgd = SGD
rmsprop = RMSprop
adagrad = Adagrad
adadelta = Adadelta
adam = Adam
adamax = Adamax
nadam = Nadam
