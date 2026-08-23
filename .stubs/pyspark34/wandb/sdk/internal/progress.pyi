from _typeshed import Incomplete
from typing import IO, Protocol
from wandb.errors import CommError as CommError

class ProgressFn(Protocol):
    def __call__(self, new_bytes: int, total_bytes: int) -> None: ...

class Progress:
    """A helper class for displaying progress."""
    ITER_BYTES: Incomplete
    file: Incomplete
    callback: Incomplete
    bytes_read: int
    len: Incomplete
    def __init__(self, file: IO[bytes], callback: ProgressFn | None = None) -> None: ...
    def read(self, size: int = -1):
        """Read bytes and call the callback."""
    def rewind(self) -> None: ...
    def __getattr__(self, name):
        """Fallback to the file object for attrs not defined here."""
    def __iter__(self): ...
    def __next__(self): ...
    def __len__(self) -> int: ...
    next = __next__

class AsyncProgress:
    """Wrapper around Progress, to make it async iterable.

    httpx, for streaming uploads, requires the data source to be an async iterable.
    If we pass in a sync iterable (like a bare `Progress` instance), httpx will
    get confused, think we're trying to make a synchronous request, and raise.
    So we need this wrapper class to be an async iterable but *not* a sync iterable.
    """
    def __init__(self, progress: Progress) -> None: ...
    def __aiter__(self): ...
    async def __anext__(self): ...
    def __len__(self) -> int: ...
    def rewind(self) -> None: ...
