import optparse
from _typeshed import Incomplete
from pip._internal.cli.status_codes import UNKNOWN_ERROR as UNKNOWN_ERROR
from pip._internal.configuration import Configuration as Configuration, ConfigurationError as ConfigurationError
from pip._internal.utils.misc import redact_auth_from_url as redact_auth_from_url, strtobool as strtobool
from typing import Any, List

logger: Incomplete

class PrettyHelpFormatter(optparse.IndentedHelpFormatter):
    """A prettier/less verbose help formatter for optparse."""
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def format_option_strings(self, option: optparse.Option) -> str: ...
    def format_heading(self, heading: str) -> str: ...
    def format_usage(self, usage: str) -> str:
        """
        Ensure there is only one newline between usage and the first heading
        if there is no description.
        """
    def format_description(self, description: str) -> str: ...
    def format_epilog(self, epilog: str) -> str: ...
    def indent_lines(self, text: str, indent: str) -> str: ...

class UpdatingDefaultsHelpFormatter(PrettyHelpFormatter):
    """Custom help formatter for use in ConfigOptionParser.

    This is updates the defaults before expanding them, allowing
    them to show up correctly in the help listing.

    Also redact auth from url type options
    """
    def expand_default(self, option: optparse.Option) -> str: ...

class CustomOptionParser(optparse.OptionParser):
    def insert_option_group(self, idx: int, *args: Any, **kwargs: Any) -> optparse.OptionGroup:
        """Insert an OptionGroup at a given position."""
    @property
    def option_list_all(self) -> List[optparse.Option]:
        """Get a list of all options, including those in option groups."""

class ConfigOptionParser(CustomOptionParser):
    """Custom option parser which updates its defaults by checking the
    configuration files and environmental variables"""
    name: Incomplete
    config: Incomplete
    def __init__(self, *args: Any, name: str, isolated: bool = False, **kwargs: Any) -> None: ...
    def check_default(self, option: optparse.Option, key: str, val: Any) -> Any: ...
    def get_default_values(self) -> optparse.Values:
        """Overriding to make updating the defaults after instantiation of
        the option parser possible, _update_defaults() does the dirty work."""
    def error(self, msg: str) -> None: ...
