from _typeshed import Incomplete
from pip._internal.cache import WheelCache as WheelCache
from pip._internal.exceptions import InvalidWheelFilename as InvalidWheelFilename, UnsupportedWheel as UnsupportedWheel
from pip._internal.metadata import FilesystemWheel as FilesystemWheel, get_wheel_distribution as get_wheel_distribution
from pip._internal.models.link import Link as Link
from pip._internal.models.wheel import Wheel as Wheel
from pip._internal.operations.build.wheel import build_wheel_pep517 as build_wheel_pep517
from pip._internal.operations.build.wheel_editable import build_wheel_editable as build_wheel_editable
from pip._internal.operations.build.wheel_legacy import build_wheel_legacy as build_wheel_legacy
from pip._internal.req.req_install import InstallRequirement as InstallRequirement
from pip._internal.utils.logging import indent_log as indent_log
from pip._internal.utils.misc import ensure_dir as ensure_dir, hash_file as hash_file
from pip._internal.utils.setuptools_build import make_setuptools_clean_args as make_setuptools_clean_args
from pip._internal.utils.subprocess import call_subprocess as call_subprocess
from pip._internal.utils.temp_dir import TempDirectory as TempDirectory
from pip._internal.utils.urls import path_to_url as path_to_url
from pip._internal.vcs import vcs as vcs
from pip._vendor.packaging.utils import canonicalize_name as canonicalize_name, canonicalize_version as canonicalize_version
from pip._vendor.packaging.version import InvalidVersion as InvalidVersion, Version as Version
from typing import Iterable, List, Tuple

logger: Incomplete
BuildResult = Tuple[List[InstallRequirement], List[InstallRequirement]]

def should_build_for_wheel_command(req: InstallRequirement) -> bool: ...
def should_build_for_install_command(req: InstallRequirement) -> bool: ...
def build(requirements: Iterable[InstallRequirement], wheel_cache: WheelCache, verify: bool, build_options: List[str], global_options: List[str]) -> BuildResult:
    """Build wheels.

    :return: The list of InstallRequirement that succeeded to build and
        the list of InstallRequirement that failed to build.
    """
