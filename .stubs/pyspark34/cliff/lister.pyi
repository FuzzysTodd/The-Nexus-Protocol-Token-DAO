import abc
from . import display as display
from _typeshed import Incomplete

class Lister(display.DisplayCommandBase, metaclass=abc.ABCMeta):
    """Command base class for providing a list of data as output."""
    log: Incomplete
    @property
    def formatter_namespace(self): ...
    @property
    def formatter_default(self): ...
    @property
    def need_sort_by_cliff(self):
        """Whether sort procedure is performed by cliff itself.

        Should be overridden (return False) when there is a need to implement
        custom sorting procedure or data is already sorted.
        """
    @abc.abstractmethod
    def take_action(self, parsed_args):
        """Run command.

        Return a tuple containing the column names and an iterable containing
        the data to be listed.
        """
    def get_parser(self, prog_name): ...
    def produce_output(self, parsed_args, column_names, data): ...
