from .log import RefLog, RefLogEntry
from _typeshed import Incomplete
from git.objects.commit import Commit
from git.refs import Head, Reference, RemoteReference, TagReference
from git.repo import Repo
from git.types import Commit_ish, PathLike
from typing import Any, Iterator, TypeVar

__all__ = ['SymbolicReference']

T_References = TypeVar('T_References', bound='SymbolicReference')

class SymbolicReference:
    """Represents a special case of a reference such that this reference is symbolic.
    It does not point to a specific commit, but to another Head, which itself
    specifies a commit.

    A typical example for a symbolic reference is HEAD."""
    repo: Incomplete
    path: Incomplete
    def __init__(self, repo: Repo, path: PathLike, check_path: bool = False) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        :return:
            In case of symbolic references, the shortest assumable name
            is the path itself."""
    @property
    def abspath(self) -> PathLike: ...
    @classmethod
    def dereference_recursive(cls, repo: Repo, ref_path: PathLike | None) -> str:
        """
        :return: hexsha stored in the reference at the given ref_path, recursively dereferencing all
            intermediate references as required
        :param repo: the repository containing the reference at ref_path"""
    def set_commit(self, commit: Commit | SymbolicReference | str, logmsg: str | None = None) -> SymbolicReference:
        """As set_object, but restricts the type of object to be a Commit

        :raise ValueError: If commit is not a Commit object or doesn't point to
            a commit
        :return: self"""
    def set_object(self, object: Commit_ish | SymbolicReference | str, logmsg: str | None = None) -> SymbolicReference:
        """Set the object we point to, possibly dereference our symbolic reference first.
        If the reference does not exist, it will be created

        :param object: a refspec, a SymbolicReference or an Object instance. SymbolicReferences
            will be dereferenced beforehand to obtain the object they point to
        :param logmsg: If not None, the message will be used in the reflog entry to be
            written. Otherwise the reflog is not altered
        :note: plain SymbolicReferences may not actually point to objects by convention
        :return: self"""
    commit: Incomplete
    object: Incomplete
    def set_reference(self, ref: Commit_ish | SymbolicReference | str, logmsg: str | None = None) -> SymbolicReference:
        """Set ourselves to the given ref. It will stay a symbol if the ref is a Reference.
        Otherwise an Object, given as Object instance or refspec, is assumed and if valid,
        will be set which effectively detaches the reference if it was a purely
        symbolic one.

        :param ref: SymbolicReference instance, Object instance or refspec string
            Only if the ref is a SymbolicRef instance, we will point to it. Everything
            else is dereferenced to obtain the actual object.
        :param logmsg: If set to a string, the message will be used in the reflog.
            Otherwise, a reflog entry is not written for the changed reference.
            The previous commit of the entry will be the commit we point to now.

            See also: log_append()

        :return: self
        :note: This symbolic reference will not be dereferenced. For that, see
            ``set_object(...)``"""
    reference: Head | TagReference | RemoteReference | Reference
    ref = reference
    def is_valid(self) -> bool:
        """
        :return:
            True if the reference is valid, hence it can be read and points to
            a valid object or reference."""
    @property
    def is_detached(self) -> bool:
        """
        :return:
            True if we are a detached reference, hence we point to a specific commit
            instead to another reference"""
    def log(self) -> RefLog:
        """
        :return: RefLog for this reference. Its last entry reflects the latest change
            applied to this reference

        .. note:: As the log is parsed every time, its recommended to cache it for use
            instead of calling this method repeatedly. It should be considered read-only."""
    def log_append(self, oldbinsha: bytes, message: str | None, newbinsha: bytes | None = None) -> RefLogEntry:
        """Append a logentry to the logfile of this ref

        :param oldbinsha: binary sha this ref used to point to
        :param message: A message describing the change
        :param newbinsha: The sha the ref points to now. If None, our current commit sha
            will be used
        :return: added RefLogEntry instance"""
    def log_entry(self, index: int) -> RefLogEntry:
        """:return: RefLogEntry at the given index
        :param index: python list compatible positive or negative index

        .. note:: This method must read part of the reflog during execution, hence
            it should be used sparringly, or only if you need just one index.
            In that case, it will be faster than the ``log()`` method"""
    @classmethod
    def to_full_path(cls, path: PathLike | SymbolicReference) -> PathLike:
        """
        :return: string with a full repository-relative path which can be used to initialize
            a Reference instance, for instance by using ``Reference.from_path``"""
    @classmethod
    def delete(cls, repo: Repo, path: PathLike) -> None:
        '''Delete the reference at the given path

        :param repo:
            Repository to delete the reference from

        :param path:
            Short or full path pointing to the reference, i.e. refs/myreference
            or just "myreference", hence \'refs/\' is implied.
            Alternatively the symbolic reference to be deleted'''
    @classmethod
    def create(cls, repo: Repo, path: PathLike, reference: SymbolicReference | str = 'HEAD', logmsg: str | None = None, force: bool = False, **kwargs: Any) -> T_References:
        '''Create a new symbolic reference, hence a reference pointing , to another reference.

        :param repo:
            Repository to create the reference in

        :param path:
            full path at which the new symbolic reference is supposed to be
            created at, i.e. "NEW_HEAD" or "symrefs/my_new_symref"

        :param reference:
            The reference to which the new symbolic reference should point to.
            If it is a commit\'ish, the symbolic ref will be detached.

        :param force:
            if True, force creation even if a symbolic reference with that name already exists.
            Raise OSError otherwise

        :param logmsg:
            If not None, the message to append to the reflog. Otherwise no reflog
            entry is written.

        :return: Newly created symbolic Reference

        :raise OSError:
            If a (Symbolic)Reference with the same name but different contents
            already exists.

        :note: This does not alter the current HEAD, index or Working Tree'''
    def rename(self, new_path: PathLike, force: bool = False) -> SymbolicReference:
        """Rename self to a new path

        :param new_path:
            Either a simple name or a full path, i.e. new_name or features/new_name.
            The prefix refs/ is implied for references and will be set as needed.
            In case this is a symbolic ref, there is no implied prefix

        :param force:
            If True, the rename will succeed even if a head with the target name
            already exists. It will be overwritten in that case

        :return: self
        :raise OSError: In case a file at path but a different contents already exists"""
    @classmethod
    def iter_items(cls, repo: Repo, common_path: PathLike | None = None, *args: Any, **kwargs: Any) -> Iterator[T_References]:
        """Find all refs in the repository

        :param repo: is the Repo

        :param common_path:
            Optional keyword argument to the path which is to be shared by all
            returned Ref objects.
            Defaults to class specific portion if None assuring that only
            refs suitable for the actual class are returned.

        :return:
            git.SymbolicReference[], each of them is guaranteed to be a symbolic
            ref which is not detached and pointing to a valid ref

            List is lexicographically sorted
            The returned objects represent actual subclasses, such as Head or TagReference"""
    @classmethod
    def from_path(cls, repo: Repo, path: PathLike) -> T_References:
        """
        :param path: full .git-directory-relative path name to the Reference to instantiate
        :note: use to_full_path() if you only have a partial path of a known Reference Type
        :return:
            Instance of type Reference, Head, or Tag
            depending on the given path"""
    def is_remote(self) -> bool:
        """:return: True if this symbolic reference points to a remote branch"""
