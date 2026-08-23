from pip._internal.distributions.base import AbstractDistribution as AbstractDistribution
from pip._internal.index.package_finder import PackageFinder as PackageFinder
from pip._internal.metadata import BaseDistribution as BaseDistribution, FilesystemWheel as FilesystemWheel, get_wheel_distribution as get_wheel_distribution
from pip._vendor.packaging.utils import canonicalize_name as canonicalize_name

class WheelDistribution(AbstractDistribution):
    """Represents a wheel distribution.

    This does not need any preparation as wheels can be directly unpacked.
    """
    @property
    def build_tracker_id(self) -> str | None: ...
    def get_metadata_distribution(self) -> BaseDistribution:
        """Loads the metadata from the wheel file into memory and returns a
        Distribution that uses it, not relying on the wheel file or
        requirement.
        """
    def prepare_distribution_metadata(self, finder: PackageFinder, build_isolation: bool, check_build_deps: bool) -> None: ...
