from .base import Candidate as Candidate, CandidateVersion as CandidateVersion, Constraint as Constraint, Requirement as Requirement
from .candidates import AlreadyInstalledCandidate as AlreadyInstalledCandidate, BaseCandidate as BaseCandidate, EditableCandidate as EditableCandidate, ExtrasCandidate as ExtrasCandidate, LinkCandidate as LinkCandidate, RequiresPythonCandidate as RequiresPythonCandidate, as_base_candidate as as_base_candidate
from .found_candidates import FoundCandidates as FoundCandidates, IndexCandidateInfo as IndexCandidateInfo
from .requirements import ExplicitRequirement as ExplicitRequirement, RequiresPythonRequirement as RequiresPythonRequirement, SpecifierRequirement as SpecifierRequirement, SpecifierWithoutExtrasRequirement as SpecifierWithoutExtrasRequirement, UnsatisfiableRequirement as UnsatisfiableRequirement
from _typeshed import Incomplete
from pip._internal.cache import CacheEntry as CacheEntry, WheelCache as WheelCache
from pip._internal.exceptions import DistributionNotFound as DistributionNotFound, InstallationError as InstallationError, MetadataInconsistent as MetadataInconsistent, UnsupportedPythonVersion as UnsupportedPythonVersion, UnsupportedWheel as UnsupportedWheel
from pip._internal.index.package_finder import PackageFinder as PackageFinder
from pip._internal.metadata import BaseDistribution as BaseDistribution, get_default_environment as get_default_environment
from pip._internal.models.link import Link as Link
from pip._internal.models.wheel import Wheel as Wheel
from pip._internal.operations.prepare import RequirementPreparer as RequirementPreparer
from pip._internal.req.constructors import install_req_drop_extras as install_req_drop_extras, install_req_from_link_and_ireq as install_req_from_link_and_ireq
from pip._internal.req.req_install import InstallRequirement as InstallRequirement, check_invalid_constraint_type as check_invalid_constraint_type
from pip._internal.resolution.base import InstallRequirementProvider as InstallRequirementProvider
from pip._internal.utils.compatibility_tags import get_supported as get_supported
from pip._internal.utils.hashes import Hashes as Hashes
from pip._internal.utils.packaging import get_requirement as get_requirement
from pip._internal.utils.virtualenv import running_under_virtualenv as running_under_virtualenv
from pip._vendor.packaging.requirements import InvalidRequirement as InvalidRequirement
from pip._vendor.packaging.specifiers import SpecifierSet as SpecifierSet
from pip._vendor.packaging.utils import NormalizedName as NormalizedName, canonicalize_name as canonicalize_name
from pip._vendor.resolvelib import ResolutionImpossible as ResolutionImpossible
from typing import Dict, Iterable, Iterator, List, Mapping, NamedTuple, Protocol, Tuple, TypeVar

class ConflictCause(Protocol):
    requirement: RequiresPythonRequirement
    parent: Candidate

logger: Incomplete
C = TypeVar('C')
Cache = Dict[Link, C]

class CollectedRootRequirements(NamedTuple):
    requirements: List[Requirement]
    constraints: Dict[str, Constraint]
    user_requested: Dict[str, int]

class Factory:
    preparer: Incomplete
    def __init__(self, finder: PackageFinder, preparer: RequirementPreparer, make_install_req: InstallRequirementProvider, wheel_cache: WheelCache | None, use_user_site: bool, force_reinstall: bool, ignore_installed: bool, ignore_requires_python: bool, py_version_info: Tuple[int, ...] | None = None) -> None: ...
    @property
    def force_reinstall(self) -> bool: ...
    def find_candidates(self, identifier: str, requirements: Mapping[str, Iterable[Requirement]], incompatibilities: Mapping[str, Iterator[Candidate]], constraint: Constraint, prefers_installed: bool) -> Iterable[Candidate]: ...
    def collect_root_requirements(self, root_ireqs: List[InstallRequirement]) -> CollectedRootRequirements: ...
    def make_requirement_from_candidate(self, candidate: Candidate) -> ExplicitRequirement: ...
    def make_requirements_from_spec(self, specifier: str, comes_from: InstallRequirement | None, requested_extras: Iterable[str] = ()) -> Iterator[Requirement]:
        """
        Returns requirement objects associated with the given specifier. In most cases
        this will be a single object but the following special cases exist:
            - the specifier has markers that do not apply -> result is empty
            - the specifier has both a constraint and extras -> result is split
                in two requirement objects: one with the constraint and one with the
                extra. This allows centralized constraint handling for the base,
                resulting in fewer candidate rejections.
        """
    def make_requires_python_requirement(self, specifier: SpecifierSet) -> Requirement | None: ...
    def get_wheel_cache_entry(self, link: Link, name: str | None) -> CacheEntry | None:
        """Look up the link in the wheel cache.

        If ``preparer.require_hashes`` is True, don't use the wheel cache,
        because cached wheels, always built locally, have different hashes
        than the files downloaded from the index server and thus throw false
        hash mismatches. Furthermore, cached wheels at present have
        nondeterministic contents due to file modification times.
        """
    def get_dist_to_uninstall(self, candidate: Candidate) -> BaseDistribution | None: ...
    def get_installation_error(self, e: ResolutionImpossible[Requirement, Candidate], constraints: Dict[str, Constraint]) -> InstallationError: ...
