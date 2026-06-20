from tensorflow.python.distribute import central_storage_strategy as central_storage_strategy
from tensorflow.python.ops import clip_ops as clip_ops

def all_reduce_sum_gradients(grads_and_vars):
    """Returns all-reduced gradients aggregated via summation.

  Args:
    grads_and_vars: List of (gradient, variable) pairs.

  Returns:
    List of (gradient, variable) pairs where gradients have been all-reduced.
  """
def filter_empty_gradients(grads_and_vars):
    """Filter out `(grad, var)` pairs that have a gradient equal to `None`."""
def make_gradient_clipnorm_fn(clipnorm):
    """Creates a gradient transformation function for clipping by norm."""
def make_global_gradient_clipnorm_fn(clipnorm):
    """Creates a gradient transformation function for clipping by norm."""
def make_gradient_clipvalue_fn(clipvalue):
    """Creates a gradient transformation function for clipping by value."""
def strategy_supports_no_merge_call():
    """Returns if the current Strategy can operate in pure replica context."""
