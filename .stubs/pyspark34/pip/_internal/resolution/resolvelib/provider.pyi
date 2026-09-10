from .base import Candidate as Candidate, Constraint as Constraint, Requirement as Requirement
from .candidates import REQUIRES_PYTHON_IDENTIFIER as REQUIRES_PYTHON_IDENTIFIER
from .factory import Factory as Factory
from pip._vendor.resolvelib.providers import AbstractProvider as AbstractProvider, Preference as Preference
from pip._vendor.resolvelib.resolvers import RequirementInformation as RequirementInformation
from typing import Dict, Iterable, Iterator, Mapping, Sequence, TypeVar

PreferenceInformation = RequirementInformation[Requirement, Candidate]
D = TypeVar('D')
V = TypeVar('V')

class PipProvider(_ProviderBase):
    """Pip's provider implementation for resolvelib.

    :params constraints: A mapping of constraints specified by the user. Keys
        are canonicalized project names.
    :params ignore_dependencies: Whether the user specified ``--no-deps``.
    :params upgrade_strategy: The user-specified upgrade strategy.
    :params user_requested: A set of canonicalized package names that the user
        supplied for pip to install/upgrade.
    """
    def __init__(self, factory: Factory, constraints: Dict[str, Constraint], ignore_dependencies: bool, upgrade_strategy: str, user_requested: Dict[str, int]) -> None: ...
    def identify(self, requirement_or_candidate: Requirement | Candidate) -> str: ...
    def get_preference(self, identifier: str, resolutions: Mapping[str, Candidate], candidates: Mapping[str, Iterator[Candidate]], information: Mapping[str, Iterable['PreferenceInformation']], backtrack_causes: Sequence['PreferenceInformation']) -> Preference:
        '''Produce a sort key for given requirement based on preference.

        The lower the return value is, the more preferred this group of
        arguments is.

        Currently pip considers the following in order:

        * Prefer if any of the known requirements is "direct", e.g. points to an
          explicit URL.
        * If equal, prefer if any requirement is "pinned", i.e. contains
          operator ``===`` or ``==``.
        * If equal, calculate an approximate "depth" and resolve requirements
          closer to the user-specified requirements first. If the depth cannot
          by determined (eg: due to no matching parents), it is considered
          infinite.
        * Order user-specified requirements by the order they are specified.
        * If equal, prefers "non-free" requirements, i.e. contains at least one
          operator, such as ``>=`` or ``<``.
        * If equal, order alphabetically for consistency (helps debuggability).
        '''
    def find_matches(self, identifier: str, requirements: Mapping[str, Iterator[Requirement]], incompatibilities: Mapping[str, Iterator[Candidate]]) -> Iterable[Candidate]: ...
    def is_satisfied_by(self, requirement: Requirement, candidate: Candidate) -> bool: ...
    def get_dependencies(self, candidate: Candidate) -> Sequence[Requirement]: ...
    @staticmethod
    def is_backtrack_cause(identifier: str, backtrack_causes: Sequence['PreferenceInformation']) -> bool: ...
