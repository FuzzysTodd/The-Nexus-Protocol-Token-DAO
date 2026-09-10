import abc
from _typeshed import Incomplete
from optparse import Values
from pip._internal.cli import cmdoptions as cmdoptions
from pip._internal.cli.req_command import IndexGroupCommand as IndexGroupCommand
from pip._internal.cli.status_codes import SUCCESS as SUCCESS
from pip._internal.exceptions import CommandError as CommandError
from pip._internal.index.collector import LinkCollector as LinkCollector
from pip._internal.index.package_finder import PackageFinder as PackageFinder
from pip._internal.metadata import BaseDistribution as BaseDistribution, get_environment as get_environment
from pip._internal.metadata.base import DistributionVersion as DistributionVersion
from pip._internal.models.selection_prefs import SelectionPreferences as SelectionPreferences
from pip._internal.network.session import PipSession as PipSession
from pip._internal.utils.compat import stdlib_pkgs as stdlib_pkgs
from pip._internal.utils.misc import tabulate as tabulate, write_output as write_output
from pip._vendor.packaging.utils import canonicalize_name as canonicalize_name
from typing import Generator, List, Tuple

class _DistWithLatestInfo(BaseDistribution, metaclass=abc.ABCMeta):
    """Give the distribution object a couple of extra fields.

        These will be populated during ``get_outdated()``. This is dirty but
        makes the rest of the code much cleaner.
        """
    latest_version: DistributionVersion
    latest_filetype: str

logger: Incomplete

class ListCommand(IndexGroupCommand):
    """
    List installed packages, including editables.

    Packages are listed in a case-insensitive sorted order.
    """
    ignore_require_venv: bool
    usage: str
    def add_options(self) -> None: ...
    def run(self, options: Values, args: List[str]) -> int: ...
    def get_outdated(self, packages: _ProcessedDists, options: Values) -> _ProcessedDists: ...
    def get_uptodate(self, packages: _ProcessedDists, options: Values) -> _ProcessedDists: ...
    def get_not_required(self, packages: _ProcessedDists, options: Values) -> _ProcessedDists: ...
    def iter_packages_latest_infos(self, packages: _ProcessedDists, options: Values) -> Generator['_DistWithLatestInfo', None, None]: ...
    def output_package_listing(self, packages: _ProcessedDists, options: Values) -> None: ...
    def output_package_listing_columns(self, data: List[List[str]], header: List[str]) -> None: ...

def format_for_columns(pkgs: _ProcessedDists, options: Values) -> Tuple[List[List[str]], List[str]]:
    """
    Convert the package data into something usable
    by output_package_listing_columns.
    """
def format_for_json(packages: _ProcessedDists, options: Values) -> str: ...
