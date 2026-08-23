from .symbolic import SymbolicReference, T_References
from _typeshed import Incomplete
from git.repo import Repo
from git.types import Commit_ish, PathLike
from git.util import IterableObj, LazyMixin
from typing import Any, Iterator

__all__ = ['Reference']

class Reference(SymbolicReference, LazyMixin, IterableObj):
    """Represents a named reference to any object. Subclasses may apply restrictions though,
    i.e. Heads can only point to commits."""
    path: Incomplete
    def __init__(self, repo: Repo, path: PathLike, check_path: bool = True) -> None:
        """Initialize this instance

        :param repo: Our parent repository
        :param path:
            Path relative to the .git/ directory pointing to the ref in question, i.e.
            refs/heads/master
        :param check_path: if False, you can provide any path. Otherwise the path must start with the
            default path prefix of this type."""
    def set_object(self, object: Commit_ish | SymbolicReference | str, logmsg: str | None = None) -> Reference:
        """Special version which checks if the head-log needs an update as well

        :return: self"""
    @property
    def name(self) -> str:
        """:return: (shortest) Name of this reference - it may contain path components"""
    @classmethod
    def iter_items(cls, repo: Repo, common_path: PathLike | None = None, *args: Any, **kwargs: Any) -> Iterator[T_References]:
        """Equivalent to SymbolicReference.iter_items, but will return non-detached
        references as well."""
    @property
    def remote_name(self) -> str:
        """
        :return:
            Name of the remote we are a reference of, such as 'origin' for a reference
            named 'origin/master'"""
    @property
    def remote_head(self) -> str:
        """:return: Name of the remote head itself, i.e. master.
        :note: The returned name is usually not qualified enough to uniquely identify
            a branch"""
