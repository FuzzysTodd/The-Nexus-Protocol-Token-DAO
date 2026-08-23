from .base import Candidate as Candidate, CandidateVersion as CandidateVersion, Requirement as Requirement, format_name as format_name
from .factory import Factory as Factory
from _typeshed import Incomplete
from pip._internal.exceptions import HashError as HashError, InstallationSubprocessError as InstallationSubprocessError, MetadataInconsistent as MetadataInconsistent
from pip._internal.metadata import BaseDistribution as BaseDistribution
from pip._internal.models.link import Link as Link, links_equivalent as links_equivalent
from pip._internal.models.wheel import Wheel as Wheel
from pip._internal.req.constructors import install_req_from_editable as install_req_from_editable, install_req_from_line as install_req_from_line
from pip._internal.req.req_install import InstallRequirement as InstallRequirement
from pip._internal.utils.direct_url_helpers import direct_url_from_link as direct_url_from_link
from pip._internal.utils.misc import normalize_version_info as normalize_version_info
from pip._vendor.packaging.utils import NormalizedName as NormalizedName, canonicalize_name as canonicalize_name
from pip._vendor.packaging.version import Version as Version
from typing import Any, FrozenSet, Iterable, Tuple

logger: Incomplete
BaseCandidate: Incomplete
REQUIRES_PYTHON_IDENTIFIER: Incomplete

def as_base_candidate(candidate: Candidate) -> BaseCandidate | None:
    """The runtime version of BaseCandidate."""
def make_install_req_from_link(link: Link, template: InstallRequirement) -> InstallRequirement: ...
def make_install_req_from_editable(link: Link, template: InstallRequirement) -> InstallRequirement: ...

class _InstallRequirementBackedCandidate(Candidate):
    '''A candidate backed by an ``InstallRequirement``.

    This represents a package request with the target not being already
    in the environment, and needs to be fetched and installed. The backing
    ``InstallRequirement`` is responsible for most of the leg work; this
    class exposes appropriate information to the resolver.

    :param link: The link passed to the ``InstallRequirement``. The backing
        ``InstallRequirement`` will use this link to fetch the distribution.
    :param source_link: The link this candidate "originates" from. This is
        different from ``link`` when the link is found in the wheel cache.
        ``link`` would point to the wheel cache, while this points to the
        found remote link (e.g. from pypi.org).
    '''
    dist: BaseDistribution
    is_installed: bool
    def __init__(self, link: Link, source_link: Link, ireq: InstallRequirement, factory: Factory, name: NormalizedName | None = None, version: CandidateVersion | None = None) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    @property
    def source_link(self) -> Link | None: ...
    @property
    def project_name(self) -> NormalizedName:
        """The normalised name of the project the candidate refers to"""
    @property
    def name(self) -> str: ...
    @property
    def version(self) -> CandidateVersion: ...
    def format_for_error(self) -> str: ...
    def iter_dependencies(self, with_requires: bool) -> Iterable[Requirement | None]: ...
    def get_install_requirement(self) -> InstallRequirement | None: ...

class LinkCandidate(_InstallRequirementBackedCandidate):
    is_editable: bool
    def __init__(self, link: Link, template: InstallRequirement, factory: Factory, name: NormalizedName | None = None, version: CandidateVersion | None = None) -> None: ...

class EditableCandidate(_InstallRequirementBackedCandidate):
    is_editable: bool
    def __init__(self, link: Link, template: InstallRequirement, factory: Factory, name: NormalizedName | None = None, version: CandidateVersion | None = None) -> None: ...

class AlreadyInstalledCandidate(Candidate):
    is_installed: bool
    source_link: Incomplete
    dist: Incomplete
    def __init__(self, dist: BaseDistribution, template: InstallRequirement, factory: Factory) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    @property
    def project_name(self) -> NormalizedName: ...
    @property
    def name(self) -> str: ...
    @property
    def version(self) -> CandidateVersion: ...
    @property
    def is_editable(self) -> bool: ...
    def format_for_error(self) -> str: ...
    def iter_dependencies(self, with_requires: bool) -> Iterable[Requirement | None]: ...
    def get_install_requirement(self) -> InstallRequirement | None: ...

class ExtrasCandidate(Candidate):
    '''A candidate that has \'extras\', indicating additional dependencies.

    Requirements can be for a project with dependencies, something like
    foo[extra].  The extras don\'t affect the project/version being installed
    directly, but indicate that we need additional dependencies. We model that
    by having an artificial ExtrasCandidate that wraps the "base" candidate.

    The ExtrasCandidate differs from the base in the following ways:

    1. It has a unique name, of the form foo[extra]. This causes the resolver
       to treat it as a separate node in the dependency graph.
    2. When we\'re getting the candidate\'s dependencies,
       a) We specify that we want the extra dependencies as well.
       b) We add a dependency on the base candidate.
          See below for why this is needed.
    3. We return None for the underlying InstallRequirement, as the base
       candidate will provide it, and we don\'t want to end up with duplicates.

    The dependency on the base candidate is needed so that the resolver can\'t
    decide that it should recommend foo[extra1] version 1.0 and foo[extra2]
    version 2.0. Having those candidates depend on foo=1.0 and foo=2.0
    respectively forces the resolver to recognise that this is a conflict.
    '''
    base: Incomplete
    extras: Incomplete
    def __init__(self, base: BaseCandidate, extras: FrozenSet[str], *, comes_from: InstallRequirement | None = None) -> None:
        """
        :param comes_from: the InstallRequirement that led to this candidate if it
            differs from the base's InstallRequirement. This will often be the
            case in the sense that this candidate's requirement has the extras
            while the base's does not. Unlike the InstallRequirement backed
            candidates, this requirement is used solely for reporting purposes,
            it does not do any leg work.
        """
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    @property
    def project_name(self) -> NormalizedName: ...
    @property
    def name(self) -> str:
        """The normalised name of the project the candidate refers to"""
    @property
    def version(self) -> CandidateVersion: ...
    def format_for_error(self) -> str: ...
    @property
    def is_installed(self) -> bool: ...
    @property
    def is_editable(self) -> bool: ...
    @property
    def source_link(self) -> Link | None: ...
    def iter_dependencies(self, with_requires: bool) -> Iterable[Requirement | None]: ...
    def get_install_requirement(self) -> InstallRequirement | None: ...

class RequiresPythonCandidate(Candidate):
    is_installed: bool
    source_link: Incomplete
    def __init__(self, py_version_info: Tuple[int, ...] | None) -> None: ...
    @property
    def project_name(self) -> NormalizedName: ...
    @property
    def name(self) -> str: ...
    @property
    def version(self) -> CandidateVersion: ...
    def format_for_error(self) -> str: ...
    def iter_dependencies(self, with_requires: bool) -> Iterable[Requirement | None]: ...
    def get_install_requirement(self) -> InstallRequirement | None: ...
