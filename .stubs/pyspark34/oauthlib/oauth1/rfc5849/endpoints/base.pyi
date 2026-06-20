from .. import CONTENT_TYPE_FORM_URLENCODED as CONTENT_TYPE_FORM_URLENCODED, SIGNATURE_HMAC_SHA1 as SIGNATURE_HMAC_SHA1, SIGNATURE_HMAC_SHA256 as SIGNATURE_HMAC_SHA256, SIGNATURE_HMAC_SHA512 as SIGNATURE_HMAC_SHA512, SIGNATURE_PLAINTEXT as SIGNATURE_PLAINTEXT, SIGNATURE_RSA_SHA1 as SIGNATURE_RSA_SHA1, SIGNATURE_RSA_SHA256 as SIGNATURE_RSA_SHA256, SIGNATURE_RSA_SHA512 as SIGNATURE_RSA_SHA512, SIGNATURE_TYPE_AUTH_HEADER as SIGNATURE_TYPE_AUTH_HEADER, SIGNATURE_TYPE_BODY as SIGNATURE_TYPE_BODY, SIGNATURE_TYPE_QUERY as SIGNATURE_TYPE_QUERY, errors as errors, signature as signature, utils as utils
from _typeshed import Incomplete
from oauthlib.common import CaseInsensitiveDict as CaseInsensitiveDict, Request as Request, generate_token as generate_token

class BaseEndpoint:
    request_validator: Incomplete
    token_generator: Incomplete
    def __init__(self, request_validator, token_generator: Incomplete | None = None) -> None: ...
