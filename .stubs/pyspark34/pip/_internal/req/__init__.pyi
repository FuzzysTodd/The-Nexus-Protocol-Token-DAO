from .req_file import parse_requirements as parse_requirements
from .req_install import InstallRequirement as InstallRequirement
from .req_set import RequirementSet as RequirementSet
from _typeshed import Incomplete
from typing import List, Sequence

__all__ = ['RequirementSet', 'InstallRequirement', 'parse_requirements', 'install_given_reqs']

class InstallationResult:
    name: Incomplete
    def __init__(self, name: str) -> None: ...

def install_given_reqs(requirements: List[InstallRequirement], global_options: Sequence[str], root: str | None, home: str | None, prefix: str | None, warn_script_location: bool, use_user_site: bool, pycompile: bool) -> List[InstallationResult]:
    """
    Install everything in the given list.

    (to be called after having downloaded and unpacked the packages)
    """
