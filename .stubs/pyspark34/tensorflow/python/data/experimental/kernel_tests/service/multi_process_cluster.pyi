from _typeshed import Incomplete
from tensorflow.core.protobuf import data_service_pb2 as data_service_pb2, service_config_pb2 as service_config_pb2
from tensorflow.python.data.experimental.service import server_lib as server_lib
from tensorflow.python.distribute import multi_process_lib as multi_process_lib
from tensorflow.python.framework import test_util as test_util
from tensorflow.python.platform import googletest as googletest

class _RemoteWorkerProcess(multi_process_lib.Process):
    """Runs a worker server in a new process to simulate a remote worker."""
    def __init__(self, dispatcher_address, port, worker_tags, pipe_writer) -> None: ...
    def run(self) -> None: ...
    def start_worker(self) -> None: ...

class MultiProcessCluster:
    '''tf.data service cluster with local and remote workers.

  Represents a cluster with a dispatcher, `num_local_workers` local workers, and
  `num_remote_workers` remote workers. Remote workers run in separate processes.
  This is useful to test reading from local in-process workers. For example:

  ```
  cluster = multi_process_cluster.MultiProcessCluster(
      num_local_workers=1, num_remote_workers=3)
  num_elements = 10
  dataset = self.make_distributed_range_dataset(
      num_elements, cluster, target_workers="LOCAL")
  self.assertDatasetProduces(dataset, list(range(num_elements)))
  ```
  '''
    def __init__(self, num_local_workers, num_remote_workers, worker_tags: Incomplete | None = None, worker_addresses: Incomplete | None = None, deployment_mode=...) -> None: ...
    def start_local_worker(self, worker_tags: Incomplete | None = None) -> None: ...
    def start_remote_worker(self, worker_tags: Incomplete | None = None) -> None:
        """Runs a tf.data service worker in a remote process."""
    def restart_dispatcher(self) -> None: ...
    def restart_local_workers(self) -> None: ...
    def dispatcher_address(self): ...
    def local_worker_addresses(self): ...
    def remote_worker_addresses(self): ...
    def __del__(self) -> None: ...

def test_main() -> None:
    """Main function to be called within `__main__` of a test file."""
