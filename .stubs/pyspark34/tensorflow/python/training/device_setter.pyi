from _typeshed import Incomplete
from tensorflow.core.framework import node_def_pb2 as node_def_pb2
from tensorflow.python.training import server_lib as server_lib
from tensorflow.python.util.tf_export import tf_export as tf_export

STANDARD_PS_OPS: Incomplete

class _RoundRobinStrategy:
    """Returns the next ps task index for placement in round-robin order.

  This class is not to be used directly by users.  See instead
  `replica_device_setter()` below.
  """
    def __init__(self, num_tasks) -> None:
        """Create a new `_RoundRobinStrategy`.

    Args:
      num_tasks: Number of ps tasks to cycle among.
    """
    def __call__(self, unused_op):
        """Choose a ps task index for the given `Operation`.

    Args:
      unused_op: An `Operation` to be placed on ps.

    Returns:
      The next ps task index to use for the `Operation`. Returns the next
      index, in the range `[offset, offset + num_tasks)`.
    """

class _ReplicaDeviceChooser:
    """Class to choose devices for Ops in a replicated training setup.

  This class is not to be used directly by users.  See instead
  `replica_device_setter()` below.
  """
    def __init__(self, ps_tasks, ps_device, worker_device, merge_devices, ps_ops, ps_strategy) -> None:
        """Create a new `_ReplicaDeviceChooser`.

    Args:
      ps_tasks: Number of tasks in the `ps` job.
      ps_device: String.  Name of the `ps` job.
      worker_device: String.  Name of the `worker` job.
      merge_devices: Boolean. Set to True to allow merging of device specs.
      ps_ops: List of strings representing `Operation` types that need to be
        placed on `ps` devices.
      ps_strategy: A callable invoked for every ps `Operation` (i.e. matched by
        `ps_ops`), that takes the `Operation` and returns the ps task index to
        use.
    """
    def device_function(self, op):
        """Choose a device for `op`.

    Args:
      op: an `Operation`.

    Returns:
      The device to use for the `Operation`.
    """

def replica_device_setter(ps_tasks: int = 0, ps_device: str = '/job:ps', worker_device: str = '/job:worker', merge_devices: bool = True, cluster: Incomplete | None = None, ps_ops: Incomplete | None = None, ps_strategy: Incomplete | None = None):
    '''Return a `device function` to use when building a Graph for replicas.

  Device Functions are used in `with tf.device(device_function):` statement to
  automatically assign devices to `Operation` objects as they are constructed,
  Device constraints are added from the inner-most context first, working
  outwards. The merging behavior adds constraints to fields that are yet unset
  by a more inner context. Currently the fields are (job, task, cpu/gpu).

  If `cluster` is `None`, and `ps_tasks` is 0, the returned function is a no-op.
  Otherwise, the value of `ps_tasks` is derived from `cluster`.

  By default, only Variable ops are placed on ps tasks, and the placement
  strategy is round-robin over all ps tasks. A custom `ps_strategy` may be used
  to do more intelligent placement, such as
  `tf.contrib.training.GreedyLoadBalancingStrategy`.

  For example,

  ```python
  # To build a cluster with two ps jobs on hosts ps0 and ps1, and 3 worker
  # jobs on hosts worker0, worker1 and worker2.
  cluster_spec = {
      "ps": ["ps0:2222", "ps1:2222"],
      "worker": ["worker0:2222", "worker1:2222", "worker2:2222"]}
  with
  tf.compat.v1.device(tf.compat.v1.train.replica_device_setter(cluster=cluster_spec)):
    # Build your graph
    v1 = tf.Variable(...)  # assigned to /job:ps/task:0
    v2 = tf.Variable(...)  # assigned to /job:ps/task:1
    v3 = tf.Variable(...)  # assigned to /job:ps/task:0
  # Run compute
  ```

  Args:
    ps_tasks: Number of tasks in the `ps` job.  Ignored if `cluster` is
      provided.
    ps_device: String.  Device of the `ps` job.  If empty no `ps` job is used.
      Defaults to `ps`.
    worker_device: String.  Device of the `worker` job.  If empty no `worker`
      job is used.
    merge_devices: `Boolean`. If `True`, merges or only sets a device if the
      device constraint is completely unset. merges device specification rather
      than overriding them.
    cluster: `ClusterDef` proto or `ClusterSpec`.
    ps_ops: List of strings representing `Operation` types that need to be
      placed on `ps` devices.  If `None`, defaults to `STANDARD_PS_OPS`.
    ps_strategy: A callable invoked for every ps `Operation` (i.e. matched by
      `ps_ops`), that takes the `Operation` and returns the ps task index to
      use.  If `None`, defaults to a round-robin strategy across all `ps`
      devices.

  Returns:
    A function to pass to `tf.device()`.

  Raises:
    TypeError if `cluster` is not a dictionary or `ClusterDef` protocol buffer,
    or if `ps_strategy` is provided but not a callable.
  '''
