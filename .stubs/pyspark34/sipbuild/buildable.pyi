from .exceptions import UserException as UserException
from .installable import Installable as Installable
from .py_versions import OLDEST_SUPPORTED_MINOR as OLDEST_SUPPORTED_MINOR
from .version import SIP_VERSION_STR as SIP_VERSION_STR
from _typeshed import Incomplete

class Buildable:
    """ Encapsulate the components used to build something that can be
    installed.
    """
    project: Incomplete
    name: Incomplete
    builder_settings: Incomplete
    installables: Incomplete
    build_dir: Incomplete
    def __init__(self, project, name) -> None:
        """ Initialise the buildable. """

class BuildableFromSources(Buildable):
    """ Encapsulate the sources used to build an extension module, executable
    etc.
    """
    target: Incomplete
    uses_limited_api: Incomplete
    define_macros: Incomplete
    sources: Incomplete
    headers: Incomplete
    include_dirs: Incomplete
    libraries: Incomplete
    library_dirs: Incomplete
    extra_compile_args: Incomplete
    extra_link_args: Incomplete
    extra_objects: Incomplete
    debug: bool
    def __init__(self, project, name, target, *, uses_limited_api: bool = False) -> None:
        """ Initialise the buildable. """
    def make_names_relative(self) -> None:
        """ Make all file and directory names relative to the build directory.
        """

class BuildableExecutable(BuildableFromSources):
    """ Encapsulate the sources used to build an executable. """

class BuildableModule(BuildableFromSources):
    """ Encapsulate the sources used to build an extension module. """
    fq_name: Incomplete
    exceptions: bool
    static: bool
    def __init__(self, project, name, fq_name, *, uses_limited_api: bool = False) -> None:
        """ Initialise the sources. """
    def get_install_subdir(self):
        """ Return the sub-directory the extension module should be installed
        in relative to the eventual target directory.
        """
    def get_module_extension(self):
        """ Return the filename extension that a module should have. """

class BuildableBindings(BuildableModule):
    """ Encapsulate the sources used to build the extension module for a set of
    bindings.
    """
    bindings: Incomplete
    def __init__(self, bindings, fq_name, *, uses_limited_api: bool = False) -> None:
        """ Initialise the sources. """
    def get_bindings_installable(self, name):
        """ Return an installable for the buildable's bindings directory. """
    def write_configuration(self, bindings_dir) -> None:
        """ Write the configuration of the bindings and add it as an
        installable.
        """
