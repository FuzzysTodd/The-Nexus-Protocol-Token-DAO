from .config import BaseConfig, ConfigDict
from .main import BaseModel
from .typing import CallableGenerator
from typing import Any, Callable, ClassVar, Dict, Generator, Type, TypeVar, overload

__all__ = ['dataclass', 'set_validation', 'create_pydantic_model_from_dataclass', 'is_builtin_dataclass', 'make_dataclass_validator']

DataclassT = TypeVar('DataclassT', bound='Dataclass')

class Dataclass:
    __dataclass_fields__: ClassVar[Dict[str, Any]]
    __dataclass_params__: ClassVar[Any]
    __post_init__: ClassVar[Callable[..., None]]
    __pydantic_run_validation__: ClassVar[bool]
    __post_init_post_parse__: ClassVar[Callable[..., None]]
    __pydantic_initialised__: ClassVar[bool]
    __pydantic_model__: ClassVar[Type[BaseModel]]
    __pydantic_validate_values__: ClassVar[Callable[[Dataclass], None]]
    __pydantic_has_field_info_default__: ClassVar[bool]
    def __init__(self, *args: object, **kwargs: object) -> None: ...
    @classmethod
    def __get_validators__(cls) -> CallableGenerator: ...
    @classmethod
    def __validate__(cls, v: Any) -> DataclassT: ...

@overload
def dataclass(*, init: bool = True, repr: bool = True, eq: bool = True, order: bool = False, unsafe_hash: bool = False, frozen: bool = False, config: ConfigDict | Type[object] | None = None, validate_on_init: bool | None = None, use_proxy: bool | None = None, kw_only: bool = ...) -> Callable[[Type[_T]], 'DataclassClassOrWrapper']: ...
@overload
def dataclass(_cls: Type[_T], *, init: bool = True, repr: bool = True, eq: bool = True, order: bool = False, unsafe_hash: bool = False, frozen: bool = False, config: ConfigDict | Type[object] | None = None, validate_on_init: bool | None = None, use_proxy: bool | None = None, kw_only: bool = ...) -> DataclassClassOrWrapper: ...
def set_validation(cls, value: bool) -> Generator[Type['DataclassT'], None, None]: ...

class DataclassProxy:
    def __init__(self, dc_cls: Type['Dataclass']) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, __name: str, __value: Any) -> None: ...
    def __instancecheck__(self, instance: Any) -> bool: ...
    def __copy__(self) -> DataclassProxy: ...
    def __deepcopy__(self, memo: Any) -> DataclassProxy: ...

def create_pydantic_model_from_dataclass(dc_cls: Type['Dataclass'], config: Type[Any] = ..., dc_cls_doc: str | None = None) -> Type['BaseModel']: ...
def is_builtin_dataclass(_cls: Type[Any]) -> bool:
    """
    Whether a class is a stdlib dataclass
    (useful to discriminated a pydantic dataclass that is actually a wrapper around a stdlib dataclass)

    we check that
    - `_cls` is a dataclass
    - `_cls` is not a processed pydantic dataclass (with a basemodel attached)
    - `_cls` is not a pydantic dataclass inheriting directly from a stdlib dataclass
    e.g.
    ```
    @dataclasses.dataclass
    class A:
        x: int

    @pydantic.dataclasses.dataclass
    class B(A):
        y: int
    ```
    In this case, when we first check `B`, we make an extra check and look at the annotations ('y'),
    which won't be a superset of all the dataclass fields (only the stdlib fields i.e. 'x')
    """
def make_dataclass_validator(dc_cls: Type['Dataclass'], config: Type[BaseConfig]) -> CallableGenerator:
    """
    Create a pydantic.dataclass from a builtin dataclass to add type validation
    and yield the validators
    It retrieves the parameters of the dataclass and forwards them to the newly created dataclass
    """
