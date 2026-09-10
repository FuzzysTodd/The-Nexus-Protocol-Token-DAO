from _typeshed import Incomplete
from traitlets.config import LoggingConfigurable as LoggingConfigurable
from traitlets.traitlets import Unicode as Unicode
from typing import Any

def recursive_update(target: dict[Any, Any], new: dict[Any, Any]) -> None:
    """Recursively update one dictionary using another.

    None values will delete their keys.
    """

class BaseJSONConfigManager(LoggingConfigurable):
    """General JSON config manager

    Deals with persisting/storing config in a json file
    """
    config_dir: Incomplete
    def ensure_config_dir_exists(self) -> None: ...
    def file_name(self, section_name: str) -> str: ...
    def get(self, section_name: str) -> Any:
        """Retrieve the config data for the specified section.

        Returns the data as a dictionary, or an empty dictionary if the file
        doesn't exist.
        """
    def set(self, section_name: str, data: Any) -> None:
        """Store the given config data."""
    def update(self, section_name: str, new_data: Any) -> Any:
        """Modify the config section by recursively updating it with new_data.

        Returns the modified config data as a dictionary.
        """
