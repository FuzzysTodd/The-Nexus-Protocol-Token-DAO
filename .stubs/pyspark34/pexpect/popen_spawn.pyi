from .exceptions import EOF as EOF
from .spawnbase import PY3 as PY3, SpawnBase as SpawnBase
from .utils import string_types as string_types
from _typeshed import Incomplete

class PopenSpawn(SpawnBase):
    crlf: Incomplete
    proc: Incomplete
    pid: Incomplete
    closed: bool
    def __init__(self, cmd, timeout: int = 30, maxread: int = 2000, searchwindowsize: Incomplete | None = None, logfile: Incomplete | None = None, cwd: Incomplete | None = None, env: Incomplete | None = None, encoding: Incomplete | None = None, codec_errors: str = 'strict', preexec_fn: Incomplete | None = None) -> None: ...
    flag_eof: bool
    def read_nonblocking(self, size, timeout): ...
    def write(self, s) -> None:
        """This is similar to send() except that there is no return value.
        """
    def writelines(self, sequence) -> None:
        """This calls write() for each element in the sequence.

        The sequence can be any iterable object producing strings, typically a
        list of strings. This does not add line separators. There is no return
        value.
        """
    def send(self, s):
        """Send data to the subprocess' stdin.

        Returns the number of bytes written.
        """
    def sendline(self, s: str = ''):
        """Wraps send(), sending string ``s`` to child process, with os.linesep
        automatically appended. Returns number of bytes written. """
    exitstatus: Incomplete
    signalstatus: Incomplete
    terminated: bool
    def wait(self):
        """Wait for the subprocess to finish.

        Returns the exit code.
        """
    def kill(self, sig) -> None:
        """Sends a Unix signal to the subprocess.

        Use constants from the :mod:`signal` module to specify which signal.
        """
    def sendeof(self) -> None:
        """Closes the stdin pipe from the writing end."""
