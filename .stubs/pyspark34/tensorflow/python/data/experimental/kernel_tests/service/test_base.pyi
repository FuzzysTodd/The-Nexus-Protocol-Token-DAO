from _typeshed import Incomplete
from tensorflow.core.protobuf import service_config_pb2 as service_config_pb2
from tensorflow.python.data.experimental.ops import data_service_ops as data_service_ops
from tensorflow.python.data.experimental.service import server_lib as server_lib
from tensorflow.python.data.kernel_tests import test_base as test_base
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.framework import combinations as combinations, dtypes as dtypes
from tensorflow.python.ops import math_ops as math_ops
from tensorflow.python.platform import googletest as googletest

TMP_WORK_DIR: str
NO_WORK_DIR: str
TEST_HEARTBEAT_INTERVAL_MS: int
TEST_DISPATCHER_TIMEOUT_MS: int
TEST_WORKER_TIMEOUT_MS: int
TEST_JOB_GC_CHECK_INTERNAL_MS: int
PROTOCOL: str

def all_cluster_configurations(): ...

class TestWorker:
    """A tf.data service worker."""
    def __init__(self, dispatcher_address, shutdown_quiet_period_ms, data_transfer_protocol: Incomplete | None = None, port: int = 0, worker_tags: Incomplete | None = None, cross_trainer_cache_size_bytes: Incomplete | None = None) -> None: ...
    def stop(self) -> None: ...
    def start(self) -> None: ...
    def restart(self, use_same_port: bool = True) -> None:
        """Restarts the worker, stopping it first if it is already running."""
    def join(self) -> None: ...
    def num_tasks(self): ...
    def snapshot_task_progresses(self): ...
    def worker_address(self): ...

class TestCluster:
    """Test tf.data service cluster."""
    dispatcher: Incomplete
    workers: Incomplete
    def __init__(self, num_workers, dispatcher_port: int = 0, work_dir=..., fault_tolerant_mode: bool = True, job_gc_check_interval_ms=..., job_gc_timeout_ms: Incomplete | None = None, worker_timeout_ms=..., worker_shutdown_quiet_period_ms: int = 0, start: bool = True, data_transfer_protocol: Incomplete | None = None) -> None:
        """Creates a tf.data service test cluster.

    Args:
      num_workers: The number of workers to initially add to the cluster.
      dispatcher_port: The port to use for the dispatcher.
      work_dir: The work directory to use for the dispatcher. If set to
        `TMP_WORK_DIR`, the cluster will create a new temporary directory to use
        as the work directory. If set to `NO_WORK_DIR`, no work directory will
        be used.
      fault_tolerant_mode: Whether the dispatcher should write its state to a
        journal so that it can recover from restarts.
      job_gc_check_interval_ms: How often the dispatcher should scan through to
        delete old and unused jobs, in milliseconds.
      job_gc_timeout_ms: How long a job needs to be unused before it becomes a
        candidate for garbage collection, in milliseconds.
      worker_timeout_ms: How long to wait for a worker to heartbeat before
        considering it missing, in milliseconds.
      worker_shutdown_quiet_period_ms: When shutting down a worker, how long to
        wait for the gRPC server to process the final requests.
      start: Whether to immediately start the servers in the cluster. If
        `False`, the servers can be started later by calling
        `start_dispatcher()` and `start_workers()`.
      data_transfer_protocol: (Optional.) The protocol to use for transferring
        data with the tf.data service.
    """
    def dispatcher_address(self): ...
    def add_worker(self, start: bool = True) -> None: ...
    def start_dispatcher(self) -> None: ...
    def start_workers(self) -> None: ...
    def stop_dispatcher(self) -> None: ...
    def stop_worker(self, index) -> None: ...
    def stop_workers(self) -> None: ...
    def restart_dispatcher(self) -> None:
        """Stops `dispatcher` and creates a new dispatcher with the same port.

    Restarting is supported only when the dispatcher is configured with
    `fault_tolerant_mode=True`.
    """
    def num_registered_workers(self): ...
    def num_tasks_on_workers(self): ...
    def snapshot_streams(self, path): ...
    def __del__(self) -> None: ...

class TestBase(test_base.DatasetTestBase):
    """Base class for tf.data service tests."""
    def make_distributed_dataset(self, dataset, cluster, processing_mode: str = 'parallel_epochs', job_name: Incomplete | None = None, consumer_index: Incomplete | None = None, num_consumers: Incomplete | None = None, max_outstanding_requests: Incomplete | None = None, data_transfer_protocol: Incomplete | None = None, compression: str = 'AUTO', cross_trainer_cache: Incomplete | None = None, target_workers: str = 'AUTO'): ...
    def make_distributed_range_dataset(self, num_elements, cluster, processing_mode: str = 'parallel_epochs', job_name: Incomplete | None = None, max_outstanding_requests: Incomplete | None = None, data_transfer_protocol: Incomplete | None = None, compression: str = 'AUTO', cross_trainer_cache: Incomplete | None = None, target_workers: str = 'AUTO'): ...
    def make_coordinated_read_dataset(self, cluster, num_consumers, sharding_policy=...):
        """Creates a dataset that performs coordinated reads.

    The dataset simulates `num_consumers` consumers by using parallel
    interleave to read with `num_consumers` threads, one for each consumer. The
    nth element of the dataset is produced by consumer `n % num_consumers`.

    The dataset executed on each worker will produce groups of `num_consumers`
    sequentially increasing numbers. For example, if `num_consumers=3` a worker
    dataset could produce [0, 1, 2, 9, 10, 11, 21, 22, 23]. This enables
    `checkCoordinatedReadGroups` below to assess whether the values received in
    each step came from the same group.

    Args:
      cluster: A tf.data service `TestCluster`.
      num_consumers: The number of consumers to simulate.
      sharding_policy: The sharding policy to use. Currently only OFF and
        DYNAMIC are supported.

    Returns:
      A dataset that simulates reading with `num_consumers` consumers.
    """
    def checkCoordinatedReadGroups(self, results, num_consumers) -> None:
        """Validates results from a `make_coordinted_read_dataset` dataset.

    Each group of `num_consumers` results should be consecutive, indicating that
    they were produced by the same worker.

    Args:
      results: The elements produced by the dataset.
      num_consumers: The number of consumers.
    """
    def read(self, get_next, results, count) -> None: ...
