from _typeshed import Incomplete
from optparse import Values
from pip._internal.cli.base_command import Command as Command
from pip._internal.cli.status_codes import ERROR as ERROR, SUCCESS as SUCCESS
from pip._internal.metadata import BaseDistribution as BaseDistribution, get_default_environment as get_default_environment
from pip._internal.utils.misc import write_output as write_output
from pip._vendor.packaging.utils import canonicalize_name as canonicalize_name
from typing import Generator, Iterable, List, NamedTuple

logger: Incomplete

class ShowCommand(Command):
    """
    Show information about one or more installed packages.

    The output is in RFC-compliant mail header format.
    """
    usage: str
    ignore_require_venv: bool
    def add_options(self) -> None: ...
    def run(self, options: Values, args: List[str]) -> int: ...

class _PackageInfo(NamedTuple):
    name: str
    version: str
    location: str
    editable_project_location: str | None
    requires: List[str]
    required_by: List[str]
    installer: str
    metadata_version: str
    classifiers: List[str]
    summary: str
    homepage: str
    project_urls: List[str]
    author: str
    author_email: str
    license: str
    entry_points: List[str]
    files: List[str] | None

def search_packages_info(query: List[str]) -> Generator[_PackageInfo, None, None]:
    """
    Gather details from installed distributions. Print distribution name,
    version, location, and installed files. Installed files requires a
    pip generated 'installed-files.txt' in the distributions '.egg-info'
    directory.
    """
def print_results(distributions: Iterable[_PackageInfo], list_files: bool, verbose: bool) -> bool:
    """
    Print the information from installed distributions found.
    """
