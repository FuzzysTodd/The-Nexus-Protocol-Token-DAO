from _typeshed import Incomplete
from inspect import Signature
from typing import Any

def get_logger() -> Any:
    """An entry point of the plug-in and return the usage logger."""

class PandasOnSparkUsageLogger:
    """
    The reference implementation of usage logger.

    The usage logger needs to provide the following methods:

        - log_success(self, class_name, name, duration, signature=None)
        - log_failure(self, class_name, name, ex, duration, signature=None)
        - log_missing(self, class_name, name, is_deprecated=False, signature=None)
    """
    logger: Incomplete
    def __init__(self) -> None: ...
    def log_success(self, class_name: str, name: str, duration: float, signature: Signature | None = None) -> None:
        """
        Log the function or property call is successfully finished.

        :param class_name: the target class name
        :param name: the target function or property name
        :param duration: the duration to finish the function or property call
        :param signature: the signature if the target is a function, else None
        """
    def log_failure(self, class_name: str, name: str, ex: Exception, duration: float, signature: Signature | None = None) -> None:
        """
        Log the function or property call failed.

        :param class_name: the target class name
        :param name: the target function or property name
        :param ex: the exception causing the failure
        :param duration: the duration until the function or property call fails
        :param signature: the signature if the target is a function, else None
        """
    def log_missing(self, class_name: str, name: str, is_deprecated: bool = False, signature: Signature | None = None) -> None:
        """
        Log the missing or deprecated function or property is called.

        :param class_name: the target class name
        :param name: the target function or property name
        :param is_deprecated: True if the function or property is marked as deprecated
        :param signature: the original function signature if the target is a function, else None
        """
