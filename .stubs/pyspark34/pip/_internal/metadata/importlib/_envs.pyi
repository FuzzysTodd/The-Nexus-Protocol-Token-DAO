import importlib
from ._compat import BadMetadata as BadMetadata, BasePath as BasePath, get_dist_name as get_dist_name, get_info_location as get_info_location
from ._dists import Distribution as Distribution
from _typeshed import Incomplete
from pip._internal.metadata.base import BaseDistribution as BaseDistribution, BaseEnvironment as BaseEnvironment
from pip._internal.models.wheel import Wheel as Wheel
from pip._internal.utils.deprecation import deprecated as deprecated
from pip._internal.utils.filetypes import WHEEL_EXTENSION as WHEEL_EXTENSION
from pip._vendor.packaging.utils import NormalizedName as NormalizedName, canonicalize_name as canonicalize_name
from typing import Iterator, List, Sequence, Tuple

logger: Incomplete

class _DistributionFinder:
    """Finder to locate distributions.

    The main purpose of this class is to memoize found distributions' names, so
    only one distribution is returned for each package name. At lot of pip code
    assumes this (because it is setuptools's behavior), and not doing the same
    can potentially cause a distribution in lower precedence path to override a
    higher precedence one if the caller is not careful.

    Eventually we probably want to make it possible to see lower precedence
    installations as well. It's useful feature, after all.
    """
    FoundResult = Tuple[importlib.metadata.Distribution, BasePath | None]
    def __init__(self) -> None: ...
    def find(self, location: str) -> Iterator[BaseDistribution]:
        """Find distributions in a location.

        The path can be either a directory, or a ZIP archive.
        """
    def find_linked(self, location: str) -> Iterator[BaseDistribution]:
        """Read location in egg-link files and return distributions in there.

        The path should be a directory; otherwise this returns nothing. This
        follows how setuptools does this for compatibility. The first non-empty
        line in the egg-link is read as a path (resolved against the egg-link's
        containing directory if relative). Distributions found at that linked
        location are returned.
        """
    def find_eggs(self, location: str) -> Iterator[BaseDistribution]:
        """Find eggs in a location.

        This actually uses the old *pkg_resources* backend. We likely want to
        deprecate this so we can eventually remove the *pkg_resources*
        dependency entirely. Before that, this should first emit a deprecation
        warning for some versions when using the fallback since importing
        *pkg_resources* is slow for those who don't need it.
        """

class Environment(BaseEnvironment):
    def __init__(self, paths: Sequence[str]) -> None: ...
    @classmethod
    def default(cls) -> BaseEnvironment: ...
    @classmethod
    def from_paths(cls, paths: List[str] | None) -> BaseEnvironment: ...
    def get_distribution(self, name: str) -> BaseDistribution | None: ...
