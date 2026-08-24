from _typeshed import Incomplete
from contextlib import AbstractContextManager

class chdir(AbstractContextManager):
    """Non thread-safe context manager to change the current working directory."""
    path: Incomplete
    def __init__(self, path) -> None:
        """Initialize the manager."""
    def __enter__(self) -> None:
        """Enter the context."""
    def __exit__(self, *excinfo) -> None:
        """Exit the context."""
