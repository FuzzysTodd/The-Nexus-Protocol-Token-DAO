from .security import passwd_check as passwd_check, set_password as set_password
from .utils import get_anonymous_username as get_anonymous_username
from _typeshed import Incomplete
from dataclasses import dataclass
from jupyter_server.base.handlers import JupyterHandler as JupyterHandler
from jupyter_server.serverapp import ServerApp as ServerApp
from traitlets import Bool, Unicode
from traitlets.config import LoggingConfigurable
from typing import Awaitable

@dataclass
class User:
    """Object representing a User

    This or a subclass should be returned from IdentityProvider.get_user
    """
    username: str
    name: str = ...
    display_name: str = ...
    initials: str | None = ...
    avatar_url: str | None = ...
    color: str | None = ...
    def __post_init__(self) -> None: ...
    def fill_defaults(self) -> None:
        """Fill out default fields in the identity model

        - Ensures all values are defined
        - Fills out derivative values for name fields fields
        - Fills out null values for optional fields
        """
    def __init__(self, username, name, display_name, initials, avatar_url, color) -> None: ...

class IdentityProvider(LoggingConfigurable):
    """
    Interface for providing identity management and authentication.

    Two principle methods:

    - :meth:`~jupyter_server.auth.IdentityProvider.get_user` returns a :class:`~.User` object
      for successful authentication, or None for no-identity-found.
    - :meth:`~jupyter_server.auth.IdentityProvider.identity_model` turns a :class:`~jupyter_server.auth.User` into a JSONable dict.
      The default is to use :py:meth:`dataclasses.asdict`,
      and usually shouldn't need override.

    Additional methods can customize authentication.

    .. versionadded:: 2.0
    """
    cookie_name: str | Unicode
    cookie_options: Incomplete
    secure_cookie: bool | Bool
    get_secure_cookie_kwargs: Incomplete
    token: str | Unicode
    login_handler_class: Incomplete
    logout_handler_class: Incomplete
    token_generated: bool
    need_token: bool | Bool
    def get_user(self, handler: JupyterHandler) -> User | None | Awaitable[User | None]:
        """Get the authenticated user for a request

        Must return a :class:`jupyter_server.auth.User`,
        though it may be a subclass.

        Return None if the request is not authenticated.

        _may_ be a coroutine
        """
    def identity_model(self, user: User) -> dict:
        """Return a User as an Identity model"""
    def get_handlers(self) -> list:
        """Return list of additional handlers for this identity provider

        For example, an OAuth callback handler.
        """
    def user_to_cookie(self, user: User) -> str:
        """Serialize a user to a string for storage in a cookie

        If overriding in a subclass, make sure to define user_from_cookie as well.

        Default is just the user's username.
        """
    def user_from_cookie(self, cookie_value: str) -> User | None:
        """Inverse of user_to_cookie"""
    def get_cookie_name(self, handler: JupyterHandler) -> str:
        """Return the login cookie name

        Uses IdentityProvider.cookie_name, if defined.
        Default is to generate a string taking host into account to avoid
        collisions for multiple servers on one hostname with different ports.
        """
    def set_login_cookie(self, handler: JupyterHandler, user: User) -> None:
        """Call this on handlers to set the login cookie for success"""
    def clear_login_cookie(self, handler: JupyterHandler) -> None:
        """Clear the login cookie, effectively logging out the session."""
    def get_user_cookie(self, handler: JupyterHandler) -> User | None | Awaitable[User | None]:
        """Get user from a cookie

        Calls user_from_cookie to deserialize cookie value
        """
    auth_header_pat: Incomplete
    def get_token(self, handler: JupyterHandler) -> str | None:
        """Get the user token from a request

        Default:

        - in URL parameters: ?token=<token>
        - in header: Authorization: token <token>
        """
    async def get_user_token(self, handler: JupyterHandler) -> User | None:
        """Identify the user based on a token in the URL or Authorization header

        Returns:
        - uuid if authenticated
        - None if not
        """
    def generate_anonymous_user(self, handler: JupyterHandler) -> User:
        """Generate a random anonymous user.

        For use when a single shared token is used,
        but does not identify a user.
        """
    def should_check_origin(self, handler: JupyterHandler) -> bool:
        """Should the Handler check for CORS origin validation?

        Origin check should be skipped for token-authenticated requests.

        Returns:
        - True, if Handler must check for valid CORS origin.
        - False, if Handler should skip origin check since requests are token-authenticated.
        """
    def is_token_authenticated(self, handler: JupyterHandler) -> bool:
        """Returns True if handler has been token authenticated. Otherwise, False.

        Login with a token is used to signal certain things, such as:

        - permit access to REST API
        - xsrf protection
        - skip origin-checks for scripts
        """
    def validate_security(self, app: ServerApp, ssl_options: dict | None = None) -> None:
        """Check the application's security.

        Show messages, or abort if necessary, based on the security configuration.
        """
    def process_login_form(self, handler: JupyterHandler) -> User | None:
        """Process login form data

        Return authenticated User if successful, None if not.
        """
    @property
    def auth_enabled(self):
        """Is authentication enabled?

        Should always be True, but may be False in rare, insecure cases
        where requests with no auth are allowed.

        Previously: LoginHandler.get_login_available
        """
    @property
    def login_available(self):
        """Whether a LoginHandler is needed - and therefore whether the login page should be displayed."""
    @property
    def logout_available(self):
        """Whether a LogoutHandler is needed."""

class PasswordIdentityProvider(IdentityProvider):
    """A password identity provider."""
    hashed_password: Incomplete
    password_required: Incomplete
    allow_password_change: Incomplete
    @property
    def login_available(self) -> bool:
        """Whether a LoginHandler is needed - and therefore whether the login page should be displayed."""
    @property
    def auth_enabled(self) -> bool:
        """Return whether any auth is enabled"""
    def passwd_check(self, password):
        """Check password against our stored hashed password"""
    def process_login_form(self, handler: JupyterHandler) -> User | None:
        """Process login form data

        Return authenticated User if successful, None if not.
        """
    def validate_security(self, app: ServerApp, ssl_options: dict | None = None) -> None:
        """Handle security validation."""

class LegacyIdentityProvider(PasswordIdentityProvider):
    """Legacy IdentityProvider for use with custom LoginHandlers

    Login configuration has moved from LoginHandler to IdentityProvider
    in Jupyter Server 2.0.
    """
    settings: Incomplete
    @property
    def auth_enabled(self): ...
    def get_user(self, handler: JupyterHandler) -> User | None:
        """Get the user."""
    @property
    def login_available(self): ...
    def should_check_origin(self, handler: JupyterHandler) -> bool:
        """Whether we should check origin."""
    def is_token_authenticated(self, handler: JupyterHandler) -> bool:
        """Whether we are token authenticated."""
    def validate_security(self, app: ServerApp, ssl_options: dict | None = None) -> None:
        """Validate security."""
