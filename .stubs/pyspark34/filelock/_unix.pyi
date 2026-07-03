from ._api import BaseFileLock

__all__ = ['has_fcntl', 'UnixFileLock']

has_fcntl: bool

class UnixFileLock(BaseFileLock):
    """Uses the :func:`fcntl.flock` to hard lock the lock file on unix systems."""
