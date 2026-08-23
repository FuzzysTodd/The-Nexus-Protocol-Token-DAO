from . import expand as expand
from ..errors import FileError as FileError, OptionError as OptionError
from ..extern.packaging.requirements import InvalidRequirement as InvalidRequirement, Requirement as Requirement
from ..extern.packaging.specifiers import SpecifierSet as SpecifierSet
from ..extern.packaging.version import InvalidVersion as InvalidVersion, Version as Version
from ..warnings import SetuptoolsDeprecationWarning as SetuptoolsDeprecationWarning
from _typeshed import Incomplete
from distutils.dist import DistributionMetadata
from setuptools.dist import Distribution as Distribution
from typing import Dict, Generic, Tuple, TypeVar

SingleCommandOptions: Incomplete
AllCommandOptions: Incomplete
Target = TypeVar('Target', bound='Distribution' | 'DistributionMetadata')

def read_configuration(filepath: _Path, find_others: bool = False, ignore_option_errors: bool = False) -> dict:
    """Read given configuration file and returns options from it as a dict.

    :param str|unicode filepath: Path to configuration file
        to get options from.

    :param bool find_others: Whether to search for other configuration files
        which could be on in various places.

    :param bool ignore_option_errors: Whether to silently ignore
        options, values of which could not be resolved (e.g. due to exceptions
        in directives such as file:, attr:, etc.).
        If False exceptions are propagated as expected.

    :rtype: dict
    """
def apply_configuration(dist: Distribution, filepath: _Path) -> Distribution:
    """Apply the configuration from a ``setup.cfg`` file into an existing
    distribution object.
    """
def configuration_to_dict(handlers: Tuple['ConfigHandler', ...]) -> dict:
    """Returns configuration data gathered by given handlers as a dict.

    :param list[ConfigHandler] handlers: Handlers list,
        usually from parse_configuration()

    :rtype: dict
    """
def parse_configuration(distribution: Distribution, command_options: AllCommandOptions, ignore_option_errors: bool = False) -> Tuple['ConfigMetadataHandler', 'ConfigOptionsHandler']:
    """Performs additional parsing of configuration options
    for a distribution.

    Returns a list of used option handlers.

    :param Distribution distribution:
    :param dict command_options:
    :param bool ignore_option_errors: Whether to silently ignore
        options, values of which could not be resolved (e.g. due to exceptions
        in directives such as file:, attr:, etc.).
        If False exceptions are propagated as expected.
    :rtype: list
    """

class ConfigHandler(Generic[Target]):
    """Handles metadata supplied in configuration files."""
    section_prefix: str
    aliases: Dict[str, str]
    ignore_option_errors: Incomplete
    target_obj: Incomplete
    sections: Incomplete
    set_options: Incomplete
    ensure_discovered: Incomplete
    def __init__(self, target_obj: Target, options: AllCommandOptions, ignore_option_errors, ensure_discovered: expand.EnsurePackagesDiscovered) -> None: ...
    @property
    def parsers(self) -> None:
        """Metadata item name to parser function mapping."""
    def __setitem__(self, option_name, value) -> None: ...
    def parse_section(self, section_options) -> None:
        """Parses configuration file section.

        :param dict section_options:
        """
    def parse(self) -> None:
        """Parses configuration file items from one
        or more related sections.

        """

class ConfigMetadataHandler(ConfigHandler['DistributionMetadata']):
    section_prefix: str
    aliases: Incomplete
    strict_mode: bool
    package_dir: Incomplete
    root_dir: Incomplete
    def __init__(self, target_obj: DistributionMetadata, options: AllCommandOptions, ignore_option_errors: bool, ensure_discovered: expand.EnsurePackagesDiscovered, package_dir: dict | None = None, root_dir: _Path = ...) -> None: ...
    @property
    def parsers(self):
        """Metadata item name to parser function mapping."""

class ConfigOptionsHandler(ConfigHandler['Distribution']):
    section_prefix: str
    root_dir: Incomplete
    package_dir: Incomplete
    def __init__(self, target_obj: Distribution, options: AllCommandOptions, ignore_option_errors: bool, ensure_discovered: expand.EnsurePackagesDiscovered) -> None: ...
    @property
    def parsers(self):
        """Metadata item name to parser function mapping."""
    def parse_section_packages__find(self, section_options):
        """Parses `packages.find` configuration file section.

        To be used in conjunction with _parse_packages().

        :param dict section_options:
        """
    def parse_section_entry_points(self, section_options) -> None:
        """Parses `entry_points` configuration file section.

        :param dict section_options:
        """
    def parse_section_package_data(self, section_options) -> None:
        """Parses `package_data` configuration file section.

        :param dict section_options:
        """
    def parse_section_exclude_package_data(self, section_options) -> None:
        """Parses `exclude_package_data` configuration file section.

        :param dict section_options:
        """
    def parse_section_extras_require(self, section_options):
        """Parses `extras_require` configuration file section.

        :param dict section_options:
        """
    def parse_section_data_files(self, section_options) -> None:
        """Parses `data_files` configuration file section.

        :param dict section_options:
        """

class _AmbiguousMarker(SetuptoolsDeprecationWarning):
    @classmethod
    def message(cls, **kw): ...

class _DeprecatedConfig(SetuptoolsDeprecationWarning): ...
