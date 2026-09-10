from _typeshed import Incomplete
from pip._internal.build_env import BuildEnvironment as BuildEnvironment
from pip._internal.distributions.base import AbstractDistribution as AbstractDistribution
from pip._internal.exceptions import InstallationError as InstallationError
from pip._internal.index.package_finder import PackageFinder as PackageFinder
from pip._internal.metadata import BaseDistribution as BaseDistribution
from pip._internal.utils.subprocess import runner_with_spinner_message as runner_with_spinner_message

logger: Incomplete

class SourceDistribution(AbstractDistribution):
    """Represents a source distribution.

    The preparation step for these needs metadata for the packages to be
    generated, either using PEP 517 or using the legacy `setup.py egg_info`.
    """
    @property
    def build_tracker_id(self) -> str | None:
        """Identify this requirement uniquely by its link."""
    def get_metadata_distribution(self) -> BaseDistribution: ...
    def prepare_distribution_metadata(self, finder: PackageFinder, build_isolation: bool, check_build_deps: bool) -> None: ...
