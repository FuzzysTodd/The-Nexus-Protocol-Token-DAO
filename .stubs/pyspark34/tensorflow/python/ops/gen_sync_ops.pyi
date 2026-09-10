from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def sync_device(name: Incomplete | None = None):
    """Synchronizes the device this op is run on.

  Only GPU ops are asynchrous in TensorFlow, and so this only has an effect when
  run on GPUs. On GPUs, this op synchronizes the GPU's compute stream.

  Args:
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

SyncDevice: Incomplete

def sync_device_eager_fallback(name, ctx): ...
