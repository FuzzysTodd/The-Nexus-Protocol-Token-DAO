from .head import Head
from git import Remote
from git.repo import Repo
from git.types import PathLike
from typing import Any, Iterator, NoReturn

__all__ = ['RemoteReference']

class RemoteReference(Head):
    """Represents a reference pointing to a remote head."""
    @classmethod
    def iter_items(cls, repo: Repo, common_path: PathLike | None = None, remote: Remote | None = None, *args: Any, **kwargs: Any) -> Iterator['RemoteReference']:
        """Iterate remote references, and if given, constrain them to the given remote"""
    @classmethod
    def delete(cls, repo: Repo, *refs: RemoteReference, **kwargs: Any) -> None:
        """Delete the given remote references

        :note:
            kwargs are given for comparability with the base class method as we
            should not narrow the signature."""
    @classmethod
    def create(cls, *args: Any, **kwargs: Any) -> NoReturn:
        """Used to disable this method"""
