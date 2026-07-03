import abc
from _typeshed import Incomplete

class TimeoutError(Exception):
    """Indicates that a particular call timed out."""
class CancelledError(Exception):
    """Indicates that the computation underlying a Future was cancelled."""

class Future(abc.ABC, metaclass=abc.ABCMeta):
    """A representation of a computation in another control flow.

  Computations represented by a Future may be yet to be begun, may be ongoing,
  or may have already completed.
  """
    @abc.abstractmethod
    def cancel(self):
        """Attempts to cancel the computation.

    This method does not block.

    Returns:
      True if the computation has not yet begun, will not be allowed to take
        place, and determination of both was possible without blocking. False
        under all other circumstances including but not limited to the
        computation's already having begun, the computation's already having
        finished, and the computation's having been scheduled for execution on a
        remote system for which a determination of whether or not it commenced
        before being cancelled cannot be made without blocking.
    """
    @abc.abstractmethod
    def cancelled(self):
        """Describes whether the computation was cancelled.

    This method does not block.

    Returns:
      True if the computation was cancelled any time before its result became
        immediately available. False under all other circumstances including but
        not limited to this object's cancel method not having been called and
        the computation's result having become immediately available.
    """
    @abc.abstractmethod
    def running(self):
        """Describes whether the computation is taking place.

    This method does not block.

    Returns:
      True if the computation is scheduled to take place in the future or is
        taking place now, or False if the computation took place in the past or
        was cancelled.
    """
    @abc.abstractmethod
    def done(self):
        """Describes whether the computation has taken place.

    This method does not block.

    Returns:
      True if the computation is known to have either completed or have been
        unscheduled or interrupted. False if the computation may possibly be
        executing or scheduled to execute later.
    """
    @abc.abstractmethod
    def result(self, timeout: Incomplete | None = None):
        """Accesses the outcome of the computation or raises its exception.

    This method may return immediately or may block.

    Args:
      timeout: The length of time in seconds to wait for the computation to
        finish or be cancelled, or None if this method should block until the
        computation has finished or is cancelled no matter how long that takes.

    Returns:
      The return value of the computation.

    Raises:
      TimeoutError: If a timeout value is passed and the computation does not
        terminate within the allotted time.
      CancelledError: If the computation was cancelled.
      Exception: If the computation raised an exception, this call will raise
        the same exception.
    """
    @abc.abstractmethod
    def exception(self, timeout: Incomplete | None = None):
        """Return the exception raised by the computation.

    This method may return immediately or may block.

    Args:
      timeout: The length of time in seconds to wait for the computation to
        terminate or be cancelled, or None if this method should block until
        the computation is terminated or is cancelled no matter how long that
        takes.

    Returns:
      The exception raised by the computation, or None if the computation did
        not raise an exception.

    Raises:
      TimeoutError: If a timeout value is passed and the computation does not
        terminate within the allotted time.
      CancelledError: If the computation was cancelled.
    """
    @abc.abstractmethod
    def traceback(self, timeout: Incomplete | None = None):
        """Access the traceback of the exception raised by the computation.

    This method may return immediately or may block.

    Args:
      timeout: The length of time in seconds to wait for the computation to
        terminate or be cancelled, or None if this method should block until
        the computation is terminated or is cancelled no matter how long that
        takes.

    Returns:
      The traceback of the exception raised by the computation, or None if the
        computation did not raise an exception.

    Raises:
      TimeoutError: If a timeout value is passed and the computation does not
        terminate within the allotted time.
      CancelledError: If the computation was cancelled.
    """
    @abc.abstractmethod
    def add_done_callback(self, fn):
        """Adds a function to be called at completion of the computation.

    The callback will be passed this Future object describing the outcome of
    the computation.

    If the computation has already completed, the callback will be called
    immediately.

    Args:
      fn: A callable taking this Future object as its single parameter.
    """
