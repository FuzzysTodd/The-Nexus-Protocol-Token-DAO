from .base import Candidate as Candidate, Requirement as Requirement
from .factory import Factory as Factory
from _typeshed import Incomplete
from pip._internal.cache import WheelCache as WheelCache
from pip._internal.index.package_finder import PackageFinder as PackageFinder
from pip._internal.operations.prepare import RequirementPreparer as RequirementPreparer
from pip._internal.req.constructors import install_req_extend_extras as install_req_extend_extras
from pip._internal.req.req_install import InstallRequirement as InstallRequirement
from pip._internal.req.req_set import RequirementSet as RequirementSet
from pip._internal.resolution.base import BaseResolver as BaseResolver, InstallRequirementProvider as InstallRequirementProvider
from pip._internal.resolution.resolvelib.provider import PipProvider as PipProvider
from pip._internal.resolution.resolvelib.reporter import PipDebuggingReporter as PipDebuggingReporter, PipReporter as PipReporter
from pip._internal.utils.packaging import get_requirement as get_requirement
from pip._vendor.packaging.utils import canonicalize_name as canonicalize_name
from pip._vendor.resolvelib import BaseReporter as BaseReporter, ResolutionImpossible as ResolutionImpossible
from pip._vendor.resolvelib.resolvers import Result as RLResult
from pip._vendor.resolvelib.structs import DirectedGraph as DirectedGraph
from typing import Dict, List, Set, Tuple

Result = RLResult[Requirement, Candidate, str]
logger: Incomplete

class Resolver(BaseResolver):
    factory: Incomplete
    ignore_dependencies: Incomplete
    upgrade_strategy: Incomplete
    def __init__(self, preparer: RequirementPreparer, finder: PackageFinder, wheel_cache: WheelCache | None, make_install_req: InstallRequirementProvider, use_user_site: bool, ignore_dependencies: bool, ignore_installed: bool, ignore_requires_python: bool, force_reinstall: bool, upgrade_strategy: str, py_version_info: Tuple[int, ...] | None = None) -> None: ...
    def resolve(self, root_reqs: List[InstallRequirement], check_supported_wheels: bool) -> RequirementSet: ...
    def get_installation_order(self, req_set: RequirementSet) -> List[InstallRequirement]:
        """Get order for installation of requirements in RequirementSet.

        The returned list contains a requirement before another that depends on
        it. This helps ensure that the environment is kept consistent as they
        get installed one-by-one.

        The current implementation creates a topological ordering of the
        dependency graph, giving more weight to packages with less
        or no dependencies, while breaking any cycles in the graph at
        arbitrary points. We make no guarantees about where the cycle
        would be broken, other than it *would* be broken.
        """

def get_topological_weights(graph: DirectedGraph[str | None], requirement_keys: Set[str]) -> Dict[str | None, int]:
    '''Assign weights to each node based on how "deep" they are.

    This implementation may change at any point in the future without prior
    notice.

    We first simplify the dependency graph by pruning any leaves and giving them
    the highest weight: a package without any dependencies should be installed
    first. This is done again and again in the same way, giving ever less weight
    to the newly found leaves. The loop stops when no leaves are left: all
    remaining packages have at least one dependency left in the graph.

    Then we continue with the remaining graph, by taking the length for the
    longest path to any node from root, ignoring any paths that contain a single
    node twice (i.e. cycles). This is done through a depth-first search through
    the graph, while keeping track of the path to the node.

    Cycles in the graph result would result in node being revisited while also
    being on its own path. In this case, take no action. This helps ensure we
    don\'t get stuck in a cycle.

    When assigning weight, the longer path (i.e. larger length) is preferred.

    We are only interested in the weights of packages that are in the
    requirement_keys.
    '''
