from ..request_validator import RequestValidator as RequestValidator
from ..utils import is_secure_transport as is_secure_transport
from _typeshed import Incomplete
from oauthlib.common import add_params_to_uri as add_params_to_uri
from oauthlib.oauth2.rfc6749 import errors as errors, utils as utils
from oauthlib.uri_validate import is_absolute_uri as is_absolute_uri

log: Incomplete

class ValidatorsContainer:
    '''
    Container object for holding custom validator callables to be invoked
    as part of the grant type `validate_authorization_request()` or
    `validate_authorization_request()` methods on the various grant types.

    Authorization validators must be callables that take a request object and
    return a dict, which may contain items to be added to the `request_info`
    returned from the grant_type after validation.

    Token validators must be callables that take a request object and
    return None.

    Both authorization validators and token validators may raise OAuth2
    exceptions if validation conditions fail.

    Authorization validators added to `pre_auth` will be run BEFORE
    the standard validations (but after the critical ones that raise
    fatal errors) as part of `validate_authorization_request()`

    Authorization validators added to `post_auth` will be run AFTER
    the standard validations as part of `validate_authorization_request()`

    Token validators added to `pre_token` will be run BEFORE
    the standard validations as part of `validate_token_request()`

    Token validators added to `post_token` will be run AFTER
    the standard validations as part of `validate_token_request()`

    For example:

    >>> def my_auth_validator(request):
    ...    return {\'myval\': True}
    >>> auth_code_grant = AuthorizationCodeGrant(request_validator)
    >>> auth_code_grant.custom_validators.pre_auth.append(my_auth_validator)
    >>> def my_token_validator(request):
    ...     if not request.everything_okay:
    ...         raise errors.OAuth2Error("uh-oh")
    >>> auth_code_grant.custom_validators.post_token.append(my_token_validator)
    '''
    pre_auth: Incomplete
    post_auth: Incomplete
    pre_token: Incomplete
    post_token: Incomplete
    def __init__(self, post_auth, post_token, pre_auth, pre_token) -> None: ...
    @property
    def all_pre(self): ...
    @property
    def all_post(self): ...

class GrantTypeBase:
    error_uri: Incomplete
    request_validator: Incomplete
    default_response_mode: str
    refresh_token: bool
    response_types: Incomplete
    def __init__(self, request_validator: Incomplete | None = None, **kwargs) -> None: ...
    def register_response_type(self, response_type) -> None: ...
    def register_code_modifier(self, modifier) -> None: ...
    def register_token_modifier(self, modifier) -> None: ...
    def create_authorization_response(self, request, token_handler) -> None:
        """
        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        :param token_handler: A token handler instance, for example of type
                              oauthlib.oauth2.BearerToken.
        """
    def create_token_response(self, request, token_handler) -> None:
        """
        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        :param token_handler: A token handler instance, for example of type
                              oauthlib.oauth2.BearerToken.
        """
    def add_token(self, token, token_handler, request):
        """
        :param token:
        :param token_handler: A token handler instance, for example of type
                              oauthlib.oauth2.BearerToken.
        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        """
    def validate_grant_type(self, request) -> None:
        """
        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        """
    def validate_scopes(self, request) -> None:
        """
        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        """
    def prepare_authorization_response(self, request, token, headers, body, status):
        """Place token according to response mode.

        Base classes can define a default response mode for their authorization
        response by overriding the static `default_response_mode` member.

        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        :param token:
        :param headers:
        :param body:
        :param status:
        """
