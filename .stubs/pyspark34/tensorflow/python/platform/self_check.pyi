from tensorflow.python.platform import build_info as build_info

MSVCP_DLL_NAMES: str

def preload_check() -> None:
    """Raises an exception if the environment is not correctly configured.

  Raises:
    ImportError: If the check detects that the environment is not correctly
      configured, and attempting to load the TensorFlow runtime will fail.
  """
