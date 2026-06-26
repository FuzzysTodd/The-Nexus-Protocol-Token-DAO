from _typeshed import Incomplete
from fastapi.exceptions import HTTPException as HTTPException
from fastapi.security.base import SecurityBase as SecurityBase
from fastapi.security.utils import get_authorization_scheme_param as get_authorization_scheme_param
from pydantic import BaseModel
from starlette.requests import Request as Request

class HTTPBasicCredentials(BaseModel):
    username: str
    password: str

class HTTPAuthorizationCredentials(BaseModel):
    scheme: str
    credentials: str

class HTTPBase(SecurityBase):
    model: Incomplete
    scheme_name: Incomplete
    auto_error: Incomplete
    def __init__(self, *, scheme: str, scheme_name: str | None = None, description: str | None = None, auto_error: bool = True) -> None: ...
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None: ...

class HTTPBasic(HTTPBase):
    model: Incomplete
    scheme_name: Incomplete
    realm: Incomplete
    auto_error: Incomplete
    def __init__(self, *, scheme_name: str | None = None, realm: str | None = None, description: str | None = None, auto_error: bool = True) -> None: ...
    async def __call__(self, request: Request) -> HTTPBasicCredentials | None: ...

class HTTPBearer(HTTPBase):
    model: Incomplete
    scheme_name: Incomplete
    auto_error: Incomplete
    def __init__(self, *, bearerFormat: str | None = None, scheme_name: str | None = None, description: str | None = None, auto_error: bool = True) -> None: ...
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None: ...

class HTTPDigest(HTTPBase):
    model: Incomplete
    scheme_name: Incomplete
    auto_error: Incomplete
    def __init__(self, *, scheme_name: str | None = None, description: str | None = None, auto_error: bool = True) -> None: ...
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None: ...
