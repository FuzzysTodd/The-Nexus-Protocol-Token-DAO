from _typeshed import Incomplete
from pip._internal.exceptions import BadCommand as BadCommand, InstallationError as InstallationError
from pip._internal.metadata import BaseDistribution as BaseDistribution, get_environment as get_environment
from pip._internal.req.constructors import install_req_from_editable as install_req_from_editable, install_req_from_line as install_req_from_line
from pip._internal.req.req_file import COMMENT_RE as COMMENT_RE
from pip._internal.utils.direct_url_helpers import direct_url_as_pep440_direct_reference as direct_url_as_pep440_direct_reference
from pip._vendor.packaging.utils import canonicalize_name as canonicalize_name
from pip._vendor.packaging.version import Version as Version
from typing import Container, Generator, Iterable, List, NamedTuple

logger: Incomplete

class _EditableInfo(NamedTuple):
    requirement: str
    comments: List[str]

def freeze(requirement: List[str] | None = None, local_only: bool = False, user_only: bool = False, paths: List[str] | None = None, isolated: bool = False, exclude_editable: bool = False, skip: Container[str] = ()) -> Generator[str, None, None]: ...

class FrozenRequirement:
    name: Incomplete
    canonical_name: Incomplete
    req: Incomplete
    editable: Incomplete
    comments: Incomplete
    def __init__(self, name: str, req: str, editable: bool, comments: Iterable[str] = ()) -> None: ...
    @classmethod
    def from_dist(cls, dist: BaseDistribution) -> FrozenRequirement: ...
