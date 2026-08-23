import threading
from _typeshed import Incomplete
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.util import compat as compat

class EventFileWriter:
    """Writes `Event` protocol buffers to an event file.

  The `EventFileWriter` class creates an event file in the specified directory,
  and asynchronously writes Event protocol buffers to the file. The Event file
  is encoded using the tfrecord format, which is similar to RecordIO.

  This class is not thread-safe.
  """
    def __init__(self, logdir, max_queue: int = 10, flush_secs: int = 120, filename_suffix: Incomplete | None = None) -> None:
        """Creates a `EventFileWriter` and an event file to write to.

    On construction the summary writer creates a new event file in `logdir`.
    This event file will contain `Event` protocol buffers, which are written to
    disk via the add_event method.

    The other arguments to the constructor control the asynchronous writes to
    the event file:

    *  `flush_secs`: How often, in seconds, to flush the added summaries
       and events to disk.
    *  `max_queue`: Maximum number of summaries or events pending to be
       written to disk before one of the 'add' calls block.

    Args:
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

class _EventLoggerThread(threading.Thread):
    """Thread that logs events."""
    daemon: bool
    failure_exc_info: Incomplete
    def __init__(self, queue, ev_writer, flush_secs, flush_complete, flush_sentinel, close_sentinel) -> None:
        """Creates an _EventLoggerThread.

    Args:
      queue: A CloseableQueue from which to dequeue events. The queue will be
        closed just before the thread exits, whether due to `close_sentinel` or
        any exception raised in the writing loop.
      ev_writer: An event writer. Used to log brain events for
        the visualizer.
      flush_secs: How often, in seconds, to flush the
        pending file to disk.
      flush_complete: A threading.Event that will be set whenever a flush
        operation requested via `flush_sentinel` has been completed.
      flush_sentinel: A sentinel element in queue that tells this thread to
        flush the writer and mark the current flush operation complete.
      close_sentinel: A sentinel element in queue that tells this thread to
        terminate and close the queue.
    """
    def run(self) -> None: ...

class CloseableQueue:
    """Stripped-down fork of the standard library Queue that is closeable."""
    def __init__(self, maxsize: int = 0) -> None:
        """Create a queue object with a given maximum size.

    Args:
      maxsize: int size of queue. If <= 0, the queue size is infinite.
    """
    def get(self):
        """Remove and return an item from the queue.

    If the queue is empty, blocks until an item is available.

    Returns:
      an item from the queue
    """
    def put(self, item) -> None:
        """Put an item into the queue.

    If the queue is closed, fails immediately.

    If the queue is full, blocks until space is available or until the queue
    is closed by a call to close(), at which point this call fails.

    Args:
      item: an item to add to the queue

    Raises:
      QueueClosedError: if insertion failed because the queue is closed
    """
    def close(self) -> None:
        """Closes the queue, causing any pending or future `put()` calls to fail."""

class QueueClosedError(Exception):
    """Raised when CloseableQueue.put() fails because the queue is closed."""
