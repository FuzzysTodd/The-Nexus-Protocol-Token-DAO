from _typeshed import Incomplete

class FileBaton:
    """A primitive, file-based synchronization utility."""
    lock_file_path: Incomplete
    wait_seconds: Incomplete
    fd: Incomplete
    def __init__(self, lock_file_path, wait_seconds: float = 0.1) -> None:
        """
        Creates a new :class:`FileBaton`.

        Args:
            lock_file_path: The path to the file used for locking.
            wait_seconds: The seconds to periorically sleep (spin) when
                calling ``wait()``.
        """
    def try_acquire(self):
        """
        Tries to atomically create a file under exclusive access.

        Returns:
            True if the file could be created, else False.
        """
    def wait(self) -> None:
        """
        Periodically sleeps for a certain amount until the baton is released.

        The amount of time slept depends on the ``wait_seconds`` parameter
        passed to the constructor.
        """
    def release(self) -> None:
        """Releases the baton and removes its file."""
