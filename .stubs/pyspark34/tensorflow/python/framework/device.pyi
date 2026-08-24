from tensorflow.python import tf2 as tf2
from tensorflow.python.framework import device_spec as device_spec

DeviceSpec = device_spec.DeviceSpecV2
DeviceSpec = device_spec.DeviceSpecV1

def check_valid(spec) -> None:
    """Check that a device spec is valid.

  Args:
    spec: a string.

  Raises:
    An exception if the spec is invalid.
  """
def is_device_spec(obj):
    """Abstract away the fact that DeviceSpecV2 is the base class."""
def canonical_name(device):
    """Returns a canonical name for the given `DeviceSpec` or device name."""
def merge_device(spec):
    '''Returns a device function that merges devices specifications.

  This can be used to merge partial specifications of devices. The
  innermost setting for a device field takes precedence. For example:

    with tf.device(merge_device("/device:GPU:0"))
      # Nodes created here have device "/device:GPU:0"
      with tf.device(merge_device("/job:worker")):
        # Nodes created here have device "/job:worker/device:GPU:0"
        with tf.device(merge_device("/device:CPU:0")):
          # Nodes created here have device "/job:worker/device:CPU:0"
          with tf.device(merge_device("/job:ps")):
            # Nodes created here have device "/job:ps/device:CPU:0"

  Args:
    spec: A `DeviceSpec` or a device spec string (partially) describing the
      device that should be used for all nodes created in the scope of
      the returned device function\'s with block.

  Returns:
    A MergeDevice object with the above-described behavior.

  Raises:
    ValueError: if the spec was not valid.
  '''

class MergeDevice:
    """Wraps a device specification (DeviceSpec or str) with merge functionality.

  When called, this class will merge a node_def with its own spec. It also
  exposes a `shortcut_string_merge` method which can significantly improve
  performance of device placement.
  """
    def __init__(self, spec) -> None: ...
    def __call__(self, node_def): ...
    def shortcut_string_merge(self, node_def):
        """Merge a node def without materializing a full DeviceSpec object.

    Often a device merge is invoked in order to generate a string which can be
    passed into the c api. In such a case, we can cache the
      node_def.device  ->  merge_result_string

    map, and in most cases avoid:
      - Materializing a copy of self._spec (In the case of DeviceSpecV1)
      - Materializing a DeviceSpec for node_def.device
      - A DeviceSpec.merge_from invocation

    In practice the cache hit rate for this function is very high, because the
    number of invocations when iterating through the device stack is much
    larger than the number of devices.

    Args:
      node_def: An Operation (or Operation-like) to merge device constraints
        with self._spec

    Returns:
      A string containing the merged device specification.
    """
    @property
    def is_null_merge(self):
        """Indicate whether the wrapped spec is empty.

    In the degenerate case where self._spec is an empty specification, a caller
    may wish to skip a merge step entirely. (However this class does not have
    enough information to make that determination.)

    Returns:
      A boolean indicating whether a device merge will be trivial.
    """
