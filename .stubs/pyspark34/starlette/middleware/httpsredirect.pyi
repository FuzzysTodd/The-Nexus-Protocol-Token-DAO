from _typeshed import Incomplete
from starlette.datastructures import URL as URL
from starlette.responses import RedirectResponse as RedirectResponse
from starlette.types import ASGIApp as ASGIApp, Receive as Receive, Scope as Scope, Send as Send

class HTTPSRedirectMiddleware:
    app: Incomplete
    def __init__(self, app: ASGIApp) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
