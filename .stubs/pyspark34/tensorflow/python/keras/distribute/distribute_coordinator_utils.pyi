from _typeshed import Incomplete
from tensorflow.core.protobuf import cluster_pb2 as cluster_pb2, config_pb2 as config_pb2
from tensorflow.python.client import session as session
from tensorflow.python.training import monitored_session as monitored_session, server_lib as server_lib

def get_current_worker_context():
    """Returns the current task context."""

class _TaskType:
    PS: str
    WORKER: str
    CHIEF: str
    EVALUATOR: str
    CLIENT: str

class _WorkerContext:
    """The worker context class.

  This context object provides configuration information for each task. One
  context manager with a worker context object will be created per
  invocation to the `worker_fn` where `get_current_worker_context` can be called
  to access the worker context object.
  """
    def __init__(self, strategy, cluster_spec, task_type, task_id, session_config: Incomplete | None = None, rpc_layer: str = 'grpc', worker_barrier: Incomplete | None = None) -> None:
        '''Initialize the worker context object.

    Args:
      strategy: a `DistributionStrategy` object.
      cluster_spec: a ClusterSpec object. It can be empty or None in the local
        training case.
      task_type: a string indicating the role of the corresponding task, such as
        "worker" or "ps". It can be None if it is local training or in-graph
        replicated training.
      task_id: an integer indicating id of the corresponding task. It can be
        None if it is local training or in-graph replicated training.
      session_config: an optional `tf.compat.v1.ConfigProto` object.
      rpc_layer: optional string specifying the RPC protocol for communication
        with worker masters. If None or empty, hosts in the `cluster_spec` will
        be used directly.
      worker_barrier: optional, the barrier object for worker synchronization.
    '''
    def __enter__(self) -> None: ...
    def __exit__(self, unused_exception_type: type[BaseException] | None, unused_exception_value: BaseException | None, unused_traceback: types.TracebackType | None) -> None: ...
    def wait_for_other_workers(self) -> None:
        """Waits for other workers to reach the same call to this method.

    Raises:
      ValueError: if `worker_barrier` is not passed to the __init__ method.
    """
    def session_creator(self, scaffold: Incomplete | None = None, config: Incomplete | None = None, checkpoint_dir: Incomplete | None = None, checkpoint_filename_with_path: Incomplete | None = None, max_wait_secs: int = 7200):
        """Returns a session creator.

    The returned session creator will be configured with the correct master
    target and session configs. It will also run either init ops or ready ops
    by querying the `strategy` object when `create_session` is called on it.

    Args:
      scaffold: A `Scaffold` used for gathering or building supportive ops. If
        not specified a default one is created. It's used to finalize the graph.
      config: `ConfigProto` proto used to configure the session.
      checkpoint_dir: A string. Optional path to a directory where to restore
        variables.
      checkpoint_filename_with_path: Full file name path to the checkpoint file.
        Only one of `checkpoint_dir` or `checkpoint_filename_with_path` can be
        specified.
      max_wait_secs: Maximum time to wait for the session to become available.

    Returns:
      a descendant of SessionCreator.
    """
    @property
    def session_config(self): ...
    @property
    def has_barrier(self):
        """Whether the barrier is set or not."""
    @property
    def distributed_mode(self):
        """Whether it is distributed training or not."""
    @property
    def cluster_spec(self):
        """Returns a copy of the cluster_spec object."""
    @property
    def task_type(self):
        """Returns the role of the corresponding task."""
    @property
    def task_id(self):
        """Returns the id or index of the corresponding task."""
    @property
    def master_target(self):
        """Returns the session master for the corresponding task to connect to."""
    @property
    def is_chief(self):
        """Returns whether the task is a chief node."""
    @property
    def num_workers(self):
        """Returns number of workers in the cluster, including chief."""
    @property
    def experimental_should_init(self):
        """Whether to run init ops."""
    @property
    def should_checkpoint(self):
        """Whether to save checkpoint."""
    @property
    def should_save_summary(self):
        """Whether to save summaries."""

