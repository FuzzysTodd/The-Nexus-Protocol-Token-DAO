from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.python.distribute import parameter_server_strategy_v2 as parameter_server_strategy_v2
from tensorflow.python.distribute.coordinator import coordinator_context as coordinator_context, metric_utils as metric_utils, watchdog as watchdog
from tensorflow.python.eager import cancellation as cancellation, context as context, def_function as def_function, executor as executor
from tensorflow.python.framework import errors as errors, func_graph as func_graph, ops as ops
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import tf_export as tf_export

RemoteValueStatus: Incomplete
RemoteValue: Incomplete
RemoteValueImpl: Incomplete
PerWorkerValues: Incomplete

class ClosureInputError(Exception):
    """Wrapper for errors from resource building.

  When a closure starts, it first checks for errors in any of its inputs, which
  are RemoteValues from resource closures. If there were any errors, it wraps
  the exception in this class and raises so it can be handled by the worker
  failure handler.

  Attributes:
    original_exception:
  """
    original_exception: Incomplete
    def __init__(self, original_exception) -> None: ...

class ClosureAbortedError(Exception):
    """Wrapper for errors from training closures, to attach to resource closures.

  This wrapper is used when a dependent training closure fails to set errors on
  its required resource closures.

  Attributes:
    original_exception: The Exception to wrap
  """
    original_exception: Incomplete
    def __init__(self, original_exception) -> None: ...

class Closure:
    """Hold a function to be scheduled and its arguments."""
    def __init__(self, function, cancellation_mgr, args: Incomplete | None = None, kwargs: Incomplete | None = None) -> None: ...
    def build_output_remote_value(self): ...
    def maybe_call_with_output_remote_value(self, method): ...
    def mark_cancelled(self): ...
    def execute_on(self, worker):
        """Executes the closure on the given worker.

    Args:
      worker: a `Worker` object.
    """

class ResourceClosure(Closure):
    def build_output_remote_value(self): ...

class _CoordinatedClosureQueue:
    """Manage a queue of closures, inflight count and errors from execution.

  This class is thread-safe.
  """
    def __init__(self) -> None: ...
    def stop(self) -> None: ...
    def put(self, closure, tag: Incomplete | None = None):
        """Put a closure into the queue for later execution.

    If `mark_failed` was called before `put`, the error from the first
    invocation of `mark_failed` will be raised.

    Args:
      closure: The `Closure` to put into the queue.
      tag: if not None, put into a queue with the given tag.
    """
    def get(self, timeout: Incomplete | None = None, tag: Incomplete | None = None):
        """Return a closure from the queue to be executed.

    It will try to fetch an item from the queue with the given tag. If this
    queue is empty, it will then check the global queue.

    Args:
      timeout: timeout when waiting for a closure to be put.
      tag: optional tag to specify which queue to query first before querying
        the global queue.

    Returns:
      a closure or None after timeout.
    """
    def mark_finished(self) -> None:
        """Let the queue know that a closure has been successfully executed."""
    def put_back(self, closure):
        """Put the closure back into the queue as it was not properly executed."""
    def wait(self, timeout: Incomplete | None = None):
        """Wait for all closures to be finished before returning.

    If `mark_failed` was called before or during `wait`, the error from the
    first invocation of `mark_failed` will be raised.

    Args:
      timeout: A float specifying a timeout for the wait in seconds.

    Returns:
      True unless the given timeout expired, in which case it returns False.
    """
    def mark_failed(self, e) -> None:
        """Sets error and unblocks any wait() call."""
    def done(self):
        """Returns true if the queue is empty and there is no inflight closure.

    If `mark_failed` was called before `done`, the error from the first
    invocation of `mark_failed` will be raised.
    """
    def clear_tag_unlocked(self, tag) -> None: ...

class WorkerPreemptionHandler:
    """Handles worker preemptions."""
    def __init__(self, server_def, cluster) -> None: ...
    def stop(self) -> None:
        """Ensure the worker preemption thread is closed."""
    def wait_on_failure(self, on_failure_fn: Incomplete | None = None, on_transient_failure_fn: Incomplete | None = None, on_recovery_fn: Incomplete | None = None, worker_device_name: str = '(unknown)') -> Generator[None, None, None]:
        """Catches worker preemption error and wait until failed workers are back.

    Args:
      on_failure_fn: an optional function to run if preemption happens.
      on_transient_failure_fn: an optional function to run if transient failure
        happens.
      on_recovery_fn: an optional function to run when a worker is recovered
        from preemption.
      worker_device_name: the device name of the worker instance that is passing
        through the failure.

    Yields:
      None.
    """

