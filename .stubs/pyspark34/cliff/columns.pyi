import abc

class FormattableColumn(metaclass=abc.ABCMeta):
    def __init__(self, value) -> None: ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    @abc.abstractmethod
    def human_readable(self):
        """Return a basic human readable version of the data."""
    def machine_readable(self):
        """Return a raw data structure using only Python built-in types.

        It must be possible to serialize the return value directly
        using a formatter like JSON, and it will be up to the
        formatter plugin to decide how to make that transformation.
        """
