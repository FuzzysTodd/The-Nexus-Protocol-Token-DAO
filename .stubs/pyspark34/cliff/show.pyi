import abc
from . import display as display

class ShowOne(display.DisplayCommandBase, metaclass=abc.ABCMeta):
    """Command base class for displaying data about a single object.
    """
    @property
    def formatter_namespace(self): ...
    @property
    def formatter_default(self): ...
    @abc.abstractmethod
    def take_action(self, parsed_args):
        """Return a two-part tuple with a tuple of column names
        and a tuple of values.
        """
    def produce_output(self, parsed_args, column_names, data): ...
    def dict2columns(self, data):
        """Implement the common task of converting a dict-based object
        to the two-column output that ShowOne expects.
        """
