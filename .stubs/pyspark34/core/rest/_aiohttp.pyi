import collections.abc
from ..exceptions import ResponseNotReadError as ResponseNotReadError
from ..pipeline.transport._aiohttp import AioHttpStreamDownloadGenerator as AioHttpStreamDownloadGenerator
from ._http_response_impl_async import AsyncHttpResponseBackcompatMixin as AsyncHttpResponseBackcompatMixin, AsyncHttpResponseImpl as AsyncHttpResponseImpl
from _typeshed import Incomplete
from multidict import CIMultiDict
from typing import Iterator

class _ItemsView(collections.abc.ItemsView):
    def __init__(self, ref) -> None: ...
    def __iter__(self): ...
    def __contains__(self, item) -> bool: ...

class _KeysView(collections.abc.KeysView):
    def __init__(self, items) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __contains__(self, key) -> bool: ...

class _ValuesView(collections.abc.ValuesView):
    def __init__(self, items) -> None: ...
    def __iter__(self): ...
    def __contains__(self, value) -> bool: ...

class _CIMultiDict(CIMultiDict):
    """Dictionary with the support for duplicate case-insensitive keys."""
    def __iter__(self): ...
    def keys(self):
        """Return a new view of the dictionary's keys.

        :return: A new view of the dictionary's keys
        :rtype: ~collections.abc.KeysView
        """
    def items(self):
        """Return a new view of the dictionary's items.

        :return: A new view of the dictionary's items
        :rtype: ~collections.abc.ItemsView
        """
    def values(self):
        """Return a new view of the dictionary's values.

        :return: A new view of the dictionary's values
        :rtype: ~collections.abc.ValuesView
        """
    def __getitem__(self, key: str) -> str: ...
    def get(self, key, default: Incomplete | None = None): ...

class _RestAioHttpTransportResponseBackcompatMixin(AsyncHttpResponseBackcompatMixin):
    """Backcompat mixin for aiohttp responses.

    Need to add it's own mixin because it has function load_body, which other
    transport responses don't have, and also because we need to synchronously
    decompress the body if users call .body()
    """
    def body(self) -> bytes:
        """Return the whole body as bytes in memory.

        Have to modify the default behavior here. In AioHttp, we do decompression
        when accessing the body method. The behavior here is the same as if the
        caller did an async read of the response first. But for backcompat reasons,
        we need to support this decompression within the synchronous body method.

        :return: The response's bytes
        :rtype: bytes
        """
    def __getattr__(self, attr): ...

class RestAioHttpTransportResponse(AsyncHttpResponseImpl, _RestAioHttpTransportResponseBackcompatMixin):
    def __init__(self, *, internal_response, decompress: bool = True, **kwargs) -> None: ...
    @property
    def content(self) -> bytes:
        """Return the response's content in bytes.

        :return: The response's content in bytes
        :rtype: bytes
        """
    async def read(self) -> bytes:
        """Read the response's bytes into memory.

        :return: The response's bytes
        :rtype: bytes
        """
    async def close(self) -> None:
        """Close the response.

        :return: None
        :rtype: None
        """
