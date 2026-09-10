import typing
from _typeshed import Incomplete
from starlette.datastructures import Headers as Headers, MutableHeaders as MutableHeaders
from starlette.types import ASGIApp as ASGIApp, Message as Message, Receive as Receive, Scope as Scope, Send as Send

class GZipMiddleware:
    app: Incomplete
    minimum_size: Incomplete
    compresslevel: Incomplete
    def __init__(self, app: ASGIApp, minimum_size: int = 500, compresslevel: int = 9) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...

class GZipResponder:
    app: Incomplete
    minimum_size: Incomplete
    send: Incomplete
    initial_message: Incomplete
    started: bool
    content_encoding_set: bool
    gzip_buffer: Incomplete
    gzip_file: Incomplete
    def __init__(self, app: ASGIApp, minimum_size: int, compresslevel: int = 9) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    async def send_with_gzip(self, message: Message) -> None: ...

async def unattached_send(message: Message) -> typing.NoReturn: ...
