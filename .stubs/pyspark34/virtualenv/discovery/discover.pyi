from abc import ABCMeta, abstractmethod

__all__ = ['Discover']

class Discover(metaclass=ABCMeta):
    """Discover and provide the requested Python interpreter."""
    @classmethod
    def add_parser_arguments(cls, parser) -> None:
        """
        Add CLI arguments for this discovery mechanisms.

        :param parser: the CLI parser
        """
    def __init__(self, options) -> None:
        """
        Create a new discovery mechanism.

        :param options: the parsed options as defined within :meth:`add_parser_arguments`
        """
    @abstractmethod
    def run(self):
        """
        Discovers an interpreter.

        :return: the interpreter ready to use for virtual environment creation
        """
    @property
    def interpreter(self):
        """:return: the interpreter as returned by :meth:`run`, cached"""
