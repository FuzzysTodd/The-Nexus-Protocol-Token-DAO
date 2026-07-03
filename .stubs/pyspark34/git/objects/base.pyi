from _typeshed import Incomplete
from git.refs.reference import Reference
from git.repo import Repo
from git.types import Commit_ish, Lit_commit_ish, PathLike
from git.util import LazyMixin
from gitdb.base import OStream
from typing import Any

__all__ = ['Object', 'IndexObject']

class Object(LazyMixin):
    """Implements an Object which may be Blobs, Trees, Commits and Tags"""
    NULL_HEX_SHA: Incomplete
    NULL_BIN_SHA: Incomplete
    TYPES: Incomplete
    type: Lit_commit_ish | None
    repo: Incomplete
    binsha: Incomplete
    def __init__(self, repo: Repo, binsha: bytes) -> None:
        """Initialize an object by identifying it by its binary sha.
        All keyword arguments will be set on demand if None.

        :param repo: repository this object is located in

        :param binsha: 20 byte SHA1"""
    @classmethod
    def new(cls, repo: Repo, id: str | Reference) -> Commit_ish:
        """
        :return: New Object instance of a type appropriate to the object type behind
            id. The id of the newly created object will be a binsha even though
            the input id may have been a Reference or Rev-Spec

        :param id: reference, rev-spec, or hexsha

        :note: This cannot be a __new__ method as it would always call __init__
            with the input id which is not necessarily a binsha."""
    @classmethod
    def new_from_sha(cls, repo: Repo, sha1: bytes) -> Commit_ish:
        """
        :return: new object instance of a type appropriate to represent the given
            binary sha1
        :param sha1: 20 byte binary sha1"""
    def __eq__(self, other: Any) -> bool:
        """:return: True if the objects have the same SHA1"""
    def __ne__(self, other: Any) -> bool:
        """:return: True if the objects do not have the same SHA1"""
    def __hash__(self) -> int:
        """:return: Hash of our id allowing objects to be used in dicts and sets"""
    @property
    def hexsha(self) -> str:
        """:return: 40 byte hex version of our 20 byte binary sha"""
    @property
    def data_stream(self) -> OStream:
        """:return:  File Object compatible stream to the uncompressed raw data of the object
        :note: returned streams must be read in order"""
    def stream_data(self, ostream: OStream) -> Object:
        """Writes our data directly to the given output stream

        :param ostream: File object compatible stream object.
        :return: self"""

class IndexObject(Object):
    """Base for all objects that can be part of the index file , namely Tree, Blob and
    SubModule objects"""
    mode: Incomplete
    path: Incomplete
    def __init__(self, repo: Repo, binsha: bytes, mode: None | int = None, path: None | PathLike = None) -> None:
        """Initialize a newly instanced IndexObject

        :param repo: is the Repo we are located in
        :param binsha: 20 byte sha1
        :param mode:
            is the stat compatible file mode as int, use the stat module
            to evaluate the information
        :param path:
            is the path to the file in the file system, relative to the git repository root, i.e.
            file.ext or folder/other.ext
        :note:
            Path may not be set of the index object has been created directly as it cannot
            be retrieved without knowing the parent tree."""
    def __hash__(self) -> int:
        """
        :return:
            Hash of our path as index items are uniquely identifiable by path, not
            by their data !"""
    @property
    def name(self) -> str:
        """:return: Name portion of the path, effectively being the basename"""
    @property
    def abspath(self) -> PathLike:
        """
        :return:
            Absolute path to this index object in the file system ( as opposed to the
            .path field which is a path relative to the git repository ).

            The returned path will be native to the system and contains '' on windows."""
