from sentry_sdk import Hub as Hub
from sentry_sdk._functools import wraps as wraps
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import OP as OP
from sentry_sdk.tracing import Span as Span
from sentry_sdk.utils import ContextVar as ContextVar, capture_internal_exceptions as capture_internal_exceptions, transaction_from_function as transaction_from_function
from typing import Any, Callable, TypeVar

F = TypeVar('F', bound=Callable[..., Any])
import_string_name: str

def patch_django_middlewares() -> None: ...
