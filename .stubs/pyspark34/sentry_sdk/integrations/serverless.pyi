from sentry_sdk._compat import reraise as reraise
from sentry_sdk._functools import wraps as wraps
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.utils import event_from_exception as event_from_exception
from typing import Any, Callable, TypeVar, overload

F = TypeVar('F', bound=Callable[..., Any])

@overload
def serverless_function(f: F, flush: bool = True) -> F: ...
@overload
def serverless_function(f: None = None, flush: bool = True) -> Callable[[F], F]: ...
