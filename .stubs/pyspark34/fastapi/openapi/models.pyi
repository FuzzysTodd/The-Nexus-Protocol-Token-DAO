from _typeshed import Incomplete
from enum import Enum
from fastapi._compat import CoreSchema as CoreSchema, GetJsonSchemaHandler as GetJsonSchemaHandler, JsonSchemaValue as JsonSchemaValue, PYDANTIC_V2 as PYDANTIC_V2, with_info_plain_validator_function as with_info_plain_validator_function
from fastapi.logger import logger as logger
from pydantic import AnyUrl as AnyUrl, BaseModel, EmailStr
from typing import Any, Callable, Dict, Iterable, List, Set, Type
from typing_extensions import Annotated, Literal, TypedDict

class EmailStr(str):
    @classmethod
    def __get_validators__(cls) -> Iterable[Callable[..., Any]]: ...
    @classmethod
    def validate(cls, v: Any) -> str: ...
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler) -> JsonSchemaValue: ...
    @classmethod
    def __get_pydantic_core_schema__(cls, source: Type[Any], handler: Callable[[Any], CoreSchema]) -> CoreSchema: ...

class Contact(BaseModel):
    name: str | None
    url: AnyUrl | None
    email: EmailStr | None
    model_config: Incomplete
    class Config:
        extra: str

class License(BaseModel):
    name: str
    identifier: str | None
    url: AnyUrl | None
    model_config: Incomplete
    class Config:
        extra: str

class Info(BaseModel):
    title: str
    summary: str | None
    description: str | None
    termsOfService: str | None
    contact: Contact | None
    license: License | None
    version: str
    model_config: Incomplete
    class Config:
        extra: str

class ServerVariable(BaseModel):
    enum: Annotated[List[str] | None, None]
    default: str
    description: str | None
    model_config: Incomplete
    class Config:
        extra: str

class Server(BaseModel):
    url: AnyUrl | str
    description: str | None
    variables: Dict[str, ServerVariable] | None
    model_config: Incomplete
    class Config:
        extra: str

class Reference(BaseModel):
    ref: str

class Discriminator(BaseModel):
    propertyName: str
    mapping: Dict[str, str] | None

class XML(BaseModel):
    name: str | None
    namespace: str | None
    prefix: str | None
    attribute: bool | None
    wrapped: bool | None
    model_config: Incomplete
    class Config:
        extra: str

class ExternalDocumentation(BaseModel):
    description: str | None
    url: AnyUrl
    model_config: Incomplete
    class Config:
        extra: str

class Schema(BaseModel):
    schema_: str | None
    vocabulary: str | None
    id: str | None
    anchor: str | None
    dynamicAnchor: str | None
    ref: str | None
    dynamicRef: str | None
    defs: Dict[str, 'SchemaOrBool'] | None
    comment: str | None
    allOf: List['SchemaOrBool'] | None
    anyOf: List['SchemaOrBool'] | None
    oneOf: List['SchemaOrBool'] | None
    not_: SchemaOrBool | None
    if_: SchemaOrBool | None
    then: SchemaOrBool | None
    else_: SchemaOrBool | None
    dependentSchemas: Dict[str, 'SchemaOrBool'] | None
    prefixItems: List['SchemaOrBool'] | None
    items: SchemaOrBool | List['SchemaOrBool'] | None
    contains: SchemaOrBool | None
    properties: Dict[str, 'SchemaOrBool'] | None
    patternProperties: Dict[str, 'SchemaOrBool'] | None
    additionalProperties: SchemaOrBool | None
    propertyNames: SchemaOrBool | None
    unevaluatedItems: SchemaOrBool | None
    unevaluatedProperties: SchemaOrBool | None
    type: str | None
    enum: List[Any] | None
    const: Any | None
    multipleOf: float | None
    maximum: float | None
    exclusiveMaximum: float | None
    minimum: float | None
    exclusiveMinimum: float | None
    maxLength: int | None
    minLength: int | None
    pattern: str | None
    maxItems: int | None
    minItems: int | None
    uniqueItems: bool | None
    maxContains: int | None
    minContains: int | None
    maxProperties: int | None
    minProperties: int | None
    required: List[str] | None
    dependentRequired: Dict[str, Set[str]] | None
    format: str | None
    contentEncoding: str | None
    contentMediaType: str | None
    contentSchema: SchemaOrBool | None
    title: str | None
    description: str | None
    default: Any | None
    deprecated: bool | None
    readOnly: bool | None
    writeOnly: bool | None
    examples: List[Any] | None
    discriminator: Discriminator | None
    xml: XML | None
    externalDocs: ExternalDocumentation | None
    example: Annotated[Any | None, None]
    model_config: Incomplete
    class Config:
        extra: str
SchemaOrBool = Schema | bool

class Example(TypedDict, total=False):
    summary: str | None
    description: str | None
    value: Any | None
    externalValue: AnyUrl | None

class ParameterInType(Enum):
    query: str
    header: str
    path: str
    cookie: str

class Encoding(BaseModel):
    contentType: str | None
    headers: Dict[str, Header | Reference] | None
    style: str | None
    explode: bool | None
    allowReserved: bool | None
    model_config: Incomplete
    class Config:
        extra: str

class MediaType(BaseModel):
    schema_: Schema | Reference | None
    example: Any | None
    examples: Dict[str, Example | Reference] | None
    encoding: Dict[str, Encoding] | None
    model_config: Incomplete
    class Config:
        extra: str

