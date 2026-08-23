from _typeshed import Incomplete
from tensorflow.core.protobuf import cluster_pb2 as cluster_pb2, device_filters_pb2 as device_filters_pb2, tensorflow_server_pb2 as tensorflow_server_pb2
from tensorflow.python.framework import errors as errors
from tensorflow.python.util import compat as compat, deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

class Server:
    """An in-process TensorFlow server, for use in distributed training.

  A `tf.distribute.Server` instance encapsulates a set of devices and a
  `tf.compat.v1.Session` target that
  can participate in distributed training. A server belongs to a
  cluster (specified by a `tf.train.ClusterSpec`), and
  corresponds to a particular task in a named job. The server can
  communicate with any other server in the same cluster.
  """
    def __init__(self, server_or_cluster_def, job_name: Incomplete | None = None, task_index: Incomplete | None = None, protocol: Incomplete | None = None, config: Incomplete | None = None, start: bool = True) -> None:
        '''Creates a new server with the given definition.

    The `job_name`, `task_index`, and `protocol` arguments are optional, and
    override any information provided in `server_or_cluster_def`.

    Args:
      server_or_cluster_def: A `tf.train.ServerDef` or `tf.train.ClusterDef`
        protocol buffer, or a `tf.train.ClusterSpec` object, describing the
        server to be created and/or the cluster of which it is a member.
      job_name: (Optional.) Specifies the name of the job of which the server is
        a member. Defaults to the value in `server_or_cluster_def`, if
        specified.
      task_index: (Optional.) Specifies the task index of the server in its job.
        Defaults to the value in `server_or_cluster_def`, if specified.
        Otherwise defaults to 0 if the server\'s job has only one task.
      protocol: (Optional.) Specifies the protocol to be used by the server.
        Acceptable values include `"grpc", "grpc+verbs"`. Defaults to the value
        in `server_or_cluster_def`, if specified. Otherwise defaults to
        `"grpc"`.
      config: (Options.) A `tf.compat.v1.ConfigProto` that specifies default
        configuration options for all sessions that run on this server.
      start: (Optional.) Boolean, indicating whether to start the server after
        creating it. Defaults to `True`.

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        creating the TensorFlow server.
    '''
    def __del__(self) -> None: ...
    def start(self) -> None:
        """Starts this server.

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        starting the TensorFlow server.
    """
    def join(self) -> None:
        """Blocks until the server has shut down.

    This method currently blocks forever.

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        joining the TensorFlow server.
    """
    @property
    def server_def(self):
        """Returns the `tf.train.ServerDef` for this server.

    Returns:
      A `tf.train.ServerDef` protocol buffer that describes the configuration
      of this server.
    """
    @property
    def target(self):
        """Returns the target for a `tf.compat.v1.Session` to connect to this server.

    To create a
    `tf.compat.v1.Session` that
    connects to this server, use the following snippet:

    ```python
    server = tf.distribute.Server(...)
    with tf.compat.v1.Session(server.target):
      # ...
    ```

    Returns:
      A string containing a session target for this server.
    """
    @staticmethod
    def create_local_server(config: Incomplete | None = None, start: bool = True):
        '''Creates a new single-process cluster running on the local host.

    This method is a convenience wrapper for creating a
    `tf.distribute.Server` with a `tf.train.ServerDef` that specifies a
    single-process cluster containing a single task in a job called
    `"local"`.

    Args:
      config: (Options.) A `tf.compat.v1.ConfigProto` that specifies default
        configuration options for all sessions that run on this server.
      start: (Optional.) Boolean, indicating whether to start the server after
        creating it. Defaults to `True`.

    Returns:
      A local `tf.distribute.Server`.
    '''

