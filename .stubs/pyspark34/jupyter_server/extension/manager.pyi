from .config import ExtensionConfigManager as ExtensionConfigManager
from .utils import ExtensionMetadataError as ExtensionMetadataError, ExtensionModuleNotFound as ExtensionModuleNotFound, get_loader as get_loader, get_metadata as get_metadata
from _typeshed import Incomplete
from traitlets import HasTraits
from traitlets.config import LoggingConfigurable

class ExtensionPoint(HasTraits):
    """A simple API for connecting to a Jupyter Server extension
    point defined by metadata and importable from a Python package.
    """
    metadata: Incomplete
    @property
    def linked(self):
        """Has this extension point been linked to the server.

        Will pull from ExtensionApp's trait, if this point
        is an instance of ExtensionApp.
        """
    @property
    def app(self):
        """If the metadata includes an `app` field"""
    @property
    def config(self):
        """Return any configuration provided by this extension point."""
    @property
    def module_name(self):
        """Name of the Python package module where the extension's
        _load_jupyter_server_extension can be found.
        """
    @property
    def name(self):
        """Name of the extension.

        If it's not provided in the metadata, `name` is set
        to the extensions' module name.
        """
    @property
    def module(self):
        """The imported module (using importlib.import_module)"""
    def validate(self):
        """Check that both a linker and loader exists."""
    def link(self, serverapp) -> None:
        """Link the extension to a Jupyter ServerApp object.

        This looks for a `_link_jupyter_server_extension` function
        in the extension's module or ExtensionApp class.
        """
    def load(self, serverapp):
        """Load the extension in a Jupyter ServerApp object.

        This looks for a `_load_jupyter_server_extension` function
        in the extension's module or ExtensionApp class.
        """

class ExtensionPackage(LoggingConfigurable):
    '''An API for interfacing with a Jupyter Server extension package.

    Usage:

    ext_name = "my_extensions"
    extpkg = ExtensionPackage(name=ext_name)
    '''
    name: Incomplete
    enabled: Incomplete
    extension_points: Incomplete
    module: Incomplete
    metadata: Incomplete
    version: Incomplete
    def __init__(self, **kwargs) -> None:
        """Initialize an extension package."""
    def validate(self):
        """Validate all extension points in this package."""
    def link_point(self, point_name, serverapp) -> None:
        """Link an extension point."""
    def load_point(self, point_name, serverapp):
        """Load an extension point."""
    def link_all_points(self, serverapp) -> None:
        """Link all extension points."""
    def load_all_points(self, serverapp):
        """Load all extension points."""

class ExtensionManager(LoggingConfigurable):
    """High level interface for findind, validating,
    linking, loading, and managing Jupyter Server extensions.

    Usage:
    m = ExtensionManager(config_manager=...)
    """
    config_manager: Incomplete
    serverapp: Incomplete
    extensions: Incomplete
    @property
    def sorted_extensions(self):
        """Returns an extensions dictionary, sorted alphabetically."""
    linked_extensions: Incomplete
    @property
    def extension_apps(self):
        """Return mapping of extension names and sets of ExtensionApp objects."""
    @property
    def extension_points(self):
        """Return mapping of extension point names and ExtensionPoint objects."""
    def from_config_manager(self, config_manager) -> None:
        """Add extensions found by an ExtensionConfigManager"""
    def from_jpserver_extensions(self, jpserver_extensions) -> None:
        """Add extensions from 'jpserver_extensions'-like dictionary."""
    def add_extension(self, extension_name, enabled: bool = False):
        """Try to add extension to manager, return True if successful.
        Otherwise, return False.
        """
    def link_extension(self, name) -> None:
        """Link an extension by name."""
    def load_extension(self, name) -> None:
        """Load an extension by name."""
    async def stop_extension(self, name, apps) -> None:
        """Call the shutdown hooks in the specified apps."""
    def link_all_extensions(self) -> None:
        """Link all enabled extensions
        to an instance of ServerApp
        """
    def load_all_extensions(self) -> None:
        """Load all enabled extensions and append them to
        the parent ServerApp.
        """
    async def stop_all_extensions(self) -> None:
        """Call the shutdown hooks in all extensions."""
    def any_activity(self):
        """Check for any activity currently happening across all extension applications."""
