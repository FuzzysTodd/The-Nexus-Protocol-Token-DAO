from _typeshed import Incomplete
from tempfile import TemporaryDirectory

class NamedFileInTemporaryDirectory:
    file: Incomplete
    def __init__(self, filename, mode: str = 'w+b', bufsize: int = -1, add_to_syspath: bool = False, **kwds) -> None:
        """
        Open a file named `filename` in a temporary directory.

        This context manager is preferred over `NamedTemporaryFile` in
        stdlib `tempfile` when one needs to reopen the file.

        Arguments `mode` and `bufsize` are passed to `open`.
        Rest of the arguments are passed to `TemporaryDirectory`.

        """
    def cleanup(self) -> None: ...
    __del__ = cleanup
    def __enter__(self): ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class TemporaryWorkingDirectory(TemporaryDirectory):
    """
    Creates a temporary directory and sets the cwd to that directory.
    Automatically reverts to previous cwd upon cleanup.
    Usage example:

        with TemporaryWorkingDirectory() as tmpdir:
            ...
    """
    old_wd: Incomplete
    def __enter__(self): ...
    def __exit__(self, exc: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None): ...
