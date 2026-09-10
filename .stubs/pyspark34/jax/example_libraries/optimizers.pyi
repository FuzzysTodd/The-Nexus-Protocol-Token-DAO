from _typeshed import Incomplete
from jax import tree_util as tree_util
from jax._src.util import safe_map as safe_map, safe_zip as safe_zip, unzip2 as unzip2
from jax.tree_util import register_pytree_node as register_pytree_node, tree_flatten as tree_flatten, tree_map as tree_map, tree_unflatten as tree_unflatten
from typing import Any, Callable, NamedTuple

map = safe_map
zip = safe_zip

class OptimizerState(NamedTuple):
    packed_state: Incomplete
    tree_def: Incomplete
    subtree_defs: Incomplete
Array = Any
Params = Any
State = Any
Updates = Params
InitFn = Callable[[Params], OptimizerState]
Step = int
UpdateFn = Callable[[Step, Updates, OptimizerState], OptimizerState]
ParamsFn = Callable[[OptimizerState], Params]

class Optimizer(NamedTuple):
    init_fn: InitFn
    update_fn: UpdateFn
    params_fn: ParamsFn
Schedule = Callable[[Step], float]

def optimizer(opt_maker: Callable[..., tuple[Callable[[Params], State], Callable[[Step, Updates, Params], Params], Callable[[State], Params]]]) -> Callable[..., Optimizer]:
    """Decorator to make an optimizer defined for arrays generalize to containers.

  With this decorator, you can write init, update, and get_params functions that
  each operate only on single arrays, and convert them to corresponding
  functions that operate on pytrees of parameters. See the optimizers defined in
  optimizers.py for examples.

  Args:
    opt_maker: a function that returns an ``(init_fun, update_fun, get_params)``
      triple of functions that might only work with ndarrays, as per

      .. code-block:: haskell

          init_fun :: ndarray -> OptStatePytree ndarray
          update_fun :: OptStatePytree ndarray -> OptStatePytree ndarray
          get_params :: OptStatePytree ndarray -> ndarray

  Returns:
    An ``(init_fun, update_fun, get_params)`` triple of functions that work on
    arbitrary pytrees, as per

    .. code-block:: haskell

          init_fun :: ParameterPytree ndarray -> OptimizerState
          update_fun :: OptimizerState -> OptimizerState
          get_params :: OptimizerState -> ParameterPytree ndarray

    The OptimizerState pytree type used by the returned functions is isomorphic
    to ``ParameterPytree (OptStatePytree ndarray)``, but may store the state
    instead as e.g. a partially-flattened data structure for performance.
  """
def sgd(step_size):
    """Construct optimizer triple for stochastic gradient descent.

  Args:
    step_size: positive scalar, or a callable representing a step size schedule
      that maps the iteration index to a positive scalar.

  Returns:
    An (init_fun, update_fun, get_params) triple.
  """
def momentum(step_size: Schedule, mass: float):
    """Construct optimizer triple for SGD with momentum.

  Args:
    step_size: positive scalar, or a callable representing a step size schedule
      that maps the iteration index to a positive scalar.
    mass: positive scalar representing the momentum coefficient.

  Returns:
    An (init_fun, update_fun, get_params) triple.
  """
def nesterov(step_size: Schedule, mass: float):
    """Construct optimizer triple for SGD with Nesterov momentum.

  Args:
    step_size: positive scalar, or a callable representing a step size schedule
      that maps the iteration index to a positive scalar.
    mass: positive scalar representing the momentum coefficient.

  Returns:
    An (init_fun, update_fun, get_params) triple.
  """
def adagrad(step_size, momentum: float = 0.9):
    """Construct optimizer triple for Adagrad.

  Adaptive Subgradient Methods for Online Learning and Stochastic Optimization:
  http://www.jmlr.org/papers/volume12/duchi11a/duchi11a.pdf

  Args:
    step_size: positive scalar, or a callable representing a step size schedule
      that maps the iteration index to a positive scalar.
    momentum: optional, a positive scalar value for momentum

  Returns:
    An (init_fun, update_fun, get_params) triple.
  """
def rmsprop(step_size, gamma: float = 0.9, eps: float = 1e-08):
    """Construct optimizer triple for RMSProp.

  Args:
    step_size: positive scalar, or a callable representing a step size schedule
      that maps the iteration index to a positive scalar.
      gamma: Decay parameter.
      eps: Epsilon parameter.

  Returns:
    An (init_fun, update_fun, get_params) triple.
  """
