from _typeshed import Incomplete
from enum import Enum
from fastapi import params as params
from fastapi._compat import ModelField as ModelField, Undefined as Undefined, lenient_issubclass as lenient_issubclass
from fastapi.datastructures import Default as Default, DefaultPlaceholder as DefaultPlaceholder
from fastapi.dependencies.models import Dependant as Dependant
from fastapi.dependencies.utils import get_body_field as get_body_field, get_dependant as get_dependant, get_parameterless_sub_dependant as get_parameterless_sub_dependant, get_typed_return_annotation as get_typed_return_annotation, solve_dependencies as solve_dependencies
from fastapi.encoders import jsonable_encoder as jsonable_encoder
from fastapi.exceptions import FastAPIError as FastAPIError, RequestValidationError as RequestValidationError, ResponseValidationError as ResponseValidationError, WebSocketRequestValidationError as WebSocketRequestValidationError
from fastapi.types import DecoratedCallable as DecoratedCallable, IncEx as IncEx
from fastapi.utils import create_cloned_field as create_cloned_field, create_response_field as create_response_field, generate_unique_id as generate_unique_id, get_value_or_default as get_value_or_default, is_body_allowed_for_status_code as is_body_allowed_for_status_code
from starlette import routing
from starlette.requests import Request as Request
from starlette.responses import Response
from starlette.routing import BaseRoute as BaseRoute, Match
from starlette.types import ASGIApp as ASGIApp, Lifespan as Lifespan, Scope as Scope
from starlette.websockets import WebSocket as WebSocket
from typing import Any, Callable, Coroutine, Dict, List, Sequence, Set, Tuple, Type

async def serialize_response(*, field: ModelField | None = None, response_content: Any, include: IncEx | None = None, exclude: IncEx | None = None, by_alias: bool = True, exclude_unset: bool = False, exclude_defaults: bool = False, exclude_none: bool = False, is_coroutine: bool = True) -> Any: ...
async def run_endpoint_function(*, dependant: Dependant, values: Dict[str, Any], is_coroutine: bool) -> Any: ...
def get_request_handler(dependant: Dependant, body_field: ModelField | None = None, status_code: int | None = None, response_class: Type[Response] | DefaultPlaceholder = ..., response_field: ModelField | None = None, response_model_include: IncEx | None = None, response_model_exclude: IncEx | None = None, response_model_by_alias: bool = True, response_model_exclude_unset: bool = False, response_model_exclude_defaults: bool = False, response_model_exclude_none: bool = False, dependency_overrides_provider: Any | None = None) -> Callable[[Request], Coroutine[Any, Any, Response]]: ...
def get_websocket_app(dependant: Dependant, dependency_overrides_provider: Any | None = None) -> Callable[[WebSocket], Coroutine[Any, Any, Any]]: ...

class APIWebSocketRoute(routing.WebSocketRoute):
    path: Incomplete
    endpoint: Incomplete
    name: Incomplete
    dependencies: Incomplete
    dependant: Incomplete
    app: Incomplete
    def __init__(self, path: str, endpoint: Callable[..., Any], *, name: str | None = None, dependencies: Sequence[params.Depends] | None = None, dependency_overrides_provider: Any | None = None) -> None: ...
    def matches(self, scope: Scope) -> Tuple[Match, Scope]: ...

