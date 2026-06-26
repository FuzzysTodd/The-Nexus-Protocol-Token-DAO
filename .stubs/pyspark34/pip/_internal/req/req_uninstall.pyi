from _typeshed import Incomplete
from pip._internal.exceptions import UninstallationError as UninstallationError
from pip._internal.locations import get_bin_prefix as get_bin_prefix, get_bin_user as get_bin_user
from pip._internal.metadata import BaseDistribution as BaseDistribution
from pip._internal.utils.compat import WINDOWS as WINDOWS
from pip._internal.utils.egg_link import egg_link_path_from_location as egg_link_path_from_location
from pip._internal.utils.logging import getLogger as getLogger, indent_log as indent_log
from pip._internal.utils.misc import ask as ask, normalize_path as normalize_path, renames as renames, rmtree as rmtree
from pip._internal.utils.temp_dir import AdjacentTempDirectory as AdjacentTempDirectory, TempDirectory as TempDirectory
from pip._internal.utils.virtualenv import running_under_virtualenv as running_under_virtualenv
from typing import Generator, Iterable, Set, Tuple

logger: Incomplete

def uninstallation_paths(dist: BaseDistribution) -> Generator[str, None, None]:
    """
    Yield all the uninstallation paths for dist based on RECORD-without-.py[co]

    Yield paths to all the files in RECORD. For each .py file in RECORD, add
    the .pyc and .pyo in the same directory.

    UninstallPathSet.add() takes care of the __pycache__ .py[co].

    If RECORD is not found, raises UninstallationError,
    with possible information from the INSTALLER file.

    https://packaging.python.org/specifications/recording-installed-packages/
    """
def compact(paths: Iterable[str]) -> Set[str]:
    """Compact a path set to contain the minimal number of paths
    necessary to contain all paths in the set. If /a/path/ and
    /a/path/to/a/file.txt are both in the set, leave only the
    shorter path."""
def compress_for_rename(paths: Iterable[str]) -> Set[str]:
    """Returns a set containing the paths that need to be renamed.

    This set may include directories when the original sequence of paths
    included every file on disk.
    """
def compress_for_output_listing(paths: Iterable[str]) -> Tuple[Set[str], Set[str]]:
    """Returns a tuple of 2 sets of which paths to display to user

    The first set contains paths that would be deleted. Files of a package
    are not added and the top-level directory of the package has a '*' added
    at the end - to signify that all it's contents are removed.

    The second set contains files that would have been skipped in the above
    folders.
    """

class StashedUninstallPathSet:
    """A set of file rename operations to stash files while
    tentatively uninstalling them."""
    def __init__(self) -> None: ...
    def stash(self, path: str) -> str:
        """Stashes the directory or file and returns its new location.
        Handle symlinks as files to avoid modifying the symlink targets.
        """
    def commit(self) -> None:
        """Commits the uninstall by removing stashed files."""
    def rollback(self) -> None:
        """Undoes the uninstall by moving stashed files back."""
    @property
    def can_rollback(self) -> bool: ...

class UninstallPathSet:
    """A set of file paths to be removed in the uninstallation of a
    requirement."""
    def __init__(self, dist: BaseDistribution) -> None: ...
    def add(self, path: str) -> None: ...
    def add_pth(self, pth_file: str, entry: str) -> None: ...
    def remove(self, auto_confirm: bool = False, verbose: bool = False) -> None:
        """Remove paths in ``self._paths`` with confirmation (unless
        ``auto_confirm`` is True)."""
    def rollback(self) -> None:
        """Rollback the changes previously made by remove()."""
    def commit(self) -> None:
        """Remove temporary save dir: rollback will no longer be possible."""
    @classmethod
    def from_dist(cls, dist: BaseDistribution) -> UninstallPathSet: ...

class UninstallPthEntries:
    file: Incomplete
    entries: Incomplete
    def __init__(self, pth_file: str) -> None: ...
    def add(self, entry: str) -> None: ...
    def remove(self) -> None: ...
    def rollback(self) -> bool: ...
