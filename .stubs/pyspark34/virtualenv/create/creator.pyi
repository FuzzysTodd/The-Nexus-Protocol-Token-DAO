from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod

__all__ = ['Creator', 'CreatorMeta']

class CreatorMeta:
    error: Incomplete
    def __init__(self) -> None: ...

class Creator(metaclass=ABCMeta):
    """A class that given a python Interpreter creates a virtual environment."""
    interpreter: Incomplete
    dest: Incomplete
    clear: Incomplete
    no_vcs_ignore: Incomplete
    pyenv_cfg: Incomplete
    app_data: Incomplete
    env: Incomplete
    def __init__(self, options, interpreter) -> None:
        """
        Construct a new virtual environment creator.

        :param options: the CLI option as parsed from :meth:`add_parser_arguments`
        :param interpreter: the interpreter to create virtual environment from
        """
    @classmethod
    def can_create(cls, interpreter):
        """
        Determine if we can create a virtual environment.

        :param interpreter: the interpreter in question
        :return: ``None`` if we can't create, any other object otherwise that will be forwarded to                   :meth:`add_parser_arguments`
        """
    @classmethod
    def add_parser_arguments(cls, parser, interpreter, meta, app_data) -> None:
        """
        Add CLI arguments for the creator.

        :param parser: the CLI parser
        :param app_data: the application data folder
        :param interpreter: the interpreter we're asked to create virtual environment for
        :param meta: value as returned by :meth:`can_create`
        """
    @abstractmethod
    def create(self):
        """Perform the virtual environment creation."""
    @classmethod
    def validate_dest(cls, raw_value):
        """No path separator in the path, valid chars and must be write-able."""
    def run(self) -> None: ...
    def set_pyenv_cfg(self) -> None: ...
    def setup_ignore_vcs(self) -> None:
        """Generate ignore instructions for version control systems."""
    @property
    def debug(self):
        """:return: debug information about the virtual environment (only valid after :meth:`create` has run)"""
    @staticmethod
    def debug_script(): ...
