from _typeshed import Incomplete
from tensorflow.core.protobuf import queue_runner_pb2 as queue_runner_pb2
from tensorflow.python.client import session as session
from tensorflow.python.eager import context as context
from tensorflow.python.framework import errors as errors, ops as ops
from tensorflow.python.util import deprecation as deprecation
from tensorflow.python.util.tf_export import tf_export as tf_export

class QueueRunner:
    """Holds a list of enqueue operations for a queue, each to be run in a thread.

  Queues are a convenient TensorFlow mechanism to compute tensors
  asynchronously using multiple threads. For example in the canonical 'Input
  Reader' setup one set of threads generates filenames in a queue; a second set
  of threads read records from the files, processes them, and enqueues tensors
  on a second queue; a third set of threads dequeues these input records to
  construct batches and runs them through training operations.

  There are several delicate issues when running multiple threads that way:
  closing the queues in sequence as the input is exhausted, correctly catching
  and reporting exceptions, etc.

  The `QueueRunner`, combined with the `Coordinator`, helps handle these issues.

  @compatibility(TF2)
  QueueRunners are not compatible with eager execution. Instead, please
  use [tf.data](https://www.tensorflow.org/guide/data) to get data into your
  model.
  @end_compatibility
  """
    def __init__(self, queue: Incomplete | None = None, enqueue_ops: Incomplete | None = None, close_op: Incomplete | None = None, cancel_op: Incomplete | None = None, queue_closed_exception_types: Incomplete | None = None, queue_runner_def: Incomplete | None = None, import_scope: Incomplete | None = None) -> None:
        """Create a QueueRunner.

    On construction the `QueueRunner` adds an op to close the queue.  That op
    will be run if the enqueue ops raise exceptions.

    When you later call the `create_threads()` method, the `QueueRunner` will
    create one thread for each op in `enqueue_ops`.  Each thread will run its
    enqueue op in parallel with the other threads.  The enqueue ops do not have
    to all be the same op, but it is expected that they all enqueue tensors in
    `queue`.

    Args:
      queue: A `Queue`.
      enqueue_ops: List of enqueue ops to run in threads later.
      close_op: Op to close the queue. Pending enqueue ops are preserved.
      cancel_op: Op to close the queue and cancel pending enqueue ops.
      queue_closed_exception_types: Optional tuple of Exception types that
        indicate that the queue has been closed when raised during an enqueue
        operation.  Defaults to `(tf.errors.OutOfRangeError,)`.  Another common
        case includes `(tf.errors.OutOfRangeError, tf.errors.CancelledError)`,
        when some of the enqueue ops may dequeue from other Queues.
      queue_runner_def: Optional `QueueRunnerDef` protocol buffer. If specified,
        recreates the QueueRunner from its contents. `queue_runner_def` and the
        other arguments are mutually exclusive.
      import_scope: Optional `string`. Name scope to add. Only used when
        initializing from protocol buffer.

    Raises:
      ValueError: If both `queue_runner_def` and `queue` are both specified.
      ValueError: If `queue` or `enqueue_ops` are not provided when not
        restoring from `queue_runner_def`.
      RuntimeError: If eager execution is enabled.
    """
    @property
    def queue(self): ...
    @property
    def enqueue_ops(self): ...
    @property
    def close_op(self): ...
    @property
    def cancel_op(self): ...
    @property
    def queue_closed_exception_types(self): ...
    @property
    def exceptions_raised(self):
        """Exceptions raised but not handled by the `QueueRunner` threads.

    Exceptions raised in queue runner threads are handled in one of two ways
    depending on whether or not a `Coordinator` was passed to
    `create_threads()`:

    * With a `Coordinator`, exceptions are reported to the coordinator and
      forgotten by the `QueueRunner`.
    * Without a `Coordinator`, exceptions are captured by the `QueueRunner` and
      made available in this `exceptions_raised` property.

    Returns:
      A list of Python `Exception` objects.  The list is empty if no exception
      was captured.  (No exceptions are captured when using a Coordinator.)
    """
    @property
    def name(self):
        """The string name of the underlying Queue."""
    def create_threads(self, sess, coord: Incomplete | None = None, daemon: bool = False, start: bool = False):
        """Create threads to run the enqueue ops for the given session.

    This method requires a session in which the graph was launched.  It creates
    a list of threads, optionally starting them.  There is one thread for each
    op passed in `enqueue_ops`.

    The `coord` argument is an optional coordinator that the threads will use
    to terminate together and report exceptions.  If a coordinator is given,
    this method starts an additional thread to close the queue when the
    coordinator requests a stop.

    If previously created threads for the given session are still running, no
    new threads will be created.

    Args:
      sess: A `Session`.
      coord: Optional `Coordinator` object for reporting errors and checking
        stop conditions.
      daemon: Boolean.  If `True` make the threads daemon threads.
      start: Boolean.  If `True` starts the threads.  If `False` the
        caller must call the `start()` method of the returned threads.

    Returns:
      A list of threads.
    """
    def to_proto(self, export_scope: Incomplete | None = None):
        """Converts this `QueueRunner` to a `QueueRunnerDef` protocol buffer.

    Args:
      export_scope: Optional `string`. Name scope to remove.

    Returns:
      A `QueueRunnerDef` protocol buffer, or `None` if the `Variable` is not in
      the specified name scope.
    """
    @staticmethod
    def from_proto(queue_runner_def, import_scope: Incomplete | None = None):
        """Returns a `QueueRunner` object created from `queue_runner_def`."""

def add_queue_runner(qr, collection=...) -> None:
    """Adds a `QueueRunner` to a collection in the graph.

  When building a complex model that uses many queues it is often difficult to
  gather all the queue runners that need to be run.  This convenience function
  allows you to add a queue runner to a well known collection in the graph.

  The companion method `start_queue_runners()` can be used to start threads for
  all the collected queue runners.

  @compatibility(TF2)
  QueueRunners are not compatible with eager execution. Instead, please
  use [tf.data](https://www.tensorflow.org/guide/data) to get data into your
  model.
  @end_compatibility

  Args:
    qr: A `QueueRunner`.
    collection: A `GraphKey` specifying the graph collection to add
      the queue runner to.  Defaults to `GraphKeys.QUEUE_RUNNERS`.
  """
def start_queue_runners(sess: Incomplete | None = None, coord: Incomplete | None = None, daemon: bool = True, start: bool = True, collection=...):
    """Starts all queue runners collected in the graph.

  This is a companion method to `add_queue_runner()`.  It just starts
  threads for all queue runners collected in the graph.  It returns
  the list of all threads.

  @compatibility(TF2)
  QueueRunners are not compatible with eager execution. Instead, please
  use [tf.data](https://www.tensorflow.org/guide/data) to get data into your
  model.
  @end_compatibility

  Args:
    sess: `Session` used to run the queue ops.  Defaults to the
      default session.
    coord: Optional `Coordinator` for coordinating the started threads.
    daemon: Whether the threads should be marked as `daemons`, meaning
      they don't block program exit.
    start: Set to `False` to only create the threads, not start them.
    collection: A `GraphKey` specifying the graph collection to
      get the queue runners from.  Defaults to `GraphKeys.QUEUE_RUNNERS`.

  Raises:
    ValueError: if `sess` is None and there isn't any default session.
    TypeError: if `sess` is not a `tf.compat.v1.Session` object.

  Returns:
    A list of threads.

  Raises:
    RuntimeError: If called with eager execution enabled.
    ValueError: If called without a default `tf.compat.v1.Session` registered.
  """
