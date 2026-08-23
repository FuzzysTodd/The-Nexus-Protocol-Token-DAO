from .exceptions import UserException as UserException
from .pyproject import PyProjectOptionException as PyProjectOptionException
from _typeshed import Incomplete

class Configurable:
    """ A base class for an object that can be configured by a pyproject.toml,
    a build script or (possibly) the user via command line options.
    """
    def add_command_line_options(self, parser, tool, all_options, options: Incomplete | None = None) -> None:
        """ Add the object's command line options to an argument parser and
        update a map of Object instances and the configurables that they should
        be applied to.
        """
    def apply_nonuser_defaults(self, tool) -> None:
        """ Set default values for each non-user configurable option that
        hasn't been set yet.
        """
    def apply_user_defaults(self, tool) -> None:
        """ Set default values for each user configurable option that hasn't
        been set yet.
        """
    def configure(self, pyproject, section_name, tool) -> None:
        """ Perform the initial configuration of an object. """
    def get_options(self):
        """ Return a list of configurable options. """
    def initialise_options(self, kwargs) -> None:
        """ Initialise the options. """
    def verify_configuration(self, tool) -> None:
        """ Verify that the configuration is complete and consistent. """

class Option:
    """ Encapsulate a configuration option.  This defines and implements an
    attribute of a Configurable object.  The value of the attribute can be set
    either by __init__(), the pyproject.toml file and by the user using a
    command line argument (in that order).  Once the value is set it cannot be
    changed subsequently.  For example, if an attribute is set
    in pyproject.toml then the user will not then be able to modify it from the
    command line.  The value can only be changed from the command line if the
    Option object has help text specified.
    """
    BUILD_TOOLS: Incomplete
    option_nr: int
    name: Incomplete
    user_name: Incomplete
    option_type: Incomplete
    default: Incomplete
    choices: Incomplete
    help: Incomplete
    metavar: Incomplete
    inverted: Incomplete
    tools: Incomplete
    dest: Incomplete
    def __init__(self, name, *, option_type=..., choices: Incomplete | None = None, default: Incomplete | None = None, help: Incomplete | None = None, metavar: Incomplete | None = None, inverted: bool = False, tools: Incomplete | None = None) -> None:
        """ Initialise the option. """
