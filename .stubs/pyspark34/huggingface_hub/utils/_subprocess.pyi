import subprocess
from .logging import get_logger as get_logger
from _typeshed import Incomplete
from io import StringIO
from pathlib import Path
from typing import Generator, IO, List, Tuple

logger: Incomplete

def capture_output() -> Generator[StringIO, None, None]:
    '''Capture output that is printed to terminal.

    Taken from https://stackoverflow.com/a/34738440

    Example:
    ```py
    >>> with capture_output() as output:
    ...     print("hello world")
    >>> assert output.getvalue() == "hello world
"
    ```
    '''
def run_subprocess(command: str | List[str], folder: str | Path | None = None, check: bool = True, **kwargs) -> subprocess.CompletedProcess:
    """
    Method to run subprocesses. Calling this will capture the `stderr` and `stdout`,
    please call `subprocess.run` manually in case you would like for them not to
    be captured.

    Args:
        command (`str` or `List[str]`):
            The command to execute as a string or list of strings.
        folder (`str`, *optional*):
            The folder in which to run the command. Defaults to current working
            directory (from `os.getcwd()`).
        check (`bool`, *optional*, defaults to `True`):
            Setting `check` to `True` will raise a `subprocess.CalledProcessError`
            when the subprocess has a non-zero exit code.
        kwargs (`Dict[str]`):
            Keyword arguments to be passed to the `subprocess.run` underlying command.

    Returns:
        `subprocess.CompletedProcess`: The completed process.
    """
def run_interactive_subprocess(command: str | List[str], folder: str | Path | None = None, **kwargs) -> Generator[Tuple[IO[str], IO[str]], None, None]:
    '''Run a subprocess in an interactive mode in a context manager.

    Args:
        command (`str` or `List[str]`):
            The command to execute as a string or list of strings.
        folder (`str`, *optional*):
            The folder in which to run the command. Defaults to current working
            directory (from `os.getcwd()`).
        kwargs (`Dict[str]`):
            Keyword arguments to be passed to the `subprocess.run` underlying command.

    Returns:
        `Tuple[IO[str], IO[str]]`: A tuple with `stdin` and `stdout` to interact
        with the process (input and output are utf-8 encoded).

    Example:
    ```python
    with _interactive_subprocess("git credential-store get") as (stdin, stdout):
        # Write to stdin
        stdin.write("url=hf.co
username=obama
".encode("utf-8"))
        stdin.flush()

        # Read from stdout
        output = stdout.read().decode("utf-8")
    ```
    '''
