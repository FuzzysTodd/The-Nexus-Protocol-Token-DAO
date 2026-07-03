from _typeshed import Incomplete
from pip._internal.distributions import make_distribution_for_install_requirement as make_distribution_for_install_requirement
from pip._internal.metadata import get_default_environment as get_default_environment
from pip._internal.metadata.base import DistributionVersion as DistributionVersion
from pip._internal.req.req_install import InstallRequirement as InstallRequirement
from pip._internal.utils.deprecation import deprecated as deprecated
from pip._vendor.packaging.requirements import Requirement as Requirement
from pip._vendor.packaging.specifiers import LegacySpecifier as LegacySpecifier
from pip._vendor.packaging.utils import NormalizedName as NormalizedName, canonicalize_name as canonicalize_name
from pip._vendor.packaging.version import LegacyVersion as LegacyVersion
from typing import Callable, Dict, List, NamedTuple, Tuple

logger: Incomplete

class PackageDetails(NamedTuple):
    version: DistributionVersion
    dependencies: List[Requirement]
PackageSet = Dict[NormalizedName, PackageDetails]
Missing = Tuple[NormalizedName, Requirement]
Conflicting = Tuple[NormalizedName, DistributionVersion, Requirement]
MissingDict = Dict[NormalizedName, List[Missing]]
ConflictingDict = Dict[NormalizedName, List[Conflicting]]
CheckResult = Tuple[MissingDict, ConflictingDict]
ConflictDetails = Tuple[PackageSet, CheckResult]

def create_package_set_from_installed() -> Tuple[PackageSet, bool]:
    """Converts a list of distributions into a PackageSet."""
def check_package_set(package_set: PackageSet, should_ignore: Callable[[str], bool] | None = None) -> CheckResult:
    """Check if a package set is consistent

    If should_ignore is passed, it should be a callable that takes a
    package name and returns a boolean.
    """
def check_install_conflicts(to_install: List[InstallRequirement]) -> ConflictDetails:
    """For checking if the dependency graph would be consistent after     installing given requirements
    """
def warn_legacy_versions_and_specifiers(package_set: PackageSet) -> None: ...
