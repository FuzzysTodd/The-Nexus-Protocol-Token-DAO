from _typeshed import Incomplete
from pip._internal.models.link import Link
from pip._internal.req.req_install import InstallRequirement
from pip._vendor.packaging.markers import Marker
from pip._vendor.packaging.requirements import Requirement
from typing import Dict, List, Set, Tuple

__all__ = ['install_req_from_editable', 'install_req_from_line', 'parse_editable']

def parse_editable(editable_req: str) -> Tuple[str | None, str, Set[str]]:
    """Parses an editable requirement into:
        - a requirement name
        - an URL
        - extras
        - editable options
    Accepted requirements:
        svn+http://blahblah@rev#egg=Foobar[baz]&subdirectory=version_subdir
        .[some_extra]
    """

class RequirementParts:
    requirement: Incomplete
    link: Incomplete
    markers: Incomplete
    extras: Incomplete
    def __init__(self, requirement: Requirement | None, link: Link | None, markers: Marker | None, extras: Set[str]) -> None: ...

def install_req_from_editable(editable_req: str, comes_from: InstallRequirement | str | None = None, *, use_pep517: bool | None = None, isolated: bool = False, global_options: List[str] | None = None, hash_options: Dict[str, List[str]] | None = None, constraint: bool = False, user_supplied: bool = False, permit_editable_wheels: bool = False, config_settings: Dict[str, str | List[str]] | None = None) -> InstallRequirement: ...
def install_req_from_line(name: str, comes_from: str | InstallRequirement | None = None, *, use_pep517: bool | None = None, isolated: bool = False, global_options: List[str] | None = None, hash_options: Dict[str, List[str]] | None = None, constraint: bool = False, line_source: str | None = None, user_supplied: bool = False, config_settings: Dict[str, str | List[str]] | None = None) -> InstallRequirement:
    """Creates an InstallRequirement from a name, which might be a
    requirement, directory containing 'setup.py', filename, or URL.

    :param line_source: An optional string describing where the line is from,
        for logging purposes in case of an error.
    """
