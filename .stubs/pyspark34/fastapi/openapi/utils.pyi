from _typeshed import Incomplete
from fastapi import routing as routing
from fastapi._compat import GenerateJsonSchema as GenerateJsonSchema, JsonSchemaValue as JsonSchemaValue, ModelField as ModelField, Undefined as Undefined, get_compat_model_name_map as get_compat_model_name_map, get_definitions as get_definitions, get_schema_from_model_field as get_schema_from_model_field, lenient_issubclass as lenient_issubclass
from fastapi.datastructures import DefaultPlaceholder as DefaultPlaceholder
from fastapi.dependencies.models import Dependant as Dependant
from fastapi.dependencies.utils import get_flat_dependant as get_flat_dependant, get_flat_params as get_flat_params
from fastapi.encoders import jsonable_encoder as jsonable_encoder
from fastapi.openapi.constants import METHODS_WITH_BODY as METHODS_WITH_BODY, REF_PREFIX as REF_PREFIX, REF_TEMPLATE as REF_TEMPLATE
from fastapi.openapi.models import OpenAPI as OpenAPI
from fastapi.params import Body as Body, Param as Param
from fastapi.responses import Response as Response
from fastapi.types import ModelNameMap as ModelNameMap
from fastapi.utils import deep_dict_update as deep_dict_update, generate_operation_id_for_path as generate_operation_id_for_path, is_body_allowed_for_status_code as is_body_allowed_for_status_code
from starlette.routing import BaseRoute as BaseRoute
from typing import Any, Dict, List, Sequence, Set, Tuple
from typing_extensions import Literal

validation_error_definition: Incomplete
validation_error_response_definition: Incomplete
status_code_ranges: Dict[str, str]

def get_openapi_security_definitions(flat_dependant: Dependant) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]: ...
def get_openapi_operation_parameters(*, all_route_params: Sequence[ModelField], schema_generator: GenerateJsonSchema, model_name_map: ModelNameMap, field_mapping: Dict[Tuple[ModelField, Literal['validation', 'serialization']], JsonSchemaValue], separate_input_output_schemas: bool = True) -> List[Dict[str, Any]]: ...
def get_openapi_operation_request_body(*, body_field: ModelField | None, schema_generator: GenerateJsonSchema, model_name_map: ModelNameMap, field_mapping: Dict[Tuple[ModelField, Literal['validation', 'serialization']], JsonSchemaValue], separate_input_output_schemas: bool = True) -> Dict[str, Any] | None: ...
def generate_operation_id(*, route: routing.APIRoute, method: str) -> str: ...
def generate_operation_summary(*, route: routing.APIRoute, method: str) -> str: ...
def get_openapi_operation_metadata(*, route: routing.APIRoute, method: str, operation_ids: Set[str]) -> Dict[str, Any]: ...
def get_openapi_path(*, route: routing.APIRoute, operation_ids: Set[str], schema_generator: GenerateJsonSchema, model_name_map: ModelNameMap, field_mapping: Dict[Tuple[ModelField, Literal['validation', 'serialization']], JsonSchemaValue], separate_input_output_schemas: bool = True) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]: ...
def get_fields_from_routes(routes: Sequence[BaseRoute]) -> List[ModelField]: ...
def get_openapi(*, title: str, version: str, openapi_version: str = '3.1.0', summary: str | None = None, description: str | None = None, routes: Sequence[BaseRoute], webhooks: Sequence[BaseRoute] | None = None, tags: List[Dict[str, Any]] | None = None, servers: List[Dict[str, str | Any]] | None = None, terms_of_service: str | None = None, contact: Dict[str, str | Any] | None = None, license_info: Dict[str, str | Any] | None = None, separate_input_output_schemas: bool = True) -> Dict[str, Any]: ...
