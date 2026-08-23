from _typeshed import Incomplete
from errno import EINTR

__all__ = ['ZMQBaseError', 'ZMQBindError', 'ZMQError', 'NotDone', 'ContextTerminated', 'InterruptedSystemCall', 'Again', 'ZMQVersionError']

class ZMQBaseError(Exception):
    """Base exception class for 0MQ errors in Python."""

class ZMQError(ZMQBaseError):
    """Wrap an errno style error.

    Parameters
    ----------
    errno : int
        The ZMQ errno or None.  If None, then ``zmq_errno()`` is called and
        used.
    msg : string
        Description of the error or None.
    """
    errno: int | None
    strerror: Incomplete
    def __init__(self, errno: int | None = None, msg: str | None = None) -> None:
        """Wrap an errno style error.

        Parameters
        ----------
        errno : int
            The ZMQ errno or None.  If None, then ``zmq_errno()`` is called and
            used.
        msg : string
            Description of the error or None.
        """

class ZMQBindError(ZMQBaseError):
    """An error for ``Socket.bind_to_random_port()``.

    See Also
    --------
    .Socket.bind_to_random_port
    """
class NotDone(ZMQBaseError):
    """Raised when timeout is reached while waiting for 0MQ to finish with a Message

    See Also
    --------
    .MessageTracker.wait : object for tracking when ZeroMQ is done
    """

class ContextTerminated(ZMQError):
    """Wrapper for zmq.ETERM

    .. versionadded:: 13.0
    """
    def __init__(self, errno: str = 'ignored', msg: str = 'ignored') -> None: ...

class Again(ZMQError):
    """Wrapper for zmq.EAGAIN

    .. versionadded:: 13.0
    """
    def __init__(self, errno: str = 'ignored', msg: str = 'ignored') -> None: ...

class InterruptedSystemCall(ZMQError, InterruptedError):
    """Wrapper for EINTR

    This exception should be caught internally in pyzmq
    to retry system calls, and not propagate to the user.

    .. versionadded:: 14.7
    """
    errno = EINTR
    def __init__(self, errno: str = 'ignored', msg: str = 'ignored') -> None: ...

class ZMQVersionError(NotImplementedError):
    """Raised when a feature is not provided by the linked version of libzmq.

    .. versionadded:: 14.2
    """
    min_version: Incomplete
    msg: Incomplete
    version: Incomplete
    def __init__(self, min_version: str, msg: str = 'Feature') -> None: ...
