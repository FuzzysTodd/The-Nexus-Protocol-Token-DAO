from _typeshed import Incomplete
from fastapi.exceptions import HTTPException as HTTPException
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.param_functions import Form as Form
from fastapi.security.base import SecurityBase as SecurityBase
from fastapi.security.utils import get_authorization_scheme_param as get_authorization_scheme_param
from starlette.requests import Request as Request
from typing import Any, Dict, List
from typing_extensions import Annotated

class OAuth2PasswordRequestForm:
    '''
    This is a dependency class, use it like:

        @app.post("/login")
        def login(form_data: OAuth2PasswordRequestForm = Depends()):
            data = form_data.parse()
            print(data.username)
            print(data.password)
            for scope in data.scopes:
                print(scope)
            if data.client_id:
                print(data.client_id)
            if data.client_secret:
                print(data.client_secret)
            return data


    It creates the following Form request parameters in your endpoint:

    grant_type: the OAuth2 spec says it is required and MUST be the fixed string "password".
        Nevertheless, this dependency class is permissive and allows not passing it. If you want to enforce it,
        use instead the OAuth2PasswordRequestFormStrict dependency.
    username: username string. The OAuth2 spec requires the exact field name "username".
    password: password string. The OAuth2 spec requires the exact field name "password".
    scope: Optional string. Several scopes (each one a string) separated by spaces. E.g.
        "items:read items:write users:read profile openid"
    client_id: optional string. OAuth2 recommends sending the client_id and client_secret (if any)
        using HTTP Basic auth, as: client_id:client_secret
    client_secret: optional string. OAuth2 recommends sending the client_id and client_secret (if any)
        using HTTP Basic auth, as: client_id:client_secret
    '''
    grant_type: Incomplete
    username: Incomplete
    password: Incomplete
    scopes: Incomplete
    client_id: Incomplete
    client_secret: Incomplete
    def __init__(self, *, grant_type: Annotated[str | None, None] = None, username: Annotated[str, None], password: Annotated[str, None], scope: Annotated[str, None] = '', client_id: Annotated[str | None, None] = None, client_secret: Annotated[str | None, None] = None) -> None: ...

class OAuth2PasswordRequestFormStrict(OAuth2PasswordRequestForm):
    '''
    This is a dependency class, use it like:

        @app.post("/login")
        def login(form_data: OAuth2PasswordRequestFormStrict = Depends()):
            data = form_data.parse()
            print(data.username)
            print(data.password)
            for scope in data.scopes:
                print(scope)
            if data.client_id:
                print(data.client_id)
            if data.client_secret:
                print(data.client_secret)
            return data


    It creates the following Form request parameters in your endpoint:

    grant_type: the OAuth2 spec says it is required and MUST be the fixed string "password".
        This dependency is strict about it. If you want to be permissive, use instead the
        OAuth2PasswordRequestForm dependency class.
    username: username string. The OAuth2 spec requires the exact field name "username".
    password: password string. The OAuth2 spec requires the exact field name "password".
    scope: Optional string. Several scopes (each one a string) separated by spaces. E.g.
        "items:read items:write users:read profile openid"
    client_id: optional string. OAuth2 recommends sending the client_id and client_secret (if any)
        using HTTP Basic auth, as: client_id:client_secret
    client_secret: optional string. OAuth2 recommends sending the client_id and client_secret (if any)
        using HTTP Basic auth, as: client_id:client_secret
    '''
    def __init__(self, grant_type: Annotated[str, None], username: Annotated[str, None], password: Annotated[str, None], scope: Annotated[str, None] = '', client_id: Annotated[str | None, None] = None, client_secret: Annotated[str | None, None] = None) -> None: ...

class OAuth2(SecurityBase):
    model: Incomplete
    scheme_name: Incomplete
    auto_error: Incomplete
    def __init__(self, *, flows: OAuthFlowsModel | Dict[str, Dict[str, Any]] = ..., scheme_name: str | None = None, description: str | None = None, auto_error: bool = True) -> None: ...
    async def __call__(self, request: Request) -> str | None: ...

class OAuth2PasswordBearer(OAuth2):
    def __init__(self, tokenUrl: str, scheme_name: str | None = None, scopes: Dict[str, str] | None = None, description: str | None = None, auto_error: bool = True) -> None: ...
    async def __call__(self, request: Request) -> str | None: ...

class OAuth2AuthorizationCodeBearer(OAuth2):
    def __init__(self, authorizationUrl: str, tokenUrl: str, refreshUrl: str | None = None, scheme_name: str | None = None, scopes: Dict[str, str] | None = None, description: str | None = None, auto_error: bool = True) -> None: ...
    async def __call__(self, request: Request) -> str | None: ...

class SecurityScopes:
    scopes: Incomplete
    scope_str: Incomplete
    def __init__(self, scopes: List[str] | None = None) -> None: ...
