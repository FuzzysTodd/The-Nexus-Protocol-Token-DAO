from _typeshed import Incomplete
from pip._internal.utils.misc import enum as enum, rmtree as rmtree
from typing import Any, Generator

logger: Incomplete
tempdir_kinds: Incomplete

def global_tempdir_manager() -> Generator[None, None, None]: ...

class TempDirectoryTypeRegistry:
    """Manages temp directory behavior"""
    def __init__(self) -> None: ...
    def set_delete(self, kind: str, value: bool) -> None:
        """Indicate whether a TempDirectory of the given kind should be
        auto-deleted.
        """
    def get_delete(self, kind: str) -> bool:
        """Get configured auto-delete flag for a given TempDirectory type,
        default True.
        """

def tempdir_registry() -> Generator[TempDirectoryTypeRegistry, None, None]:
    """Provides a scoped global tempdir registry that can be used to dictate
    whether directories should be deleted.
    """

class _Default: ...

class TempDirectory:
    """Helper class that owns and cleans up a temporary directory.

    This class can be used as a context manager or as an OO representation of a
    temporary directory.

    Attributes:
        path
            Location to the created temporary directory
        delete
            Whether the directory should be deleted when exiting
            (when used as a contextmanager)

    Methods:
        cleanup()
            Deletes the temporary directory

    When used as a context manager, if the delete attribute is True, on
    exiting the context the temporary directory is deleted.
    """
    delete: Incomplete
    kind: Incomplete
    ignore_cleanup_errors: Incomplete
    def __init__(self, path: str | None = None, delete: bool | None | _Default = ..., kind: str = 'temp', globally_managed: bool = False, ignore_cleanup_errors: bool = True) -> None: ...
    @property
    def path(self) -> str: ...
    def __enter__(self) -> _T: ...
    def __exit__(self, exc: Any, value: Any, tb: Any) -> None: ...
    def cleanup(self) -> None:
        """Remove the temporary directory created and reset state"""

class AdjacentTempDirectory(TempDirectory):
    """Helper class that creates a temporary directory adjacent to a real one.

    Attributes:
        original
            The original directory to create a temp directory for.
        path
            After calling create() or entering, contains the full
            path to the temporary directory.
        delete
            Whether the directory should be deleted when exiting
            (when used as a contextmanager)

    """
    LEADING_CHARS: str
    original: Incomplete
    def __init__(self, original: str, delete: bool | None = None) -> None: ...
