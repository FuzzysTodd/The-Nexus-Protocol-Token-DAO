from _typeshed import Incomplete
from fastapi.concurrency import AsyncExitStack as AsyncExitStack
from starlette.types import ASGIApp as ASGIApp, Receive as Receive, Scope as Scope, Send as Send

class AsyncExitStackMiddleware:
    app: Incomplete
    context_name: Incomplete
    def __init__(self, app: ASGIApp, context_name: str = 'fastapi_astack') -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
