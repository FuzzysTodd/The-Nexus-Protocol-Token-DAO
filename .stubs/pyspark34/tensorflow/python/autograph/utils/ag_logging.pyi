from _typeshed import Incomplete
from tensorflow.python.util.tf_export import tf_export as tf_export

VERBOSITY_VAR_NAME: str
DEFAULT_VERBOSITY: int
verbosity_level: Incomplete
echo_log_to_stdout: bool

def set_verbosity(level, alsologtostdout: bool = False) -> None:
    """Sets the AutoGraph verbosity level.

  _Debug logging in AutoGraph_

  More verbose logging is useful to enable when filing bug reports or doing
  more in-depth debugging.

  There are two means to control the logging verbosity:

   * The `set_verbosity` function

   * The `AUTOGRAPH_VERBOSITY` environment variable

  `set_verbosity` takes precedence over the environment variable.

  For example:

  ```python
  import os
  import tensorflow as tf

  os.environ['AUTOGRAPH_VERBOSITY'] = '5'
  # Verbosity is now 5

  tf.autograph.set_verbosity(0)
  # Verbosity is now 0

  os.environ['AUTOGRAPH_VERBOSITY'] = '1'
  # No effect, because set_verbosity was already called.
  ```

  Logs entries are output to [absl](https://abseil.io)'s
  [default output](https://abseil.io/docs/python/guides/logging),
  with `INFO` level.
  Logs can be mirrored to stdout by using the `alsologtostdout` argument.
  Mirroring is enabled by default when Python runs in interactive mode.

  Args:
    level: int, the verbosity level; larger values specify increased verbosity;
      0 means no logging. When reporting bugs, it is recommended to set this
      value to a larger number, like 10.
    alsologtostdout: bool, whether to also output log messages to `sys.stdout`.
  """
def trace(*args) -> None:
    """Traces argument information at compilation time.

  `trace` is useful when debugging, and it always executes during the tracing
  phase, that is, when the TF graph is constructed.

  _Example usage_

  ```python
  import tensorflow as tf

  for i in tf.range(10):
    tf.autograph.trace(i)
  # Output: <Tensor ...>
  ```

  Args:
    *args: Arguments to print to `sys.stdout`.
  """
def get_verbosity(): ...
def has_verbosity(level): ...
def error(level, msg, *args, **kwargs) -> None: ...
def log(level, msg, *args, **kwargs) -> None: ...
def warning(msg, *args, **kwargs) -> None: ...
