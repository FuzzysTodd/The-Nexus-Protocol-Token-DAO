from ..base.handlers import JupyterHandler as JupyterHandler
from .security import passwd_check as passwd_check, set_password as set_password
from _typeshed import Incomplete

class LoginFormHandler(JupyterHandler):
    """The basic tornado login handler

    accepts login form, passed to IdentityProvider.process_login_form.
    """
    def get(self) -> None:
        """Get the login form."""
    def post(self) -> None:
        """Post a login."""

class LegacyLoginHandler(LoginFormHandler):
    """Legacy LoginHandler, implementing most custom auth configuration.

    Deprecated in jupyter-server 2.0.
    Login configuration has moved to IdentityProvider.
    """
    @property
    def hashed_password(self): ...
    def passwd_check(self, a, b):
        """Check a passwd."""
    def post(self) -> None:
        """Post a login form."""
    @classmethod
    def set_login_cookie(cls, handler, user_id: Incomplete | None = None):
        """Call this on handlers to set the login cookie for success"""
    auth_header_pat: Incomplete
    @classmethod
    def get_token(cls, handler):
        """Get the user token from a request

        Default:

        - in URL parameters: ?token=<token>
        - in header: Authorization: token <token>
        """
    @classmethod
    def should_check_origin(cls, handler):
        """DEPRECATED in 2.0, use IdentityProvider API"""
    @classmethod
    def is_token_authenticated(cls, handler):
        """DEPRECATED in 2.0, use IdentityProvider API"""
    @classmethod
    def get_user(cls, handler):
        """DEPRECATED in 2.0, use IdentityProvider API"""
    @classmethod
    def get_user_cookie(cls, handler):
        """DEPRECATED in 2.0, use IdentityProvider API"""
    @classmethod
    def get_user_token(cls, handler):
        """DEPRECATED in 2.0, use IdentityProvider API"""
    @classmethod
    def validate_security(cls, app, ssl_options: Incomplete | None = None) -> None:
        """DEPRECATED in 2.0, use IdentityProvider API"""
    @classmethod
    def password_from_settings(cls, settings):
        """DEPRECATED in 2.0, use IdentityProvider API"""
    @classmethod
    def get_login_available(cls, settings):
        """DEPRECATED in 2.0, use IdentityProvider API"""
LoginHandler = LegacyLoginHandler
