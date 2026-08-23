from _typeshed import Incomplete
from keras.utils import keras_logging as keras_logging

INTERACTIVE_LOGGING: Incomplete

def enable_interactive_logging() -> None:
    """Turn on interactive logging.

    When interactive logging is enabled, Keras displays logs via stdout.
    This provides the best experience when using Keras in an interactive
    environment such as a shell or a notebook.
    """
def disable_interactive_logging() -> None:
    """Turn off interactive logging.

    When interactive logging is disabled, Keras sends logs to `absl.logging`.
    This is the best option when using Keras in a non-interactive
    way, such as running a training or inference job on a server.
    """
def is_interactive_logging_enabled():
    """Check if interactive logging is enabled.

    To switch between writing logs to stdout and `absl.logging`, you may use
    `keras.utils.enable_interactive_logging()` and
    `keras.utils.disable_interactie_logging()`.

    Returns:
      Boolean (True if interactive logging is enabled and False otherwise).
    """
def print_msg(message, line_break: bool = True) -> None:
    """Print the message to absl logging or stdout."""
def path_to_string(path):
    """Convert `PathLike` objects to their string representation.

    If given a non-string typed path object, converts it to its string
    representation.

    If the object passed to `path` is not among the above, then it is
    returned unchanged. This allows e.g. passthrough of file objects
    through this function.

    Args:
      path: `PathLike` object that represents a path

    Returns:
      A string representation of the path argument, if Python support exists.
    """
def ask_to_proceed_with_overwrite(filepath):
    """Produces a prompt asking about overwriting a file.

    Args:
        filepath: the path to the file to be overwritten.

    Returns:
        True if we can proceed with overwrite, False otherwise.
    """
