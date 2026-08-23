import logging
from .types import Files_TD, PathLike, Protocol, SupportsIndex, Total_TD
from _typeshed import Incomplete
from abc import abstractmethod
from git.config import GitConfigParser, SectionConstraint
from git.repo.base import Repo
from typing import Any, AnyStr, BinaryIO, Callable, Dict, IO, Iterator, List, Tuple, TypeVar, overload

__all__ = ['stream_copy', 'join_path', 'to_native_path_linux', 'join_path_native', 'Stats', 'IndexFileSHA1Writer', 'IterableObj', 'IterableList', 'BlockingLockFile', 'LockFile', 'Actor', 'get_user_id', 'assure_directory_exists', 'RemoteProgress', 'CallableRemoteProgress', 'rmtree', 'unbare_repo', 'HIDE_WINDOWS_KNOWN_ERRORS', 'to_native_path_windows']

T_IterableObj = TypeVar('T_IterableObj', bound='IterableObj' | 'Has_id_attribute', covariant=True)
HIDE_WINDOWS_KNOWN_ERRORS: Incomplete
T = TypeVar('T')

def unbare_repo(func: Callable[..., T]) -> Callable[..., T]:
    """Methods with this decorator raise :class:`.exc.InvalidGitRepositoryError` if they
    encounter a bare repository"""
def rmtree(path: PathLike) -> None:
    """Remove the given directory tree recursively.

    :note: We use :func:`shutil.rmtree` but adjust its behaviour to see whether files that
        couldn't be deleted are read-only. Windows will not remove them in that case."""
def stream_copy(source: BinaryIO, destination: BinaryIO, chunk_size: int = ...) -> int:
    """Copy all data from the source stream into the destination stream in chunks
    of size chunk_size

    :return: amount of bytes written"""
def join_path(a: PathLike, *p: PathLike) -> PathLike:
    """Join path tokens together similar to osp.join, but always use
    '/' instead of possibly '' on windows."""
def to_native_path_windows(path: PathLike) -> PathLike: ...
def to_native_path_linux(path: PathLike) -> str: ...
to_native_path = to_native_path_windows
to_native_path = to_native_path_linux

def join_path_native(a: PathLike, *p: PathLike) -> PathLike:
    """
    As join path, but makes sure an OS native path is returned. This is only
        needed to play it safe on my dear windows and to assure nice paths that only
        use ''"""
def assure_directory_exists(path: PathLike, is_file: bool = False) -> bool:
    """Assure that the directory pointed to by path exists.

    :param is_file: If True, path is assumed to be a file and handled correctly.
        Otherwise it must be a directory
    :return: True if the directory was created, False if it already existed"""
def get_user_id() -> str:
    """:return: string identifying the currently active system user as name@node"""

class RemoteProgress:
    """
    Handler providing an interface to parse progress information emitted by git-push
    and git-fetch and to dispatch callbacks allowing subclasses to react to the progress.
    """
    BEGIN: Incomplete
    END: Incomplete
    COUNTING: Incomplete
    COMPRESSING: Incomplete
    WRITING: Incomplete
    RECEIVING: Incomplete
    RESOLVING: Incomplete
    FINDING_SOURCES: Incomplete
    CHECKING_OUT: Incomplete
    STAGE_MASK: Incomplete
    OP_MASK: Incomplete
    DONE_TOKEN: str
    TOKEN_SEPARATOR: str
    re_op_absolute: Incomplete
    re_op_relative: Incomplete
    error_lines: Incomplete
    other_lines: Incomplete
    def __init__(self) -> None: ...
    def new_message_handler(self) -> Callable[[str], None]:
        """
        :return:
            a progress handler suitable for handle_process_output(), passing lines on to this Progress
            handler in a suitable format"""
    def line_dropped(self, line: str) -> None:
        """Called whenever a line could not be understood and was therefore dropped."""
    def update(self, op_code: int, cur_count: str | float, max_count: str | float | None = None, message: str = '') -> None:
        """Called whenever the progress changes

        :param op_code:
            Integer allowing to be compared against Operation IDs and stage IDs.

            Stage IDs are BEGIN and END. BEGIN will only be set once for each Operation
            ID as well as END. It may be that BEGIN and END are set at once in case only
            one progress message was emitted due to the speed of the operation.
            Between BEGIN and END, none of these flags will be set

            Operation IDs are all held within the OP_MASK. Only one Operation ID will
            be active per call.
        :param cur_count: Current absolute count of items

        :param max_count:
            The maximum count of items we expect. It may be None in case there is
            no maximum number of items or if it is (yet) unknown.

        :param message:
            In case of the 'WRITING' operation, it contains the amount of bytes
            transferred. It may possibly be used for other purposes as well.

        You may read the contents of the current line in self._cur_line"""

class CallableRemoteProgress(RemoteProgress):
    """An implementation forwarding updates to any callable"""
    def __init__(self, fn: Callable) -> None: ...
    def update(self, *args: Any, **kwargs: Any) -> None: ...

class Actor:
    """Actors hold information about a person acting on the repository. They
    can be committers and authors or anything with a name and an email as
    mentioned in the git log entries."""
    name_only_regex: Incomplete
    name_email_regex: Incomplete
    env_author_name: str
    env_author_email: str
    env_committer_name: str
    env_committer_email: str
    conf_name: str
    conf_email: str
    name: Incomplete
    email: Incomplete
    def __init__(self, name: str | None, email: str | None) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    @classmethod
    def committer(cls, config_reader: None | GitConfigParser | SectionConstraint = None) -> Actor:
        """
        :return: Actor instance corresponding to the configured committer. It behaves
            similar to the git implementation, such that the environment will override
            configuration values of config_reader. If no value is set at all, it will be
            generated
        :param config_reader: ConfigReader to use to retrieve the values from in case
            they are not set in the environment"""
    @classmethod
    def author(cls, config_reader: None | GitConfigParser | SectionConstraint = None) -> Actor:
        """Same as committer(), but defines the main author. It may be specified in the environment,
        but defaults to the committer"""

