import threading
from _typeshed import Incomplete
from tensorboard.compat import tf as tf
from tensorboard.compat.proto import event_pb2 as event_pb2
from tensorboard.summary.writer.record_writer import RecordWriter as RecordWriter

class AtomicCounter:
    def __init__(self, initial_value) -> None: ...
    def get(self): ...

class EventFileWriter:
    """Writes `Event` protocol buffers to an event file.

    The `EventFileWriter` class creates an event file in the specified
    directory, and asynchronously writes Event protocol buffers to the
    file. The Event file is encoded using the tfrecord format, which is
    similar to RecordIO.
    """
    def __init__(self, logdir, max_queue_size: int = 10, flush_secs: int = 120, filename_suffix: str = '') -> None:
        """Creates a `EventFileWriter` and an event file to write to.

        On construction the summary writer creates a new event file in `logdir`.
        This event file will contain `Event` protocol buffers, which are written to
        disk via the add_event method.
        The other arguments to the constructor control the asynchronous writes to
        the event file:

        Args:
          logdir: A string. Directory where event file will be written.
          max_queue_size: Integer. Size of the queue for pending events and summaries.
          flush_secs: Number. How often, in seconds, to flush the
            pending events and summaries to disk.
        """
    def get_logdir(self):
        """Returns the directory where event file will be written."""
    def add_event(self, event) -> None:
        """Adds an event to the event file.

        Args:
          event: An `Event` protocol buffer.
        """
    def flush(self) -> None:
        """Flushes the event file to disk.

        Call this method to make sure that all pending events have been
        written to disk.
        """
    def close(self) -> None:
        """Performs a final flush of the event file to disk, stops the
        write/flush worker and closes the file.

        Call this method when you do not need the summary writer
        anymore.
        """

class _AsyncWriter:
    """Writes bytes to a file."""
    def __init__(self, record_writer, max_queue_size: int = 20, flush_secs: int = 120) -> None:
        """Writes bytes to a file asynchronously. An instance of this class
        holds a queue to keep the incoming data temporarily. Data passed to the
        `write` function will be put to the queue and the function returns
        immediately. This class also maintains a thread to write data in the
        queue to disk. The first initialization parameter is an instance of
        `tensorboard.summary.record_writer` which computes the CRC checksum and
        then write the combined result to the disk. So we use an async approach
        to improve performance.

        Args:
            record_writer: A RecordWriter instance
            max_queue_size: Integer. Size of the queue for pending bytestrings.
            flush_secs: Number. How often, in seconds, to flush the
                pending bytestrings to disk.
        """
    def write(self, bytestring) -> None:
        """Enqueue the given bytes to be written asychronously."""
    def flush(self) -> None:
        """Write all the enqueued bytestring before this flush call to disk.

        Block until all the above bytestring are written.
        """
    def close(self) -> None:
        """Closes the underlying writer, flushing any pending writes first."""

class _AsyncWriterThread(threading.Thread):
    """Thread that processes asynchronous writes for _AsyncWriter."""
    daemon: bool
    exception: Incomplete
    def __init__(self, queue, record_writer, flush_secs) -> None:
        """Creates an _AsyncWriterThread.

        Args:
          queue: A Queue from which to dequeue data.
          record_writer: An instance of record_writer writer.
          flush_secs: How often, in seconds, to flush the
            pending file to disk.
        """
    def stop(self) -> None: ...
    def run(self) -> None: ...