class APIRoute(routing.Route):
    path: Incomplete
    endpoint: Incomplete
    response_model: Incomplete
    summary: Incomplete
    response_description: Incomplete
    deprecated: Incomplete
    operation_id: Incomplete
    response_model_include: Incomplete
    response_model_exclude: Incomplete
    response_model_by_alias: Incomplete
    response_model_exclude_unset: Incomplete
    response_model_exclude_defaults: Incomplete
    response_model_exclude_none: Incomplete
    include_in_schema: Incomplete
    response_class: Incomplete
    dependency_overrides_provider: Incomplete
    callbacks: Incomplete
    openapi_extra: Incomplete
    generate_unique_id_function: Incomplete
    tags: Incomplete
    responses: Incomplete
    name: Incomplete
    methods: Incomplete
    unique_id: Incomplete
    status_code: Incomplete
    response_field: Incomplete
    secure_cloned_response_field: Incomplete
    dependencies: Incomplete
    description: Incomplete
    response_fields: Incomplete
    dependant: Incomplete
    body_field: Incomplete
    app: Incomplete
    def __init__(self, path: str, endpoint: Callable[..., Any], *, response_model: Any = ..., status_code: int | None = None, tags: List[str | Enum] | None = None, dependencies: Sequence[params.Depends] | None = None, summary: str | None = None, description: str | None = None, response_description: str = 'Successful Response', responses: Dict[int | str, Dict[str, Any]] | None = None, deprecated: bool | None = None, name: str | None = None, methods: Set[str] | List[str] | None = None, operation_id: str | None = None, response_model_include: IncEx | None = None, response_model_exclude: IncEx | None = None, response_model_by_alias: bool = True, response_model_exclude_unset: bool = False, response_model_exclude_defaults: bool = False, response_model_exclude_none: bool = False, include_in_schema: bool = True, response_class: Type[Response] | DefaultPlaceholder = ..., dependency_overrides_provider: Any | None = None, callbacks: List[BaseRoute] | None = None, openapi_extra: Dict[str, Any] | None = None, generate_unique_id_function: Callable[[APIRoute], str] | DefaultPlaceholder = ...) -> None: ...
    def get_route_handler(self) -> Callable[[Request], Coroutine[Any, Any, Response]]: ...
    def matches(self, scope: Scope) -> Tuple[Match, Scope]: ...

