import enum
from _typeshed import Incomplete
from abc import ABC
from typing import NamedTuple

class Outcome(ABC):
    """A sum type describing the outcome of some call.

  Attributes:
    kind: One of Kind.RETURNED or Kind.RAISED respectively indicating that the
      call returned a value or raised an exception.
    return_value: The value returned by the call. Must be present if kind is
      Kind.RETURNED.
    exception: The exception raised by the call. Must be present if kind is
      Kind.RAISED.
  """
    class Kind(enum.Enum):
        """Identifies the general kind of the outcome of some call."""
        RETURNED: Incomplete
        RAISED: Incomplete

class _EasyOutcome(NamedTuple('_EasyOutcome', [('kind', Incomplete), ('return_value', Incomplete), ('exception', Incomplete)]), Outcome):
    """A trivial implementation of Outcome."""

def with_exceptions_logged(behavior, message):
    """Wraps a callable in a try-except that logs any exceptions it raises.

  Args:
    behavior: Any callable.
    message: A string to log if the behavior raises an exception.

  Returns:
    A callable that when executed invokes the given behavior. The returned
      callable takes the same arguments as the given behavior but returns a
      future.Outcome describing whether the given behavior returned a value or
      raised an exception.
  """
def call_logging_exceptions(behavior, message, *args, **kwargs):
    """Calls a behavior in a try-except that logs any exceptions it raises.

  Args:
    behavior: Any callable.
    message: A string to log if the behavior raises an exception.
    *args: Positional arguments to pass to the given behavior.
    **kwargs: Keyword arguments to pass to the given behavior.

  Returns:
    An Outcome describing whether the given behavior returned a value or raised
      an exception.
  """
