from pip._internal.req.req_install import InstallRequirement as InstallRequirement
from pip._internal.req.req_set import RequirementSet as RequirementSet
from typing import Callable, List

InstallRequirementProvider = Callable[[str, InstallRequirement | None], InstallRequirement]

class BaseResolver:
    def resolve(self, root_reqs: List[InstallRequirement], check_supported_wheels: bool) -> RequirementSet: ...
    def get_installation_order(self, req_set: RequirementSet) -> List[InstallRequirement]: ...
