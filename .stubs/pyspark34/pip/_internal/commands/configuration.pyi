from _typeshed import Incomplete
from optparse import Values
from pip._internal.cli.base_command import Command as Command
from pip._internal.cli.status_codes import ERROR as ERROR, SUCCESS as SUCCESS
from pip._internal.configuration import Configuration as Configuration, Kind as Kind, get_configuration_files as get_configuration_files, kinds as kinds
from pip._internal.exceptions import PipError as PipError
from pip._internal.utils.logging import indent_log as indent_log
from pip._internal.utils.misc import get_prog as get_prog, write_output as write_output
from typing import List

logger: Incomplete

class ConfigurationCommand(Command):
    '''
    Manage local and global configuration.

    Subcommands:

    - list: List the active configuration (or from the file specified)
    - edit: Edit the configuration file in an editor
    - get: Get the value associated with command.option
    - set: Set the command.option=value
    - unset: Unset the value associated with command.option
    - debug: List the configuration files and values defined under them

    Configuration keys should be dot separated command and option name,
    with the special prefix "global" affecting any command. For example,
    "pip config set global.index-url https://example.org/" would configure
    the index url for all commands, but "pip config set download.timeout 10"
    would configure a 10 second timeout only for "pip download" commands.

    If none of --user, --global and --site are passed, a virtual
    environment configuration file is used if one is active and the file
    exists. Otherwise, all modifications happen to the user file by
    default.
    '''
    ignore_require_venv: bool
    usage: str
    def add_options(self) -> None: ...
    configuration: Incomplete
    def run(self, options: Values, args: List[str]) -> int: ...
    def list_values(self, options: Values, args: List[str]) -> None: ...
    def get_name(self, options: Values, args: List[str]) -> None: ...
    def set_name_value(self, options: Values, args: List[str]) -> None: ...
    def unset_name(self, options: Values, args: List[str]) -> None: ...
    def list_config_values(self, options: Values, args: List[str]) -> None:
        """List config key-value pairs across different config files"""
    def print_config_file_values(self, variant: Kind) -> None:
        """Get key-value pairs from the file of a variant"""
    def print_env_var_values(self) -> None:
        """Get key-values pairs present as environment variables"""
    def open_in_editor(self, options: Values, args: List[str]) -> None: ...
