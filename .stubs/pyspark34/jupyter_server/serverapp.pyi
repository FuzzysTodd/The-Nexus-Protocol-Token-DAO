from _typeshed import Incomplete
from collections.abc import Generator
from jupyter_core.application import JupyterApp
from jupyter_server import DEFAULT_EVENTS_SCHEMA_PATH as DEFAULT_EVENTS_SCHEMA_PATH, DEFAULT_JUPYTER_SERVER_PORT as DEFAULT_JUPYTER_SERVER_PORT, DEFAULT_STATIC_FILES_PATH as DEFAULT_STATIC_FILES_PATH, DEFAULT_TEMPLATE_PATH_LIST as DEFAULT_TEMPLATE_PATH_LIST, JUPYTER_SERVER_EVENTS_URI as JUPYTER_SERVER_EVENTS_URI, __version__ as __version__
from jupyter_server._sysinfo import get_sys_info as get_sys_info
from jupyter_server._tz import utcnow as utcnow
from jupyter_server.auth.authorizer import AllowAllAuthorizer as AllowAllAuthorizer, Authorizer as Authorizer
from jupyter_server.auth.identity import IdentityProvider as IdentityProvider, LegacyIdentityProvider as LegacyIdentityProvider, PasswordIdentityProvider as PasswordIdentityProvider
from jupyter_server.auth.login import LoginHandler as LoginHandler
from jupyter_server.auth.logout import LogoutHandler as LogoutHandler
from jupyter_server.base.handlers import FileFindHandler as FileFindHandler, MainHandler as MainHandler, RedirectWithParams as RedirectWithParams, Template404 as Template404
from jupyter_server.extension.config import ExtensionConfigManager as ExtensionConfigManager
from jupyter_server.extension.manager import ExtensionManager as ExtensionManager
from jupyter_server.extension.serverextension import ServerExtensionApp as ServerExtensionApp
from jupyter_server.gateway.connections import GatewayWebSocketConnection as GatewayWebSocketConnection
from jupyter_server.gateway.managers import GatewayClient as GatewayClient, GatewayKernelSpecManager as GatewayKernelSpecManager, GatewayMappingKernelManager as GatewayMappingKernelManager, GatewaySessionManager as GatewaySessionManager
from jupyter_server.log import log_request as log_request
from jupyter_server.services.config import ConfigManager as ConfigManager
from jupyter_server.services.contents.filemanager import AsyncFileContentsManager as AsyncFileContentsManager, FileContentsManager as FileContentsManager
from jupyter_server.services.contents.largefilemanager import AsyncLargeFileManager as AsyncLargeFileManager
from jupyter_server.services.contents.manager import AsyncContentsManager as AsyncContentsManager, ContentsManager as ContentsManager
from jupyter_server.services.kernels.connection.base import BaseKernelWebsocketConnection as BaseKernelWebsocketConnection
from jupyter_server.services.kernels.connection.channels import ZMQChannelsWebsocketConnection as ZMQChannelsWebsocketConnection
from jupyter_server.services.kernels.kernelmanager import AsyncMappingKernelManager as AsyncMappingKernelManager, MappingKernelManager as MappingKernelManager
from jupyter_server.services.sessions.sessionmanager import SessionManager as SessionManager
from jupyter_server.transutils import trans as trans
from jupyter_server.utils import check_pid as check_pid, fetch as fetch, pathname2url as pathname2url, unix_socket_in_use as unix_socket_in_use, url_escape as url_escape, url_path_join as url_path_join, urlencode_unix_socket_path as urlencode_unix_socket_path, urljoin as urljoin
from tornado import web

MIN_TORNADO: Incomplete
JUPYTER_SERVICE_HANDLERS: Incomplete
DEFAULT_SERVER_PORT = DEFAULT_JUPYTER_SERVER_PORT

