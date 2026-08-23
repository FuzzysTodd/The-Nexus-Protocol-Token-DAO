from _typeshed import Incomplete

class ExceptionPexpect(Exception):
    """Base class for all exceptions raised by this module.
    """
    value: Incomplete
    def __init__(self, value) -> None: ...
    def get_trace(self):
        """This returns an abbreviated stack trace with lines that only concern
        the caller. In other words, the stack trace inside the Pexpect module
        is not included. """

class EOF(ExceptionPexpect):
    """Raised when EOF is read from a child.
    This usually means the child has exited."""
class TIMEOUT(ExceptionPexpect):
    """Raised when a read time exceeds the timeout. """
