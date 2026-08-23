from _typeshed import Incomplete
from fastapi.security.base import SecurityBase as SecurityBase
from starlette.requests import Request as Request

class OpenIdConnect(SecurityBase):
    model: Incomplete
    scheme_name: Incomplete
    auto_error: Incomplete
    def __init__(self, *, openIdConnectUrl: str, scheme_name: str | None = None, description: str | None = None, auto_error: bool = True) -> None: ...
    async def __call__(self, request: Request) -> str | None: ...
