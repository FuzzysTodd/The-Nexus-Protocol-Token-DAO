from _typeshed import Incomplete
from typing import Any

LOG_STRING: Incomplete
LOG_STRING_NOCOLOR: str
ERROR_STRING: Incomplete
WARN_STRING: Incomplete
PRINTED_MESSAGES: Incomplete

def termsetup(settings, logger) -> None: ...
def termlog(string: str = '', newline: bool = True, repeat: bool = True, prefix: bool = True) -> None:
    """Log to standard error with formatting.

    Arguments:
        string (str, optional): The string to print
        newline (bool, optional): Print a newline at the end of the string
        repeat (bool, optional): If set to False only prints the string once per process
    """
def termwarn(string: str, **kwargs: Any) -> None: ...
def termerror(string: str, **kwargs: Any) -> None: ...