class APIRouter(routing.Router):
    prefix: Incomplete
    tags: Incomplete
    dependencies: Incomplete
    deprecated: Incomplete
    include_in_schema: Incomplete
    responses: Incomplete
    callbacks: Incomplete
    dependency_overrides_provider: Incomplete
    route_class: Incomplete
    default_response_class: Incomplete
    generate_unique_id_function: Incomplete
    def __init__(self, *, prefix: str = '', tags: List[str | Enum] | None = None, dependencies: Sequence[params.Depends] | None = None, default_response_class: Type[Response] = ..., responses: Dict[int | str, Dict[str, Any]] | None = None, callbacks: List[BaseRoute] | None = None, routes: List[routing.BaseRoute] | None = None, redirect_slashes: bool = True, default: ASGIApp | None = None, dependency_overrides_provider: Any | None = None, route_class: Type[APIRoute] = ..., on_startup: Sequence[Callable[[], Any]] | None = None, on_shutdown: Sequence[Callable[[], Any]] | None = None, lifespan: Lifespan[Any] | None = None, deprecated: bool | None = None, include_in_schema: bool = True, generate_unique_id_function: Callable[[APIRoute], str] = ...) -> None: ...
    def route(self, path: str, methods: List[str] | None = None, name: str | None = None, include_in_schema: bool = True) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def add_api_route(self, path: str, endpoint: Callable[..., Any], *, response_model: Any = ..., status_code: int | None = None, tags: List[str | Enum] | None = None, dependencies: Sequence[params.Depends] | None = None, summary: str | None = None, description: str | None = None, response_description: str = 'Successful Response', responses: Dict[int | str, Dict[str, Any]] | None = None, deprecated: bool | None = None, methods: Set[str] | List[str] | None = None, operation_id: str | None = None, response_model_include: IncEx | None = None, response_model_exclude: IncEx | None = None, response_model_by_alias: bool = True, response_model_exclude_unset: bool = False, response_model_exclude_defaults: bool = False, response_model_exclude_none: bool = False, include_in_schema: bool = True, response_class: Type[Response] | DefaultPlaceholder = ..., name: str | None = None, route_class_override: Type[APIRoute] | None = None, callbacks: List[BaseRoute] | None = None, openapi_extra: Dict[str, Any] | None = None, generate_unique_id_function: Callable[[APIRoute], str] | DefaultPlaceholder = ...) -> None: ...
    def api_route(self, path: str, *, response_model: Any = ..., status_code: int | None = None, tags: List[str | Enum] | None = None, dependencies: Sequence[params.Depends] | None = None, summary: str | None = None, description: str | None = None, response_description: str = 'Successful Response', responses: Dict[int | str, Dict[str, Any]] | None = None, deprecated: bool | None = None, methods: List[str] | None = None, operation_id: str | None = None, response_model_include: IncEx | None = None, response_model_exclude: IncEx | None = None, response_model_by_alias: bool = True, response_model_exclude_unset: bool = False, response_model_exclude_defaults: bool = False, response_model_exclude_none: bool = False, include_in_schema: bool = True, response_class: Type[Response] = ..., name: str | None = None, callbacks: List[BaseRoute] | None = None, openapi_extra: Dict[str, Any] | None = None, generate_unique_id_function: Callable[[APIRoute], str] = ...) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def add_api_websocket_route(self, path: str, endpoint: Callable[..., Any], name: str | None = None, *, dependencies: Sequence[params.Depends] | None = None) -> None: ...
    def websocket(self, path: str, name: str | None = None, *, dependencies: Sequence[params.Depends] | None = None) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def websocket_route(self, path: str, name: str | None = None) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def include_router(self, router: APIRouter, *, prefix: str = '', tags: List[str | Enum] | None = None, dependencies: Sequence[params.Depends] | None = None, default_response_class: Type[Response] = ..., responses: Dict[int | str, Dict[str, Any]] | None = None, callbacks: List[BaseRoute] | None = None, deprecated: bool | None = None, include_in_schema: bool = True, generate_unique_id_function: Callable[[APIRoute], str] = ...) -> None: ...
    def get(self, path: str, *, response_model: Any = ..., status_code: int | None = None, tags: List[str | Enum] | None = None, dependencies: Sequence[params.Depends] | None = None, summary: str | None = None, description: str | None = None, response_description: str = 'Successful Response', responses: Dict[int | str, Dict[str, Any]] | None = None, deprecated: bool | None = None, operation_id: str | None = None, response_model_include: IncEx | None = None, response_model_exclude: IncEx | None = None, response_model_by_alias: bool = True, response_model_exclude_unset: bool = False, response_model_exclude_defaults: bool = False, response_model_exclude_none: bool = False, include_in_schema: bool = True, response_class: Type[Response] = ..., name: str | None = None, callbacks: List[BaseRoute] | None = None, openapi_extra: Dict[str, Any] | None = None, generate_unique_id_function: Callable[[APIRoute], str] = ...) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def put(self, path: str, *, response_model: Any = ..., status_code: int | None = None, tags: List[str | Enum] | None = None, dependencies: Sequence[params.Depends] | None = None, summary: str | None = None, description: str | None = None, response_description: str = 'Successful Response', responses: Dict[int | str, Dict[str, Any]] | None = None, deprecated: bool | None = None, operation_id: str | None = None, response_model_include: IncEx | None = None, response_model_exclude: IncEx | None = None, response_model_by_alias: bool = True, response_model_exclude_unset: bool = False, response_model_exclude_defaults: bool = False, response_model_exclude_none: bool = False, include_in_schema: bool = True, response_class: Type[Response] = ..., name: str | None = None, callbacks: List[BaseRoute] | None = None, openapi_extra: Dict[str, Any] | None = None, generate_unique_id_function: Callable[[APIRoute], str] = ...) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def post(self, path: str, *, response_model: Any = ..., status_code: int | None = None, tags: List[str | Enum] | None = None, dependencies: Sequence[params.Depends] | None = None, summary: str | None = None, description: str | None = None, response_description: str = 'Successful Response', responses: Dict[int | str, Dict[str, Any]] | None = None, deprecated: bool | None = None, operation_id: str | None = None, response_model_include: IncEx | None = None, response_model_exclude: IncEx | None = None, response_model_by_alias: bool = True, response_model_exclude_unset: bool = False, response_model_exclude_defaults: bool = False, response_model_exclude_none: bool = False, include_in_schema: bool = True, response_class: Type[Response] = ..., name: str | None = None, callbacks: List[BaseRoute] | None = None, openapi_extra: Dict[str, Any] | None = None, generate_unique_id_function: Callable[[APIRoute], str] = ...) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def delete(self, path: str, *, response_model: Any = ..., status_code: int | None = None, tags: List[str | Enum] | None = None, dependencies: Sequence[params.Depends] | None = None, summary: str | None = None, description: str | None = None, response_description: str = 'Successful Response', responses: Dict[int | str, Dict[str, Any]] | None = None, deprecated: bool | None = None, operation_id: str | None = None, response_model_include: IncEx | None = None, response_model_exclude: IncEx | None = None, response_model_by_alias: bool = True, response_model_exclude_unset: bool = False, response_model_exclude_defaults: bool = False, response_model_exclude_none: bool = False, include_in_schema: bool = True, response_class: Type[Response] = ..., name: str | None = None, callbacks: List[BaseRoute] | None = None, openapi_extra: Dict[str, Any] | None = None, generate_unique_id_function: Callable[[APIRoute], str] = ...) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def options(self, path: str, *, response_model: Any = ..., status_code: int | None = None, tags: List[str | Enum] | None = None, dependencies: Sequence[params.Depends] | None = None, summary: str | None = None, description: str | None = None, response_description: str = 'Successful Response', responses: Dict[int | str, Dict[str, Any]] | None = None, deprecated: bool | None = None, operation_id: str | None = None, response_model_include: IncEx | None = None, response_model_exclude: IncEx | None = None, response_model_by_alias: bool = True, response_model_exclude_unset: bool = False, response_model_exclude_defaults: bool = False, response_model_exclude_none: bool = False, include_in_schema: bool = True, response_class: Type[Response] = ..., name: str | None = None, callbacks: List[BaseRoute] | None = None, openapi_extra: Dict[str, Any] | None = None, generate_unique_id_function: Callable[[APIRoute], str] = ...) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def head(self, path: str, *, response_model: Any = ..., status_code: int | None = None, tags: List[str | Enum] | None = None, dependencies: Sequence[params.Depends] | None = None, summary: str | None = None, description: str | None = None, response_description: str = 'Successful Response', responses: Dict[int | str, Dict[str, Any]] | None = None, deprecated: bool | None = None, operation_id: str | None = None, response_model_include: IncEx | None = None, response_model_exclude: IncEx | None = None, response_model_by_alias: bool = True, response_model_exclude_unset: bool = False, response_model_exclude_defaults: bool = False, response_model_exclude_none: bool = False, include_in_schema: bool = True, response_class: Type[Response] = ..., name: str | None = None, callbacks: List[BaseRoute] | None = None, openapi_extra: Dict[str, Any] | None = None, generate_unique_id_function: Callable[[APIRoute], str] = ...) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def patch(self, path: str, *, response_model: Any = ..., status_code: int | None = None, tags: List[str | Enum] | None = None, dependencies: Sequence[params.Depends] | None = None, summary: str | None = None, description: str | None = None, response_description: str = 'Successful Response', responses: Dict[int | str, Dict[str, Any]] | None = None, deprecated: bool | None = None, operation_id: str | None = None, response_model_include: IncEx | None = None, response_model_exclude: IncEx | None = None, response_model_by_alias: bool = True, response_model_exclude_unset: bool = False, response_model_exclude_defaults: bool = False, response_model_exclude_none: bool = False, include_in_schema: bool = True, response_class: Type[Response] = ..., name: str | None = None, callbacks: List[BaseRoute] | None = None, openapi_extra: Dict[str, Any] | None = None, generate_unique_id_function: Callable[[APIRoute], str] = ...) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def trace(self, path: str, *, response_model: Any = ..., status_code: int | None = None, tags: List[str | Enum] | None = None, dependencies: Sequence[params.Depends] | None = None, summary: str | None = None, description: str | None = None, response_description: str = 'Successful Response', responses: Dict[int | str, Dict[str, Any]] | None = None, deprecated: bool | None = None, operation_id: str | None = None, response_model_include: IncEx | None = None, response_model_exclude: IncEx | None = None, response_model_by_alias: bool = True, response_model_exclude_unset: bool = False, response_model_exclude_defaults: bool = False, response_model_exclude_none: bool = False, include_in_schema: bool = True, response_class: Type[Response] = ..., name: str | None = None, callbacks: List[BaseRoute] | None = None, openapi_extra: Dict[str, Any] | None = None, generate_unique_id_function: Callable[[APIRoute], str] = ...) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def on_event(self, event_type: str) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
