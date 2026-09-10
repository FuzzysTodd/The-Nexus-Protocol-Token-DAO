from ..pipeline.transport._requests_asyncio import AsyncioStreamDownloadGenerator as AsyncioStreamDownloadGenerator
from ._http_response_impl_async import AsyncHttpResponseImpl as AsyncHttpResponseImpl
from ._requests_basic import _RestRequestsTransportResponseBase

class RestAsyncioRequestsTransportResponse(AsyncHttpResponseImpl, _RestRequestsTransportResponseBase):
    """Asynchronous streaming of data from the response."""
    def __init__(self, **kwargs) -> None: ...
    async def close(self) -> None:
        """Close the response.

        :return: None
        :rtype: None
        """