def random_ports(port, n) -> Generator[Incomplete, None, None]:
    """Generate a list of n random ports near the given port.

    The first 5 ports will be sequential, and the remaining n-5 will be
    randomly selected in the range [port-2*n, port+2*n].
    """
def load_handlers(name):
    """Load the (URL pattern, handler) tuples for each component."""

class ServerWebApplication(web.Application):
    """A server web application."""
    def __init__(self, jupyter_app, default_services, kernel_manager, contents_manager, session_manager, kernel_spec_manager, config_manager, event_logger, extra_services, log, base_url, default_url, settings_overrides, jinja_env_options, *, authorizer: Incomplete | None = None, identity_provider: Incomplete | None = None, kernel_websocket_connection_class: Incomplete | None = None) -> None:
        """Initialize a server web application."""
    def init_settings(self, jupyter_app, kernel_manager, contents_manager, session_manager, kernel_spec_manager, config_manager, event_logger, extra_services, log, base_url, default_url, settings_overrides, jinja_env_options: Incomplete | None = None, *, authorizer: Incomplete | None = None, identity_provider: Incomplete | None = None, kernel_websocket_connection_class: Incomplete | None = None):
        """Initialize settings for the web application."""
    def init_handlers(self, default_services, settings):
        """Load the (URL pattern, handler) tuples for each component."""
    def last_activity(self):
        """Get a UTC timestamp for when the server last did something.

        Includes: API activity, kernel activity, kernel shutdown, and terminal
        activity.
        """

class JupyterPasswordApp(JupyterApp):
    """Set a password for the Jupyter server.

    Setting a password secures the Jupyter server
    and removes the need for token-based authentication.
    """
    description: str
    def start(self) -> None:
        """Start the password app."""

def shutdown_server(server_info, timeout: int = 5, log: Incomplete | None = None):
    """Shutdown a Jupyter server in a separate process.

    *server_info* should be a dictionary as produced by list_running_servers().

    Will first try to request shutdown using /api/shutdown .
    On Unix, if the server is still running after *timeout* seconds, it will
    send SIGTERM. After another timeout, it escalates to SIGKILL.

    Returns True if the server was stopped by any means, False if stopping it
    failed (on Windows).
    """

class JupyterServerStopApp(JupyterApp):
    """An application to stop a Jupyter server."""
    version: str
    description: str
    port: Incomplete
    sock: Incomplete
    def parse_command_line(self, argv: Incomplete | None = None) -> None:
        """Parse command line options."""
    def shutdown_server(self, server):
        """Shut down a server."""
    def start(self) -> None:
        """Start the server stop app."""

class JupyterServerListApp(JupyterApp):
    """An application to list running Jupyter servers."""
    version: str
    description: str
    flags: Incomplete
    jsonlist: Incomplete
    json: Incomplete
    def start(self) -> None:
        """Start the server list application."""

flags: Incomplete
aliases: Incomplete

