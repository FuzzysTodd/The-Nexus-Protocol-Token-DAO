import io
import os
import typing as t
from . import formatting as formatting, termui as termui, utils as utils
from .core import BaseCommand as BaseCommand
from _typeshed import Incomplete
from types import TracebackType

class EchoingStdin:
    def __init__(self, input: t.BinaryIO, output: t.BinaryIO) -> None: ...
    def __getattr__(self, x: str) -> t.Any: ...
    def read(self, n: int = -1) -> bytes: ...
    def read1(self, n: int = -1) -> bytes: ...
    def readline(self, n: int = -1) -> bytes: ...
    def readlines(self) -> t.List[bytes]: ...
    def __iter__(self) -> t.Iterator[bytes]: ...

class _NamedTextIOWrapper(io.TextIOWrapper):
    def __init__(self, buffer: t.BinaryIO, name: str, mode: str, **kwargs: t.Any) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def mode(self) -> str: ...

def make_input_stream(input: str | bytes | t.IO[t.Any] | None, charset: str) -> t.BinaryIO: ...

class Result:
    """Holds the captured result of an invoked CLI script."""
    runner: Incomplete
    stdout_bytes: Incomplete
    stderr_bytes: Incomplete
    return_value: Incomplete
    exit_code: Incomplete
    exception: Incomplete
    exc_info: Incomplete
    def __init__(self, runner: CliRunner, stdout_bytes: bytes, stderr_bytes: bytes | None, return_value: t.Any, exit_code: int, exception: BaseException | None, exc_info: t.Tuple[t.Type[BaseException], BaseException, TracebackType] | None = None) -> None: ...
    @property
    def output(self) -> str:
        """The (standard) output as unicode string."""
    @property
    def stdout(self) -> str:
        """The standard output as unicode string."""
    @property
    def stderr(self) -> str:
        """The standard error as unicode string."""

class CliRunner:
    """The CLI runner provides functionality to invoke a Click command line
    script for unittesting purposes in a isolated environment.  This only
    works in single-threaded systems without any concurrency as it changes the
    global interpreter state.

    :param charset: the character set for the input and output data.
    :param env: a dictionary with environment variables for overriding.
    :param echo_stdin: if this is set to `True`, then reading from stdin writes
                       to stdout.  This is useful for showing examples in
                       some circumstances.  Note that regular prompts
                       will automatically echo the input.
    :param mix_stderr: if this is set to `False`, then stdout and stderr are
                       preserved as independent streams.  This is useful for
                       Unix-philosophy apps that have predictable stdout and
                       noisy stderr, such that each may be measured
                       independently
    """
    charset: Incomplete
    env: Incomplete
    echo_stdin: Incomplete
    mix_stderr: Incomplete
    def __init__(self, charset: str = 'utf-8', env: t.Mapping[str, str | None] | None = None, echo_stdin: bool = False, mix_stderr: bool = True) -> None: ...
    def get_default_prog_name(self, cli: BaseCommand) -> str:
        '''Given a command object it will return the default program name
        for it.  The default is the `name` attribute or ``"root"`` if not
        set.
        '''
    def make_env(self, overrides: t.Mapping[str, str | None] | None = None) -> t.Mapping[str, str | None]:
        """Returns the environment overrides for invoking a script."""
    def isolation(self, input: str | bytes | t.IO[t.Any] | None = None, env: t.Mapping[str, str | None] | None = None, color: bool = False) -> t.Iterator[t.Tuple[io.BytesIO, io.BytesIO | None]]:
        '''A context manager that sets up the isolation for invoking of a
        command line tool.  This sets up stdin with the given input data
        and `os.environ` with the overrides from the given dictionary.
        This also rebinds some internals in Click to be mocked (like the
        prompt functionality).

        This is automatically done in the :meth:`invoke` method.

        :param input: the input stream to put into sys.stdin.
        :param env: the environment overrides as dictionary.
        :param color: whether the output should contain color codes. The
                      application can still override this explicitly.

        .. versionchanged:: 8.0
            ``stderr`` is opened with ``errors="backslashreplace"``
            instead of the default ``"strict"``.

        .. versionchanged:: 4.0
            Added the ``color`` parameter.
        '''
    def invoke(self, cli: BaseCommand, args: str | t.Sequence[str] | None = None, input: str | bytes | t.IO[t.Any] | None = None, env: t.Mapping[str, str | None] | None = None, catch_exceptions: bool = True, color: bool = False, **extra: t.Any) -> Result:
        """Invokes a command in an isolated environment.  The arguments are
        forwarded directly to the command line script, the `extra` keyword
        arguments are passed to the :meth:`~clickpkg.Command.main` function of
        the command.

        This returns a :class:`Result` object.

        :param cli: the command to invoke
        :param args: the arguments to invoke. It may be given as an iterable
                     or a string. When given as string it will be interpreted
                     as a Unix shell command. More details at
                     :func:`shlex.split`.
        :param input: the input data for `sys.stdin`.
        :param env: the environment overrides.
        :param catch_exceptions: Whether to catch any other exceptions than
                                 ``SystemExit``.
        :param extra: the keyword arguments to pass to :meth:`main`.
        :param color: whether the output should contain color codes. The
                      application can still override this explicitly.

        .. versionchanged:: 8.0
            The result object has the ``return_value`` attribute with
            the value returned from the invoked command.

        .. versionchanged:: 4.0
            Added the ``color`` parameter.

        .. versionchanged:: 3.0
            Added the ``catch_exceptions`` parameter.

        .. versionchanged:: 3.0
            The result object has the ``exc_info`` attribute with the
            traceback if available.
        """
    def isolated_filesystem(self, temp_dir: str | os.PathLike[str] | None = None) -> t.Iterator[str]:
        """A context manager that creates a temporary directory and
        changes the current working directory to it. This isolates tests
        that affect the contents of the CWD to prevent them from
        interfering with each other.

        :param temp_dir: Create the temporary directory under this
            directory. If given, the created directory is not removed
            when exiting.

        .. versionchanged:: 8.0
            Added the ``temp_dir`` parameter.
        """
