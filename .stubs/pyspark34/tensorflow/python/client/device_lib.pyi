from _typeshed import Incomplete
from tensorflow.core.framework import device_attributes_pb2 as device_attributes_pb2
from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow

def list_local_devices(session_config: Incomplete | None = None):
    """List the available devices available in the local process.

  Args:
    session_config: a session config proto or None to use the default config.

  Returns:
    A list of `DeviceAttribute` protocol buffers.
  """
