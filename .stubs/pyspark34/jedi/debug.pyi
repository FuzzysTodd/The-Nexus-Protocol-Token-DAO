from _typeshed import Incomplete
from collections.abc import Generator
from typing import Callable

class Fore:
    RED: str
    GREEN: str
    YELLOW: str
    MAGENTA: str
    RESET: str
    BLUE: str

NOTICE: Incomplete
WARNING: Incomplete
SPEED: Incomplete
enable_speed: bool
enable_warning: bool
enable_notice: bool
debug_function: Callable[[str, str], None] | None

def reset_time() -> None: ...
def increase_indent(func):
    """Decorator for makin """
def increase_indent_cm(title: Incomplete | None = None, color: str = 'MAGENTA') -> Generator[None, None, None]: ...
def dbg(message, *args, color: str = 'GREEN') -> None:
    """ Looks at the stack, to see if a debug message should be printed. """
def warning(message, *args, format: bool = True) -> None: ...
def speed(name) -> None: ...
def print_to_stdout(color, str_out) -> None:
    """
    The default debug function that prints to standard out.

    :param str color: A string that is an attribute of ``colorama.Fore``.
    """
