from ..settings import settings as settings
from .common import change_context as change_context, get_function_and_class_name as get_function_and_class_name
from typing import Any, Callable, TypeVar, overload
from typing_extensions import ParamSpec

P = ParamSpec('P')
T = TypeVar('T')

@overload
def distributed_trace(__func: Callable[P, T]) -> Callable[P, T]: ...
@overload
def distributed_trace(**kwargs: Any) -> Callable[[Callable[P, T]], Callable[P, T]]: ...
