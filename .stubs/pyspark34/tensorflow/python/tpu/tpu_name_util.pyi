from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Text

def core(num: int) -> Text:
    """Returns the device name for a core in a replicated TPU computation.

  Args:
    num: the virtual core number within each replica to which operators should
    be assigned.
  Returns:
    A device name, suitable for passing to `tf.device()`.
  """
