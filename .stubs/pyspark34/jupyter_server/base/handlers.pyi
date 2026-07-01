from _typeshed import Incomplete
from jupyter_events import EventLogger as EventLogger
from jupyter_server import CallContext as CallContext
from jupyter_server._sysinfo import get_sys_info as get_sys_info
from jupyter_server._tz import utcnow as utcnow
from jupyter_server.auth import authorized as authorized
from jupyter_server.auth.identity import User as User
from jupyter_server.i18n import combine_translations as combine_translations
from jupyter_server.services.security import csp_report_uri as csp_report_uri
from jupyter_server.utils import ensure_async as ensure_async, filefind as filefind, url_escape as url_escape, url_is_absolute as url_is_absolute, url_path_join as url_path_join, urldecode_unix_socket_path as urldecode_unix_socket_path
from tornado import web

def json_sys_info():
    """Get sys info as json."""
def log():
    """Get the application log."""

class AuthenticatedHandler(web.RequestHandler):
    """A RequestHandler with an authenticated user."""
    @property
    def base_url(self) -> str: ...
    @property
    def content_security_policy(self):
        """The default Content-Security-Policy header

        Can be overridden by defining Content-Security-Policy in settings['headers']
        """
    def set_default_headers(self) -> None:
        """Set the default headers."""
    @property
    def cookie_name(self): ...
    def force_clear_cookie(self, name, path: str = '/', domain: Incomplete | None = None):
        """Force a cookie clear."""
    def clear_login_cookie(self):
        """Clear a login cookie."""
    def get_current_user(self):
        """Get the current user."""
    def skip_check_origin(self):
        """Ask my login_handler if I should skip the origin_check

        For example: in the default LoginHandler, if a request is token-authenticated,
        origin checking should be skipped.
        """
    @property
    def token_authenticated(self):
        """Have I been authenticated with a token?"""
    @property
    def logged_in(self):
        """Is a user currently logged in?"""
    @property
    def login_handler(self):
        """Return the login handler for this application, if any."""
    @property
    def token(self):
        """Return the login token for this application, if any."""
    @property
    def login_available(self):
        """May a user proceed to log in?

        This returns True if login capability is available, irrespective of
        whether the user is already logged in or not.

        """
    @property
    def authorizer(self): ...
    @property
    def identity_provider(self): ...

class JupyterHandler(AuthenticatedHandler):
    """Jupyter-specific extensions to authenticated handling

    Mostly property shortcuts to Jupyter-specific settings.
    """
    @property
    def config(self): ...
    @property
    def log(self):
        """use the Jupyter log by default, falling back on tornado's logger"""
    @property
    def jinja_template_vars(self):
        """User-supplied values to supply to jinja templates."""
    @property
    def serverapp(self): ...
    @property
    def version_hash(self):
        """The version hash to use for cache hints for static files"""
    @property
    def mathjax_url(self): ...
    @property
    def mathjax_config(self): ...
    @property
    def default_url(self): ...
    @property
    def ws_url(self): ...
    @property
    def contents_js_source(self): ...
    @property
    def kernel_manager(self): ...
    @property
    def contents_manager(self): ...
    @property
    def session_manager(self): ...
    @property
    def terminal_manager(self): ...
    @property
    def kernel_spec_manager(self): ...
    @property
    def config_manager(self): ...
    @property
    def event_logger(self) -> EventLogger: ...
    @property
    def allow_origin(self):
        """Normal Access-Control-Allow-Origin"""
    @property
    def allow_origin_pat(self):
        """Regular expression version of allow_origin"""
    @property
    def allow_credentials(self):
        """Whether to set Access-Control-Allow-Credentials"""
    def set_default_headers(self) -> None:
        """Add CORS headers, if defined"""
    def set_cors_headers(self) -> None:
        """Add CORS headers, if defined

        Now that current_user is async (jupyter-server 2.0),
        must be called at the end of prepare(), instead of in set_default_headers.
        """
    def set_attachment_header(self, filename) -> None:
        """Set Content-Disposition: attachment header

        As a method to ensure handling of filename encoding
        """
    def get_origin(self): ...
    def check_origin(self, origin_to_satisfy_tornado: str = ''):
        """Check Origin for cross-site API requests, including websockets

        Copied from WebSocket with changes:

        - allow unspecified host/origin (e.g. scripts)
        - allow token-authenticated requests
        """
    def check_referer(self):
        """Check Referer for cross-site requests.
        Disables requests to certain endpoints with
        external or missing Referer.
        If set, allow_origin settings are applied to the Referer
        to whitelist specific cross-origin sites.
        Used on GET for api endpoints and /files/
        to block cross-site inclusion (XSSI).
        """
    def check_xsrf_cookie(self):
        """Bypass xsrf cookie checks when token-authenticated"""
    def check_host(self):
        """Check the host header if remote access disallowed.

        Returns True if the request should continue, False otherwise.
        """
    current_user: Incomplete
    async def prepare(self):
        """Pepare a response."""
    def get_template(self, name):
        """Return the jinja template object for a given name"""
    def render_template(self, name, **ns):
        """Render a template by name."""
    @property
    def template_namespace(self): ...
    def get_json_body(self):
        """Return the body of the request as JSON data."""
    def write_error(self, status_code, **kwargs) -> None:
        """render custom error pages"""

