from ..grant_types import AuthorizationCodeGrant as AuthorizationCodeGrant, HybridGrant as HybridGrant, ImplicitGrant as ImplicitGrant
from ..grant_types.dispatchers import AuthorizationCodeGrantDispatcher as AuthorizationCodeGrantDispatcher, AuthorizationTokenGrantDispatcher as AuthorizationTokenGrantDispatcher, ImplicitTokenGrantDispatcher as ImplicitTokenGrantDispatcher
from ..tokens import JWTToken as JWTToken
from .userinfo import UserInfoEndpoint as UserInfoEndpoint
from _typeshed import Incomplete
from oauthlib.oauth2.rfc6749.endpoints import AuthorizationEndpoint as AuthorizationEndpoint, IntrospectEndpoint as IntrospectEndpoint, ResourceEndpoint as ResourceEndpoint, RevocationEndpoint as RevocationEndpoint, TokenEndpoint as TokenEndpoint
from oauthlib.oauth2.rfc6749.grant_types import ClientCredentialsGrant as ClientCredentialsGrant, RefreshTokenGrant as RefreshTokenGrant, ResourceOwnerPasswordCredentialsGrant as ResourceOwnerPasswordCredentialsGrant
from oauthlib.oauth2.rfc6749.tokens import BearerToken as BearerToken

class Server(AuthorizationEndpoint, IntrospectEndpoint, TokenEndpoint, ResourceEndpoint, RevocationEndpoint, UserInfoEndpoint):
    """An all-in-one endpoint featuring all four major grant types."""
    auth_grant: Incomplete
    implicit_grant: Incomplete
    password_grant: Incomplete
    credentials_grant: Incomplete
    refresh_grant: Incomplete
    openid_connect_auth: Incomplete
    openid_connect_implicit: Incomplete
    openid_connect_hybrid: Incomplete
    bearer: Incomplete
    jwt: Incomplete
    auth_grant_choice: Incomplete
    implicit_grant_choice: Incomplete
    token_grant_choice: Incomplete
    def __init__(self, request_validator, token_expires_in: Incomplete | None = None, token_generator: Incomplete | None = None, refresh_token_generator: Incomplete | None = None, *args, **kwargs) -> None:
        """Construct a new all-grants-in-one server.

        :param request_validator: An implementation of
                                  oauthlib.oauth2.RequestValidator.
        :param token_expires_in: An int or a function to generate a token
                                 expiration offset (in seconds) given a
                                 oauthlib.common.Request object.
        :param token_generator: A function to generate a token from a request.
        :param refresh_token_generator: A function to generate a token from a
                                        request for the refresh token.
        :param kwargs: Extra parameters to pass to authorization-,
                       token-, resource-, and revocation-endpoint constructors.
        """
