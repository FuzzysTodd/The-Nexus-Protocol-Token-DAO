from tensorflow.python.keras import backend as backend
from tensorflow.python.ops import variables as variables

def global_batch_size_supported(distribution_strategy): ...
def call_replica_local_fn(fn, *args, **kwargs):
    """Call a function that uses replica-local variables.

  This function correctly handles calling `fn` in a cross-replica
  context.

  Args:
    fn: The function to call.
    *args: Positional arguments to the `fn`.
    **kwargs: Keyword argument to `fn`.

  Returns:
    The result of calling `fn`.
  """
def is_distributed_variable(v):
    """Returns whether `v` is a distributed variable."""
