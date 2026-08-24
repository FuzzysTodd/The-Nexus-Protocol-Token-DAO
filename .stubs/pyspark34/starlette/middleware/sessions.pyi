from _typeshed import Incomplete
from starlette.datastructures import MutableHeaders as MutableHeaders, Secret as Secret
from starlette.requests import HTTPConnection as HTTPConnection
from starlette.types import ASGIApp as ASGIApp, Message as Message, Receive as Receive, Scope as Scope, Send as Send
from typing import Literal

class SessionMiddleware:
    app: Incomplete
    signer: Incomplete
    session_cookie: Incomplete
    max_age: Incomplete
    path: Incomplete
    security_flags: Incomplete
    def __init__(self, app: ASGIApp, secret_key: str | Secret, session_cookie: str = 'session', max_age: int | None = ..., path: str = '/', same_site: Literal['lax', 'strict', 'none'] = 'lax', https_only: bool = False) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
