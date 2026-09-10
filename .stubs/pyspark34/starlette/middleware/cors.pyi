import typing
from _typeshed import Incomplete
from starlette.datastructures import Headers as Headers, MutableHeaders as MutableHeaders
from starlette.responses import PlainTextResponse as PlainTextResponse, Response as Response
from starlette.types import ASGIApp as ASGIApp, Message as Message, Receive as Receive, Scope as Scope, Send as Send

ALL_METHODS: Incomplete
SAFELISTED_HEADERS: Incomplete

class CORSMiddleware:
    app: Incomplete
    allow_origins: Incomplete
    allow_methods: Incomplete
    allow_headers: Incomplete
    allow_all_origins: Incomplete
    allow_all_headers: Incomplete
    preflight_explicit_allow_origin: Incomplete
    allow_origin_regex: Incomplete
    simple_headers: Incomplete
    preflight_headers: Incomplete
    def __init__(self, app: ASGIApp, allow_origins: typing.Sequence[str] = (), allow_methods: typing.Sequence[str] = ('GET',), allow_headers: typing.Sequence[str] = (), allow_credentials: bool = False, allow_origin_regex: str | None = None, expose_headers: typing.Sequence[str] = (), max_age: int = 600) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    def is_allowed_origin(self, origin: str) -> bool: ...
    def preflight_response(self, request_headers: Headers) -> Response: ...
    async def simple_response(self, scope: Scope, receive: Receive, send: Send, request_headers: Headers) -> None: ...
    async def send(self, message: Message, send: Send, request_headers: Headers) -> None: ...
    @staticmethod
    def allow_explicit_origin(headers: MutableHeaders, origin: str) -> None: ...
