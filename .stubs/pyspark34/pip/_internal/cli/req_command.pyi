from _typeshed import Incomplete
from optparse import Values
from pip._internal.cache import WheelCache as WheelCache
from pip._internal.cli import cmdoptions as cmdoptions
from pip._internal.cli.base_command import Command as Command
from pip._internal.cli.command_context import CommandContextMixIn as CommandContextMixIn
from pip._internal.exceptions import CommandError as CommandError, PreviousBuildDirError as PreviousBuildDirError
from pip._internal.index.collector import LinkCollector as LinkCollector
from pip._internal.index.package_finder import PackageFinder as PackageFinder
from pip._internal.models.selection_prefs import SelectionPreferences as SelectionPreferences
from pip._internal.models.target_python import TargetPython as TargetPython
from pip._internal.network.session import PipSession as PipSession
from pip._internal.operations.build.build_tracker import BuildTracker as BuildTracker
from pip._internal.operations.prepare import RequirementPreparer as RequirementPreparer
from pip._internal.req.constructors import install_req_from_editable as install_req_from_editable, install_req_from_line as install_req_from_line, install_req_from_parsed_requirement as install_req_from_parsed_requirement, install_req_from_req_string as install_req_from_req_string
from pip._internal.req.req_file import parse_requirements as parse_requirements
from pip._internal.req.req_install import InstallRequirement as InstallRequirement
from pip._internal.resolution.base import BaseResolver as BaseResolver
from pip._internal.self_outdated_check import pip_self_version_check as pip_self_version_check
from pip._internal.utils.temp_dir import TempDirectory as TempDirectory, TempDirectoryTypeRegistry as TempDirectoryTypeRegistry, tempdir_kinds as tempdir_kinds
from pip._internal.utils.virtualenv import running_under_virtualenv as running_under_virtualenv
from typing import Any, List, Tuple

logger: Incomplete

class SessionCommandMixin(CommandContextMixIn):
    """
    A class mixin for command classes needing _build_session().
    """
    def __init__(self) -> None: ...
    def get_default_session(self, options: Values) -> PipSession:
        """Get a default-managed session."""

class IndexGroupCommand(Command, SessionCommandMixin):
    """
    Abstract base class for commands with the index_group options.

    This also corresponds to the commands that permit the pip version check.
    """
    def handle_pip_version_check(self, options: Values) -> None:
        """
        Do the pip version check if not disabled.

        This overrides the default behavior of not doing the check.
        """

KEEPABLE_TEMPDIR_TYPES: Incomplete

def warn_if_run_as_root() -> None:
    """Output a warning for sudo users on Unix.

    In a virtual environment, sudo pip still writes to virtualenv.
    On Windows, users may run pip as Administrator without issues.
    This warning only applies to Unix root users outside of virtualenv.
    """
def with_cleanup(func: Any) -> Any:
    """Decorator for common logic related to managing temporary
    directories.
    """

class RequirementCommand(IndexGroupCommand):
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    @staticmethod
    def determine_resolver_variant(options: Values) -> str:
        """Determines which resolver should be used, based on the given options."""
    @classmethod
    def make_requirement_preparer(cls, temp_build_dir: TempDirectory, options: Values, build_tracker: BuildTracker, session: PipSession, finder: PackageFinder, use_user_site: bool, download_dir: str | None = None, verbosity: int = 0) -> RequirementPreparer:
        """
        Create a RequirementPreparer instance for the given parameters.
        """
    @classmethod
    def make_resolver(cls, preparer: RequirementPreparer, finder: PackageFinder, options: Values, wheel_cache: WheelCache | None = None, use_user_site: bool = False, ignore_installed: bool = True, ignore_requires_python: bool = False, force_reinstall: bool = False, upgrade_strategy: str = 'to-satisfy-only', use_pep517: bool | None = None, py_version_info: Tuple[int, ...] | None = None) -> BaseResolver:
        """
        Create a Resolver instance for the given parameters.
        """
    def get_requirements(self, args: List[str], options: Values, finder: PackageFinder, session: PipSession) -> List[InstallRequirement]:
        """
        Parse command-line arguments into the corresponding requirements.
        """
    @staticmethod
    def trace_basic_info(finder: PackageFinder) -> None:
        """
        Trace basic information about the provided objects.
        """
