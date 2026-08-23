import pathlib
from .abc import AbstractStreamWriter
from .typedefs import LooseHeaders
from .web_request import BaseRequest
from .web_response import StreamResponse
from _typeshed import Incomplete

__all__ = ['FileResponse']

class FileResponse(StreamResponse):
    """A response object can be used to send files."""
    def __init__(self, path: str | pathlib.Path, chunk_size: int = ..., status: int = 200, reason: str | None = None, headers: LooseHeaders | None = None) -> None: ...
    content_type: Incomplete
    etag: Incomplete
    last_modified: Incomplete
    content_length: Incomplete
    async def prepare(self, request: BaseRequest) -> AbstractStreamWriter | None: ...
