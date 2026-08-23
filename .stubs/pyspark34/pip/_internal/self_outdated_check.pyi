import datetime
import optparse
from _typeshed import Incomplete
from dataclasses import dataclass
from pip._internal.index.collector import LinkCollector as LinkCollector
from pip._internal.index.package_finder import PackageFinder as PackageFinder
from pip._internal.metadata import get_default_environment as get_default_environment
from pip._internal.metadata.base import DistributionVersion as DistributionVersion
from pip._internal.models.selection_prefs import SelectionPreferences as SelectionPreferences
from pip._internal.network.session import PipSession as PipSession
from pip._internal.utils.compat import WINDOWS as WINDOWS
from pip._internal.utils.entrypoints import get_best_invocation_for_this_pip as get_best_invocation_for_this_pip, get_best_invocation_for_this_python as get_best_invocation_for_this_python
from pip._internal.utils.filesystem import adjacent_tmp_file as adjacent_tmp_file, check_path_owner as check_path_owner, replace as replace
from pip._internal.utils.misc import ensure_dir as ensure_dir
from pip._vendor.rich.console import Group as Group
from pip._vendor.rich.markup import escape as escape
from pip._vendor.rich.text import Text as Text

logger: Incomplete

class SelfCheckState:
    def __init__(self, cache_dir: str) -> None: ...
    @property
    def key(self) -> str: ...
    def get(self, current_time: datetime.datetime) -> str | None:
        """Check if we have a not-outdated version loaded already."""
    def set(self, pypi_version: str, current_time: datetime.datetime) -> None: ...

@dataclass
class UpgradePrompt:
    old: str
    new: str
    def __rich__(self) -> Group: ...
    def __init__(self, old, new) -> None: ...

def was_installed_by_pip(pkg: str) -> bool:
    """Checks whether pkg was installed by pip

    This is used not to display the upgrade message when pip is in fact
    installed by system package manager, such as dnf on Fedora.
    """
def pip_self_version_check(session: PipSession, options: optparse.Values) -> None:
    """Check for an update for pip.

    Limit the frequency of checks to once per week. State is stored either in
    the active virtualenv or in the user's USER_CACHE_DIR keyed off the prefix
    of the pip script path.
    """
