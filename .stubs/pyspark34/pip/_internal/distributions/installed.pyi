from pip._internal.distributions.base import AbstractDistribution as AbstractDistribution
from pip._internal.index.package_finder import PackageFinder as PackageFinder
from pip._internal.metadata import BaseDistribution as BaseDistribution

class InstalledDistribution(AbstractDistribution):
    """Represents an installed package.

    This does not need any preparation as the required information has already
    been computed.
    """
    @property
    def build_tracker_id(self) -> str | None: ...
    def get_metadata_distribution(self) -> BaseDistribution: ...
    def prepare_distribution_metadata(self, finder: PackageFinder, build_isolation: bool, check_build_deps: bool) -> None: ...
