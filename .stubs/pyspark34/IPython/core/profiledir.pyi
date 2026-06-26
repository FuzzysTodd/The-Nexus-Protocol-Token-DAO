from ..paths import get_ipython_package_dir as get_ipython_package_dir
from ..utils.path import ensure_dir_exists as ensure_dir_exists, expand_path as expand_path
from _typeshed import Incomplete
from pathlib import Path
from traitlets.config.configurable import LoggingConfigurable

class ProfileDirError(Exception): ...

class ProfileDir(LoggingConfigurable):
    """An object to manage the profile directory and its resources.

    The profile directory is used by all IPython applications, to manage
    configuration, logging and security.

    This object knows how to find, create and manage these directories. This
    should be used by any code that wants to handle profiles.
    """
    security_dir_name: Incomplete
    log_dir_name: Incomplete
    startup_dir_name: Incomplete
    pid_dir_name: Incomplete
    static_dir_name: Incomplete
    security_dir: Incomplete
    log_dir: Incomplete
    startup_dir: Incomplete
    pid_dir: Incomplete
    static_dir: Incomplete
    location: Incomplete
    def check_log_dir(self, change: Incomplete | None = None) -> None: ...
    def check_startup_dir(self, change: Incomplete | None = None) -> None: ...
    def check_security_dir(self, change: Incomplete | None = None) -> None: ...
    def check_pid_dir(self, change: Incomplete | None = None) -> None: ...
    def check_dirs(self) -> None: ...
    def copy_config_file(self, config_file: str, path: Path, overwrite: bool = False) -> bool:
        """Copy a default config file into the active profile directory.

        Default configuration files are kept in :mod:`IPython.core.profile`.
        This function moves these from that location to the working profile
        directory.
        """
    @classmethod
    def create_profile_dir(cls, profile_dir, config: Incomplete | None = None):
        """Create a new profile directory given a full path.

        Parameters
        ----------
        profile_dir : str
            The full path to the profile directory.  If it does exist, it will
            be used.  If not, it will be created.
        """
    @classmethod
    def create_profile_dir_by_name(cls, path, name: str = 'default', config: Incomplete | None = None):
        '''Create a profile dir by profile name and path.

        Parameters
        ----------
        path : unicode
            The path (directory) to put the profile directory in.
        name : unicode
            The name of the profile.  The name of the profile directory will
            be "profile_<profile>".
        '''
    @classmethod
    def find_profile_dir_by_name(cls, ipython_dir, name: str = 'default', config: Incomplete | None = None):
        '''Find an existing profile dir by profile name, return its ProfileDir.

        This searches through a sequence of paths for a profile dir.  If it
        is not found, a :class:`ProfileDirError` exception will be raised.

        The search path algorithm is:
        1. ``os.getcwd()`` # removed for security reason.
        2. ``ipython_dir``

        Parameters
        ----------
        ipython_dir : unicode or str
            The IPython directory to use.
        name : unicode or str
            The name of the profile.  The name of the profile directory
            will be "profile_<profile>".
        '''
    @classmethod
    def find_profile_dir(cls, profile_dir, config: Incomplete | None = None):
        """Find/create a profile dir and return its ProfileDir.

        This will create the profile directory if it doesn't exist.

        Parameters
        ----------
        profile_dir : unicode or str
            The path of the profile directory.
        """
