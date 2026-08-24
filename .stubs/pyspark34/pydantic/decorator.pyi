from .main import BaseModel
from .typing import AnyCallable
from _typeshed import Incomplete
from typing import Any, Callable, Dict, Tuple, Type, TypeVar, overload

__all__ = ['validate_arguments']

AnyCallableT = TypeVar('AnyCallableT', bound=AnyCallable)
ConfigType = None | Type[Any] | Dict[str, Any]

@overload
def validate_arguments(func: None = None, *, config: ConfigType = None) -> Callable[[AnyCallableT], 'AnyCallableT']: ...
@overload
def validate_arguments(func: AnyCallableT) -> AnyCallableT: ...

class ValidatedFunction:
    raw_function: Incomplete
    arg_mapping: Incomplete
    positional_only_args: Incomplete
    v_args_name: str
    v_kwargs_name: str
    def __init__(self, function: AnyCallableT, config: ConfigType) -> None: ...
    def init_model_instance(self, *args: Any, **kwargs: Any) -> BaseModel: ...
    def call(self, *args: Any, **kwargs: Any) -> Any: ...
    def build_values(self, args: Tuple[Any, ...], kwargs: Dict[str, Any]) -> Dict[str, Any]: ...
    def execute(self, m: BaseModel) -> Any: ...
    model: Incomplete
    def create_model(self, fields: Dict[str, Any], takes_args: bool, takes_kwargs: bool, config: ConfigType) -> None: ...
