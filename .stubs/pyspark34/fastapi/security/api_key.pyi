from _typeshed import Incomplete
from fastapi.openapi.models import APIKey as APIKey, APIKeyIn as APIKeyIn
from fastapi.security.base import SecurityBase as SecurityBase
from starlette.requests import Request as Request

class APIKeyBase(SecurityBase): ...

class APIKeyQuery(APIKeyBase):
    model: Incomplete
    scheme_name: Incomplete
    auto_error: Incomplete
    def __init__(self, *, name: str, scheme_name: str | None = None, description: str | None = None, auto_error: bool = True) -> None: ...
    async def __call__(self, request: Request) -> str | None: ...

class APIKeyHeader(APIKeyBase):
    model: Incomplete
    scheme_name: Incomplete
    auto_error: Incomplete
    def __init__(self, *, name: str, scheme_name: str | None = None, description: str | None = None, auto_error: bool = True) -> None: ...
    async def __call__(self, request: Request) -> str | None: ...

class APIKeyCookie(APIKeyBase):
    model: Incomplete
    scheme_name: Incomplete
    auto_error: Incomplete
    def __init__(self, *, name: str, scheme_name: str | None = None, description: str | None = None, auto_error: bool = True) -> None: ...
    async def __call__(self, request: Request) -> str | None: ...
