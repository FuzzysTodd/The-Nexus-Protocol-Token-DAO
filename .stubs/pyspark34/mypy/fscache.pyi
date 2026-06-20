import os
from _typeshed import Incomplete
from mypy.util import hash_digest as hash_digest

class FileSystemCache:
    package_root: Incomplete
    def __init__(self) -> None: ...
    def set_package_root(self, package_root: list[str]) -> None: ...
    stat_cache: Incomplete
    stat_error_cache: Incomplete
    listdir_cache: Incomplete
    listdir_error_cache: Incomplete
    isfile_case_cache: Incomplete
    exists_case_cache: Incomplete
    read_cache: Incomplete
    read_error_cache: Incomplete
    hash_cache: Incomplete
    fake_package_cache: Incomplete
    def flush(self) -> None:
        """Start another transaction and empty all caches."""
    def stat(self, path: str) -> os.stat_result: ...
    def init_under_package_root(self, path: str) -> bool:
        """Is this path an __init__.py under a package root?

        This is used to detect packages that don't contain __init__.py
        files, which is needed to support Bazel.  The function should
        only be called for non-existing files.

        It will return True if it refers to a __init__.py file that
        Bazel would create, so that at runtime Python would think the
        directory containing it is a package.  For this to work you
        must pass one or more package roots using the --package-root
        flag.

        As an exceptional case, any directory that is a package root
        itself will not be considered to contain a __init__.py file.
        This is different from the rules Bazel itself applies, but is
        necessary for mypy to properly distinguish packages from other
        directories.

        See https://docs.bazel.build/versions/master/be/python.html,
        where this behavior is described under legacy_create_init.
        """
    def listdir(self, path: str) -> list[str]: ...
    def isfile(self, path: str) -> bool: ...
    def isfile_case(self, path: str, prefix: str) -> bool:
        """Return whether path exists and is a file.

        On case-insensitive filesystems (like Mac or Windows) this returns
        False if the case of path's last component does not exactly match
        the case found in the filesystem.

        We check also the case of other path components up to prefix.
        For example, if path is 'user-stubs/pack/mod.pyi' and prefix is 'user-stubs',
        we check that the case of 'pack' and 'mod.py' matches exactly, 'user-stubs' will be
        case insensitive on case insensitive filesystems.

        The caller must ensure that prefix is a valid file system prefix of path.
        """
    def exists_case(self, path: str, prefix: str) -> bool:
        """Return whether path exists - checking path components in case sensitive
        fashion, up to prefix.
        """
    def isdir(self, path: str) -> bool: ...
    def exists(self, path: str) -> bool: ...
    def read(self, path: str) -> bytes: ...
    def hash_digest(self, path: str) -> str: ...
    def samefile(self, f1: str, f2: str) -> bool: ...

def copy_os_error(e: OSError) -> OSError: ...
