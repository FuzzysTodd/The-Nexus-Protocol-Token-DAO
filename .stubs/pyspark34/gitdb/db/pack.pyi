from _typeshed import Incomplete
from collections.abc import Generator
from gitdb.db.base import CachingDB, FileDBBase, ObjectDBR
from gitdb.util import LazyMixin

__all__ = ['PackedDB']

class PackedDB(FileDBBase, ObjectDBR, CachingDB, LazyMixin):
    """A database operating on a set of object packs"""
    def __init__(self, root_path) -> None: ...
    def has_object(self, sha): ...
    def info(self, sha): ...
    def stream(self, sha): ...
    def sha_iter(self) -> Generator[Incomplete, None, None]: ...
    def size(self): ...
    def store(self, istream) -> None:
        """Storing individual objects is not feasible as a pack is designed to
        hold multiple objects. Writing or rewriting packs for single objects is
        inefficient"""
    def update_cache(self, force: bool = False):
        """
        Update our cache with the actually existing packs on disk. Add new ones,
        and remove deleted ones. We keep the unchanged ones

        :param force: If True, the cache will be updated even though the directory
            does not appear to have changed according to its modification timestamp.
        :return: True if the packs have been updated so there is new information,
            False if there was no change to the pack database"""
    def entities(self):
        """:return: list of pack entities operated upon by this database"""
    def partial_to_complete_sha(self, partial_binsha, canonical_length):
        """:return: 20 byte sha as inferred by the given partial binary sha
        :param partial_binsha: binary sha with less than 20 bytes
        :param canonical_length: length of the corresponding canonical representation.
            It is required as binary sha's cannot display whether the original hex sha
            had an odd or even number of characters
        :raise AmbiguousObjectName:
        :raise BadObject: """
