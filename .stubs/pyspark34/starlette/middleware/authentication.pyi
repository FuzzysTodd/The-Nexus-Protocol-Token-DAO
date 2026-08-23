import typing
from _typeshed import Incomplete
from starlette.authentication import AuthCredentials as AuthCredentials, AuthenticationBackend as AuthenticationBackend, AuthenticationError as AuthenticationError, UnauthenticatedUser as UnauthenticatedUser
from starlette.requests import HTTPConnection as HTTPConnection
from starlette.responses import PlainTextResponse as PlainTextResponse, Response as Response
from starlette.types import ASGIApp as ASGIApp, Receive as Receive, Scope as Scope, Send as Send

class AuthenticationMiddleware:
    app: Incomplete
    backend: Incomplete
    on_error: Incomplete
    def __init__(self, app: ASGIApp, backend: AuthenticationBackend, on_error: typing.Callable[[HTTPConnection, AuthenticationError], Response] | None = None) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    @staticmethod
    def default_on_error(conn: HTTPConnection, exc: Exception) -> Response: ...
