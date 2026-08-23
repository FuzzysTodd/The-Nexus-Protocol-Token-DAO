from _typeshed import Incomplete

class Transaction:
    """Filesystem transaction write context

    Gathers files for deferred commit or discard, so that several write
    operations can be finalized semi-atomically. This works by having this
    instance as the ``.transaction`` attribute of the given filesystem
    """
    fs: Incomplete
    files: Incomplete
    def __init__(self, fs) -> None:
        """
        Parameters
        ----------
        fs: FileSystem instance
        """
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None:
        """End transaction and commit, if exit is not due to exception"""
    def start(self) -> None:
        """Start a transaction on this FileSystem"""
    def complete(self, commit: bool = True) -> None:
        """Finish transaction: commit or discard all deferred files"""

class FileActor:
    files: Incomplete
    def __init__(self) -> None: ...
    def commit(self) -> None: ...
    def discard(self) -> None: ...
    def append(self, f) -> None: ...

class DaskTransaction(Transaction):
    files: Incomplete
    def __init__(self, fs) -> None:
        """
        Parameters
        ----------
        fs: FileSystem instance
        """
    def complete(self, commit: bool = True) -> None:
        """Finish transaction: commit or discard all deferred files"""
