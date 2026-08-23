from _typeshed import Incomplete
from pip._internal.models.link import Link as Link, links_equivalent as links_equivalent
from pip._internal.req.req_install import InstallRequirement as InstallRequirement
from pip._internal.utils.hashes import Hashes as Hashes
from pip._vendor.packaging.specifiers import SpecifierSet as SpecifierSet
from pip._vendor.packaging.utils import NormalizedName as NormalizedName
from pip._vendor.packaging.version import LegacyVersion as LegacyVersion, Version as Version
from typing import FrozenSet, Iterable

CandidateLookup: Incomplete
CandidateVersion = LegacyVersion | Version

def format_name(project: NormalizedName, extras: FrozenSet[NormalizedName]) -> str: ...

class Constraint:
    specifier: Incomplete
    hashes: Incomplete
    links: Incomplete
    def __init__(self, specifier: SpecifierSet, hashes: Hashes, links: FrozenSet[Link]) -> None: ...
    @classmethod
    def empty(cls) -> Constraint: ...
    @classmethod
    def from_ireq(cls, ireq: InstallRequirement) -> Constraint: ...
    def __bool__(self) -> bool: ...
    def __and__(self, other: InstallRequirement) -> Constraint: ...
    def is_satisfied_by(self, candidate: Candidate) -> bool: ...

class Requirement:
    @property
    def project_name(self) -> NormalizedName:
        '''The "project name" of a requirement.

        This is different from ``name`` if this requirement contains extras,
        in which case ``name`` would contain the ``[...]`` part, while this
        refers to the name of the project.
        '''
    @property
    def name(self) -> str:
        """The name identifying this requirement in the resolver.

        This is different from ``project_name`` if this requirement contains
        extras, where ``project_name`` would not contain the ``[...]`` part.
        """
    def is_satisfied_by(self, candidate: Candidate) -> bool: ...
    def get_candidate_lookup(self) -> CandidateLookup: ...
    def format_for_error(self) -> str: ...

class Candidate:
    @property
    def project_name(self) -> NormalizedName:
        '''The "project name" of the candidate.

        This is different from ``name`` if this candidate contains extras,
        in which case ``name`` would contain the ``[...]`` part, while this
        refers to the name of the project.
        '''
    @property
    def name(self) -> str:
        """The name identifying this candidate in the resolver.

        This is different from ``project_name`` if this candidate contains
        extras, where ``project_name`` would not contain the ``[...]`` part.
        """
    @property
    def version(self) -> CandidateVersion: ...
    @property
    def is_installed(self) -> bool: ...
    @property
    def is_editable(self) -> bool: ...
    @property
    def source_link(self) -> Link | None: ...
    def iter_dependencies(self, with_requires: bool) -> Iterable[Requirement | None]: ...
    def get_install_requirement(self) -> InstallRequirement | None: ...
    def format_for_error(self) -> str: ...
