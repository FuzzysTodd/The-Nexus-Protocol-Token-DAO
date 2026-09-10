import abc
from .configurable import Configurable as Configurable
from _typeshed import Incomplete
from abc import ABC, abstractmethod

class AbstractBuilder(Configurable, ABC, metaclass=abc.ABCMeta):
    """ This specifies the API of a builder. """
    project: Incomplete
    def __init__(self, project, **kwargs) -> None:
        """ Initialise the builder. """
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
    @abstractmethod
    def install(self):
        """ Install the project. """
