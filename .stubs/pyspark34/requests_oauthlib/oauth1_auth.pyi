from _typeshed import Incomplete
from oauthlib.oauth1 import Client
from requests.auth import AuthBase

CONTENT_TYPE_FORM_URLENCODED: str
CONTENT_TYPE_MULTI_PART: str
unicode = str
log: Incomplete

class OAuth1(AuthBase):
    """Signs the request using OAuth 1 (RFC5849)"""
    client_class = Client
    force_include_body: Incomplete
    client: Incomplete
    def __init__(self, client_key, client_secret: Incomplete | None = None, resource_owner_key: Incomplete | None = None, resource_owner_secret: Incomplete | None = None, callback_uri: Incomplete | None = None, signature_method=..., signature_type=..., rsa_key: Incomplete | None = None, verifier: Incomplete | None = None, decoding: str = 'utf-8', client_class: Incomplete | None = None, force_include_body: bool = False, **kwargs) -> None: ...
    def __call__(self, r):
        """Add OAuth parameters to the request.

        Parameters may be included from the body if the content-type is
        urlencoded, if no content type is set a guess is made.
        """