class ClusterSpec:
    '''Represents a cluster as a set of "tasks", organized into "jobs".

  A `tf.train.ClusterSpec` represents the set of processes that
  participate in a distributed TensorFlow computation. Every
  `tf.distribute.Server` is constructed in a particular cluster.

  To create a cluster with two jobs and five tasks, you specify the
  mapping from job names to lists of network addresses (typically
  hostname-port pairs).

  ```python
  cluster = tf.train.ClusterSpec({"worker": ["worker0.example.com:2222",
                                             "worker1.example.com:2222",
                                             "worker2.example.com:2222"],
                                  "ps": ["ps0.example.com:2222",
                                         "ps1.example.com:2222"]})
  ```

  Each job may also be specified as a sparse mapping from task indices
  to network addresses. This enables a server to be configured without
  needing to know the identity of (for example) all other worker
  tasks:

  ```python
  cluster = tf.train.ClusterSpec({"worker": {1: "worker1.example.com:2222"},
                                  "ps": ["ps0.example.com:2222",
                                         "ps1.example.com:2222"]})
  ```
  '''
    def __init__(self, cluster) -> None:
        """Creates a `ClusterSpec`.

    Args:
      cluster: A dictionary mapping one or more job names to (i) a list of
        network addresses, or (ii) a dictionary mapping integer task indices to
        network addresses; or a `tf.train.ClusterDef` protocol buffer.

    Raises:
      TypeError: If `cluster` is not a dictionary mapping strings to lists
        of strings, and not a `tf.train.ClusterDef` protobuf.
    """
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def as_dict(self):
        """Returns a dictionary from job names to their tasks.

    For each job, if the task index space is dense, the corresponding
    value will be a list of network addresses; otherwise it will be a
    dictionary mapping (sparse) task indices to the corresponding
    addresses.

    Returns:
      A dictionary mapping job names to lists or dictionaries
      describing the tasks in those jobs.
    """
    def as_cluster_def(self):
        """Returns a `tf.train.ClusterDef` protocol buffer based on this cluster."""
    @property
    def jobs(self):
        """Returns a list of job names in this cluster.

    Returns:
      A list of strings, corresponding to the names of jobs in this cluster.
    """
    def num_tasks(self, job_name):
        """Returns the number of tasks defined in the given job.

    Args:
      job_name: The string name of a job in this cluster.

    Returns:
      The number of tasks defined in the given job.

    Raises:
      ValueError: If `job_name` does not name a job in this cluster.
    """
    def task_indices(self, job_name):
        """Returns a list of valid task indices in the given job.

    Args:
      job_name: The string name of a job in this cluster.

    Returns:
      A list of valid task indices in the given job.

    Raises:
      ValueError: If `job_name` does not name a job in this cluster,
      or no task with index `task_index` is defined in that job.
    """
    def task_address(self, job_name, task_index):
        """Returns the address of the given task in the given job.

    Args:
      job_name: The string name of a job in this cluster.
      task_index: A non-negative integer.

    Returns:
      The address of the given task in the given job.

    Raises:
      ValueError: If `job_name` does not name a job in this cluster,
      or no task with index `task_index` is defined in that job.
    """
    def job_tasks(self, job_name):
        """Returns a mapping from task ID to address in the given job.

    NOTE: For backwards compatibility, this method returns a list. If
    the given job was defined with a sparse set of task indices, the
    length of this list may not reflect the number of tasks defined in
    this job. Use the `tf.train.ClusterSpec.num_tasks` method
    to find the number of tasks defined in a particular job.

    Args:
      job_name: The string name of a job in this cluster.

    Returns:
      A list of task addresses, where the index in the list
      corresponds to the task index of each task. The list may contain
      `None` if the job was defined with a sparse set of task indices.

    Raises:
      ValueError: If `job_name` does not name a job in this cluster.
    """

class ClusterDeviceFilters:
    '''Represent a collection of device filters for the remote workers in cluster.

  NOTE: this is an experimental API and subject to changes.

  Set device filters for selective jobs and tasks. For each remote worker, the
  device filters are a list of strings. When any filters are present, the remote
  worker will ignore all devices which do not match any of its filters. Each
  filter can be partially specified, e.g. "/job:ps", "/job:worker/replica:3",
  etc. Note that a device is always visible to the worker it is located on.

  For example, to set the device filters for a parameter server cluster:

  ```python
  cdf = tf.config.experimental.ClusterDeviceFilters()
  for i in range(num_workers):
    cdf.set_device_filters(\'worker\', i, [\'/job:ps\'])
  for i in range(num_ps):
    cdf.set_device_filters(\'ps\', i, [\'/job:worker\'])

  tf.config.experimental_connect_to_cluster(cluster_def,
                                            cluster_device_filters=cdf)
  ```

  The device filters can be partically specified. For remote tasks that do not
  have device filters specified, all devices will be visible to them.
  '''
    def __init__(self) -> None: ...
    def set_device_filters(self, job_name, task_index, device_filters) -> None:
        """Set the device filters for given job name and task id."""
