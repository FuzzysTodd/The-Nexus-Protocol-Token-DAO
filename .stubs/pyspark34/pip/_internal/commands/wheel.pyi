from _typeshed import Incomplete
from optparse import Values
from pip._internal.cache import WheelCache as WheelCache
from pip._internal.cli import cmdoptions as cmdoptions
from pip._internal.cli.req_command import RequirementCommand as RequirementCommand, with_cleanup as with_cleanup
from pip._internal.cli.status_codes import SUCCESS as SUCCESS
from pip._internal.exceptions import CommandError as CommandError
from pip._internal.operations.build.build_tracker import get_build_tracker as get_build_tracker
from pip._internal.req.req_install import InstallRequirement as InstallRequirement, check_legacy_setup_py_options as check_legacy_setup_py_options
from pip._internal.utils.misc import ensure_dir as ensure_dir, normalize_path as normalize_path
from pip._internal.utils.temp_dir import TempDirectory as TempDirectory
from pip._internal.wheel_builder import build as build, should_build_for_wheel_command as should_build_for_wheel_command
from typing import List

logger: Incomplete

class WheelCommand(RequirementCommand):
    """
    Build Wheel archives for your requirements and dependencies.

    Wheel is a built-package format, and offers the advantage of not
    recompiling your software during every install. For more details, see the
    wheel docs: https://wheel.readthedocs.io/en/latest/

    'pip wheel' uses the build system interface as described here:
    https://pip.pypa.io/en/stable/reference/build-system/

    """
    usage: str
    def add_options(self) -> None: ...
    def run(self, options: Values, args: List[str]) -> int: ...
