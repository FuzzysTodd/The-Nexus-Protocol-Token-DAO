from ..core import Command as Command
from ..debug import DEBUG as DEBUG
from ..errors import DistutilsOptionError as DistutilsOptionError, DistutilsPlatformError as DistutilsPlatformError
from ..file_util import write_file as write_file
from ..sysconfig import get_config_vars as get_config_vars
from ..util import change_root as change_root, convert_path as convert_path, get_platform as get_platform, subst_vars as subst_vars
from _typeshed import Incomplete

HAS_USER_SITE: bool
WINDOWS_SCHEME: Incomplete
INSTALL_SCHEMES: Incomplete
SCHEME_KEYS: Incomplete

class install(Command):
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    negative_opt: Incomplete
    prefix: Incomplete
    exec_prefix: Incomplete
    home: Incomplete
    user: int
    install_base: Incomplete
    install_platbase: Incomplete
    root: Incomplete
    install_purelib: Incomplete
    install_platlib: Incomplete
    install_headers: Incomplete
    install_lib: Incomplete
    install_scripts: Incomplete
    install_data: Incomplete
    install_userbase: Incomplete
    install_usersite: Incomplete
    compile: Incomplete
    optimize: Incomplete
    extra_path: Incomplete
    install_path_file: int
    force: int
    skip_build: int
    warn_dir: int
    build_base: Incomplete
    build_lib: Incomplete
    record: Incomplete
    def initialize_options(self) -> None:
        """Initializes options."""
    config_vars: Incomplete
    install_libbase: Incomplete
    def finalize_options(self) -> None:
        """Finalizes options."""
    def dump_dirs(self, msg) -> None:
        """Dumps the list of user options."""
    def finalize_unix(self) -> None:
        """Finalizes options for posix platforms."""
    def finalize_other(self) -> None:
        """Finalizes options for non-posix platforms"""
    def select_scheme(self, name) -> None: ...
    def expand_basedirs(self) -> None:
        """Calls `os.path.expanduser` on install_base, install_platbase and
        root."""
    def expand_dirs(self) -> None:
        """Calls `os.path.expanduser` on install dirs."""
    def convert_paths(self, *names) -> None:
        """Call `convert_path` over `names`."""
    path_file: Incomplete
    extra_dirs: Incomplete
    def handle_extra_path(self) -> None:
        """Set `path_file` and `extra_dirs` using `extra_path`."""
    def change_roots(self, *names) -> None:
        """Change the install directories pointed by name using root."""
    def create_home_path(self) -> None:
        """Create directories under ~."""
    def run(self) -> None:
        """Runs the command."""
    def create_path_file(self) -> None:
        """Creates the .pth file"""
    def get_outputs(self):
        """Assembles the outputs of all the sub-commands."""
    def get_inputs(self):
        """Returns the inputs of all the sub-commands"""
    def has_lib(self):
        """Returns true if the current distribution has any Python
        modules to install."""
    def has_headers(self):
        """Returns true if the current distribution has any headers to
        install."""
    def has_scripts(self):
        """Returns true if the current distribution has any scripts to.
        install."""
    def has_data(self):
        """Returns true if the current distribution has any data to.
        install."""
    sub_commands: Incomplete