def run_distribute_coordinator(worker_fn, strategy, eval_fn: Incomplete | None = None, eval_strategy: Incomplete | None = None, cluster_spec: Incomplete | None = None, task_type: Incomplete | None = None, task_id: Incomplete | None = None, session_config: Incomplete | None = None, rpc_layer: str = 'grpc'):
    '''Runs the coordinator for distributed TensorFlow.

  This function runs a split coordinator for distributed TensorFlow in its
  default mode, i.e the STANDALONE_CLIENT mode. Given a `cluster_spec`
  specifying server addresses and their roles in a cluster, this coordinator
  will figure out how to set them up, give the underlying function the right
  targets for master sessions via a scope object and coordinate their training.
  The cluster consisting of standard servers needs to be brought up either with
  the standard server binary or with a binary running distribute coordinator
  with `task_type` set to non-client type which will then turn into standard
  servers.

  In addition to be the distribute coordinator, this is also the source of
  configurations for each job in the distributed training. As there are multiple
  ways to configure a distributed TensorFlow cluster, its context object
  provides these configurations so that users or higher-level APIs don\'t have to
  figure out the configuration for each job by themselves.

  In the between-graph replicated training, this coordinator will create
  multiple threads and each calls the `worker_fn` which is supposed to create
  its own graph and connect to one worker master given by its context object. In
  the in-graph replicated training, it has only one thread calling this
  `worker_fn`.

  Another mode is the INDEPENDENT_WORKER mode where each server runs a
  distribute coordinator which will start a standard server and optionally runs
  `worker_fn` depending whether it is between-graph training or in-graph
  replicated training.

  The `strategy` object is expected to be a DistributionStrategy object which
  has implemented methods needed by distributed coordinator such as
  `configure(session_config, cluster_spec, task_type, task_id)` which configures
  the strategy object for a specific task and `experimental_should_init`
  property which instructs the distribute coordinator whether to run init ops
  for a task. The distribute coordinator will make a copy of the `strategy`
  object, call its `configure` method and pass it to `worker_fn` as an argument.

  The `worker_fn` defines the training logic and is called under its own
  worker context which can be accessed to via `get_current_worker_context`. A
  worker context provides access to configurations for each task, e.g. the
  task_type, task_id, master target and so on. Since `worker_fn` will be called
  in a thread and possibly multiple times, caller should be careful when it
  accesses global data. For example, it is unsafe to define flags in a
  `worker_fn` or to define different environment variables for different
  `worker_fn`s.

  The `worker_fn` for the between-graph replication is defined as if there is
  only one worker corresponding to the `worker_fn` and possibly ps jobs. For
  example, when training with parameter servers, it assigns variables to
  parameter servers and all other operations to that worker. In the in-graph
  replication case, the `worker_fn` has to define operations for all worker
  jobs. Using a distribution strategy can simplify the `worker_fn` by not having
  to worry about the replication and device assignment of variables and
  operations.

  This method is intended to be invoked by high-level APIs so that users don\'t
  have to explicitly call it to run this coordinator. For those who don\'t use
  high-level APIs, to change a program to use this coordinator, wrap everything
  in a the program after global data definitions such as commandline flag
  definition into the `worker_fn` and get task-specific configurations from
  the worker context.

  The `cluster_spec` can be either passed by the argument or parsed from the
  "TF_CONFIG" environment variable. Example of a TF_CONFIG:
  ```
    cluster = {\'chief\': [\'host0:2222\'],
               \'ps\': [\'host1:2222\', \'host2:2222\'],
               \'worker\': [\'host3:2222\', \'host4:2222\', \'host5:2222\']}
    os.environ[\'TF_CONFIG\'] = json.dumps({\'cluster\': cluster})
  ```

  If `cluster_spec` is not given in any format, it becomes local training and
  this coordinator will connect to a local session.

  For evaluation, if "evaluator" exists in the cluster_spec, a separate thread
  will be created to call `eval_fn` with its `task_type` set to "evaluator". If
  `eval_fn` is not defined, fall back to `worker_fn`. This implies that
  evaluation will be done on a single machine if there is an "evaluator" task.
  If "evaluator" doesn\'t exist in the cluster_spec, it entirely depends on the
  `worker_fn` for how to do evaluation.

  Args:
    worker_fn: the function to be called. The function should accept a
      `strategy` object and will be given access to a context object via a
      context manager scope.
    strategy: a DistributionStrategy object specifying whether it should run
      between-graph replicated training or not, whether to run init ops, etc.
      This object will also be configured given `session_config`,
      `cluster_spec`, `task_type` and `task_id`.
    eval_fn: optional function for "evaluator" task. If `eval_fn` is not passed
      in but a "evaluator" task is found in the `cluster_spec`, the `worker_fn`
      will be used for this task.
    eval_strategy: optional DistributionStrategy object for "evaluator" task.
    cluster_spec: a dict, ClusterDef or ClusterSpec specifying servers and roles
      in a cluster. If not set or empty, fall back to local training.
    task_type: the current task type, optional if this is a client.
    task_id: the current task id, optional if this is a client.
    session_config: an optional `tf.compat.v1.ConfigProto` object which will be
      passed to `strategy`\'s `configure` method and used to create a session.
    rpc_layer: optional string, the protocol for RPC, e.g. "grpc".

  Raises:
    ValueError: if `cluster_spec` is supplied but not a dict or a ClusterDef or
      a ClusterSpec.

  Returns:
    In the client job, return the value returned by `worker_fn` if
    it is in-graph replication or INDEPENDENT_WORKER mode; return None
    otherwise.
  '''
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
