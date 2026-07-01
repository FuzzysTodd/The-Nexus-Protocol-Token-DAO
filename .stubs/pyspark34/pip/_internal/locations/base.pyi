from _typeshed import Incomplete
from pip._internal.exceptions import InstallationError as InstallationError
from pip._internal.utils import appdirs as appdirs
from pip._internal.utils.virtualenv import running_under_virtualenv as running_under_virtualenv

USER_CACHE_DIR: Incomplete
site_packages: str

def get_major_minor_version() -> str:
    '''
    Return the major-minor version of the current Python as a string, e.g.
    "3.7" or "3.10".
    '''
def change_root(new_root: str, pathname: str) -> str:
    """Return 'pathname' with 'new_root' prepended.

    If 'pathname' is relative, this is equivalent to os.path.join(new_root, pathname).
    Otherwise, it requires making 'pathname' relative and then joining the
    two, which is tricky on DOS/Windows and Mac OS.

    This is borrowed from Python's standard library's distutils module.
    """
def get_src_prefix() -> str: ...

user_site: str | None

def is_osx_framework() -> bool: ...
