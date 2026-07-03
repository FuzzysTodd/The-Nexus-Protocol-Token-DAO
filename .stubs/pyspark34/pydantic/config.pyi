from .fields import ModelField
from .main import BaseModel
from .typing import AnyArgTCallable, AnyCallable
from .utils import GetterDict
from enum import Enum
from typing import Any, Callable, Dict, ForwardRef, Tuple, Type, overload
from typing_extensions import Literal, Protocol, TypedDict

__all__ = ['BaseConfig', 'ConfigDict', 'get_config', 'Extra', 'inherit_config', 'prepare_config']

class SchemaExtraCallable(Protocol):
    @overload
    def __call__(self, schema: Dict[str, Any]) -> None: ...
    @overload
    def __call__(self, schema: Dict[str, Any], model_class: Type[BaseModel]) -> None: ...

class Extra(str, Enum):
    allow: str
    ignore: str
    forbid: str

class ConfigDict(TypedDict, total=False):
    title: str | None
    anystr_lower: bool
    anystr_strip_whitespace: bool
    min_anystr_length: int
    max_anystr_length: int | None
    validate_all: bool
    extra: Extra
    allow_mutation: bool
    frozen: bool
    allow_population_by_field_name: bool
    use_enum_values: bool
    fields: Dict[str, str | Dict[str, str]]
    validate_assignment: bool
    error_msg_templates: Dict[str, str]
    arbitrary_types_allowed: bool
    orm_mode: bool
    getter_dict: Type[GetterDict]
    alias_generator: Callable[[str], str] | None
    keep_untouched: Tuple[type, ...]
    schema_extra: Dict[str, object] | SchemaExtraCallable
    json_loads: Callable[[str], object]
    json_dumps: AnyArgTCallable[str]
    json_encoders: Dict[Type[object], AnyCallable]
    underscore_attrs_are_private: bool
    allow_inf_nan: bool
    copy_on_model_validation: Literal['none', 'deep', 'shallow']
    post_init_call: Literal['before_validation', 'after_validation']
ConfigDict = dict

class BaseConfig:
    title: str | None
    anystr_lower: bool
    anystr_upper: bool
    anystr_strip_whitespace: bool
    min_anystr_length: int
    max_anystr_length: int | None
    validate_all: bool
    extra: Extra
    allow_mutation: bool
    frozen: bool
    allow_population_by_field_name: bool
    use_enum_values: bool
    fields: Dict[str, str | Dict[str, str]]
    validate_assignment: bool
    error_msg_templates: Dict[str, str]
    arbitrary_types_allowed: bool
    orm_mode: bool
    getter_dict: Type[GetterDict]
    alias_generator: Callable[[str], str] | None
    keep_untouched: Tuple[type, ...]
    schema_extra: Dict[str, Any] | SchemaExtraCallable
    json_loads: Callable[[str], Any]
    json_dumps: Callable[..., str]
    json_encoders: Dict[Type[Any] | str | ForwardRef, AnyCallable]
    underscore_attrs_are_private: bool
    allow_inf_nan: bool
    copy_on_model_validation: Literal['none', 'deep', 'shallow']
    smart_union: bool
    post_init_call: Literal['before_validation', 'after_validation']
    @classmethod
    def get_field_info(cls, name: str) -> Dict[str, Any]:
        """
        Get properties of FieldInfo from the `fields` property of the config class.
        """
    @classmethod
    def prepare_field(cls, field: ModelField) -> None:
        """
        Optional hook to check or modify fields during model creation.
        """

def get_config(config: ConfigDict | Type[object] | None) -> Type[BaseConfig]: ...
def inherit_config(self_config: ConfigType, parent_config: ConfigType, **namespace: Any) -> ConfigType: ...
def prepare_config(config: Type[BaseConfig], cls_name: str) -> None: ...
