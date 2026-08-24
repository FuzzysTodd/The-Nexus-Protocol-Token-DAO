from _typeshed import Incomplete
from git.compat import safe_decode as safe_decode
from git.repo.base import Repo as Repo
from git.types import PathLike as PathLike
from git.util import remove_password_if_present as remove_password_if_present
from gitdb.exc import AmbiguousObjectName as AmbiguousObjectName, BadName as BadName, BadObject as BadObject, BadObjectType as BadObjectType, InvalidDBRoot as InvalidDBRoot, ODBError as ODBError, ParseError as ParseError, UnsupportedOperation as UnsupportedOperation, to_hex_sha as to_hex_sha
from typing import List, Sequence, Tuple

class GitError(Exception):
    """Base class for all package exceptions"""
class InvalidGitRepositoryError(GitError):
    """Thrown if the given repository appears to have an invalid format."""
class WorkTreeRepositoryUnsupported(InvalidGitRepositoryError):
    """Thrown to indicate we can't handle work tree repositories"""
class NoSuchPathError(GitError, OSError):
    """Thrown if a path could not be access by the system."""
class UnsafeProtocolError(GitError):
    """Thrown if unsafe protocols are passed without being explicitly allowed."""
class UnsafeOptionError(GitError):
    """Thrown if unsafe options are passed without being explicitly allowed."""

class CommandError(GitError):
    """Base class for exceptions thrown at every stage of `Popen()` execution.

    :param command:
        A non-empty list of argv comprising the command-line.
    """
    command: Incomplete
    status: Incomplete
    stdout: Incomplete
    stderr: Incomplete
    def __init__(self, command: List[str] | Tuple[str, ...] | str, status: str | int | None | Exception = None, stderr: bytes | str | None = None, stdout: bytes | str | None = None) -> None: ...

class GitCommandNotFound(CommandError):
    """Thrown if we cannot find the `git` executable in the PATH or at the path given by
    the GIT_PYTHON_GIT_EXECUTABLE environment variable"""
    def __init__(self, command: List[str] | Tuple[str] | str, cause: str | Exception) -> None: ...

class GitCommandError(CommandError):
    """Thrown if execution of the git command fails with non-zero status code."""
    def __init__(self, command: List[str] | Tuple[str, ...] | str, status: str | int | None | Exception = None, stderr: bytes | str | None = None, stdout: bytes | str | None = None) -> None: ...

class CheckoutError(GitError):
    """Thrown if a file could not be checked out from the index as it contained
    changes.

    The .failed_files attribute contains a list of relative paths that failed
    to be checked out as they contained changes that did not exist in the index.

    The .failed_reasons attribute contains a string informing about the actual
    cause of the issue.

    The .valid_files attribute contains a list of relative paths to files that
    were checked out successfully and hence match the version stored in the
    index"""
    failed_files: Incomplete
    failed_reasons: Incomplete
    valid_files: Incomplete
    def __init__(self, message: str, failed_files: Sequence[PathLike], valid_files: Sequence[PathLike], failed_reasons: List[str]) -> None: ...

class CacheError(GitError):
    """Base for all errors related to the git index, which is called cache internally"""
class UnmergedEntriesError(CacheError):
    """Thrown if an operation cannot proceed as there are still unmerged
    entries in the cache"""

class HookExecutionError(CommandError):
    """Thrown if a hook exits with a non-zero exit code. It provides access to the exit code and the string returned
    via standard output"""
    def __init__(self, command: List[str] | Tuple[str, ...] | str, status: str | int | None | Exception, stderr: bytes | str | None = None, stdout: bytes | str | None = None) -> None: ...

class RepositoryDirtyError(GitError):
    """Thrown whenever an operation on a repository fails as it has uncommitted changes that would be overwritten"""
    repo: Incomplete
    message: Incomplete
    def __init__(self, repo: Repo, message: str) -> None: ...
