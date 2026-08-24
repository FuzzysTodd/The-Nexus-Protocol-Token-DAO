from ..pipeline.transport._requests_trio import TrioStreamDownloadGenerator as TrioStreamDownloadGenerator
from ._http_response_impl_async import AsyncHttpResponseImpl as AsyncHttpResponseImpl
from ._requests_basic import _RestRequestsTransportResponseBase

class RestTrioRequestsTransportResponse(AsyncHttpResponseImpl, _RestRequestsTransportResponseBase):
    """Asynchronous streaming of data from the response."""
    def __init__(self, **kwargs) -> None: ...
    async def close(self) -> None: ...
