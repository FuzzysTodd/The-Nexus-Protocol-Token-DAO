from ..settings import settings as settings
from .common import change_context as change_context, get_function_and_class_name as get_function_and_class_name
from typing import Any, Awaitable, Callable, TypeVar, overload
from typing_extensions import ParamSpec

P = ParamSpec('P')
T = TypeVar('T')

@overload
def distributed_trace_async(__func: Callable[P, Awaitable[T]]) -> Callable[P, Awaitable[T]]: ...
@overload
def distributed_trace_async(**kwargs: Any) -> Callable[[Callable[P, Awaitable[T]]], Callable[P, Awaitable[T]]]: ...
