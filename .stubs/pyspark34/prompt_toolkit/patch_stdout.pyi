from _typeshed import Incomplete
from typing import Generator, TextIO

__all__ = ['patch_stdout', 'StdoutProxy']

def patch_stdout(raw: bool = False) -> Generator[None, None, None]:
    """
    Replace `sys.stdout` by an :class:`_StdoutProxy` instance.

    Writing to this proxy will make sure that the text appears above the
    prompt, and that it doesn't destroy the output from the renderer.  If no
    application is curring, the behaviour should be identical to writing to
    `sys.stdout` directly.

    Warning: If a new event loop is installed using `asyncio.set_event_loop()`,
        then make sure that the context manager is applied after the event loop
        is changed. Printing to stdout will be scheduled in the event loop
        that's active when the context manager is created.

    :param raw: (`bool`) When True, vt100 terminal escape sequences are not
                removed/escaped.
    """

class _Done:
    """Sentinel value for stopping the stdout proxy."""

class StdoutProxy:
    """
    File-like object, which prints everything written to it, output above the
    current application/prompt. This class is compatible with other file
    objects and can be used as a drop-in replacement for `sys.stdout` or can
    for instance be passed to `logging.StreamHandler`.

    The current application, above which we print, is determined by looking
    what application currently runs in the `AppSession` that is active during
    the creation of this instance.

    This class can be used as a context manager.

    In order to avoid having to repaint the prompt continuously for every
    little write, a short delay of `sleep_between_writes` seconds will be added
    between writes in order to bundle many smaller writes in a short timespan.
    """
    sleep_between_writes: Incomplete
    raw: Incomplete
    app_session: Incomplete
    closed: bool
    def __init__(self, sleep_between_writes: float = 0.2, raw: bool = False) -> None: ...
    def __enter__(self) -> StdoutProxy: ...
    def __exit__(self, *args: object) -> None: ...
    def close(self) -> None:
        """
        Stop `StdoutProxy` proxy.

        This will terminate the write thread, make sure everything is flushed
        and wait for the write thread to finish.
        """
    def write(self, data: str) -> int: ...
    def flush(self) -> None:
        """
        Flush buffered output.
        """
    @property
    def original_stdout(self) -> TextIO: ...
    def fileno(self) -> int: ...
    def isatty(self) -> bool: ...
    @property
    def encoding(self) -> str: ...
    @property
    def errors(self) -> str: ...