class Worker:
    '''A worker in a cluster.

  Attributes:
    worker_index: The index of the worker in the cluster.
    device_name: The device string of the worker, e.g. "/job:worker/task:1".
    executor: The worker\'s executor for remote function execution.
    failure_handler: The failure handler used to handler worker preemption
      failure.
  '''
    worker_index: Incomplete
    device_name: Incomplete
    executor: Incomplete
    failure_handler: Incomplete
    def __init__(self, worker_index, device_name, cluster) -> None: ...
    def stop(self) -> None:
        """Ensure the worker thread is closed."""
    def create_resource(self, function, args: Incomplete | None = None, kwargs: Incomplete | None = None):
        """Synchronously creates a per-worker resource represented by a `RemoteValue`.

    Args:
      function: the resource function to be run remotely. It should be a
        `tf.function`, a concrete function or a Python function.
      args: positional arguments to be passed to the function.
      kwargs: keyword arguments to be passed to the function.

    Returns:
      one or several RemoteValue objects depending on the function return
      values.
    """

class Cluster:
    """A cluster with workers.

  We assume all function errors are fatal and based on this assumption our
  error reporting logic is:
  1) Both `schedule` and `join` can raise a non-retryable error which is the
  first error seen by the coordinator from any previously scheduled functions.
  2) When an error is raised, there is no guarantee on how many previously
  scheduled functions have been executed; functions that have not been executed
  will be thrown away and marked as cancelled.
  3) After an error is raised, the internal state of error will be cleared.
  I.e. functions can continue to be scheduled and subsequent calls of `schedule`
  or `join` will not raise the same error again.

  Attributes:
    failure_handler: The failure handler used to handler worker preemption
      failure.
    workers: a list of `Worker` objects in the cluster.
    closure_queue: the global Closure queue.
    resource_cancellation_mgr: the cancellation manager used to cancel resource
      closures.
  """
    closure_queue: Incomplete
    failure_handler: Incomplete
    workers: Incomplete
    resource_cancellation_mgr: Incomplete
    def __init__(self, strategy) -> None:
        """Initializes the cluster instance."""
    def stop(self) -> None:
        """Stop worker, worker preemption threads, and the closure queue."""
    def schedule(self, function, args, kwargs):
        """Schedules `function` to be dispatched to a worker for execution.

    Args:
      function: The function to be dispatched to a worker for execution
        asynchronously.
      args: Positional arguments for `fn`.
      kwargs: Keyword arguments for `fn`.

    Returns:
      A `RemoteValue` object.
    """
    def join(self) -> None:
        """Blocks until all scheduled functions are executed."""
    def done(self):
        """Returns true if all scheduled functions are executed."""

