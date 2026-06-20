from .routing import APIRoute as APIRoute
from fastapi._compat import BaseConfig as BaseConfig, ModelField as ModelField, PYDANTIC_V2 as PYDANTIC_V2, PydanticSchemaGenerationError as PydanticSchemaGenerationError, Undefined as Undefined, UndefinedType as UndefinedType, Validator as Validator, lenient_issubclass as lenient_issubclass
from fastapi.datastructures import DefaultPlaceholder as DefaultPlaceholder, DefaultType as DefaultType
from pydantic import BaseModel
from pydantic.fields import FieldInfo
from typing import Any, Dict, MutableMapping, Set, Type
from typing_extensions import Literal

def is_body_allowed_for_status_code(status_code: int | str | None) -> bool: ...
def get_path_param_names(path: str) -> Set[str]: ...
def create_response_field(name: str, type_: Type[Any], class_validators: Dict[str, Validator] | None = None, default: Any | None = ..., required: bool | UndefinedType = ..., model_config: Type[BaseConfig] = ..., field_info: FieldInfo | None = None, alias: str | None = None, mode: Literal['validation', 'serialization'] = 'validation') -> ModelField:
    """
    Create a new response field. Raises if type_ is invalid.
    """
def create_cloned_field(field: ModelField, *, cloned_types: MutableMapping[Type[BaseModel], Type[BaseModel]] | None = None) -> ModelField: ...
def generate_operation_id_for_path(*, name: str, path: str, method: str) -> str: ...
def generate_unique_id(route: APIRoute) -> str: ...
def deep_dict_update(main_dict: Dict[Any, Any], update_dict: Dict[Any, Any]) -> None: ...
def get_value_or_default(first_item: DefaultPlaceholder | DefaultType, *extra_items: DefaultPlaceholder | DefaultType) -> DefaultPlaceholder | DefaultType:
    """
    Pass items or `DefaultPlaceholder`s by descending priority.

    The first one to _not_ be a `DefaultPlaceholder` will be returned.

    Otherwise, the first item (a `DefaultPlaceholder`) will be returned.
    """
def match_pydantic_error_url(error_type: str) -> Any: ...
