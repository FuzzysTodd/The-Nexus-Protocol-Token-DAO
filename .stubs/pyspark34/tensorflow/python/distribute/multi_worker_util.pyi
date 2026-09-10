from _typeshed import Incomplete
from tensorflow.core.protobuf import cluster_pb2 as cluster_pb2
from tensorflow.python.training import server_lib as server_lib

def normalize_cluster_spec(cluster_spec):
    """Makes `cluster_spec` into a `ClusterSpec` object.

  Args:
    cluster_spec: a dict, ClusterDef or ClusterSpec object specifying the
      cluster configurations.

  Returns:
    a `ClusterSpec` object.

  Raises:
    ValueError: if `cluster_spec` is not a dict or a `ClusterSpec` or a
      `ClusterDef`.
  """
def task_count(cluster_spec, task_type): ...
def is_chief(cluster_spec: Incomplete | None = None, task_type: Incomplete | None = None, task_id: Incomplete | None = None):
    """Returns whether the given task is chief in the cluster.

  Since there is at most one evaluator and the evaluator itself should be
  independent of the training cluster, the evaluator job is also a chief job on
  its own.

  If this is currently running under a `_WorkerContext` of distribute
  coordinator, the arguments can be omitted as the result is already available.

  Args:
    cluster_spec: a dict, `ClusterDef` or `ClusterSpec` object specifying the
      cluster configurations.
    task_type: the task type in the cluster.
    task_id: the task id in the cluster.

  Returns:
    a boolean indicating whether the given task is chief.

  Raises:
    ValueError: if `task_type` is not in the `cluster_spec` or `task_id` exceeds
      the maximum id of the `task_type`.
  """
def collective_leader(cluster_spec, task_type, task_id):
    """Return the job name for the leader of for collective ops.

  Args:
    cluster_spec: a dict, `ClusterDef` or `ClusterSpec` object specifying the
      cluster configurations.
    task_type: the task type in the cluster.
    task_id: the task id in the cluster.

  Returns:
    a string indicating the leader job name or empty string if no need to set
    leader job.
  """
def coordination_leader(cluster_spec):
    """Return the task name of the coordination service leader.

  Args:
    cluster_spec: a dict, `ClusterDef` or `ClusterSpec` object sxpecifying the
      cluster configurations.

  Returns:
    a string indicating the task name of the coordination service leader.
  """
def worker_count(cluster_spec, task_type):
    """Returns the number of workers in the cluster."""
def id_in_cluster(cluster_spec, task_type, task_id):
    '''Returns a unique id for the task in the `task_type`\'s cluster.

  It returns an id ranging from [0, `worker_count(task_type, task_id)`).

  Note: this function assumes that "evaluate" job is in its own cluster or its
  own partition of a cluster.

  Args:
    cluster_spec: a dict, `ClusterDef` or `ClusterSpec` object to be validated.
    task_type: string indicating the type of the task.
    task_id: the id of the `task_type` in this cluster.

  Returns:
    an int indicating the unique id.

  Throws:
    ValueError: if `task_type` is not "chief", "worker" or "evaluator".
  '''
def should_save_checkpoint():
    """Returns whether the current worker should save checkpoints.

  In multi-worker training, if saving checkpoint is requested by user, or needed
  for fault-tolerance, the cluster should save checkpoint but not necessarily
  every worker in the cluster should.

  TODO(rchao): Consider generalizing this util to be `should_save_file` as there
  can be other files to save such as summary.

  Returns:
      Whether this particular worker in the cluster should save checkpoints.
  """
def should_load_checkpoint():
    """Returns whether the current worker should load checkpoints.

  In multi-worker training, if loading checkpoint is requested by user, or
  needed for fault-tolerance, the cluster should load checkpoint but not
  necessarily every worker in the cluster should.

  Returns:
      Whether this particular worker in the cluster should load checkpoints.
  """
def wait_for_other_workers():
    """Waits for other workers to reach the same call to this method."""
def has_worker_context():
    """Returns whether a worker context has been entered."""