class Stats:
    """
    Represents stat information as presented by git at the end of a merge. It is
    created from the output of a diff operation.

    ``Example``::

     c = Commit( sha1 )
     s = c.stats
     s.total         # full-stat-dict
     s.files         # dict( filepath : stat-dict )

    ``stat-dict``

    A dictionary with the following keys and values::

      deletions = number of deleted lines as int
      insertions = number of inserted lines as int
      lines = total number of lines changed as int, or deletions + insertions

    ``full-stat-dict``

    In addition to the items in the stat-dict, it features additional information::

     files = number of changed files as int"""
    total: Incomplete
    files: Incomplete
    def __init__(self, total: Total_TD, files: Dict[PathLike, Files_TD]) -> None: ...

class IndexFileSHA1Writer:
    """Wrapper around a file-like object that remembers the SHA1 of
    the data written to it. It will write a sha when the stream is closed
    or if the asked for explicitly using write_sha.

    Only useful to the indexfile

    :note: Based on the dulwich project"""
    f: Incomplete
    sha1: Incomplete
    def __init__(self, f: IO) -> None: ...
    def write(self, data: AnyStr) -> int: ...
    def write_sha(self) -> bytes: ...
    def close(self) -> bytes: ...
    def tell(self) -> int: ...

class LockFile:
    """Provides methods to obtain, check for, and release a file based lock which
    should be used to handle concurrent access to the same file.

    As we are a utility class to be derived from, we only use protected methods.

    Locks will automatically be released on destruction"""
    def __init__(self, file_path: PathLike) -> None: ...
    def __del__(self) -> None: ...

class BlockingLockFile(LockFile):
    """The lock file will block until a lock could be obtained, or fail after
    a specified timeout.

    :note: If the directory containing the lock was removed, an exception will
        be raised during the blocking period, preventing hangs as the lock
        can never be obtained."""
    def __init__(self, file_path: PathLike, check_interval_s: float = 0.3, max_block_time_s: int = ...) -> None:
        """Configure the instance

        :param check_interval_s:
            Period of time to sleep until the lock is checked the next time.
            By default, it waits a nearly unlimited time

        :param max_block_time_s: Maximum amount of seconds we may lock"""

class IterableList(List[T_IterableObj]):
    """
    List of iterable objects allowing to query an object by id or by named index::

     heads = repo.heads
     heads.master
     heads['master']
     heads[0]

    Iterable parent objects = [Commit, SubModule, Reference, FetchInfo, PushInfo]
    Iterable via inheritance = [Head, TagReference, RemoteReference]
    ]
    It requires an id_attribute name to be set which will be queried from its
    contained items to have a means for comparison.

    A prefix can be specified which is to be used in case the id returned by the
    items always contains a prefix that does not matter to the user, so it
    can be left out."""
    def __new__(cls, id_attr: str, prefix: str = '') -> IterableList[T_IterableObj]: ...
    def __init__(self, id_attr: str, prefix: str = '') -> None: ...
    def __contains__(self, attr: object) -> bool: ...
    def __getattr__(self, attr: str) -> T_IterableObj: ...
    def __getitem__(self, index: SupportsIndex | int | slice | str) -> T_IterableObj: ...
    def __delitem__(self, index: SupportsIndex | int | slice | str) -> None: ...

class IterableClassWatcher(type):
    """Metaclass that watches"""
    def __init__(cls, name: str, bases: Tuple, clsdict: Dict) -> None: ...

class Iterable(metaclass=IterableClassWatcher):
    """Defines an interface for iterable items which is to assure a uniform
    way to retrieve and iterate items within the git repository"""
    @classmethod
    def list_items(cls, repo: Repo, *args: Any, **kwargs: Any) -> Any:
        """
        Deprecated, use IterableObj instead.
        Find all items of this type - subclasses can specify args and kwargs differently.
        If no args are given, subclasses are obliged to return all items if no additional
        arguments arg given.

        :note: Favor the iter_items method as it will

        :return: list(Item,...) list of item instances"""
    @classmethod
    def iter_items(cls, repo: Repo, *args: Any, **kwargs: Any) -> Any:
        """For more information about the arguments, see list_items
        :return:  iterator yielding Items"""

class IterableObj(Protocol):
    """Defines an interface for iterable items which is to assure a uniform
    way to retrieve and iterate items within the git repository

    Subclasses = [Submodule, Commit, Reference, PushInfo, FetchInfo, Remote]"""
    @classmethod
    def list_items(cls, repo: Repo, *args: Any, **kwargs: Any) -> IterableList[T_IterableObj]:
        """
        Find all items of this type - subclasses can specify args and kwargs differently.
        If no args are given, subclasses are obliged to return all items if no additional
        arguments arg given.

        :note: Favor the iter_items method as it will

        :return: list(Item,...) list of item instances"""
    @classmethod
    @abstractmethod
    def iter_items(cls, repo: Repo, *args: Any, **kwargs: Any) -> Iterator[T_IterableObj]:
        """For more information about the arguments, see list_items
        :return:  iterator yielding Items"""

class NullHandler(logging.Handler):
    def emit(self, record: object) -> None: ...
