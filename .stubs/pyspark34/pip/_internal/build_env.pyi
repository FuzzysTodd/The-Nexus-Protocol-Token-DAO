from _typeshed import Incomplete
from pip._internal.cli.spinners import open_spinner as open_spinner
from pip._internal.index.package_finder import PackageFinder as PackageFinder
from pip._internal.locations import get_platlib as get_platlib, get_purelib as get_purelib, get_scheme as get_scheme
from pip._internal.metadata import get_default_environment as get_default_environment, get_environment as get_environment
from pip._internal.utils.subprocess import call_subprocess as call_subprocess
from pip._internal.utils.temp_dir import TempDirectory as TempDirectory, tempdir_kinds as tempdir_kinds
from pip._vendor.certifi import where as where
from pip._vendor.packaging.requirements import Requirement as Requirement
from pip._vendor.packaging.version import Version as Version
from types import TracebackType
from typing import Iterable, Set, Tuple, Type

logger: Incomplete

class _Prefix:
    path: Incomplete
    setup: bool
    bin_dir: Incomplete
    lib_dirs: Incomplete
    def __init__(self, path: str) -> None: ...

def get_runnable_pip() -> str:
    """Get a file to pass to a Python executable, to run the currently-running pip.

    This is used to run a pip subprocess, for installing requirements into the build
    environment.
    """

class BuildEnvironment:
    """Creates and manages an isolated environment to install build deps"""
    def __init__(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...
    def check_requirements(self, reqs: Iterable[str]) -> Tuple[Set[Tuple[str, str]], Set[str]]:
        """Return 2 sets:
        - conflicting requirements: set of (installed, wanted) reqs tuples
        - missing requirements: set of reqs
        """
    def install_requirements(self, finder: PackageFinder, requirements: Iterable[str], prefix_as_string: str, *, kind: str) -> None: ...

class NoOpBuildEnvironment(BuildEnvironment):
    """A no-op drop-in replacement for BuildEnvironment"""
    def __init__(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...
    def cleanup(self) -> None: ...
    def install_requirements(self, finder: PackageFinder, requirements: Iterable[str], prefix_as_string: str, *, kind: str) -> None: ...
