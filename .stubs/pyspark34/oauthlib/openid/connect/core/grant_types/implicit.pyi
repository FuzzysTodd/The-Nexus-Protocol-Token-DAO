from .base import GrantTypeBase as GrantTypeBase
from _typeshed import Incomplete
from oauthlib.oauth2.rfc6749.errors import InvalidRequestError as InvalidRequestError

log: Incomplete

class ImplicitGrant(GrantTypeBase):
    proxy_target: Incomplete
    def __init__(self, request_validator: Incomplete | None = None, **kwargs) -> None: ...
    def add_id_token(self, token, token_handler, request): ...
    def openid_authorization_validator(self, request):
        """Additional validation when following the implicit flow.
        """
