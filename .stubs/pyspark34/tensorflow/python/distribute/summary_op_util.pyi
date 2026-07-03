from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.framework import ops as ops, tensor_util as tensor_util

def skip_summary():
    """Determines if summary should be skipped.

  If using multiple replicas in distributed strategy, skip summaries on all
  replicas except the first one (replica_id=0).

  Returns:
    True if the summary is skipped; False otherwise.
  """
