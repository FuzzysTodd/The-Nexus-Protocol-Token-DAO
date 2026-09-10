from .extern.packaging.markers import Marker as Marker
from .extern.packaging.requirements import Requirement as Requirement
from .extern.packaging.version import Version as Version
from .warnings import SetuptoolsDeprecationWarning as SetuptoolsDeprecationWarning

def get_metadata_version(self): ...
def rfc822_unescape(content: str) -> str:
    """Reverse RFC-822 escaping by removing leading whitespaces from content."""
def read_pkg_file(self, file) -> None:
    """Reads the metadata values from a file object."""
def single_line(val):
    """
    Quick and dirty validation for Summary pypa/setuptools#1390.
    """
def write_pkg_info(self, base_dir) -> None:
    """Write the PKG-INFO file into the release tree."""
def write_pkg_file(self, file) -> None:
    """Write the PKG-INFO format data to a file object."""
