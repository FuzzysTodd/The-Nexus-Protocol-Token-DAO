from .utils import deprecation as deprecation
from _typeshed import Incomplete
from typing import Any, Iterator, List

pjoin: Incomplete
APPNAME: Incomplete
UF_HIDDEN: Incomplete

def envset(name: str, default: bool | None = False) -> bool | None:
    """Return the boolean value of a given environment variable.

    An environment variable is considered set if it is assigned to a value
    other than 'no', 'n', 'false', 'off', '0', or '0.0' (case insensitive)

    If the environment variable is not defined, the default value is returned.
    """
def use_platform_dirs() -> bool:
    """Determine if platformdirs should be used for system-specific paths.

    We plan for this to default to False in jupyter_core version 5 and to True
    in jupyter_core version 6.
    """
def get_home_dir() -> str:
    """Get the real path of the home directory"""
def prefer_environment_over_user() -> bool:
    """Determine if environment-level paths should take precedence over user-level paths."""
def jupyter_config_dir() -> str:
    """Get the Jupyter config directory for this platform and user.

    Returns JUPYTER_CONFIG_DIR if defined, otherwise the appropriate
    directory for the platform.
    """
def jupyter_data_dir() -> str:
    """Get the config directory for Jupyter data files for this platform and user.

    These are non-transient, non-configuration files.

    Returns JUPYTER_DATA_DIR if defined, else a platform-appropriate path.
    """
def jupyter_runtime_dir() -> str:
    """Return the runtime dir for transient jupyter files.

    Returns JUPYTER_RUNTIME_DIR if defined.

    The default is now (data_dir)/runtime on all platforms;
    we no longer use XDG_RUNTIME_DIR after various problems.
    """

SYSTEM_JUPYTER_PATH: Incomplete
programdata: Incomplete
ENV_JUPYTER_PATH: List[str]

def jupyter_path(*subdirs: str) -> List[str]:
    """Return a list of directories to search for data files

    JUPYTER_PATH environment variable has highest priority.

    If the JUPYTER_PREFER_ENV_PATH environment variable is set, the environment-level
    directories will have priority over user-level directories.

    If the Python site.ENABLE_USER_SITE variable is True, we also add the
    appropriate Python user site subdirectory to the user-level directories.


    If ``*subdirs`` are given, that subdirectory will be added to each element.

    Examples:

    >>> jupyter_path()
    ['~/.local/jupyter', '/usr/local/share/jupyter']
    >>> jupyter_path('kernels')
    ['~/.local/jupyter/kernels', '/usr/local/share/jupyter/kernels']
    """

SYSTEM_CONFIG_PATH: Incomplete
ENV_CONFIG_PATH: List[str]

def jupyter_config_path() -> List[str]:
    """Return the search path for Jupyter config files as a list.

    If the JUPYTER_PREFER_ENV_PATH environment variable is set, the
    environment-level directories will have priority over user-level
    directories.

    If the Python site.ENABLE_USER_SITE variable is True, we also add the
    appropriate Python user site subdirectory to the user-level directories.
    """
def exists(path: str) -> bool:
    """Replacement for `os.path.exists` which works for host mapped volumes
    on Windows containers
    """
def is_file_hidden_win(abs_path: str, stat_res: Any | None = None) -> bool:
    """Is a file hidden?

    This only checks the file itself; it should be called in combination with
    checking the directory containing the file.

    Use is_hidden() instead to check the file and its parent directories.

    Parameters
    ----------
    abs_path : unicode
        The absolute path to check.
    stat_res : os.stat_result, optional
        The result of calling stat() on abs_path. If not passed, this function
        will call stat() internally.
    """
def is_file_hidden_posix(abs_path: str, stat_res: Any | None = None) -> bool:
    """Is a file hidden?

    This only checks the file itself; it should be called in combination with
    checking the directory containing the file.

    Use is_hidden() instead to check the file and its parent directories.

    Parameters
    ----------
    abs_path : unicode
        The absolute path to check.
    stat_res : os.stat_result, optional
        The result of calling stat() on abs_path. If not passed, this function
        will call stat() internally.
    """
is_file_hidden = is_file_hidden_posix

def is_hidden(abs_path: str, abs_root: str = '') -> bool:
    """Is a file hidden or contained in a hidden directory?

    This will start with the rightmost path element and work backwards to the
    given root to see if a path is hidden or in a hidden directory. Hidden is
    determined by either name starting with '.' or the UF_HIDDEN flag as
    reported by stat.

    If abs_path is the same directory as abs_root, it will be visible even if
    that is a hidden folder. This only checks the visibility of files
    and directories *within* abs_root.

    Parameters
    ----------
    abs_path : unicode
        The absolute path to check for hidden directories.
    abs_root : unicode
        The absolute path of the root directory in which hidden directories
        should be checked for.
    """
def win32_restrict_file_to_user(fname: str) -> None:
    """Secure a windows file to read-only access for the user.
    Follows guidance from win32 library creator:
    http://timgolden.me.uk/python/win32_how_do_i/add-security-to-a-file.html

    This method should be executed against an already generated file which
    has no secrets written to it yet.

    Parameters
    ----------

    fname : unicode
        The path to the file to secure
    """
def get_file_mode(fname: str) -> int:
    """Retrieves the file mode corresponding to fname in a filesystem-tolerant manner.

    Parameters
    ----------

    fname : unicode
        The path to the file to get mode from

    """

allow_insecure_writes: Incomplete

def secure_write(fname: str, binary: bool = False) -> Iterator[Any]:
    """Opens a file in the most restricted pattern available for
    writing content. This limits the file mode to `0o0600` and yields
    the resulting opened filed handle.

    Parameters
    ----------

    fname : unicode
        The path to the file to write

    binary: boolean
        Indicates that the file is binary
    """
def issue_insecure_write_warning() -> None:
    """Issue an insecure write warning."""
