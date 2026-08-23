from typing import Any

__all__ = ['Timeout']

class Timeout(TimeoutError):
    """Raised when the lock could not be acquired in *timeout* seconds."""
    def __init__(self, lock_file: str) -> None: ...
    def __reduce__(self) -> str | tuple[Any, ...]: ...
    @property
    def lock_file(self) -> str:
        """:return: The path of the file lock."""
