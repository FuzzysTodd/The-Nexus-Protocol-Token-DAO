from .handler import ExtensionHandlerMixin as ExtensionHandlerMixin
from _typeshed import Incomplete
from jupyter_core.application import JupyterApp
from jupyter_server.serverapp import ServerApp as ServerApp
from jupyter_server.utils import is_namespace_package as is_namespace_package, url_path_join as url_path_join
from traitlets import HasTraits, Unicode

class ExtensionAppJinjaMixin(HasTraits):
    """Use Jinja templates for HTML templates on top of an ExtensionApp."""
    jinja2_options: Incomplete

class JupyterServerExtensionException(Exception):
    """Exception class for raising for Server extensions errors."""

class ExtensionApp(JupyterApp):
    """Base class for configurable Jupyter Server Extension Applications.

    ExtensionApp subclasses can be initialized two ways:

    - Extension is listed as a jpserver_extension, and ServerApp calls
      its load_jupyter_server_extension classmethod. This is the
      classic way of loading a server extension.

    - Extension is launched directly by calling its `launch_instance`
      class method. This method can be set as a entry_point in
      the extensions setup.py.
    """
    load_other_extensions: bool
    serverapp_config: dict
    open_browser: Incomplete
    @property
    def config_file_paths(self):
        """Look on the same path as our parent for config files"""
    name: str | Unicode
    @classmethod
    def get_extension_package(cls):
        """Get an extension package."""
    @classmethod
    def get_extension_point(cls):
        """Get an extension point."""
    extension_url: str
    default_url: Incomplete
    file_url_prefix: Incomplete
    classes: Incomplete
    serverapp: Incomplete
    static_url_prefix: Incomplete
    static_paths: Incomplete
    template_paths: Incomplete
    settings: Incomplete
    handlers: Incomplete
    def initialize_settings(self) -> None:
        """Override this method to add handling of settings."""
    def initialize_handlers(self) -> None:
        """Override this method to append handlers to a Jupyter Server."""
    def initialize_templates(self) -> None:
        """Override this method to add handling of template files."""
    def initialize(self) -> None:
        """Initialize the extension app. The
        corresponding server app and webapp should already
        be initialized by this step.

        - Appends Handlers to the ServerApp,
        - Passes config and settings from ExtensionApp
          to the Tornado web application
        - Points Tornado Webapp to templates and static assets.
        """
    def start(self) -> None:
        """Start the underlying Jupyter server.

        Server should be started after extension is initialized.
        """
    def current_activity(self) -> None:
        """Return a list of activity happening in this extension."""
    async def stop_extension(self) -> None:
        """Cleanup any resources managed by this extension."""
    def stop(self) -> None:
        """Stop the underlying Jupyter server."""
    @classmethod
    def load_classic_server_extension(cls, serverapp) -> None:
        """Enables extension to be loaded as classic Notebook (jupyter/notebook) extension."""
    serverapp_class = ServerApp
    @classmethod
    def make_serverapp(cls, **kwargs):
        """Instantiate the ServerApp

        Override to customize the ServerApp before it loads any configuration
        """
    @classmethod
    def initialize_server(cls, argv: Incomplete | None = None, load_other_extensions: bool = True, **kwargs):
        """Creates an instance of ServerApp and explicitly sets
        this extension to enabled=True (i.e. superceding disabling
        found in other config from files).

        The `launch_instance` method uses this method to initialize
        and start a server.
        """
    @classmethod
    def launch_instance(cls, argv: Incomplete | None = None, **kwargs) -> None:
        """Launch the extension like an application. Initializes+configs a stock server
        and appends the extension to the server. Then starts the server and routes to
        extension's landing page.
        """
