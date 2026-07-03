from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def file_system_set_configuration(scheme, key, value, name: Incomplete | None = None):
    """Set configuration of the file system.

  Args:
    scheme: A `Tensor` of type `string`. File system scheme.
    key: A `Tensor` of type `string`. The name of the configuration option.
    value: A `Tensor` of type `string`. The value of the configuration option.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

FileSystemSetConfiguration: Incomplete

def file_system_set_configuration_eager_fallback(scheme, key, value, name, ctx): ...
