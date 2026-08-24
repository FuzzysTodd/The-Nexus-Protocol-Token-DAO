from _typeshed import Incomplete

log: Incomplete

class Dispatcher:
    default_grant: Incomplete
    oidc_grant: Incomplete

class AuthorizationCodeGrantDispatcher(Dispatcher):
    """
    This is an adapter class that will route simple Authorization Code
    requests, those that have `response_type=code` and a scope including
    `openid` to either the `default_grant` or the `oidc_grant` based on
    the scopes requested.
    """
    default_grant: Incomplete
    oidc_grant: Incomplete
    def __init__(self, default_grant: Incomplete | None = None, oidc_grant: Incomplete | None = None) -> None: ...
    def create_authorization_response(self, request, token_handler):
        """Read scope and route to the designated handler."""
    def validate_authorization_request(self, request):
        """Read scope and route to the designated handler."""

class ImplicitTokenGrantDispatcher(Dispatcher):
    """
    This is an adapter class that will route simple Authorization
    requests, those that have `id_token` in `response_type` and a scope
    including `openid` to either the `default_grant` or the `oidc_grant`
    based on the scopes requested.
    """
    default_grant: Incomplete
    oidc_grant: Incomplete
    def __init__(self, default_grant: Incomplete | None = None, oidc_grant: Incomplete | None = None) -> None: ...
    def create_authorization_response(self, request, token_handler):
        """Read scope and route to the designated handler."""
    def validate_authorization_request(self, request):
        """Read scope and route to the designated handler."""

class AuthorizationTokenGrantDispatcher(Dispatcher):
    """
    This is an adapter class that will route simple Token requests, those that authorization_code have a scope
    including 'openid' to either the default_grant or the oidc_grant based on the scopes requested.
    """
    default_grant: Incomplete
    oidc_grant: Incomplete
    request_validator: Incomplete
    def __init__(self, request_validator, default_grant: Incomplete | None = None, oidc_grant: Incomplete | None = None) -> None: ...
    def create_token_response(self, request, token_handler):
        """Read scope and route to the designated handler."""
