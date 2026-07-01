from .cmd import Command as Command
from .config import PyPIRCCommand as PyPIRCCommand
from .dist import Distribution as Distribution
from .extension import Extension as Extension

__all__ = ['Distribution', 'Command', 'PyPIRCCommand', 'Extension', 'setup']

def setup(**attrs):
    """The gateway to the Distutils: do everything your setup script needs
    to do, in a highly flexible and user-driven way.  Briefly: create a
    Distribution instance; find and parse config files; parse the command
    line; run each Distutils command found there, customized by the options
    supplied to 'setup()' (as keyword arguments), in config files, and on
    the command line.

    The Distribution instance might be an instance of a class supplied via
    the 'distclass' keyword argument to 'setup'; if no such class is
    supplied, then the Distribution class (in dist.py) is instantiated.
    All other arguments to 'setup' (except for 'cmdclass') are used to set
    attributes of the Distribution instance.

    The 'cmdclass' argument, if supplied, is a dictionary mapping command
    names to command classes.  Each command encountered on the command line
    will be turned into a command class, which is in turn instantiated; any
    class found in 'cmdclass' is used in place of the default, which is
    (for command 'foo_bar') class 'foo_bar' in module
    'distutils.command.foo_bar'.  The command class must provide a
    'user_options' attribute which is a list of option specifiers for
    'distutils.fancy_getopt'.  Any command-line options between the current
    and the next command are used to set attributes of the current command
    object.

    When the entire command-line has been successfully parsed, calls the
    'run()' method on each command object in turn.  This method will be
    driven entirely by the Distribution object (which each command object
    has a reference to, thanks to its constructor), and the
    command-specific options that became attributes of each command
    object.
    """
