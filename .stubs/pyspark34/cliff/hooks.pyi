import abc
from _typeshed import Incomplete

class CommandHook(metaclass=abc.ABCMeta):
    """Base class for command hooks.

    :param app: Command instance being invoked
    :paramtype app: cliff.command.Command

    """
    cmd: Incomplete
    def __init__(self, command) -> None: ...
    @abc.abstractmethod
    def get_parser(self, parser):
        """Return an :class:`argparse.ArgumentParser`.

        :param parser: An existing ArgumentParser instance to be modified.
        :paramtype parser: ArgumentParser
        :returns: ArgumentParser
        """
    @abc.abstractmethod
    def get_epilog(self):
        """Return text to add to the command help epilog."""
    @abc.abstractmethod
    def before(self, parsed_args):
        """Called before the command's take_action() method.

        :param parsed_args: The arguments to the command.
        :paramtype parsed_args: argparse.Namespace
        :returns: argparse.Namespace
        """
    @abc.abstractmethod
    def after(self, parsed_args, return_code):
        """Called after the command's take_action() method.

        :param parsed_args: The arguments to the command.
        :paramtype parsed_args: argparse.Namespace
        :param return_code: The value returned from take_action().
        :paramtype return_code: int
        :returns: int
        """
