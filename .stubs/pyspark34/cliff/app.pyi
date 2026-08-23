from . import complete as complete, help as help, utils as utils
from _typeshed import Incomplete

class App:
    """Application base class.

    :param description: one-liner explaining the program purpose
    :paramtype description: str
    :param version: application version number
    :paramtype version: str
    :param command_manager: plugin loader
    :paramtype command_manager: cliff.commandmanager.CommandManager
    :param stdin: Standard input stream
    :paramtype stdin: readable I/O stream
    :param stdout: Standard output stream
    :paramtype stdout: writable I/O stream
    :param stderr: Standard error output stream
    :paramtype stderr: writable I/O stream
    :param interactive_app_factory: callable to create an
                                    interactive application
    :paramtype interactive_app_factory: cliff.interactive.InteractiveApp
    :param deferred_help: True - Allow subcommands to accept --help with
                          allowing to defer help print after initialize_app
    :paramtype deferred_help: bool
    """
    NAME: Incomplete
    LOG: Incomplete
    CONSOLE_MESSAGE_FORMAT: str
    LOG_FILE_MESSAGE_FORMAT: str
    DEFAULT_VERBOSE_LEVEL: int
    DEFAULT_OUTPUT_ENCODING: str
    command_manager: Incomplete
    interactive_app_factory: Incomplete
    deferred_help: Incomplete
    parser: Incomplete
    interactive_mode: bool
    interpreter: Incomplete
    def __init__(self, description, version, command_manager, stdin: Incomplete | None = None, stdout: Incomplete | None = None, stderr: Incomplete | None = None, interactive_app_factory: Incomplete | None = None, deferred_help: bool = False) -> None:
        """Initialize the application.
        """
    def build_option_parser(self, description, version, argparse_kwargs: Incomplete | None = None):
        """Return an argparse option parser for this application.

        Subclasses may override this method to extend
        the parser with more global options.

        :param description: full description of the application
        :paramtype description: str
        :param version: version number for the application
        :paramtype version: str
        :param argparse_kwargs: extra keyword argument passed to the
                                ArgumentParser constructor
        :paramtype extra_kwargs: dict
        """
    def configure_logging(self) -> None:
        """Create logging handlers for any log output.
        """
    def print_help_if_requested(self) -> None:
        """Print help and exits if deferred help is enabled and requested.

        '--help' shows the help message and exits:
         * without calling initialize_app if not self.deferred_help (default),
         * after initialize_app call if self.deferred_help,
         * during initialize_app call if self.deferred_help and subclass calls
           explicitly this method in initialize_app.
        """
    def run(self, argv):
        """Equivalent to the main program for the application.

        :param argv: input arguments and options
        :paramtype argv: list of str
        """
    def initialize_app(self, argv) -> None:
        """Hook for subclasses to take global initialization action
        after the arguments are parsed but before a command is run.
        Invoked only once, even in interactive mode.

        :param argv: List of arguments, including the subcommand to run.
                     Empty for interactive mode.
        """
    def prepare_to_run_command(self, cmd) -> None:
        """Perform any preliminary work needed to run a command.

        :param cmd: command processor being invoked
        :paramtype cmd: cliff.command.Command
        """
    def clean_up(self, cmd, result, err) -> None:
        """Hook run after a command is done to shutdown the app.

        :param cmd: command processor being invoked
        :paramtype cmd: cliff.command.Command
        :param result: return value of cmd
        :paramtype result: int
        :param err: exception or None
        :paramtype err: Exception
        """
    def interact(self): ...
    def get_fuzzy_matches(self, cmd):
        """return fuzzy matches of unknown command
        """
    def run_subcommand(self, argv): ...
