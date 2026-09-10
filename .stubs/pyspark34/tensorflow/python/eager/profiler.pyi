from _typeshed import Incomplete
from tensorflow.python.eager import context as context
from tensorflow.python.framework import errors as errors
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.util import compat as compat
from tensorflow.python.util.deprecation import deprecated as deprecated

class ProfilerAlreadyRunningError(Exception): ...
class ProfilerNotRunningError(Exception): ...

def start(options: Incomplete | None = None) -> None:
    """Start profiling.

  Args:
    options: profiler options.

  Raises:
    ProfilerAlreadyRunningError: If another profiling session is running.
  """
def stop():
    """Stop current profiling session and return its result.

  Returns:
    A binary string of tensorflow.tpu.Trace. User can write the string
    to file for offline analysis by tensorboard.

  Raises:
    ProfilerNotRunningError: If there is no active profiling session.
  """
def maybe_create_event_file(logdir) -> None:
    """Create an empty event file if not already exists.

  This event file indicates that we have a plugins/profile/ directory in the
  current logdir.

  Args:
    logdir: log directory.
  """
def save(logdir, result) -> None:
    """Save profile result to TensorBoard logdir.

  Args:
    logdir: log directory read by TensorBoard.
    result: profiling result returned by stop().
  """
def start_profiler_server(port) -> None:
    """Start a profiler grpc server that listens to given port.

  The profiler server will keep the program running even the training finishes.
  Please shutdown the server with CTRL-C. It can be used in both eager mode and
  graph mode. The service defined in
  tensorflow/core/profiler/profiler_service.proto. Please use
  tensorflow/contrib/tpu/profiler/capture_tpu_profile to capture tracable
  file following https://cloud.google.com/tpu/docs/cloud-tpu-tools#capture_trace

  Args:
    port: port profiler server listens to.
  """

class Profiler:
    '''Context-manager eager profiler api.

  Example usage:
  ```python
  with Profiler("/path/to/logdir"):
    # do some work
  ```
  '''
    def __init__(self, logdir) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, typ: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None: ...
