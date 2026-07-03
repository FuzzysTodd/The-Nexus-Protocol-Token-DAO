from _typeshed import Incomplete
from pydantic import BaseModel as BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException
from typing import Any, Dict, Sequence, Type

class HTTPException(StarletteHTTPException):
    def __init__(self, status_code: int, detail: Any = None, headers: Dict[str, str] | None = None) -> None: ...

RequestErrorModel: Type[BaseModel]
WebSocketErrorModel: Type[BaseModel]

class FastAPIError(RuntimeError):
    """
    A generic, FastAPI-specific error.
    """

class ValidationException(Exception):
    def __init__(self, errors: Sequence[Any]) -> None: ...
    def errors(self) -> Sequence[Any]: ...

class RequestValidationError(ValidationException):
    body: Incomplete
    def __init__(self, errors: Sequence[Any], *, body: Any = None) -> None: ...

class WebSocketRequestValidationError(ValidationException): ...

class ResponseValidationError(ValidationException):
    body: Incomplete
    def __init__(self, errors: Sequence[Any], *, body: Any = None) -> None: ...
