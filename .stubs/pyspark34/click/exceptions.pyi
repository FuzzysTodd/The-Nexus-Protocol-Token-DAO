import typing as t
from ._compat import get_text_stderr as get_text_stderr
from .core import Command as Command, Context as Context, Parameter as Parameter
from .utils import echo as echo, format_filename as format_filename
from _typeshed import Incomplete

class ClickException(Exception):
    """An exception that Click can handle and show to the user."""
    exit_code: int
    message: Incomplete
    def __init__(self, message: str) -> None: ...
    def format_message(self) -> str: ...
    def show(self, file: t.IO[t.Any] | None = None) -> None: ...

class UsageError(ClickException):
    """An internal exception that signals a usage error.  This typically
    aborts any further handling.

    :param message: the error message to display.
    :param ctx: optionally the context that caused this error.  Click will
                fill in the context automatically in some situations.
    """
    exit_code: int
    ctx: Incomplete
    cmd: Incomplete
    def __init__(self, message: str, ctx: Context | None = None) -> None: ...
    def show(self, file: t.IO[t.Any] | None = None) -> None: ...

class BadParameter(UsageError):
    """An exception that formats out a standardized error message for a
    bad parameter.  This is useful when thrown from a callback or type as
    Click will attach contextual information to it (for instance, which
    parameter it is).

    .. versionadded:: 2.0

    :param param: the parameter object that caused this error.  This can
                  be left out, and Click will attach this info itself
                  if possible.
    :param param_hint: a string that shows up as parameter name.  This
                       can be used as alternative to `param` in cases
                       where custom validation should happen.  If it is
                       a string it's used as such, if it's a list then
                       each item is quoted and separated.
    """
    param: Incomplete
    param_hint: Incomplete
    def __init__(self, message: str, ctx: Context | None = None, param: Parameter | None = None, param_hint: str | None = None) -> None: ...
    def format_message(self) -> str: ...

class MissingParameter(BadParameter):
    """Raised if click required an option or argument but it was not
    provided when invoking the script.

    .. versionadded:: 4.0

    :param param_type: a string that indicates the type of the parameter.
                       The default is to inherit the parameter type from
                       the given `param`.  Valid values are ``'parameter'``,
                       ``'option'`` or ``'argument'``.
    """
    param_type: Incomplete
    def __init__(self, message: str | None = None, ctx: Context | None = None, param: Parameter | None = None, param_hint: str | None = None, param_type: str | None = None) -> None: ...
    def format_message(self) -> str: ...

class NoSuchOption(UsageError):
    """Raised if click attempted to handle an option that does not
    exist.

    .. versionadded:: 4.0
    """
    option_name: Incomplete
    possibilities: Incomplete
    def __init__(self, option_name: str, message: str | None = None, possibilities: t.Sequence[str] | None = None, ctx: Context | None = None) -> None: ...
    def format_message(self) -> str: ...

class BadOptionUsage(UsageError):
    """Raised if an option is generally supplied but the use of the option
    was incorrect.  This is for instance raised if the number of arguments
    for an option is not correct.

    .. versionadded:: 4.0

    :param option_name: the name of the option being used incorrectly.
    """
    option_name: Incomplete
    def __init__(self, option_name: str, message: str, ctx: Context | None = None) -> None: ...

class BadArgumentUsage(UsageError):
    """Raised if an argument is generally supplied but the use of the argument
    was incorrect.  This is for instance raised if the number of values
    for an argument is not correct.

    .. versionadded:: 6.0
    """

class FileError(ClickException):
    """Raised if a file cannot be opened."""
    ui_filename: Incomplete
    filename: Incomplete
    def __init__(self, filename: str, hint: str | None = None) -> None: ...
    def format_message(self) -> str: ...

class Abort(RuntimeError):
    """An internal signalling exception that signals Click to abort."""

class Exit(RuntimeError):
    """An exception that indicates that the application should exit with some
    status code.

    :param code: the status code to exit with.
    """
    exit_code: Incomplete
    def __init__(self, code: int = 0) -> None: ...
