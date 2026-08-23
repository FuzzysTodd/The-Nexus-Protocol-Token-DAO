from _typeshed import Incomplete
from jupyter_core.application import JupyterApp
from jupyter_server._version import __version__ as __version__
from jupyter_server.extension.config import ExtensionConfigManager as ExtensionConfigManager
from jupyter_server.extension.manager import ExtensionManager as ExtensionManager, ExtensionPackage as ExtensionPackage

class ArgumentConflict(ValueError): ...

class BaseExtensionApp(JupyterApp):
    """Base extension installer app"""
    flags: Incomplete
    aliases: Incomplete
    version = __version__
    user: Incomplete
    sys_prefix: Incomplete
    python: Incomplete
    @property
    def config_dir(self): ...

GREEN_ENABLED: Incomplete
RED_DISABLED: Incomplete
GREEN_OK: Incomplete
RED_X: Incomplete

def toggle_server_extension_python(import_name, enabled: Incomplete | None = None, parent: Incomplete | None = None, user: bool = False, sys_prefix: bool = True) -> None:
    """Toggle the boolean setting for a given server extension
    in a Jupyter config file.
    """

flags: Incomplete

class ToggleServerExtensionApp(BaseExtensionApp):
    """A base class for enabling/disabling extensions"""
    name: str
    description: Incomplete
    flags = flags
    def toggle_server_extension(self, import_name) -> None:
        """Change the status of a named server extension.

        Uses the value of `self._toggle_value`.

        Parameters
        ---------

        import_name : str
            Importable Python module (dotted-notation) exposing the magic-named
            `load_jupyter_server_extension` function
        """
    def start(self) -> None:
        """Perform the App's actions as configured"""

class EnableServerExtensionApp(ToggleServerExtensionApp):
    """An App that enables (and validates) Server Extensions"""
    name: str
    description: str

class DisableServerExtensionApp(ToggleServerExtensionApp):
    """An App that disables Server Extensions"""
    name: str
    description: str

class ListServerExtensionsApp(BaseExtensionApp):
    """An App that lists (and validates) Server Extensions"""
    name: str
    version = __version__
    description: str
    def list_server_extensions(self) -> None:
        """List all enabled and disabled server extensions, by config path

        Enabled extensions are validated, potentially generating warnings.
        """
    def start(self) -> None:
        """Perform the App's actions as configured"""

class ServerExtensionApp(BaseExtensionApp):
    """Root level server extension app"""
    name: str
    version = __version__
    description: str
    examples: Incomplete
    subcommands: dict
    def start(self) -> None:
        """Perform the App's actions as configured"""

main: Incomplete
