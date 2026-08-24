import argparse
from . import command as command
from _typeshed import Incomplete

class HelpExit(SystemExit):
    """Special exception type to trigger quick exit from the application

    We subclass from SystemExit to preserve API compatibility for
    anything that used to catch SystemExit, but use a different class
    so that cliff's Application can tell the difference between
    something trying to hard-exit and help saying it's done.
    """

class HelpAction(argparse.Action):
    '''Provide a custom action so the -h and --help options
    to the main app will print a list of the commands.

    The commands are determined by checking the CommandManager
    instance, passed in as the "default" value for the action.
    '''
    def __call__(self, parser, namespace, values, option_string: Incomplete | None = None): ...

class HelpCommand(command.Command):
    """print detailed help for another command
    """
    def get_parser(self, prog_name): ...
    def take_action(self, parsed_args): ...
