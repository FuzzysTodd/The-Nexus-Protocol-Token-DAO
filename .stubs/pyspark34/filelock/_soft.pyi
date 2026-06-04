from ._api import BaseFileLock

__all__ = ['SoftFileLock']

class SoftFileLock(BaseFileLock):
    """Simply watches the existence of the lock file."""
