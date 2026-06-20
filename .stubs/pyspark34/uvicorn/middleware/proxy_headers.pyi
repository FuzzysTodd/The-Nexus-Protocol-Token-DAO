from _typeshed import Incomplete
from typing import List
from uvicorn._types import ASGI3Application as ASGI3Application, ASGIReceiveCallable as ASGIReceiveCallable, ASGISendCallable as ASGISendCallable, HTTPScope as HTTPScope, Scope as Scope, WebSocketScope as WebSocketScope

class ProxyHeadersMiddleware:
    app: Incomplete
    trusted_hosts: Incomplete
    always_trust: Incomplete
    def __init__(self, app: ASGI3Application, trusted_hosts: List[str] | str = '127.0.0.1') -> None: ...
    def get_trusted_client_host(self, x_forwarded_for_hosts: List[str]) -> str | None: ...
    async def __call__(self, scope: Scope, receive: ASGIReceiveCallable, send: ASGISendCallable) -> None: ...