class ClusterCoordinator:
    """An object to schedule and coordinate remote function execution.

  This class is used to create fault-tolerant resources and dispatch functions
  to remote TensorFlow servers.

  Currently, this class is not supported to be used in a standalone manner. It
  should be used in conjunction with a `tf.distribute` strategy that is designed
  to work with it. The `ClusterCoordinator` class currently only works
  `tf.distribute.experimental.ParameterServerStrategy`.

  __The `schedule`/`join` APIs__

  The most important APIs provided by this class is the `schedule`/`join` pair.
  The `schedule` API is non-blocking in that it queues a `tf.function` and
  returns a `RemoteValue` immediately. The queued functions will be dispatched
  to remote workers in background threads and their `RemoteValue`s will be
  filled asynchronously. Since `schedule` doesn’t require worker assignment, the
  `tf.function` passed in can be executed on any available worker. If the worker
  it is executed on becomes unavailable before its completion, it will be
  migrated to another worker. Because of this fact and function execution is not
  atomic, a function may be executed more than once.

  __Handling Task Failure__

  This class when used with
  `tf.distribute.experimental.ParameterServerStrategy`, comes with built-in
  fault tolerance for worker failures. That is, when some workers are not
  available for any reason to be reached from the coordinator, the training
  progress continues to be made with the remaining workers. Upon recovery of a
  failed worker, it will be added for function execution after datasets created
  by `create_per_worker_dataset` are re-built on it.

  When a parameter server fails, a `tf.errors.UnavailableError` is raised by
  `schedule`, `join` or `done`. In this case, in addition to bringing back the
  failed parameter server, users should restart the coordinator so that it
  reconnects to workers and parameter servers, re-creates the variables, and
  loads checkpoints. If the coordinator fails, after the user brings it back,
  the program will automatically connect to workers and parameter servers, and
  continue the progress from a checkpoint.

  It is thus essential that in user's program, a checkpoint file is periodically
  saved, and restored at the start of the program. If an
  `tf.keras.optimizers.Optimizer` is checkpointed, after restoring from a
  checkpoiont, its `iterations` property roughly indicates the number of steps
  that have been made. This can be used to decide how many epochs and steps are
  needed before the training completion.

  See `tf.distribute.experimental.ParameterServerStrategy` docstring for an
  example usage of this API.

  This is currently under development, and the API as well as implementation
  are subject to changes.
  """
    def __new__(cls, strategy): ...
    def __init__(self, strategy) -> None:
        """Initialization of a `ClusterCoordinator` instance.

    Args:
      strategy: a supported `tf.distribute.Strategy` object. Currently, only
        `tf.distribute.experimental.ParameterServerStrategy` is supported.

    Raises:
      ValueError: if the strategy being used is not supported.
    """
    def __del__(self) -> None: ...
    @property
    def strategy(self):
        """Returns the `Strategy` associated with the `ClusterCoordinator`."""
    def schedule(self, fn, args: Incomplete | None = None, kwargs: Incomplete | None = None):
        """Schedules `fn` to be dispatched to a worker for asynchronous execution.

    This method is non-blocking in that it queues the `fn` which will be
    executed later and returns a
    `tf.distribute.experimental.coordinator.RemoteValue` object immediately.
    `fetch` can be called on it to wait for the function execution to finish
    and retrieve its output from a remote worker. On the other hand, call
    `tf.distribute.experimental.coordinator.ClusterCoordinator.join` to wait for
    all scheduled functions to finish.

    `schedule` guarantees that `fn` will be executed on a worker at least once;
    it could be more than once if its corresponding worker fails in the middle
    of its execution. Note that since worker can fail at any point when
    executing the function, it is possible that the function is partially
    executed, but `tf.distribute.experimental.coordinator.ClusterCoordinator`
    guarantees that in those events, the function will eventually be executed on
    any worker that is available.

    If any previously scheduled function raises an error, `schedule` will raise
    any one of those errors, and clear the errors collected so far. What happens
    here, some of the previously scheduled functions may have not been executed.
    User can call `fetch` on the returned
    `tf.distribute.experimental.coordinator.RemoteValue` to inspect if they have
    executed, failed, or cancelled, and reschedule the corresponding function if
    needed.

    When `schedule` raises, it guarantees that there is no function that is
    still being executed.

    At this time, there is no support of worker assignment for function
    execution, or priority of the workers.

    `args` and `kwargs` are the arguments passed into `fn`, when `fn` is
    executed on a worker. They can be
    `tf.distribute.experimental.coordinator.PerWorkerValues` and in this case,
    the argument will be substituted with the corresponding component on the
    target worker. Arguments that are not
    `tf.distribute.experimental.coordinator.PerWorkerValues` will be passed into
    `fn` as-is. Currently, `tf.distribute.experimental.coordinator.RemoteValue`
    is not supported to be input `args` or `kwargs`.

    Args:
      fn: A `tf.function`; the function to be dispatched to a worker for
        execution asynchronously. Regular python function is not supported to be
        scheduled.
      args: Positional arguments for `fn`.
      kwargs: Keyword arguments for `fn`.

    Returns:
      A `tf.distribute.experimental.coordinator.RemoteValue` object that
      represents the output of the function scheduled.

    Raises:
      Exception: one of the exceptions caught by the coordinator from any
        previously scheduled function, since the last time an error was thrown
        or since the beginning of the program.
    """
    def join(self) -> None:
        """Blocks until all the scheduled functions have finished execution.

    If any previously scheduled function raises an error, `join` will fail by
    raising any one of those errors, and clear the errors collected so far. If
    this happens, some of the previously scheduled functions may have not been
    executed. Users can call `fetch` on the returned
    `tf.distribute.experimental.coordinator.RemoteValue` to inspect if they have
    executed, failed, or cancelled. If some that have been cancelled need to be
    rescheduled, users should call `schedule` with the function again.

    When `join` returns or raises, it guarantees that there is no function that
    is still being executed.

    Raises:
      Exception: one of the exceptions caught by the coordinator by any
        previously scheduled function since the last time an error was thrown or
        since the beginning of the program.
    """
    def done(self):
        """Returns whether all the scheduled functions have finished execution.

    If any previously scheduled function raises an error, `done` will fail by
    raising any one of those errors.

    When `done` returns True or raises, it guarantees that there is no function
    that is still being executed.

    Returns:
      Whether all the scheduled functions have finished execution.
    Raises:
      Exception: one of the exceptions caught by the coordinator by any
        previously scheduled function since the last time an error was thrown or
        since the beginning of the program.
    """
    def create_per_worker_dataset(self, dataset_fn):
        """Create dataset on each worker.

    This creates dataset on workers from the input which can be either a
    `tf.data.Dataset`, a `tf.distribute.DistributedDataset` or a function which
    returns a dataset, and returns an object that represents the collection of
    those individual datasets. Calling `iter` on such collection of datasets
    returns a `tf.distribute.experimental.coordinator.PerWorkerValues`, which is
    a collection of iterators, where the iterators have been placed on
    respective workers.

    Calling `next` on a `PerWorkerValues` of iterator is unsupported. The
    iterator is meant to be passed as an argument into
    `tf.distribute.experimental.coordinator.ClusterCoordinator.schedule`. When
    the scheduled function is about to be executed by a worker, the
    function will receive the individual iterator that corresponds to the
    worker. The `next` method can be called on an iterator inside a
    scheduled function when the iterator is an input of the function.

    Currently the `schedule` method assumes workers are all the same and thus
    assumes the datasets on different workers are the same, except they may be
    shuffled differently if they contain a `dataset.shuffle` operation and a
    random seed is not set. Because of this, we also recommend the datasets to
    be repeated indefinitely and schedule a finite number of steps instead of
    relying on the `OutOfRangeError` from a dataset.


    Example:

    ```python
    strategy = tf.distribute.experimental.ParameterServerStrategy(
        cluster_resolver=...)
    coordinator = tf.distribute.experimental.coordinator.ClusterCoordinator(
        strategy=strategy)

    @tf.function
    def worker_fn(iterator):
      return next(iterator)

    def per_worker_dataset_fn():
      return strategy.distribute_datasets_from_function(
          lambda x: tf.data.Dataset.from_tensor_slices([3] * 3))

    per_worker_dataset = coordinator.create_per_worker_dataset(
        per_worker_dataset_fn)
    per_worker_iter = iter(per_worker_dataset)
    remote_value = coordinator.schedule(worker_fn, args=(per_worker_iter,))
    assert remote_value.fetch() == 3
    ```

    Args:
      dataset_fn: The dataset function that returns a dataset. This is to be
        executed on the workers.

    Returns:
      An object that represents the collection of those individual
      datasets. `iter` is expected to be called on this object that returns
      a `tf.distribute.experimental.coordinator.PerWorkerValues` of the
      iterators (that are on the workers).
    """
    def fetch(self, val):
        """Blocking call to fetch results from the remote values.

    This is a wrapper around
    `tf.distribute.experimental.coordinator.RemoteValue.fetch` for a
    `RemoteValue` structure; it returns the execution results of
    `RemoteValue`s. If not ready, wait for them while blocking the caller.

    Example:
    ```python
    strategy = ...
    coordinator = tf.distribute.experimental.coordinator.ClusterCoordinator(
        strategy)

    def dataset_fn():
      return tf.data.Dataset.from_tensor_slices([1, 1, 1])

    with strategy.scope():
      v = tf.Variable(initial_value=0)

    @tf.function
    def worker_fn(iterator):
      def replica_fn(x):
        v.assign_add(x)
        return v.read_value()
      return strategy.run(replica_fn, args=(next(iterator),))

    distributed_dataset = coordinator.create_per_worker_dataset(dataset_fn)
    distributed_iterator = iter(distributed_dataset)
    result = coordinator.schedule(worker_fn, args=(distributed_iterator,))
    assert coordinator.fetch(result) == 1
    ```

    Args:
      val: The value to fetch the results from. If this is structure of
        `tf.distribute.experimental.coordinator.RemoteValue`, `fetch()` will be
        called on the individual
        `tf.distribute.experimental.coordinator.RemoteValue` to get the result.

    Returns:
      If `val` is a `tf.distribute.experimental.coordinator.RemoteValue` or a
      structure of `tf.distribute.experimental.coordinator.RemoteValue`s,
      return the fetched `tf.distribute.experimental.coordinator.RemoteValue`
      values immediately if they are available, or block the call until they are
      available, and return the fetched
      `tf.distribute.experimental.coordinator.RemoteValue` values with the same
      structure. If `val` is other types, return it as-is.
    """
