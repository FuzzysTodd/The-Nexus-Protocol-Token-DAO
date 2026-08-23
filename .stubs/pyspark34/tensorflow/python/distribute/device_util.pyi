from _typeshed import Incomplete
from tensorflow.python.eager import context as context
from tensorflow.python.framework import config as config, ops as ops

def canonicalize(d, default: Incomplete | None = None):
    '''Canonicalize device string.

  If d has missing components, the rest would be deduced from the `default`
  argument or from \'/replica:0/task:0/device:CPU:0\'. For example:
    If d = \'/cpu:0\', default=\'/job:worker/task:1\', it returns
      \'/job:worker/replica:0/task:1/device:CPU:0\'.
    If d = \'/cpu:0\', default=\'/job:worker\', it returns
      \'/job:worker/replica:0/task:0/device:CPU:0\'.
    If d = \'/gpu:0\', default=None, it returns
      \'/replica:0/task:0/device:GPU:0\'.

  Note: This uses "job:localhost" as the default if executing eagerly.

  Args:
    d: a device string or tf.config.LogicalDevice
    default: a string for default device if d doesn\'t have all components.

  Returns:
    a canonicalized device string.
  '''
def canonicalize_without_job_and_task(d):
    '''Partially canonicalize device string.

  This returns device string from `d` without including job and task.
  This is most useful for parameter server strategy where the device strings are
  generated on the chief, but executed on workers.

   For example:
    If d = \'/cpu:0\', default=\'/job:worker/task:1\', it returns
      \'/replica:0/device:CPU:0\'.
    If d = \'/cpu:0\', default=\'/job:worker\', it returns
      \'/replica:0/device:CPU:0\'.
    If d = \'/gpu:0\', default=None, it returns
      \'/replica:0/device:GPU:0\'.

  Note: This uses "job:localhost" as the default if executing eagerly.

  Args:
    d: a device string or tf.config.LogicalDevice

  Returns:
    a partially canonicalized device string.
  '''
def resolve(d):
    """Canonicalize `d` with current device as default."""

class _FakeNodeDef:
    """A fake NodeDef for _FakeOperation."""
    op: str
    name: str
    def __init__(self) -> None: ...

class _FakeOperation:
    """A fake Operation object to pass to device functions."""
    device: str
    type: str
    name: str
    node_def: Incomplete
    def __init__(self) -> None: ...

def current():
    """Return a string (not canonicalized) for the current device."""
def get_host_for_device(device):
    """Returns the corresponding host device for the given device."""
def local_devices_from_num_gpus(num_gpus):
    """Returns device strings for local GPUs or CPU."""
