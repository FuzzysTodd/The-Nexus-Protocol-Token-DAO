import tensorflow as tf
from _typeshed import Incomplete

class _FeedingQueueRunner(tf.compat.v1.train.queue_runner.QueueRunner):
    """A queue runner that allows the feeding of values such as numpy arrays."""
    def __init__(self, queue: Incomplete | None = None, enqueue_ops: Incomplete | None = None, close_op: Incomplete | None = None, cancel_op: Incomplete | None = None, feed_fns: Incomplete | None = None, queue_closed_exception_types: Incomplete | None = None) -> None:
        """Initialize the queue runner.

    For further documentation, see `queue_runner.py`. Note that
    `FeedingQueueRunner` does not support construction from protobuffer nor
    serialization to protobuffer.

    Args:
      queue: A `Queue`.
      enqueue_ops: List of enqueue ops to run in threads later.
      close_op: Op to close the queue. Pending enqueue ops are preserved.
      cancel_op: Op to close the queue and cancel pending enqueue ops.
      feed_fns: a list of functions that return a dictionary mapping fed
        `Tensor`s to values. Must be the same length as `enqueue_ops`.
      queue_closed_exception_types: Optional tuple of Exception types that
        indicate that the queue has been closed when raised during an enqueue
        operation.  Defaults to `(tf.errors.OutOfRangeError,
        tf.errors.CancelledError)`.

    Raises:
      ValueError: `feed_fns` is not `None` and has different length than
        `enqueue_ops`.
    """
    def create_threads(self, sess, coord: Incomplete | None = None, daemon: bool = False, start: bool = False):
        """Create threads to run the enqueue ops for the given session.

    This method requires a session in which the graph was launched.  It creates
    a list of threads, optionally starting them.  There is one thread for each
    op passed in `enqueue_ops`.

    The `coord` argument is an optional coordinator, that the threads will use
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
      start: Boolean.  If `True` starts the threads.  If `False` the caller must
        call the `start()` method of the returned threads.

    Returns:
      A list of threads.
    """
    def to_proto(self) -> None: ...
