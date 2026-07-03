import abc
from . import command as command
from _typeshed import Incomplete

class DisplayCommandBase(command.Command, metaclass=abc.ABCMeta):
    """Command base class for displaying data about a single object.
    """
    def __init__(self, app, app_args, cmd_name: Incomplete | None = None) -> None: ...
    @property
    @abc.abstractmethod
    def formatter_namespace(self):
        """String specifying the namespace to use for loading formatter plugins."""
    @property
    @abc.abstractmethod
    def formatter_default(self):
        """String specifying the name of the default formatter."""
    def get_parser(self, prog_name): ...
    @abc.abstractmethod
    def produce_output(self, parsed_args, column_names, data):
        """Use the formatter to generate the output.

        :param parsed_args: argparse.Namespace instance with argument values
        :param column_names: sequence of strings containing names
                             of output columns
        :param data: iterable with values matching the column names
        """
    formatter: Incomplete
    def run(self, parsed_args): ...
