from _typeshed import Incomplete
from optparse import Values
from pip._internal.cli import cmdoptions as cmdoptions
from pip._internal.cli.req_command import IndexGroupCommand as IndexGroupCommand
from pip._internal.cli.status_codes import ERROR as ERROR, SUCCESS as SUCCESS
from pip._internal.commands.search import print_dist_installation_info as print_dist_installation_info
from pip._internal.exceptions import CommandError as CommandError, DistributionNotFound as DistributionNotFound, PipError as PipError
from pip._internal.index.collector import LinkCollector as LinkCollector
from pip._internal.index.package_finder import PackageFinder as PackageFinder
from pip._internal.models.selection_prefs import SelectionPreferences as SelectionPreferences
from pip._internal.models.target_python import TargetPython as TargetPython
from pip._internal.network.session import PipSession as PipSession
from pip._internal.utils.misc import write_output as write_output
from pip._vendor.packaging.version import LegacyVersion as LegacyVersion, Version as Version
from typing import Any, List

logger: Incomplete

class IndexCommand(IndexGroupCommand):
    """
    Inspect information available from package indexes.
    """
    ignore_require_venv: bool
    usage: str
    def add_options(self) -> None: ...
    def run(self, options: Values, args: List[str]) -> int: ...
    def get_available_package_versions(self, options: Values, args: List[Any]) -> None: ...
