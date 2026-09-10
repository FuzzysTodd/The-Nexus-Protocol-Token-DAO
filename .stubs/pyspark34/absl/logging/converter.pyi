from _typeshed import Incomplete

STANDARD_CRITICAL: Incomplete
STANDARD_ERROR: Incomplete
STANDARD_WARNING: Incomplete
STANDARD_INFO: Incomplete
STANDARD_DEBUG: Incomplete
ABSL_FATAL: int
ABSL_ERROR: int
ABSL_WARNING: int
ABSL_WARN: int
ABSL_INFO: int
ABSL_DEBUG: int
ABSL_LEVELS: Incomplete
ABSL_NAMES: Incomplete
ABSL_TO_STANDARD: Incomplete
STANDARD_TO_ABSL: Incomplete

def get_initial_for_level(level):
    """Gets the initial that should start the log line for the given level.

  It returns:

  * ``'I'`` when: ``level < STANDARD_WARNING``.
  * ``'W'`` when: ``STANDARD_WARNING <= level < STANDARD_ERROR``.
  * ``'E'`` when: ``STANDARD_ERROR <= level < STANDARD_CRITICAL``.
  * ``'F'`` when: ``level >= STANDARD_CRITICAL``.

  Args:
    level: int, a Python standard logging level.

  Returns:
    The first initial as it would be logged by the C++ logging module.
  """
def absl_to_cpp(level):
    """Converts an absl log level to a cpp log level.

  Args:
    level: int, an absl.logging level.

  Raises:
    TypeError: Raised when level is not an integer.

  Returns:
    The corresponding integer level for use in Abseil C++.
  """
def absl_to_standard(level):
    """Converts an integer level from the absl value to the standard value.

  Args:
    level: int, an absl.logging level.

  Raises:
    TypeError: Raised when level is not an integer.

  Returns:
    The corresponding integer level for use in standard logging.
  """
def string_to_standard(level):
    """Converts a string level to standard logging level value.

  Args:
    level: str, case-insensitive ``'debug'``, ``'info'``, ``'warning'``,
        ``'error'``, ``'fatal'``.

  Returns:
    The corresponding integer level for use in standard logging.
  """
def standard_to_absl(level):
    """Converts an integer level from the standard value to the absl value.

  Args:
    level: int, a Python standard logging level.

  Raises:
    TypeError: Raised when level is not an integer.

  Returns:
    The corresponding integer level for use in absl logging.
  """
def standard_to_cpp(level):
    """Converts an integer level from the standard value to the cpp value.

  Args:
    level: int, a Python standard logging level.

  Raises:
    TypeError: Raised when level is not an integer.

  Returns:
    The corresponding integer level for use in cpp logging.
  """
