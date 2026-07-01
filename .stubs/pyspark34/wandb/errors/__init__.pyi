from _typeshed import Incomplete

__all__ = ['Error', 'CommError', 'AuthenticationError', 'UsageError', 'UnsupportedError']

class Error(Exception):
    """Base W&B Error."""
    message: Incomplete
    context: Incomplete
    def __init__(self, message, context: dict | None = None) -> None: ...

class CommError(Error):
    """Error communicating with W&B servers."""
    exc: Incomplete
    message: Incomplete
    def __init__(self, msg, exc: Incomplete | None = None) -> None: ...

class AuthenticationError(CommError):
    """Raised when authentication fails."""
class UsageError(Error):
    """Raised when an invalid usage of the SDK API is detected."""
class UnsupportedError(UsageError):
    """Raised when trying to use a feature that is not supported."""
