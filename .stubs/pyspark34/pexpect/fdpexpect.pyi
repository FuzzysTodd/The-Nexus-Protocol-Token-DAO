from .spawnbase import SpawnBase
from _typeshed import Incomplete

__all__ = ['fdspawn']

class fdspawn(SpawnBase):
    """This is like pexpect.spawn but allows you to supply your own open file
    descriptor. For example, you could use it to read through a file looking
    for patterns, or to control a modem or serial device. """
    args: Incomplete
    command: Incomplete
    child_fd: Incomplete
    own_fd: bool
    closed: bool
    name: Incomplete
    use_poll: Incomplete
    def __init__(self, fd, args: Incomplete | None = None, timeout: int = 30, maxread: int = 2000, searchwindowsize: Incomplete | None = None, logfile: Incomplete | None = None, encoding: Incomplete | None = None, codec_errors: str = 'strict', use_poll: bool = False) -> None:
        """This takes a file descriptor (an int) or an object that support the
        fileno() method (returning an int). All Python file-like objects
        support fileno(). """
    def close(self) -> None:
        """Close the file descriptor.

        Calling this method a second time does nothing, but if the file
        descriptor was closed elsewhere, :class:`OSError` will be raised.
        """
    def isalive(self):
        """This checks if the file descriptor is still valid. If :func:`os.fstat`
        does not raise an exception then we assume it is alive. """
    def terminate(self, force: bool = False) -> None:
        """Deprecated and invalid. Just raises an exception."""
    def send(self, s):
        """Write to fd, return number of bytes written"""
    def sendline(self, s):
        """Write to fd with trailing newline, return number of bytes written"""
    def write(self, s) -> None:
        """Write to fd, return None"""
    def writelines(self, sequence) -> None:
        """Call self.write() for each item in sequence"""
    def read_nonblocking(self, size: int = 1, timeout: int = -1):
        """
        Read from the file descriptor and return the result as a string.

        The read_nonblocking method of :class:`SpawnBase` assumes that a call
        to os.read will not block (timeout parameter is ignored). This is not
        the case for POSIX file-like objects such as sockets and serial ports.

        Use :func:`select.select`, timeout is implemented conditionally for
        POSIX systems.

        :param int size: Read at most *size* bytes.
        :param int timeout: Wait timeout seconds for file descriptor to be
            ready to read. When -1 (default), use self.timeout. When 0, poll.
        :return: String containing the bytes read
        """
