from jupyter_server.services.config.manager import ConfigManager as ConfigManager

DEFAULT_SECTION_NAME: str

class ExtensionConfigManager(ConfigManager):
    """A manager class to interface with Jupyter Server Extension config
    found in a `config.d` folder. It is assumed that all configuration
    files in this directory are JSON files.
    """
    def get_jpserver_extensions(self, section_name=...):
        """Return the jpserver_extensions field from all
        config files found."""
    def enabled(self, name, section_name=..., include_root: bool = True):
        """Is the extension enabled?"""
    def enable(self, name) -> None:
        """Enable an extension by name."""
    def disable(self, name) -> None:
        """Disable an extension by name."""
