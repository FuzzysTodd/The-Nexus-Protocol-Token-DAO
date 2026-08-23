from .base import Output
from typing import TextIO

__all__ = ['create_output']

def create_output(stdout: TextIO | None = None, always_prefer_tty: bool = False) -> Output:
    """
    Return an :class:`~prompt_toolkit.output.Output` instance for the command
    line.

    :param stdout: The stdout object
    :param always_prefer_tty: When set, look for `sys.stderr` if `sys.stdout`
        is not a TTY. Useful if `sys.stdout` is redirected to a file, but we
        still want user input and output on the terminal.

        By default, this is `False`. If `sys.stdout` is not a terminal (maybe
        it's redirected to a file), then a `PlainTextOutput` will be returned.
        That way, tools like `print_formatted_text` will write plain text into
        that file.
    """
