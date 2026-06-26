from _typeshed import Incomplete
from traitlets.config import LoggingConfigurable

def recursive_update(target, new) -> None:
    """Recursively update one dictionary using another.

    None values will delete their keys.
    """
def remove_defaults(data, defaults) -> None:
    """Recursively remove items from dict that are already in defaults"""

class BaseJSONConfigManager(LoggingConfigurable):
    """General JSON config manager

    Deals with persisting/storing config in a json file with optionally
    default values in a {section_name}.d directory.
    """
    config_dir: Incomplete
    read_directory: Incomplete
    def ensure_config_dir_exists(self) -> None:
        """Will try to create the config_dir directory."""
    def file_name(self, section_name):
        """Returns the json filename for the section_name: {config_dir}/{section_name}.json"""
    def directory(self, section_name):
        """Returns the directory name for the section name: {config_dir}/{section_name}.d"""
    def get(self, section_name, include_root: bool = True):
        """Retrieve the config data for the specified section.

        Returns the data as a dictionary, or an empty dictionary if the file
        doesn't exist.

        When include_root is False, it will not read the root .json file,
        effectively returning the default values.
        """
    def set(self, section_name, data) -> None:
        """Store the given config data."""
    def update(self, section_name, new_data):
        """Modify the config section by recursively updating it with new_data.

        Returns the modified config data as a dictionary.
        """
