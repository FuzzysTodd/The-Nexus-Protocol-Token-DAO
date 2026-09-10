from ._api import BaseFileLock

__all__ = ['WindowsFileLock']

class WindowsFileLock(BaseFileLock):
    """Uses the :func:`msvcrt.locking` function to hard lock the lock file on Windows systems."""
