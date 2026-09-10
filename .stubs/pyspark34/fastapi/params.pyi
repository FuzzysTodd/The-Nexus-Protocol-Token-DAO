from ._compat import PYDANTIC_V2 as PYDANTIC_V2, Undefined as Undefined
from _typeshed import Incomplete
from enum import Enum
from fastapi.openapi.models import Example as Example
from pydantic.fields import FieldInfo
from typing import Any, Callable, Dict, List, Sequence
from typing_extensions import Annotated

class ParamTypes(Enum):
    query: str
    header: str
    path: str
    cookie: str

class Param(FieldInfo):
    in_: ParamTypes
    deprecated: Incomplete
    example: Incomplete
    include_in_schema: Incomplete
    openapi_examples: Incomplete
    def __init__(self, default: Any = ..., *, default_factory: Callable[[], Any] | None = ..., annotation: Any | None = None, alias: str | None = None, alias_priority: int | None = ..., validation_alias: str | None = None, serialization_alias: str | None = None, title: str | None = None, description: str | None = None, gt: float | None = None, ge: float | None = None, lt: float | None = None, le: float | None = None, min_length: int | None = None, max_length: int | None = None, pattern: str | None = None, regex: Annotated[str | None, None] = None, discriminator: str | None = None, strict: bool | None = ..., multiple_of: float | None = ..., allow_inf_nan: bool | None = ..., max_digits: int | None = ..., decimal_places: int | None = ..., examples: List[Any] | None = None, example: Annotated[Any | None, None] = ..., openapi_examples: Dict[str, Example] | None = None, deprecated: bool | None = None, include_in_schema: bool = True, json_schema_extra: Dict[str, Any] | None = None, **extra: Any) -> None: ...

class Path(Param):
    in_: Incomplete
    def __init__(self, default: Any = ..., *, default_factory: Callable[[], Any] | None = ..., annotation: Any | None = None, alias: str | None = None, alias_priority: int | None = ..., validation_alias: str | None = None, serialization_alias: str | None = None, title: str | None = None, description: str | None = None, gt: float | None = None, ge: float | None = None, lt: float | None = None, le: float | None = None, min_length: int | None = None, max_length: int | None = None, pattern: str | None = None, regex: Annotated[str | None, None] = None, discriminator: str | None = None, strict: bool | None = ..., multiple_of: float | None = ..., allow_inf_nan: bool | None = ..., max_digits: int | None = ..., decimal_places: int | None = ..., examples: List[Any] | None = None, example: Annotated[Any | None, None] = ..., openapi_examples: Dict[str, Example] | None = None, deprecated: bool | None = None, include_in_schema: bool = True, json_schema_extra: Dict[str, Any] | None = None, **extra: Any) -> None: ...

class Query(Param):
    in_: Incomplete
    def __init__(self, default: Any = ..., *, default_factory: Callable[[], Any] | None = ..., annotation: Any | None = None, alias: str | None = None, alias_priority: int | None = ..., validation_alias: str | None = None, serialization_alias: str | None = None, title: str | None = None, description: str | None = None, gt: float | None = None, ge: float | None = None, lt: float | None = None, le: float | None = None, min_length: int | None = None, max_length: int | None = None, pattern: str | None = None, regex: Annotated[str | None, None] = None, discriminator: str | None = None, strict: bool | None = ..., multiple_of: float | None = ..., allow_inf_nan: bool | None = ..., max_digits: int | None = ..., decimal_places: int | None = ..., examples: List[Any] | None = None, example: Annotated[Any | None, None] = ..., openapi_examples: Dict[str, Example] | None = None, deprecated: bool | None = None, include_in_schema: bool = True, json_schema_extra: Dict[str, Any] | None = None, **extra: Any) -> None: ...

class Header(Param):
    in_: Incomplete
    convert_underscores: Incomplete
    def __init__(self, default: Any = ..., *, default_factory: Callable[[], Any] | None = ..., annotation: Any | None = None, alias: str | None = None, alias_priority: int | None = ..., validation_alias: str | None = None, serialization_alias: str | None = None, convert_underscores: bool = True, title: str | None = None, description: str | None = None, gt: float | None = None, ge: float | None = None, lt: float | None = None, le: float | None = None, min_length: int | None = None, max_length: int | None = None, pattern: str | None = None, regex: Annotated[str | None, None] = None, discriminator: str | None = None, strict: bool | None = ..., multiple_of: float | None = ..., allow_inf_nan: bool | None = ..., max_digits: int | None = ..., decimal_places: int | None = ..., examples: List[Any] | None = None, example: Annotated[Any | None, None] = ..., openapi_examples: Dict[str, Example] | None = None, deprecated: bool | None = None, include_in_schema: bool = True, json_schema_extra: Dict[str, Any] | None = None, **extra: Any) -> None: ...

