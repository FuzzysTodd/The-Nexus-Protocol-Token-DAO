from .abstract_builder import AbstractBuilder as AbstractBuilder
from .abstract_project import AbstractProject as AbstractProject
from .bindings import Bindings as Bindings
from .configurable import Configurable as Configurable, Option as Option
from .exceptions import UserException as UserException
from .module import resolve_abi_version as resolve_abi_version
from .py_versions import OLDEST_SUPPORTED_MINOR as OLDEST_SUPPORTED_MINOR
from .pyproject import PyProjectException as PyProjectException, PyProjectOptionException as PyProjectOptionException
from _typeshed import Incomplete
from collections.abc import Generator

class Project(AbstractProject, Configurable):
    """ Encapsulate a project containing one or more sets of bindings. """
    root_dir: Incomplete
    arguments: Incomplete
    bindings: Incomplete
    bindings_factories: Incomplete
    builder: Incomplete
    buildables: Incomplete
    installables: Incomplete
    def __init__(self, **kwargs) -> None:
        """ Initialise the project. """
    bindings_factory: Incomplete
    py_major_version: Incomplete
    py_minor_version: Incomplete
    builder_factory: Incomplete
    py_platform: Incomplete
    py_debug: Incomplete
    def apply_nonuser_defaults(self, tool) -> None:
        """ Set default values for non-user options that haven't been set yet.
        """
    name: Incomplete
    build_dir: str
    def apply_user_defaults(self, tool) -> None:
        """ Set default values for user options that haven't been set yet. """
    def build(self) -> None:
        """ Build the project in-situ. """
    def build_sdist(self, sdist_directory):
        """ Build an sdist for the project and return the name of the sdist
        file.
        """
    def build_wheel(self, wheel_directory):
        """ Build a wheel for the project and return the name of the wheel
        file.
        """
    def get_bindings_dir(self):
        """ Return the name of the 'bindings' directory relative to the
        eventual target directory.
        """
    def get_distinfo_dir(self, target_dir):
        """ Return the name of the .dist-info directory for a target directory.
        """
    def get_dunder_init(self):
        """ Return the contents of the __init__.py to install. """
    def get_metadata_overrides(self):
        """ Return a mapping of PEP 566 metadata names and values that will
        override any corresponding values defined in the pyproject.toml file.
        A typical use is to determine a project's version dynamically.
        """
    def get_options(self):
        """ Return the list of configurable options. """
    def get_package_dir(self):
        """ Return the name of the package directory relative to the eventual
        target directory.  This is the directory containing the shared sip
        module (if there is one) or the target directory (if not).  It will
        normally be where the individual bindings are installed.
        """
    def get_platform_tag(self):
        """ Return the platform tag to use in a wheel name.  This default
        implementation uses the platform name and applies PEP defined
        conventions depending on OS version and GLIBC version as appropriate.
        """
    def get_requires_dists(self):
        """ Return any 'Requires-Dist' to add to the project's meta-data. """
    def get_sip_distinfo_command_line(self, sip_distinfo, inventory, generator: Incomplete | None = None, wheel_tag: Incomplete | None = None, generator_version: Incomplete | None = None):
        """ Return a sequence of command line arguments to invoke sip-distinfo.
        """
    def install(self) -> None:
        """ Install the project. """
    @property
    def minimum_glibc_version(self):
        """ The getter for the minimum GLIBC version. """
    @minimum_glibc_version.setter
    def minimum_glibc_version(self, value) -> None:
        """ The setter for the minimum GLIBC version. """
    @property
    def minimum_macos_version(self):
        """ The getter for the minimum macOS version. """
    @minimum_macos_version.setter
    def minimum_macos_version(self, value) -> None:
        """ The setter for the minimum macOS version. """
    @staticmethod
    def open_for_writing(fname):
        """ Open a file for writing while handling any errors. """
    def progress(self, message) -> None:
        """ Print a progress message unless they are disabled. """
    def project_path(self, path, relative_to: Incomplete | None = None):
        """ Return a normalised version of a path.  A relative path is assumed
        to be relate to the project directory or some other provided directory.
        """
    def read_command_pipe(self, args, *, and_stderr: bool = False, fatal: bool = True) -> Generator[Incomplete, None, None]:
        """ A generator for each line of a pipe from a command's stdout. """
    def run_command(self, args, *, fatal: bool = True) -> None:
        """ Run a command and display the output if requested. """
    def setup(self, pyproject, tool, tool_description) -> None:
        """ Complete the configuration of the project. """
    def update(self, tool) -> None:
        """ This should be re-implemented by any user supplied sub-class to
        carry out any updates to the configuration as required.  The current
        directory will be the temporary build directory.
        """
    def update_buildable_bindings(self) -> None:
        """ Update the list of bindings to ensure they are either buildable or
        have been explicitly enabled.
        """
    sip_files_dir: Incomplete
    sip_include_dirs: Incomplete
    abi_version: Incomplete
    dunder_init: bool
    wheel_includes: Incomplete
    def verify_configuration(self, tool) -> None:
        """ Verify that the configuration is complete and consistent. """
