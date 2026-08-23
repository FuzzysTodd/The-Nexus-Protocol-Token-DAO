from _typeshed import Incomplete
from pip._internal.cache import WheelCache as WheelCache
from pip._internal.exceptions import BestVersionAlreadyInstalled as BestVersionAlreadyInstalled, DistributionNotFound as DistributionNotFound, HashError as HashError, HashErrors as HashErrors, InstallationError as InstallationError, NoneMetadataError as NoneMetadataError, UnsupportedPythonVersion as UnsupportedPythonVersion
from pip._internal.index.package_finder import PackageFinder as PackageFinder
from pip._internal.metadata import BaseDistribution as BaseDistribution
from pip._internal.models.link import Link as Link
from pip._internal.models.wheel import Wheel as Wheel
from pip._internal.operations.prepare import RequirementPreparer as RequirementPreparer
from pip._internal.req.req_install import InstallRequirement as InstallRequirement, check_invalid_constraint_type as check_invalid_constraint_type
from pip._internal.req.req_set import RequirementSet as RequirementSet
from pip._internal.resolution.base import BaseResolver as BaseResolver, InstallRequirementProvider as InstallRequirementProvider
from pip._internal.utils import compatibility_tags as compatibility_tags
from pip._internal.utils.compatibility_tags import get_supported as get_supported
from pip._internal.utils.direct_url_helpers import direct_url_from_link as direct_url_from_link
from pip._internal.utils.logging import indent_log as indent_log
from pip._internal.utils.misc import normalize_version_info as normalize_version_info
from pip._internal.utils.packaging import check_requires_python as check_requires_python
from pip._vendor.packaging import specifiers as specifiers
from pip._vendor.packaging.requirements import Requirement as Requirement
from typing import DefaultDict, List, Tuple

logger: Incomplete
DiscoveredDependencies = DefaultDict[str, List[InstallRequirement]]

class Resolver(BaseResolver):
    """Resolves which packages need to be installed/uninstalled to perform     the requested operation without breaking the requirements of any package.
    """
    preparer: Incomplete
    finder: Incomplete
    wheel_cache: Incomplete
    upgrade_strategy: Incomplete
    force_reinstall: Incomplete
    ignore_dependencies: Incomplete
    ignore_installed: Incomplete
    ignore_requires_python: Incomplete
    use_user_site: Incomplete
    def __init__(self, preparer: RequirementPreparer, finder: PackageFinder, wheel_cache: WheelCache | None, make_install_req: InstallRequirementProvider, use_user_site: bool, ignore_dependencies: bool, ignore_installed: bool, ignore_requires_python: bool, force_reinstall: bool, upgrade_strategy: str, py_version_info: Tuple[int, ...] | None = None) -> None: ...
    def resolve(self, root_reqs: List[InstallRequirement], check_supported_wheels: bool) -> RequirementSet:
        """Resolve what operations need to be done

        As a side-effect of this method, the packages (and their dependencies)
        are downloaded, unpacked and prepared for installation. This
        preparation is done by ``pip.operations.prepare``.

        Once PyPI has static dependency metadata available, it would be
        possible to move the preparation to become a step separated from
        dependency resolution.
        """
    def get_installation_order(self, req_set: RequirementSet) -> List[InstallRequirement]:
        """Create the installation order.

        The installation order is topological - requirements are installed
        before the requiring thing. We break cycles at an arbitrary point,
        and make no other guarantees.
        """
