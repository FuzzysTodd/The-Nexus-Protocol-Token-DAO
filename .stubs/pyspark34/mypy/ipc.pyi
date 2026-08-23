from _typeshed import Incomplete
from types import TracebackType
from typing_extensions import Final

class IPCException(Exception):
    """Exception for IPC issues."""

class IPCBase:
    """Base class for communication between the dmypy client and server.

    This contains logic shared between the client and server, such as reading
    and writing.
    """
    connection: _IPCHandle
    name: Incomplete
    timeout: Incomplete
    def __init__(self, name: str, timeout: float | None) -> None: ...
    def read(self, size: int = 100000) -> bytes:
        """Read bytes from an IPC connection until its empty."""
    def write(self, data: bytes) -> None:
        """Write bytes to an IPC connection."""
    def close(self) -> None: ...

class IPCClient(IPCBase):
    """The client side of an IPC connection."""
    connection: Incomplete
    def __init__(self, name: str, timeout: float | None) -> None: ...
    def __enter__(self) -> IPCClient: ...
    def __exit__(self, exc_ty: type[BaseException] | None = None, exc_val: BaseException | None = None, exc_tb: TracebackType | None = None) -> None: ...

class IPCServer(IPCBase):
    BUFFER_SIZE: Final[Incomplete]
    connection: Incomplete
    sock_directory: Incomplete
    sock: Incomplete
    def __init__(self, name: str, timeout: float | None = None) -> None: ...
    def __enter__(self) -> IPCServer: ...
    def __exit__(self, exc_ty: type[BaseException] | None = None, exc_val: BaseException | None = None, exc_tb: TracebackType | None = None) -> None: ...
    def cleanup(self) -> None: ...
    @property
    def connection_name(self) -> str: ...