class ParameterBase(BaseModel):
    description: str | None
    required: bool | None
    deprecated: bool | None
    style: str | None
    explode: bool | None
    allowReserved: bool | None
    schema_: Schema | Reference | None
    example: Any | None
    examples: Dict[str, Example | Reference] | None
    content: Dict[str, MediaType] | None
    model_config: Incomplete
    class Config:
        extra: str

class Parameter(ParameterBase):
    name: str
    in_: ParameterInType

class Header(ParameterBase): ...

class RequestBody(BaseModel):
    description: str | None
    content: Dict[str, MediaType]
    required: bool | None
    model_config: Incomplete
    class Config:
        extra: str

class Link(BaseModel):
    operationRef: str | None
    operationId: str | None
    parameters: Dict[str, Any | str] | None
    requestBody: Any | str | None
    description: str | None
    server: Server | None
    model_config: Incomplete
    class Config:
        extra: str

class Response(BaseModel):
    description: str
    headers: Dict[str, Header | Reference] | None
    content: Dict[str, MediaType] | None
    links: Dict[str, Link | Reference] | None
    model_config: Incomplete
    class Config:
        extra: str

class Operation(BaseModel):
    tags: List[str] | None
    summary: str | None
    description: str | None
    externalDocs: ExternalDocumentation | None
    operationId: str | None
    parameters: List[Parameter | Reference] | None
    requestBody: RequestBody | Reference | None
    responses: Dict[str, Response | Any] | None
    callbacks: Dict[str, Dict[str, 'PathItem'] | Reference] | None
    deprecated: bool | None
    security: List[Dict[str, List[str]]] | None
    servers: List[Server] | None
    model_config: Incomplete
    class Config:
        extra: str

class PathItem(BaseModel):
    ref: str | None
    summary: str | None
    description: str | None
    get: Operation | None
    put: Operation | None
    post: Operation | None
    delete: Operation | None
    options: Operation | None
    head: Operation | None
    patch: Operation | None
    trace: Operation | None
    servers: List[Server] | None
    parameters: List[Parameter | Reference] | None
    model_config: Incomplete
    class Config:
        extra: str

class SecuritySchemeType(Enum):
    apiKey: str
    http: str
    oauth2: str
    openIdConnect: str

class SecurityBase(BaseModel):
    type_: SecuritySchemeType
    description: str | None
    model_config: Incomplete
    class Config:
        extra: str

class APIKeyIn(Enum):
    query: str
    header: str
    cookie: str

class APIKey(SecurityBase):
    type_: SecuritySchemeType
    in_: APIKeyIn
    name: str

class HTTPBase(SecurityBase):
    type_: SecuritySchemeType
    scheme: str

class HTTPBearer(HTTPBase):
    scheme: Literal['bearer']
    bearerFormat: str | None

class OAuthFlow(BaseModel):
    refreshUrl: str | None
    scopes: Dict[str, str]
    model_config: Incomplete
    class Config:
        extra: str

class OAuthFlowImplicit(OAuthFlow):
    authorizationUrl: str

class OAuthFlowPassword(OAuthFlow):
    tokenUrl: str

class OAuthFlowClientCredentials(OAuthFlow):
    tokenUrl: str

class OAuthFlowAuthorizationCode(OAuthFlow):
    authorizationUrl: str
    tokenUrl: str

class OAuthFlows(BaseModel):
    implicit: OAuthFlowImplicit | None
    password: OAuthFlowPassword | None
    clientCredentials: OAuthFlowClientCredentials | None
    authorizationCode: OAuthFlowAuthorizationCode | None
    model_config: Incomplete
    class Config:
        extra: str

class OAuth2(SecurityBase):
    type_: SecuritySchemeType
    flows: OAuthFlows

class OpenIdConnect(SecurityBase):
    type_: SecuritySchemeType
    openIdConnectUrl: str
SecurityScheme = APIKey | HTTPBase | OAuth2 | OpenIdConnect | HTTPBearer

class Components(BaseModel):
    schemas: Dict[str, Schema | Reference] | None
    responses: Dict[str, Response | Reference] | None
    parameters: Dict[str, Parameter | Reference] | None
    examples: Dict[str, Example | Reference] | None
    requestBodies: Dict[str, RequestBody | Reference] | None
    headers: Dict[str, Header | Reference] | None
    securitySchemes: Dict[str, SecurityScheme | Reference] | None
    links: Dict[str, Link | Reference] | None
    callbacks: Dict[str, Dict[str, PathItem] | Reference | Any] | None
    pathItems: Dict[str, PathItem | Reference] | None
    model_config: Incomplete
    class Config:
        extra: str

class Tag(BaseModel):
    name: str
    description: str | None
    externalDocs: ExternalDocumentation | None
    model_config: Incomplete
    class Config:
        extra: str

class OpenAPI(BaseModel):
    openapi: str
    info: Info
    jsonSchemaDialect: str | None
    servers: List[Server] | None
    paths: Dict[str, PathItem | Any] | None
    webhooks: Dict[str, PathItem | Reference] | None
    components: Components | None
    security: List[Dict[str, List[str]]] | None
    tags: List[Tag] | None
    externalDocs: ExternalDocumentation | None
    model_config: Incomplete
    class Config:
        extra: str
