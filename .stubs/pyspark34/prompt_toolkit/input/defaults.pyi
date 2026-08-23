from .base import Input, PipeInput
from typing import ContextManager, TextIO

__all__ = ['create_input', 'create_pipe_input']

def create_input(stdin: TextIO | None = None, always_prefer_tty: bool = False) -> Input:
    """
    Create the appropriate `Input` object for the current os/environment.

    :param always_prefer_tty: When set, if `sys.stdin` is connected to a Unix
        `pipe`, check whether `sys.stdout` or `sys.stderr` are connected to a
        pseudo terminal. If so, open the tty for reading instead of reading for
        `sys.stdin`. (We can open `stdout` or `stderr` for reading, this is how
        a `$PAGER` works.)
    """
def create_pipe_input() -> ContextManager[PipeInput]:
    """
    Create an input pipe.
    This is mostly useful for unit testing.

    Usage::

        with create_pipe_input() as input:
            input.send_text('inputdata')

    Breaking change: In prompt_toolkit 3.0.28 and earlier, this was returning
    the `PipeInput` directly, rather than through a context manager.
    """
