from _typeshed import Incomplete
from fastapi._compat import ModelField as ModelField
from fastapi.security.base import SecurityBase as SecurityBase
from typing import Any, Callable, List, Sequence

class SecurityRequirement:
    security_scheme: Incomplete
    scopes: Incomplete
    def __init__(self, security_scheme: SecurityBase, scopes: Sequence[str] | None = None) -> None: ...

class Dependant:
    path_params: Incomplete
    query_params: Incomplete
    header_params: Incomplete
    cookie_params: Incomplete
    body_params: Incomplete
    dependencies: Incomplete
    security_requirements: Incomplete
    request_param_name: Incomplete
    websocket_param_name: Incomplete
    http_connection_param_name: Incomplete
    response_param_name: Incomplete
    background_tasks_param_name: Incomplete
    security_scopes: Incomplete
    security_scopes_param_name: Incomplete
    name: Incomplete
    call: Incomplete
    use_cache: Incomplete
    path: Incomplete
    cache_key: Incomplete
    def __init__(self, *, path_params: List[ModelField] | None = None, query_params: List[ModelField] | None = None, header_params: List[ModelField] | None = None, cookie_params: List[ModelField] | None = None, body_params: List[ModelField] | None = None, dependencies: List['Dependant'] | None = None, security_schemes: List[SecurityRequirement] | None = None, name: str | None = None, call: Callable[..., Any] | None = None, request_param_name: str | None = None, websocket_param_name: str | None = None, http_connection_param_name: str | None = None, response_param_name: str | None = None, background_tasks_param_name: str | None = None, security_scopes_param_name: str | None = None, security_scopes: List[str] | None = None, use_cache: bool = True, path: str | None = None) -> None: ...
