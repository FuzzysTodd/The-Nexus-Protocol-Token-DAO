import os
import typing
from _typeshed import Incomplete
from datetime import datetime
from starlette._compat import md5_hexdigest as md5_hexdigest
from starlette.background import BackgroundTask as BackgroundTask
from starlette.concurrency import iterate_in_threadpool as iterate_in_threadpool
from starlette.datastructures import MutableHeaders as MutableHeaders, URL as URL
from starlette.types import Receive as Receive, Scope as Scope, Send as Send
from typing import Literal

def guess_type(url: str | os.PathLike[str], strict: bool = True) -> typing.Tuple[str | None, str | None]: ...

class Response:
    media_type: Incomplete
    charset: str
    status_code: Incomplete
    background: Incomplete
    body: Incomplete
    def __init__(self, content: typing.Any = None, status_code: int = 200, headers: typing.Mapping[str, str] | None = None, media_type: str | None = None, background: BackgroundTask | None = None) -> None: ...
    def render(self, content: typing.Any) -> bytes: ...
    raw_headers: Incomplete
    def init_headers(self, headers: typing.Mapping[str, str] | None = None) -> None: ...
    @property
    def headers(self) -> MutableHeaders: ...
    def set_cookie(self, key: str, value: str = '', max_age: int | None = None, expires: datetime | str | int | None = None, path: str = '/', domain: str | None = None, secure: bool = False, httponly: bool = False, samesite: Literal['lax', 'strict', 'none'] | None = 'lax') -> None: ...
    def delete_cookie(self, key: str, path: str = '/', domain: str | None = None, secure: bool = False, httponly: bool = False, samesite: Literal['lax', 'strict', 'none'] | None = 'lax') -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...

class HTMLResponse(Response):
    media_type: str

class PlainTextResponse(Response):
    media_type: str

class JSONResponse(Response):
    media_type: str
    def __init__(self, content: typing.Any, status_code: int = 200, headers: typing.Dict[str, str] | None = None, media_type: str | None = None, background: BackgroundTask | None = None) -> None: ...
    def render(self, content: typing.Any) -> bytes: ...

class RedirectResponse(Response):
    def __init__(self, url: str | URL, status_code: int = 307, headers: typing.Mapping[str, str] | None = None, background: BackgroundTask | None = None) -> None: ...

Content: Incomplete
SyncContentStream: Incomplete
AsyncContentStream: Incomplete
ContentStream: Incomplete

class StreamingResponse(Response):
    body_iterator: AsyncContentStream
    status_code: Incomplete
    media_type: Incomplete
    background: Incomplete
    def __init__(self, content: ContentStream, status_code: int = 200, headers: typing.Mapping[str, str] | None = None, media_type: str | None = None, background: BackgroundTask | None = None) -> None: ...
    async def listen_for_disconnect(self, receive: Receive) -> None: ...
    async def stream_response(self, send: Send) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...

class FileResponse(Response):
    chunk_size: Incomplete
    path: Incomplete
    status_code: Incomplete
    filename: Incomplete
    send_header_only: Incomplete
    media_type: Incomplete
    background: Incomplete
    stat_result: Incomplete
    def __init__(self, path: str | os.PathLike[str], status_code: int = 200, headers: typing.Mapping[str, str] | None = None, media_type: str | None = None, background: BackgroundTask | None = None, filename: str | None = None, stat_result: os.stat_result | None = None, method: str | None = None, content_disposition_type: str = 'attachment') -> None: ...
    def set_stat_headers(self, stat_result: os.stat_result) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