class Cookie(Param):
    in_: Incomplete
    def __init__(self, default: Any = ..., *, default_factory: Callable[[], Any] | None = ..., annotation: Any | None = None, alias: str | None = None, alias_priority: int | None = ..., validation_alias: str | None = None, serialization_alias: str | None = None, title: str | None = None, description: str | None = None, gt: float | None = None, ge: float | None = None, lt: float | None = None, le: float | None = None, min_length: int | None = None, max_length: int | None = None, pattern: str | None = None, regex: Annotated[str | None, None] = None, discriminator: str | None = None, strict: bool | None = ..., multiple_of: float | None = ..., allow_inf_nan: bool | None = ..., max_digits: int | None = ..., decimal_places: int | None = ..., examples: List[Any] | None = None, example: Annotated[Any | None, None] = ..., openapi_examples: Dict[str, Example] | None = None, deprecated: bool | None = None, include_in_schema: bool = True, json_schema_extra: Dict[str, Any] | None = None, **extra: Any) -> None: ...

class Body(FieldInfo):
    embed: Incomplete
    media_type: Incomplete
    deprecated: Incomplete
    example: Incomplete
    include_in_schema: Incomplete
    openapi_examples: Incomplete
    def __init__(self, default: Any = ..., *, default_factory: Callable[[], Any] | None = ..., annotation: Any | None = None, embed: bool = False, media_type: str = 'application/json', alias: str | None = None, alias_priority: int | None = ..., validation_alias: str | None = None, serialization_alias: str | None = None, title: str | None = None, description: str | None = None, gt: float | None = None, ge: float | None = None, lt: float | None = None, le: float | None = None, min_length: int | None = None, max_length: int | None = None, pattern: str | None = None, regex: Annotated[str | None, None] = None, discriminator: str | None = None, strict: bool | None = ..., multiple_of: float | None = ..., allow_inf_nan: bool | None = ..., max_digits: int | None = ..., decimal_places: int | None = ..., examples: List[Any] | None = None, example: Annotated[Any | None, None] = ..., openapi_examples: Dict[str, Example] | None = None, deprecated: bool | None = None, include_in_schema: bool = True, json_schema_extra: Dict[str, Any] | None = None, **extra: Any) -> None: ...

class Form(Body):
    def __init__(self, default: Any = ..., *, default_factory: Callable[[], Any] | None = ..., annotation: Any | None = None, media_type: str = 'application/x-www-form-urlencoded', alias: str | None = None, alias_priority: int | None = ..., validation_alias: str | None = None, serialization_alias: str | None = None, title: str | None = None, description: str | None = None, gt: float | None = None, ge: float | None = None, lt: float | None = None, le: float | None = None, min_length: int | None = None, max_length: int | None = None, pattern: str | None = None, regex: Annotated[str | None, None] = None, discriminator: str | None = None, strict: bool | None = ..., multiple_of: float | None = ..., allow_inf_nan: bool | None = ..., max_digits: int | None = ..., decimal_places: int | None = ..., examples: List[Any] | None = None, example: Annotated[Any | None, None] = ..., openapi_examples: Dict[str, Example] | None = None, deprecated: bool | None = None, include_in_schema: bool = True, json_schema_extra: Dict[str, Any] | None = None, **extra: Any) -> None: ...

class File(Form):
    def __init__(self, default: Any = ..., *, default_factory: Callable[[], Any] | None = ..., annotation: Any | None = None, media_type: str = 'multipart/form-data', alias: str | None = None, alias_priority: int | None = ..., validation_alias: str | None = None, serialization_alias: str | None = None, title: str | None = None, description: str | None = None, gt: float | None = None, ge: float | None = None, lt: float | None = None, le: float | None = None, min_length: int | None = None, max_length: int | None = None, pattern: str | None = None, regex: Annotated[str | None, None] = None, discriminator: str | None = None, strict: bool | None = ..., multiple_of: float | None = ..., allow_inf_nan: bool | None = ..., max_digits: int | None = ..., decimal_places: int | None = ..., examples: List[Any] | None = None, example: Annotated[Any | None, None] = ..., openapi_examples: Dict[str, Example] | None = None, deprecated: bool | None = None, include_in_schema: bool = True, json_schema_extra: Dict[str, Any] | None = None, **extra: Any) -> None: ...

class Depends:
    dependency: Incomplete
    use_cache: Incomplete
    def __init__(self, dependency: Callable[..., Any] | None = None, *, use_cache: bool = True) -> None: ...

class Security(Depends):
    scopes: Incomplete
    def __init__(self, dependency: Callable[..., Any] | None = None, *, scopes: Sequence[str] | None = None, use_cache: bool = True) -> None: ...
