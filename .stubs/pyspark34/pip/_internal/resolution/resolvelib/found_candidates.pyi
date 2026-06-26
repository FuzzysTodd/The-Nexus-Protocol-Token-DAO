from .base import Candidate as Candidate
from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, Callable, Iterator, Set

IndexCandidateInfo: Incomplete
SequenceCandidate = Sequence[Candidate]

class FoundCandidates(SequenceCandidate):
    """A lazy sequence to provide candidates to the resolver.

    The intended usage is to return this from `find_matches()` so the resolver
    can iterate through the sequence multiple times, but only access the index
    page when remote packages are actually needed. This improve performances
    when suitable candidates are already installed on disk.
    """
    def __init__(self, get_infos: Callable[[], Iterator[IndexCandidateInfo]], installed: Candidate | None, prefers_installed: bool, incompatible_ids: Set[int]) -> None: ...
    def __getitem__(self, index: Any) -> Any: ...
    def __iter__(self) -> Iterator[Candidate]: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
