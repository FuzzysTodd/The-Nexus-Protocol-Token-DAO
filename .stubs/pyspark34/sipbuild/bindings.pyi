from .buildable import BuildableBindings as BuildableBindings
from .code_generator import generateCode as generateCode, py2c as py2c
from .configurable import Configurable as Configurable, Option as Option
from .exceptions import UserException as UserException
from .generator import parse as parse, resolve as resolve
from .generator.outputs import output_api as output_api, output_extract as output_extract, output_pyi as output_pyi
from .installable import Installable as Installable
from .module import copy_nonshared_sources as copy_nonshared_sources
from .version import SIP_VERSION as SIP_VERSION
from _typeshed import Incomplete

class Bindings(Configurable):
    """ The encapsulation of a module's bindings. """
    project: Incomplete
    name: Incomplete
    def __init__(self, project, name, **kwargs) -> None:
        """ Initialise the bindings. """
    sip_file: Incomplete
    def apply_nonuser_defaults(self, tool) -> None:
        """ Set default values for each non-user configurable option that
        hasn't been set yet.
        """
    protected_is_public: Incomplete
    def apply_user_defaults(self, tool) -> None:
        """ Set default values for user options that haven't been set yet. """
    def generate(self):
        """ Generate the bindings source code and optional additional extracts.
        and return a BuildableBindings instance containing the details of
        everything needed to build the bindings.
        """
    def get_options(self):
        """ Return the list of configurable options. """
    def is_buildable(self):
        """ Return True if the bindings are buildable.  This will not be called
        if the bindings have been explicitly enabled.
        """
    extra_objects: Incomplete
    headers: Incomplete
    include_dirs: Incomplete
    library_dirs: Incomplete
    sources: Incomplete
    source_suffix: Incomplete
    def verify_configuration(self, tool) -> None:
        """ Verify that the configuration is complete and consistent. """