class APIHandler(JupyterHandler):
    """Base class for API handlers"""
    async def prepare(self) -> None:
        """Prepare an API response."""
    def write_error(self, status_code, **kwargs) -> None:
        """APIHandler errors are JSON, not human pages"""
    def get_login_url(self):
        """Get the login url."""
    @property
    def content_security_policy(self): ...
    def update_api_activity(self) -> None:
        """Update last_activity of API requests"""
    def finish(self, *args, **kwargs):
        """Finish an API response."""
    def options(self, *args, **kwargs) -> None:
        """Get the options."""

class Template404(JupyterHandler):
    """Render our 404 template"""
    async def prepare(self) -> None:
        """Prepare a 404 response."""

class AuthenticatedFileHandler(JupyterHandler, web.StaticFileHandler):
    """static files should only be accessible when logged in"""
    auth_resource: str
    @property
    def content_security_policy(self): ...
    def head(self, path):
        """Get the head response for a path."""
    def get(self, path, **kwargs):
        """Get a file by path."""
    def get_content_type(self):
        """Get the content type."""
    def set_headers(self) -> None:
        """Set the headers."""
    def compute_etag(self) -> None:
        """Compute the etag."""
    def validate_absolute_path(self, root, absolute_path):
        """Validate and return the absolute path.

        Requires tornado 3.1

        Adding to tornado's own handling, forbids the serving of hidden files.
        """

def json_errors(method):
    """Decorate methods with this to return GitHub style JSON errors.

    This should be used on any JSON API on any handler method that can raise HTTPErrors.

    This will grab the latest HTTPError exception using sys.exc_info
    and then:

    1. Set the HTTP status code based on the HTTPError
    2. Create and return a JSON body with a message field describing
       the error in a human readable form.
    """

HTTPError: Incomplete

class FileFindHandler(JupyterHandler, web.StaticFileHandler):
    '''subclass of StaticFileHandler for serving files from a search path

    The setting "static_immutable_cache" can be set up to serve some static
    file as immutable (e.g. file name containing a hash). The setting is a
    list of base URL, every static file URL starting with one of those will
    be immutable.
    '''
    root: tuple
    def set_headers(self) -> None:
        """Set the headers."""
    no_cache_paths: Incomplete
    default_filename: Incomplete
    def initialize(self, path, default_filename: Incomplete | None = None, no_cache_paths: Incomplete | None = None) -> None:
        """Initialize the file find handler."""
    def compute_etag(self) -> None:
        """Compute the etag."""
    @classmethod
    def get_absolute_path(cls, roots, path):
        """locate a file to serve on our static file search path"""
    def validate_absolute_path(self, root, absolute_path):
        """check if the file should be served (raises 404, 403, etc.)"""

class APIVersionHandler(APIHandler):
    """An API handler for the server version."""
    def get(self) -> None:
        """Get the server version info."""

class TrailingSlashHandler(web.RequestHandler):
    """Simple redirect handler that strips trailing slashes

    This should be the first, highest priority handler.
    """
    def get(self) -> None:
        """Handle trailing slashes in a get."""
    post = get
    put = get

class MainHandler(JupyterHandler):
    """Simple handler for base_url."""
    def get(self) -> None:
        """Get the main template."""
    post = get
    put = get

class FilesRedirectHandler(JupyterHandler):
    """Handler for redirecting relative URLs to the /files/ handler"""
    @staticmethod
    async def redirect_to_files(self, path) -> None:
        """make redirect logic a reusable static method

        so it can be called from other handlers.
        """
    def get(self, path: str = ''): ...

class RedirectWithParams(web.RequestHandler):
    """Sam as web.RedirectHandler, but preserves URL parameters"""
    def initialize(self, url, permanent: bool = True) -> None:
        """Initialize a redirect handler."""
    def get(self) -> None:
        """Get a redirect."""

class PrometheusMetricsHandler(JupyterHandler):
    """
    Return prometheus metrics for this server
    """
    def get(self) -> None:
        """Get prometheus metrics."""

path_regex: str
default_handlers: Incomplete
