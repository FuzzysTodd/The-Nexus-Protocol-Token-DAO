from _typeshed import Incomplete

__all__ = ['get_path_uid', 'stdlib_pkgs', 'WINDOWS']

def get_path_uid(path: str) -> int:
    """
    Return path's uid.

    Does not follow symlinks:
        https://github.com/pypa/pip/pull/935#discussion_r5307003

    Placed this function in compat due to differences on AIX and
    Jython, that should eventually go away.

    :raises OSError: When path is a symlink or can't be read.
    """

stdlib_pkgs: Incomplete
WINDOWS: Incomplete
