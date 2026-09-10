from tensorflow.python.util import tf_decorator as tf_decorator
from tensorflow.python.util.tf_export import tf_export as tf_export

def is_traceback_filtering_enabled():
    """Check whether traceback filtering is currently enabled.

  See also `tf.debugging.enable_traceback_filtering()` and
  `tf.debugging.disable_traceback_filtering()`. Note that filtering out
  internal frames from the tracebacks of exceptions raised by TensorFlow code
  is the default behavior.

  Returns:
    True if traceback filtering is enabled
    (e.g. if `tf.debugging.enable_traceback_filtering()` was called),
    and False otherwise (e.g. if `tf.debugging.disable_traceback_filtering()`
    was called).
  """
def enable_traceback_filtering() -> None:
    """Enable filtering out TensorFlow-internal frames in exception stack traces.

  Raw TensorFlow stack traces involve many internal frames, which can be
  challenging to read through, while not being actionable for end users.
  By default, TensorFlow filters internal frames in most exceptions that it
  raises, to keep stack traces short, readable, and focused on what's
  actionable for end users (their own code).

  If you have previously disabled traceback filtering via
  `tf.debugging.disable_traceback_filtering()`, you can re-enable it via
  `tf.debugging.enable_traceback_filtering()`.

  Raises:
    RuntimeError: If Python version is not at least 3.7.
  """
def disable_traceback_filtering() -> None:
    """Disable filtering out TensorFlow-internal frames in exception stack traces.

  Raw TensorFlow stack traces involve many internal frames, which can be
  challenging to read through, while not being actionable for end users.
  By default, TensorFlow filters internal frames in most exceptions that it
  raises, to keep stack traces short, readable, and focused on what's
  actionable for end users (their own code).

  Calling `tf.debugging.disable_traceback_filtering` disables this filtering
  mechanism, meaning that TensorFlow exceptions stack traces will include
  all frames, in particular TensorFlow-internal ones.

  **If you are debugging a TensorFlow-internal issue, you need to call
  `tf.debugging.disable_traceback_filtering`**.
  To re-enable traceback filtering afterwards, you can call
  `tf.debugging.enable_traceback_filtering()`.
  """
def include_frame(fname): ...
def filter_traceback(fn):
    """Decorator to filter out TF-internal stack trace frames in exceptions.

  Raw TensorFlow stack traces involve many internal frames, which can be
  challenging to read through, while not being actionable for end users.
  By default, TensorFlow filters internal frames in most exceptions that it
  raises, to keep stack traces short, readable, and focused on what's
  actionable for end users (their own code).

  Arguments:
    fn: The function or method to decorate. Any exception raised within the
      function will be reraised with its internal stack trace frames filtered
      out.

  Returns:
    Decorated function or method.
  """
