from _typeshed import Incomplete
from optparse import Values
from pip._internal.cache import WheelCache as WheelCache
from pip._internal.cli import cmdoptions as cmdoptions
from pip._internal.cli.cmdoptions import make_target_python as make_target_python
from pip._internal.cli.req_command import RequirementCommand as RequirementCommand, warn_if_run_as_root as warn_if_run_as_root, with_cleanup as with_cleanup
from pip._internal.cli.status_codes import ERROR as ERROR, SUCCESS as SUCCESS
from pip._internal.exceptions import CommandError as CommandError, InstallationError as InstallationError
from pip._internal.locations import get_scheme as get_scheme
from pip._internal.metadata import get_environment as get_environment
from pip._internal.models.installation_report import InstallationReport as InstallationReport
from pip._internal.operations.build.build_tracker import get_build_tracker as get_build_tracker
from pip._internal.operations.check import ConflictDetails as ConflictDetails, check_install_conflicts as check_install_conflicts
from pip._internal.req import install_given_reqs as install_given_reqs
from pip._internal.req.req_install import InstallRequirement as InstallRequirement, check_legacy_setup_py_options as check_legacy_setup_py_options
from pip._internal.utils.compat import WINDOWS as WINDOWS
from pip._internal.utils.filesystem import test_writable_dir as test_writable_dir
from pip._internal.utils.logging import getLogger as getLogger
from pip._internal.utils.misc import check_externally_managed as check_externally_managed, ensure_dir as ensure_dir, get_pip_version as get_pip_version, protect_pip_from_modification_on_windows as protect_pip_from_modification_on_windows, write_output as write_output
from pip._internal.utils.temp_dir import TempDirectory as TempDirectory
from pip._internal.utils.virtualenv import running_under_virtualenv as running_under_virtualenv, virtualenv_no_global as virtualenv_no_global
from pip._internal.wheel_builder import build as build, should_build_for_install_command as should_build_for_install_command
from pip._vendor.rich import print_json as print_json
from typing import List

logger: Incomplete

class InstallCommand(RequirementCommand):
    '''
    Install packages from:

    - PyPI (and other indexes) using requirement specifiers.
    - VCS project urls.
    - Local project directories.
    - Local or remote source archives.

    pip also supports installing from "requirements files", which provide
    an easy way to specify a whole environment to be installed.
    '''
    usage: str
    def add_options(self) -> None: ...
    def run(self, options: Values, args: List[str]) -> int: ...

def get_lib_location_guesses(user: bool = False, home: str | None = None, root: str | None = None, isolated: bool = False, prefix: str | None = None) -> List[str]: ...
def site_packages_writable(root: str | None, isolated: bool) -> bool: ...
def decide_user_install(use_user_site: bool | None, prefix_path: str | None = None, target_dir: str | None = None, root_path: str | None = None, isolated_mode: bool = False) -> bool:
    """Determine whether to do a user install based on the input options.

    If use_user_site is False, no additional checks are done.
    If use_user_site is True, it is checked for compatibility with other
    options.
    If use_user_site is None, the default behaviour depends on the environment,
    which is provided by the other arguments.
    """
def create_os_error_message(error: OSError, show_traceback: bool, using_user_site: bool) -> str:
    """Format an error message for an OSError

    It may occur anytime during the execution of the install command.
    """
