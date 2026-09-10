from .base import AppData, ContentStore
from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['AppDataDisabled', 'ContentStoreNA']

class AppDataDisabled(AppData):
    """No application cache available (most likely as we don't have write permissions)."""
    transient: bool
    can_update: bool
    def __init__(self) -> None: ...
    error: Incomplete
    def close(self) -> None:
        """Do nothing."""
    def reset(self) -> None:
        """Do nothing."""
    def py_info(self, path): ...
    def embed_update_log(self, distribution, for_py_version): ...
    def extract(self, path, to_folder) -> None: ...
    def locked(self, path) -> Generator[None, None, None]:
        """Do nothing."""
    @property
    def house(self) -> None: ...
    def wheel_image(self, for_py_version, name) -> None: ...
    def py_info_clear(self) -> None:
        """Nothing to clear."""

class ContentStoreNA(ContentStore):
    def exists(self): ...
    def read(self) -> None:
        """Nothing to read."""
    def write(self, content) -> None:
        """Nothing to write."""
    def remove(self) -> None:
        """Nothing to remove."""
    def locked(self) -> Generator[None, None, None]: ...
