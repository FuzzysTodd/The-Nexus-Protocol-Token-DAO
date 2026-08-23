from _typeshed import Incomplete
from jupyter_server.config_manager import BaseJSONConfigManager as BaseJSONConfigManager, recursive_update as recursive_update
from traitlets.config import LoggingConfigurable

class ConfigManager(LoggingConfigurable):
    """Config Manager used for storing frontend config"""
    config_dir_name: Incomplete
    def get(self, section_name):
        """Get the config from all config sections."""
    def set(self, section_name, data):
        """Set the config only to the user's config."""
    def update(self, section_name, new_data):
        """Update the config only to the user's config."""
    read_config_path: Incomplete
    write_config_dir: Incomplete
    write_config_manager: Incomplete