class ServerApp(JupyterApp):
    """The Jupyter Server application class."""
    name: str
    version: str
    description: str
    examples: Incomplete
    flags: Incomplete
    aliases: Incomplete
    classes: Incomplete
    subcommands: dict
    default_services: Incomplete
    file_to_run: Incomplete
    file_url_prefix: Incomplete
    allow_origin: Incomplete
    allow_origin_pat: Incomplete
    allow_credentials: Incomplete
    allow_root: Incomplete
    autoreload: Incomplete
    default_url: Incomplete
    ip: Incomplete
    custom_display_url: Incomplete
    port_env: str
    port_default_value = DEFAULT_JUPYTER_SERVER_PORT
    port: Incomplete
    port_retries_env: str
    port_retries_default_value: int
    port_retries: Incomplete
    sock: Incomplete
    sock_mode: Incomplete
    certfile: Incomplete
    keyfile: Incomplete
    client_ca: Incomplete
    cookie_secret_file: Incomplete
    cookie_secret: Incomplete
    token: Incomplete
    min_open_files_limit: Incomplete
    max_body_size: Incomplete
    max_buffer_size: Incomplete
    password: Incomplete
    password_required: Incomplete
    allow_password_change: Incomplete
    disable_check_xsrf: Incomplete
    allow_remote_access: Incomplete
    use_redirect_file: Incomplete
    local_hostnames: Incomplete
    open_browser: Incomplete
    browser: Incomplete
    webbrowser_open_new: Incomplete
    tornado_settings: Incomplete
    websocket_compression_options: Incomplete
    terminado_settings: Incomplete
    cookie_options: Incomplete
    get_secure_cookie_kwargs: Incomplete
    ssl_options: Incomplete
    jinja_environment_options: Incomplete
    jinja_template_vars: Incomplete
    base_url: Incomplete
    extra_static_paths: Incomplete
    @property
    def static_file_path(self):
        """return extra paths + the default location"""
    static_custom_path: Incomplete
    extra_template_paths: Incomplete
    @property
    def template_file_path(self):
        """return extra paths + the default locations"""
    extra_services: Incomplete
    websocket_url: Incomplete
    quit_button: Incomplete
    contents_manager_class: Incomplete
    kernel_manager_class: Incomplete
    session_manager_class: Incomplete
    kernel_websocket_connection_class: Incomplete
    config_manager_class: Incomplete
    kernel_spec_manager: Incomplete
    kernel_spec_manager_class: Incomplete
    login_handler_class: Incomplete
    logout_handler_class: Incomplete
    authorizer_class: Incomplete
    identity_provider_class: Incomplete
    trust_xheaders: Incomplete
    event_logger: Incomplete
    info_file: Incomplete
    no_browser_open_file: Incomplete
    browser_open_file: Incomplete
    browser_open_file_to_run: Incomplete
    pylab: Incomplete
    notebook_dir: Incomplete
    external_connection_dir: Incomplete
    allow_external_kernels: Incomplete
    root_dir: Incomplete
    preferred_dir: Incomplete
    jpserver_extensions: Incomplete
    reraise_server_extension_failures: Incomplete
    kernel_ws_protocol: Incomplete
    limit_rate: Incomplete
    iopub_msg_rate_limit: Incomplete
    iopub_data_rate_limit: Incomplete
    rate_limit_window: Incomplete
    shutdown_no_activity_timeout: Incomplete
    terminals_enabled: Incomplete
    authenticate_prometheus: Incomplete
    static_immutable_cache: Incomplete
    @property
    def starter_app(self):
        """Get the Extension that started this server."""
    def parse_command_line(self, argv: Incomplete | None = None) -> None:
        """Parse the command line options."""
    gateway_config: Incomplete
    kernel_manager: Incomplete
    contents_manager: Incomplete
    session_manager: Incomplete
    config_manager: Incomplete
    identity_provider: Incomplete
    authorizer: Incomplete
    def init_configurables(self) -> None:
        """Initialize configurables."""
    def init_logging(self) -> None:
        """Initialize logging."""
    def init_event_logger(self) -> None:
        """Initialize the Event Bus."""
    web_app: Incomplete
    def init_webapp(self) -> None:
        """initialize tornado webapp"""
    def init_resources(self) -> None:
        """initialize system resources"""
    @property
    def public_url(self): ...
    @property
    def local_url(self): ...
    @property
    def display_url(self):
        """Human readable string with URLs for interacting
        with the running Jupyter Server
        """
    @property
    def connection_url(self): ...
    def init_signal(self) -> None:
        """Initialize signal handlers."""
    def init_components(self) -> None:
        """Check the components submodule, and warn if it's unclean"""
    def find_server_extensions(self) -> None:
        """
        Searches Jupyter paths for jpserver_extensions.
        """
    extension_manager: Incomplete
    def init_server_extensions(self) -> None:
        """
        If an extension's metadata includes an 'app' key,
        the value must be a subclass of ExtensionApp. An instance
        of the class will be created at this step. The config for
        this instance will inherit the ServerApp's config object
        and load its own config.
        """
    def load_server_extensions(self) -> None:
        """Load any extensions specified by config.

        Import the module, then call the load_jupyter_server_extension function,
        if one exists.

        The extension API is experimental, and may change in future releases.
        """
    def init_mime_overrides(self) -> None: ...
    def shutdown_no_activity(self) -> None:
        """Shutdown server on timeout when there are no kernels or terminals."""
    def init_shutdown_no_activity(self) -> None:
        """Initialize a shutdown on no activity."""
    @property
    def http_server(self):
        """An instance of Tornado's HTTPServer class for the Server Web Application."""
    def init_httpserver(self) -> None:
        """Creates an instance of a Tornado HTTPServer for the Server Web Application
        and sets the http_server attribute.
        """
    def initialize(self, argv: Incomplete | None = None, find_extensions: bool = True, new_httpserver: bool = True, starter_extension: Incomplete | None = None) -> None:
        """Initialize the Server application class, configurables, web application, and http server.

        Parameters
        ----------
        argv : list or None
            CLI arguments to parse.
        find_extensions : bool
            If True, find and load extensions listed in Jupyter config paths. If False,
            only load extensions that are passed to ServerApp directy through
            the `argv`, `config`, or `jpserver_extensions` arguments.
        new_httpserver : bool
            If True, a tornado HTTPServer instance will be created and configured for the Server Web
            Application. This will set the http_server attribute of this class.
        starter_extension : str
            If given, it references the name of an extension point that started the Server.
            We will try to load configuration from extension point
        """
    async def cleanup_kernels(self) -> None:
        """Shutdown all kernels.

        The kernels will shutdown themselves when this process no longer exists,
        but explicit shutdown allows the KernelManagers to cleanup the connection files.
        """
    async def cleanup_extensions(self) -> None:
        """Call shutdown hooks in all extensions."""
    def running_server_info(self, kernel_count: bool = True):
        """Return the current working directory and the server url information"""
    def server_info(self):
        """Return a JSONable dict of information about this server."""
    def write_server_info_file(self) -> None:
        """Write the result of server_info() to the JSON file info_file."""
    def remove_server_info_file(self) -> None:
        """Remove the jpserver-<pid>.json file created for this server.

        Ignores the error raised when the file has already been removed.
        """
    def write_browser_open_files(self) -> None:
        """Write an `browser_open_file` and `browser_open_file_to_run` files

        This can be used to open a file directly in a browser.
        """
    def write_browser_open_file(self) -> None:
        """Write an jpserver-<pid>-open.html file

        This can be used to open the notebook in a browser
        """
    def remove_browser_open_files(self) -> None:
        """Remove the `browser_open_file` and `browser_open_file_to_run` files
        created for this server.

        Ignores the error raised when the file has already been removed.
        """
    def remove_browser_open_file(self) -> None:
        """Remove the jpserver-<pid>-open.html file created for this server.

        Ignores the error raised when the file has already been removed.
        """
    def launch_browser(self) -> None:
        """Launch the browser."""
    def start_app(self) -> None:
        """Start the Jupyter Server application."""
    def start_ioloop(self) -> None:
        """Start the IO Loop."""
    io_loop: Incomplete
    def init_ioloop(self) -> None:
        """init self.io_loop so that an extension can use it by io_loop.call_later() to create background tasks"""
    def start(self) -> None:
        """Start the Jupyter server app, after initialization

        This method takes no arguments so all configuration and initialization
        must be done prior to calling this method."""
    def stop(self, from_signal: bool = False) -> None:
        """Cleanup resources and stop the server."""

def list_running_servers(runtime_dir: Incomplete | None = None, log: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """Iterate over the server info files of running Jupyter servers.

    Given a runtime directory, find jpserver-* files in the security directory,
    and yield dicts of their information, each one pertaining to
    a currently running Jupyter server instance.
    """

main: Incomplete

launch_new_instance: Incomplete
