from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, summary_ops_v2 as summary_ops_v2
from tensorflow.python.platform import gfile as gfile

class EventFileWriterV2:
    """Writes `Event` protocol buffers to an event file via the graph.

  The `EventFileWriterV2` class is backed by the summary file writer in the v2
  summary API (currently in tf.contrib.summary), so it uses a shared summary
  writer resource and graph ops to write events.

  As with the original EventFileWriter, this class will asynchronously write
  Event protocol buffers to the backing file. The Event file is encoded using
  the tfrecord format, which is similar to RecordIO.
  """
    def __init__(self, session, logdir, max_queue: int = 10, flush_secs: int = 120, filename_suffix: str = '') -> None:
        """Creates an `EventFileWriterV2` and an event file to write to.

    On construction, this calls `tf.contrib.summary.create_file_writer` within
    the graph from `session.graph` to look up a shared summary writer resource
    for `logdir` if one exists, and create one if not. Creating the summary
    writer resource in turn creates a new event file in `logdir` to be filled
    with `Event` protocol buffers passed to `add_event`. Graph ops to control
    this writer resource are added to `session.graph` during this init call;
    stateful methods on this class will call `session.run()` on these ops.

    Note that because the underlying resource is shared, it is possible that
    other parts of the code using the same session may interact independently
    with the resource, e.g. by flushing or even closing it. It is the caller's
    responsibility to avoid any undesirable sharing in this regard.

    The remaining arguments to the constructor (`flush_secs`, `max_queue`, and
    `filename_suffix`) control the construction of the shared writer resource
    if one is created. If an existing resource is reused, these arguments have
    no effect.  See `tf.contrib.summary.create_file_writer` for details.

    Args:
      session: A `tf.compat.v1.Session`. Session that will hold shared writer
        resource. The writer ops will be added to session.graph during this
        init call.
      logdir: A string. Directory where event file will be written.
      max_queue: Integer. Size of the queue for pending events and summaries.
      flush_secs: Number. How often, in seconds, to flush the
        pending events and summaries to disk.
      filename_suffix: A string. Every event file's name is suffixed with
        `filename_suffix`.
    """
    def get_logdir(self):
        """Returns the directory where event file will be written."""
    def reopen(self) -> None:
        """Reopens the EventFileWriter.

    Can be called after `close()` to add more events in the same directory.
    The events will go into a new events file.

    Does nothing if the EventFileWriter was not closed.
    """
    def add_event(self, event) -> None:
        """Adds an event to the event file.

    Args:
      event: An `Event` protocol buffer.
    """
    def flush(self) -> None:
        """Flushes the event file to disk.

    Call this method to make sure that all pending events have been written to
    disk.
    """
    def close(self) -> None:
        """Flushes the event file to disk and close the file.

    Call this method when you do not need the summary writer anymore.
    """
