from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.core.protobuf import config_pb2 as config_pb2, rewriter_config_pb2 as rewriter_config_pb2
from tensorflow.python.client import session as session
from tensorflow.python.distribute import multi_process_runner as multi_process_runner
from tensorflow.python.distribute.cluster_resolver import SimpleClusterResolver as SimpleClusterResolver, TFConfigClusterResolver as TFConfigClusterResolver
from tensorflow.python.eager import context as context, remote as remote
from tensorflow.python.framework import errors as errors, ops as ops, test_util as test_util
from tensorflow.python.platform import test as test
from tensorflow.python.training import coordinator as coordinator, server_lib as server_lib
from tensorflow.python.util import deprecation as deprecation, nest as nest
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.tf_export import tf_export as tf_export

original_run_std_server: Incomplete
pick_unused_port: Incomplete

def create_in_process_cluster(num_workers, num_ps, has_chief: bool = False, has_eval: bool = False, rpc_layer: str = 'grpc'):
    """Create an in-process cluster that consists of only standard server."""

class MultiProcessCluster:
    """A cluster of TensorFlow servers in separate processes.

  This class is not thread-safe.
  """
    def __init__(self, cluster_resolver, stream_output: bool = False, collective_leader: Incomplete | None = None) -> None: ...
    def start(self) -> None:
        """Starts one TensorFlow server for each task in the cluster_resolver.

    It will wait until all the servers are up before returns.
    """
    def stop(self) -> None:
        """Stops all the servers."""
    def kill_task(self, task_type, task_id) -> None:
        '''Kill a server given task_type and task_id.

    Args:
      task_type: the type of the task such as "worker".
      task_id: the id the task such as 1.
    '''
    def start_task(self, task_type, task_id) -> None:
        '''Starts a server given task_type and task_id.

    Args:
      task_type: the type of the task such as "worker".
      task_id: the id the task such as 1.

    Raises:
      ValueError: if the server already exists.
    '''
    @property
    def cluster_resolver(self): ...

def create_multi_process_cluster(num_workers, num_ps, has_chief: bool = False, has_eval: bool = False, rpc_layer: str = 'grpc', stream_output: bool = False, collective_leader: Incomplete | None = None): ...
def create_cluster_spec(has_chief: bool = False, num_workers: int = 1, num_ps: int = 0, has_eval: bool = False):
    '''Create a cluster spec with tasks with unused local ports.

  This utility finds available ports at localhost, and returns a dict that
  represents the cluster spec that utilizes those ports, according to the
  arguments. The dict representing the cluster spec contains task types, and
  their instances\' addresses. Note that this is usually only for testing purpose
  using multiple processes in the local machine, and should not be used for real
  multi-worker TensorFlow programs, where the addresses need to point to the
  processes at separate machines.

  This util is useful when creating the `cluster_spec` arg for
  `tf.__internal__.distribute.multi_process_runner.run`.

  Args:
    has_chief: Whether the generated cluster spec should contain "chief" task
      type.
    num_workers: Number of workers to use in the cluster spec.
    num_ps: Number of parameter servers to use in the cluster spec.
    has_eval: Whether this cluster spec has evaluator.

  Returns:
    A dict that represents the cluster spec using localhost ports for the tasks.

  Example:

  ```python
  cluster_spec =
  tf.__internal__.distribute.multi_process_runner.create_cluster_spec(
      has_chief=True, num_workers=2, num_ps=2)
  # An example of cluster_spec is
  # {\'chief\': [\'localhost:23381\'],
  # \'worker\': [\'localhost:19197\', \'localhost:22903\'],
  # \'ps\': [\'localhost:16912\', \'localhost:21535\']}

  cluster_spec =
  tf.__internal__.distribute.multi_process_runner.create_cluster_spec(
      has_chief=False, num_workers=0, num_ps=0, has_eval=True)
  # An example of cluster_spec is
  # {\'evaluator\': [\'localhost:23381\']}
  ```
  '''
def skip_if_grpc_server_cant_be_started(test_obj) -> Generator[None, None, None]: ...

class MultiWorkerTestBase(test.TestCase):
    """Base class for testing multi node strategy and dataset."""
    @classmethod
    def setUpClass(cls, num_workers: int = 2, num_ps: int = 1) -> None:
        """Create a local cluster with 2 workers."""
    def setUp(self) -> None: ...
    def session(self, graph: Incomplete | None = None, config: Incomplete | None = None, target: Incomplete | None = None) -> Generator[Incomplete, None, None]:
        """Create a test session with master target set to the testing cluster.

    Creates a test session that connects to the local testing cluster.

    Args:
      graph: Optional graph to use during the returned session.
      config: An optional config_pb2.ConfigProto to use to configure the
        session.
      target: the target of session to connect to.

    Yields:
      A Session object that should be used as a context manager to surround
      the graph building and execution code in a test case.
    """
    def cached_session(self, graph: Incomplete | None = None, config: Incomplete | None = None, target: Incomplete | None = None) -> Generator[Incomplete, None, None]:
        """Create a test session with master target set to the testing cluster.

    Creates a test session that connects to the local testing cluster.
    The session is only created once per test and then reused.

    Args:
      graph: Optional graph to use during the returned session.
      config: An optional config_pb2.ConfigProto to use to configure the
        session.
      target: the target of session to connect to.

    Yields:
      A Session object that should be used as a context manager to surround
      the graph building and execution code in a test case. Note that the
      session will live until the end of the test.
    """

class SingleWorkerTestBaseGraph(MultiWorkerTestBase):
    """Base class for testing remote single worker strategy graph and dataset."""
    @classmethod
    def setUpClass(cls) -> None: ...

class SingleWorkerTestBaseEager(test.TestCase):
    """Base class for testing remote single worker strategy eager and dataset."""
    def setUp(self) -> None: ...
    def cached_session(self): ...

class DummySession:
    def __enter__(self) -> None: ...
    def __exit__(self, exception_type: type[BaseException] | None, exception_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class MockOsEnv(collections_abc.Mapping):
    """A class that allows per-thread TF_CONFIG."""
    def __init__(self, *args) -> None: ...
    def get(self, key, default: Incomplete | None = None): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, val) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...

class IndependentWorkerTestBase(test.TestCase):
    """Testing infra for independent workers."""
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def run_multiple_tasks_in_threads(self, task_fn, cluster_spec, *args, **kwargs): ...
    def join_independent_workers(self, worker_threads) -> None: ...

class MultiWorkerMultiProcessTest(test.TestCase):
    """Testing infra for independent workers using multiple processes."""
    def run_multiple_tasks_in_processes(self, cmd_args, cluster_spec):
        """Run `cmd_args` in a process for each task in `cluster_spec`."""
    def join_independent_workers(self, worker_processes) -> None: ...
    def stream_stderr(self, processes, print_only_first: bool = False) -> None:
        """Consume stderr of all processes and print to stdout.

    To reduce the amount of logging, caller can set print_only_first to True.
    In that case, this function only prints stderr from the first process of
    each type.

    Args:
      processes: A dictionary from process type string -> list of processes.
      print_only_first: If true, only print output from first process of each
        type.
    """

def get_tf_config_task(): ...
def get_tf_config_cluster_spec(): ...
def get_task_type(): ...
def get_task_index(): ...
def is_chief(): ...
