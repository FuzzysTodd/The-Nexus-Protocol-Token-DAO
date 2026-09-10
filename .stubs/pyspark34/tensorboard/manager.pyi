import dataclasses
from tensorboard import version as version
from tensorboard.util import tb_logging as tb_logging

@dataclasses.dataclass(frozen=True)
class TensorBoardInfo:
    """Holds the information about a running TensorBoard instance.

    Attributes:
      version: Version of the running TensorBoard.
      start_time: Seconds since epoch.
      pid: ID of the process running TensorBoard.
      port: Port on which TensorBoard is running.
      path_prefix: Relative prefix to the path, may be empty.
      logdir: Data location used by the TensorBoard server, may be empty.
      db: Database connection used by the TensorBoard server, may be empty.
      cache_key: Opaque, as given by `cache_key` below.
    """
    version: str
    start_time: int
    pid: int
    port: int
    path_prefix: str
    logdir: str
    db: str
    cache_key: str
    def __init__(self, version, start_time, pid, port, path_prefix, logdir, db, cache_key) -> None: ...

def data_source_from_info(info):
    '''Format the data location for the given TensorBoardInfo.

    Args:
      info: A TensorBoardInfo value.

    Returns:
      A human-readable string describing the logdir or database connection
      used by the server: e.g., "logdir /tmp/logs".
    '''
def cache_key(working_directory, arguments, configure_kwargs):
    """Compute a `TensorBoardInfo.cache_key` field.

    The format returned by this function is opaque. Clients may only
    inspect it by comparing it for equality with other results from this
    function.

    Args:
      working_directory: The directory from which TensorBoard was launched
        and relative to which paths like `--logdir` and `--db` are
        resolved.
      arguments: The command-line args to TensorBoard, as `sys.argv[1:]`.
        Should be a list (or tuple), not an unparsed string. If you have a
        raw shell command, use `shlex.split` before passing it to this
        function.
      configure_kwargs: A dictionary of additional argument values to
        override the textual `arguments`, with the same semantics as in
        `tensorboard.program.TensorBoard.configure`. May be an empty
        dictionary.

    Returns:
      A string such that if two (prospective or actual) TensorBoard
      invocations have the same cache key then it is safe to use one in
      place of the other. The converse is not guaranteed: it is often safe
      to change the order of TensorBoard arguments, or to explicitly set
      them to their default values, or to move them between `arguments`
      and `configure_kwargs`, but such invocations may yield distinct
      cache keys.
    """
def write_info_file(tensorboard_info) -> None:
    """Write TensorBoardInfo to the current process's info file.

    This should be called by `main` once the server is ready. When the
    server shuts down, `remove_info_file` should be called.

    Args:
      tensorboard_info: A valid `TensorBoardInfo` object.

    Raises:
      ValueError: If any field on `info` is not of the correct type.
    """
def remove_info_file() -> None:
    """Remove the current process's TensorBoardInfo file, if it exists.

    If the file does not exist, no action is taken and no error is
    raised.
    """
def get_all():
    """Return TensorBoardInfo values for running TensorBoard processes.

    This function may not provide a perfect snapshot of the set of running
    processes. Its result set may be incomplete if the user has cleaned
    their /tmp/ directory while TensorBoard processes are running. It may
    contain extraneous entries if TensorBoard processes exited uncleanly
    (e.g., with SIGKILL or SIGQUIT).

    Entries in the info directory that do not represent valid
    `TensorBoardInfo` values will be silently ignored.

    Returns:
      A fresh list of `TensorBoardInfo` objects.
    """

@dataclasses.dataclass(frozen=True)
class StartReused:
    """Possible return value of the `start` function.

    Indicates that a call to `start` was compatible with an existing
    TensorBoard process, which can be reused according to the provided
    info.

    Attributes:
      info: A `TensorBoardInfo` object.
    """
    info: TensorBoardInfo
    def __init__(self, info) -> None: ...

@dataclasses.dataclass(frozen=True)
class StartLaunched:
    """Possible return value of the `start` function.

    Indicates that a call to `start` successfully launched a new
    TensorBoard process, which is available with the provided info.

    Attributes:
      info: A `TensorBoardInfo` object.
    """
    info: TensorBoardInfo
    def __init__(self, info) -> None: ...

@dataclasses.dataclass(frozen=True)
class StartFailed:
    """Possible return value of the `start` function.

    Indicates that a call to `start` tried to launch a new TensorBoard
    instance, but the subprocess exited with the given exit code and
    output streams. (If the contents of the output streams are no longer
    available---e.g., because the user has emptied /tmp/---then the
    corresponding values will be `None`.)

    Attributes:
      exit_code: As `Popen.returncode` (negative for signal).
      stdout: Error message to stdout if the stream could not be read.
      stderr: Error message to stderr if the stream could not be read.
    """
    exit_code: int
    stdout: str | None
    stderr: str | None
    def __init__(self, exit_code, stdout, stderr) -> None: ...

@dataclasses.dataclass(frozen=True)
class StartExecFailed:
    """Possible return value of the `start` function.

    Indicates that a call to `start` failed to invoke the subprocess.

    Attributes:
      os_error: `OSError` due to `Popen` invocation.
      explicit_binary: If the TensorBoard executable was chosen via the
        `TENSORBOARD_BINARY` environment variable, then this field contains
        the path to that binary; otherwise `None`.
    """
    os_error: OSError
    explicit_binary: str | None
    def __init__(self, os_error, explicit_binary) -> None: ...

@dataclasses.dataclass(frozen=True)
class StartTimedOut:
    """Possible return value of the `start` function.

    Indicates that a call to `start` launched a TensorBoard process, but
    that process neither exited nor wrote its info file within the allowed
    timeout period. The process may still be running under the included
    PID.

    Attributes:
      pid: ID of the process running TensorBoard.
    """
    pid: int
    def __init__(self, pid) -> None: ...

def start(arguments, timeout=...):
    """Start a new TensorBoard instance, or reuse a compatible one.

    If the cache key determined by the provided arguments and the current
    working directory (see `cache_key`) matches the cache key of a running
    TensorBoard process (see `get_all`), that process will be reused.

    Otherwise, a new TensorBoard process will be spawned with the provided
    arguments, using the `tensorboard` binary from the system path.

    Args:
      arguments: List of strings to be passed as arguments to
        `tensorboard`. (If you have a raw command-line string, see
        `shlex.split`.)
      timeout: `datetime.timedelta` object describing how long to wait for
        the subprocess to initialize a TensorBoard server and write its
        `TensorBoardInfo` file. If the info file is not written within
        this time period, `start` will assume that the subprocess is stuck
        in a bad state, and will give up on waiting for it and return a
        `StartTimedOut` result. Note that in such a case the subprocess
        will not be killed. Default value is 60 seconds.

    Returns:
      A `StartReused`, `StartLaunched`, `StartFailed`, or `StartTimedOut`
      object.
    """
