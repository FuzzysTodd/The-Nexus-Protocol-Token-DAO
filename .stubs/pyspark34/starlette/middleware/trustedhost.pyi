import typing
from _typeshed import Incomplete
from starlette.datastructures import Headers as Headers, URL as URL
from starlette.responses import PlainTextResponse as PlainTextResponse, RedirectResponse as RedirectResponse, Response as Response
from starlette.types import ASGIApp as ASGIApp, Receive as Receive, Scope as Scope, Send as Send

ENFORCE_DOMAIN_WILDCARD: str

class TrustedHostMiddleware:
    app: Incomplete
    allowed_hosts: Incomplete
    allow_any: Incomplete
    www_redirect: Incomplete
    def __init__(self, app: ASGIApp, allowed_hosts: typing.Sequence[str] | None = None, www_redirect: bool = True) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
