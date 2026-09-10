import abc
from _typeshed import Incomplete
from tensorboard.compat.proto import event_pb2 as event_pb2, summary_pb2 as summary_pb2
from tensorboard.summary.writer import event_file_writer as event_file_writer
from tensorboard.util import tensor_util as tensor_util

class Output(abc.ABC, metaclass=abc.ABCMeta):
    """Interface for emitting tensor-formatted summary data.

    Implementations of this interface can be passed to Writer to customize
    how summary data is actually persisted (e.g. to disk, to memory, over
    the network, etc.).

    TODO(#4581): This API should be considered EXPERIMENTAL and subject to
    backwards-incompatible changes without notice.
    """
    @abc.abstractmethod
    def emit_scalar(self, *, plugin_name, tag, data, step, wall_time, tag_metadata: Incomplete | None = None, description: Incomplete | None = None):
        """Emits one scalar data point to this Output.

        Args:
          plugin_name: string name to uniquely identify the type of time series
            (historically associated with a TensorBoard plugin).
          tag: string tag used to uniquely identify this time series.
          data: `np.float32` scalar value for this data point.
          step: `np.int64` scalar step value for this data point.
          wall_time: `float` seconds since the Unix epoch, representing the
            real-world timestamp for this data point.
          tag_metadata: optional bytes containing metadata for this entire time
            series. This should be constant for a given tag; only the first
            value encountered will be used.
          description: optional string description for this entire time series.
            This should be constant for a given tag; only the first value
            encountered will be used.
        """
    @abc.abstractmethod
    def flush(self):
        """Flushes any data that has been buffered."""
    @abc.abstractmethod
    def close(self):
        """Closes the Output and also flushes any buffered data."""

class DirectoryOutput(Output):
    """Outputs summary data by writing event files to a log directory.

    TODO(#4581): This API should be considered EXPERIMENTAL and subject to
    backwards-incompatible changes without notice.
    """
    def __init__(self, path) -> None:
        """Creates a `DirectoryOutput` for the given path."""
    def emit_scalar(self, *, plugin_name, tag, data, step, wall_time, tag_metadata: Incomplete | None = None, description: Incomplete | None = None) -> None:
        """See `Output`."""
    def flush(self) -> None:
        """See `Output`."""
    def close(self) -> None:
        """See `Output`."""
