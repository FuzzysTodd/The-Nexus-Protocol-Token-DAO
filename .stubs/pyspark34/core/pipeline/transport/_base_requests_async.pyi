from ._base_async import AsyncHttpTransport as AsyncHttpTransport
from ._requests_basic import RequestsTransport as RequestsTransport
from types import TracebackType
from typing import Type

class RequestsAsyncTransportBase(RequestsTransport, AsyncHttpTransport):
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type: Type[BaseException] | None = None, exc_value: BaseException | None = None, traceback: TracebackType | None = None): ...
