from _typeshed import Incomplete
from requests import Session as Session
from requests.models import Response as Response
from typing import Any

log: Incomplete
HEADERS: Incomplete

class HTTPRangeRequestUnsupported(Exception): ...

class LazyZipOverHTTP:
    """File-like object mapped to a ZIP file over HTTP.

    This uses HTTP range requests to lazily fetch the file's content,
    which is supposed to be fed to ZipFile.  If such requests are not
    supported by the server, raise HTTPRangeRequestUnsupported
    during initialization.
    """
    def __init__(self, url: str, session: Session, chunk_size: int = ...) -> None: ...
    @property
    def mode(self) -> str:
        """Opening mode, which is always rb."""
    @property
    def name(self) -> str:
        """Path to the underlying file."""
    def seekable(self) -> bool:
        """Return whether random access is supported, which is True."""
    def close(self) -> None:
        """Close the file."""
    @property
    def closed(self) -> bool:
        """Whether the file is closed."""
    def read(self, size: int = -1) -> bytes:
        """Read up to size bytes from the object and return them.

        As a convenience, if size is unspecified or -1,
        all bytes until EOF are returned.  Fewer than
        size bytes may be returned if EOF is reached.
        """
    def readable(self) -> bool:
        """Return whether the file is readable, which is True."""
    def seek(self, offset: int, whence: int = 0) -> int:
        """Change stream position and return the new absolute position.

        Seek to offset relative position indicated by whence:
        * 0: Start of stream (the default).  pos should be >= 0;
        * 1: Current position - pos may be negative;
        * 2: End of stream - pos usually negative.
        """
    def tell(self) -> int:
        """Return the current position."""
    def truncate(self, size: int | None = None) -> int:
        """Resize the stream to the given size in bytes.

        If size is unspecified resize to the current position.
        The current stream position isn't changed.

        Return the new file size.
        """
    def writable(self) -> bool:
        """Return False."""
    def __enter__(self) -> LazyZipOverHTTP: ...
    def __exit__(self, *exc: Any) -> bool | None: ...

class LazyConda(LazyZipOverHTTP):
    def prefetch(self, conda_file_id) -> None:
        """
        Conda fork specific. Prefetch the `.info` range from the remote archive.
        Reduces number of Range requests to 2 or 3 (1 or 2 for the directory, 1
        for the file).

        conda_file_id: name of .conda without path or `.conda` extension
        """
