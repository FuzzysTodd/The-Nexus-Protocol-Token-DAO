from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod

__all__ = ['Seeder']

class Seeder(metaclass=ABCMeta):
    """A seeder will install some seed packages into a virtual environment."""
    enabled: Incomplete
    env: Incomplete
    def __init__(self, options, enabled) -> None:
        """
        Create.

        :param options: the parsed options as defined within :meth:`add_parser_arguments`
        :param enabled: a flag weather the seeder is enabled or not
        """
    @classmethod
    def add_parser_arguments(cls, parser, interpreter, app_data) -> None:
        """
        Add CLI arguments for this seed mechanisms.

        :param parser: the CLI parser
        :param app_data: the CLI parser
        :param interpreter: the interpreter this virtual environment is based of
        """
    @abstractmethod
    def run(self, creator):
        """
        Perform the seed operation.

        :param creator: the creator (based of :class:`virtualenv.create.creator.Creator`) we used to create this         virtual environment
        """
