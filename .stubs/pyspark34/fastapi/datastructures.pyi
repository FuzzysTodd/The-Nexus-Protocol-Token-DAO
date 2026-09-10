from _typeshed import Incomplete
from fastapi._compat import CoreSchema as CoreSchema, GetJsonSchemaHandler as GetJsonSchemaHandler, JsonSchemaValue as JsonSchemaValue, PYDANTIC_V2 as PYDANTIC_V2, with_info_plain_validator_function as with_info_plain_validator_function
from starlette.datastructures import UploadFile as StarletteUploadFile
from typing import Any, Callable, Dict, Iterable, Type, TypeVar

class UploadFile(StarletteUploadFile):
    @classmethod
    def __get_validators__(cls) -> Iterable[Callable[..., Any]]: ...
    @classmethod
    def validate(cls, v: Any) -> Any: ...
    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None: ...
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler) -> JsonSchemaValue: ...
    @classmethod
    def __get_pydantic_core_schema__(cls, source: Type[Any], handler: Callable[[Any], CoreSchema]) -> CoreSchema: ...

class DefaultPlaceholder:
    """
    You shouldn't use this class directly.

    It's used internally to recognize when a default value has been overwritten, even
    if the overridden default value was truthy.
    """
    value: Incomplete
    def __init__(self, value: Any) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, o: object) -> bool: ...
DefaultType = TypeVar('DefaultType')

def Default(value: DefaultType) -> DefaultType:
    """
    You shouldn't use this function directly.

    It's used internally to recognize when a default value has been overwritten, even
    if the overridden default value was truthy.
    """
