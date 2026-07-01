from _typeshed import Incomplete
from tensorflow.core.protobuf import service_config_pb2 as service_config_pb2
from tensorflow.python import pywrap_tensorflow as pywrap_tensorflow
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

class DispatcherConfig(NamedTuple('DispatcherConfig', [('port', Incomplete), ('protocol', Incomplete), ('work_dir', Incomplete), ('fault_tolerant_mode', Incomplete), ('worker_addresses', Incomplete), ('job_gc_check_interval_ms', Incomplete), ('job_gc_timeout_ms', Incomplete), ('worker_timeout_ms', Incomplete)])):
    '''Configuration class for tf.data service dispatchers.

  Fields:
    port: Specifies the port to bind to. A value of 0 indicates that the server
      may bind to any available port.
    protocol: The protocol to use for communicating with the tf.data service,
      e.g. "grpc".
    work_dir: A directory to store dispatcher state in. This
      argument is required for the dispatcher to be able to recover from
      restarts.
    fault_tolerant_mode: Whether the dispatcher should write its state to a
      journal so that it can recover from restarts. Dispatcher state, including
      registered datasets and created jobs, is synchronously written to the
      journal before responding to RPCs. If `True`, `work_dir` must also be
      specified.
    worker_addresses: If the job uses auto-sharding, it needs to specify a fixed
      list of worker addresses that will register with the dispatcher. The
      worker addresses should be in the format `"host"` or `"host:port"`, where
      `"port"` is an integer, named port, or `%port%` to match any port.
    job_gc_check_interval_ms: How often the dispatcher should scan through to
      delete old and unused jobs, in milliseconds. If not set, the runtime will
      select a reasonable default. A higher value will reduce load on the
      dispatcher, while a lower value will reduce the time it takes for the
      dispatcher to garbage collect expired jobs.
    job_gc_timeout_ms: How long a job needs to be unused before it becomes a
      candidate for garbage collection, in milliseconds. A value of -1 indicates
      that jobs should never be garbage collected. If not set, the runtime will
      select a reasonable default. A higher value will cause jobs to stay around
      longer with no consumers. This is useful if there is a large gap in
      time between when consumers read from the job. A lower value will reduce
      the time it takes to reclaim the resources from expired jobs.
    worker_timeout_ms: How long to wait for a worker to heartbeat before
      considering it missing. If not set, the runtime will select a reasonable
      default.
  '''
    def __new__(cls, port: int = 0, protocol: Incomplete | None = None, work_dir: Incomplete | None = None, fault_tolerant_mode: bool = False, worker_addresses: Incomplete | None = None, job_gc_check_interval_ms: Incomplete | None = None, job_gc_timeout_ms: Incomplete | None = None, worker_timeout_ms: Incomplete | None = None): ...

class DispatchServer:
    '''An in-process tf.data service dispatch server.

  A `tf.data.experimental.service.DispatchServer` coordinates a cluster of
  `tf.data.experimental.service.WorkerServer`s. When the workers start, they
  register themselves with the dispatcher.

  >>> dispatcher = tf.data.experimental.service.DispatchServer()
  >>> dispatcher_address = dispatcher.target.split("://")[1]
  >>> worker = tf.data.experimental.service.WorkerServer(
  ...     tf.data.experimental.service.WorkerConfig(
  ...     dispatcher_address=dispatcher_address))
  >>> dataset = tf.data.Dataset.range(10)
  >>> dataset = dataset.apply(tf.data.experimental.service.distribute(
  ...     processing_mode="parallel_epochs", service=dispatcher.target))
  >>> print(list(dataset.as_numpy_iterator()))
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  When starting a dedicated tf.data dispatch process, use join() to block
  after starting up the server, until the server terminates.

  ```
  dispatcher = tf.data.experimental.service.DispatchServer(
      tf.data.experimental.service.DispatcherConfig(port=5050))
  dispatcher.join()
  ```

  Call stop() to gracefully terminate the dispatcher. The server automatically
  stops when all reference to it have been deleted.

  To start a `DispatchServer` in fault-tolerant mode, set `work_dir` and
  `fault_tolerant_mode` like below:

  ```
  dispatcher = tf.data.experimental.service.DispatchServer(
      tf.data.experimental.service.DispatcherConfig(
          port=5050,
          work_dir="gs://my-bucket/dispatcher/work_dir",
          fault_tolerant_mode=True))
  ```
  '''
    def __init__(self, config: Incomplete | None = None, start: bool = True) -> None:
        """Creates a new dispatch server.

    Args:
      config: (Optional.) A `tf.data.experimental.service.DispatcherConfig`
        configration. If `None`, the dispatcher will use default
        configuration values.
      start: (Optional.) Boolean, indicating whether to start the server after
        creating it. Defaults to True.
    """
    def start(self) -> None:
        """Starts this server.

    >>> dispatcher = tf.data.experimental.service.DispatchServer(start=False)
    >>> dispatcher.start()

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        starting the server.
    """
    def join(self) -> None:
        """Blocks until the server has shut down.

    This is useful when starting a dedicated dispatch process.

    ```
    dispatcher = tf.data.experimental.service.DispatchServer(
        tf.data.experimental.service.DispatcherConfig(port=5050))
    dispatcher.join()
    ```

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        joining the server.
    """
    def stop(self) -> None:
        """Stops the server.

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        stopping the server.
    """
    @property
    def target(self):
        '''Returns a target that can be used to connect to the server.

    >>> dispatcher = tf.data.experimental.service.DispatchServer()
    >>> dataset = tf.data.Dataset.range(10)
    >>> dataset = dataset.apply(tf.data.experimental.service.distribute(
    ...     processing_mode="parallel_epochs", service=dispatcher.target))

    The returned string will be in the form protocol://address, e.g.
    "grpc://localhost:5050".
    '''
    def __del__(self) -> None: ...

