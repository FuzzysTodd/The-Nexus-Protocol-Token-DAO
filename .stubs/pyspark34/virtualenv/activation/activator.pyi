from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod

__all__ = ['Activator']

class Activator(metaclass=ABCMeta):
    """Generates activate script for the virtual environment."""
    flag_prompt: Incomplete
    def __init__(self, options) -> None:
        """
        Create a new activator generator.

        :param options: the parsed options as defined within :meth:`add_parser_arguments`
        """
    @classmethod
    def supports(cls, interpreter):
        """
        Check if the activation script is supported in the given interpreter.

        :param interpreter: the interpreter we need to support
        :return: ``True`` if supported, ``False`` otherwise
        """
    @classmethod
    def add_parser_arguments(cls, parser, interpreter) -> None:
        """
        Add CLI arguments for this activation script.

        :param parser: the CLI parser
        :param interpreter: the interpreter this virtual environment is based of
        """
    @abstractmethod
    def generate(self, creator):
        """
        Generate activate script for the given creator.

        :param creator: the creator (based of :class:`virtualenv.create.creator.Creator`) we used to create this         virtual environment
        """
