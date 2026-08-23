from _typeshed import Incomplete

def disk_used(path):
    """get the disk usage for the given directory

    Args:
        path (str): path string.

    Returns:
        int corresponding to disk usage in blocks.
    """
def kbytes(text):
    """convert memory text to the corresponding value in kilobytes

    Args:
        text (str): string corresponding to an abbreviation of size.

    Returns:
        int representation of text.

    Examples:
        >>> kbytes('10K')
        10
        >>> 
        >>> kbytes('10G')
        10485760
    """

RM_SUBDIRS_RETRY_TIME: float

def rmtree(path, self: bool = True, ignore_errors: bool = False, onerror: Incomplete | None = None) -> None:
    """remove directories in the given path

    Args:
        path (str): path string of root of directories to delete.
        self (bool, default=True): if False, delete subdirectories, not path.
        ignore_errors (bool, default=False): if True, silently ignore errors.
        onerror (function, default=None): custom error handler.

    Returns:
        None

    Notes:
        If self=False, the directory indicated by path is left in place,
        and its subdirectories are erased. If self=True, path is also removed.

        If ignore_errors=True, errors are ignored. Otherwise, onerror is called
        to handle the error with arguments ``(func, path, exc_info)``, where
        *func* is ``os.listdir``, ``os.remove``, or ``os.rmdir``; *path* is the
        argument to the function that caused it to fail; and *exc_info* is a
        tuple returned by ``sys.exc_info()``. If ignore_errors=False and
        onerror=None, an exception is raised.
    """
