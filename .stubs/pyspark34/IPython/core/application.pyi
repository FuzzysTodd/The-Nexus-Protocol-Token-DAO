from IPython.core import crashhandler as crashhandler, release as release
from IPython.core.profiledir import ProfileDir as ProfileDir, ProfileDirError as ProfileDirError
from IPython.paths import get_ipython_dir as get_ipython_dir, get_ipython_package_dir as get_ipython_package_dir
from IPython.utils.path import ensure_dir_exists as ensure_dir_exists
from _typeshed import Incomplete
from traitlets.config.application import Application
from traitlets.config.loader import PyFileConfigLoader

programdata: Incomplete
SYSTEM_CONFIG_DIRS: Incomplete
ENV_CONFIG_DIRS: Incomplete
IPYTHON_SUPPRESS_CONFIG_ERRORS: Incomplete
base_aliases: Incomplete
base_flags: Incomplete

class ProfileAwareConfigLoader(PyFileConfigLoader):
    """A Python file config loader that is aware of IPython profiles."""
    def load_subconfig(self, fname, path: Incomplete | None = None, profile: Incomplete | None = None): ...

class BaseIPythonApplication(Application):
    name: str
    description: str
    version: Incomplete
    aliases = base_aliases
    flags = base_flags
    classes: Incomplete
    python_config_loader_class = ProfileAwareConfigLoader
    config_file_specified: Incomplete
    config_file_name: Incomplete
    builtin_profile_dir: Incomplete
    config_file_paths: Incomplete
    extra_config_file: Incomplete
    profile: Incomplete
    add_ipython_dir_to_sys_path: Incomplete
    ipython_dir: Incomplete
    profile_dir: Incomplete
    overwrite: Incomplete
    auto_create: Incomplete
    config_files: Incomplete
    copy_config_files: Incomplete
    verbose_crash: Incomplete
    crash_handler_class: Incomplete
    def __init__(self, **kwargs) -> None: ...
    crash_handler: Incomplete
    def init_crash_handler(self) -> None:
        """Create a crash handler, typically setting sys.excepthook to it."""
    def excepthook(self, etype, evalue, tb):
        """this is sys.excepthook after init_crashhandler

        set self.verbose_crash=True to use our full crashhandler, instead of
        a regular traceback with a short message (crash_handler_lite)
        """
    def load_config_file(self, suppress_errors=...) -> None:
        """Load the config file.

        By default, errors in loading config are handled, and a warning
        printed on screen. For testing, the suppress_errors option is set
        to False, so errors will make tests fail.

        `suppress_errors` default value is to be `None` in which case the
        behavior default to the one of `traitlets.Application`.

        The default value can be set :
           - to `False` by setting 'IPYTHON_SUPPRESS_CONFIG_ERRORS' environment variable to '0', or 'false' (case insensitive).
           - to `True` by setting 'IPYTHON_SUPPRESS_CONFIG_ERRORS' environment variable to '1' or 'true' (case insensitive).
           - to `None` by setting 'IPYTHON_SUPPRESS_CONFIG_ERRORS' environment variable to '' (empty string) or leaving it unset.

        Any other value are invalid, and will make IPython exit with a non-zero return code.
        """
    def init_profile_dir(self) -> None:
        """initialize the profile dir"""
    def init_config_files(self) -> None:
        """[optionally] copy default config files into profile dir."""
    def stage_default_config_file(self) -> None:
        """auto generate default config file, and stage it into the profile."""
    def initialize(self, argv: Incomplete | None = None) -> None: ...
