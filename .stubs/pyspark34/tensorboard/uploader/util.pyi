from _typeshed import Incomplete

class RateLimiter:
    """Helper class for rate-limiting using a fixed minimum interval."""
    def __init__(self, interval_secs) -> None:
        """Constructs a RateLimiter that permits a tick() every
        `interval_secs`."""
    def tick(self) -> None:
        """Blocks until it has been at least `interval_secs` since last
        tick()."""

def get_user_config_directory():
    """Returns a platform-specific root directory for user config settings."""
def make_file_with_directories(path, private: bool = False) -> None:
    """Creates a file and its containing directories, if they don't already
    exist.

    If `private` is True, the file will be made private (readable only by the
    current user) and so will the leaf directory. Pre-existing contents of the
    file are not modified.

    Passing `private=True` is not supported on Windows because it doesn't support
    the relevant parts of `os.chmod()`.

    Args:
      path: str, The path of the file to create.
      private: boolean, Whether to make the file and leaf directory readable only
        by the current user.

    Raises:
      RuntimeError: If called on Windows with `private` set to True.
    """
def set_timestamp(pb, seconds_since_epoch) -> None:
    """Sets a `Timestamp` proto message to a floating point UNIX time.

    This is like `pb.FromNanoseconds(int(seconds_since_epoch * 1e9))` but
    without introducing floating-point error.

    Args:
      pb: A `google.protobuf.Timestamp` message to mutate.
      seconds_since_epoch: A `float`, as returned by `time.time`.
    """
def format_time(timestamp_pb, now: Incomplete | None = None):
    '''Converts a `timestamp_pb2.Timestamp` to human-readable string.

    This always includes the absolute date and time, and for recent dates
    may include a relative time like "(just now)" or "(2 hours ago)". It
    should thus be used for ephemeral values. Use `format_time_absolute`
    if the output will be persisted.

    Args:
      timestamp_pb: A `google.protobuf.timestamp_pb2.Timestamp` value to
        convert to string. The input will not be modified.
      now: A `datetime.datetime` object representing the current time,
        used for determining relative times like "just now". Optional;
        defaults to `datetime.datetime.now()`.

    Returns:
      A string suitable for human consumption.
    '''
def format_time_absolute(timestamp_pb):
    '''Converts a `timestamp_pb2.Timestamp` to UTC time string.

    This will always be of the form "2001-02-03T04:05:06Z".

    Args:
      timestamp_pb: A `google.protobuf.timestamp_pb2.Timestamp` value to
        convert to string. The input will not be modified.

    Returns:
      An RFC 3339 date-time string.
    '''
