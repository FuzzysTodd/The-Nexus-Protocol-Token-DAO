from _typeshed import Incomplete

class Errors:
    ERROR_VALUE_NONE: str
    ERROR_VALUE_EMPTY_STRING: str
    ERROR_RESPONSE_MALFORMED_XML: str

class OAuth2Parameters:
    GRANT_TYPE: str
    CLIENT_ASSERTION: str
    CLIENT_ASSERTION_TYPE: str
    CLIENT_ID: str
    CLIENT_SECRET: str
    REDIRECT_URI: str
    RESOURCE: str
    CODE: str
    CODE_VERIFIER: str
    SCOPE: str
    ASSERTION: str
    AAD_API_VERSION: str
    USERNAME: str
    PASSWORD: str
    REFRESH_TOKEN: str
    LANGUAGE: str
    DEVICE_CODE: str

class OAuth2GrantType:
    AUTHORIZATION_CODE: str
    REFRESH_TOKEN: str
    CLIENT_CREDENTIALS: str
    JWT_BEARER: str
    PASSWORD: str
    SAML1: str
    SAML2: str
    DEVICE_CODE: str

class OAuth2ResponseParameters:
    CODE: str
    TOKEN_TYPE: str
    ACCESS_TOKEN: str
    ID_TOKEN: str
    REFRESH_TOKEN: str
    CREATED_ON: str
    EXPIRES_ON: str
    EXPIRES_IN: str
    RESOURCE: str
    ERROR: str
    ERROR_DESCRIPTION: str

class OAuth2DeviceCodeResponseParameters:
    USER_CODE: str
    DEVICE_CODE: str
    VERIFICATION_URL: str
    EXPIRES_IN: str
    INTERVAL: str
    MESSAGE: str
    ERROR: str
    ERROR_DESCRIPTION: str

class OAuth2Scope:
    OPENID: str

class OAuth2:
    Parameters: Incomplete
    GrantType: Incomplete
    ResponseParameters: Incomplete
    DeviceCodeResponseParameters: Incomplete
    Scope: Incomplete
    IdTokenMap: Incomplete

class TokenResponseFields:
    TOKEN_TYPE: str
    ACCESS_TOKEN: str
    REFRESH_TOKEN: str
    CREATED_ON: str
    EXPIRES_ON: str
    EXPIRES_IN: str
    RESOURCE: str
    USER_ID: str
    ERROR: str
    ERROR_DESCRIPTION: str
    IS_MRRT: str

class IdTokenFields:
    USER_ID: str
    IS_USER_ID_DISPLAYABLE: str
    TENANT_ID: str
    GIVE_NAME: str
    FAMILY_NAME: str
    IDENTITY_PROVIDER: str

class Misc:
    MAX_DATE: int
    CLOCK_BUFFER: int

class Jwt:
    SELF_SIGNED_JWT_LIFETIME: int
    AUDIENCE: str
    ISSUER: str
    SUBJECT: str
    NOT_BEFORE: str
    EXPIRES_ON: str
    JWT_ID: str

class UserRealm:
    federation_protocol_type: Incomplete
    account_type: Incomplete

class Saml:
    TokenTypeV1: str
    TokenTypeV2: str
    OasisWssSaml11TokenProfile11: str
    OasisWssSaml2TokenProfile2: str

class XmlNamespaces:
    namespaces: Incomplete

class Cache:
    HASH_ALGORITHM: str

class HttpError:
    UNAUTHORIZED: int

class AADConstants:
    WORLD_WIDE_AUTHORITY: str
    WELL_KNOWN_AUTHORITY_HOSTS: Incomplete
    INSTANCE_DISCOVERY_ENDPOINT_TEMPLATE: str
    AUTHORIZE_ENDPOINT_PATH: str
    TOKEN_ENDPOINT_PATH: str
    DEVICE_ENDPOINT_PATH: str

class AdalIdParameters:
    SKU: str
    VERSION: str
    OS: str
    CPU: str
    PYTHON_SKU: str

class WSTrustVersion:
    UNDEFINED: str
    WSTRUST13: str
    WSTRUST2005: str
