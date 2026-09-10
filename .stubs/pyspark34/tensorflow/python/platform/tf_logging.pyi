from _typeshed import Incomplete
from tensorflow.python.util.tf_export import tf_export as tf_export

def get_logger():
    '''Return TF logger instance.

  Returns:
    An instance of the Python logging library Logger.

  See Python documentation (https://docs.python.org/3/library/logging.html)
  for detailed API. Below is only a summary.

  The logger has 5 levels of logging from the most serious to the least:

  1. FATAL
  2. ERROR
  3. WARN
  4. INFO
  5. DEBUG

  The logger has the following methods, based on these logging levels:

  1. fatal(msg, *args, **kwargs)
  2. error(msg, *args, **kwargs)
  3. warn(msg, *args, **kwargs)
  4. info(msg, *args, **kwargs)
  5. debug(msg, *args, **kwargs)

  The `msg` can contain string formatting.  An example of logging at the `ERROR`
  level
  using string formating is:

  >>> tf.get_logger().error("The value %d is invalid.", 3)

  You can also specify the logging verbosity.  In this case, the
  WARN level log will not be emitted:

  >>> tf.get_logger().setLevel(ERROR)
  >>> tf.get_logger().warn("This is a warning.")
  '''
def log(level, msg, *args, **kwargs) -> None: ...
def debug(msg, *args, **kwargs) -> None: ...
def error(msg, *args, **kwargs) -> None: ...
def fatal(msg, *args, **kwargs) -> None: ...
def info(msg, *args, **kwargs) -> None: ...
def warn(msg, *args, **kwargs) -> None: ...
def warning(msg, *args, **kwargs) -> None: ...
def TaskLevelStatusMessage(msg) -> None: ...
def flush() -> None: ...
def vlog(level, msg, *args, **kwargs) -> None: ...
def log_every_n(level, msg, n, *args) -> None:
    """Log 'msg % args' at level 'level' once per 'n' times.

  Logs the 1st call, (N+1)st call, (2N+1)st call,  etc.
  Not threadsafe.

  Args:
    level: The level at which to log.
    msg: The message to be logged.
    n: The number of times this should be called before it is logged.
    *args: The args to be substituted into the msg.
  """
def log_first_n(level, msg, n, *args) -> None:
    """Log 'msg % args' at level 'level' only first 'n' times.

  Not threadsafe.

  Args:
    level: The level at which to log.
    msg: The message to be logged.
    n: The number of times this should be called before it is logged.
    *args: The args to be substituted into the msg.
  """
def log_if(level, msg, condition, *args) -> None:
    """Log 'msg % args' at level 'level' only if condition is fulfilled."""
def google2_log_prefix(level, timestamp: Incomplete | None = None, file_and_line: Incomplete | None = None):
    """Assemble a logline prefix using the google2 format."""
def get_verbosity():
    """Return how much logging output will be produced."""
def set_verbosity(v) -> None:
    """Sets the threshold for what messages will be logged."""