class WorkerConfig(NamedTuple('WorkerConfig', [('dispatcher_address', Incomplete), ('worker_address', Incomplete), ('port', Incomplete), ('protocol', Incomplete), ('heartbeat_interval_ms', Incomplete), ('dispatcher_timeout_ms', Incomplete), ('data_transfer_protocol', Incomplete), ('data_transfer_address', Incomplete)])):
    '''Configuration class for tf.data service dispatchers.

  Fields:
    dispatcher_address: Specifies the address of the dispatcher.
    worker_address: Specifies the address of the worker server. This address is
      passed to the dispatcher so that the dispatcher can tell clients how to
      connect to this worker.
    port: Specifies the port to bind to. A value of 0 indicates that the worker
      can bind to any available port.
    protocol: A string indicating the protocol to be used by the worker to
      connect to the dispatcher. E.g. "grpc".
    heartbeat_interval_ms: How often the worker should heartbeat to the
      dispatcher, in milliseconds. If not set, the runtime will select a
      reasonable default. A higher value will reduce the load on the dispatcher,
      while a lower value will reduce the time it takes to reclaim resources
      from finished jobs.
    dispatcher_timeout_ms: How long, in milliseconds, to retry requests to the
      dispatcher before giving up and reporting an error. Defaults to 1 hour.
    data_transfer_protocol: A string indicating the protocol to be used by the
      worker to transfer data to the client. E.g. "grpc".
    data_transfer_address: A string indicating the data transfer address of the
      worker server.
  '''
    def __new__(cls, dispatcher_address, worker_address: Incomplete | None = None, port: int = 0, protocol: Incomplete | None = None, heartbeat_interval_ms: Incomplete | None = None, dispatcher_timeout_ms: Incomplete | None = None, data_transfer_protocol: Incomplete | None = None, data_transfer_address: Incomplete | None = None): ...

class WorkerServer:
    '''An in-process tf.data service worker server.

  A `tf.data.experimental.service.WorkerServer` performs `tf.data.Dataset`
  processing for user-defined datasets, and provides the resulting elements over
  RPC. A worker is associated with a single
  `tf.data.experimental.service.DispatchServer`.

  >>> dispatcher = tf.data.experimental.service.DispatchServer()
  >>> dispatcher_address = dispatcher.target.split("://")[1]
  >>> worker = tf.data.experimental.service.WorkerServer(
  ...     tf.data.experimental.service.WorkerConfig(
  ...         dispatcher_address=dispatcher_address))
  >>> dataset = tf.data.Dataset.range(10)
  >>> dataset = dataset.apply(tf.data.experimental.service.distribute(
  ...     processing_mode="parallel_epochs", service=dispatcher.target))
  >>> print(list(dataset.as_numpy_iterator()))
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  When starting a dedicated tf.data worker process, use join() to block
  after starting up the worker, until the worker terminates.

  ```
  worker = tf.data.experimental.service.WorkerServer(
      port=5051, dispatcher_address="localhost:5050")
  worker.join()
  ```

  Call stop() to gracefully terminate the worker. The worker automatically stops
  when all reference to it have been deleted.
  '''
    def __init__(self, config, start: bool = True) -> None:
        """Creates a new worker server.

    Args:
      config: A `tf.data.experimental.service.WorkerConfig` configration.
      start: (Optional.) Boolean, indicating whether to start the server after
        creating it. Defaults to True.
    """
    def start(self) -> None:
        """Starts this server.

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        starting the server.
    """
    def join(self) -> None:
        '''Blocks until the server has shut down.

    This is useful when starting a dedicated worker process.

    ```
    worker_server = tf.data.experimental.service.WorkerServer(
        port=5051, dispatcher_address="localhost:5050")
    worker_server.join()
    ```

    This method currently blocks forever.

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        joining the server.
    '''
    def stop(self) -> None:
        """Stops the server.

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        stopping the server.
    """
    def __del__(self) -> None: ...
