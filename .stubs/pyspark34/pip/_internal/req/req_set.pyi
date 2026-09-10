from _typeshed import Incomplete
from pip._internal.req.req_install import InstallRequirement as InstallRequirement
from pip._internal.utils.deprecation import deprecated as deprecated
from pip._vendor.packaging.specifiers import LegacySpecifier as LegacySpecifier
from pip._vendor.packaging.utils import canonicalize_name as canonicalize_name
from pip._vendor.packaging.version import LegacyVersion as LegacyVersion
from typing import List

logger: Incomplete

class RequirementSet:
    requirements: Incomplete
    check_supported_wheels: Incomplete
    unnamed_requirements: Incomplete
    def __init__(self, check_supported_wheels: bool = True) -> None:
        """Create a RequirementSet."""
    def add_unnamed_requirement(self, install_req: InstallRequirement) -> None: ...
    def add_named_requirement(self, install_req: InstallRequirement) -> None: ...
    def has_requirement(self, name: str) -> bool: ...
    def get_requirement(self, name: str) -> InstallRequirement: ...
    @property
    def all_requirements(self) -> List[InstallRequirement]: ...
    @property
    def requirements_to_install(self) -> List[InstallRequirement]:
        """Return the list of requirements that need to be installed.

        TODO remove this property together with the legacy resolver, since the new
             resolver only returns requirements that need to be installed.
        """
    def warn_legacy_versions_and_specifiers(self) -> None: ...
