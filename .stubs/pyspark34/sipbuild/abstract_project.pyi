import abc
from .exceptions import UserException as UserException
from .pyproject import PyProject as PyProject, PyProjectOptionException as PyProjectOptionException
from _typeshed import Incomplete
from abc import ABC, abstractmethod

class AbstractProject(ABC, metaclass=abc.ABCMeta):
    """ This specifies the API of a project. """
    @classmethod
    def bootstrap(cls, tool, tool_description: str = '', arguments: Incomplete | None = None):
        """ Return an AbstractProject instance fully configured for a
        particular command line tool.
        """
    @abstractmethod
    def build(self):
        """ Build the project in-situ. """
    @abstractmethod
    def build_sdist(self, sdist_directory):
        """ Build an sdist for the project and return the name of the sdist
        file.
        """
    @abstractmethod
    def build_wheel(self, wheel_directory):
        """ Build a wheel for the project and return the name of the wheel
        file.
        """
    @staticmethod
    def import_callable(name, base_type):
        """ Import a callable from either a .py file or specified as
        module[:object].
        """
    @abstractmethod
    def install(self):
        """ Install the project. """
    @abstractmethod
    def setup(self, pyproject, tool, tool_description):
        """ Complete the configuration of the project. """
