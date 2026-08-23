import configparser
from _typeshed import Incomplete
from collections.abc import Generator

entry_point_pattern: Incomplete
file_in_zip_pattern: Incomplete
__version__: str

class BadEntryPoint(Exception):
    """Raised when an entry point can't be parsed.
    """
    epstr: Incomplete
    def __init__(self, epstr) -> None: ...
    @staticmethod
    def err_to_warnings() -> Generator[None, None, None]: ...

class NoSuchEntryPoint(Exception):
    """Raised by :func:`get_single` when no matching entry point is found."""
    group: Incomplete
    name: Incomplete
    def __init__(self, group, name) -> None: ...

class CaseSensitiveConfigParser(configparser.ConfigParser):
    optionxform: Incomplete

class EntryPoint:
    name: Incomplete
    module_name: Incomplete
    object_name: Incomplete
    extras: Incomplete
    distro: Incomplete
    def __init__(self, name, module_name, object_name, extras: Incomplete | None = None, distro: Incomplete | None = None) -> None: ...
    def load(self):
        """Load the object to which this entry point refers.
        """
    @classmethod
    def from_string(cls, epstr, name, distro: Incomplete | None = None):
        """Parse an entry point from the syntax in entry_points.txt

        :param str epstr: The entry point string (not including 'name =')
        :param str name: The name of this entry point
        :param Distribution distro: The distribution in which the entry point was found
        :rtype: EntryPoint
        :raises BadEntryPoint: if *epstr* can't be parsed as an entry point.
        """

class Distribution:
    name: Incomplete
    version: Incomplete
    def __init__(self, name, version) -> None: ...
    @classmethod
    def from_name_version(cls, name):
        '''Parse a distribution from a "name-version" string

        :param str name: The name-version string (entrypoints-0.3)
        Returns an :class:`Distribution` object
        '''

def iter_files_distros(path: Incomplete | None = None, repeated_distro: str = 'first') -> Generator[Incomplete, None, None]: ...
def get_single(group, name, path: Incomplete | None = None):
    """Find a single entry point.

    Returns an :class:`EntryPoint` object, or raises :exc:`NoSuchEntryPoint`
    if no match is found.
    """
def get_group_named(group, path: Incomplete | None = None):
    """Find a group of entry points with unique names.

    Returns a dictionary of names to :class:`EntryPoint` objects.
    """
def get_group_all(group, path: Incomplete | None = None):
    """Find all entry points in a group.

    Returns a list of :class:`EntryPoint` objects.
    """
