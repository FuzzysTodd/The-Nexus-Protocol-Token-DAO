from _typeshed import Incomplete
from oauthlib.oauth2.rfc6749.tokens import TokenBase as TokenBase, get_token_from_header as get_token_from_header, random_token_generator as random_token_generator

class JWTToken(TokenBase):
    request_validator: Incomplete
    token_generator: Incomplete
    refresh_token_generator: Incomplete
    expires_in: Incomplete
    def __init__(self, request_validator: Incomplete | None = None, token_generator: Incomplete | None = None, expires_in: Incomplete | None = None, refresh_token_generator: Incomplete | None = None) -> None: ...
    def create_token(self, request, refresh_token: bool = False):
        """Create a JWT Token, using requestvalidator method."""
    def validate_request(self, request): ...
    def estimate_type(self, request): ...