def rmsprop_momentum(step_size, gamma: float = 0.9, eps: float = 1e-08, momentum: float = 0.9):
    """Construct optimizer triple for RMSProp with momentum.

  This optimizer is separate from the rmsprop optimizer because it needs to
  keep track of additional parameters.

  Args:
    step_size: positive scalar, or a callable representing a step size schedule
      that maps the iteration index to a positive scalar.
    gamma: Decay parameter.
    eps: Epsilon parameter.
    momentum: Momentum parameter.

  Returns:
    An (init_fun, update_fun, get_params) triple.
  """
def adam(step_size, b1: float = 0.9, b2: float = 0.999, eps: float = 1e-08):
    """Construct optimizer triple for Adam.

  Args:
    step_size: positive scalar, or a callable representing a step size schedule
      that maps the iteration index to a positive scalar.
    b1: optional, a positive scalar value for beta_1, the exponential decay rate
      for the first moment estimates (default 0.9).
    b2: optional, a positive scalar value for beta_2, the exponential decay rate
      for the second moment estimates (default 0.999).
    eps: optional, a positive scalar value for epsilon, a small constant for
      numerical stability (default 1e-8).

  Returns:
    An (init_fun, update_fun, get_params) triple.
  """
def adamax(step_size, b1: float = 0.9, b2: float = 0.999, eps: float = 1e-08):
    """Construct optimizer triple for AdaMax (a variant of Adam based on infinity norm).

  Args:
    step_size: positive scalar, or a callable representing a step size schedule
      that maps the iteration index to a positive scalar.
    b1: optional, a positive scalar value for beta_1, the exponential decay rate
      for the first moment estimates (default 0.9).
    b2: optional, a positive scalar value for beta_2, the exponential decay rate
      for the second moment estimates (default 0.999).
    eps: optional, a positive scalar value for epsilon, a small constant for
      numerical stability (default 1e-8).

  Returns:
    An (init_fun, update_fun, get_params) triple.
  """
def sm3(step_size, momentum: float = 0.9):
    """Construct optimizer triple for SM3.

  Memory-Efficient Adaptive Optimization for Large-Scale Learning.
  https://arxiv.org/abs/1901.11150

  Args:
    step_size: positive scalar, or a callable representing a step size schedule
      that maps the iteration index to a positive scalar.
    momentum: optional, a positive scalar value for momentum

  Returns:
    An (init_fun, update_fun, get_params) triple.
  """
def constant(step_size) -> Schedule: ...
def exponential_decay(step_size, decay_steps, decay_rate): ...
def inverse_time_decay(step_size, decay_steps, decay_rate, staircase: bool = False): ...
def polynomial_decay(step_size, decay_steps, final_step_size, power: float = 1.0): ...
def piecewise_constant(boundaries: Any, values: Any): ...
def make_schedule(scalar_or_schedule: float | Schedule) -> Schedule: ...
def l2_norm(tree):
    """Compute the l2 norm of a pytree of arrays. Useful for weight decay."""
def clip_grads(grad_tree, max_norm):
    """Clip gradients stored as a pytree of arrays to maximum norm `max_norm`."""

class JoinPoint:
    """Marks the boundary between two joined (nested) pytrees."""
    subtree: Incomplete
    def __init__(self, subtree) -> None: ...
    def __iter__(self): ...

def unpack_optimizer_state(opt_state):
    """Converts an OptimizerState to a marked pytree.

  Converts an OptimizerState to a marked pytree with the leaves of the outer
  pytree represented as JoinPoints to avoid losing information. This function is
  intended to be useful when serializing optimizer states.

  Args:
    opt_state: An OptimizerState
  Returns:
    A pytree with JoinPoint leaves that contain a second level of pytrees.
  """
def pack_optimizer_state(marked_pytree):
    """Converts a marked pytree to an OptimizerState.

  The inverse of unpack_optimizer_state. Converts a marked pytree with the
  leaves of the outer pytree represented as JoinPoints back into an
  OptimizerState. This function is intended to be useful when deserializing
  optimizer states.

  Args:
    marked_pytree: A pytree containing JoinPoint leaves that hold more pytrees.
  Returns:
    An equivalent OptimizerState to the input argument.
  """
