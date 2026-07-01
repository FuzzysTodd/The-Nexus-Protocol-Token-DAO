from _typeshed import Incomplete

class Writer:
    """Writes summary data for visualization in TensorBoard.

    This class is not thread-safe.

    TODO(#4581): This API should be considered EXPERIMENTAL and subject to
    backwards-incompatible changes without notice.
    """
    def __init__(self, output) -> None:
        """Constructs a Writer.

        Args:
          output: `tensorboard.summary.Output` object, or a string which will be
            interpreted as shorthand for an `Output` of the appropriate type. The
            only currently supported type is `DirectoryOutput`, where the string
            value given here will be used as the directory path.
        """
    def flush(self) -> None:
        """Flushes any buffered data."""
    def close(self) -> None:
        """Closes the writer and prevents further use."""
    def add_scalar(self, tag, data, step, *, wall_time: Incomplete | None = None, description: Incomplete | None = None) -> None:
        """Adds a scalar summary.

        Args:
          tag: string tag used to uniquely identify this time series.
          data: numeric scalar value for this data point. Accepts any value that
            can be converted to a `np.float32` scalar.
          step: integer step value for this data point. Accepts any value that
            can be converted to a `np.int64` scalar.
          wall_time: optional `float` seconds since the Unix epoch, representing
            the real-world timestamp for this data point. Defaults to None in
            which case the current time will be used.
          description: optional string description for this entire time series.
            This should be constant for a given tag; only the first value
            encountered will be used.
        """
