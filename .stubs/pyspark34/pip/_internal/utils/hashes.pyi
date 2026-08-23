from _typeshed import Incomplete
from pip._internal.exceptions import HashMismatch as HashMismatch, HashMissing as HashMissing, InstallationError as InstallationError
from pip._internal.utils.misc import read_chunks as read_chunks
from typing import BinaryIO, Dict, Iterable, List

FAVORITE_HASH: str
STRONG_HASHES: Incomplete

class Hashes:
    """A wrapper that builds multiple hashes at once and checks them against
    known-good values

    """
    def __init__(self, hashes: Dict[str, List[str]] | None = None) -> None:
        """
        :param hashes: A dict of algorithm names pointing to lists of allowed
            hex digests
        """
    def __and__(self, other: Hashes) -> Hashes: ...
    @property
    def digest_count(self) -> int: ...
    def is_hash_allowed(self, hash_name: str, hex_digest: str) -> bool:
        """Return whether the given hex digest is allowed."""
    def check_against_chunks(self, chunks: Iterable[bytes]) -> None:
        """Check good hashes against ones built from iterable of chunks of
        data.

        Raise HashMismatch if none match.

        """
    def check_against_file(self, file: BinaryIO) -> None:
        """Check good hashes against a file-like object

        Raise HashMismatch if none match.

        """
    def check_against_path(self, path: str) -> None: ...
    def has_one_of(self, hashes: Dict[str, str]) -> bool:
        """Return whether any of the given hashes are allowed."""
    def __bool__(self) -> bool:
        """Return whether I know any known-good hashes."""
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class MissingHashes(Hashes):
    """A workalike for Hashes used when we're missing a hash for a requirement

    It computes the actual hash of the requirement and raises a HashMissing
    exception showing it to the user.

    """
    def __init__(self) -> None:
        """Don't offer the ``hashes`` kwarg."""
